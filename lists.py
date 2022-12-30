cities=["denizli","manisa","aydın","mugla","afyon"]

#print(cities)

#print(cities[0]) #0. indexteki veriyi getirir

#print(cities[-1]) #son indexteki veriyi getirir

#print(len(cities))

#print(cities[0:2]) # 0 dan başlayarak 2. indexe kadar olan elemaları ekrana yazdırır

#print(cities[:-2])  # son iki elemanı yazdırmaz 


"""
cities[4]="kütahya" # index numarasıyla değişiklik yapıldı

print(cities)

cities.append("ayfon") # list e yeni eleman ekleme

print(cities)

cities.insert(0,"balıkesir") # 0. indexe balıkesir eklendi
"""
"""
print(cities)

del cities[0] # 0. index teki elemanı siler geri gelmez

print(cities)

"""
"""
cities_2=cities.pop() # pop ile silinen elemana ulaşabiliriz

print(cities)

print(cities_2)

"""

"""
cities.remove("mugla")

print(cities)
"""

"""
print(cities)

print(sorted(cities)) # sorted sadece bu satırda çalışıp listte değişiklik yapmaz

cities.sort() # alfabetik siralama yapar

print(cities)

cities.sort(reverse=True) # ters sıralama

print(cities)

"""

#print("ankara" in cities) # cities listinde ankara değeri var mı yok mu?

for city in cities:
    print(city) # print in içerde başlamasının sebebi bu satırın for loop bloğunda olduğunu gösterir