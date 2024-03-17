import random
from collections import defaultdict

tokens=["I", "try", "to" , "learn", "something", "new", "every", "day"]

graph=defaultdict(list)

print(graph["word"]) 


for i, token in enumerate(tokens):
    print(i, token)

#raffle that picks randomly from set of tokens provided
print(random.choice(tokens))
print(random.choice(tokens))
print(random.choice(tokens))


        

