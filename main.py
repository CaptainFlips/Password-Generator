import secrets

password = ''

alphabet = [
    'a','b','c','d','e','f','g','h','i',
    'j','k','l','m','n','o','p','q','r',
    's','t','u','v','w','x','y','z'
]

symbols = [
    '{','}','(',')','[',']','#',':',';','^',
    ',','.','?','!','|','&','_','`','~','@',
    '$','%','/','\\','=','+','-','*','"',"'"
]

numbers = ['0','1','2','3','4','5','6','7','8','9']

selected_characters = []
generator = 'password'

secretsGenerator = secrets.SystemRandom()

while True:

    while True:
        type_choice = input('\nWould you like the password or the number generator? (P or N) ')
        if type_choice.upper() == 'N':
            generator = 'number'
            break
        elif type_choice.upper() == 'P':
            break
        else:
            print('\nInvalid answer, try again. ')

    if generator == 'number':
        break

    while True:
        letter_choice = input('\nWould you like the password to include letters? (Y or N) ')
        if letter_choice.upper() == 'Y':
            selected_characters += alphabet
            break
        elif letter_choice.upper() == 'N':
            break
        else:
            print('\nInvalid answer, try again. ')

    while True:
        number_choice = input('\nWould you like the password to include numbers? (Y or N) ')
        if number_choice.upper() == 'Y':
            selected_characters += numbers
            break
        elif number_choice.upper() == 'N':
            break
        else:
            print('\nInvalid answer, try again. ')

    while True:
        symbol_choice = input('\nWould you like the password to include symbols? (Y or N) ')
        if symbol_choice.upper() == 'Y':
            selected_characters += symbols
            break
        elif symbol_choice.upper() == 'N':
            break
        else:
            print('\nInvalid answer, try again. ')


    if len(selected_characters) == 0:
        print('\nPlease select at least one option.')
    else:
        break

if generator == 'number':

    while True:
        try:
            lenght = int(input('\nHow long would you like the number to be? '))
            if lenght > 0:
                break
        except ValueError:
            pass
        print('\nInvalid answer, try again')

    for i in range(lenght):
        character = secretsGenerator.randint(0,9)
        password += str(character)

    print('\nnumber:')
    print('\t'*2+ password)
    input('\nPress ENTER to exit')

else:

    while True:
        try:
            lenght = int(input('\nHow long would you like the password to be? '))
            if lenght > 0:
                break
        except ValueError:
            pass
        print('\nInvalid answer, try again')

    for i in range(lenght):
        case = secrets.randbelow(2)

        character = secrets.choice(selected_characters)

        if case == 1:
            character = character.upper()

        password += character

    print('\npassword:')
    print('\t'*2+ password)
    input('\nPress ENTER to exit')