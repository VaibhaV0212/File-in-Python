f = open('MyData', 'r')
'''
print(f.tell())             # tell the current line
print(f.readline())
print(f.tell())
print(f.seek(4))            #pointer ko desured value pr le jayega aur usk bd sab print kr dega
print(f.readline())
'''
f.close()
print('---------')


f = open('MyData', 'a+')
print('Enter the text to append : ')
while str != '@':
    str = input()
    if(str != '@'):
        f.write(str+ "\t \n")

f.seek(0,0)
print('The file contains = ')
str = f.read()
print(str)
f.close()
