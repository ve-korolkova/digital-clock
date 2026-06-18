# Импортируем необходимые модули из стандартной библиотеки
from tkinter import Tk, Label, Frame, Button
from time import strftime
import datetime

# Флаг для формата времени (24-часовой по умолчанию)
use_24h_format = True
# Флаг для текущей темы (тёмная по умолчанию)
current_theme = "dark"

# Создаём главное окно приложения
root = Tk()
root.title("Мои цифровые часы")

# Устанавливаем размер окна и запрещаем его изменение
root.geometry("400x200")
root.resizable(width=False, height=False)

# Создаём основной фрейм для центрирования содержимого
main_frame = Frame(root)
main_frame.pack(expand=True)

# Метка для отображения времени
time_label = Label(
    main_frame,
    font=('Helvetica', 36, 'bold'),
    background='black',
    foreground='cyan',
    padx=20,
    pady=10
)
time_label.pack(pady=(0, 10))

# Новая метка для отображения даты
date_label = Label(
    root,
    font=('calibri', 20),
    background='purple',
    foreground='lightgray'
)
date_label.pack(anchor='center')

# Кнопка для переключения формата времени
def toggle_time_format():
    global use_24h_format
    use_24h_format = not use_24h_format
    # Обновляем отображение сразу после переключения
    update_clock()

format_button = Button(
    main_frame,
    text="12/24ч",
    command=toggle_time_format,
    bg='gray',
    fg='white'
)
format_button.pack(pady=5)

# Функция смены темы
def toggle_theme():
    global current_theme
    if current_theme == "dark":
        # Светлая тема
        root.configure(background='white')
        time_label.configure(background='white', foreground='black')
        date_label.configure(background='white', foreground='gray')
        format_button.configure(bg='lightgray', fg='black')
        current_theme = "light"
    else:
        # Тёмная тема
        root.configure(background='black')
        time_label.configure(background='black', foreground='cyan')
        date_label.configure(background='black', foreground='lightblue')
        format_button.configure(bg='gray', fg='white')
        current_theme = "dark"

# Кнопка для смены темы
theme_button = Button(
    main_frame,
    text="Тема",
    command=toggle_theme,
    bg='gray',
    fg='white'
)
theme_button.pack(pady=5)

# Функция обновления времени и даты
def update_clock():
    # Получаем текущее время
    current_time_str = strftime('%H:%M:%S')

    # Мигание секунд (двоеточие мигает каждую секунду)
    if int(strftime('%S')) % 2 == 0:
        current_time = current_time_str
    else:
        # Заменяем последнее двоеточие на пробел, чтобы создать эффект мигания
        current_time = current_time_str[:-3] + ' ' + current_time_str[-2:]

    # Получаем текущее время в зависимости от выбранного формата (с учётом мигания)
    if use_24h_format:
        pass  # current_time уже содержит нужное значение с миганием
    else:
        # Для 12‑часового формата берём исходное время без мигания для преобразования
        original_time = strftime('%I:%M:%S %p')
        if int(strftime('%S')) % 2 == 0:
            current_time = original_time
        else:
            current_time = original_time[:-3] + ' ' + original_time[-2:]

    # Получаем текущую дату
    current_date = strftime('%d.%m.%Y')  # Используем strftime для единообразия

    # Обновляем текст в метках
    time_label.config(text=current_time)
    date_label.config(text=current_date)  # Обновляем новую метку с датой

    # Планируем следующее обновление через 1000 мс (1 секунда)
    root.after(1000, update_clock)

# Дополнительная функция для инициализации
def init_app():
    """Инициализация приложения: настройка и запуск обновления"""
    print("Приложение запущено. Часы стартуют...")
    update_clock()  # Запускаем обновление сразу после запуска

# Запускаем инициализацию приложения
init_app()

# Основной цикл приложения
root.mainloop()
