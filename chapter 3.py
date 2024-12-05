"""
#practice 3.1
names = ['wu si','niu dongcui','han leilei','shan kun']
print(names[0].title())
print(names[1].title())
print(names[-1].title())
print(names[-2].title())

#practice 3.2
message1 = f'how are you,{names[0].title()}'
message2 = f'how are you,{names[1].title()}'
message3 = f'how are you,{names[-2].title()}'
message4 = f'how are you,{names[-1].title()}'
print(message1,message2,message3,message4)

#practice3.3
motor = ['honda','kiwisaki','dayang']
message = f'l would like to own a {motor[1].title()} motorcycle'
print(message5)

#practice 3.4
inviting_person = ['qiao busi','qin shihuang','albert einstein']
print(inviting_person)

#practice 3.5
inviting_person = ['qiao busi','qin shihuang','albert einstein']
pop_person = inviting_person.pop(1)
inviting_person.insert(1,'yuhuang dadi')
print(inviting_person)
print(pop_person)

#practice 3.6
inviting_person = ['qiao busi','qin shihuang','albert einstein']
inviting_person.insert(0,'xi jinping')
inviting_person.insert(2,'baba')
inviting_person.append('mama')
print(inviting_person)

#practice 3.7
inviting_person = ['xi jinping', 'qiao busi', 'baba', 'qin shihuang', 'albert einstein', 'mama']
name1 = inviting_person.pop()
print(f'i am sorry {name1.title()},the dinner is cancle')
name2 = inviting_person.pop()
print(f'i am sorry {name2.title()},the dinner is cancle')
name3 = inviting_person[0]
print(f'i am glade to inverting {name3} to com the dinner')
del inviting_person[0]
del inviting_person[0]
del inviting_person[0]
del inviting_person[0]
print(inviting_person)

#practice 3.8
places = ['kanasi','jiuzhaigou','lushan','changbaishan','guilin']
print(places)
print(sorted(places))
print(places)
print(sorted(places,reverse=True))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
#sort排序
places.sort()
print(places)
places.sort(reverse=True)
print(places)

#practice 3.9
inviting_person = ['xi jinping', 'qiao busi', 'baba', 'qin shihuang', 'albert einstein', 'mama']
n = len(inviting_person)
print(f'i invite {n} person to the dinner')
"""
#practice