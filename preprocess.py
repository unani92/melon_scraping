import pandas as pd
from konlpy.tag import Mecab
from konlpy.tag import Okt
import re

# okt
okt = Okt()
def tokenize(doc):
    # norm은 정규화, stem은 근어로 표시하기를 나타냄
    return ['/'.join(t) for t in okt.pos(doc, norm=True, stem=True)]


# 기쁨, 슬픔, 새벽감성, 사랑 네가지 데이터셋 데이터프레임으로 변환
summer_df = pd.read_json('summer.json')
print(f'joy: {summer_df.shape[0]}')
love_df = pd.read_json('love.json')
print(f'love: {love_df.shape[0]}')
midnight_df = pd.read_json('midnight.json')
print(f'midnight: {midnight_df.shape[0]}')
sad_df = pd.read_json('sad.json')
print(f'sad: {sad_df.shape[0]}')

df_all = pd.concat([summer_df, love_df, midnight_df, sad_df])

# 가사 비어있는 로우 제거, 가사에서 각종 특수문자 제거
df_havs_lyric = df_all[df_all['lyric'] != ''][['lyric', 'type']]
df_havs_lyric['lyric'] = df_havs_lyric['lyric'].apply(lambda x: re.sub('[^0-9a-zA-Zㄱ-힗]', ' ', x))

# mecab
filter_pos = ['NNG', 'NNP', 'NNB', 'NR', 'NP', 'VV', 'VA', 'VX', 'AX', 'VCP', 'VCN', 'MM', 'MAG', 'MAJ']
pos_tagger = Mecab()

def morphs(text):
    tokens = pos_tagger.pos(text)

    # 형태소 분석하여 필요한 품사의 단어만 문장으로 구성하여 반환
    return ' '.join([word for word, pos in filter(lambda x: (x[1] in filter_pos), tokens)])

df_havs_lyric['lyric'] = df_havs_lyric['lyric'].apply(morphs)
df_havs_lyric = df_havs_lyric[df_havs_lyric['lyric'] != '']

# result = re.sub('[^0-9a-zA-Zㄱ-힗]', '', myStr)
# for song in summer_data:
#     if song['lyric'] != '':
#         lyrics += song['lyric']
#
# okt = Okt()
# res = okt.pos(text, norm=True, stem=True)
# eng = [word for word, typ in res if typ == "Alpha"]
# no_josa = [word for word, typ in res if typ != "Alpha" and typ != "Josa"]
# no_josa_res = []
# stopwords = ['’', ',', '-', '_', '\r\n\t\t\t\t', '.',  "'", '(', ')']
# for word in no_josa:
#     if word not in stopwords:
#         no_josa_res.append(word)
#
# print(no_josa_res)

# naive bayes 알고리즘 사용
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB # 다항분포 나이브 베이즈 모델
from sklearn.metrics import accuracy_score #정확도 계산
from sklearn.model_selection import train_test_split

train, test = train_test_split(df_havs_lyric, test_size=0.2)
print(test.head(20))

dtmvector = CountVectorizer()
X_train_dtm = dtmvector.fit_transform(train.lyric)
tdidf_transformer = TfidfTransformer()
tdidfv = tdidf_transformer.fit_transform(X_train_dtm)
mod = MultinomialNB()
mod.fit(tdidfv, train.type)
MultinomialNB(alpha=1.0, class_prior=None, fit_prior=True)

X_test_dtm = dtmvector.transform(test.lyric) #테스트 데이터를 DTM으로 변환
tfidfv_test = tdidf_transformer.transform(X_test_dtm) #DTM을 TF-IDF 행렬로 변환

predicted = mod.predict(tfidfv_test) #테스트 데이터에 대한 예측
print("정확도:", accuracy_score(test.type, predicted)) #예측값과 실제값 비교
print(predicted)
# print(mod.predict_proba(tfidfv_test))