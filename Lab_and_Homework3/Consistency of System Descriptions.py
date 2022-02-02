from logic import TruthTable
prop=[]
i = 0

for i in range(0, 100):
    cin = input('Enter proposition: ')
    myTable = TruthTable([cin])
    prop.append(myTable.table) 
    cont = input('Would you like to enter more (Y/N): ')
    if(cont == 'N' or cont == 'n'):
        break
    else: 
        i = i + 1

for k in range(0,len(prop)- 1):
    if (prop[k] == prop[k + 1]):
        print('Your description is consistent.')
    else:
        print('Your description is not consistent.')
        
