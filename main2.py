from tkinter import *
from tkinter import ttk, Frame
from tkinter.scrolledtext import ScrolledText
import main as m

a = input('Выберите, с телефона(1) или с компьютера(2) хотите посмотреть превью объявления >> ').lower()
if a == '1' or a == 'с телефона':
    W1 = Tk()
    W1.geometry('450x800+750+10')
    W1.resizable(False, False)
    W1.title('Такси 15-62 цизыжды')
    icon = PhotoImage(file='2023-01-27_16.43.16.png')
    W1.iconphoto(False, PhotoImage(file='2023-01-27_16.43.16.png'))

    title_mob = ttk.Label(text='Продажа Nissan Skyline, ' + str(m.year) + ' год(а)\n ' + m.car_city, font='Arial 18 bold roman')
    title_mob.pack(anchor='nw',padx=20,pady=10)

    picture = PhotoImage(file='Car_mobila/skyline.png')
    picture1mini = PhotoImage(file='Car_mobila/mini1.png')

    picture2 = PhotoImage(file='Car_mobila/skylinezad.png')
    picture2mini = PhotoImage(file='Car_mobila/mini4.png')

    picture3 = PhotoImage(file='Car_mobila/skylinesalon.png')
    picture3mini = PhotoImage(file='Car_mobila/mini3.png')

    picture4 = PhotoImage(file='Car_mobila/skylinedvigatel.png')
    picture4mini = PhotoImage(file='Car_mobila/mini2.png')
    car_picture = ttk.Label(image=picture)

    mob_frame = Frame(W1)
    main_pic = ttk.Button(image=picture)
    main_pic.pack()

    def change_gl(image):
        main_pic['image'] = image

    #carpic2 = ttk.Button(f_bot, image=picture2mini,command=lambda f=picture2, h=picture1mini: change_gl(f))
    carpic = ttk.Button(mob_frame, image=picture1mini, command=lambda f=picture: change_gl(f))
    carpic2 = ttk.Button(mob_frame, image=picture2mini, command=lambda f=picture2: change_gl(f))
    carpic3 = ttk.Button(mob_frame, image=picture3mini,command=lambda f=picture3: change_gl(f))
    carpic4 = ttk.Button(mob_frame, image=picture4mini,command=lambda f=picture4: change_gl(f))
    mob_frame.pack()
    carpic.pack(side=LEFT)
    carpic2.pack(side=LEFT)
    carpic3.pack(side=LEFT)
    carpic4.pack(side=LEFT)


    cena_avto = str(m.nissan) + '₽'#отличная/хорошая/нормальная/высокая цена
    price = ttk.Label(text=cena_avto, font='Arial 18 bold roman')
    price.pack(anchor='nw', padx=20, pady=10)


    if m.start_price - m.nissan >= 1500000:
        info_price = ttk.Label(text='Отличная цена', background='#009933',foreground='white')
        info_price.pack(anchor='nw', padx=20, pady=6)
    elif 500000 <= m.start_price - m.nissan <= 1500000:
        info_price = ttk.Label(text='Хорошая цена', background='#76FF7A', foreground='black')
        info_price.pack(anchor='nw', padx=20, pady=6)
    elif 500000 <= m.start_price - m.nissan <= 1000000:
        info_price = ttk.Label(text='Нормальная цена', background='#b4fac8', foreground='#57ad80')
        info_price.pack(anchor='nw', padx=20, pady=6)
    elif 0 <= m.start_price - m.nissan < 500000 or m.nissan > m.start_price:
        info_price = ttk.Label(text='Высокая цена', background='#b8b8b8', foreground='#545252')
        info_price.pack(anchor='nw', padx=20, pady=6)

    #сделать цветную кнопку с информацией о цене (отличная/хорошая/нормальная/высокая цена)
        '''первый фрейм с названиями характеристиками машины'''

    main_frame = ttk.Frame(W1, borderwidth=1, relief=SOLID)
    main_frame.pack(anchor='nw', padx=15)
    frame_left = ttk.Frame(main_frame, borderwidth=1,relief=SOLID)
    frame_right = ttk.Frame(main_frame, borderwidth=1,relief=SOLID)
    frame_left.pack(anchor='nw',side=LEFT)
    frame_right.pack(anchor='nw',side=LEFT)

    har_1 = ttk.Label(frame_left, text='Двигатель', foreground='grey', font="Arial 12 roman")
    har_2 = ttk.Label(frame_left, text='Мощность', foreground='grey', font="Arial 12 roman")
    har_3 = ttk.Label(frame_left, text='Коробка передач', foreground='grey', font="Arial 12 roman")
    har_4 = ttk.Label(frame_left, text='Привод', foreground='grey', font="Arial 12 roman")
    har_5 = ttk.Label(frame_left, text='Цвет', foreground='grey', font="Arial 12 roman")
    har_6 = ttk.Label(frame_left, text='Пробег, км', foreground='grey', font="Arial 12 roman")
    har_7 = ttk.Label(frame_left, text='Руль', foreground='grey', font="Arial 12 roman")
    har_8 = ttk.Label(frame_left, text='Поколение', foreground='grey', font="Arial 12 roman")

    har_9 = ttk.Label(frame_right, text='бензин,  ' + str(m.volume) + ' л', foreground='black', font="Arial 12 roman")
    har_10 = ttk.Label(frame_right, text=str(m.modification) + ' л.с.', foreground='black', font="Arial 12 roman")
    har_11 = ttk.Label(frame_right, text=m.kpp, foreground='black', font="Arial 12 roman")
    har_12 = ttk.Label(frame_right, text=m.driving_gear, foreground='black', font="Arial 12 roman")
    har_13 = ttk.Label(frame_right, text=m.color, foreground='black', font="Arial 12 roman")
    har_14 = ttk.Label(frame_right, text=str(m.mileage), foreground='black', font="Arial 12 roman")
    har_15 = ttk.Label(frame_right, text=m.rule, foreground='black', font="Arial 12 roman")
    har_16 = ttk.Label(frame_right, text=m.model[-3:], foreground='black', font="Arial 12 roman")

    har_1.pack(anchor='nw',padx=20, pady=2)
    har_2.pack(anchor='nw', padx=20, pady=2)
    har_3.pack(anchor='nw', padx=20, pady=2)
    har_4.pack(anchor='nw', padx=20, pady=2)
    har_5.pack(anchor='nw', padx=20, pady=2)
    har_6.pack(anchor='nw', padx=20, pady=2)
    har_7.pack(anchor='nw', padx=20, pady=2)
    har_8.pack(anchor='nw', padx=20, pady=2)

    har_9.pack(anchor='nw', padx=20, pady=2)
    har_10.pack(anchor='nw', padx=20, pady=2)
    har_11.pack(anchor='nw', padx=20, pady=2)
    har_12.pack(anchor='nw', padx=20, pady=2)
    har_13.pack(anchor='nw', padx=20, pady=2)
    har_14.pack(anchor='nw', padx=20, pady=2)
    har_15.pack(anchor='nw', padx=20, pady=2)
    har_16.pack(anchor='nw', padx=20, pady=2)

    title_text = ttk.Label(text='Введите описание машины', font='Arial 13 roman')
    title_text.pack(anchor='nw', padx=20, pady=10)

    comment = ScrolledText(width=50, height=10, wrap='word')
    comment.pack(fill=BOTH, expand=True)

    W1.mainloop()


