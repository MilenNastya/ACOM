import cv2
import numpy as np

#Задание 2
# img1 = cv2.imread('pic1.png',cv2.IMREAD_GRAYSCALE)
# img2 = cv2.imread('pic1.jpg',cv2.IMREAD_REDUCED_COLOR_8) #считывает изображение в формате BGR, а также уменьшает размер изображения на один-восемь.
# img3 = cv2.imread('pic1.raw',cv2.IMREAD_ANYDEPTH)
# cv2.namedWindow('gray', cv2.WINDOW_NORMAL)
# cv2.namedWindow('bgr', cv2.WINDOW_GUI_EXPANDED)
# cv2.namedWindow('16|32 bit', cv2.WINDOW_AUTOSIZE)
# cv2.imshow('gray',img1)
# cv2.imshow('bgr', img2)
# cv2.imshow('16|32 bit', img3)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


#Задание 3

# cap=cv2.VideoCapture('my_video.mp4',cv2.CAP_ANY)
# while True:
#     ret1, frame1 = cap.read()
#     if not(ret1):
#         break
#     cv2.imshow('mov',frame1)
#     if cv2.waitKey(1) & 0XFF == 27:
#         break
#
# cap1=cv2.VideoCapture('my_video.mp4',cv2.CAP_ANY)
# while True:
#     ret, frame = cap1.read()
#     if not(ret):
#         break
#     gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#     cv2.imshow('mp4',gray)
#     if cv2.waitKey(15) & 0xFF == 27:
#         break
# cap1.release()  # Освобождаем ресурс видео
# cv2.destroyAllWindows()  # Закрываем все окна




# #Задание 4
# cap=cv2.VideoCapture(r'my_video.mp4',cv2.CAP_ANY)
# ret,frame=cap.read()
# w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# video_writer = cv2.VideoWriter("output.mp4", fourcc, 25, (w, h))
# while True:
#     ret, frame = cap.read()
#     if not(ret):
#         break
#     cv2.imshow('mp4',frame)
#     video_writer.write(frame)
#     if cv2.waitKey(1) & 0XFF == 27:
#         break
# cap.release()
# cv2.destroyAllWindows()

#Задание 5
# # чтение изображения
# img = cv2.imread('pic1.jpg')
# # окна для отображения изображений
# cv2.namedWindow('Original Image', cv2.WINDOW_AUTOSIZE)
# cv2.namedWindow('HSV Image', cv2.WINDOW_AUTOSIZE)
# cv2.imshow('Original Image', img)
# # преобразование изображение в формат HSV
# hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# cv2.imshow('HSV Image', hsv)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#Задание 6
#
# cap = cv2.VideoCapture(0)
#
# # Определяем центр кадра
# width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#
# while True:
#     ret, img = cap.read()
#     if not ret:
#         break
#     mirrored_img = cv2.flip(img, 1)
#
#     # Горизонтальный прямоугольник
#     start_point_horizontal = (width // 2 - 100, height // 2 - 20)
#     end_point_horizontal = (width // 2 + 100, height // 2 + 20)
#
#     # Верхний вертикальный прямоугольник
#     start_point_vertical_top = (width // 2 - 20, height // 2 - 100)
#     end_point_vertical_top = (width // 2 + 20, height // 2 - 20)
#
#     # Нижний вертикальный прямоугольник
#     start_point_vertical_bottom = (width // 2 - 20, height // 2 + 20)
#     end_point_vertical_bottom = (width // 2 + 20, height // 2 + 100)
#
#     # Размытие горизонтального региона
#     region_of_interest = mirrored_img[start_point_horizontal[1]:end_point_horizontal[1],
#                          start_point_horizontal[0]:end_point_horizontal[0]]
#     blurred_region = cv2.GaussianBlur(region_of_interest, (25, 25), 0)
#     mirrored_img[start_point_horizontal[1]:end_point_horizontal[1],
#     start_point_horizontal[0]:end_point_horizontal[0]] = blurred_region
#
#     overlay = mirrored_img.copy()
#
#     # Отрисовка прямоугольников
#     cv2.rectangle(overlay, start_point_horizontal, end_point_horizontal, (0, 0, 255), 3)
#     cv2.rectangle(overlay, start_point_vertical_top, end_point_vertical_top, (0, 0, 255), 3)
#     cv2.rectangle(overlay, start_point_vertical_bottom, end_point_vertical_bottom, (0, 0, 255), 3)
#
#     alpha = 0.9
#     mirrored_img = cv2.addWeighted(overlay, alpha, mirrored_img, 1 - alpha, 0)
#
#     cv2.imshow('mp4', mirrored_img)
#     if cv2.waitKey(1) & 0xFF == 27:
#         break
#
# cap.release()
# cv2.destroyAllWindows()

#Задание 7
# def readIPWriteTOFile():
#     video = cv2.VideoCapture(0)
#     ok, img = video.read()
#     w = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
#     h = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
#     fourcc = cv2.VideoWriter_fourcc(*'XVID')
#     video_writer = cv2.VideoWriter("output_2.mp4", fourcc, 25, (w, h))
#     while (True):
#         ok, img = video.read()
#         cv2.imshow('Webcam video', img)
#         video_writer.write(img)
#         # выход при нажатии клавиши 'esc'
#         if cv2.waitKey(1) & 0xFF == 27:
#             break
#             video.release()
#             cv2.destroyAllWindows()
#
# readIPWriteTOFile()

#Задание 8
# cap=cv2.VideoCapture(0)
# width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# while True:
#     ret, frame = cap.read()
#     if not(ret):
#         break
#     sp1 = (int(width/2)-15, int(height/2)-60)
#     ep1 = (int(width/2)+15, int(height/2)+60)
#     sp2 = (int(width/2)-60, int(height/2)-15)
#     ep2 = (int(width/2)+60, int(height/2)+15)
#     blue,green,red=frame[int(width/2)][int(height/2)]
#     color=(blue,green,red)
#     max_val = max(color)
#     max_index = color.index(max_val)
#     color=tuple(255 if i == max_index else 0 for i, x in enumerate(color))
#     print(color)
#     rec1=cv2.rectangle(frame,sp1,ep1,color,-1)
#     res=cv2.rectangle(rec1,sp2,ep2,color,-1)
#     cv2.imshow('mp4',res)
#     if cv2.waitKey(1) & 0XFF == 27:
#         break
# cv2.destroyAllWindows()





