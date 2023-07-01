#задача про продажу тачки на авито
class Car:
    """описание свойств тачки"""
    def __init__(self, mark, driving_gear, speed, rule, model, color, year, volume, condition, modification, mileage, start_price, finish_price):
        self.mark = mark
        self.driving_gear = driving_gear
        self.speed = speed
        self.rule = rule

        self.model = model #'Skyline GT-R R34'
        self.color = color
        self.year = year
        self.volume = volume

        self.condition = condition #'Не битый, не крашеный'
        self.modification = modification #'250 л.с.'
        self.mileage = mileage

        self.start_price = start_price
        self.finish_price = finish_price

    def Sale_plus(self):
        '''расчёт цены тачки со всеми поюсами по цене (без проблемных моментов)'''
        print('Марка вашей машины: ' + self.mark + ' Это значит, что к цене добавляется 590 000 ₽')
        self.finish_price += 569000

        if self.model[-2:] == '33':
            allowance = 550000
        elif self.model[-2:] == '32':
            allowance = 600000
        elif self.model[-2:] == '35':
            allowance = 6000000
        elif self.model[-2:] == '34':
            allowance = 800000
        else:
            allowance = 10

        self.finish_price += allowance
        print('Поколение вашей машины ' + self.model[-2:] + ' тогда надбавка к стоимости составит: ' + str(allowance) + ' ₽')
        return self.finish_price

    def Sale_grabezh(self):
        """расчёт цены тачки с учётом всех минусов по цене (проблемными моментами)"""
        if 200 <= self.modification < 220:
            reduction = 10000
            print('От цены отнимается налог в размере 10 000 ₽')
        elif 220 <= self.modification < 450:
            reduction = 45000
            print('От цены отнимается налог в размере 45 000 ₽')
        elif 450 <= self.modification < 600:
            reduction = 67500
            print('От цены отнимается налог в размере 67 000 ₽')
        elif 600 <= self.modification < 850:
            reduction = 127500
        else:
            reduction = 130000
            print('Мощность вашей машины:' + str(self.modification) + ', тогда от цены отнимается налог в размере ', str(reduction) + ' ₽.')
            self.finish_price -= reduction

        if self.mileage < 20000:
            print('Ваш пробег составляет: ' + str(self.mileage) + 'КМ. В таком случае к цене прибавится 35000 ₽')
            self.finish_price += 35000
        elif 20000 <= self.finish_price < 80000:
            reduction1 = 0
            print('Ваш пробег составляет: ' + str(self.mileage) + 'КМ. В таком случае цена не изменится')
        else:
            print('Ваш пробег составляет: ' + str(self.mileage) + 'КМ. В таком от цены отнимется' + (17000 + 6000 * ((self.mileage / 10000) - 8)) + ' ₽')



        self.finish_price -= minus_price

        return self.finish_price

    def Info(self):
        print('В среднем ,похожие на ваш автомобиль, стоят ' + str(self.finish_price) + ' ₽.' + ' Цена вашей машины: ' + str(self.finish_price) + ' ₽')
        otv = input('Согласны ли вы с такой ценой? >> ').lower()
        if otv == 'да':
            print('Чел хорош ┬─┬ ノ( ゜-゜ノ)')
        else:
            print('Знай, ты лох')

    def get_Cena(self):
        cena = self.finish_price
        return cena

mark = 'Nissan'
driving_gear = 'AWD'
speed = '280 км/ч'
rule = 'Правый'
kpp = 'Механика'

start_price = 2000000
finish_price = 0

model = input('Введите модель вашей марки Nissan: ')
color = input('Введите цвет машины: ')
year = input('Введите год выпуска вашей машины: ')
modification = int(input('Введите мощность вашей машины: '))
volume = float(input('Введите объем вашей машины: '))
mileage = int(input('Введите пробег вашей машины в км: '))

condititon = input('Опишите состояние вашей машины: ').lower()
condititon1 = int(input('Опишите состояние повреждений вашей машины от 0 до 10 (только цифра): '))
if 0 <= condititon1 <= 2:
    print('В таком случае цена никак не изменится')
    minus_price = 0
elif 3 <= condititon1 <= 5:
    print('В таком случае от цены отнимается 130 000 рублей ')
    minus_price = 130000
elif 6 <= condititon1 <= 8:
    print('В таком случае от цены отнимается 200 000 рублей')
    minus_price = 200000
else:
    print('В таком случае от цены отнимается 500 000 рублей')
    minus_price = 500000

if condititon == 'попадал в дтп':
    dtp_kol = int(input('Введите кол-во аварий, в которые попадал данный автомобиль: '))
if condititon == 'есть ограничения':
    print('Подробнее расскажите про этот момент при собеседовании. На данный момент от стоимости продажи отнимается 150 000 рублей')
    minus_price = 150000

car_city = input('Укажите,в каком городе продаёте машину: ')

skyline = Car(mark, driving_gear, speed, rule, model, color, year, volume, condititon, modification, mileage, start_price, finish_price)
skyline.Sale_plus()
skyline.Sale_grabezh()
skyline.Info()
nissan = skyline.get_Cena()