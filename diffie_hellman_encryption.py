
p = 23 #modulus 
g = 5 #base 

def diffie_hellman(alice_private, bob_private): 
    """Try coding the Diffie-Hellman key exchange. 
    p and g are established already. 
    """
    #------START--------# 
    
    alice_public = (g**alice_private)%p
    
    bob_public = (g**bob_private)%p
    
    #print(alice_public, bob_public)
    
    alice_final = (bob_public ** alice_private)%p
    
    bob_final = (alice_public** bob_private)%p
    
    print(alice_final, bob_final)


    #------END--------# 

diffie_hellman(8, 16)