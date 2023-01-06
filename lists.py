cities=["denizli","manisa","aydin","mugla","afyon"]

#print(cities)

#print(cities[0]) #0. indexteki veriyi getirir

#print(cities[-1]) #son indexteki veriyi getirir

#print(len(cities))

#print(cities[0:2]) # 0 dan başlayarak 2. indexe kadar olan elemaları ekrana yazdırır

#print(cities[:-2])  # son iki elemanı yazdırmaz 


"""
cities[4]="kütahya" # index numarasiyla degisiklik yapildi

print(cities)

cities.append("ayfon") # list e yeni eleman ekleme

print(cities)

cities.insert(0,"balikesir") # 0. indexe balikesir eklendi
"""
"""
print(cities)

del cities[0] # 0. index teki elemani siler geri gelmez

print(cities)

"""
"""
cities_2=cities.pop() # pop ile silinen elemana ulasabiliriz

print(cities)

print(cities_2)

"""

"""
cities.remove("mugla")

print(cities)
"""

"""
print(cities)

print(sorted(cities)) # sorted sadece bu satirda çalisip listte degisiklik yapmaz

cities.sort() # alfabetik siralama yapar

print(cities)

cities.sort(reverse=True) # ters siralama

print(cities)

"""

#print("ankara" in cities) # cities listinde ankara degeri var mi yok mu?

for city in cities:
    print(city) # print in icerde baslamasinin sebebi bu satirin for loop blogunda oldugunu gosterir