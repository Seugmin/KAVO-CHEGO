class Student:

    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True

    def to_study(self):
        print("Time to study")
        self.progress += 0.15
        self.gladness -= 3
    def to_sleep(self):
        pass
    def to_child(self):
        pass

nick = Student(name = "Nick")
nick.to_study()
print(nick.progress)
print(nick.gladness)