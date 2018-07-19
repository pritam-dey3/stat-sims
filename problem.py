import random

a = []

class box:
  def __init__(self,num=0, left = None, right = None):
    self.num = num
    self.ball_count = 0
    self.right = right
    self.left = left
  def donate_ball(self):
    self.right.ball_count += 1
    self.left.ball_count += 1

def initiate():
  a.append(box(num = 1))
  for i in range(1,10):
    a.append(box(num=i+1, left = a[i-1]))
    a[i-1].right = a[i]
  a[0].left = a[9]
  a[9].right = a[0]

def distribute():
  for i in range(100):
    a[random.randrange(1,11)].donate_ball()
  
initiate()
for i in range(10):
  print(a[i].ball_count)
