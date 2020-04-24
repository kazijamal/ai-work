# ai-work

## Tuesday 03/10/20

### Moore's Law Pattern
- the pattern is self-reproducing

-------------------------------------------------------------------

## Monday 03/09/20

### Moore's Law
- Every year and a half to two years, the number of transistors in a processor doubles.
- created by Gordon Moore when observing integrated circuits and transistors
- correct for the past 45 years, but starting to reach its limit

### Transistors
- a mechanism by which decisions can be made
- can do amplification and decision-making
- engraved onto integrated circuits
- engineers found out how to make them smaller
- smaller transistors
  - require less energy to run
  - can be closer together so they can communicate with eachother faster
  - processing time decreases
  - cost per transistor decreases
  
-------------------------------------------------------------------

## Friday 02/14/20

### Premature optimization is the root of all evil.

### Dictionaries
- create a list of length N where N is prime and greater than the number of elements you have to store
    - this list is called a hash map
- use a hashing function on the element you wish to store and modulo by N to get an index in the list
- if two elements have the same hash there is a collision
    - one method of handling collision is putting the element in the slot following the hash
- O(1) element retrieval

-------------------------------------------------------------------

## Thursday 02/13/20

### Classes
```python
class Fred:

    def __init__(self):
        self.a = 5

    def q(self):
        self.t = 18
        self.n()

    def n():
        print(5)

w = Fred()
w.a = "Harry"
w.m = 35
```

-------------------------------------------------------------------

## Wednesday 02/12/20

### NP ?= P

-------------------------------------------------------------------

## Tuesday 02/11/20

### Classes

#### Creating Classes
```python
class Student:

    def __init__(self, in_name = 'Q', in_gpa = 2.7):
        self.name = in_name
        self.gpa = in_gpa
        self.ns = 18.7

    def inc(self, hm = 0.1):
        self.gpa += hm
```

#### Using Classes
```python
a = Student(in_gpa = 2.5)
print(a.gpa)
a.inc(48)
```

-------------------------------------------------------------------

## Monday 02/10/20

> Any sufficiently advanced technology is indistinguishable from magic - Arthur C. Clarke

-------------------------------------------------------------------

## Thursday 02/06/20

### Solution to Baseball Card Problem
for N cards, number of attempts is N times log base e of N

-------------------------------------------------------------------

## Friday 01/31/20

### String Review
- strings are immutable
```python
A = 'ABCDEFGHIJ'
A[0] # 'A'
C = A[1] + A[3] # 'AD'
D = A[1:4] # 'BCD'
E = A[-1] # 'J'
A[0] = 'Z' # error because strings are immutable
A = 'Z' + A[1:] # 'ZBCDEFGHIJ'
```

### List Review
- lists are heterogenous and can have multiple types
```python
P = [1, 5, 'A', [3,4]]
P = 'Z' + P[1:] # error because you can only concatenate lists with other lists
P = ['Z'] + P[1:] # ['Z', 5, 'A', [3,4]]
P[0] = 'Z' # ['Z', 5, 'A', [3,4]]
Q = P # Q is a reference to P
Q[0] = 45 # P will change because Q is a reference to P, they refer to the same list
Q = P + [] or Q = P[:] or Q = P.copy() # if Q is changed P will not change, Q is not a reference to P
```

### Dictionary Review
- any type that is immutable can be a key
- any type can be a value
- no order whatsoever
- getting a value provided a key can be done in O(1) time
- no searching involved due to hashmaps
```python
D['THALER, ALMA'] = [15, 3, 0] # { 'THALER, ALMA': [15, 3, 0] }
```

### random library
```python
import random
x = random.randint(1,9)
```

-------------------------------------------------------------------

## Thursday 01/30/20

### Cells
- cells can refer to variables or functions from other cells
- cells must be executed before referenced by other cells

-------------------------------------------------------------------

## Wednesday 01/29/20

### Jupyter Notebook
- development area working inside of the browser
- code executed within the browser
- the entire program structure is a Jupyter Notebook
- cells are within notebooks, and can be code or text (in markdown)
- can be used offline with files saved with IPYNB file extensions