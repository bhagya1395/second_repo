# s=[1,2,3,4]
# l=list(map(lambda x:2*x,s))
# print(l)
#
# l=list(map(lambda x:x, 'intellipaat'))
# print(l)
#
# l1=list(map(lambda x:x,range(11)))
# print(l1)
#
# list1=[1,2,3,4,5,6,7,8]
# l=list(filter(lambda x:x%2!=0 ,list1))
# print(l)
#
# l=[1,2,3,4,5]
# l=[x for x in l if x%2==0]
# print(l)
#
# from functools import reduce
# l1=[1,2,3,4,5,6,7]
# l=reduce(lambda x,y:x+y,l1)
# print(l)
#
# l=[1,2,3,4,5]
# l1=sum([x for x in l])
# print(l1)
#
# l=[x for x in range(21) if x%2==0]
# print(l)
#
# l=[x for x in range(50) if x%2==0 if x%5==0]
# print(l)
#
# even_odd = [f"{x} is even" if x%2==0 else f"{x} is odd" for x in range(10)]
# print(even_odd)
#
# for x in range(4,7):
#     for y in range(1,11):
#         print(f"{x}*{y}={x*y}")
#
# l=[[x*y for y in range(1,11)] for x in range(4,7)]
# print(l)
#
# car={"brand":"Ford","model":"Mustang","year":1995}
# print(car.get("model"))
#
#
# car={"brand":"Ford","model":"Mustang","year":1995}
# print(car.get("car",117))
#
# car={"brand":"Ford","model":"Mustang","year":1995}
# print(car.values())
#
# car={"brand":"Ford","model":"Mustang","year":1995}
# print(car.keys())
#
# d={"brand":"Ford","model":"Mustang","year":1995}
# for v in d.values():
#     print(v)
#
# d={"brand":"Ford","model":"Mustang","year":1995}
# for k,v in d.items():
#     print(k,"--",v)
#
# d={100:"Bhagyashree",200:"Priyanka",300:"Dnyaneshwar"}
# print(d.popitem())
# print(d)
# print(sum(d.keys()))
#
# print('hello')
#
# d={100:"Bhagyashree",200:"Priyanka",300:"Dnyaneshwar"}
# print(d.pop(100 ))
# print(d)

#
# l=[[1,2,3,4,'a','b'],[6,'c',5],[7,'d'],['f','e',8]]
# list=[' '.join([str(x) for x in lst]) for lst in l]
# l1=l[0]
# a="".join(map(str,l1))
# l2=l[1]
# b="".join(map(str,l2))
# l3=l[2]
# c="".join(map(str,l3))
# l4=l[3]
# d="".join(map(str,l4))
# p=sorted(a+b+c+d)
# new_list=[]
# new_list.append(p[:6])
# new_list.append(p[6:9])
# new_list.append(p[9:11])
# new_list.append(p[11:14])
# print(new_list)
# print(type(new_list))


l=[[1,2,3,4,'a','b'],[6,'c',5],[7,'d'],['f','e',8]]
l1=[element for innerList in l for element in innerList]
a="".join(map(str,l1))
s=sorted(a)
new_list=[]
new_list.append(s[:6])
new_list.append(s[6:9])
new_list.append(s[9:11])
new_list.append(s[11:14])
print(new_list)
print(type(new_list))

