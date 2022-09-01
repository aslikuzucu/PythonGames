import random

def play():
    user = input("'t' tas icin, 'k' kagit icin, 'm' makas icin\n")
    computer = random.choice(['t', 'k', 'm'])

    if user == computer:
        return "Cakisma var!"

    #t>m, m>k, k>t
    if is_win (user,computer):
        return 'Kazandin!'
    return 'Kaybettin!'

def is_win(oyuncu,rakip):
    #return true if player wins
    #t>m, m>k, k>t
    if (oyuncu == 't' and rakip == 'm') or (oyuncu == 'm'and rakip=='k') \
        or (oyuncu =='k' and rakip == 't'):
        return True
print(play())




