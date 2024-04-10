

print("Hello python")
a = [1, "bobo", 3]
for i in a:
    print(i)
print(a[1])
class ErrorFactory:
    pass
    def locura():
         pass
ErrorFactory.locura()
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("Hello my name is", self.name)

person1 = Person("Amancio", 36)
person1.myfunc()
print(person1.name)
if person1.name == "Juan":
    print("Hello Juan")
else:
        print("Hello {}".format(person1.name))
        print(f"Is {person1.name} older than 30? {person1.age > 30}")

my_dict = {
    "name": "John",
    "age": 36,
    "country": "Norway",
    "city": "Oslo"
}
print(my_dict["country"])
# This is a comment
"""
This is a multi line comment
"""