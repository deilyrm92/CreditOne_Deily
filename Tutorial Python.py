#!/usr/bin/env python
# coding: utf-8

# Sección 2
# 2.1.2 Interactive Mode

# In[2]:


the_world_is_flat = True
if the_world_is_flat:
    print("Be careful not to fall off!")


# 2.2 The Interpreter and its Enviroment
# 2.2.1 Sorce Code Enconding

# In[3]:


# -*- coding: encoding -*-


# In[4]:


# -*- coding: cp1252 -*-
# Declare Windows 1252


# In[5]:


#!/usr/bin/env python3
# -*- coding: cp1252 -*-


# Sección 3

# In[6]:


# this is the first comment
spam = 1  # and this is the second comment
          # ... and now a third!
text = "# This is not a comment because it's inside quotes."


# In[7]:


spam


# In[8]:


text


# 3.1 Usand Python como calculadora
# 3.1.1 Numeros

# In[9]:


2 + 2


# In[10]:


50 - 5*6


# In[11]:


(50 - 5*6) / 4


# In[12]:


8 / 5  # division always returns a floating point number


# Float

# In[13]:


17 / 3  # classic division returns a float


# In[14]:


17 // 3  # floor division discards the fractional part


# In[15]:


17 % 3  # the % operator returns the remainder of the division


# In[16]:


5 * 3 + 2  # result * divisor + remainder


# Potencias

# In[17]:


5 ** 2  # 5 squared


# In[18]:


2 ** 7  # 2 to the power of 7


# uso del =

# In[19]:


width = 20


# In[20]:


height = 5 * 9


# In[21]:


width * height


# Variables no definidas

# In[22]:


n  # try to access an undefined variable


# Uso de Operaciones Mixtas (int FLoat)

# In[ ]:


4 * 3.75 - 1


# Uso de variable _ (Utiliza el ultimo valor impreso)

# In[ ]:


tax = 12.5 / 100


# In[ ]:


price = 100.50


# In[ ]:


price * tax


# In[ ]:


price + _


# In[ ]:


round(_, 2)


# 3.1.2 Strings

# In[ ]:


'spam eggs'  # single quotes


# In[ ]:


'doesn\'t'  # use \' to escape the single quote...


# In[ ]:


"doesn't"  # ...or use double quotes instead


# In[ ]:


'"Yes," they said.'


# In[ ]:


"\"Yes,\" they said."


# In[ ]:


'"Isn\'t," they said.'


# Las comillas simples y caracteres especiales no se imprimen por lo que se debe usar print()

# In[ ]:


'"Isn\'t," they said.'


# In[ ]:


print('"Isn\'t," they said.')


# In[ ]:


s = 'First line.\nSecond line.'  # \n means newline


# In[ ]:


s  # without print(), \n is included in the output
'First line.\nSecond line.'


# In[ ]:


print(s)

Agregando la r en el Print, utiliza la cadena sin procesar \n
# In[23]:


print('C:\some\name')


# In[24]:


print(r'C:\some\name')


# In[25]:


Varias lineas separando cada una con comillas triples y 


# In[ ]:


