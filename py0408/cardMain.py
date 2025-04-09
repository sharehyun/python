# 카드 프로그램 - card객체사용
# cardMain.py
# 카드리스트 호출
# 카드객체 호출 45장??
# 각각 5장을 나눠준 다음, 비교해서 큰수가 승리하는 형태로 구현

from cardModule import *

c1 = Card(sh,no,5)
c1.card_list()
c1.ran_shuffle()
c1.card_deal()
c1.card_match()