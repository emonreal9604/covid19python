import cv2

imgcapture = cv2.VideoCapture(0)
results = True

while(results):
    ret, frame = imgcapture.read()
    cv2.imwrite("xd.jpg", frame)
    results = False
    print("Image Captured..")

imgcapture.release()