elif a == '2' or a == 'с компьютера':
    W2 = Tk()
    W2.title('Окно для пекаря')
    w = W2.winfo_screenwidth()  # ширина экрана
    h = W2.winfo_screenheight()  # высота экрана
    W2.geometry(f'{w}x{h}')
    W2.iconphoto(False, PhotoImage(file='2023-01-27_16.43.16.png'))  # иконка окна

    t_2 = 'Продажа Nissan Skyline, ' + str(m.year) + ' год(а)\n ' + m.car_city
    title_comp = ttk.Label(text=t_2, font='Arial 26 bold roman')
    title_comp.pack(anchor='nw',padx=60,pady=25)

    picture = PhotoImage(file='Car_pc/skyline_pc.png')
    picture_mini = PhotoImage(file='Car_pc/skyline_mini_pc.png')

    picture2 = PhotoImage(file='Car_pc/skyline_zad_pc.png')
    picture_mini2 = PhotoImage(file='Car_pc/skyline_zad_pc_mini.png')

    picture3 = PhotoImage(file='Car_pc/skyline_salon_pc.png')
    picture_mini3 = PhotoImage(file='Car_pc/skyline_salon_pc_mini.png')

    picture4 = PhotoImage(file='Car_pc/skyline_dvig_pc.png')
    picture_mini4 = PhotoImage(file='Car_pc/skyline_dvig_pc_mini.png')

    """создание самого главного фрейма, в котором находятся два менее главных фреймов"""
    batya_frame = ttk.Frame(W2, borderwidth=1, relief=SOLID)
    batya_frame.pack()

    '''создание  первого основного фрейма,где есть левый фрейм(тачка) и правый(описание)'''
    main_frame1 = ttk.Frame(batya_frame, borderwidth=1, relief=SOLID)
    main_frame1.pack(side=LEFT)

    frame_top = ttk.Frame(main_frame1, borderwidth=1, relief=SOLID)
    frame_top.pack()
    frame_left = Frame(frame_top,borderwidth=1,relief=SOLID) #создание левого фрейма
    frame_left.pack(side=LEFT, anchor='nw', padx=60, pady=10)
    car_pic_osn = ttk.Button(frame_left, image=picture)
    car_pic_osn.pack()

    def change_gl_pic(image):
        car_pic_osn['image'] = image

    car_pic1_pk = ttk.Button(frame_left, image=picture_mini, command=lambda x=picture: change_gl_pic(x))
    car_pic2_pk = ttk.Button(frame_left, image=picture_mini2, command=lambda x=picture2: change_gl_pic(x))
    car_pic3_pk = ttk.Button(frame_left, image=picture_mini3, command=lambda x=picture3: change_gl_pic(x))
    car_pic4_pk = ttk.Button(frame_left, image=picture_mini4, command=lambda x=picture4: change_gl_pic(x))

    car_pic1_pk.pack(side=LEFT)
    car_pic2_pk.pack(side=LEFT)
    car_pic3_pk.pack(side=LEFT)
    car_pic4_pk.pack(side=LEFT)

    frame_right = Frame(frame_top,borderwidth=1,relief=SOLID) #создание правого фрейма
    frame_right.pack(side=RIGHT,anchor='nw', padx=60, pady=10)
    cena_avto = str(m.nissan) + '₽'  # отличная/хорошая/нормальная/высокая цена
    price = ttk.Label(frame_right, text=cena_avto, font='Arial 24 bold roman')
    price.pack(anchor='nw', padx=20, pady=10)

    if m.start_price - m.nissan >= 1500000:
        info_price = ttk.Label(frame_right,text='Отличная цена', background='#009933', foreground='white')
        info_price.pack(anchor='nw',padx=16, pady=6)
    elif 500000 <= m.start_price - m.nissan <= 1500000:
        info_price = ttk.Label(frame_right,text='Хорошая цена', background='#76FF7A', foreground='black')
        info_price.pack(anchor='nw', padx=16,pady=6)
    elif 500000 <= m.start_price - m.nissan <= 1000000:
        info_price = ttk.Label(frame_right,text='Нормальная цена', background='#b4fac8', foreground='#57ad80')
        info_price.pack(anchor='nw', padx=16,pady=6)
    elif 0 <= m.start_price - m.nissan < 500000 or m.nissan > m.start_price:
        info_price = ttk.Label(frame_right,text='Высокая цена', background='#b8b8b8', foreground='#545252')
        info_price.pack(anchor='nw',padx=16,pady=6)

    frame_right1 = ttk.Frame(frame_right,borderwidth=1, relief=SOLID)
    frame_right2 = ttk.Frame(frame_right,borderwidth=1, relief=SOLID)
    frame_right1.pack(anchor='nw',side=LEFT)
    frame_right2.pack(anchor='nw',side=LEFT)

    har_1 = ttk.Label(frame_right1, text='Двигатель', foreground='grey', font="Arial 12 roman")
    har_2 = ttk.Label(frame_right1, text='Мощность', foreground='grey', font="Arial 12 roman")
    har_3 = ttk.Label(frame_right1, text='Коробка передач', foreground='grey', font="Arial 12 roman")
    har_4 = ttk.Label(frame_right1, text='Привод', foreground='grey', font="Arial 12 roman")
    har_5 = ttk.Label(frame_right1, text='Цвет', foreground='grey', font="Arial 12 roman")
    har_6 = ttk.Label(frame_right1, text='Пробег, км', foreground='grey', font="Arial 12 roman")
    har_7 = ttk.Label(frame_right1, text='Руль', foreground='grey', font="Arial 12 roman")
    har_8 = ttk.Label(frame_right1, text='Поколение', foreground='grey', font="Arial 12 roman")

    har_9 = ttk.Label(frame_right2, text='бензин,  ' + str(m.volume) + ' л', foreground='black', font="Arial 12 roman")
    har_10 = ttk.Label(frame_right2, text=str(m.modification) + ' л.с.', foreground='black', font="Arial 12 roman")
    har_11 = ttk.Label(frame_right2, text=m.kpp, foreground='black', font="Arial 12 roman")
    har_12 = ttk.Label(frame_right2, text=m.driving_gear, foreground='black', font="Arial 12 roman")
    har_13 = ttk.Label(frame_right2, text=m.color, foreground='black', font="Arial 12 roman")
    har_14 = ttk.Label(frame_right2, text=str(m.mileage), foreground='black', font="Arial 12 roman")
    har_15 = ttk.Label(frame_right2, text=m.rule, foreground='black', font="Arial 12 roman")
    har_16 = ttk.Label(frame_right2, text=m.model[-3:], foreground='black', font="Arial 12 roman")

    har_1.pack(anchor='nw', pady=3)
    har_2.pack(anchor='nw', pady=3)
    har_3.pack(anchor='nw', pady=3)
    har_4.pack(anchor='nw', pady=3)
    har_5.pack(anchor='nw', pady=3)
    har_6.pack(anchor='nw', pady=3)
    har_7.pack(anchor='nw', pady=3)
    har_8.pack(anchor='nw', pady=3)

    har_9.pack(anchor='nw', pady=3)
    har_10.pack(anchor='nw', pady=3)
    har_11.pack(anchor='nw', pady=3)
    har_12.pack(anchor='nw', pady=3)
    har_13.pack(anchor='nw', pady=3)
    har_14.pack(anchor='nw', pady=3)
    har_15.pack(anchor='nw', pady=3)
    har_16.pack(anchor='nw', pady=3)

    frame_bottom = ttk.Frame(main_frame1,borderwidth=1,relief=SOLID)
    frame_bottom.pack()
    title_text = ttk.Label(frame_bottom, text='Введите описание машины', font='Arial 13 roman')
    title_text.pack(anchor='sw', padx=60, pady=10)
    comment = ScrolledText(frame_bottom,width=155, height=10, wrap='word')
    comment.pack(anchor='sw',expand=True, padx=60)

    main_frame2 = ttk.Frame(batya_frame, borderwidth=1, relief=SOLID)
    main_frame2.pack(side=LEFT,anchor='ne')
    i = PhotoImage(file='Car_pc/top_reklama.png')
    advertisement = ttk.Label(main_frame2, image=i)
    advertisement.pack()

    W2.mainloop()