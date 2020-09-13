# 멜론 음원데이터 스크래핑

## 사용법

```bash
$ python parse.py
```

1. 시간 좀 오래결립니다.... 켜놓고 다른거 하시는거 추천
2. 사랑노래(`love.json`), 새벽감성(`midnight.json`), 슬픈노래(`sad.json`), 신나는노래(`summer.json`)
 이렇게 4개 카테고리로 파일이 각기 저장됩니다. 
3. 한글 인코딩 문제 때문에 파일 직접 열어보면 인코딩이 되어있지 않습니다.
```bash
$ python open.py
```
예시 데이터
    - `lyric`: 가사 부분이고 향후 웹서비스를 위해 가사 화면에 표시하기 좋게 슬래시로 끊어서 저장해둠. 전처리 당연히 짤라내고 분석 돌릴 예정
    - `type`: 학습을 위해 종속변수로서 사랑, 새벽감성, 슬픔, 즐거움 네가지 범주로 저장해둠
```python
[{'album': {'id': 10286982,
            'img': 'https://cdnimg.melon.co.kr/cm/album/images/102/86/982/10286982_500.jpg?2f04262baf6d2231dea855c32cc46ade/melon/quality/80/optimize',
            'name': 'Plate'},
  'artist': [{'id': 597191, 'name': 'CHEEZE (치즈)'}],
  'genre': ['R&B;', 'Soul, 인디음악'],
  'id': 31808249,
  'img': 'https://cdnimg.melon.co.kr/cm/album/images/102/86/982/10286982_500.jpg?2f04262baf6d2231dea855c32cc46ade/melon/quality/80/optimize',
  'like': 14273,
  'lyric': 'oh hi-hello 하나 둘 셋/은근 네 눈에 띌 준비를 해/i know everyday 너 몰래 이래/볼 때마다 넌 '
           '짓궂게 웃지만/서툴러도 뭐 어때 어느새 물들은/두 볼은 더 빨갛게/조금은 더 가깝게/Love is always '
           'better/널 닮은 색을 골라/내겐 it’s all of you/Orange-colored view/And I '
           'know it always better/둥둥 떠올라/매일 it’s all of you/몰라서 묻는 거 알아/너라서 '
           '그런가 봐 그게 너라서/you know everyday 넌 원래 그래/작은 눈빛에도 조금 예민해/나도 모르게 모든 게 '
           '너와 이어져/틈이 없어 이대로도 난 완벽한 걸/Love is always better/널 닮은 색을 골라/내겐 it’s '
           'all of you/Orange-colored view/And I know it always better/둥둥 '
           '떠올라/매일 it’s all of you/몰라서 묻는 거 알아/Love is always better/이리저리 '
           '둘러봐/내겐 it’s all of you/Orange-colored view/And I know it always '
           'better/숨이 차올라/매일 it’s all of you/Orange-colored view and you/I '
           'don’t know how it happened/but I know what to do/I don’t know how '
           'it happened/but I know what to do/I don’t know how to handle/but I '
           'know how to do/',
  'name': 'Orange',
  'released': '2019.05.19',
  'type': 'love'},
    ...
    ...
 ]
```

## 고민하는 것
1. 가사 전처리를 해야되는데 `konlpy`로 전처리하면 영어는 다 죽여야되는지...
2. 토큰화할때 조사 다 날려도 되겟지?????
3. 감정 4개로 학습하고 어떤 노래를 넣었을 때 감정 하나로 분류가 딱 안될거 같은 느낌
    - 그래서 사랑 70에 슬픔 20 즐거움 10 이런 식으로 결과를 뱉을 수 있을지....
    
## 중간결과
#### 200913
<img width="487" alt="스크린샷 2020-09-13 오후 11 34 40" src="https://user-images.githubusercontent.com/53211781/93021365-30b6eb00-f61d-11ea-9760-2351d1a61f71.png">

1. naive bayes 알고리즘 사용
    - 최대 정확도 79퍼까지 봤습니다. 
    - 더 좋은 알고리즘 있나 찾아보고 80퍼대까지 올려보고 싶네요
2. 새벽감성 이해 못함....
    - 새벽감성 있으면 정확도가 50퍼 ~ 60퍼대로 급감함
    - 새벽감성 맞출 정확도도 높아야 30퍼대
    - 빼고 돌리니까 최대 79퍼까지 정확도 상승

3. 느낀점
    - 기쁨, 슬픔, 설렘의 감정은 꽤 정확하게 추출하는 것으로 보임
    - 설문조사가 시급합니다.(날씨별, 시간대별로 어떤 감정선의 노래를 선호하는)지
    - 계절별로도 가사를 통한 감정선 추출이 가능할까요????