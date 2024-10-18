import cv2
import numpy as np

def gaussian_function(x, y, sigma, center_x, center_y):
    coefficient = 1 / (2 * np.pi * (sigma ** 2))
    exponent = np.exp(-((x - center_x) ** 2 + (y - center_y) ** 2) / (2 * (sigma ** 2)))
    return coefficient * exponent

def gaussian_blur(input_image, kernel_dimension, sigma_value):
    kernel_matrix = np.ones((kernel_dimension, kernel_dimension))
    center = (kernel_dimension - 1) / 2

    # Заполнение ядра значениями функции Гаусса
    for i in range(kernel_dimension):
        for j in range(kernel_dimension):
            kernel_matrix[i, j] = gaussian_function(i, j, sigma_value, center, center)

    print("Kernel Matrix for size: ", kernel_dimension)
    print(kernel_matrix)

    # Нормализация ядра
    kernel_sum = kernel_matrix.sum()
    kernel_matrix /= kernel_sum
    print("Normalized Kernel Matrix: \n", kernel_matrix, "\n")

    blurred_image = input_image.copy()
    offset = kernel_dimension // 2

    # Применение гауссового размывания
    for y in range(offset, blurred_image.shape[0] - offset):
        for x in range(offset, blurred_image.shape[1] - offset):
            pixel_value = 0
            for ky in range(-offset, offset + 1):
                for kx in range(-offset, offset + 1):
                    pixel_value += input_image[y + ky, x + kx] * kernel_matrix[ky + offset, kx + offset]
            blurred_image[y, x] = pixel_value
    return blurred_image

# Загрузка изображения и применение фильтра
original_image = cv2.imread("nuvotivsi.jpg", cv2.IMREAD_GRAYSCALE)
blurred_1 = gaussian_blur(original_image, 3, 100)
# blurred_2 = gaussian_blur(original_image, 3, 10)
# blurred_3 = gaussian_blur(original_image, 5, 100)
# blurred_4 = gaussian_blur(original_image, 5, 10)
# blurred_5 = gaussian_blur(original_image, 7, 10)
blurred_6 = gaussian_blur(original_image, 11, 100)

# Размер для отображения
scaling_factor = 50
new_width = int(original_image.shape[1] * scaling_factor / 100)
new_height = int(original_image.shape[0] * scaling_factor / 100)
new_dimensions = (new_width, new_height)

resized_original = cv2.resize(original_image, new_dimensions, interpolation=cv2.INTER_AREA)
resized_blur1 = cv2.resize(blurred_1, new_dimensions, interpolation=cv2.INTER_AREA)
# resized_blur2 = cv2.resize(blurred_2, new_dimensions, interpolation=cv2.INTER_AREA)
# resized_blur3 = cv2.resize(blurred_3, new_dimensions, interpolation=cv2.INTER_AREA)
# resized_blur4 = cv2.resize(blurred_4, new_dimensions, interpolation=cv2.INTER_AREA)
# resized_blur5 = cv2.resize(blurred_5, new_dimensions, interpolation=cv2.INTER_AREA)
resized_blur6 = cv2.resize(blurred_6, new_dimensions, interpolation=cv2.INTER_AREA)

cv2.imshow("Original Image", resized_original)
cv2.imshow("Kernel size 3 | Std Dev 100", resized_blur1)
# cv2.imshow("Kernel size 3 | Std Dev 10", resized_blur2)
# cv2.imshow("Kernel size 5 | Std Dev 100", resized_blur3)
# cv2.imshow("Kernel size 5 | Std Dev 10", resized_blur4)
# cv2.imshow("Kernel size 7 | Std Dev 100", resized_blur5)
cv2.imshow("Kernel size 7 | Std Dev 100", resized_blur6)
cv2.waitKey(0)
cv2.destroyAllWindows()
