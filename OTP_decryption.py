def find_OTP_key(plaintext1, ciphertext1, ciphertext2):
    """You're an adversary Eve and you're listening to messages sent between Alice and Bob. 
        You know Alice and Bob are encrypting their messages with a One Time Pad. 
        While snooping, you find that Alice accidentally revealed the plaintext (in binary) to her message! 
        Find out what the key that Alice and Bob are using, and find out what Alice and Bob are talking about. 
        
        Important Notes: 
        Inputs will be in binary but the output should be in English text! 
        The function binary_to_english is given to you so you can convert the messages to English.
        Use the str_xor that I provided under help functions:) 
        """
        
    OTP_key = str_xor(plaintext1, ciphertext1)
    
    plaintext2 = str_xor(OTP_key, ciphertext2)
    
    
    print("Alice: ", binary_to_english(plaintext1))
    print("Bob: ", binary_to_english(plaintext2))
        
###----HELP FUNCTIONS!!! DON'T TOUCH :)----###

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
