import asn1tools as asn
import json
import random

### STUDENT PERSPECTIVE ###

# Below code should behave like a black-box.
# That means that by clicking RUN (and, perhaps, changing the location of the exercise file), your output file should be generated.

# set file names
base_location = './'
ops_loc = base_location + 'operations.asn'
exs_loc = base_location + 'input.ops'

###### Creating an exercise list file ######

# Create a JSON file containing exercises
def createExerciseJSONfile():
    exercises = {'exercises' : []}         # initialize empty exercise list

    # given exercises
    ex = {'display-poly' : {'mod': 7, 'f': [1,2,6], 'answer': 'X^2+2X+6', 'answer-poly':[1,2,6]}}
    exercises['exercises'].append(ex)

    ex = {'display-poly' : {'mod': 5, 'f': [1,2,6], 'answer': 'X^2+2X+1', 'answer-poly':[1,2,1]}}
    exercises['exercises'].append(ex)

    ex = {'display-poly' : {'mod': 7, 'f': [1,2,0], 'answer': 'X^2+2X', 'answer-poly':[1,2,0]}}
    exercises['exercises'].append(ex)

    ex = {'display-poly' : {'mod': 7, 'f': [1,2,7], 'answer': 'X^2+2X', 'answer-poly':[1,2,0]}}
    exercises['exercises'].append(ex)

    ex = {'display-poly' : {'mod': 7, 'f': [0,1,2,0], 'answer': 'X^2+2X', 'answer-poly':[1,2,0]}}
    exercises['exercises'].append(ex)

    ex = {'display-poly' : {'mod': 7, 'f': [-1,0,1,3], 'answer': '6X^3+X+3', 'answer-poly':[6,0,1,3]}}
    exercises['exercises'].append(ex)

    ex = {'display-poly' : {'mod': 7, 'f': [0,1,10,-1,0,2,3], 'answer': 'X^5+3X^4+6X^3+2X+3', 'answer-poly':[1,3,6,0,2,3]}}
    exercises['exercises'].append(ex)

    ex = {'display-poly' : {'mod': 7, 'f': [0], 'answer': '0', 'answer-poly':[0]}}
    exercises['exercises'].append(ex)

    ex = {'display-poly' : {'mod': 7, 'f': [0,0], 'answer': '0', 'answer-poly':[0]}}
    exercises['exercises'].append(ex)


    ex = {'subtract-poly': {'mod': 5, 'f': [1, 2, 3], 'g': [1, 2, 1]}}
    exercises['exercises'].append(ex)


    ex = {'irreducible' : {'mod': 2, 'f': [1,1,1], 'answer': True}}
    exercises['exercises'].append(ex)

    ex = {'irreducible' : {'mod': 3, 'f': [1,1,1], 'answer': False}}
    exercises['exercises'].append(ex)


    ex = {'find-irred' : {'mod': 2, 'deg': 3, 'answer': 'X^3+X+1', 'answer-poly':[1,0,1,1]}}
    exercises['exercises'].append(ex)

    ex = {'find-irred' : {'mod': 2, 'deg': 3, 'answer': 'X^3+X^2+1', 'answer-poly':[1,1,0,1]}}
    exercises['exercises'].append(ex)

    ex = {'find-irred' : {'mod': 2, 'deg': 4, 'answer': 'X^4+X+1', 'answer-poly':[1,0,0,1,1]}}
    exercises['exercises'].append(ex)


    ex = {'display-field' : {'mod': 5, 'mod-poly': [1,0,2], 'a': [1,1], 'answer': 'X+1', 'answer-poly':[1,1]}}
    exercises['exercises'].append(ex)

    ex = {'display-field' : {'mod': 5, 'mod-poly': [1,0,2], 'a': [1,0,0], 'answer': '3', 'answer-poly':[3]}}
    exercises['exercises'].append(ex)

    ex = {'display-field' : {'mod': 7, 'mod-poly': [2,-2], 'a': [1,1,1], 'answer': '3', 'answer-poly':[3]}}
    exercises['exercises'].append(ex)


    ex = {'add-table' : {'mod': 2, 'mod-poly':[1,1,1], 'answer':[['0','1','X','X+1'],['1','0','X+1','X'],['X','X+1','0','1'],['X+1','X','1','0']], 'answer-poly':[[[0],[1],[1,0],[1,1]],[[1],[0],[1,1],[1,0]],[[1,0],[1,1],[0],[1]],[[1,1],[1,0],[1],[0]]]}}
    exercises['exercises'].append(ex)

    ex = {'mult-table' : {'mod': 2, 'mod-poly':[1,1,1], 'answer':[['0','0','0','0'],['0','1','X','X+1'],['0','X','X+1','1'],['0','X+1','1','X']], 'answer-poly':[[[0],[0],[0],[0]],[[0],[1],[1,0],[1,1]],[[0],[1,0],[1,1],[1]],[[0],[1,1],[1],[1,0]]]}}
    exercises['exercises'].append(ex)

    ex = {'add-table' : {'mod': 7, 'mod-poly':[1,0], 'answer':[["0","1","2","3","4","5","6"],["1","2","3","4","5","6","0"],["2","3","4","5","6","0","1"],["3","4","5","6","0","1","2"],["4","5","6","0","1","2","3"],["5","6","0","1","2","3","4"],["6","0","1","2","3","4","5"]], 'answer-poly':[[[0],[1],[2],[3],[4],[5],[6]],[[1],[2],[3],[4],[5],[6],[0]],[[2],[3],[4],[5],[6],[0],[1]],[[3],[4],[5],[6],[0],[1],[2]],[[4],[5],[6],[0],[1],[2],[3]],[[5],[6],[0],[1],[2],[3],[4]],[[6],[0],[1],[2],[3],[4],[5]]]}}
    exercises['exercises'].append(ex)

    ex = {'mult-table' : {'mod': 7, 'mod-poly':[1,0], 'answer':[["0","0","0","0","0","0","0"],["0","1","2","3","4","5","6"],["0","2","4","6","1","3","5"],["0","3","6","2","5","1","4"],["0","4","1","5","2","6","3"],["0","5","3","1","6","4","2"],["0","6","5","4","3","2","1"]], 'answer-poly':[[[0],[0],[0],[0],[0],[0],[0]],[[0],[1],[2],[3],[4],[5],[6]],[[0],[2],[4],[6],[1],[3],[5]],[[0],[3],[6],[2],[5],[1],[4]],[[0],[4],[1],[5],[2],[6],[3]],[[0],[5],[3],[1],[6],[4],[2]],[[0],[6],[5],[4],[3],[2],[1]]]}}
    exercises['exercises'].append(ex)

    # Encode exercise list and print to file
    my_file = open(exs_loc, 'wb+')                          # write to binary file
    my_file.write(json.dumps(exercises, indent=2).encode()) # add encoded exercise list
    my_file.close()
    return

