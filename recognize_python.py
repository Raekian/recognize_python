num1 = 42
num2 = 2.3
# variable declaration - numbers, int & float
boolean = True
#boolean data type
string = 'Hello World'
#string data type
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
#list data type
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
#dictionary data type
fruit = ('blueberry', 'strawberry', 'banana')
# tuples data type
print(type(fruit))
#type check
print(pizza_toppings[1])
#access value
pizza_toppings.append('Mushrooms')
#add value
print(person['name'])
#access value
person['name'] = 'George'
#change value
person['eye_color'] = 'blue'
#add value
print(fruit[2])
#access value


if num1 > 45:
    #if conditional
    print("It's greater")
else:
    #else conditional
    print("It's lower")


if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")
    #conditional, length check, log statement

for x in range(5):
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)
x = 0
while(x < 5):
    print(x)
    x += 1
    #while loop

pizza_toppings.pop()
pizza_toppings.pop(1)
#delete values

print(person)
person.pop('eye_color')
print(person)
#log statement, remove value

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break
        #breaks the for loop

def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()
#log statement

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)
#x is parameter and 4 is the argument

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""
#comment multiline, comment single lines below.

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)