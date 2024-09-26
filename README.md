# Project-Description

This Python script is a simple water reminder notification system that uses the `winotify` library to display a desktop notification on Windows systems. The notification reminds the user to drink water after a set period of time (2 hours in this case).

# How it works
The script uses a while loop to increment a counter every second, simulating a timer. When the counter reaches 7200 seconds (2 hours), the script triggers a desktop notification using the `winotify` library. The notification displays a friendly message `"Time to drink water"` with a custom icon. After displaying the notification, the script resets the counter to 0 and starts the timer again.


# Features
- Customizable notification title, message, and icon<br>
- Adjustable timer duration (currently set to 2 hours)<br>
- Uses `winotify` library for desktop notifications on Windows systems<br>
- Simple and lightweight script that runs indefinitely<br>

# Code Explanation
The script consists of the following components:

- Importing the necessary libraries: `time` for timing and winotify for desktop notifications<br>
- Defining a `Notification` object with a custom app ID, title, message, duration, and icon<br>
- Defining a `timer` function that increments a counter every second using a while loop<br>
- When the counter reaches 7200 seconds, the script triggers the notification using the `show` method<br>
- The script resets the counter to 0 and calls the `timer` function again to start the timer over<br>

# Customization
You can customize the notification title, message, and icon by modifying the `Notification` object. You can also adjust the timer duration by changing the value of the `sec` variable in the while loop.
