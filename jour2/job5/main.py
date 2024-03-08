word = 'snake'
usr_word = input('Type the word "' + word + '":')
while usr_word != word:
    usr_word = input('Try again!: ')
print('Correct!')