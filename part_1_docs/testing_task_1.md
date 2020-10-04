### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1:                          # should be ==
      return True
    else                                        # no colon
      return False
   

  dif highest_card(self, card1 card2):          # def not dif. need comman between card1 and card2
  if card1.value > card2.value:                 # needs indent
    return card                                 # should return card1
  else:                                         # needs indent
    return card2
  


def cards_total(self, cards):                   # entire block needs indent
  total                                         # = 0
  for card in cards:
    total += card.value
    return "You have a total of" + total        # should be same line as for. total needs sting
  
```
