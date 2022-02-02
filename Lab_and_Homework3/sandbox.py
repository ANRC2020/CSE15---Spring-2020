from logic import TruthTable
V = []
B = []
Q = []
a = []
b = []
var = ''

def first():
    list3.append(list1[0+ (numvar +1)*x:(numvar +1)+(numvar +1)*x])

while True:
     x = input("Enter  a proposition: ")
     V.append(x)
     c = str(input("Would you like to enter a more (Y/N) :"))
     if (c in ['y', 'Y']):
         continue
     if (c in ['n', 'N']):
         break

for i in range(0, len(V)):
    A= 'and'
    C='or'
    D='->'
    E='<->'
    F='-'
    Space = ' '
    if (str(A) in V[i]):        
        V[i] = V[i].replace(' and ', "")
        var = var + str(V[i])
    if (str(C) in V[i]):
        V[i] = V[i].replace(' or ', "")
        var = var + str(V[i])
    if (str(D) in V[i]):
        V[i] = V[i].replace( ' -> ', "")
        var = var + str(V[i])
    if (str(E) in V[i]):
        V[i] = V[i].replace(' <-> ', "")
        str(V[i])
    if (str(F) in V[i]):
        V[i] = V[i].replace('-', "")
        var = var + str(V[i])
    elif (str(Space) in V[i]):
        V[i] = V[i].replace(' ', "")
        var = var + str(V[i])
        
list2 = []
for x in range(0, len(str(var))):
    list2.append(var[x])
for i in range(0, len(list2)):
    Capital = 65
    Character = 97
    if (ord(list2[i]) >= 97 and ord(list2[i]) <= 123):
        for y in range(0, 26):
            chr(Character)
            if (chr(Character) == list2[i]):
                B.append(list2[i])
            Character = Character + 1
    if(ord(list2[i]) >= 65 and ord(list2[i]) <= 91):
        for y in range(0, 26):
            chr(Capital)
            if (chr(Capital) == list2[i]):
                B.append(list2[i])
            Capital = Capital + 1

print(list(set(B)))

cin =input("Enter logic statement: ")
i = TruthTable([cin])

i = str(i.table)
i = i.replace("[","")
i = i.replace("]","")
i = i.replace(" ","")
i = i.replace(",","")

list1 = []
for x in range(0, len(str(i))):
    list1.append(i[x])

numvar = 2
length = (len(list1)/(numvar +1))
list3 = []
for x in range(0,int(length)):
    first()
    
print(list3)
list4 = []
for x in range(0, len(str(i))):
    if((x) % int(numvar + 1)== numvar):
        list4.append(list1[x])

print(list4)

for x in range(0,len(list4)):
    if(list4[x] == 1):
        print(list3[int(list4[x])])