print("""Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")


# Concatenar

# In[ ]:


# 3 times 'un', followed by 'ium'


# In[ ]:


3 * 'un' + 'ium' 


# In[ ]:


'Py' 'thon'


# Romper Cadenas Largas

# In[ ]:


text = ('Put several strings within parentheses '
        'to have them joined together.') 


# In[ ]:


text


# In[ ]:


prefix = 'Py'


# Sin embargo cuando se incluyen variables no funciona para romper la cadena.

# In[ ]:


prefix 'thon'  # can't concatenate a variable and a string literal


# In[26]:


Se debe concatenar con +


# In[ ]:


prefix + 'thon'


# Ventores en los String

# In[ ]:


word = 'Python'


# In[ ]:


word[0]  # character in position 0


# In[ ]:


word[5]  # character in position 5


# In[ ]:


word[-1]  # last character


# In[ ]:


word[-2]  # second-last character


# In[ ]:


word[-6]


# In[ ]:


word[0:2]  # characters from position 0 (included) to 2 (excluded)


# In[ ]:


word[2:5]  # characters from position 2 (included) to 5 (excluded)


# In[ ]:


word[:2] + word[2:]


# In[ ]:


word[:4] + word[4:]


# In[ ]:


word[:2]   # character from the beginning to position 2 (excluded)


# In[ ]:


word[4:]   # characters from position 4 (included) to the end


# In[ ]:


word[-2:]  # characters from the second-last (included) to the end


# Resumen de los vectores en los String para valores positivos o negativos
# +---+---+---+---+---+---+
#  | P | y | t | h | o | n |
#  +---+---+---+---+---+---+
#  0   1   2   3   4   5   6
# -6  -5  -4  -3  -2  -1

# In[ ]:


word[42]  # the word only has 6 character


# In[ ]:


word[4:42]


# In[ ]:


word[42:]


# In[27]:


word[0] = 'J' # Las posiciones en los ventores no pueden ser modificadas


# In[ ]:


word[2:] = 'py'


# In[ ]:


'J' + word[1:] # Se debera crear una nueva


# In[ ]:


word[:2] + 'py'


# In[ ]:


Contar los valores de una cadena


# In[ ]:


s = 'supercalifragilisticexpialidocious'


# In[ ]:


len(s)


# 3.1.3 Listas

# In[ ]:


squares = [1, 4, 9, 16, 25]


# In[ ]:


squares


# In[ ]:


squares[0]  # indexing returns the item


# In[ ]:


squares[-1]


# In[ ]:


squares[-3:]  # slicing returns a new list


# In[ ]:


squares[:]


# In[ ]:


squares + [36, 49, 64, 81, 100]


# In[ ]:


cubes = [1, 8, 27, 65, 125]  # something's wrong here


# In[ ]:


4 ** 3  # the cube of 4 is 64, not 65!


# In[ ]:


cubes[3] = 64  # replace the wrong value


# In[ ]:


cubes


# In[ ]:


cubes.append(216)  # add the cube of 6


# In[ ]:


cubes.append(7 ** 3)  # and the cube of 7


# In[ ]:


cubes


# In[28]:


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']


# In[29]:


letters


# In[30]:


# replace some values
letters[2:5] = ['C', 'D', 'E']


# In[31]:


letters


# In[32]:


# now remove them
letters[2:5] = []
letters


# In[33]:


# clear the list by replacing all the elements with an empty list
letters[:] = []
letters


# In[34]:


letters = ['a', 'b', 'c', 'd']
len(letters)


# In[35]:


a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
x


# In[36]:


x[0]


# In[37]:


x[0][1]


# 3.2 Primeros Pasos hacia la Programación

# In[38]:


# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b


# In[39]:


i = 256*256
print('The value of i is', i)


# In[40]:


a, b = 0, 1
while a < 1000:
    print(a, end=',')
    a, b = b, a+b


# 4 Mas Herramientas de control de flujo

# 4.1 If Declaraciones

# In[41]:


x = int(input("Please enter an integer: "))
#Please enter an integer: 42
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')


# 4.2 For Declaraciones

# In[ ]:


# Measure some strings:
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))


# In[ ]:


# Strategy:  Iterate over a copy
users = ['Deily', 'Stacy', 'Jaz']
users.items = ['Deily', 'Stacy', 'Jaz']
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]


# In[ ]:


# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status


# In[ ]:





# In[ ]:


for i in range(5,10):
    print(i)


# In[ ]:


for i in range(0,10,3):
    print(i)


# In[ ]:


for i in range(-10,-100,-30):
    print(i)


# In[ ]:


a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])


# In[ ]:


print(range(10)) # se debe imprimir con el for


# In[ ]:


sum(range(4))  # 0 + 1 + 2 + 3


# In[ ]:


list(range(4))


# 4.4 Break and continue declaraciones y else para salida de bucles

# In[ ]:


for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')


# In[ ]:


for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found a number", num)


# 4.5 Pass

# In[ ]:


while True:
    pass  # Busy-wait for keyboard interrupt (Ctrl+C)


# In[ ]:


class MyEmptyClass:
    pass


# In[ ]:


def initlog(*args):
    pass   # Remember to implement this!


# 4.6. Definiendo funciones

# In[62]:


def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


# In[48]:


# Now call the function we just defined:
fib(2000) 


# In[44]:


fib
#<function fib at 10042ed0>
f = fib
f(100)


# In[42]:


fib(0)
print(fib(0))


# In[64]:


def fib2(n):  # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)    # see below
        a, b = b, a+b
    return result

f100 = fib2(100)    # call it
f100                # write the result


# 4.7. Más sobre la definición de funciones

# 4.7.1. Valores de argumento predeterminados

# In[79]:


def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)


# In[80]:


i = 5

def f(arg=i):
    print(arg)

i = 6
f()


# In[82]:


def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))


# In[83]:


def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L


# 4.7.2. Argumentos de palabras clave

# In[84]:


def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


# In[85]:


parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword


# LLamados invali

# In[86]:


parrot()                     # required argument missing
parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
parrot(110, voltage=220)     # duplicate value for the same argument
parrot(actor='John Cleese')  # unknown keyword argument


# In[87]:


def function(a):
    pass

function(0, a=0)


# In[88]:


def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


# In[89]:


cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

4.7.3. Parámetros especiales

def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
      -----------    ----------     ----------
        |             |                  |
        |        Positional or keyword   |
        |                                - Keyword only
         -- Positional only
# 4.7.3.4. Ejemplos de funciones

# In[107]:


def standard_arg(arg):
    print(arg)

def standard_arg(arg):
    print(arg)

def pos_only_arg(arg,/):
    print(arg)

def kwd_only_arg(*, arg):
    print(arg)

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)


# In[105]:


standard_arg(2)


# In[96]:


standard_arg(arg=2)


# In[97]:


pos_only_arg(1)


# In[ ]:





# In[ ]:





# In[ ]:



