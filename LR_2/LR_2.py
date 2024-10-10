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
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# cap.release()
# cv2.destroyAllWindows()

#     # Задание 2: Применить фильтрацию изображения для выделения красного цвета
#     # Определяем диапазоны для красного цвета
# cap = cv2.VideoCapture(0)
#
# while True:
#     ret, frame = cap.read()
#     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#
#     mask = cv2.inRange(hsv, (140,50,120), (179,255,255))
#     onlyRed_frame = cv2.bitwise_and(frame, frame, mask = mask)
#
#     cv2.imshow('RED OBJ', onlyRed_frame)
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# cap.release()
# cv2.destroyAllWindows()
#
#     # Задание 3: Морфологические преобразования

# cap = cv2.VideoCapture(0)
#
# while True:
#     ret, frame = cap.read()
#     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#
#     mask = cv2.inRange(hsv, (140,50,120), (179,255,255))
#     #mask = cv2.inRange(hsv, lower_red, upper_red)
#
#     kernel = np.ones((5, 5), np.uint8)
#
#     image_opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
#     image_closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
#     cv2.imshow("Open", image_opening)
#     cv2.imshow("Close", image_closing)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# cap.release()
# cv2.destroyAllWindows()
#
# def erode(image, kernel):
#     m, n = image.shape
#     km, kn = kernel.shape
#     hkm = km // 2
#     hkn = kn // 2
#     eroded = np.copy(image)
#
#     for i in range(hkm, m - hkm):
#         for j in range(hkn, n - hkn):
#             eroded[i, j] = np.min(
#                 image[i - hkm:i + hkm + 1, j - hkn:j + hkn + 1][kernel == 1])
#
#     return eroded
#
# def dilate(image, kernel):
#     m, n = image.shape
#     km, kn = kernel.shape
#     hkm = km // 2
#     hkn = kn // 2
#     dilated = np.copy(image)
#
#     for i in range(hkm, m - hkm):
#         for j in range(hkn, n - hkn):
#             dilated[i, j] = np.max(
#                 image[i - hkm:i + hkm + 1, j - hkn:j + hkn + 1][kernel == 1])
#
#     return dilated
#
# #     # Задание 4 и 5: Нахождение моментов и площади объекта
# cap = cv2.VideoCapture(0)
#
# while True:
#     ret, frame = cap.read()
#     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#
#     mask = cv2.inRange(hsv, (140,50,120), (179,255,255))
#     #mask = cv2.inRange(hsv, lower_red, upper_red)
#
#     moments = cv2.moments(mask)
#     area = moments['m00']
#
#     if area > 0:
#         width = height = int(np.sqrt(area))
#         c_x = int(moments["m10"] / moments["m00"])
#         c_y = int(moments["m01"] / moments["m00"])
#         cv2.rectangle(frame,
#             (c_x - (width // 12), c_y - (height // 12)),
#             (c_x + (width // 12), c_y + (height // 12)),
#             (0, 0, 0), 2)
#
#     cv2.imshow('Rectanle_frame', frame)
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# cap.release()
# cv2.destroyAllWindows()
