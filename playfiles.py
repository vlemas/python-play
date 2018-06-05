
#with open('test.txt', 'a') as f:
 #   f.write('even nicer!!\n')
i=0
with open('test.txt', 'r') as f:
    i+=1
    print(str(i) +' ' + f.readline())
    for line in f:
        i+=1
        print(str(i) +' ' + line, end='')
