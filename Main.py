import asn1tools as asn
import json

### AfS software assignment 1 - example code ###

# set file names
base_location = './'
ops_loc = base_location + 'operations.asn'
exs_loc = base_location + 'my_exercises'
ans_loc = base_location + 'my_answers'

# global counter for the number of elementary additions/subtractions operations
count_add = 0
# global counter for the number of elementary multiplication operations
count_mul = 0

# global variables for result of Euclidean Algorithm
answ_d = ''
answ_a = ''
answ_b = ''

###### Creating an exercise list file ######

# Create a JSON file containing exercises
def createExerciseJSONfile():
    exercises = {'exercises' : []}                                      # initialize empty exercise list

    # example exercise
    ex = {'add' : {'radix' : 10, 'x' : '-150', 'y' : '-6', 'answer' : '-156'}} # create add exercise
    #exercises['exercises'].append(ex)                                   # add exercise to list


    # given exercises

    ex = {'add' : {'radix' : 2, 'x' : '1010100001110101001010001100101110111101101110000101011100111000000000010111010010110000001101011100', 'y' : '1001100111111111001111101100000011100001111100100001001001011000101111111010011111010011010101000110', 'answer' : '10100001001110100011001111000110010011111101010100110100110010000110000010001110010000011100010100010'}}
    #exercises['exercises'].append(ex)

    ex = {'add' : {'radix' : 2, 'x' : '1010100001110101001010001100101110111101101110000101011100111000000000010111010010110000001101011100', 'y' : '-1001100111111111001111101100000011100001111100100001001001011000101111111010011111010011010101000110', 'answer' : '111001110101111010100000101011011011110001100100010011011111010000011100110011011100111000010110'}}
    #exercises['exercises'].append(ex)

    ex = {'subtract' : {'radix' : 2, 'x' : '1010100001110101001010001100101110111101101110000101011100111000000000010111010010110000001101011100', 'y' : '1001100111111111001111101100000011100001111100100001001001011000101111111010011111010011010101000110', 'answer' : '111001110101111010100000101011011011110001100100010011011111010000011100110011011100111000010110'}}
    #exercises['exercises'].append(ex)

    ex = {'subtract' : {'radix' : 2, 'x' : '1010100001110101001010001100101110111101101110000101011100111000000000010111010010110000001101011100', 'y' : '-1001100111111111001111101100000011100001111100100001001001011000101111111010011111010011010101000110', 'answer' : '10100001001110100011001111000110010011111101010100110100110010000110000010001110010000011100010100010'}}
    #exercises['exercises'].append(ex)

    ex = {'multiply' : {'radix' : 2, 'x' : '1010100001110101001010001100101110111101101110000101011100111000000000010111010010110000001101011100', 'y' : '1001100111111111001111101100000011100001111100100001001001011000101111111010011111010011010101000110', 'answer' : '1100101010101011111101101100000101100111100001101011011001011101000111010100011101110100001111110001110111001101101001100110001110010110011001111000100110110011011010101100010001000001111011100101000', 'count-mul': '...', 'count-add': '...'}}
    #exercises['exercises'].append(ex)

    ex = {'karatsuba' : {'radix' : 2, 'x' : '1010100001110101001010001100101110111101101110000101011100111000000000010111010010110000001101011100', 'y' : '1001100111111111001111101100000011100001111100100001001001011000101111111010011111010011010101000110', 'answer' : '1100101010101011111101101100000101100111100001101011011001011101000111010100011101110100001111110001110111001101101001100110001110010110011001111000100110110011011010101100010001000001111011100101000', 'count-mul': '...', 'count-add': '...'}}
    #exercises['exercises'].append(ex)


    ex = {'add' : {'radix' : 3, 'x' : '2020111212202021100001212221022010021001', 'y' : '1202222101212012211022202222112120020101', 'answer' : '11000111021121111011101122220211200111102'}}
    #exercises['exercises'].append(ex)

    ex = {'add' : {'radix' : 3, 'x' : '2020111212202021100001212221022010021001', 'y' : '-1202222101212012211022202222112120020101', 'answer' : '110112110220001111202002221202120000200'}}
    #exercises['exercises'].append(ex)

    ex = {'subtract' : {'radix' : 3, 'x' : '2020111212202021100001212221022010021001', 'y' : '1202222101212012211022202222112120020101', 'answer' : '110112110220001111202002221202120000200'}}
    #exercises['exercises'].append(ex)

    ex = {'subtract' : {'radix' : 3, 'x' : '2020111212202021100001212221022010021001', 'y' : '-1202222101212012211022202222112120020101', 'answer' : '11000111021121111011101122220211200111102'}}
    #exercises['exercises'].append(ex)

    ex = {'multiply' : {'radix' : 3, 'x' : '2020111212202021100001212221022010021001', 'y' : '1202222101212012211022202222112120020101', 'answer' : '10222112100001022222012101100012020101212101011201011110022221012121011022211101', 'count-mul': '...', 'count-add': '...'}}
    #exercises['exercises'].append(ex)

    ex = {'karatsuba' : {'radix' : 3, 'x' : '2020111212202021100001212221022010021001', 'y' : '1202222101212012211022202222112120020101', 'answer' : '10222112100001022222012101100012020101212101011201011110022221012121011022211101', 'count-mul': '...', 'count-add': '...'}}
    #exercises['exercises'].append(ex)


    ex = {'add' : {'radix' : 7, 'x' : '255250226011363161263502222556', 'y' : '153556502550413362430240350510', 'answer' : '442140031562106554024042603366'}}
    #exercises['exercises'].append(ex)

    ex = {'add' : {'radix' : 7, 'x' : '255250226011363161263502222556', 'y' : '-153556502550413362430240350510', 'answer' : '101360423130646465533231542046'}}
    #exercises['exercises'].append(ex)

    ex = {'subtract' : {'radix' : 7, 'x' : '255250226011363161263502222556', 'y' : '153556502550413362430240350510', 'answer' : '101360423130646465533231542046'}}
    #exercises['exercises'].append(ex)

    ex = {'subtract' : {'radix' : 7, 'x' : '255250226011363161263502222556', 'y' : '-153556502550413362430240350510', 'answer' : '442140031562106554024042603366'}}
    #exercises['exercises'].append(ex)

    ex = {'multiply' : {'radix' : 7, 'x' : '255250226011363161263502222556', 'y' : '153556502550413362430240350510', 'answer' : '50303335051551042446540232630332141424231165632644465060060', 'count-mul': '...', 'count-add': '...'}}
    #exercises['exercises'].append(ex)

    ex = {'karatsuba' : {'radix' : 7, 'x' : '255250226011363161263502222556', 'y' : '153556502550413362430240350510', 'answer' : '50303335051551042446540232630332141424231165632644465060060', 'count-mul': '...', 'count-add': '...'}}
    #exercises['exercises'].append(ex)


    ex = {'add' : {'radix' : 16, 'x' : '82a4d3f8bfab54bb3011', 'y' : 'cb95aa820d14888e48c3', 'answer' : '14e3a7e7accbfdd4978d4'}}
    #exercises['exercises'].append(ex)

    ex = {'add' : {'radix' : 16, 'x' : '82a4d3f8bfab54bb3011', 'y' : '-cb95aa820d14888e48c3', 'answer' : '-48f0d6894d6933d318b2'}}
    #exercises['exercises'].append(ex)

    ex = {'subtract' : {'radix' : 16, 'x' : '82a4d3f8bfab54bb3011', 'y' : 'cb95aa820d14888e48c3', 'answer' : '-48f0d6894d6933d318b2'}}
    #exercises['exercises'].append(ex)

    ex = {'subtract' : {'radix' : 16, 'x' : '82a4d3f8bfab54bb3011', 'y' : '-cb95aa820d14888e48c3', 'answer' : '14e3a7e7accbfdd4978d4'}}
    #exercises['exercises'].append(ex)

    ex = {'multiply' : {'radix' : 16, 'x' : '82a4d3f8bfab54bb3011', 'y' : 'cb95aa820d14888e48c3', 'answer' : '67e5150972e817d639ac0f8795213f07e18864f3', 'count-mul': '...', 'count-add': '...'}}
    #exercises['exercises'].append(ex)

    ex = {'karatsuba' : {'radix' : 16, 'x' : '82a4d3f8bfab54bb3011', 'y' : 'cb95aa820d14888e48c3', 'answer' : '67e5150972e817d639ac0f8795213f07e18864f3', 'count-mul': '...', 'count-add': '...'}}
    #exercises['exercises'].append(ex)

    ex = {'reduce' : {'radix' : 16, 'x' : 'd26936c465648ef03a1ade904737b30428155781', 'm' : '157f77a46f4c796bb774', 'answer' : '2c0793480f2afd6dc5d'}}
    #exercises['exercises'].append(ex)

    ex = {'mod-add' : {'radix' : 16, 'x' : '93f76ca85dfdbf3f1790', 'y' : 'c2a72e55e1956be991ca', 'm' : '157f77a46f4c796bb774', 'answer' : '1426985bba180dd8e98e'}}
    #exercises['exercises'].append(ex)

    ex = {'mod-subtract' : {'radix' : 16, 'x' : '93f76ca85dfdbf3f1790', 'y' : 'c2a72e55e1956be991ca', 'm' : '157f77a46f4c796bb774', 'answer' : '11cea53fca4dbf98ac22'}}
    #exercises['exercises'].append(ex)

    ex = {'mod-subtract' : {'radix' : 16, 'x' : 'c2a72e55e1956be991ca', 'y' : '93f76ca85dfdbf3f1790', 'm' : '157f77a46f4c796bb774', 'answer' : '3b0d264a4feb9d30b52'}}
    #exercises['exercises'].append(ex)

    ex = {'mod-multiply' : {'radix' : 16, 'x' : '93f76ca85dfdbf3f1790', 'y' : 'c2a72e55e1956be991ca', 'm' : '157f77a46f4c796bb774', 'answer' : 'dad2e63149941a790c4'}}
    #exercises['exercises'].append(ex)

    ex = {'euclid' : {'radix' : 16, 'x' : 'c1b715933d2d1dcb0e23', 'y' : '157f77a46f4c796bb774', 'answ-d' : '1', 'answ-a' : '8bb87443ec917fa3e87', 'answ-b' : '-4eb01402d28cbe3588c1'}}
    #exercises['exercises'].append(ex)

    ex = {'inverse' : {'radix' : 16, 'x' : 'c1b715933d2d1dcb0e23', 'm' : '157f77a46f4c796bb774', 'answer' : '8bb87443ec917fa3e87'}}
    exercises['exercises'].append(ex)

    ex = {'euclid' : {'radix' : 16, 'x' : 'b22b5d17e57a41599185', 'y' : '157f77a46f4c796bb774', 'answ-d' : '19', 'answ-a' : '-74ba5fd6968445267', 'answ-b' : '3c769a8d705995e753'}}
    #exercises['exercises'].append(ex)

    ex = {'inverse' : {'radix' : 16, 'x' : 'b22b5d17e57a41599185', 'm' : '157f77a46f4c796bb774', 'answer' : 'ERROR - inverse does not exist'}}
    #exercises['exercises'].append(ex)

    # Encode exercise list and print to file
    my_file = open(exs_loc, 'wb+')                                     # write to binary file
    my_file.write(json.dumps(exercises).encode())                      # add encoded exercise list
    my_file.close()
    return

