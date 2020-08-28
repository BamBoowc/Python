motorcycles  = ['honda', 'yamaha', 'suzuki'] 
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)
motorcycles.insert(0, 'ducati')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

del motorcycles[2]
print(motorcycles)

motorcycles_1 = []
motorcycles_1.append('honda')
motorcycles_1.append('yamaha')
motorcycles_1.append('suzuki')
print(motorcycles_1)

motorcycles_2  = ['honda', 'yamaha', 'suzuki'] 
print(motorcycles)
popped_motorcycle = motorcycles_2.pop()
print(motorcycles_2) 
print(popped_motorcycle)

motorcycles_2  = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles_2.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")

motorcycles_2  = ['honda', 'yamaha', 'suzuki'] 
print(motorcycles_2)
motorcycles_2.remove('yamaha')
print(motorcycles_2)

motorcycles_2  = ['honda', 'yamaha', 'suzuki'] 
print(motorcycles_2)
too_expensive = 'yamaha'
motorcycles_2.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me")
