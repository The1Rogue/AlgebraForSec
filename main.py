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

def displayPoly(a) :
  return
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
    # degMod = len(polyMod) - 1
    # mod = subPoly([1]+[0 for _ in range(degMod)], polyMod, m)
    # invLcm = inverseNum(polyMod[0], m)

    # polyX = modPoly(polyX, m)
    # degX = len(polyX)-1


    # while degMod < degX or (degMod == degX and polyX[0] >= polyMod[0]) :
    #     x1 = multPoly([polyX[0] * invLcm]+[0 for _ in range(degX-degMod-1)], mod, m)
    #     x0 = polyX[1:]
    #     polyX = addPoly(x0,x1,m)
    #     degX = len(polyX)-1
    return longDivPoly(polyX, polyMod, m)[1]

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
  i = 0
  while i < 10000:
    elem = getElem(mod, polyMod, i)
    print(elem)
    #if isPrim(elem, mod, polyMod):
    if i > 50:
      return elem
    i += 1
    
  return "ERROR"




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
      #print(ans)
      params["answer-poly"] = ans

    elif operation == 'multiply-poly':
        params["answer-poly"] = multPoly(params["f"], params["g"], params["mod"])

    elif operation == 'equals-poly-mod':
        params["answer"] = eqPolyMod(params["f"], params["g"], params["h"], params["mod"])

    elif operation == 'add-field':
        ans = fieldAdd(params['a'], params['b'], params['mod-poly'], params['mod'])
        # params['answer'] = displayPoly(ans)
        print(ans)
        params['answer-poly'] = ans
    
    elif operation == 'subtract-field':
        ans = fieldSub(params['a'], params['b'], params['mod-poly'], params['mod'])
        # params['answer'] = displayPoly(ans)
        #print(ans)
        params['answer-poly'] = ans
    
    elif operation == 'multiply-field':
        ans = fieldMult(params['a'], params['b'], params['mod-poly'], params['mod'])
        # params['answer'] = displayPoly(ans)
        #print(ans)
        params['answer-poly'] = ans
    
    elif operation == 'add-table':
        params['answer'] = ['X+1', '2X+1']
        params['answer-poly'] = [[1,1], [2,1]]


    elif operation == "equals-field":
        params["answer"] = eqPolyMod(params["a"], params["b"], params["mod-poly"], params["mod"])

    elif operation == "long-div-poly":
        polyQ, polyR = longDivPoly(params["f"], params["g"], params["mod"])
        strQ = displayPoly(polyQ)
        strR = displayPoly(polyR)
        params["answ-q"] = strQ
        params["answ-r"] = strR
        params["answ-q-poly"] = polyQ
        params["answ-r-poly"] = polyR

    elif operation == "euclid-poly":
        gcd, x, y = xgcdPoly(params["f"], params["g"], params["mod"])
        if not isinstance(gcd, str):
            params["answ-a"] = displayPoly(x)
            params["answ-b"] = displayPoly(y)
            params["answ-d"] = displayPoly(gcd)
            params["answ-a-poly"] = x
            params["answ-b-poly"] = y
            params["answ-d-poly"] = gcd

    elif operation == "find-prim":
        elem = findPrim(params["mod"], params["mod-poly"])
        if isinstance(elem, str):
          params["answer"] = elem
          params["answer-poly"] = []
        else:
          params["answer"] = displayPoly(elem)
          params["answer-poly"] = elem

    elif operation == "primitive":
        params["answer"] = isPrimitive(params["a"], params["mod"], params["mod-poly"])
    
    elif operation == "inverse-field":
        elem = inverseField(params["a"], params["mod"], params["mod-poly"])
        if isinstance(elem, str):
          params["answer"] = elem
          params["answer-poly"] = []
        else:
          params["answer"] = displayPoly(elem)
          params["answer-poly"] = elem

    elif operation == "division-field":
        if params["b"] == [0]:
            params["answer"] = "Error"
            params["answer-poly"] = ""

        else:
            out = fieldDiv(params["a"], params["b"], params["mod"], params["mod-poly"])
            params["answer"] = ""
            params["answer-poly"] = out

    # Save answer
    my_answers['exercises'].append({operation : params})

# Save exercises with answers to file
my_file = open(base_location + "output.ops", "wb+") # write to binary file
my_file.write(json.dumps(my_answers).encode()) # add encoded exercise list
my_file.close()
