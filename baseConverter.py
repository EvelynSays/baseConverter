# Output Strings
sep = "»»——✧——««"
greeting = "Hello, I'm Base Bear!"
askName = "What is your name? "
greetName = "Nice to meet you, {}!"
jobDescription = "I can change any base 10 number into Binary!"
base10Question = "What base 10 number would you like me to convert today?"
base10Thanks = "Thank you! {}? Awesome! I'm going to work my magic now!"


# ASCII
baseBearHeart = "ʕ•ᴥ•ʔﾉ♡"
baseBearStar = "ʕ •ᴥ•ʔゝ☆"
baseBearStrong = "ᕦ ʕ •ᴥ•ʔᕤ"
baseBearMagic = "✧･ﾟ: *✧･ﾟ:* 　　 *:･ﾟ✧*:･ﾟ✧"

# Variables
userName = "Evelyn"
binaryResult = ""
base10 = 234
exponent = 0 
exponents = []
currentExponent = 0



# Welcome
print(greeting)
print(baseBearHeart)
#userName = input(askName + "\n")
print(greetName.format(userName) + "\n")
print(jobDescription + "\n")
print(sep + "\n")
print(baseBearStrong)
# base10 = input(base10Question)
print(base10Thanks.format(base10) + "\n")
print(baseBearMagic + "\n")

# Process


""" 
for (i = 0; 'exponent' < base 10; i++)
=> add the exponent to 'exponents' list -?- (return exponents.append(exponent)) -?-
==> calculate the next exponent

(would have full list of exponents after the above for loop?)

for (i = 0; 'exponents' isn't empty; i++)
=> reassign currentExponent to the last value in 'exponents'
==> prune the last exponent from 'exponents'
===> check if base fits into exponent

       !! if it does
=> add a 1 to the binary string
==> subtract the exponent from base10
===> reassign base10 as the result of the subtraction
====> check the new base 10

        !! if it doesnt
=> add a 0 to the binary string
==> reassign currentExponent to the next exponent
===> check the next exponent




 """
