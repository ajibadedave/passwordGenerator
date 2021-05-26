# This is a program to generate passwords that meet the standard requirements and are secure enough.

############################################################################
#               GOALS                                                      #
# 1. Password should have 16 characters                                    #
# 2. Password should have mixture of upper case and lower case characters  #
# 3. Password should include special characters                            #
# 4. Password should be random                                             #
# 5. Password can be saved, maybe in a text file for now                   #      
#                                                                          #
############################################################################

import random # Will be used to generate random numbers that range from A-Z, a-z and special characters

# Will look into using seed numbers to map passwords to specific accounts

password = '' # An empty string to start

def passChar():
    passNum = random.randint(33, 122)
    character = chr(passNum)
    return character

# FOR loop to run 16 times to get 16 characters
for i in range(16):
    password = password + passChar()

print('Your new password is', password)