# call this function to create exercises-file with exercises included inside it
# or put it in comment to use existing exercises-file
#createExerciseJSONfile()


###### Using an exercise list file ######

# Compile specification
spec = asn.compile_files(ops_loc, codec = "jer")

# Read exercise list
exercise_file = open(exs_loc, 'rb')                # open binary file
file_data = exercise_file.read()                   # read byte array
my_exercises = spec.decode('Exercises', file_data) # decode after specification
exercise_file.close()                              # close file


###### Support functions ######

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
    x,y=padArray(x,y)
    for i in range(1, len(x)):
        if x[i] > y[i]:
            return '>'
        if x[i] < y[i]:
            return '<'
    return '='


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



###### Integer arithmetic ######

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
    y_1 = y[:]
    if y_1[0] == 'pos':
        y_1[0] = 'neg'
    else:
        y_1[0] = 'pos'
    return addition(r, x, y_1)

#Checks which addition case is the current exercise and adds elements in the array accordingly.
#Cases are: Both positive, both negative, both different sign
#In the first and second case we can just add all the elements with the primary school method
#In the third case we check which numbers magnitude is bigger and subtract the smaller from the larger and keep the larger's sign
def addition(r, x, y):
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
            answer.insert(0, ins)
        if cmp =='>':
            answer.insert(0, x[0])
        else:
            answer.insert(0, y[0])
    return answer

#Calls multiplication funciton, but before that
#turn 'x' and 'y' into lists
#Finally provide answer converted back to string with removed possible 0 padding.
#Input:  radix: integer number between 2 and 16
#        x, y:  Strings for the two values to be multiplied (x*y)
#Output: result of the function as String (x*y)
def preMultiply(radix, x, y):
    x, y = parseString(x), parseString(y)

    answer, n_add, n_mult = multiply(radix, x, y)

    #Get answer from multiplication function and convert back to string and remove possible 0 padding
    return (toString(removePadding(answer)))


def subUntil(num, divisor):
    count = 0
    while num >= divisor:
        num -= divisor
        count += 1
    return num, count


