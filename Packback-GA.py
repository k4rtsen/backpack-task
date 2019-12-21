import random

packback = int(input('Введите размер рюкзака: '))
count = int(input('Введите количество вещей: '))
things = []
bot = []

#Поиск наилучшего решения
def search_best():
    index = -1
    max_wei = max_price = 0
    for i in range(len(bot)):
        price = wei = 0
        for j in range(count):
            if (bot[i][j] == 1):
                wei += things[j][0]
                price += things[j][1]
        if (packback >= wei):
            if (price > max_price):
                max_price = price
                max_wei = wei
                index = i + 1
    if (index != -1):
        return 'Вес: ' + str(max_wei) + ' Цена: ' + str(max_price) + ' Номер бота: ' + str(index)
    else: return 'Любая выборка превышает размер рюкзака.'
#------------------------------------------------------------

#Создание новых ботов(скрещивание). 10% от общего количество
def create_new_bots(size):
    a = b = -1
    while a == b:
        a = random.randint(0, size - 1)
        b = random.randint(0, size - 1)
    end = size // 10
    for i in range(size, size + end):
        bot.append([])
        for j in range(count):
            if (random.randint(0,1) == 0): bot[i].append(bot[a][j])
            else: bot[i].append(bot[b][j])
        mutation(i)
#------------------------------------------------------------

#Мутация в 0,25% случаях
def mutation(index):
    if (random.randint(1,100) < 25):
        if (bot[index - 1][random.randint(0, count - 1)] == 1): bot[index - 1][random.randint(0, count - 1)] = 0
        else: bot[index - 1][random.randint(0, count - 1)] = 1
#------------------------------------------------------------

#Инициализация таблицы вещей, веса которых от 1 до 9, а ценности от 10 до 100
for i in range(count):
    things.append([])
    for j in range(2):
        if (j == 0):
            r = random.randint(1,9)
            things[i].append(r)
        else:
            r = random.randint(10,100)
            things[i].append(r)

#Инициализация хромосом ботов 0 и 1
for i in range(10):
    bot.append([])
    for j in range(count):
        bot[i].append(random.randint(0,1))

print(things)
bot.sort()

for i in range(100):
    print(i, ': ', search_best())
    create_new_bots(len(bot))

for i in range(len(bot)):
    print(i, 'bot: ', bot[i])

input('Press ENTER to exit...')