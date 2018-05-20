#Project Euler - Problem 1
nums = list(range(1000))
ans = 0
for num in nums:
    if num%3 == 0 or num%5 == 0:
        #print(num)
        ans += num
print(ans)

#Project Euler - Problem 2
a = 1
b = 2
suma = 2
for x in range(32):
    c = a+b
    a = b
    b = c
    if c%2 == 0 and c < 4000000:

        suma+=c
print(suma)

#Exercise 3-1 Name
names = ["Asad","Najeeb","Kashif","Sufyan"]
for person in names:
	print(person)

#Exercise 3-2 Greetings
names = ["Asad","Najeeb","Kashif","Sufyan"]
for person in names:
    print("Dear "+person+", Have a good day")

#Exercise 3-3 Your Own list
transportations = ["Bike", "Car", "Plane"]
for a in transportations:
    print("I would like to own a "+a)

#Exercise 3-4  Guest List
guests = ["Asad","Najeeb","Kashif","Sufyan"]
for a in guests:
    print("Hey "+a+", Join me at dinner on this weekend.")

#Exercise 3-5  Guest List
guests = ["Asad","Najeeb","Kashif","Sufyan"]
del guests[1]
for a in guests:
   print("Hey "+a+", Join me at dinner on this weekend.")

#Exercise 3-6  More Guests
guests = ["Asad","Najeeb","Kashif","Sufyan"]
guests.insert(0,"Khalid")
guests.insert(3,"Shoaib")
guests.append("Arsalan")
for a in guests:
   print("Hey "+a+", Join me at dinner on this weekend.")

#Exercise 3-8  Seeing the World
wonders = ["Great Pyramid of Giza","Hanging Gardens of Babylon","Statue of Zeus at Olympia","Temple of Artemis at Ephesus","Mausoleum at Halicarnassus","Colossus of Rhodes","Lighthouse of Alexandria"]
#Print your list in its original order
print(wonders)
#Use sorted() to print your list in alphabetical order
print(sorted(wonders))
#Show that your list is still in its original order by printing it.
print(wonders)
#Use sorted() to print your list in reverse alphabetical order
print(sorted(wonders,reverse=True))
#Show that your list is still in its original order by printing it again.
print(wonders)
#Use reverse() to change the order of your list. 
wonders.reverse()
print(wonders)
#Use reverse() to change the order of your list again. 
wonders.reverse()
print(wonders)
#Use sort() to change your list so it’s stored in alphabetical order. 
wonders.sort()
print(wonders)
#Usel. sort() to change your list so it’s stored in reverse alphabetical order
wonders.sort(reverse=True)
print(wonders)

#Exercise 4-10 Slices
items = ['Pizza', 'Coldrink', 'Carrot cake', 'Cannoli', 'Ice cream','Burger']
print("The first three items in the list are:")
print(items[:3])
print("Three items from the middle of the list are:")
length = len(items)
if length%2 == 0:
	print(items[int(length/2-1.5):int(length/2+1.5)])
else:
	print(items[int(length/2-1.5):int(length/2+1.5)])
print("The last three items in the list are:")
print(items[-3:])

#Exercise 4-11 My Pizzas, Your Pizzas
pizzas = ["Pepperoni","Chicken Tikka","Hawaiian pizza","Italiano Crust","Crunchy Thin Crust"]
friend_pizzas = pizzas[:]
pizzas.insert(0,'Fajita')
friend_pizzas.insert(0,'Chicken Golden')
if pizzas == friend_pizzas:
	print("Both lists are same.")
else:
	print("Both lists are not same")

print("My favorite pizzas are:")
for pizza in pizzas:
	print(pizza)

print("My friend’s favorite pizzas are")
for friend_pizza in friend_pizzas:
	print(friend_pizza)
	
#Exercise 4-12 More Foods
pizzas = ["Pepperoni","Chicken Tikka","Hawaiian pizza","Italiano Crust","Crunchy Thin Crust"]
foods = ["Cake","Ice Cream","Halwa Puri","Fries","Burger"]

print("Pizzas are:")
for pizza in pizzas:
	print(pizza)

print("Foods are")
for food in foods:
	print(food)
	
#Exercise 4-13 Buffet
foods = ("Cake","Ice Cream","Halwa Puri","Fries","Burger")
print("Foods are")
for food in foods:
	print(food)
foods.insert(0,"New Food")	
foods = ("Chips","Ice Cream","Halwa Puri","Fries","Juice")
print("Foods are")
for food in foods:
	print(food)