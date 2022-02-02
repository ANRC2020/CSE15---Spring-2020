from logic import TruthTable
a = input('Enter proposition 1: ')
b = input('Enter proposition 2: ')
myTable = TruthTable([a])
print (myTable.table)
c = (myTable.table)
print()
myTable = TruthTable([b])
print (myTable.table)
print()
d = (myTable.table)
if (c == d):
    print('The propositions are equivalent')
else:
    print('The propositions are not equivalent')
    