# call this function to create exercises-file with exercises included inside it
# or put it in comment to use existing exercises-file
createExerciseJSONfile()

###### Using an exercise list file ######

# Compile specification
spec = asn.compile_files(ops_loc, codec = "jer")

# Read exercise list
exercise_file = open(exs_loc, 'rb')                                # open binary file
file_data = exercise_file.read()                                   # read byte array
my_exercises = spec.decode('Exercises', file_data)                 # decode after specification
exercise_file.close()

# Create answer JSON
my_answers = {'exercises': []}

#Add 0 padding to the front of x or y array so they are the same size and same order digits line up
def padArray(x, y):
    #If they already have the same length skip the function
    if (len(x) != len(y)):
        #For the amount of digits in the greater array loop and add 0's to the smaller array
        for i in range(max(len(x), len(y))+1):
            if len(x) < i:
                x.insert(1, 0)
            if len(y) < i:
                y.insert(1, 0)
    return x, y


#Remove any padding leftover from calculating with padding assuming no array with only sign and zeroes is entered
def removePadding(x):
    i=1
    #Loop to remove all padding
    while(True):
        #If a 0 array is entered break immediately and return same array
        if i >= len(x):
            break
        #If x is a leading zero remove it and reset index counter to previous position otherwise it skips over one indez
        if x[i] == 0:
            x.pop(i)
            i -= 1
        #Break if a non-zero element is found since
        elif x[i] > 0:
            break
        i +=1
    if(len(x) == 1):
        return ["pos", 0]
    return x


