import secrets

password = ''

alphabet = [
    'a','b','c','d','e','f','g','h','i',
    'j','k','l','m','n','o','p','q','r',
    's','t','u','v','w','x','y','z'
]

alphabet_and_symbols = [
    'a','b','c','d','e','f','g','h','i',
    'j','k','l','m','n','o','p','q','r',
    's','t','u','v','w','x','y','z',
    '{','}','(',')','[',']','#',':',';','^',
    ',','.','?','!','|','&','_','`','~','@',
    '$','%','/','\\','=','+','-','*','"',"'"
]

symbol_choice = input('Would you like the password to include symbols? (Y or N) ')

while True:
    if symbol_choice.upper() == 'Y' or symbol_choice.upper() == 'N':
        break
    else:
        symbol_choice = input('\nInvalid answer, answer with Y or N. ')

if symbol_choice.upper() == 'Y':
    symbol_toggle = True
else:
    symbol_toggle = False

while True:
    try:
        lenght = int(input('\nHow long would you like the password to be? '))
        break
    except ValueError:
        print('\nInvalid answer, try again')


characters = 26
if symbol_toggle == True:
    characters += 30

for i in range(lenght):
    case = secrets.randbelow(2)
    if symbol_toggle == False:
        character = secrets.choice(alphabet)
    else:
        character = secrets.choice(alphabet_and_symbols)

    if case == 1:
        character = character.upper()

    password += character

print('password:\n')
print(password)
print('')