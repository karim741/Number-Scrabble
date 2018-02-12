print("pick one of these numbers ")
list=[1,2,3,4,5,6,7,8,9]
print(list)
for i in range(1000):
    a=int(input("Player 1 Please pick a number from the list: "))
    if a in list:
        list.remove(a)
        break
print(list)
for j in range(1000):
    b=int(input("Player 2 Please pick a number from the list: "))
    if b in list:
        list.remove(b)
        break
print(list)
for k in range(1000):
    c=int(input("Player 1 Please pick a number from the list: "))
    if c in list:
        list.remove(c)
        break
print(list)
for l in range(1000):
    d=int(input("Player 2 Please pick a number from the list: "))
    if d in list:
        list.remove(d)
        break
print(list)
for m in range(1000):
    e=int(input("Player 1 Please pick a number from the list: "))
    if e in list:
        list.remove(e)
        break
print(list)
for i in range(1000):
    f=int(input("Player 2 Please pick a number from the list: "))
    if f in list:
        list.remove(f)
        break
if a+c+e>=15 and b+d+f<15:
    print(" player 1 score is " ,a+c+e,"Player 1 wins")
elif b+d+f>=15 and a+c+e<15:
    print(" player 2 score is " ,b+d+f,"Player 2 wins")
else:
    print("Draw")
