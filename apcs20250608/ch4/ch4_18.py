cars = ['honda','BMW','Toyota','audi']
#小寫 > 大寫
print(cars)
cars.sort()
print(cars)
cars.sort(key=len)
print(cars)
cars.sort(key=lambda v:v.upper())
print(cars)