def multiply(radix, x, y):
    # Parse parameters
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


def reduce(radix, x, m):
    if x[0] == "neg":
        x[0] = "pos"
        x = reduce(radix, x, m)
        return subtract(radix, m, x)

    m2 = m.copy()
    m.insert(1, 0)

    while len(x) > len(m)-1 or (len(x) == len(m)-1 and cmpMagnitude(x, m2) != "<"):
        diff = len(x) - len(m)
        x = removePadding(subtract(radix, x, m + [0 for _ in range(diff)]))
    return x

#Calls reduce funciton, but before that
#turn 'x' and 'm' into lists
#Finally provide answer converted back to string with removed possible 0 padding.
#Input:  radix: integer number between 2 and 16
#        x, m:  Strings for the two values to be reduced
#Output: result of the function as String
def preReduce(x, m, radix = 10):
    x, m = parseString(x), parseString(m)

    answer = reduce(radix, x, m)

    #Get answer from reduce function and convert back to string and remove possible 0 padding
    return (toString(removePadding(answer)))



###### Polynomial arithmetic ######

# remove useless leading coefficients '0'
# input:  list with integer or string coefficients
# output: list with integer or string coefficients without leading '0'
def remove_leading_0_in_list(list):
    i = 0
    n = len(list) - 1
    while i < n:
        if list[i] == 0 or list[i] == "0":
            list.pop(i)
            n = n - 1
        else:
            break
    return list


# transfers list of integers/strings to a string of integers with separator ","
# input:  list of coefficients
# output: string with coefficients, separated with ","
#         in brackets "[ ... ]" like in the official inputs
def coeff_to_str(coeff):
    out = ""
    n = len(coeff)

    # coeff[0]   keeps coefficient in front of X^<polynomial deg>
    # coeff[n-1] keeps coefficient in front of X^0
    for i in range(n):
        # out[0]   keeps coefficient in front of X^<polynomial deg>
        # out[N-1] keeps coefficient in front of X^0
        out = out + "," + str(coeff[i])

    # remove leading useless comma ","
    if len(out) > 0:
        if out[0] == ",":
            out = out[1:]

    # add brackets "[ ... ]" like in the official inputs
    return "[" + out + "]"


# construct a polynomial
# input:  list with integer/string coefficients
# output: string of polynomial like a.x^3 + c.x + d
def coeffToPolynomial(coefficients):
    out = ""

    # remove useless leading coefficients '0'
    coefficients = remove_leading_0_in_list(coefficients)

    n = len(coefficients)
    if n > 0:

        # 'i' keeps the degree of 'x' for each member of the polynomial
        # coefficients[i] keeps the coefficient of each member of the polynomial
        # Example:          a.x^3 + 0.x^2 + c.x^1 + d.x^0
        #               i:  3       2       1       0
        # coefficients[i]:  a       0       c       d

        # start from free coefficient with degee "0" -> list item with number n-1
        # and finish with coefficient of the highest degree -> list item with number "0"
        for i in range (n-1, -1, -1):
            if coefficients[i] != "":

                ##group-step: prepare a.X^p
                # except when coefficient "a" is "0" like "0.X^p"
                if coefficients[i] != 0 and coefficients[i] != "0":

                    ##step: show "X" and degree "^p"
                    # add "X^p" except for the last coefficient where the degree is "0" like X^0"
                    if i != n-1:

                        ##1 sub-step: show degree "^p"
                        # add "^p" except for degree "1" like "^1"
                        if n-1-i != 1: # i != n-1-1
                            out = "^" + str(n-1-i) + out

                        ##2 sub-step: show variable "X" in front of the degree
                        out = "X" + out

                    ##step: show coefficient in front of "X"
                    if i == n-1: # when degree is "0"

                        # add even "1" for coefficient "d" (except "0")
                        out = str(coefficients[i]) + out

                    else: # for all other degrees != "0"

                        # add coefficient except useless value "1" (and also "0")
                        if coefficients[i] != 1 and coefficients[i] != "1":
                            out = str(coefficients[i]) + out

                ##step: show "+" in front of the group "a.X^p"
                # add "+" (if doesn't exist) in front ... except as first symbol of the complete expression
                if out != "" and out[0] != "+" and out[0] != "-" and i != 0:
                    out = "+" + out

        # finally remove useless first "+" if exists
        if len(out) > 2:
            if out[0] == "+":
                out = out[1:]

    # finally provide non-empty result polynomial string or "0" by default
    if out != "":
        return out
    else:
        return "0" # default in case of empty polynomial result string


