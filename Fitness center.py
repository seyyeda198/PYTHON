
class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def display(self):
        print("Name:", self.name)
        print("Role:", self.role)


class Trainer(Employee):
    def __init__(self, name, role, specialization):
        super().__init__(name, role)
        self.specialization = specialization

    def display(self):
        super().display()
        print("Specialization:", self.specialization)


class YogaInstructor(Employee):
    def __init__(self, name, role, yoga_style):
        super().__init__(name, role)
        self.yoga_style = yoga_style

    def display(self):
        super().display()
        print("Yoga Style:", self.yoga_style)


class MultiTrainer(Trainer, YogaInstructor):
    def __init__(self, name, role, specialization, yoga_style):
        Employee.__init__(self, name, role)
        self.specialization = specialization
        self.yoga_style = yoga_style

    def display(self):
        print("Name:", self.name)
        print("Role:", self.role)
        print("Specialization:", self.specialization)
        print("Yoga Style:", self.yoga_style)


obj1 = Employee("John", "Staff")
obj2 = Trainer("David", "Trainer", "Weight Training")
obj3 = YogaInstructor("Anna", "Yoga Instructor", "Hatha Yoga")
obj4 = MultiTrainer("Zarah", "Multi Trainer", "Fitness Training", "Power Yoga")


print("Employee Details")
obj1.display()

print("\nTrainer Details")
obj2.display()

print("\nYoga Instructor Details")
obj3.display()

print("\nMulti Trainer Details")
obj4.display()
