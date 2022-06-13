from collections import deque, OrderedDict

#Задание 4.3
def brackets(line):
    # Напишите тело функции
    
    bracket_stack = deque()
    
    for simdol in line:
        if simdol == '(':
            bracket_stack.append(simdol)
        elif simdol == ')' and len(bracket_stack) > 0:
            bracket_stack.pop()
        else:
            return False 
    
    return True if len(bracket_stack) == 0 else False


print(brackets("())))"))


#Задание 4.9
ratings = [('Old York', 3.3), ('New Age', 4.6), ('Old Gold', 3.3), ('General Foods', 4.8),
           ('Belissimo', 4.5), ('CakeAndCoffee', 4.2), ('CakeOClock', 4.2), ('CakeTime', 4.1),
           ('WokToWork', 4.9), ('WokAndRice', 4.9), ('Old Wine Cellar', 3.3), ('Nice Cakes', 3.9)]
         
# Отсортируйте список ratings по убыванию рейтинга. Для кафе
# с одинаковым рейтингом отсортируйте кортежи по названию.
ratings = sorted(ratings, key=lambda x: (-1*x[1], x[0]))

# Сохраните данные с рейтингом в словарь cafes, где ключами являются
# названия кафе, а значениями - их рейтинг.
cafes = OrderedDict(ratings)
print(cafes)


#Задание 4.10
from collections import defaultdict, deque

tasks = [(36871, 'office', False),
(40690, 'office', False),
(35364, 'voltage', False),
(41667, 'voltage', True),
(33850, 'office', False)]


def task_manager(tasks):
    server_tasks = defaultdict(deque)
    for task in tasks:
        if task[2]:
            server_tasks[task[1]].appendleft(task[0])
        else:
            server_tasks[task[1]].append(task[0])
    return server_tasks



print(task_manager(tasks))