# mod of polynomials
# input:  integer mod;
#         list with coefficients of polynomial 'f'
# output: list of strings for coefficients of polynomial f % mod
#         list of integers for coefficients of polynomial f % mod
def modPolyn(mod, f):
    out_str = []  # list of coefficients as strings
    out_int = []  # list of coefficients as integers

    f_len = len(f)
    if f_len > 0:
        for i in range(f_len):
            if f[i] != "":
                fi = preReduce(str(f[i]), str(mod))
                out_str.append(fi)
                # add an integer coefficient except for leading '0'
                if int(fi) != 0 or len(out_int) > 0:
                    out_int.append(int(fi))

    if len(out_int) == 0:
        # add an integer '0' if the integer coefficients list is empty
        out_int.append(0)

    return out_str, out_int


# display polynomial according to provided list of coefficients
# input:  integer mod
#         list with coefficients of polynomial 'f'
# output: string with result polynomial f % mod
def displayPoly(f, mod = 1):
    f_mod_str, f_mod_int = modPolyn(mod, f) # reduce input polynomials

    # prepare polynomial string from list of integers polynomial coefficients
    out = coeffToPolynomial(f_mod_int) # or call with (f_mod_str)

    return out, f_mod_int # like 'X^2+2X+6' , [1,2,6]


# This function uses the addition function to calculate the difference of two polynomials
# Input  : polyX, polyY: Two polynomials in the Poly object form with order < 256
#          m          : Integer < 100
# Returns: The difference of polyX and polyY mod m in Poly object form
def subPoly(polyX, polyY, m):
  polyY1 = [-1* polyY[i] for i in range(len(polyY))]

  return addPoly(polyX, polyY1, m)


# This function reduces some polynomial mod m and removes leading zeroes
# Input  : poly: some polynomial in the Poly object form with order < 256
#          m   : Integer < 100
# Returns: The Poly object of poly mod m
def modPoly(poly, m):
  ans = [x % m for x in poly]
  while(ans[0] == 0 and len(ans) > 1):
    ans.pop(0)
  return ans


# This function adds two polynomials and returns the result mod some integer
# Input  : polyX, polyY: Two polynomials in the Poly object form with order < 256
#          m          : Integer < 100
# Returns: Sum of (polyX, polyY) mod m
def addPoly(polyX, polyY, m):
  ans=[]
  sizeX = True if len(polyX) > len(polyY) else False
  for i in range(1, min(len(polyX), len(polyY))+1):
    ans.insert(0,polyX[-i]+polyY[-i])
  for i in range(min(len(polyX), len(polyY))+1, max(len(polyX), len(polyY))+1):
    if(sizeX):
      ans.insert(0,polyX[-i])
    else:
      ans.insert(0,polyY[-i])
  return modPoly(ans, m)


def multPoly(polyX, polyY, m):
    degX = len(polyX)-1
    degY = len(polyY)-1
    degOut = degX+degY
    out = [0 for _ in range(degOut+1)]

    for x in range(len(polyX)):
        for y in range(len(polyY)):
            i = (degX-x) + (degY-y)
            out[degOut-i] += (polyX[x] * polyY[y])
    out = modPoly(out, m)
    return out


def polyModPoly(polyX, polyMod, m):
    degMod = len(polyMod) - 1
    invLcm = inverseNum(polyMod[0], m)

    polyX = modPoly(polyX, m)
    degX = len(polyX)-1

    while degMod <= degX:
        lc = ((m - polyX[0]) * invLcm) % m
        x1 = multPoly([lc]+[0 for _ in range(degX-degMod)], polyMod, m)
        polyX = addPoly(polyX,x1,m)
        degX = len(polyX)-1

    return polyX


def eqPolyMod(polyX, polyY, polyMod, m):
    if polyMod != [0]:
        polyX = polyModPoly(polyX, polyMod, m)
        polyY = polyModPoly(polyY, polyMod, m)

    if len(polyX) != len(polyY):
        return False

    for i in range(len(polyX)):
        if polyX[i] != polyY[i]:
            return False
    return True


# Get the polynomial's degree
def degPoly(poly):
  return len(poly) - 1

# Get the leading coefficient
def lcPoly(poly):
  return poly[0]


# Get the inverse of a number
def inverseNum(num, m):
  gcd, inv = xgcdNum(num, m)
  inv = int(inv)

  # Numbers have to be coprime
  if gcd != 1:
    return "no inverse"

  # Make the inverse always positive
  if inv < 0:
    inv += m

  return inv


