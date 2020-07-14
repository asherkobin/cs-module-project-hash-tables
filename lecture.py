data = [None] * 10

def hashfn(s):
  total = 0
  for b in s.encode():
    total += b

  return total

def get_slot(s):
  hash_val = hashfn(s)
  return hash_val % len(data)

def put(key, value):
  slot = get_slot(key)
  data[slot] = value

def get(key):
  return data[get_slot(key)]

def delete(key):
  put(key, None)

# print(get_slot("Asher"))
# #print(get_slot("AsherKobin"))
# print(get_slot("KobinAsher"))
# #print(get_slot("Apple"))
# print(get_slot("apple"))
# #print(get_slot("bpple"))
# print(get_slot("ZZY"))
put("Asher", "Male")
put("Shirley", "Female")

print(data)

print(get("Asher"))

cache = {}
def fib(n):
  if n <= 1:
    return n

  if n not in cache:
    cache[n] = fib(n - 1) + fib(n - 2)

  return cache[n]

for i in range(20):
  print(f"{i:3} {fib(i)}")

# def expensive_function(x, y):
#   key = (x, y)

#   if key not in cache:
#     cache[key] = fn()

#   return cache[key]

# Inverse sqrt => inv_sqrt(x) = 1 / sqrt(x)
import math
inv_sqrt = {}

def build_lookup_table():
  for i in range(1, 1000):
    inv_sqrt[i] = 1 / math.sqrt(i)

build_lookup_table()

print(inv_sqrt[3])
print(inv_sqrt[12])

# sort a dictionary/hash table

d = {}
d["f"] = 12
d["a"] = 99
d["t"] = 4
d["z"] = 50

items = list(d.items())
print(items)

print(sorted(items))

items.sort(reverse=True)
print(items)

def get_key(t):
  return t[1]

#items.sort(key=get_key)

items.sort(key=lambda e: e[1])

print(items)

def print_letter_count(s):
  counts = {}

  for c in s:
    if c in counts:
      counts[c] += 1
    else:
      counts[c] = 1

  items = list(counts.items())
  items.sort(key=lambda e: e[1])

  print(items)



print_letter_count("aaaaabbbbbbcba")

encode_table = {
    'A': 'H',
    'B': 'Z',
    'C': 'Y',
    'D': 'W',
    'E': 'O',
    'F': 'R',
    'G': 'J',
    'H': 'D',
    'I': 'P',
    'J': 'T',
    'K': 'I',
    'L': 'G',
    'M': 'L',
    'N': 'C',
    'O': 'E',
    'P': 'X',
    'Q': 'K',
    'R': 'U',
    'S': 'N',
    'T': 'F',
    'U': 'A',
    'V': 'M',
    'W': 'B',
    'X': 'Q',
    'Y': 'V',
    'Z': 'S'
}

def encode(s):
  result = ""
  for c in s:
    if c in encode_table:
      result += encode_table[c]
    else:
      result += c
  return result

decode_table = {}

def build_decode_table():
  for k, v in encode_table.items():
    decode_table[v] = k

  # for key in encode_table:
  #   value = encode_table[k]

def decode(s):
  result = ""
  for c in s:
    if c in encode_table:
      result += decode_table[c]
    else:
      result += c
  return result

build_decode_table()
e = encode("@ASH!ER")
print(decode(e))

