
# x = set()
# x.add((1,2,3))
# x.add('1,2')
# a = x.pop()
#
# print(x, len(x))
# print(f'{a=}')
#
# x.add(True)
# a = x.copy()
# print(x, len(x))
# print(f'{a=}')
#
# x.remove(True)
# print(x, len(x))
# y = set(list([1,2,3,4,3,2,1]))
# print(f'{y=}')
# x.intersection(y)
#
# print(x, len(x))
# print(y,len(y))
# print(x.pop())
# x.update(y)
#
# print(x, len(x))
# print(y,len(y))


# x = {1,2,3}
# y = {4,5,6}


# # x.update(y)
# y.update(x)
# y.add(10)
# y.discard(100)
# # y.remove(1000)
# print(f'{x=}', len(x))
# print(f'{y=}',len(y))
#
# print(y.discard(100))
#
# for el in y:
#     print(el,end=' ')

# print(x | y)
# print(len(x | y))
# # x = x | y
# x.union(y)
# print(f'{x=}')

# x = {1,2,3}
# y = {1,4,5,6}
# x.union(y)
# print(x)
# # print(x | y)
# # print(y.union(x))
# print(f'{y=}')


# print(x.intersection(y))
# print(x)


# print(x)
# print(f'{y=}')

# print(y-x)
# print(x-y)
# print(x.difference(y))
# print(y.difference(x))

# x = {1,2,3}
# y = {1,4,5,6}
#
# print(x)
# print(f'{y=}')
# print(x.symmetric_difference(y))
# print(y.symmetric_difference(x))


# x = {'',2,3,4,0}
# y = {2,3,1}
# print(x==y)
# print(x>y)
# print(x<y)

# print(all(x))

# print(any(x))

#
# x.clear()
# print(x)

# z = x
# print(z,type(z))
# z.add(100)
# print(z,type(z))
# print(x)
# x.add(123)
# print(z,type(z))
# print(x)
#
# z = x.copy()
# z.add(10000)
# print(z,type(z))
# print(x)
#
# # print(z.difference(x))
# # print(z.difference_update(x))
# # c = x.difference_update(z)
# # print(c)
# c = x.intersection(z)
# print(c)
# # c = x.intersection_update()
# x.intersection_update()
# print(x)
# # print(x.intersection_update())

# x = {'', 0, 2, 3, 4, 100, 123}
# y = {1, 2, 3}
# z = {'', 0, 2, 3, 4, 100, 10000, 123}
# # for i in enumerate(x,1):
# #     print(*i)
#
#
# print()
# x.difference_update(y)  # x={'', 0, 4, 100, 123}
# # print(x.difference(y)) # x= {'', 0, 4, 100, 123}
# # print(f'{x=}')
#
# # print(x.isdisjoint(y))
# z.add(1)
# # print(x.isdisjoint(y))
# # print(f'{x=}')
#
# # print()
# # print(y.issubset(z))
# # print(z.issubset(y))
# # print()
# # print(y.issuperset(z))
# # print(z.issuperset(y))
# # z.discard('')
#
# # print(max(y))
# # a = sorted(z)
# # print(f'{a=}')
# x={1, 2, 3,10}
# y={0, 2, 3, 4, 100, 1, 10000, 123}
#
# print(f'{x=}')
# print(f'{y=}')
# print()
# # print(x.symmetric_difference(y))
# # print(y.symmetric_difference(x))
# x.symmetric_difference_update(y)
# print(f'{x=}')
#
# y.symmetric_difference_update(x)
# print(f'{y=}')