# Extended Euclidian algorithm returning gcd and x in ax + by = gcd
def xgcdNum(a, b):
  px, x = 1, 0

  # Stop when remainder hits 0
  while b > 0:
    # Calculate quotient
    q = (a - (a % b)) / b

    # Calculate x in ax + by = gcd
    x, px = px - q * x, x

    # a <- b, b <- remainder
    a, b = b, a%b
  return a, px


# Long division on polynomials
def longDivPoly(a, b, m):
  if a == [0] or b == [0]:
    return "ERROR", "ERROR"

  q = [0]
  r = a

  while degPoly(r) >= degPoly(b):
    degQ = degPoly(r) - degPoly(b)
    lcQ = lcPoly(r) * inverseNum(lcPoly(b), m)
    lcQ = lcQ % m

    # Calculate quotient
    tempQ = [0 for i in range(degQ+1)]
    tempQ[0] = lcQ
    q = addPoly(q, tempQ, m)

    # Calculate new remainder
    r = subPoly(r, multPoly(tempQ, b, m), m)

    if len(r) == 1 and r[0] == 0:
      break
  return q, r


def copyPoly(poly):
  return [poly[i] for i in range(len(poly))]


def xgcdPoly(a, b, m, normalize=True):
  x = [1]
  v = [1]
  y = [0]
  u = [0]

  # GCD is always one element if the other is 0
  # Norm this GCD to 1
  if a == [0]:
    norm = [inverseNum(lcPoly(a), m)]
    if isinstance(norm[0], str):
      return "ERROR", "", ""

    x = multPoly(x, norm, m)
    y = multPoly(y, norm, m)
    b = multPoly(b, norm, m)
    return b, x, y
  if b == [0]:
    norm = [inverseNum(lcPoly(b), m)]
    if isinstance(norm[0], str):
      return "ERROR", "", ""

    x = multPoly(x, norm, m)
    y = multPoly(y, norm, m)
    a = multPoly(a, norm, m)
    return a, x, y

  # Original a and b
  pa = copyPoly(a)
  pb = copyPoly(b)

  # While the remainder is not 0, calculate:
  while not (len(b) == 1 and b[0] == 0):
    q, r = longDivPoly(a, b, m)
    a = copyPoly(b)
    b = copyPoly(r)
    px = copyPoly(x)
    py = copyPoly(y)
    x = copyPoly(u)
    y = copyPoly(v)
    u = copyPoly(subPoly(px, multPoly(q, x, m), m))
    v = copyPoly(subPoly(py, multPoly(q, y, m), m))

  # If we don't have to normalise:
  if not normalize:
    return a, x, y

  # Calculate the norm factor
  lcGCD = lcPoly(a)
  invGCD = inverseNum(lcGCD, m)

  # Normalize x, y, and the gcd
  x = multPoly(x, [invGCD], m)
  y = multPoly(y, [invGCD], m)
  gcd = addPoly(multPoly(x, pa, m), multPoly(y, pb, m), m)
  return gcd, x, y


def isIrreducible(polyX, m):
  ans = True
  t = 1
  gcd = [1]
  while gcd == [1]:
    g = [1] + [0 for _ in range(m**t)]
    g[-2] = -1
    gcd = xgcdPoly(polyX, g, m)[0]
    t += 1
  if t == (len(polyX)-1) :
    ans = False
  return ans


# construct random irreducible polynomial based on provided mod and degree
# input:  integer mod and deg
# output: string with random polynomial of degree deg
def findIrred(mod, deg):
    out = ""
    count_constr = 0           # counts how many polynomials were constructed
    irreducible_found = False  # shows when constructed polynomial is ireducible

    while irreducible_found == False and count_constr <= 10:
        # count constructed polynomial
        count_constr += 1

        constr_int = []            # list with constructed polynomial coefficients
        for i in range(deg+1):
            if i == 0: # set coeff '1' for highest degree
                coeff = 1
            else: # choose random coeff (< mod) for smaller degrees
                if mod <= 0:   coeff = 0
                else:          coeff = random.randint(0, mod-1)
            constr_int.append(coeff)

        constr_str = coeff_to_str(constr_int);

        # check if constructed polynomial is irreducible
        irreducible_found = isIrreducible(constr_int, mod)
        if irreducible_found == True:
            print("Note: irreducible found, count_constr: " + str(count_constr))
            out = coeffToPolynomial(constr_int)
        else:
            # safety break
            if count_constr > 10:
                # don't try to find more irreducible polynomials
                out = "Break searching irreducible: " + constr_str + ", after " + str(count_constr) + " attempts"
                print(out)

    # prepare polynomial string from list of integers polynomial coefficients
    return out, constr_int



