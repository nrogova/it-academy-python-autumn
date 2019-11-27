""" Create simulator from real life. In my case it's band simulation.
Create 3-4 objects, that can describe situation.
Objects should contain attributes and methods to simulate some use cases.
Completed program should print object states, it actions and objects
interaction.
I know that it looks bad and really sorry.
I tried to understand how classes work and it helps me.
"""


class Band(object):
    pl_count = 0

    def __init__(self, name, instr, pay=90, experience=2):
        Band.pl_count += 1
        self.name = name
        self.instr = instr
        self.pay = pay
        self.experience = experience

    @staticmethod
    def count_check():
        if Band.pl_count > 4:
            print("Слишком много людей! Уйдите со сцены!")
        else:
            print("Группа выступает")

    def pay_salary(self):
        if Band.pl_count <= 4:
            self.pay += 10
            self.experience += 1
        else:
            print("Не выступили, не заплатили")

    def celebrate(self):
        if self.pay >= 100 and Band.pl_count <= 4:
            self.pay -= 5
        else:
            print('Имя: {} не может отметить, мало денег. Деньги: {}'.format
                  (self.name, self.pay))

    def display_player(self):
        print('Имя: {}. Инструмент: {}. Деньги: {} Опыт: {}'.format
              (self.name, self.instr, self.pay, self.experience))


pl1 = Band("Андрей", "гитара", 0)
pl2 = Band("Мария", "бас-гитара")
pl3 = Band("Анжела", "барабаны", experience=3)
pl4 = Band("Аня", "вoкал")
# pl5 = Band("Ваня", "барабаны")
pl1.display_player()
pl2.display_player()
pl3.display_player()
pl4.display_player()
# pl5.display_player()
print("Всего участников:", Band.pl_count)
Band.count_check()
pl1.pay_salary()
pl2.pay_salary()
pl3.pay_salary()
pl4.pay_salary()
pl1.celebrate()
pl2.celebrate()
pl3.celebrate()
pl4.celebrate()
pl1.display_player()
pl2.display_player()
pl3.display_player()
pl4.display_player()
