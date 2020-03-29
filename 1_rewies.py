import sqlite3
from tkinter import *
import os
import sys
from tkinter.ttk import Combobox
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import *


class test :

#MAIN MENU
#--------------------------------------------------------------------------------------------------------------------------	
	def __init__ (self, root):


		self.group_label = Label(root, text = "Выбрать группу", bg = "peru", font = "Courier 20")
		self.group_label.place(x = 75, rely = 0.1)
		self.group = Combobox (root)
		self.group['values'] = ("-", "ГУ11", "ГУ21", "ГУ31", "ГУ41", "ТД14", "ТД24", "ТД54") 
		self.group.current(0)
		self.group.place(x = 75, rely = 0.15, width = 280)

		self.lection_number_label = Label(root, text = "Номер лекции (по счету на сайте во вкладке лекции)", bg = "peru", font = "Courier 20")
		self.lection_number_label.place(x = 75, rely = 0.25)
		self.lection_number = Entry (root, bg = "peru", font = "Courier 20")
		self.lection_number.place(x = 75, rely = 0.3)


		self.start = Button(root, text = "Начать", bg = "peru", font = "Courier 30")
		self.start.place(relx = 0.5 , rely = 0.95, anchor = CENTER, width = 600, height = 80)
		self.start.bind ("<Button-1>", self.chrome)



#--------------------------------------------------------------------------------------------------------------------------
#MAIN MENU


	def data_handeler(self, group):

		ident = 0

		while True:

			ident = ident + 1

			con = sqlite3.connect('group.db')
			cur = con.cursor()
			data = [ident]

			cur.execute('SELECT * FROM {0} WHERE ID = ? '.format(group), data)
			rows = cur.fetchall()
			con.commit()
			rower = rows[0]

			login = rower[1]
			password = rower[2]

			driver = webdriver.Chrome()
			driver.get("http://learn-mkgtu.ru/login/")

			element_email = driver.find_element_by_name("email")
			element_email.send_keys(login)

			element_pass = driver.find_element_by_name("pass")
			element_pass.send_keys(password)

			element_login = driver.find_element_by_name("login")
			element_login.click()

			driver.get("http://learn-mkgtu.ru/learn/lection/")
			sleep(1)

			message_id = 0
			try:
				message = driver.find_element_by_xpath("/html/body/div[4]/div/div[1]")
			except NoSuchElementException:
				message_id = 1

			if message_id == 1:
				message.click()

			number_lection = "/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div/div[2]/table/tbody/tr[" + str(
				self.lection_number.get()) + "]/td[6]/a"

			save_lection = driver.find_element_by_xpath(number_lection)
			save_lection.click()


	def chrome (self, event):
		
		group = self.group.get()
		
#ГУ21
		if group == "ГУ21":

			self.data_handeler('ГУ21')
#ГУ21


#ГУ11
		if group == "ГУ11":

			self.data_handeler('ГУ11')
#ГУ11


#ГУ31

		if group == "ГУ31":

			self.data_handeler('ГУ31')
#ГУ31


#ГУ41

		if group == "ГУ41":

			self.data_handeler('ГУ41')
#ГУ41


#ТД14

		if group == "ТД14":

			self.data_handeler('ТД14')
#ТД14


#ТД24

		if group == "ТД24":

			self.data_handeler('ТД24')
#ТД24


#ТД54

		if group == "ТД54":

			self.data_handeler('ТД54')
#ТД54




				

#MAIN WINDOW
#--------------------------------------------------------------------------------------------------------------------------
root = Tk()
root.title("TEST")
root.overrideredirect(0)
root.state('zoomed')
root.config(bg="sandybrown")
t = test(root)
root.mainloop()
#--------------------------------------------------------------------------------------------------------------------------
#MAIN WINDOW
