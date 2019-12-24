import random
NACH_ZN = 10
PROC_ADD = 10
PROC_DEL = 10

class bot:      
    def __init__(self):
        self.chrom = []
        self.wei = 0
        self.price = 0
    
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

    #Мутация в 25%
    def mutation(self):
        if (random.randint(0, 99) < 25):
            r = random.randint(0, len(self.chrom) - 1)
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
            return i, lst[i].wei, lst[i].price, lst[i].chrom
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

#Удаление 5% наихудших ботов от общего количества
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
#НАЧАЛО ПРОГРАММЫ
packback = int(input('Введите размер рюкзака: '))
count = int(input('Введите количество вещей: '))
things = []
bots = []
#Инициализация таблицы вещей, веса которых от 1 до 9, а ценности от 10 до 100
for i in range(count):
    things.append([])
    things[i].append(random.randint(1,9))
    things[i].append(random.randint(10,100))

#Создаем NACH_ZN ботов
create_nz()
print(search(bots))
for _ in range(1000):
    #Сортировка и вывод наилучшего решения
    search(bots)
    #Добавляем новых ботов
    add_bots(bots)
    search(bots)
    #Удалинеие худших ботов
    delete_bots(bots)
    
print(search(bots))
print(things)
input('Press ENTER to exit...')