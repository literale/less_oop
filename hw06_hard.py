# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла
class Worker(object):
    payment = 0
    def __init__(self, init_str):
        """Constructor"""
        list_init_str = init_str.split()
        self.name = list_init_str[0]
        self.second_name = list_init_str[1]
        self.salary = list_init_str[2]
        self.post = list_init_str[3]
        self.norm_hour = list_init_str[4]
        pass
    
    def set_payment(self, payment):
        self.payment = payment
        pass

    def __str__(self):
        return "Имя: {0} Фамилия: {1} Зарплата: {2} Должность: {3} Норма часов : {4} Зарплата за месяц : {5}"\
            .format(self.name, self.second_name, self.salary, self.post, self.norm_hour, self.payment)





def main():
    workers = []
    count = 0
    #инициализируем работников
    with open('data\\workers', 'r', encoding="utf-8") as f:
        for line in f:
            #print(line)
            if count > 0:
                workers.append(Worker(line))
            count += 1

    for w in workers:
        print(w)

if __name__ == '__main__':
    main()