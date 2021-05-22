

from collections import deque

n = int(input())


for _ in range(n):
  card_num = int(input())
  card = list(map(str,input().split()))
  my_card = deque()
  my_card.append(card[0])
  for i in range(1, card_num):
    if (card[i]< my_card[-1]):
      if (card[i]> my_card[0]):
        my_card.append(card[i])
        # print("33",my_card)
      else:
        my_card.appendleft(card[i])
        # print("11",my_card)
    else:
      my_card.append(card[i])
      # print("22",my_card)
  for i in range(card_num):
    print(my_card[i], end='')
  print()
