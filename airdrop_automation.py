import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler



# The source folder where my airdrops are downloaded to
source_folder = '/Users/carlbedrot/Downloads'

# The destination folder where I want my airdrops to be moved to
destination_folder = '/Users/carlbedrot/Desktop/Airdrops'

class AirdropHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            # Get the file extension
            file_extension = os.path.splitext(event.src_path)[-1].lower()
            
            if file_extension in ['.jpg', '.heic']:
                # Check if the created file is an image (either .jpg or .heic)
                try:
                    new_file_path = os.path.join(destination_folder, os.path.basename(event.src_path))
                    os.rename(event.src_path, new_file_path)
                    print(f"Moved {event.src_path} to {new_file_path}")
                except Exception as e:
                    print(f"Error moving file {event.src_path}: {e}")

if __name__ == "__main__":
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    event_handler = AirdropHandler()
    observer = Observer()
    observer.schedule(event_handler, source_folder, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
