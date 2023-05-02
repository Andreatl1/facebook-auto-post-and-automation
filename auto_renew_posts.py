# -*- coding: utf-8 -*-
import json
import sqlite3
from configparser import ConfigParser
from time import sleep

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class App:
    def __init__(self, email= "", password= "", language="", main_url="", marketplace_your_posts="", binary_location="", driver_location="", time_to_sleep=""):
        self.email = email
        self.password = password
        self.language = language
        self.marketplace_options = None
        self.ask_to_continue = True
        self.time_to_sleep = float(time_to_sleep)
        with open('marketplace_options.json', encoding='utf-8') as f:
            self.marketplace_options = json.load(f)
            self.marketplace_options = self.marketplace_options[self.language]
        # To remove the pop up notification window
        options = Options()
        options.binary_location = binary_location
        options.set_preference("dom.webnotifications.enabled", False)
        # geckodriver allows you to use emojis, chromedriver does not
        self.driver = webdriver.Firefox(executable_path=driver_location, options=options)
        self.driver.maximize_window()
        self.main_url = main_url
        self.marketplace_your_posts = marketplace_your_posts
        self.driver.get(self.main_url)
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@data-cookiebanner="accept_button"]'))).click() #per rimuover il pop-up dei cookies
        self.log_in()
        self.move_from_home_to_marketplace_renew_posts()
        self.renew_all_post() 
        sleep(self.time_to_sleep)
        self.driver.quit()
        
        
    def log_in(self):
        email_input = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, "email")))
        email_input.send_keys(self.email)
        password_input = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, "pass")))
        password_input.send_keys(self.password)
        login_button = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@type='submit']")))
        login_button.click()
        

    def move_from_home_to_marketplace_renew_posts(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//a[@aria-label="Facebook"]')))
        self.driver.get(self.marketplace_your_posts)


    def renew_all_post(self):
        #aggiungere un eccezzione nel caso il bottone non ci sia
        sleep(6)
        #e poi click sul bottone rinnova tutto




if __name__ == '__main__':
    config_object = ConfigParser()
    config_object.read("config.ini")
    facebook = config_object["FACEBOOK"]
    configuration = config_object["CONFIG"]
    app = App(facebook["email"], facebook["password"], configuration["language"], facebook["main_url"], facebook["marketplace_renew_posts"], configuration["binary_location"], configuration["driver_location"], configuration["time_to_sleep"])