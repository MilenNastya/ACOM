import cv2


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
# чтение изображения
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
# cap = cv2.VideoCapture(0)
# frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# while True:
#     ret, frame = cap.read()
#     if not(ret):
#         break
#     flipped_frame = cv2.flip(frame, 1)
#     sp1 = (int(frame_width/2)-15, int(frame_height/2)-60)
#     ep1 = (int(frame_width/2)+15, int(frame_height/2)+60)
#     sp2 = (int(frame_width/2)-60, int(frame_height/2)-15)
#     ep2 = (int(frame_width/2)+60, int(frame_height/2)+15)
#     roi1 = flipped_frame[sp2[1]:ep2[1], sp2[0]:ep2[0]]
#     blurred_roi1 = cv2.GaussianBlur(roi1, (25, 25), 0)
#     flipped_frame[sp2[1]:ep2[1], sp2[0]:ep2[0]] = blurred_roi1
#     cv2.rectangle(flipped_frame, sp1, ep1, (0, 0, 255), 2)
#     cv2.rectangle(flipped_frame, sp2, ep2, (0, 0, 255), 2)
#     cv2.imshow('mp4', flipped_frame)
#     if cv2.waitKey(1) & 0XFF == 27:
#         break
# cap.release()
# cv2.destroyAllWindows()

#Задание 7
def readIPWriteTOFile():
    video = cv2.VideoCapture(0)
    ok, img = video.read()
    w = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    video_writer = cv2.VideoWriter("output_2.mp4", fourcc, 25, (w, h))
    while (True):
        ok, img = video.read()
        cv2.imshow('Webcam video', img)
        video_writer.write(img)
        # выход при нажатии клавиши 'esc'
        if cv2.waitKey(1) & 0xFF == 27:
            break
            video.release()
            cv2.destroyAllWindows()

readIPWriteTOFile()

#Задание 8
# cap=cv2.VideoCapture(0)
# frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# while True:
#     ret, frame = cap.read()
#     if not(ret):
#         break
#     sp1 = (int(frame_width/2)-15, int(frame_height/2)-60)
#     ep1 = (int(frame_width/2)+15, int(frame_height/2)+60)
#     sp2 = (int(frame_width/2)-60, int(frame_height/2)-15)
#     ep2 = (int(frame_width/2)+60, int(frame_height/2)+15)
#     blue,green,red=frame[int(frame_width/2)][int(frame_height/2)]
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

# #Задание 9
# cap=cv2.VideoCapture("rtsp://192.168.35.68:8080/h264_pcm.sdp")
# while True:
#     ret, frame = cap.read()
#     if not(ret):
#         break
#     cv2.imshow('mp4',frame)
#     if cv2.waitKey(1) & 0XFF == 27:
#         break

# url = "http://192.168.1.114:8080/h264_pcm.sdp"
#
# # Создайте VideoCapture объект с указанным URL
# cap = cv2.VideoCapture(url)
#
# # Проверьте, был ли поток успешно открыт
# if not cap.isOpened():
#     print("Не удалось подключиться к камере. Проверьте URL и соединение.")
#     exit()
#
# while True:
#     ret, frame = cap.read()
#
#     if not ret:
#         print("Не удается получить кадр. Попробуйте проверить соединение.")
#         break
#
#     # Отображение кадра
#     cv2.imshow('Видео с камеры телефона', frame)
#
#     # Условие для выхода из цикла по нажатию клавиши 'ESC'
#     if cv2.waitKey(1) & 0xFF == 27:
#         break
#
# # Освобождаем ресурсы
# cap.release()
# cv2.destroyAllWindows()



