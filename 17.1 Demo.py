f = open('MyData', 'r')
#print(file_handler.read())
#print(file_handler.readline())     #print only 1s line
#print(file_handler.readlines())     #print in one line
print(f.read().splitlines())     #print in one line

f1 = open('abc', 'w')    #will create a new file
#f1.write('something')   # will write in 'abc' but will delete the previous data

for data in f:
    f1.write(data)


'''
w - write data but will delete the previous data
r - read the data
a - append the data
w+ - write and read and will delete the previous one
r+ - read and write, data will not be deleted
a+ - append and read

if we attach 'b' with them it means binary, wb, rb, w+b ..... 
'''