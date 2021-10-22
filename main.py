import asn1tools as asn
import json

### STUDENT PERSPECTIVE (example) ###

# Below code should behave like a black-box.
# That means that by clicking RUN (and, perhaps, changing the location of the exercise file), your output file should be generated.

base_location = './'
ops_loc = base_location + 'operations.asn'
exs_loc = base_location + 'input.ops'

# Compile specification
spec = asn.compile_files(ops_loc, codec = "jer")

def createTestEx():
  exercise = {'exercises':[]}
  ex = {'subtract-poly': {'mod': 5, "f": [1, 2, 3], 'g': [1, 2, 1]}}
  exercise['exercises'].append(ex)
  my_file = open(exs_loc, 'wb+')                                     # write to binary file
  my_file.write(json.dumps(exercise).encode())                      # add encoded exercise list
  my_file.close()
  return

#createTestEx()
# Read exercise list
exercise_file = open(exs_loc, 'rb') # open binary file
file_data = exercise_file.read() # read byte array
my_exercises = spec.decode('Exercises', file_data) # decode after specification
exercise_file.close() # close file


# Create answer JSON
my_answers = {'exercises': []}

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
    mod = subPoly([1]+[0 for _ in range(degMod)], polyMod, m)

    polyX = modPoly(polyX, m)
    degX = len(polyX)-1
    while degMod <= degX:
        x1 = multPoly([polyX[0]]+[0 for _ in range(degX-degMod)], mod, m)
        x0 = polyX[1:]
        polyX = addPoly(x0,x1,m)
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

def fieldAdd(polyA, polyB, modPoly, m):
  return polyModPoly(addPoly(polyA, polyB, m), modPoly, m)

def fieldSub(polyA, polyB, modPoly, m):
  polyB1 = [-1*polyB[i] for i in range(len(polyB))]
  return fieldAdd(polyA, polyB1, modPoly, m)

def fieldMult(polyA, polyB, modPoly, m):
  return polyModPoly(multPoly(polyA, polyB,m), modPoly, m)

# Loop over exercises and solve
for exercise in my_exercises['exercises']:
    operation = exercise[0] # get operation type
    params = exercise[1] # get parameters

    if operation == 'add-poly':
      ans = addPoly(params["f"], params["g"], params["mod"])
      # params['answer'] = displayPoly(ans)
      params["answer-poly"] = ans
        
    elif operation == 'subtract-poly':
      ans = subPoly(params["f"], params["g"], params["mod"])
      # params['answer'] = displayPoly(ans)
      print(ans)
      params["answer-poly"] = ans

    elif operation == 'multiply-poly':
        params["answer-poly"] = multPoly(params["f"], params["g"], params["mod"])

    elif operation == 'equals-poly-mod':
        params["answer"] = eqPolyMod(params["f"], params["g"], params["h"], params["mod"])
        print(params)

    elif operation == 'add-field':
        ans = fieldAdd(params['a'], params['b'], params['mod-poly'], params['mod'])
        # params['answer'] = displayPoly(ans)
        print(ans)
        params['answer-poly'] = ans
    
    elif operation == 'subtract-field':
        ans = fieldSub(params['a'], params['b'], params['mod-poly'], params['mod'])
        # params['answer'] = displayPoly(ans)
        print(ans)
        params['answer-poly'] = ans
    
    elif operation == 'multiply-field':
        ans = fieldMult(params['a'], params['b'], params['mod-poly'], params['mod'])
        # params['answer'] = displayPoly(ans)
        print(ans)
        params['answer-poly'] = ans
    
    elif operation == 'add-table':
        params['answer'] = ['X+1', '2X+1']
        params['answer-poly'] = [[1,1], [2,1]]

    # Save answer
    my_answers['exercises'].append({operation : params})

# Save exercises with answers to file
my_file = open(base_location + "output.ops", "wb+") # write to binary file
my_file.write(json.dumps(my_answers).encode()) # add encoded exercise list
my_file.close()