#turns an input into a list, to use in operations
#input s:string example: "-1f34"
#output list ["neg",1,15,3,4]
def parseString(s):
    map = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"a":10,"b":11,"c":12,"d":13,"e":14,"f":15}
    if s.startswith("-"):
        result = ["neg"]
        s = s[1:]
    else:
        result = ["pos"]

    result += [map[i] for i in s]
    return result

#inverse of parseString
def toString(l):
    map = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "a",11: "b",12: "c", 13: "d", 14: "e",15: "f"}

    out = ""
    if l[0] == "neg":
        out = "-"

    out += "".join([map[i] for i in l[1:]])
    return out

#Assume two padded arrays enter and compare size without looking at sign
#Returns > if x>y, < if x<y and = if x=y
def cmpMagnitude(x, y):
    for i in range(1, len(x)):
        if x[i] > y[i]:
            return '>'
        if x[i] < y[i]:
            return '<'
    return '='

# function to reverse a string
def reverse(x):
    return x[::-1]

# function to convert hexadecimal symbol to decimal numerical integer value
def hexStrToDecDig(x):
    if   x == "a" or x == "A":
        result = 10
    elif x == "b" or x == "B":
        result = 11
    elif x == "c" or x == "C":
        result = 12
    elif x == "d" or x == "D":
        result = 13
    elif x == "e" or x == "E":
        result = 14
    elif x == "f" or x == "F":
        result = 15
    elif x == "0" or x == "1" or x == "2" or x == "3" or x == "4" or x == "5" or x == "6" or x == "7" or x == "8" or x == "9":
        result = int(x)
    else:
        print ("invalid input symbol '" + x + "' provided. '1' is used instead.")
        result = 1
    return result

