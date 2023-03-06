import time
import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/Lenovo/Downloads"
#to_dir = "C:/Users/Lenovo/OneDrive/Desktop/Downloaded_Files"

class FileSystemEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"Hey, {event.src_path} has been created!")
    def on_modified(self, event):
        print(f"The file, {event.src_path} has been modified!")
    def on_moved(self, event):
        print(f" {event.src_path} has been moved!")
    def on_deleted(self, event):
        print(f"Oops! {event.src_path} has been deleted!")

event_handler=FileSystemEventHandler()

observer=Observer()
observer.schedule(event_handler,from_dir,recursive=True)
observer.start()

try: 
    while True:
        time.sleep(2)
        print("Running... ")
except KeyboardInterrupt:
    #Ctrl+C
    print("Stopped.. ") 
    observer.stop()


#Exeptions: An exeption is an event that is triggered when an error occurs in an program.
# -1: Built-in-Exeptions: These event are defined by some commonly known error that can occur while the porgramm is running.
# -2: User-defined-Exeptions:These events are defined by the users to track errors differently from built-in .