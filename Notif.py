"""
Author:       Shaun Scott
Date:         June 17,2020
Description:  Windows Notification for specific directory changes
"""
# ----------------------------------------------------------------------------------------------------------------

# import Toast Notification package, time module, Observer, PatternMatchingEventHandler
import time
from win10toast import ToastNotifier
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

# Custom functions to run when events are raised
# Each function creates a windows notification that lasts for 20 seconds and print the path to the file that raised
#    the event
def on_created(event):
    myNotif.show_toast("[Notification Title]", "[Notification Message]", duration=20, threaded=True)
    print(f"Created: {event.src_path}")
    return

def on_deleted(event):
    myNotif.show_toast("[Notification Title]", "[Notification Message]", duration=20, threaded=True)
    print(f"Deleted: {event.src_path}")
    return

def on_modified(event):
    myNotif.show_toast("[Notification Title]", "[Notification Message]", duration=20, threaded=True)
    print(f"Modified: {event.src_path}")
    return

def on_moved(event):
    myNotif.show_toast("[Notification Title]", "[Notification Message]", duration=20, threaded=True)
    print(f"Moved: {event.src_path}")
    return

if __name__ == "__main__":
    # Create toast notification object
    myNotif = ToastNotifier()

    # Initialize event handler object
    watch_patterns = "*"
    ignore_patterns = ""
    ignore_directories = False
    case_sensitive = False
    event_handler = PatternMatchingEventHandler(watch_patterns, ignore_patterns, ignore_directories, case_sensitive)

    # Assign handler events to our created functions to display notification
    event_handler.on_created = on_created
    event_handler.on_deleted = on_deleted
    event_handler.on_modified = on_modified
    event_handler.on_moved = on_moved

    # Initialize Observer
    observer_path = '.'
    observe_recursively = True
    my_observer = Observer()
    my_observer.schedule(event_handler, observer_path, recursive=observe_recursively)

    # Start the observer
    my_observer.start()
    try:
        while True:
            # Set the thread sleep time
            time.sleep(1)
    except KeyboardInterrupt:
        my_observer.stop()
        my_observer.join()
