import json

with open("data_file.json", "r") as read_file:
    reagents = json.load(read_file)


print(reagents)

role = 'none'

role = input('Choose your role. Input "w" for worker or "s" for student \n')

if role == 'w':
    reag = input('\n Choose agent you want to add \n')
    summ = int(input('\n How much? \n'))

    try:
        reagents[reag] += summ
    except:
        reagents[reag] = summ
    
    print('Done')
    
if role == 's':
    reag = input('\nChoose agent you want to take\n')
    l = reagents[reag]
    print('\nHow much?\n', 'You can only take:', l, '\n')
    summ = int(input())

    while summ > l:
        print('Only ', l, ' is avilable. Please input new defenition \n')
        summ = int(input())

        reagents[reag] -= summ
        print('Done')

with open("data_file.json", "w") as write_file:
    json.dump(reagents, write_file)