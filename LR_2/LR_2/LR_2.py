import cv2
import numpy as np

# Задание 1: Прочитать изображение с камеры и перевести его в формат HSV
# cap = cv2.VideoCapture(0)
#
# while True:
#     ret, frame = cap.read()
#     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#
#     cv2.imshow('HSV', hsv)
#
#     if cv2.waitKey(1) & 0xFF == 27:
#         break
#
# cap.release()
# cv2.destroyAllWindows()

#     # Задание 2: Применить фильтрацию изображения для выделения фиолетового цвета
#     # Определяем диапазоны для красного цвета
# cap = cv2.VideoCapture(0)
# while True:
#     ret, frame= cap.read()
#     hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#     violet_mask = cv2.inRange(hsv_image, (130, 50, 120), (160, 255, 255))
#     highlighted_violet = cv2.bitwise_and(frame, frame, mask=violet_mask)
#     cv2.imshow('VIOLET OBJECTS', highlighted_violet)
#     if cv2.waitKey(1) & 0xFF == 27:
#         break
#
# # Освобождаем ресурсы
# cap.release()
# cv2.destroyAllWindows()

#
# #     # Задание 3: Морфологические преобразования
# cap = cv2.VideoCapture(0)
# while True:
#     ret, frame = cap.read()
#     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#     # определение диапазона красного цвета в HSV
#     lower_red = np.array([0, 0, 100])  # минимальные значения оттенка, насыщенности и значения(яркости)
#     upper_red = np.array([100, 100, 255])  # максимальные значения оттенка, насыщенности и значения(яркости)
#     # Маска - бинарное изображение, где пиксели, соответствующие заданному диапазону цвета, имеют значение 255 (белый), а остальные пиксели имеют значение 0 (черный).
#     mask = cv2.inRange(hsv, lower_red, upper_red)
#     # применение маски на изображение
#     res = cv2.bitwise_and(frame, frame, mask=mask)
#     # структурирующий элемент(определяет размер и форму области)
#     kernel = np.ones((5, 5), np.uint8)
#     # применение операции открытия - позволяет удалить шумы и мелкие объекты на изображении(удаление нежелательных пикселей или деталей)
#     opening = cv2.morphologyEx(res, cv2.MORPH_OPEN, kernel)
#     # применение операции закрытия - позволяет заполнить маленькие пробелы и разрывы в объектах на изображении
#     closing = cv2.morphologyEx(res, cv2.MORPH_CLOSE, kernel)
#     cv2.imshow('Opening', opening)
#     cv2.imshow('Closing', closing)
#     if cv2.waitKey(1) & 0xFF == 27:
#         break
# cap.release()
# cv2.destroyAllWindows()

# 4- 5 задание
cap = cv2.VideoCapture(0)
previous_cx, previous_cy = None, None
alpha = 0.6  # коэффициент сглаживания
while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_purple = np.array([130, 50, 50])  # минимальные значения оттенка, насыщенности и значения (яркости)
    upper_purple = np.array([160, 255, 255]) # максимальные значения оттенка, насыщенности и значения (яркости)
    mask = cv2.inRange(hsv, lower_purple, upper_purple)

    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    blurred = cv2.GaussianBlur(mask, (5, 5), 0)
    moments = cv2.moments(blurred)
    area = moments['m00']

    if area > 500:  # минимальная площадь для отсечения шумов
        # ширина и высота прямоугольника равны квадратному корню из площади объекта
        width = height = int(np.sqrt(area))
        # вычисление координат центра объекта на изображении с использованием момент первого порядка
        c_x = int(moments["m10"] / moments["m00"])
        c_y = int(moments["m01"] / moments["m00"])

        # Сглаживание движения прямоугольника
        if previous_cx is not None and previous_cy is not None:
            c_x = int(alpha * previous_cx + (1 - alpha) * c_x)
            c_y = int(alpha * previous_cy + (1 - alpha) * c_y)

        previous_cx, previous_cy = c_x, c_y
        color = (0, 0, 0) # черный цвет
        thickness = 2 # толщина
        cv2.rectangle(frame,
            (c_x - (width // 20), c_y - (height // 20)),
            (c_x + (width // 20), c_y + (height // 20)),
            color, thickness)

    cv2.imshow('HSV_frame', hsv)
    cv2.imshow('Result_frame', frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()


