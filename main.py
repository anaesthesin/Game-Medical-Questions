from tkinter import *
import csv
import random


with open('questions.csv') as file:
    data = csv.DictReader(file, delimiter=';')
    a = 0
    questions_for_student = []
    questions_for_doctor = []
    for row in data:
        if a == 10:
            break
        a += 1
        if row['level'] == '1':
            questions_for_student.append(row)
        else:
            questions_for_doctor.append(row)



class Player():
    points = 0
    name = None
    def __init__(self, status):
        self._status = status
    def plus_points(self, point):
        self.points += point
    def minus_points(self, penalty):
        self.points -= penalty
    @property
    def status(self):
        return self._status

def button_1():
    global player
    player = Player('Student')

    return level_name(root)

def button_2():
    global player
    player = Player('Doctor')
    return level_name(root)

def victorina(root):
    root.destroy()
    root = Tk()
    root.title('Загадки по Медицине')
    root.geometry('400x250+200+90')
    root.resizable(False, False)

    if player.status == 'Student':
        past_questions = []
        while True:
            number_question = random.randint(0, len(questions_for_student)-1)
            if number_question not in past_questions:
                current_question = questions_for_student[number_question]['question']
            else:
                break

    else:
        past_questions = []
        while True:
            number_question = random.randint(0, len(questions_for_doctor)-1)
            if number_question not in past_questions:
                current_question = questions_for_doctor[number_question]['question']
            else:
                break

    question = Label(root, text=current_question)
    question.grid(column=2, row=2)


def level_name(root):
    def save_name():
        entered_name = txt.get()
        player.name = entered_name
        return victorina(root)

    root.destroy()
    root = Tk()
    root.title('Загадки по Медицине')
    root.geometry('400x250+200+90')
    root.resizable(False, False)

    lbl = Label(root, text='Введи имя')
    txt = Entry(root)
    btn = Button(root, text='Ok', command=save_name)

    lbl.grid(column=2, row=3)
    txt.grid(column=2, row=4)
    btn.grid(column=6, row=4)


root = Tk()
root.geometry('400x250+200+90')
root.resizable(False, False)
root.title('Загадки по Медицине')
lbl_1 = Label(root, text='Добро пожаловать в Игру Загадки по Медицине')
lbl_2 = Label(root, text='Выбери уровень')

lbl_1.grid(column=2, row=2)
lbl_2.grid(column=2, row=3)

btn_1 = Button(root, text='Студент', command=button_1)
btn_1.grid(column=1, row=3)
btn_2 = Button(root, text='Доктор', command=button_2)
btn_2.grid(column=3, row=3)

root.mainloop()
