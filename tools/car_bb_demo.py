import os
import keras
from keras.models import load_model
import cv2
from keras.models import Sequential
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

 
path_to_test_dictionary = '/home/michalm/Desktop/auto_test'
video_path = '/home/michalm/Desktop/POC_GATE/wyjazd.mp4'

x_size = 297
y_size = 166
screnn_size_x = 1920
screnn_size_y = 1080
m_x = screnn_size_x/x_size
m_y = screnn_size_y/y_size


def find_car(network):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Błąd: Nie udało się otworzyć pliku wideo.")
    else:
        print("Wideo zostało pomyślnie otwarte.")
   
    i = 0 
    j = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Nie udało się odczytać klatki wideo. Koniec strumienia.")
            break

        print(f'FRAME SIZE {frame.shape}')
        image_prepared = __preapre_image_for_proccesing(frame)
        result = network.predict(image_prepared)
        print(result)
        draw_squer(frame,result[0])
        # print(f'KLASA : { np.argmax(result)}')
        # if np.argmax(result) == 1:
        #     i += 1

        # j+=1
        # frame = cv2.resize(frame, (x_size, y_size))   
        cv2.imshow('Klatka', frame)  # Wyświetl klatkę
        if cv2.waitKey(25) & 0xFF == ord('q'):  # Naciśnij 'q', aby zakończyć
            break
    cap.release()
    cv2.destroyAllWindows()
    print(f'J = {j} I = {i}')


def show_test_set(network):
    test_set = __load_images()
    for img in test_set:
        image_prepared = __preapre_image_for_proccesing(img)
        boxes = network.predict(image_prepared)
        print('PRDICT : ',boxes)
        draw_squer_mat(boxes[0],image_prepared)

def draw_squer(frame, bounding_box):
    color = (255, 0, 0) 
    thickness = 2  
    p1 = (int(bounding_box[0]*x_size*m_x), int(bounding_box[1]*y_size*m_y))
    p2 = (int(bounding_box[2]*x_size*m_x), int(bounding_box[1]*y_size*m_y))
    p3 = (int(bounding_box[2]*x_size*m_x), int(bounding_box[3]*y_size*m_y))
    p4 = (int(bounding_box[0]*x_size*m_x), int(bounding_box[3]*y_size*m_y))
    cv2.line(frame, p1, p4, color, thickness) 
    cv2.line(frame, p4, p3, color, thickness)
    cv2.line(frame, p3, p2, color, thickness)
    cv2.line(frame, p2, p1, color, thickness)


def __preapre_image_for_proccesing(img):
    image = cv2.resize(img, (x_size, y_size))
    image = image[np.newaxis, ...]
    return image.astype('float32')/255

def __load_images():
    images = []
    for filename in os.listdir(path_to_test_dictionary):
        img_path = os.path.join(path_to_test_dictionary, filename)
        images.append(cv2.imread(img_path, 1))
    return images 



def draw_squer_mat(bounding_box,img):
    print(bounding_box)
    x = [int(bounding_box[0]*x_size),int(bounding_box[0]*x_size),int(bounding_box[2]*x_size),int(bounding_box[2]*x_size)]
    y = [int(bounding_box[1]*y_size),int(bounding_box[3]*y_size),int(bounding_box[3]*y_size),int(bounding_box[1]*y_size)]
    fig, ax = plt.subplots()
    ax.imshow(img[0])
    rectangle = patches.Polygon(np.column_stack((x, y)), closed=True, linewidth=2, edgecolor='r', facecolor='none')
    ax.add_patch(rectangle)
    plt.xlabel('Współrzędna X')
    plt.ylabel('Współrzędna Y')
    plt.title('Wyznaczone auto')
    plt.show()


if __name__ == "__main__":
    network = load_model('/home/michalm/Desktop/POC_GATE/sieci/car_boxes_model')
    find_car(network)
    # show_test_set(network)