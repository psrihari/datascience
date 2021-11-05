# t=('a','b','c')
#
# print(type(t))
#
# myit=iter(t)
#
# print(myit)
#
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit,'sorry'))

def fct():
    for x in range (3):
        yield x**2

a=fct()
# # print(list(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a,'sorry'))

lst=list(a)

print(lst)