# function to convert decimal numerical integer value to hexadecimal symbol
def decDigToHexStr(x):
    if x < 10:
        result = str(x)
    elif x == 10:
        result = "a"
    elif x == 11:
        result = "b"
    elif x == 12:
        result = "c"
    elif x == 13:
        result = "d"
    elif x == 14:
        result = "e"
    elif x == 15:
        result = "f"
    else:
        print ("invalid number '" + x + "' provided. '1' is used instead.")
        result = 1
    return result


# compare two numbers
# return ( x "<", "=" or ">" y )
def CmpNumbers(x, y):
    if (x < y):
        return "<"
    elif (x > y):
        return ">"
    else:
        return "="

# compare two strings with hexadecimal symbols
# return  ( x "<", "=" or ">" y )
def CmpHexStr(x, y):
    negative = 0

    if (x[0] == "-"): # x is negative
        if (y[0] == "-"): # y is negative
            # both x and y are negative
            x = x[1:]
            y = y[1:]
            negative = 1
        else: # y[0] != "-", so y is non negative
            return "<"
    else: # x[0] != "-", so x is non negative
        if (y[0] == "-"): # y is negative
            return ">"
        #else both x and y are non negative

    n_x  = len(x)
    n_y  = len(y)

    # compare length
    if (n_x < n_y):
        cmpresult = "<"
    elif (n_x > n_y):
        cmpresult = ">"
    else: # x and y have equal length
        # compare symbols starting from the hiest one
        for i in range(n_x):
            cmpresult = CmpNumbers (hexStrToDecDig(x[i]), hexStrToDecDig(y[i]))
            # don't continue comparition when the first difference is found
            if cmpresult != "=":
                break

    if (negative == 1):
        # both x and y are negative => reverse comparison result
        # example: (5 < 10) => (-5 > -10)
        if (cmpresult == "<"):
            cmpresult = ">"
        elif (cmpresult == ">"):
            cmpresult = "<"
        #else keep cmpresult "="

    return cmpresult


