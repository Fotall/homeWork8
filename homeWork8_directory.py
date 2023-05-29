def input_name():
    with open('directory.txt', 'a') as data:
        n = input('Введите данные человека: ')
        data.write(n + '\n')

def export():
    with open('directory.txt', 'r') as data:
        m = input('Введите данные человека: ')
        text = data.read()
        name = ''
        t = ''
        soname = ''
        # print(type(text))
        # print(text)
        for i in text:
            if i != ' ':
                name += i
            else:
                # print(name)
                if name == m:
                    t = name
                name = ''
        print(t)
        if t != '':
            print('Bот его номер:', name)
        elif m == name:
            for i in text:
                if i != ' ':
                    soname += i
                else:
                    print(soname)
                    break
        else:
            print('его пока нет в базе')
        name = ''
def launch():
    lch = int(input('Укажите цифру, что вы хотите: 1 - ввести данные в справочник, 2 - поиск по имени(фамилии) номера'))
    if lch == 1:
        input_name()
    elif lch == 2:
        export()
    else:
        print('не правильно нажали на кнопку')
launch()


