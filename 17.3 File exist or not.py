import os, sys
fname = input('Enter file name = ')

if os.path.isfile(fname):
    f = open(fname, 'r')
else:
    print(fname+ ' does not exist')
    sys.exit()

print("CONTENT IS = ")
str = f.read()
print(str)
f.close()