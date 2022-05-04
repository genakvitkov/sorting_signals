# основная программа

from random import *
from tkinter import *    # Стандартная библиотека для создания графического интерфейса

Green = 0
Blue = 1
Red = 2
signals = [Green, Blue, Red]

                                              # Функция создания случайного массива элементов Green, Red, Blue
def unsorted():                               # Знаю, что глобальные переменные - не лучшая практика, но на текущем
    global unsorted_array                     # уровне своих навыков могу реализовать только так.
    unsorted_array = choices(signals, k=16)   # Число элементов неупорядоченного массива взял из примера в ТЗ, была
                                              # идея сделать это число случайным, возможно реализую в следующем билде)).

def sorted_s():                               # Функция сортировки. Сортировка реализована методом подсчёта, т.к.
    global sorted_array                       # диапазон возможных значений невелик, и их легко посчитать и вывести
    sorted_array = []                         # в нужном количестве и порядке. Для этого создаём сначала пустой массив,
    count = [0] * len(signals)                # затем счётчик: массив нулей, размером равный числу возможных значений.
    for i in unsorted_array:                  # Для каждого элемента неупорядоченного массива увеличиваем на 1 элемент
        count[i] += 1                         # массива-счётчика с индексом, равным значению из сортируемого массива.
    for i in range(len(count)):               # Теперь добавляем в ранее созданный пустой массив числа из диапазона
        sorted_array.extend([i] * count[i])   # длины счётчика столько раз, сколько оно записано в счётчик, причём число
                                              # из диапазона длины - это и есть нужное значение сортируемого массива

# тестирующие функции


def tests_unsorted():
    if len(unsorted_array) != 0:                   # Проверяем, что созданный массив не пустой.
        print("Test_1: passed")
    else:
        print("Test_1: failed")

    if all(i in unsorted_array for i in signals):  # Проверяем, что в созданном массиве присутствуют элементы всех
        print("Test_2: passed")                    # трёх цветов. Опасная для моего варианта реализации проверка, т.к.
    else:                                          # метод choices не гарантирует, что вернётся каждый элемент.
        print("Test_2: failed")                    # Но исходя из ТЗ такая проверка должна быть.

    if unsorted_array != sorted(unsorted_array):   # Проверяем, что неупорядоченный массив действительно неупорядочен.
        print("Test_3: passed")                    # Возможно, эта проверка избыточна, т.к. вполне возможен вариант,
    else:                                          # когда порядок элементов в новом массиве случайно совпадёт с
        print("Test_3: failed")                    # порядком в отсортированном и с т.з. логики программы, ошибкой
                                                   # это не будет. Но если подходить к ТЗ буквально, то такая проверка
                                                   # должна быть

def tests_sorted():
    if sorted_array == sorted(unsorted_array):     # Проверяем, что массив действительно отсортировался.
        print("Test_4: passed")                    # Этот же тест, по сути, проверяет, что число зелёных,
    else:                                          # синих, и красных элементов равно в обоих массивах,
        print("Test_4: failed")                    # и что длина обоих массивов одинакова, поэтому я не стал
                                                   # выносить эти проверки в отдельные тесты


# графический интерфейс


def switch_btn_2_state():            # Это небольшой костыль, который делает кнопку сортировки доступной только
    btn_2["state"] = NORMAL          # после нажатия кнопки генерации массива, чтобы функция сортировки не обращалсь
                                     # к массиву, который ещё не создан.

def clicked_unsorted():                                          # Функция кнопки генерации массива
    unsorted()
    colors = {Green: "green", Blue: "blue", Red: "red"}
    position = 70
    for i in unsorted_array:
        color = colors[i]
        frame_1 = Frame(window, width=20, height=20, bg=color)
        frame_1.place(x=position, y=125)
        position += 30
    tests_unsorted()
    switch_btn_2_state()


def clicked_sorted():                                         # Функция кнопки сортировки
    sorted_s()
    colors = {Green: "green", Blue: "blue", Red: "red"}
    position = 70
    for i in sorted_array:
        color = colors[i]
        frame_1 = Frame(window, width=20, height=20, bg=color)
        frame_1.place(x=position, y=185)
        position += 30
    tests_sorted()


window = Tk()
window.title("sorting signals")
window.geometry("600x400")
btn_1 = Button(window, text="generate signals", command=clicked_unsorted)
btn_1.pack()
btn_2 = Button(window, text="sort signals", state=DISABLED, command=clicked_sorted)  # По умолчанию кнопка сортировки
btn_2.pack()                                                                         # отключена.
window.mainloop()



