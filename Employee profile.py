
class Person:
    def __init__(self, name, age, **kwargs):
        self.name = name
        self.age = age
        super().__init__(**kwargs)

    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Employee(Person):
    def __init__(self, employee_id, **kwargs):
        self.employee_id = employee_id
        super().__init__(**kwargs)

    def show_details(self):
        super().show_details()
        print("Employee ID:", self.employee_id)


class PartTime(Person):
    def __init__(self, working_hours, **kwargs):
        self.working_hours = working_hours
        super().__init__(**kwargs)

    def show_details(self):
        super().show_details()
        print("Working Hours:", self.working_hours)


class Consultant(Employee, PartTime):
    def __init__(self, project_name, **kwargs):
        self.project_name = project_name
        super().__init__(**kwargs)

    def show_details(self):
        super().show_details()
        print("Project Name:", self.project_name)


obj1 = Person("John", 25)
obj2= Employee("E101", name="David", age=28)
obj3 = PartTime(5.5, name="Anu", age=22)
obj4 = Consultant("Python Project", name="Alex", age=30,
                employee_id="E102", working_hours=6.5)

print("Person Details")
obj1.show_details()

print("\nEmployee Details")
obj2.show_details()

print("\nPartTime Details")
obj3.show_details()

print("\nConsultant Details")
obj4.show_details()