#Change the sign of 'y' and calls preAddition funciton.
#Input:  radix: integer number between 2 and 16
#        x, y:  Strings for the two values to be subtracted (x+y)
#Output: result of the function as String (x+y)
def preSubtract(r, x, y):
    # change the sign of 'y' and make addition (x + (-y))
    if y[0] == "-":
        # remove "-"
        y = y[1:]
    else:
        # add"-"
        y = "-" + y
    return preAddition(r, x, y)

#Calls addition funciton, but before that
#turn 'x' and 'y' into lists and add padding so they have same length.
#Finally provide answer converted back to string with removed possible 0 padding.
#Input:  radix: integer number between 2 and 16
#        x, y:  Strings for the two values to be added (x+y)
#Output: result of the function as String (x+y)
def preAddition(r, x, y):
    #Get x and y and add padding so x and y are same length
    x, y = padArray(parseString(x), parseString(y))
    #Get answer from addition function and convert back to string and remove possible 0 padding
    return (toString(removePadding(addition(r, x, y))))

#Uses the fact that x-y = x+ -y. Thus it flips the sign of y and then uses the addition function to calculate the answer
def subtract(r, x, y):
    if y[0] == 'pos':
        y[0] = 'neg'
    else:
        y[0] = 'pos'
    return addition(r, x, y)

#Checks which addition case is the current exercise and adds elements in the array accordingly.
#Cases are: Both positive, both negative, both different sign
#In the first and second case we can just add all the elements with the primary school method
#In the third case we check which numbers magnitude is bigger and subtract the smaller from the larger and keep the larger's sign
def addition(r, x, y):
    global count_add
    answer = []
    carry = 0
    signx = True if x[0] == "neg" else False
    signy = True if y[0] == "neg" else False

    #Same sign addition
    if (signx and signy) or (not(signx) and not(signy)):
        for i in range(len(x)-1, 0 ,-1):
            a = x[i]
            b = y[i]
            if a+b+carry < r:
                ins = a+b+carry
                carry = 0
            else:
                ins = a+b+carry-r
                carry = 1
            #count simple addition operations
            count_add = count_add + 1
            answer.insert(0, ins)
        if carry > 0:
            answer.insert(0, carry)
        if signx:
            answer.insert(0, "neg")
        else:
            answer.insert(0, "pos")
    else:
        #Different signs addition
        cmp = cmpMagnitude(x, y)
        for i in range(len(x)-1, 0, -1):
            if cmp == '>':
                a = x[i]
                b = y[i]
            elif cmp == '<':
                a=y[i]
                b=x[i]
            else:
                return ['pos', 0]
            if a-b-carry < 0:
                ins = r+(a-b-carry)
                carry = 1
            else:
                ins = a-b-carry
                carry = 0
            #count simple addition operations
            count_add = count_add + 1
            answer.insert(0, ins)
        if cmp =='>':
            answer.insert(0, x[0])
        else:
            answer.insert(0, y[0])
    return answer


