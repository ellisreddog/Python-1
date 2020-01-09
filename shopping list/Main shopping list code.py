import statistics 
from itertools import chain
from collections import Counter
weeks = [["a","b","c","d","e"],["b","d","f","j","k"],["g","a","h","f","b"],["a","i","t","z","c"]]
unique = []
def common(weeks):   
    combined = list(chain.from_iterable(weeks)) 
    for i in range(3): 
        c = Counter(combined)
        x = c.most_common(3)
        print(i+1,": ",c[i][0]) 


def check(weeks):
    for i in range(len(weeks[0])): 
        unique.append(weeks[0][i])
        
    for i in range(1,4):
        for x in range(len(weeks[i])):
            if weeks[i][x] in unique:
                pass
            else:
                unique.append(weeks[i][x])
                
    return unique
common(weeks)
print("")
unique = check(weeks)
y  = ",".join(unique)
print (y)
