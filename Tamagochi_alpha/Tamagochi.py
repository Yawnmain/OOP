from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Tamagochi")
root.geometry("250x100")


class monster:

    def __init__(self, eat_damage=15, health=100, happy=100, play_damage=15, feedSPD=10, playSPD=10):
        self.health = health
        self.happy = happy
        self.health_max = health
        self.happy_max = happy
        self.eat_damage = eat_damage
        self.play_damage = play_damage
        self.feedSPD = feedSPD
        self.playSPD = playSPD
        self.flag = True
        self.end_flag = True

        btn = ttk.Button(text="Покормить", command=self.eating)
        btn.pack()
        btn = ttk.Button(text="Поиграть", command=self.play)
        btn.pack()
        btn = ttk.Button(text="Restart", command=self.restart)
        btn.pack()

    def eating(self):
        if self.flag:
            if self.eat_damage + self.health <= self.health_max:
                self.health += self.eat_damage
            else:
                self.health = self.health_max
            print(f"ХП: {self.health}", "\n")
        else:
            print("Зверушка умерла", "\n")

    def play(self):
        if self.flag:
            if self.play_damage + self.happy <= self.happy_max:
                self.happy += self.play_damage
            else:
                self.happy = self.happy_max
            print(f"Счастье: {self.happy}", "\n")
        else:
            print("Зверушка умерла", "\n")

    def end(self, msg):
        if self.flag:
            self.flag = False
            print(msg)

    def starv(self):
        if self.flag:
            if self.health <= 0:
                self.end("Зверушка умерла от голода")
            else:
                self.health -= self.feedSPD
                print("Я проголодалась!", "\n", f"ХП: {self.health}", "\n")

    def tilt(self):
        if self.flag:
            if self.happy <= 0:
                self.end("Зверушка умерла от депрессии")
            else:
                self.happy -= self.playSPD
                print("Я хочу играть!", "\n", f"Счастье: {self.happy}", "\n")

    def restart(self):
        self.flag = True
        self.health = 100
        self.happy = 100


Pat = monster()

# Обновление статусов каждые 5 секунд


def recursion():
    Pat.starv()
    Pat.tilt()
    root.after(5000, recursion)


recursion()
root.mainloop()
