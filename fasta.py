def getStrings(file_name):
  f = open(file_name, 'r')
  cur_name = ""
  cur_string = ""
  d = dict()
  for line in f:
    if line.startswith('>'):
      if len(cur_string) > 0:
	d[cur_name] = cur_string
      cur_name = line[1:-1]
      cur_string = ""
    else :
      cur_string += line.strip()
  d[cur_name] = cur_string
  return d

