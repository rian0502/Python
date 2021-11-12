nLOOP = int(input('Nilai n : '))
#persegi
print('\nPersegi\n')
for i in range(nLOOP):
    print("*",end=' ')
    for j in range(nLOOP-1):
        print("*",end=' ')
    print()

print()
for i in range(nLOOP):
    for j in range(nLOOP):
        if i == 0 or j == 0 or i == nLOOP-1 or j == nLOOP-1:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()

#jajargenjang kiri
print('\nJajarGenjang 1\n')
for i in reversed(range(nLOOP)):
    for j in range(i):
        print(' ',end='')
    for k in range(nLOOP):
        print('*',end=' ')
    print()

print()
for i in reversed(range(nLOOP)):
    for j in range(i):
        print(' ',end='')
    for k in range(nLOOP):
        if k == 0 or k == nLOOP-1 or i == 0 or i == nLOOP-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()


#jajargenjang kanan
print('\nJajarGenjang 2\n')

for i in range(1,nLOOP+1):
    for j in range(1,i):
        print(' ',end=' ')
    for k in range(1,nLOOP+1):
        print('*',end=' ')
    print()

print()
for i in range(1,nLOOP+1):
    for j in range(1,i):
        print(' ',end=' ')
    for k in range(1,nLOOP+1):
        if i == 1 or i == nLOOP or k == nLOOP or k == 1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()


#segitiga siku siku kiri bawah
print('\nsegitiga siku siku kiri bawah\n')
for i in range(nLOOP+1):
    for j in range(i):
        print('*',end=' ')
    print()
print()
for i in range(nLOOP+1):
    for j in range(i):
        if j == 0 or i == 1 or i == nLOOP or j == i-1:
            print('*',end=' ')
        else :
            print(' ',end=' ')
    print()

#segitiga siku siku kiri atas
print('\nsegitiga siku siku kiri atas\n')
for i in reversed(range(nLOOP+1)):
    for j in range(i):
        print('*',end=' ')
    print()

for i in reversed(range(nLOOP+1)):
    for j in range(i):
        if j == 0 or i == 1 or i == nLOOP or j == i-1:
            print('*',end=' ')
        else :
            print(' ',end=' ')
    print()


#segitiga siku siku kanan bawah
print('\nsegitiga siku siku kanan bawah\n')
for i in range(1,nLOOP+1):
    for j in range(i,nLOOP):
        print('',end=' ')
    for k in range(1,i+1):
        print('*',end='')
    print('')
print()
for i in range(1,nLOOP+1):
    for j in range(i,nLOOP):
        print('',end=' ')
    for k in range(1,i+1):
        if k == 1 or i == nLOOP+1 or k == i or i == nLOOP:
            print('*',end='')
        else :
            print('',end=' ')
    print('')

#segitiga siku siku kanan atas
print('\nsegitiga siku siku kanan atas\n')
for i in range(1,nLOOP+1):
    for j in range(0,i):
        print(' ',end='')
    for k in range((nLOOP+1)-i):
        print('*',end='')
    print('')

print()
for i in range(1,nLOOP+1):
    for j in range(0,i):
        print(' ',end='')
    for k in range((nLOOP+1)-i):
        if i == 1 or k == nLOOP-i or k == 0:
            print('*',end='')
        else :
            print('',end=' ')
    print('')