#This function calculates module addition.
#Input:  radix: integer number between 2 and 16
#        x, y:  Strings for the two values to be added (x+y)
#        m:     String for module value
#Output: result of the function as String ((x+y) mod m)
def modAdd(radix, x, y, m):
    if len(x) == 0 or len(y) == 0 or len(m) == 0:
        return "invalid input data"

    # make integer addition
    z_output = preAddition(radix, x, y) # z = x + y

    while CmpHexStr(z_output, m) != "<": # z >= m
        # make integer subtraction
        # to subtract module 'm' from this result
        z_output = preSubtract(radix, z_output, m) # z = (x + y) - m

    return z_output


#This function calculates module subtraction.
#Input:  radix: integer number between 2 and 16
#        x, y:  Strings for the two values to be subtracted (x-y)
#        m:     String for module value
#Output: result of the function as String ((x-y) mod m)
def modSubtract(radix, x, y, m):
    if len(x) == 0 or len(y) == 0 or len(m) == 0:
        return "invalid input data"

    # make integer subtraction
    z_output = preSubtract(radix, x, y) # z = x - y

    if z_output[0] == "-": # sign '-'
        # make integer addition to add module 'm' to this result
        while z_output[0] == "-":
            z_output = preAddition(radix, z_output, m) # z = z + m

    else: # sign '+'
        # make integer subtraction
        # to subtract module 'm' from this result
        # like in mod-addition functionality
        while CmpHexStr(z_output, m) != "<": # z >= m
            z_output = preSubtract(radix, z_output, m) # z = z - m

    return z_output


def subUntil(num, divisor):
    count = 0
    while num >= divisor:
        num -= divisor
        count += 1
    return num, count

def multiply(params):
    # Parse parameters
    x = parseString(params["x"])
    y = parseString(params["y"])
    radix = params["radix"]
    n_add, n_mult = 0, 0

    # Determine the sign (neg * pos and vice versa --> neg, pos otherwise)
    sign = ["pos", "neg"][((x[0] == "neg") + (y[0] == "neg")) % 2]

    # Use the smallest number as base to multiply with
    if len(x) >= len(y):
        top, btm = x, y
    else:
        top, btm = y, x

    ans = []
    carry = 0

    # Mult all numbers
    # Loop over every bottom number
    for i in range(len(btm)):
        if i == len(btm)-1:
            break

        # Add padding for indexes > 0
        ans.append([0 for _ in range(i)])
        num_btm = btm[-(i+1)]

        # Loop over every top number
        for j in range(len(top)):
            if j == len(top)-1:
                break
            num_top = top[-(j+1)]

            # Multiply the bottom with the top number and add the carry
            mult = num_btm * num_top + carry
            n_add += 1
            n_mult += 1

            # Calculate new carry and reduce answer
            mult, carry = subUntil(mult, radix)
            n_add += carry

            # Add to answer array
            ans[i].append(mult)

        # If there's a carry bigger than the number length, add it on its own
        if carry != 0:
            ans[i].append(carry)
        carry = 0
    
    # Add the multiplied numbers
    final = []
    carry = 0
    for i in range(len(ans[-1])):
        summed = carry

        # Add all numbers in the same row level
        for row in range(len(ans)):
            if len(ans[row]) > i:
                if ans[row][i] > 0:
                    summed += ans[row][i]
                    n_add += 1

        # Calculate new carry, reduce answer and add it to final array
        summed, carry = subUntil(summed, radix)
        n_add += carry
        final.append(summed)

    # If there's a carry bigger than the answer length, add it on its own
    if carry != 0:
        final.append(carry)

    # Add sign and flip the number
    final.append(sign)
    final = final[::-1]
    
    return final, n_add, n_mult
    #ToDo: calculate count_mul
    #ToDo: calculate count_add


