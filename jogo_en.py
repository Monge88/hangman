def main():
    while True:
        try:
            num = int(input('Which category do you want to guess a word?\n'
			    '1 - Country\n'
			    '2 - Sports\n'
			    '3 - Movies\n'
			    '4 - Bands\n'
			    '\nYour choice: '))
        except (ValueError, TypeError):
            print('Please type a number between 1 and 5!')
        else:
            if not 1 <= num <= 5:
                print('Please type a number between 1 and 5!')
            else:
                break

    drawn_word = list(choose_word(num).lower())
    hangman(drawn_word)


def hangman(drawn_word):
    from draw import pic
    from time import sleep

    right_word = drawn_word.copy()
    for i in range(len(right_word)):
        if right_word[i] == ' ':
            right_word[i] = ' '
        else:
            right_word[i] = '-'

    choosen_words = []
    chances = 0
    print(pic[0])
    print(''.join(right_word))
    while chances < len(pic)-1:  
        print(f'Words already choosen: {",".join(choosen_words)}')
        guess = input('Your guess: ').lower()
        sleep(0.3)

        if guess not in choosen_words:  
            choosen_words.append(guess)
        else:
            print(f'You already type the word: {guess}')
            continue

        if guess not in drawn_word:
            chances += 1
            print(pic[chances])
            print(show_word(guess, drawn_word, right_word))
            if chances == len(pic)-1:
                print(f'You lost! The secret word was {"".join(drawn_word).title()}')

        else:  
            print(pic[chances])
            final_word = show_word(guess, drawn_word, right_word)
            print(final_word)
            if ''.join(final_word) == ''.join(drawn_word):
                print('CONGRATULATIONS! YOU WON!!!!')
                break


def show_word(guess, drawn_word, right_word):
    for i, j in enumerate(drawn_word):
        if drawn_word[i] == guess:
            right_word[i] = j
    return ''.join(right_word)


def choose_word(choice):
    from categories import category
    import random
    word = ''
    if choice == 1:
        p = random.randint(1, len(category['Countries'])-1)
        word = category['Countries'][p]
    elif choice == 2:
        p = random.randint(1, len(category['Sports'])-1)
        word = category['Sports'][p]
    elif choice == 3:
        p = random.randint(1, len(category['Movies'])-1)
        word = category['Movies'][p]
    elif choice == 4:
        p = random.randint(1, len(category['Bands'])-1)
        word = category['Bands'][p]

    return word


main()
