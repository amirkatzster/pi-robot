
import logging
import pika
import sys
from services.queue import queue
import os, shutil
import cv2
import numpy as np
from services.logger import setLogger

class cameraService:

	EXCHANGE_NAME = '' 
	QUEUE_NAME = 'cameraService'

	def __init__(self):
		setLogger('cameraService')
		self.queue = queue()
		self.channel = self.queue.createChannel()
		self.recognizer = cv2.face.LBPHFaceRecognizer_create()
		self.recognizer.read('resources/trainer/trainer.yml')
		cascadePath = "resources/haarcascade_frontalface_default.xml"
		self.faceCascade = cv2.CascadeClassifier(cascadePath);
		self.font = cv2.FONT_HERSHEY_SIMPLEX
		self.id = 0
		# names related to ids: example ==> Marcelo: id=1,  etc
		self.names = ['None', 'Amir', 'Anat', 'Ety', 'Ofek', 'Staav','Gefen']
		# Initialize and start realtime video capture
		self.cam = cv2.VideoCapture(0)
		self.cam.set(3, 640) # set video widht
		self.cam.set(4, 480) # set video height
		# Define min window size to be recognized as a face
		self.minW = 0.1*self.cam.get(3)
		self.minH = 0.1*self.cam.get(4)

	def run(self): 
		logging.info('---starting to record---')
		while True:
			ret, img = self.cam.read()
			gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
			faces = self.faceCascade.detectMultiScale(
				gray,
				scaleFactor = 1.2,
				minNeighbors = 5,
				minSize = (int(self.minW), int(self.minH)),
			)

			for(x,y,w,h) in faces:
				cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
				id, confidence = self.recognizer.predict(gray[y:y+h,x:x+w])
        			# Check if confidence is less them 100 ==> "0" is perfect match 
				if (confidence < 100):
					conf = confidence
					print(self.names[id])
					print(conf)
					id = self.names[id]
					confidence = "  {0}%".format(round(100 - confidence))
					if (self.id != id and conf < 50):
						self.id = id
						self.channel.basic_publish(self.EXCHANGE_NAME,'translateServiceE2H','Hi {}.'.format(id))                                
				else:
					id = "unknown"
					confidence = "  {0}%".format(round(100 - confidence))
				cv2.putText(img, str(id), (x+5,y-5), self.font, 1, (255,255,255), 2)
				cv2.putText(img, str(confidence), (x+5,y+h-5), self.font, 1, (255,255,0), 1)   
			cv2.imshow('camera',img)

			k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
			if k == 27:
				break

		# Do a bit of cleanup
		print("\n [INFO] Exiting Program and cleanup stuff")
		self.cam.release()
		cv2.destroyAllWindows()




	def callback(self, ch, method, properties, body):
		print(" [x] %r" % body)


if __name__ == "__main__":
    cameraService().run()
