#functin for finding permutation
def all_perms(str):
    if len(str) <= 1:
        yield str
    else:
        for perm in all_perms(str[1:]):
            for i in range(len(perm)+1):
                #nb str[0:1] works in both string and list contexts
                yield perm[:i] + str[0:1] + perm[i:]

#Open a Csv file
for line in open('ile.csv'):
  #read data line by line
  for item in all_perms(line[:-1]):
    print(item)