""" Create a class named Person, with firstname and lastname properties, and a printname method: """

class Person():
    def __init__(self, first_name, last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name

    def print_name(self):
        return """
            First Name: {}
            Last Name: {}
        """.format(self.first_name, self.last_name)

# quang = Person("Clint", "Nguyen")
# print(quang.print_name())

class Student(Person):
    def __init__(self, first_name, last_name) -> None:
        super().__init__(first_name, last_name)

hoang = Student("Giap Phi", "Hoang")
print(hoang.print_name())


# ----------------------------------------------------------------------------------------------------