# -*- coding: utf-8 -*-
"""

@author: Dominique
"""

def encoder(plaintext, key):
    cipher = str.lower(plaintext)
    encoded_word=""
    num_list=[]
    for letter in cipher:
        num_list.append(ord(str(letter)))

    for item in num_list:
        if item == 32:
            encoded_word=encoded_word+ " "
        else:
            new_word = item + key
            if new_word > 122:
                new_word = new_word -26
            encoded_word = encoded_word + chr(new_word)
            
    print(encoded_word)
    
    
def decoder(cipher):
    cipher = str.lower(cipher)
    decoded_word=""
    num_list=[]
    for letter in cipher:
        num_list.append(ord(str(letter)))

    for x in range(1,26):
        for item in num_list:
                if item == 32:
                    decoded_word=decoded_word+ " "
                else:
                    new_word = item-x
                    if new_word < 97:
                        new_word = new_word +26
                    decoded_word = decoded_word + chr(new_word)
        print(decoded_word)
        decoded_word=""
