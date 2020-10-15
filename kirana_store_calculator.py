sum = 0
print('Press q to exit....')
while True:
    number = input("Enter the price : ")
    if number == 'q':
        print(f'Total : {sum}')
        print('\nThanks for using our calculator')
        break
    elif number != 'q' or number != 'Q':
        number = int(number)
        sum = sum+number
    else:
        print("Invaild input")

