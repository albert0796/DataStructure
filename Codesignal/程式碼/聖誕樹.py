n=int(input("Input a number:"))
An=1+(n-1)*2
for i in range(1,An+2,2):
    space_num=int((An-i)/2)
    space_left= chr(32)*space_num
    star='*'*i
    space_right= chr(32)*space_num
    row=space_left+star+space_right
    print(row)
    