###### Finite field arithmetic ######

# add " around each item in the provided list of coefficients
# input:  list with coefficients as integers
# output: list with coefficients as strings
def addQuotesInList(r):
    answ = []
    for idx in r:
        answ.append(str(idx))
    return answ


# display field according to provided list of coefficients
# input:  integer mod;
#         list with coefficients of polynomial 'mod_poly' and 'a'
# output: string with result polynomial (a * b) % m_poly
def displayField(mod, m_poly, a):
    a_coeff_int = []  # list of integer coefficients
    a_coeff_str, a_coeff_int = modPolyn(mod, a) # reduce input polynomials
    q, r = longDivPoly(a_coeff_int, m_poly, mod)

    # function longDivPoly returns "ERROR" when division is not possible
    if q == "ERROR" or r == "ERROR":
        return "0", [0]
    else:
        # take 'r' after division
        return coeffToPolynomial(r), r


# Find multiplicative group of a field
# input:  integer mod
#         list with coefficients of polynomial 'mod_poly'
# output: list with strings of polynomials with separator ","
def MultGroup(mod, m_poly):
    m_poly = m_poly[1:]
    target_length = len(m_poly)

    answ = []
    # from 0 through mod-1 are in the multiplicative group
    for i in range(int(mod)):
        entry = []
        for j in range(target_length-1):
            entry.append(0)
        entry.append(i)
        answ.append(entry)

    # making the rest using the intrinsic binary property of the multiplicative group
    for i in range(2, 2**target_length):

        combo = bin(i)[2:]

        while len(combo) < target_length:
            combo = "0" + combo

        element = []
        #element is indexable
        for i in range(target_length):
            element.append(-1)

        #make the element by multiplying with input
        for j in range(target_length):
            element[j] = int(preMultiply(10, str(m_poly[j]), combo[j]))
        answ.append(element)

    #remove duplicates and unnecesarry items
    remove = []
    for i in range(len(answ)):
        for j in range(i+1, len(answ)):
            if answ[i] == answ[j]:
                remove.append(j)

    remove = list(dict.fromkeys(remove))
    remove.sort(reverse = True)

    for idx in remove:
        answ.pop(idx)
    return answ


def fieldAdd(polyA, polyB, modPoly, m):
  return polyModPoly(addPoly(polyA, polyB, m), modPoly, m)

def fieldSub(polyA, polyB, modPoly, m):
  polyB1 = [-1*polyB[i] for i in range(len(polyB))]
  return fieldAdd(polyA, polyB1, modPoly, m)

def fieldMult(polyA, polyB, modPoly, m):
  return polyModPoly(multPoly(polyA, polyB,m), modPoly, m)


# Get inverse element in a field
def inverseField(elem, mod, polyMod):
  gcd, x, y = xgcdPoly(elem, polyMod, mod, False)
  if len(gcd) == 1 and gcd[0] == 1:
    return x
  return "ERROR"


def polyPower(a, pow, polyMod, mod):
    result = [1]
    while pow > 0:
        if pow%2 == 1:
            result = multPoly(result, a, mod)
            pow -= 1
        pow //= 2
        a = multPoly(a, a, mod)

    return polyModPoly(result, polyMod, mod)


