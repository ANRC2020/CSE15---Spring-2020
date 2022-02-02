values = []

for i in range(10):
    x = int(input('Enter value: '))
    if (x%2==1):
        values.append(x)
if(len(values) == 0):
        print('No odd numbers were entered')
else:
        print(max(values))
