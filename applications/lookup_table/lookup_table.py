import math
import random

lookup_table_pow = {}
lookup_table_factorial = {}
lookup_table_division = {}
lookup_table_mod = {}

def init_lookup_tables():
  for x in range(2, 14):
    for y in range(3, 6):
      lookup_table_pow[(x, y)] = math.pow(x, y)
  
  for x in range(2, 14):
    for y in range(3, 6):
      lookup_table_factorial[lookup_table_pow[(x, y)]] = math.factorial(lookup_table_pow[(x, y)])

def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    v = lookup_table_pow[(x, y)]
    v = lookup_table_factorial[v]
    v //= (x + y)
    v %= 982451653

    return v

print("Intializing Lookup Tables...")
init_lookup_tables()

# Do not modify below this line!

for i in range(2000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
