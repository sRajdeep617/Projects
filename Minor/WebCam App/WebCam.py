# using web cam to click photo
import cv2

imgCapture = cv2.VideoCapture(0)
result = True

while (result):
    ret, frame = imgCapture.read()
    cv2.imwrite('test.jpg', frame)
    result = False
    print('Image captured...')

imgCapture.release()