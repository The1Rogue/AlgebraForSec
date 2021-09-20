import asn1tools as asn
import json

### AfS software assignment 1 - example code ###

# set file names
base_location = './'
ops_loc = base_location + 'operations.asn'
exs_loc = base_location + 'my_exercises'
ans_loc = base_location + 'my_answers'

###### Creating an exercise list file ######

# How to create an exercise JSON file containing one addition exercise
exercises = {'exercises' : []}                                     # initialize empty exercise list
ex = {'add' : {'radix' : 10, 'x' : '-150', 'y' : '-6', 'answer' : ''}} # create add exercise
exercises['exercises'].append(ex)                                  # add exercise to list

# Encode exercise list and print to file
my_file = open(exs_loc, 'wb+')                                     # write to binary file
my_file.write(json.dumps(exercises).encode())                      # add encoded exercise list
my_file.close()

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

def padArray(x, y):
  print("Begin Padding")
  if (len(x) != len(y)):
    for i in range(max(len(x), len(y))+1):
      if len(x) < i:
        x.insert(1, 0)
      if len(y) < i:
        y.insert(1, 0)
  print(x, y)
  return x, y


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

def addition(r, x, y):
  answer = []
  carry = 0
  signx = True if x[0] == "neg" else False
  signy = True if y[0] == "neg" else False
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
    if signx:
      answer.insert(0, "neg")
    else:
      answer.insert(0, "pos")
  else:
    for i in range(len(x)-1, 0 ,-1):
      a = x[i]
      b = y[i]
      if a-b-carry < 0:
        ins = a-b-carry+r
        carry = 1
      else:
        ins = a-b-carry
        carry = 0
      answer.insert(0, ins)
    
  return answer

# Loop over exercises and solve
for exercise in my_exercises['exercises']:
    operation = exercise[0]                                        # get operation type
    params = exercise[1]                                           # get parameters
    answer = []
    radix = params['radix']

    if operation == 'add':
      x, y = padArray(parseString(params["x"]), parseString(params["y"]))
      ans = addition(radix, x, y)
      print(ans)

      # params['answer'] = toString(ans)
        
    if operation == 'mod-add':
        ### Do modular addition ###
        params['answer'] = '1234'
    
    if operation == 'subtract':
        ### Do subtraction ###
        params['answer'] = '-0'
        
    if operation == 'mod-substract':
        ### Do euclidean algorithm ###
        params['answ-d'] = '1'
        params['answ-a'] = '0'
        params['answ-b'] = '0'
        
    if operation == 'multiply':
        ### Do multiplication ###
        params['answer'] = '66'
        params['count-mul'] = '1'
        params['count-add'] = '2'

    if operation == 'mod-multiply':
        ### Do multiplication ###
        params['answer'] = '66'
        params['count-mul'] = '1'
        params['count-add'] = '2'        

    if operation == 'karatsuba':
        ### Do euclidean algorithm ###
        params['answ-d'] = '1'
        params['answ-a'] = '0'
        params['answ-b'] = '0'

    if operation == 'reduce':
        ### Do euclidean algorithm ###
        params['answ-d'] = '1'
        params['answ-a'] = '0'
        params['answ-b'] = '0'            

    if operation == 'euclid':
        ### Do euclidean algorithm ###
        params['answ-d'] = '1'
        params['answ-a'] = '0'
        params['answ-b'] = '0' 
        
    if operation == 'inverse':
        ### Do euclidean algorithm ###
        params['answ-d'] = '1'
        params['answ-a'] = '0'
        params['answ-b'] = '0'      

    # Save answer
    my_answers['exercises'].append({operation: params})

###### Creating an answers list file ######

# Save exercises with answers to file
my_file = open(ans_loc, 'wb+')                                       # write to binary file
my_file.write(json.dumps(my_answers).encode())                       # add encoded exercise list
my_file.close()

