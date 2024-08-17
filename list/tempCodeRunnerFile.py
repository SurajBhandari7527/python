def func(*args):
    print('do nothing')
    L=[]
    for i in args:
        L.append(i)
    print(sum(L))
func(2,3,4,5,6)