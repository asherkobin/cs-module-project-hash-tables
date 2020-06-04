def word_count(s):
  bad_chars = "\":;,.-+=/\|[]{}()*^&]"
  words = {}

  ##
  ## It would be faster to increment along the string
  ## and make decisions on the current character
  ##

  # python remvoal of characters
  s = s.translate(s.maketrans("", "", bad_chars)).lower()

  if len(s) == 0:
    return {}
  
  # trim whitespace
  new_s = ""
  saw_ws = True
  ws_chars = [" ", "\t", "\r", "\n"]
  for c in s:
    if c in ws_chars:
      if not saw_ws:
        new_s += " "
        saw_ws = True
    else:
      new_s += c
      saw_ws = False
  if new_s[-1:] == " ": # trim trailing whitespace
    new_s = new_s[:-1]

  split_str = new_s.split(" ")
  
  for word in split_str:
    if word not in words:
      words[word] = 1
    else:
      words[word] += 1
  
  return words


if __name__ == "__main__":
  print(word_count(""))
  print(word_count("Hello"))
  print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
  print(word_count('This is a test of the emergency broadcast network. This is only a test.'))