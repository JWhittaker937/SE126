import random
shotx=0
shoty=0
def shot():
    shotx=random.randint(1,6)
    shoty=random.randint(1,4)
    return shotx,shoty
map=[
    ["a1","a2","a3","a4"],
    ["b1","b2","b3","b4"],
    ["c1","c2","c3","c4"],
    ["d1","d2","d3","d4"],
    ["e1","e2","e3","e4"],
    ["f1","f2","f3","f4"],
]