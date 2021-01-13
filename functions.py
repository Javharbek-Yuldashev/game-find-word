
def get_word():
    from random import choice
    from uzwords import words
    word = choice(words)
    while "-" in word or " " in word or "‘" in word or "’" in word:
        word = choice(words)
    return (word).upper()

def display(user_letters, word):
    display_letter = ""
    for letter in word:
        if letter in user_letters.upper():
            display_letter += letter
        else:
            display_letter += "-"
    return display_letter 
    
    # user_letter = list(user_letters).upper()
    # word_letter = list(word).upper()
    # natija = []
    # for letter in word_letter:
    #     if letter in user_letter:
    #         natija.append(letter)
    #     else:
    #         natija.append('-')
    # matn = ' '.join(map(str,natija))
    # return matn
                
            
def play():
    savol = True
    while savol:
        word = get_word()
        word_letter = set(word)
        print(f"\nMen {len(word)} ta harfdan iborat so'z o'yladim. Topa olasizmi?")
        user_letters = ''
        while len(word_letter)>0:
            print(display(user_letters,word))
            if len(user_letters)>0:
                print(f"Shu vaqtgacha kiritgan harflaringiz: {user_letters}")
            letter = input("Harf kiriting: ").upper()
            if letter in user_letters:
                print("Bu harfni avval kiritgansiz. Boshqa harf kiriting")
                continue
            elif letter in word:
                word_letter.remove(letter)
                print(f"{letter} harfi to'g'ri")
            else:
                print("Bunday harf yo'q")
            user_letters += letter
        print(f"Tabriklayman. Siz {word} so'zini {len(user_letters)} ta urinish bilan topdingiz!")
        savol = int(input("Yana o'ynashni xohlaysizmi?: Ha(1), Yo'q(0): "))
    print("\nRahmat!")
    

















