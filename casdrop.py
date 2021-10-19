#!/usr/bin/python3 
# python --version => 3.9.7
# This script streams media files to
# chrome devices by placing your file
# in the ./chromecast of a running server 
# this script can also stream remote content
# from other devices 

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os, json, time, sys, logging
import pychromecast



watch_folder=os.environ.get("CASDROP_WATCH_FOLDER")
host_url=os.environ.get("CASDROP_SERVER_URL")
now_playing=None


print("\nLoading...")

try:
	services, browser = pychromecast.discovery.discover_chromecasts()# Search for chromecasts
	pychromecast.discovery.stop_discovery(browser) #stop the search
	print("\n\n[Ready to cast.]\n\n Drop your file (.mp4 || .mp3)\n  => ", watch_folder)
except:
	print("Can not fine a chromedevice(s) on your network")



def connect(devicename):
	try: 
		# # Discover and connect to chromecasts named <devicename>
		chromecasts, browser = pychromecast.get_listed_chromecasts(friendly_names=[devicename])
		# search by friendly name
		[cc.device.friendly_name for cc in chromecasts] 
		[devicename]

		cast = chromecasts[0]
		# # Start worker thread and wait for cast device to be ready
		cast.wait()
		print("\n\n[Connection Successful! ]\n\n\n[",cast.status, "]\n\n\n\n\n[", cast.device, "]")
		return cast
	except:
		return "Connection Error!"

pass


def chromecast(filename):
	extension = os.path.splitext(filename)[1]

	if (extension == ".mp4"):
		logging.info("Casting to TV....")
		mc = connect(os.environ.get("CASDROP_TV_NAME")).media_controller
		mc.play_media(host_url+filename, 'video/mp4')
		mc.block_until_active()
		return mc.status

	elif (extension == ".mp3"): 
		logging.info("Casting to TV....")
		mc = connect(os.environ.get("CASDROP_SPKR_NAME")).media_controller
		mc.play_media(host_url+filename, 'audio/mp3')
		mc.block_until_active()
		return mc.status
	else:
		return "Input file error!"
pass
	



## Wake the chromecast as soon as a file is detected in our CASDROP_WATCH_FOLDER
class MyHandler(FileSystemEventHandler): 
	def on_created(self, event):
		what = 'directory' if event.is_directory else 'file'
		logging.info("Created %s: %s", what, event.src_path)

		if event.is_directory: 
			print("[folder_upload]: Feature not supported")
			## what if user delete folder? 
		else:
			print(chromecast(os.path.basename(event.src_path)).content_id)
	

	def on_deleted(self, event):
		what = 'directory' if event.is_directory else 'file'
		logging.info("Deleted %s: %s", what, event.src_path)


#Watch for changes 
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, watch_folder, recursive = True)
observer.start() #start monitoring changes


try: 
	while True:
		time.sleep(10)
except KeyboardInterrupt: #unless I hit ctr-c
	observer.stop()

observer.join()























# # Shut down discovery
# pychromecast.discovery.stop_discovery(browser)