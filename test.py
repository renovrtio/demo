from demo import addxy

#x = int(input('请输入一个数字x：'))
#y = int(input('请输入一个数字y：'))

#print(addxy(x, y))
list1 = []
if list1:
    print('a')
else:
    print('b')

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars2 =['audi', 'subaru', 'ab']
for car in cars2:
    if car not in cars:
        print(car, 'not in cars')

for car in cars:
    if car == 'bmw':
        print(car.upper())
    elif car == 'audi':
        print(car.title())
    else:
        print(car)

# for car in cars:
#     print(car)

# cars.sort()
# for car in cars:
#     print(car)

# cars.sort(reverse=True)
# for car in cars:
#     print(car)

# for car in sorted(cars):
#     print(car)

# print(cars[-1])

# for value in range(5):
#     print(value)

# numbers = list(range(0, 5))
# for num in numbers:print(num)

# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))

# squares = [value**2 for value in range(5)]
# print(squares)

# numbers = list(range(1, 1000000))
# print(sum(numbers))

# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# # print(players[1:])

# new_players = players[:]
# players.append('players')
# print(players)
# print(new_players)