def isPrimitive(a, mod, polyMod):
    q = mod**(len(polyMod)-1)
    with open("primes.json") as f:
        primes = json.loads(f.read())
    f.close()

    for p in primes:
        if (q-1)%p == 0 and polyPower(a, (q-1)//p, polyMod, mod) == [1]:
            return False

        if p > q**.5:
            return True


def fieldDiv(a, b, mod, polyMod):
    result = [0]
    invLcb = inverseNum(b[0], mod)
    while a != [0]:
        if len(b) <= len(a):
            tmp = [a[0] * invLcb] + [0 for _ in range(len(a) - len(b))]
            result = addPoly( tmp , result, mod)
            a = subPoly(a, multPoly(tmp, b, mod), mod)
        else:
            a = addPoly(a, polyMod, mod)

    return polyModPoly(result, polyMod, mod)


# Return a field element
def getElem(mod, polyMod, offset=0):
  num = offset
  elem = []
  while offset != 0:
    q = offset // mod
    r = offset - q * mod
    offset = q
    elem.append(r)

  if len(elem) == 0:
    elem = [0]
  else:
    elem = list(reversed(elem))

  elem = polyModPoly(elem, polyMod, mod)
  return elem


# Return a primitive element in the field
def findPrim(mod, polyMod):
  i = 1
  while i < 10000:
    elem = getElem(mod, polyMod, i)

    if not isinstance(elem, str):
      if isPrimitive(elem, mod, polyMod):
        return elem

    i += 1

  return "ERROR"


# Make addition table of the field
# input:  integer mod
#         list with coefficients of polynomial 'mod_poly'
# output: list with strings of polynomials with separator ","
def addTable(mod, m_poly):
    #elements of multiplicative group are the indices
    idx = MultGroup(mod, m_poly)

    #make table using nested lists for now
    cols = []
    for i in idx:
        row = []
        for j in idx:
            row.append(addPoly(i, j, mod))
        cols.append(row)

    table = cols
    #construct the answer using the table
    answer = []
    answer_poly = []
    for rows in table:

        #construct the answer row
        answer_el = []
        answer_coeff = []
        for cols in rows:

            #construct the items in a row
            items = []
            for item in cols:
                items.append(item)
            element, coeff = displayField(mod, m_poly, items)
            answer_coeff.append(coeff)
            answer_el.append(element)

        answer.append(answer_el)
        answer_poly.append(answer_coeff)

    return answer, answer_poly


# Make multiplication table of the field
# item to add_table using multPoly instead of addPoly
# input:  integer mod
#         list with coefficients of polynomial 'mod_poly'
# output: list with strings of polynomials with separator ","
def multTable(mod, m_poly):
    #elements of multiplicative group are the indices
    idx = MultGroup(mod, m_poly)

    #make table using nested lists for now
    cols = []
    for i in idx:
        row = []
        for j in idx:
            row.append(multPoly(i, j, mod))
        cols.append(row)

    table = cols
    #construct the answer using the table
    answer = []
    answer_poly = []
    for rows in table:

        #construct the answer row
        answer_el = []
        answer_coeff = []
        for cols in rows:

            #construct the items in a row
            items = []
            for item in cols:
                items.append(item)
            element, coeff = displayField(mod, m_poly, items)
            answer_coeff.append(coeff)
            answer_el.append(element)

        answer.append(answer_el)
        answer_poly.append(answer_coeff)

    return answer, answer_poly



###### Loop over exercises and solve ######

# Create answer JSON
my_answers = {'exercises': []}

# Loop over exercises and solve
for exercise in my_exercises['exercises']:
    operation = exercise[0] # get operation type

    # get parameters
    params = exercise[1]
    if 'mod' in params:
        mod = params['mod']
    else:
        mod = ''
    if 'deg' in params:
        deg = params['deg']
    else:
        deg = ''
    if 'f' in params:
        f = params['f']
    else:
        f = ''
    if 'g' in params:
        g = params['g']
    else:
        g = ''
    if 'h' in params:
        h = params['h']
    else:
        h = ''
    if 'mod-poly' in params:
        mod_poly = params['mod-poly']
    else:
        mod_poly = ''
    if 'a' in params:
        a = params['a']
    else:
        a = ''
    if 'b' in params:
        b = params['b']
    else:
        b = ''

    #initialize answer variables
    if 'answer' in params:
        params['answer'] = ""
    if 'answ-q' in params:
        params['answ-q'] = ""
    if 'answ-r' in params:
        params['answ-r'] = ""
    if 'answ-a' in params:
        params['answ-a'] = ""
    if 'answ-b' in params:
        params['answ-b'] = ""
    if 'answ-d' in params:
        params['answ-d'] = ""
    if 'answer-poly' in params:
        params['answer-poly'] = []
    if 'answ-a-poly' in params:
        params['answ-a-poly'] = []
    if 'answ-b-poly' in params:
        params['answ-b-poly'] = []
    if 'answ-d-poly' in params:
        params['answ-d-poly'] = []
    if 'answ-q-poly' in params:
        params['answ-q-poly'] = []
    if 'answ-r-poly' in params:
        params['answ-r-poly'] = []

    if operation == 'display-poly':
        params['answer'], params['answer-poly'] = displayPoly(f, mod)

    elif operation == 'display-field':
        params['answer'], params['answer-poly'] = displayField(mod, mod_poly, a)

    elif operation == 'add-poly':
        coeff = addPoly(params['f'], params['g'], params['mod'])
        params['answer-poly'] = coeff
        params['answer'] = coeffToPolynomial(coeff)

    elif operation == 'subtract-poly':
        coeff = subPoly(params['f'], params['g'], params['mod'])
        params['answer-poly'] = coeff
        params['answer'] = coeffToPolynomial(coeff)

    elif operation == 'multiply-poly':
        coeff = multPoly(params['f'], params['g'], params['mod'])
        params['answer-poly'] = coeff
        params['answer'] = coeffToPolynomial(coeff)

    elif operation == 'equals-poly-mod':
        params['answer'] = eqPolyMod(params['f'], params['g'], params['h'], params['mod'])

    elif operation == 'long-div-poly':
        polyQ, polyR = longDivPoly(params['f'], params['g'], params['mod'])
        if not isinstance(polyQ, str):
            params['answ-q-poly'] = polyQ
            params['answ-q'] = coeffToPolynomial(polyQ)
        else: #ERROR
            params['answ-q-poly'] = []
            params['answ-q'] = polyQ

        if not isinstance(polyR, str):
            params['answ-r-poly'] = polyR
            params['answ-r'] = coeffToPolynomial(polyR)
        else: #ERROR
            params['answ-r-poly'] = []
            params['answ-r'] = polyR

    elif operation == 'euclid-poly':
        gcd, x, y = xgcdPoly(params['f'], params['g'], params['mod'])
        if not isinstance(gcd, str):
            params['answ-a-poly'] = x
            params['answ-b-poly'] = y
            params['answ-d-poly'] = gcd
            params['answ-a'] = coeffToPolynomial(x)
            params['answ-b'] = coeffToPolynomial(y)
            params['answ-d'] = coeffToPolynomial(gcd)
        #else #ERROR

    elif operation == 'irreducible':
      params['answer'] = isIrreducible(params['f'], params['mod'])

    elif operation == 'find-irred':
        params['answer'], params['answer-poly'] = findIrred(mod, deg)

    elif operation == 'add-table':
        params['answer'], params['answer-poly'] = addTable(mod, mod_poly)

    elif operation == 'mult-table':
        params['answer'], params['answer-poly'] = multTable(mod, mod_poly)

    elif operation == 'add-field':
        coeff = fieldAdd(params['a'], params['b'], params['mod-poly'], params['mod'])
        params['answer-poly'] = coeff
        params['answer'] = coeffToPolynomial(coeff)

    elif operation == 'subtract-field':
        coeff = fieldSub(params['a'], params['b'], params['mod-poly'], params['mod'])
        params['answer-poly'] = coeff
        params['answer'] = coeffToPolynomial(coeff)

    elif operation == 'multiply-field':
        coeff = fieldMult(params['a'], params['b'], params['mod-poly'], params['mod'])
        params['answer-poly'] = coeff
        params['answer'] = coeffToPolynomial(coeff)

    elif operation == 'equals-field':
        ans = eqPolyMod(params['a'], params['b'], params['mod-poly'], params['mod'])
        params['answer'] = ans

    elif operation == 'inverse-field':
        coeff = inverseField(params['a'], params['mod'], params['mod-poly'])
        if not isinstance(coeff, str):
            params['answer-poly'] = coeff
            params['answer'] = coeffToPolynomial(coeff)
        else: #ERROR
            params['answer-poly'] = []
            params['answer'] = coeff

    elif operation == 'division-field':
        if params['b'] != [0]:
            coeff = fieldDiv(params['a'], params['b'], params['mod'], params['mod-poly'])
            params['answer-poly'] = coeff
            params['answer'] = coeffToPolynomial(coeff)
        else: #ERROR
            params['answer-poly'] = []
            params['answer'] = "ERROR"

    elif operation == 'find-prim':
        coeff = findPrim(params['mod'], params['mod-poly'])
        if not isinstance(coeff, str):
            params['answer-poly'] = coeff
            params['answer'] = coeffToPolynomial(coeff)
        else: #ERROR
            params['answer'] = "ERROR"
            params['answer-poly'] = []

    elif operation == 'primitive':
        params['answer'] = isPrimitive(params['a'], params['mod'], params['mod-poly'])

    else:
        params['answer'] = "Not supported operation '" + operation + "'"

    # Save answer
    my_answers['exercises'].append({operation : params})


###### Creating an output list file ######

# Save exercises with answers to file
my_file = open(base_location + "output.ops", "wb+") # write to binary file
my_file.write(json.dumps(my_answers, indent=2).encode())      # add encoded exercise list
my_file.close()
