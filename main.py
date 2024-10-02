# This program is used to remind the user to drink water after a certain time period
# It uses the winotify library to send a notification to the user
# The notification includes a title, message, and icon
# The notification also includes a reminder sound
# The program uses a while loop to continuously check the time
# If the time exceeds 7200 seconds (2 hours), the program will send a notification
# The program will then reset the time to 0 and continue to check the time

import time
from winotify import Notification , audio

# Set up the notification
toast = Notification(app_id="Buddy",
                     title='Hey bro :)',
                     msg='Time to drink water',
                     duration='short',
                     icon=r'Here the path to the icon')

# Set up the reminder sound
toast.set_audio(audio.Reminder , loop=False)

# Initialize the time variable
sec = 0

# Define a function to check the time
def timer():
    global sec
    while sec <= 7200:
        # Wait for 1 second
        time.sleep(1)
        # Increment the time by 1 second
        sec+=1
        # Print the time (for debugging purposes)
        # print(sec)
    else:
        # If the time exceeds 2 hours, send a notification
        toast.show()
        # Reset the time to 0
        sec = 0
        # Call the timer function again
        timer()

# Call the timer function to start the program
timer()
# NOTE: All code is written by me , except comments .
