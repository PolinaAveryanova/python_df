import tkinter
import tkinter.ttk as ttk
window = tkinter.Tk()


size_pep = tkinter.StringVar()
size_marg = tkinter.StringVar()
size_gav = tkinter.StringVar()
count_pep= tkinter.IntVar()
count_marg= tkinter.IntVar()
count_gav= tkinter.IntVar()
time = tkinter.StringVar()
address = tkinter.StringVar()
phone = tkinter.StringVar()
date = tkinter.StringVar()
total_sum = tkinter.IntVar()


pizza = {'ГАВАЙСКАЯ': {'consist': ['курица',
                           'ветчина',
                           'ананас',
                           'моцарелла',
                           'томатный соус'],
               'size_price': {'M': 595, 'S': 415, 'L': 775}},
 'МАРГАРИТА': {'consist': ['томаты', 'моцарелла', 'томатный соус'],
               'size_price': {'M': 545, 'S': 395, 'L':695}},
 'ПЕППЕРОНИ': {'consist': ['пепперони', 'моцарелла', 'томатный соус'],
               'size_price': {'M': 545, 'S': 395,'L':695}}}
order_lst = dict()

def total_price():
    order_lst["pizza_order"] = {'ПЕППЕРОНИ':[{"size":size_pep.get(), 'count':count_pep.get()}],'МАРГАРИТА':[{"size":size_marg.get(), 'count':count_marg.get()}],'ГАВАЙСКАЯ':[{"size":size_gav.get(), 'count':count_gav.get()}], "date":date.get(), 'time':time.get(), 'address':address.get(), 'phone':phone.get()} 
    total = int(pizza['ПЕППЕРОНИ']['size_price'][order_lst['pizza_order']['ПЕППЕРОНИ'][0]['size']]) * int(count_pep.get()) + int(pizza['МАРГАРИТА']['size_price'][order_lst['pizza_order']['МАРГАРИТА'][0]['size']]) * int(count_marg.get())  + int(pizza['ГАВАЙСКАЯ']['size_price'][order_lst['pizza_order']['ГАВАЙСКАЯ'][0]['size']]) * int(count_gav.get())
    count = int(count_pep.get()) + int(count_marg.get()) + int(count_gav.get())
    if count >=3:
        total = total - min(int(pizza['ПЕППЕРОНИ']['size_price'][order_lst['pizza_order']['ПЕППЕРОНИ'][0]['size']]),int(pizza['ГАВАЙСКАЯ']['size_price'][order_lst['pizza_order']['ГАВАЙСКАЯ'][0]['size']]),int(pizza['МАРГАРИТА']['size_price'][order_lst['pizza_order']['МАРГАРИТА'][0]['size']]))
    if date.get() == 'Завтра':
        total = total * 0.95
    total_sum.set(total)
    return total



#Строка 0
label = tkinter.Label(window, text = "Выберите пиццы:").grid(row=0,column=0)
label = tkinter.Label(window, text = "Выберите размер:").grid(row=0,column=1)
label = tkinter.Label(window, text = "Укажите количество:").grid(row=0,column=2)

#Строка 1
label = tkinter.Label(window, text = "ПЕППЕРОНИ").grid(row=1,column=0)
combobox = ttk.Combobox(window, values = ['','S', 'M', 'L'], textvariable = size_pep).grid(row=1,column=1)
spinbox = tkinter.Spinbox(window, from_ = 0, to = 100, textvariable = count_pep).grid(row=1,column=2)

#Строка 2
label = tkinter.Label(window, text = "МАРГАРИТА").grid(row=2,column=0)
combobox = ttk.Combobox(window, values = ['','S', 'M', 'L'],  textvariable = size_marg).grid(row=2,column=1)
spinbox = tkinter.Spinbox(window, from_ = 0, to = 100, textvariable = count_marg).grid(row=2,column=2)

#Строка 3
label = tkinter.Label(window, text = "ГАВАЙСКАЯ").grid(row=3,column=0)
combobox = ttk.Combobox(window, values = ['','S', 'M', 'L'], textvariable = size_gav).grid(row=3,column=1)
spinbox = tkinter.Spinbox(window, from_ = 0, to = 100, textvariable = count_gav).grid(row=3,column=2)

#Строка 4
label = tkinter.Label(window, text = "Введите время заказа").grid(row=4,column=0)
label = tkinter.Label(window, text = "Введите адрес заказа:").grid(row=4,column=1)
label = tkinter.Label(window, text = "Введите номер телефона").grid(row=4,column=2)

#Строка 5
entry = tkinter.Entry(window, textvariable = time).grid(row=5,column=0)
entry = tkinter.Entry(window, textvariable = address ).grid(row=5,column=1)
entry = tkinter.Entry(window, textvariable = phone ).grid(row=5,column=2)


#Строка 6
label = tkinter.Label(window, text = "Выберите дату заказа").grid(row=6,column=1)

#Строка 7
combobox = ttk.Combobox(window, values = ['Сегодня','Завтра'], textvariable = date).grid(row=7,column=1)

#Строка 8
label = tkinter.Label(window, text = "Сумма заказа с учетом скидки:").grid(row=8,column=1)

#Строка 9
label = tkinter.Label(window, textvariable = total_sum  ).grid(row=9,column=1) #виджит для вывода суммы заказа

#Строка 10
button = tkinter.Button(window, text='Заказать', command = total_price).grid(row=10,column=1)

#Строка 11
button = tkinter.Button(window, text='Выход', command = window.destroy).grid(row=11,column=1)