def modMultiply(radix, x, y, m):
    # reduce function doesn't work
    return 0

    # Reduce x and y
    x = reduce(radix, parseString(x), m)
    y = reduce(radix, parseString(y), m)

    # Multiply the numbers, then reduce mod m
    mult, n_add, n_mult = multiply({x: x, y: y, radix: radix})
    mult = reduce(mult, m)

    return toString(mult)


#This function multiplies 2 values using Karatsuba method
# for faster multiplication.
#Input:  radix: integer number between 2 and 16
#        x, y:  Strings for the two values to be multiplied (x*y)
#Output: result of the function as String (x*y)
def karatsuba(radix, x, y):
    if len(x) == 0 or len(y) == 0:
        return "invalid input data"
    answer = ""

    add_neg = 0
    if x[0] == "-":
        x = x[1:]
        add_neg = 1

    if y[0] == "-":
        y = y[1:]
        if add_neg == 1:
            add_neg = 0
        else:
            add_neg = 1

    if (len(x) == 1) or (len(y) == 1):
        answer = multiply(radix, x, y)
    else:
        m = max(len(x), len(y))
        split = m // 2

        # split x in 2 parts
        x_length = len(x) // 2
        x_mod    = len(x) % 2
        if x_mod == 1:
            x_length = x_length + 1
        x_hi = x[:x_length]
        x_lo = x[x_length:]

        # split y in 2 parts
        y_length = len(y) // 2
        y_mod    = len(y) % 2
        if y_mod == 1:
            y_length = y_length + 1
        y_hi = y[:y_length]
        y_lo = y[y_length:]

        # Xhi * Yhi
        step1_hi = karatsuba(radix, x_hi, y_hi)

        # Xlo * Ylo
        step2_lo = karatsuba(radix, x_lo, y_lo)

        # Xhi + Xlo
        step3_x = preAddition(radix, x_hi, x_lo)
        # Yhi + Ylo
        step3_y = preAddition(radix, y_hi, y_lo)
        # (Xhi + Xlo) * (Yhi + Ylo)
        step3_xy = multiply(radix, step3_x, step3_y)

        # (Xhi + Xlo) * (Yhi + Ylo) - Xhi * Yhi
        step4_xy_hi = preSubtract(radix, step3_xy, step1_hi)
        # found Xhi * Ylo + Xlo * Yhi = (Xhi + Xlo) * (Yhi + Ylo) - Xhi * Yhi - Xlo * Ylo
        step4_xy_hi_lo = preSubtract(radix, step4_xy_hi, step2_lo)

        # b^(m/2)
        mult_m_2 = 10 ** split
        # (Xhi * Ylo + Xlo * Yhi) * b^(m/2)
        step5_xy_hi_lo_m_2 = multiply(radix, step4_xy_hi_lo, str(mult_m_2))

        # b^m
        mult_m = mult_m_2 ** 2
        # Xhi * Yhi * b^m
        step6_hi_m = multiply(radix, step1_hi, str(mult_m))

        # Xhi * Yhi * b^m + (Xhi * Ylo + Xlo * Yhi) * b^(m/2)
        step7_add = preAddition(radix, step6_hi_m, step5_xy_hi_lo_m_2)
        # Xhi * Yhi * b^m + (Xhi * Ylo + Xlo * Yhi) * b^(m/2) + Xlo * Ylo
        answer = preAddition(radix, step7_add, step2_lo)

        if add_neg == 1:
            answer = "-" + answer
    return answer



def reduce(radix, x, m):
    while len(x) > len(m) or (len(x) == len(m) and cmpMagnitude(x, m)):
        diff = len(x) - len(m)
        m.insert(1,0)
        x = removePadding(subtract(radix, x, m + [0 for _ in range(diff - 1)]))
    return x

