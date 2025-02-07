import random

def gizli_sayi():
    sayi = random.randint(0, 100)
    alt_sinir = 0
    ust_sinir = 100
    
    while True:
        guess = (alt_sinir + ust_sinir) // 2
        print(f"Tahmin: {guess}")  # Add a print statement to see the guesses
        if guess == sayi:
            return guess
        elif guess < sayi:
            alt_sinir = guess + 1
        else:
            ust_sinir = guess - 1

print(f"Gizli Sayı: {gizli_sayi()}")
