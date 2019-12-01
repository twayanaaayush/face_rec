import face_rec
import cv2
import serial
import time

# print(face_rec.classify_face("test.jpg"))

ser = serial.Serial()
ser.port = 'COM6'
ser.baudrate = 9600
ser.open()

n = 0
final_faces = []

while n < 1:
	# so basically this loop should contain the entire process of capturing
	# and recognising the faces in the captured images!!

	video = cv2.VideoCapture(0)

	for i in range(1,4):
		check, frame = video.read()
		cv2.imwrite("unknown{}.jpg".format(i), frame)

	video.release()

	for i in range(1,4):
		recognised_faces = face_rec.classify_face("unknown{}.jpg".format(i))
		for face in recognised_faces:
			if face not in final_faces:
				final_faces.append(face)

	for face in final_faces:
		print(face) 		
		ser.write(face.encode('utf-8'))
		time.sleep(2)

	n = n + 1


ser.close()
