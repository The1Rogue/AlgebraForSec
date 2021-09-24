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
    ex = {'add' : {'radix' : 10, 'x' : '-150', 'y' : '-6', 'answer' : ''}} # create add exercise
    exercises['exercises'].append(ex)                                   # add exercise to list


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
    #exercises['exercises'].append(ex)

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

def modAdd(radix, x, y, m):
    answer = ''
    return answer

def modSubtract(radix, x, y, m):
    answer = ''
    return answer

def multiply(radix, x, y):
    answer = ''
    #ToDo: calculate count_mul
    #ToDo: calculate count_add
    return answer

def modMultiply(radix, x, y, m):
    answer = ''
    return answer

def karatsuba(radix, x, y):
    answer = ''
    #ToDo: calculate count_mul
    #ToDo: calculate count_add
    return answer

def reduce(radix, x, m):

    while len(x) > len(m) or (len(x) == len(m) and cmpMagnitude(x, m)):
        diff = len(x) - len(m)
        x = subtract(radix, x, m + [0 for _ in range(diff - 1)])
    return x

def QandR(radix, x, y):
    q = 0
    while len(x) > len(y) or (len(x) == len(y) and cmpMagnitude(x, y)):
        diff = len(x) - len(y)
        x = subtract(radix, x, y + [0 for _ in range(diff - 1)])
        q += diff-1
    return q,x

def euclid(radix, x, y):
    axy = (1,0)
    bxy = (0,1)

    while True:
        q, r = QandR(radix, x, y)
        if r == 0:
            return x, axy[1], bxy[1] # gcd, a, b
        y, x = x, r

        axy = axy[1], axy[0] - q * axy[1]
        bxy = bxy[1], bxy[0] - q * bxy[1]


def inverse(radix, x, m):
    answer = ''
    return answer

#Assume two padded arrays enter and compare size without looking at sign
#Returns > if x>y, < if x<y and = if x=y
def cmpMagnitude(x, y):
  for i in range(1, len(x)):
    if x[i] > y[i]:
      return '>'
    if x[i] < y[i]:
      return '<'
  return '='

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

# Loop over exercises and solve
for exercise in my_exercises['exercises']:
    operation = exercise[0]                                        # get operation type
    params = exercise[1]                                           # get parameters
    answer = []

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
      print(ans)

      params['answer'] = ans
        
    elif operation == 'mod-add':
        ### Do modular addition ###
        params['answer'] = '1234'
    
    elif operation == 'subtract':
      # Get x and y from the parameters and add padding so x and y are same length
      x, y = padArray(parseString(params["x"]), parseString(params["y"]))
    
      #Get answer from addition function and convert back to string and remove possible 0 padding
      ans = (toString(removePadding(subtract(radix, x, y))))      
      #Put answer in output dictionary
      params['answer'] = ans

    elif operation == 'mod-subtract':
        ### Do euclidean algorithm ###
        params['answer'] = modSubtract(radix, x, y, m)

    elif operation == 'multiply':
        ### Do multiplication ###
        params['answer'] = multiply(radix, x, y)
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