def QandR(radix, x, y):
    q = 0
    while len(x) > len(y) or (len(x) == len(y) and cmpMagnitude(x, y)):
        diff = len(x) - len(y)
        y.insert(1,0)
        x = removePadding(subtract(radix, x, y + [0 for _ in range(diff - 1)]))
        q += diff-1
    return q,x

def euclid(radix, x, y):
    axy = (1,0)
    bxy = (0,1)

    while True:
        q, r = QandR(radix, x, y)
        if r[1] == 0:
            return x, axy[1], bxy[1] # gcd, a, b
        y, x = x, r

        axy = axy[1], axy[0] - q * axy[1]
        bxy = bxy[1], bxy[0] - q * bxy[1]
    return


def inverse(radix, x, m):
  answer = 'ERROR - inverse does not exist'
  d, a, b = euclid(radix, parseString(x), parseString(m))
  print(d)
  if d != 1:
    answer = a
    print(a)
  return answer


# Loop over exercises and solve
for exercise in my_exercises['exercises']:
    operation = exercise[0]                # get operation type

    # clear global counters before each operation
    count_mul = 0
    count_add = 0

    # get parameters
    params = exercise[1]
    if 'x' in params:
        x = params['x']
    else:
        x = ''
    if 'y' in params:
        y = params['y']
    else:
        y = ''
    if 'm' in params:
        m = params['m']
    else:
        m = ''
    if 'radix' in params:
        radix = params['radix']
    else:
        radix = ''

    if operation == 'add':
        x, y = padArray(parseString(params["x"]), parseString(params["y"]))
        ans = (toString(removePadding(addition(radix, x, y))))
        #print(ans)
        params['answer'] = ans

    elif operation == 'mod-add':
        ### Do modular addition ###
        params['answer'] = modAdd(radix, x, y, m)

    elif operation == 'subtract':
        # Get x and y from the parameters and add padding so x and y are same length
        x, y = padArray(parseString(params["x"]), parseString(params["y"]))

        #Get answer from addition function and convert back to string and remove possible 0 padding
        ans = (toString(removePadding(subtract(radix, x, y))))
        #Put answer in output dictionary
        params['answer'] = ans

    elif operation == 'mod-subtract':
        ### Do mod-subtract algorithm ###
        params['answer'] = modSubtract(radix, x, y, m)

    elif operation == 'multiply':
        ### Do multiplication ###
        ans, n_add, n_mult = multiply(params)
        params['answer'] = toString(ans)
        # add calculated counters to the result
        params['count-mul'] = count_mul
        params['count-add'] = count_add

    elif operation == 'mod-multiply':
        ### Do multiplication ###
        params['answer'] = modMultiply(radix, x, y, m)

    elif operation == 'karatsuba':
        ### Do karatsuba algorithm ###
        params['answer'] = karatsuba(radix, x, y)
        # add calculated counters to the result
        params['count-mul'] = count_mul
        params['count-add'] = count_add

    elif operation == 'reduce':
        ### Do reduce algorithm ###
        params['answer'] = reduce(radix, x, m)

    elif operation == 'euclid':
        ### Do euclidean algorithm ###
        euclid(radix, x, y)
        # add calculated answers to the result
        params['answ-d'] = answ_d
        params['answ-a'] = answ_a
        params['answ-b'] = answ_b

    elif operation == 'inverse':
        ### Do inverse algorithm ###
        params['answer'] = inverse(radix, x, m)

    else:
        print("Invalid input: not supported operation in [", radix, "] = ", operation)

    # Save answer
    my_answers['exercises'].append({operation: params})


###### Creating an answers list file ######

# Save exercises with answers to file
my_file = open(ans_loc, 'wb+')                                       # write to binary file
my_file.write(json.dumps(my_answers).encode())                       # add encoded exercise list
my_file.close()
