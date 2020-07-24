def find_OTP_key(plaintext1, ciphertext1, ciphertext2):
    """ Breaking a one time pad when the plaintext and ciphertext of Alice is known and the ciphertext of Bob is known. Plaintexts and ciphertexts are in binary. 
        """
        
    OTP_key = str_xor(plaintext1, ciphertext1)
    
    plaintext2 = str_xor(OTP_key, ciphertext2)
    
    
    print("Alice: ", binary_to_english(plaintext1))
    print("Bob: ", binary_to_english(plaintext2))

    

def str_xor(input1,input2):
    assert(len(input1) == len(input2))
    result = ''
    for x in range(len(input1)):
        if input1[x] == input2[x]:
            result += '0'
        else:
            result += '1'
    return result

def binary_to_english(bin_input):
    """Converts binary text to English"""
    bit_to_byte = [bin_input[x:x+8] for x in range(0,len(bin_input), 8)]
    byte_to_ascii = [int(x,2) for x in bit_to_byte]
    ascii_to_english = [chr(x) for x in byte_to_ascii]
    english_text = ''
    for x in ascii_to_english:
        english_text += x 
    return(english_text)
