import subprocess
import inspect
import tkinter as tk
import time
import urllib.request
import requests
import os

from PIL import Image, ImageTk
from tkinter import ttk
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
script_dir = script_dir.replace("\\","/")
print(f"The script path is: {script_dir}")

# Create an instance of FirefoxOptions
firefox_options = Options()
#firefox_options.add_argument("-headless")  # Ensure this argument is correct
browser = webdriver.Firefox(options=firefox_options)

# 'cleans' browser between station websites
refresh_http = "http://www.ri.com.au" 

browser.get(refresh_http)
time.sleep(4)

sPath = "https://www.asx.com.au/markets/company/bhp"
sPath = "https://www.asx.com.au/content/asx/investor/dashboard.html"
print(sPath)
browser.get(sPath)
time.sleep(1)

while True:
    startup = False    

 

