# a=input()
# print(f'hello '+a)

# numbers
# --------------------------
a=2
b=4.5
print(a+b)

# v=int(input('введите число'))
# print(v+10)

# strings
# -------------------------
# name=input('введите ваше имя: ')
# print('привет, '+name+'! Как дела?')

# lists
# --------------------------
a=[2,3,4,5,6,7]
print(a)
a.append('python')
print(len(a))
print(a[0])
print(a[-1])
print(a[2:5])
a.remove('python')

# dict
# --------------------------
s={'cyty':'Moscow','temperature':'20'}
print(s['cyty'])
print(s)
s['temperature']=int(s['temperature'])-5
print(s)
s.get('country','russia')
s['date']='25.11.2018'
print(s)
print(len(s))

# variables
# --------------------------
name='Sergey'
print(name)
