from tabulate import tabulate #модуль для таблицы
import random
import time

NACH_ZN = 1024 #Начальное значение
PROC_ADD = 20 #Процент добавления новых особей
PROC_DEL = 20 #Процент удаления плохих особей
PM = 25 #Процент мутации для каждого элемента хромосомы

class bot:
    #конструктор      
    def __init__(self):
        self.chrom = []
        self.wei = 0
        self.price = 0

    #Задание генов в хромосомах 0 и 1
    def set_chrom(self):
        for _ in range(count):
            self.chrom.append(random.randint(0,1))
    
    #Подсчет весов и ценностей
    def sum_bot(self):
        for i in range(len(self.chrom)):
            if self.chrom[i] == 1:
                self.wei += things[i][0]
                self.price += things[i][1]

    #Скрещивание хромосом 50\50
    def cross_chrom(self, arr1, arr2):
        p = count // 2
        for i in range(p):
            self.chrom.append(arr1[i])
        for i in range(p, count):
            self.chrom.append(arr2[i])

    #Мутация в 25% для каждой хромосомы
    def mutation(self):
        for r in range(len(self.chrom)):
            if (random.randint(0, 99) < PM):
                if (self.chrom[r] == 0): self.chrom[r] = 1
                else: self.chrom[r] = 0

#Создание начального количества ботов
def create_nz():
    for i in range(NACH_ZN):
        bots.append(bot())
        #Добавление 0 и 1 в хромосомы
        bots[i].set_chrom()
        #Вес и ценность каждой выборки
        bots[i].sum_bot()
    
#Сортировка и вывод наилучшего решения
def search(lst):
    lst.sort(reverse=True, key=lambda bot: bot.price)
    for i in range(len(lst)):
        if lst[i].wei < packback:
            return lst[i].wei, lst[i].price, lst[i].chrom
        else: flag = True
    if flag: return 'Любая выборка превыщает размер рюкзака.'

#Добавление новых ботов (PROC от общего количества)
def add_bots(arr):
    nz = len(arr)
    end = len(arr) / 100 * PROC_ADD
    x = y = -1
    #Добавление 10%
    for i in range(nz, nz + int(end)):
        while (x == y):
            x = random.randint(0, nz - 1)
            y = random.randint(0, nz - 1)
        #Добавление бота
        arr.append(bot())
        #Скрещиваем хромосом родителей (x и y)
        arr[i].cross_chrom(arr[x].chrom, arr[y].chrom)
        #Подвергаем мутации
        arr[i].mutation()
        #Сразу узнаем вес и ценность для добавленного бота
        arr[i].sum_bot()
    

#Удаление наихудших ботов от общего количества
def delete_bots(arr):
    dead = len(arr) / 100 * PROC_DEL
    dead = int(dead)
    while (dead != 0):
        for i in range(len(arr)):
            if arr[i].wei > packback:
                arr.pop(i)
                dead -= 1
                flag = False
                break
            else: flag = True
        if flag: 
            arr.pop()
            dead -= 1

#MAIN
packback = int(input('Введите размер рюкзака: '))
count = int(input('Введите количество вещей: '))

things = [] #Список вещей
bots = [] #Популяция

#Инициализация таблицы вещей, веса которых от 1 до 9, а ценности от 10 до 100
for i in range(count):
    things.append([])
    things[i].append(random.randint(1,9))
    things[i].append(random.randint(10,100))

print("\nСписок предметов:")
#Организация списка предметов в виде таблицы
print(tabulate(things, headers=['Вес', 'Цена'], tablefmt="grid"))
#print(things)

'''НАЧАЛО ГЕНЕТИЧЕСКОГО АЛГОРИТМА'''
#Создаем NACH_ZN ботов
create_nz()
best = search(bots)
if isinstance(best, str): print("\nНачальная популяция: ", best)
else: print("\nЛучшее решение для начальной популяции:", "\n- вес сбоки: ", best[0], "\n- ценность сбоки: ", best[1], "\n- предметы сбоки : ", best[2])
iterat = 0
cikl = 30 #размер цикла
#Засекаем время выполнения программы
start_time = time.time()
while (cikl > 0):
    iterat += 1
    search(bots)
    #Добавляем новых ботов
    add_bots(bots)
    search(bots)
    #Удалинеие худших ботов
    delete_bots(bots)
    cikl -= 1
    if isinstance(search(bots), str): 
        cikl += 1
        if iterat == 500:
            break

#Остановка времени
stop = time.time() - start_time
best = search(bots)
if isinstance(best, str): print("\nКонечная популяция популяция: ", best)
else: print("\nЛучшее решение для конечной популяции:", "\n- вес сбоки: ", best[0], "\n- ценность сбоки: ", best[1], "\n- предметы сбоки : ", best[2])
print("\nПрожитых поколений: ", iterat)
print("Время выполнения генетического алгоритма: ")
print("--- %s seconds ---" % (stop))
input("\nPress ENTER to exit...")