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