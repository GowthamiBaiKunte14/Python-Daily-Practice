'''print('hello')
def sample():
    print('Hello world')
    print('Bye')
print('hello')
sample()
print('hello test')'''


'''global variable'''
'''a=24
def sample():
    print(f'local spaces: {a}')
print(f'main spaces: {a}')
a=a+10
sample()
print(f'main spaces: {a}')'''


'''local variable'''
'''def sample():
    global a
    a=48
    print(f'local spaces: {a}')
a=24
print(f'main spaces: {a}')
sample()
print(f'main spaces: {a}')'''

#check even or odd
def checkEven():
    if num%2==0:
        print(f'{num} is even')
    else:
        print(f'{num} is odd')
num=int(input('Enter a number: '))
checkEven()


