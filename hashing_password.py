""" EXERCISE: You just hacked into a company's database and can only see the hash digest of the passwords. 
    You know this company does not salt their hashes and you want to see if any of the passwords are from the list of common passwords. 
    Write a code that will find out which hash digest relates to which password. 
    Try to bruteforce the MD5 hashes that you found. 
    Make sure your code output will result in something like the following: 
    Password 1 is 
    Password 2 is
    Password 3 is 
    ....
    """

#What is the library that lets you use hashes?
import hashlib 

passwordhash1 = "5f4dcc3b5aa765d61d8327deb882cf99"
passwordhash2 = "8621ffdbc5698829397d97767ac13db3"
passwordhash3 = "0acf4539a14b3aa27deeb4cbdf6e989f"
passwordhash4 = "ec0e2603172c73a8b644bb9456c1ff6e"
passwordhash5 = "baed9eee805dceb10b8701814740141d"
passwordhash6 = "0db63cdb573be8e60be1154a2ac56458"

commonpass = ["password", "password123", "123456","12345678","1111111","qwerty","baseball","football",
"dragon","michael","jennifer","superman","mustang","george","abc123","thomas","batman","wonderwoman","flash",
"ironman","test","pass","hockey","volleyball","andrew","love","pepper","salt","hockey","hammer","taylor","golfer",
"cheese","meatball","salad","food","martin","yellow","black","white","brown","red","blue","violet","purple","diamond",
"secret","guitar","violin","piano","phoenix","morgan","aaaaaa","aaaaaaaaa","bbbbbbb","aoisdjfoia","asdfgjkl","zxcvnb",
"scooter","peace","falcon","matrix","money","1273168724","abc789","whatever","gateway","chicken","duck","turkey"]

#----START helper functions, do not touch------#
def hash_value(plaintext_pass):
    return hashlib.md5(plaintext_pass.encode()).hexdigest()
#----END helper functions, do not touch------#


#-----START CODE----#
def break_hash():
    for word in commonpass:
        tempWord = hash_value(word)
        if (tempWord == passwordhash1):
            print ("Password 1 is " + word)
        if (tempWord == passwordhash2):
            print ("Password 2 is " + word)
        if (tempWord == passwordhash3):
            print ("Password 3 is " + word)
        if (tempWord == passwordhash4):
            print ("Password 4 is " + word)
        if (tempWord == passwordhash5):
            print ("Password 5 is " + word)
        if (tempWord == passwordhash6):
            print ("Password 6 is " + word)
#-----END CODE----#