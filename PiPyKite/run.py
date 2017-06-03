#! /usr/bin/python3

from flask import Flask
from flask import url_for, render_template
from camera import PiPyCam
import re
import os

cameraFolderName = 'static/dcim/'

app = Flask(__name__)












def get_camera_max_number_from_filenames(folderName):
	highwatermark = 0
	for subdir, dirs, files in os.walk(folderName):
		for file in files:
			if file.startswith("dcim") and file.endswith("jpg"):
				filenumber = get_first_integer_group(file)
				if filenumber > highwatermark: highwatermark = filenumber
	return highwatermark


def get_first_integer_group(value):
	"""Returns the first integer group from a string"""
	return int(re.search(r'\d+', value).group(0))


def update_camera_filename_high_watermark(folderName, highwatermark):
	with open(folderName+'settings.conf', 'w') as f:
		print(highwatermark, file=f)


def get_camera_filename_highwatermark(folderName):
	#with open(folderName+'settings.conf', 'r') as f:
	return False
		
def get_camera_highwatermark(folderName):
	with open(folderName+'settings.conf', 'r') as f:
		return int(f.readline())
		
		
@app.route("/test/highwatermark")
def test_highwatermark():
	return str(get_camera_highwatermark(cameraFolderName))
		
@app.route("/")
@app.route("/camera")
@app.route("/camera/")
def camera_ui():
    return render_template("camera.html")

@app.route("/gallery")
def gallery_ui():
    return render_template("gallery.html")

@app.route("/gallery/showpicture/<id>")
def show_picture(id):
    return render_template("showpicture.html")

@app.route("/api/camera/takepicture", methods=['GET', 'POST'])
def take_picture():
    cam = PiPyCam() #(url_for('static', filename=cameraFolderName))
    newHighWatermark = get_camera_highwatermark(cameraFolderName) + 1
    result = cam.TakePicture('{0}dcim{1:04d}.jpg'.format(cameraFolderName, newHighWatermark))
    update_camera_filename_high_watermark(cameraFolderName, newHighWatermark)
    
    return result





@app.before_first_request
def before_first_request():
	highwatermark = get_camera_max_number_from_filenames(cameraFolderName)
	update_camera_filename_high_watermark(cameraFolderName, highwatermark)






@app.route("/api/camera/setresolution", methods=['POST'])
def set_camera_resolution():
    return False;


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)


















