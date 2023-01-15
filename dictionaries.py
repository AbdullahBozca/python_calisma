monster_1={"name":"Guru", "power":10,"color":"Red"}

my_friend={"name":"Abdullah","age":34,"gender":"man"}
"""

print(type(monster_1))

print(monster_1)

print(monster_1["name"])   
 
"""
monster_1["position"]=100
print(monster_1)

print(monster_1.get("boy")) # boy adinda herhangi bir key olmadigindan dolayi default olarak "none" dondurur

"""
monster_1.update({"name":"AAA"})

print(monster_1)
 
"""

#del monster_1["position"]

#print(monster_1)

"""
print(monster_1.keys())

print(monster_1.values())

print(monster_1.items())
"""

for a in monster_1: # default olarak key leri donduruyor
    print(a)

for b in monster_1.values():
    print(b)