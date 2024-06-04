from gpiozero import Motor
from time import sleep

# Создаем объекты для двух моторов, указывая GPIO пины
left_motor = Motor(forward=4, backward=14)  # Мотор подключен к пинам 4 и 14
right_motor = Motor(forward=17, backward=18)  # Мотор подключен к пинам 17 и 18

def forward():
    left_motor.forward()
    right_motor.forward()
    print("Робот движется вперед")

def backward():
    left_motor.backward()
    right_motor.backward()
    print("Робот движется назад")

def left():
    left_motor.backward()
    right_motor.forward()
    print("Робот поворачивает налево")

def right():
    left_motor.forward()
    right_motor.backward()
    print("Робот поворачивает направо")

def stop():
    left_motor.stop()
    right_motor.stop()
    print("Робот остановлен")

try:
    while True:
        command = input("Введите команду (w - вперед, s - назад, a - влево, d - вправо, q - стоп): ")

        if command == 'w':
            forward()
        elif command == 's':
            backward()
        elif command == 'a':
            left()
        elif command == 'd':
            right()
        elif command == 'q':
            stop()
        else:
            print("Неверная команда")

        sleep(1)  # Пауза для выполнения команды
        stop()  # Останавливаем моторы после выполнения команды

except KeyboardInterrupt:
    stop()
    print("Программа завершена")
    