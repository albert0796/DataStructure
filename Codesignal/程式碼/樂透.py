import random
lottery=[]
while len(lottery)<6:
    ball=random.randint(1,50)
    lottery.append(ball)
print(lottery)