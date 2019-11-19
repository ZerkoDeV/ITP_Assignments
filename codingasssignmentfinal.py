famous = ["Grandma","Mom","Tzuyu"]
for i in range(3):
        print("Dear " + famous[i] + ", please come to my dinner party")

famous = ["Grandma","Mom","Tzuyu"]
popped_famous = famous.pop(2)
print(popped_famous + " " + "can't come due to some issues.")

famous.append("Cousin")
print("The new guest im inviting is my cousin")

for i in range(3):
        print("Dear " + famous[i] + ", please come to my dinner party")

print("I've found a bigger dinner table so im inviting more people")

famous.insert(0,"Brother")
famous.insert(2,"Grandpa")
famous.append("Uncle")
for i in range(6):
        print("Dear " + famous[i] + ", please come to my dinner party")

print("Im sorry but my table won't come in time and i only have space for 2 people")

famous.pop(5)
print("Uncle, Im sorry but im cancelling ur invitiation")
famous.pop(4)
print("Cousin, Im sorry but im cancelling ur invitiation")
famous.pop(2)
print("Grandma, Im sorry but im cancelling ur invitiation")
famous.pop(0)
print("Brother, Im sorry but im cancelling ur invitiation")

del famous[0]
del famous[0]
print(famous)




places = ["Korea", "Japan", "USA", "Maldives", "Seoul"]
print(places)
print(sorted(places))
print(places)
print(sorted(places,reverse=True))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)




