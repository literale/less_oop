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

    def set_payment(self, payment):
        try:
            int_payment = float(payment)
            if int_payment < 0:
                print("Отрицательное значение оплаты")
            else:
                self._payment = int_payment
        except ValueError:
            print("Некорректное значение оплаты")

    def set_done_hour(self, done_hour):
        try:
            int_done_hour = int(done_hour)
            if int_done_hour < 0:
                print("Отработано отрицательное колличество часов!")
            else:
                self._done_hour = int_done_hour
        except ValueError:
            print("Некорректное значение часов")

    def get_payment(self):
        return self._payment

    def get_done_hour(self):
        return self._done_hour

    payment = property(get_payment, set_payment)
    done_hour = property(get_done_hour, set_done_hour)

    def __init__(self, init_str):
        """Constructor"""
        try:
            list_init_str = init_str.split()
            self.name = list_init_str[0]
            self.second_name = list_init_str[1]
            self.salary = list_init_str[2]
            self.post = list_init_str[3]
            self.norm_hour = list_init_str[4]
            self._done_hour = 0
            self._payment = 0
        except IndexError:
            print("Не хватает данных в строке (выход за пределы массива)")

    def __str__(self):
        return "Имя: {0} Фамилия: {1} Зарплата: {2} Должность: {3} Норма часов : {4} " \
               "Зарплата за месяц : {5} Отработано часов : {6}"\
            .format(self.name, self.second_name, self.salary, self.post, self.norm_hour, self.payment, self.done_hour)

    # считаем плату
    def count_payment(self):
        try:
            extra_hour = int(self.done_hour) - int(self.norm_hour)
            if extra_hour == 0:
                self.payment = self.salary
            elif extra_hour > 0:
                pay_hour = float(self.salary)/float(self.norm_hour)
                self.payment = int(self.salary) + int(pay_hour*extra_hour)
            else:
                pay_hour = float(self.salary) / float(self.norm_hour)
                self.payment = int(self.salary) - int(pay_hour * extra_hour)
        except ValueError:
            print("Где-то в числовых показаьелях значение, не преобразумое в число")


def main():
    workers = []
    count = 0
    # инициализируем работников
    with open('data\\workers', 'r', encoding="utf-8") as f:
        for line in f:
            # print(line)
            if count > 0:
                workers.append(Worker(line))
            count += 1

    # Добавляем отработанные часы
    with open('data\\hours_of', 'r', encoding="utf-8") as f:
        for line in f:
            # print(line)
            line_list = line.split()
            if count > 0:
                try:
                    for w in workers:
                        if w.name == line_list[0] and w.second_name == line_list[1]:
                            w.done_hour = line_list[2]
                except IndexError:
                    print("Не хватает данных в строке (выход за пределы массива)")
                count += 1





    for w in workers:
        w.count_payment()
        print(w)


if __name__ == '__main__':
    main()