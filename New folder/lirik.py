import sys
import time

def jalanin_lirik():
    lirik = [
        ("How can we go back to being friends", 0.1),
        ("When we just shared a bed? (Yeah)              ", 0.10),
        ("How can you look at me and pretend", 0.11),
        ("I'm someone you've never met?", 0.09),
    ]

    delay = [0.3, 0.3, 0.4, 1] 
    print("\nBack To Friends ==")
    time.sleep(2)
    
    for i, (baris_lagu, delay_karakter) in enumerate(lirik):
        for karakter in baris_lagu:
            print(karakter, end='')
            sys.stdout.flush()
            time.sleep(delay_karakter)
        time.sleep(delay[i])
        print('')
    
    print("// Code Lapit")

jalanin_lirik()
