import random


class Dog:
    def init(self, name):
        self.name = name
        self.hunger = 70
        self.progress = 0
        self.alive = True

    def to_eat(self):
        print("I'm going to eat")
        self.hunger -= 50

    def to_sleep(self):
        print("I will sleep")
        self.hunger += 20
        self.progress += 10

    def to_chill(self):
        print("Rest time")
        self.progress -= 0.1

    def is_alive(self):
        if self.progress < -0.5:
            print("Cash out")
            self.alive = False
        elif self.hunger < 150:
            print("Died from binge eating")
            self.alive = False
        elif self.hunger > 0:
            print("Died from hunger")
            self.alive = False
    def end_of_the_day(self):
        print(f"Progress = {round(self.progress, 1)}")

    def live(self, day):
        d = "Day " + str(day) + " of " + self.name + " life "
        print(f"{day:=^50}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_eat()
        elif live_cube == 2:
            self.to_chill()
        elif live_cube == 3:
            self.to_sleep()
        self.end_of_the_day()
        self.is_alive()


name = input("input name ")
nick = Dog(name=name)
for i in range(366):
    if nick.alive == False:
        break
    nick.live(i)
print(nick.progress)