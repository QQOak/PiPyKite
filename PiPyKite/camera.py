import time
import picamera
import os

class PiPyCam:
	"""Encapsulates the functionality needed to take a picture"""

	#def __init__(self, folder):
	#	self.cameraImagesPath = folder

	def TakePicture(self, filename):
		with picamera.PiCamera() as camera:
			camera.resolution = (1024, 768)
			#camera.start_preview
			# Camera warm-up time
			#time.sleep(2)
			camera.capture(filename)
			
			return "{{ \"filename\": \"{0}\" }}".format(filename)
