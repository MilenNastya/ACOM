import cv2
import numpy as np


# реализация операции свёртки
def Convolution(img, kernel):
    kernel_size = len(kernel)
    x_start = kernel_size // 2
    y_start = kernel_size // 2
    # переопределение матрицы изображения для работы с каждым внутренним пикселем
    matr = np.zeros(img.shape)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if i < x_start or i >= img.shape[0] - x_start or j < y_start or j >= img.shape[1] - y_start:
                continue  # Пропустить краевые пиксели
            # операция свёртки
            val = 0
            for k in range(-x_start, x_start + 1):
                for l in range(-y_start, y_start + 1):
                    val += img[i + k][j + l] * kernel[k + x_start][l + y_start]
            matr[i][j] = val
    return matr


# нахождение округления угла между вектором градиента и осью Х
def get_angle_number(x, y):
    if x == 0 and y == 0:
        return 0  # Обработка случая, когда (x, y) = (0, 0)

    tg = y / x if x != 0 else float('inf')
    if (x < 0):
        if (y < 0):
            if (tg > 2.414):
                return 0
            elif (tg < 0.414):
                return 6
            else:
                return 7
        else:
            if (tg < -2.414):
                return 4
            elif (tg < -0.414):
                return 5
            else:
                return 6
    else:
        if (y < 0):
            if (tg < -2.414):
                return 0
            elif (tg < -0.414):
                return 1
            else:
                return 2
        else:
            if (tg < 0.414):
                return 2
            elif (tg < 2.414):
                return 3
            else:
                return 4


def main(path, standard_deviation, kernel_size):
    # Задание 1 - чтение строки полного адреса изображения и размытие Гаусса
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    imgBlur_CV2 = cv2.GaussianBlur(img, (kernel_size, kernel_size), standard_deviation)
    cv2.imshow('Blurred Image', imgBlur_CV2)

    # Задание 2 - вычисление и вывод матрицы значений длин и матрицы значений углов градиентов
    # Задание матриц оператора Собеля
    Gx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    Gy = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

    # применение операции свёртки
    img_Gx = Convolution(imgBlur_CV2, Gx)
    img_Gy = Convolution(imgBlur_CV2, Gy)

    # нахождение матрицы длины вектора градиента
    matr_gradient = np.sqrt(img_Gx ** 2 + img_Gy ** 2)

    # нахождение матрицы значений углов градиента
    img_angles = np.zeros(img.shape)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            img_angles[i][j] = get_angle_number(img_Gx[i][j], img_Gy[i][j])

    # вывод матрицы значений длин градиента
    max_gradient = np.max(matr_gradient)
    img_gradient_to_print = (matr_gradient / max_gradient) * 255
    cv2.imshow('Gradient Magnitude', img_gradient_to_print.astype(np.uint8))

    print('Матрица значений длин градиента:')
    print(img_gradient_to_print)

    # вывод матрицы значений углов градиента
    img_angles_to_print = (img_angles / 7) * 255  # необходимо для корректного отображения на экране
    cv2.imshow('Gradient Angles', img_angles_to_print.astype(np.uint8))

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Пример вызова функции main
# Убедитесь, что путь к изображению и параметры правильные
# main('pic1.jpg', 1.5, 5)
main('pic1.jpg', 5, 5)
