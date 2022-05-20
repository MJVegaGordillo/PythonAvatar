# Login/Password side
from tkinter import *
from functools import partial
import lxml

# RPA and scraping libraries
import os
import time
from unicodedata import name
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

def validateLogin(username, password):
	print("username entered :", username.get())
	print("password entered :", password.get())
	return

#window
tkWindow = Tk()  
tkWindow.geometry('400x150')  
tkWindow.title('Tkinter Login Form - pythonexamples.org')

#username label and text entry box
usernameLabel = Label(tkWindow, text="Email or Phone").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)  

#password label and password entry box
passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=0)  
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)  

validateLogin = partial(validateLogin, username, password)

#login button
loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=4, column=0)  

tkWindow.mainloop()

user  = username.get()
passw = password.get()

print(user)
print(passw)

# Right to LinkedIn

# Creating a webdriver instance
options = webdriver.ChromeOptions()
options.add_argument('start-maximized')

# to supress the error messages/logs
#options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome('C:\Program Files\SeleniumBasic\Chromedriver.exe')
driver.maximize_window()

# This instance will be used to log into LinkedIn  
# Opening linkedIn's login page
driver.get("https://linkedin.com/uas/login")
  
# waiting for the page to load
time.sleep(5)

# entering username
username = driver.find_element_by_id("username")
  
# In case of an error, try changing the element
# tag used here.

# Enter Your Email Address  
username.send_keys(user)
  
# entering password
pword = driver.find_element_by_id("password")
# In case of an error, try changing the element 
# tag used here.
  
# Enter Your Password
pword.send_keys(passw)    

# Clicking on the log in button
# Format (syntax) of writing XPath --> 
# //tagname[@attribute='value']
driver.find_element_by_xpath("//button[@type='submit']").click()
# In case of an error, try changing the
# XPath used here.

# Opening Manu Vega's Profile
# paste the URL's profile here
profile_url = "https://www.linkedin.com/in/manuvegagordillo/"
driver.get(profile_url)

# Opening Manu Vega's Profile
# paste the URL's profile here
talentinsights_url = "https://www.linkedin.com/insights/"
driver.get(talentinsights_url)

# Now using beautiful soup
# soup=BeautifulSoup(src,'lxml')
src=driver.page_source
soup = BeautifulSoup(src,  "html.parser")

# Extracting the HTML of the complete introduction box
# that contains the name, company name, and the location
intro = soup.find('div', {'class': 'pv-text-details__left-panel'})
print(intro)