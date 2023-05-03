# -*- coding: utf-8 -*-
import json
import sqlite3
from configparser import ConfigParser
from time import sleep

import pyautogui
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.service import Service


class App:
    def __init__(self, email="", password="",
                 img_base_path="", language="", main_url="", marketplace_url="", marketplace_your_posts="", 
                 binary_location="", driver_location="", time_to_sleep=""):
        self.email = email
        self.password = password
        self.img_base_path = img_base_path
        self.language = language
        self.marketplace_options = None
        self.posts = None
        self.time_to_sleep = float(time_to_sleep)
        with open('marketplace_options.json', encoding='utf-8') as f:
            self.marketplace_options = json.load(f)
            self.marketplace_options = self.marketplace_options[self.language]
        # To remove the pop up notification window
        options = Options()
        options.binary_location = binary_location
        # add parameter for running firefox in background
        options.set_preference("dom.webnotifications.enabled", False)
        # geckodriver allows you to use emojis, chromedriver does not
        self.driver = webdriver.Firefox(
            service=Service(driver_location), options=options)
        self.driver.maximize_window()
        self.main_url = main_url
        self.marketplace_url = marketplace_url
        self.marketplace_your_posts = marketplace_your_posts
        self.driver.get(self.main_url)
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@data-cookiebanner="accept_button"]'))).click()  # per rimuover il pop-up dei cookies
        self.log_in()

        # Loading posts data from db
        self.posts = self.fetch_all_posts()

        ###creating all post
        self.create_posts()

        ###deleting all post
        self.delete_all_post()
        

    def log_in(self):
        email_input = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, "email")))
        email_input.send_keys(self.email)
        password_input = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, "pass")))
        password_input.send_keys(self.password)
        login_button = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@type='submit']")))
        login_button.click()

    def fetch_all_posts(self):
        posts = None
        try:
            sqliteConnection = sqlite3.connect('articles.db')
            cursor = sqliteConnection.cursor()
            sqlite_select_query = """SELECT * from post"""
            cursor.execute(sqlite_select_query)
            posts = cursor.fetchall()
            cursor.close()

        except sqlite3.Error as error:
            print("Failed to read data from sqlite table", error)

        finally:
            if (sqliteConnection):
                sqliteConnection.close()

        return posts

    ### Feature-posts zone
    def move_from_home_to_marketplace_create_item(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(
            (By.XPATH, '//a[@aria-label="Facebook"]')))
        self.driver.get(self.marketplace_url)

    def create_posts(self):
        for post in self.posts:
            self.move_from_home_to_marketplace_create_item()
            self.create_post(post)
        sleep(2)
        self.driver.quit()

    def add_photos_to_post(self, post_folder):
        photo_button = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(
            (By.XPATH, '//div[@aria-label="' + self.marketplace_options["labels"]["Marketplace"] + '"]/div/div[3]/div[2]/div/div[@role="button"]')))
        photo_button.click()
        sleep(2)
        pyautogui.hotkey('ctrl', 'l')
        sleep(self.time_to_sleep)
        pyautogui.write(self.img_base_path + post_folder)
        sleep(self.time_to_sleep)
        pyautogui.press('backspace')
        sleep(self.time_to_sleep)
        pyautogui.press('enter')
        sleep(self.time_to_sleep)
        pyautogui.hotkey('ctrl', 'a')
        sleep(self.time_to_sleep)
        pyautogui.press('enter')
        sleep(self.time_to_sleep)
        sleep(2)

    def add_text_to_post(self, title, price, description):
        title_input = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, "//label[@aria-label='" + self.marketplace_options["labels"]["Title"] + "']/div/div/input")))
        title_input.send_keys(title)
        price_input = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, "//label[@aria-label='" + self.marketplace_options["labels"]["Price"] + "']/div/div/input")))
        price_input.send_keys(price)
        description_button = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, '//div[@aria-label="' + self.marketplace_options["labels"]["Marketplace"] + '"]/div/div[9]/div/div/div/div[@role="button"]')))
        description_button.click()
        description_input = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, "//label[@aria-label='" + self.marketplace_options["labels"]["Description"] + "']/div/div/textarea")))
        description_input.send_keys(description.replace("\r\n", "\n"))

    def post_in_more_places(self, groups):
        groups_positions = groups.split(",")  # groups_positions = groups_names

        for group_position in groups_positions:
            # group_input = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='" + self.marketplace_options["labels"]["Marketplace"] +  "']/div/div/div/div[4]/div/div/div/div/div/div/div[2]/div[" + group_position + "]")))
            group_input = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(
                (By.XPATH, "//*[contains(text(), '" + group_position + "')]")))  # filtra in base al testo e funziona il click
            group_input.click()
            sleep(self.time_to_sleep)

    def create_post(self, post):
        self.add_photos_to_post(post[8]) # Post.path
        self.add_text_to_post(post[1], post[2], post[7]) # Post.pk, Post.title, Post.description,

        category_input = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, "//label[@aria-label='" + self.marketplace_options["labels"]["Category"] + "']")))
        category_input.click()

        sleep(self.time_to_sleep)
        category_option = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, "//div[@role='dialog']/div/div/div/span/div/div[" + self.get_element_position("categories", post[3]) + "]"))) # Post.price
        category_option.click()
        sleep(self.time_to_sleep)

        state_input = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, "//label[@aria-label='" + self.marketplace_options["labels"]["State"] + "']")))
        state_input.click()
        sleep(self.time_to_sleep)
        state_option = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, '//div[@role="listbox"]/div/div/div/div/div[1]/div/div[' + self.get_element_position("states", post[4]) + ']'))) # Post.state
        state_option.click()
        sleep(self.time_to_sleep)

        next_button = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, "//div[@aria-label='" + self.marketplace_options["labels"]["Next Button"] + "']")))
        next_button.click()

        self.post_in_more_places(post[9]) # Post.label
        sleep(self.time_to_sleep)
        sleep(8)

        post_button = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(
            (By.XPATH, "//div[@aria-label='" + self.marketplace_options["labels"]["Post"] + "']")))
        post_button.click()
        sleep(self.time_to_sleep)

    ### Feature-delete zone
    def move_from_home_to_marketplace_your_posts(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//a[@aria-label="Facebook"]')))
        self.driver.get(self.marketplace_your_posts)

    def delete_post(self, post_id):
        try:
            self.move_from_home_to_marketplace_your_posts()
            # Need to ask if the first post exist
            sleep(6)
            print(self.marketplace_options["labels"]["Collection"])
            #buttons = self.driver.find_elements_by_xpath('//div[@aria-label="' + self.marketplace_options["labels"]["Collection"] + '"]/div/div/div[2]/div/div/div[3]/div/span/div/div[2]/div/div[2]/div/div[2]/div/div')
            
            #problema ci sono varie parti in quella pagina con la struttura aria-label='Altro'..., quindi direi di trovarlo in base alla parentela dei nodi e in base al titolo da rimuovere
            buttons = self.driver.find_elements_by_xpath('//div[@aria-label="' + self.marketplace_options["labels"]["Collection"] + '"]') # collection = altro
            print(buttons)
            
            buttons[len(buttons) - 1].click() # open the menu and select delete
            sleep(self.time_to_sleep)

            delete_option = self.driver.find_elements_by_xpath("//div[@role='menu']/div[1]/div/div[1]/div/div")
            delete_option[len(delete_option) - 1].click() 
            sleep(self.time_to_sleep)
            
        except:
            print("There is no more post to delete")


    def delete_all_post(self):
        for post in self.posts:
            self.delete_post(post[0]) # Post.id

    def get_element_position(self, key, specific):
        # key = categories
        if specific in self.marketplace_options[key]:
            return str(self.marketplace_options[key][specific])
        return -1


if __name__ == '__main__':
    config_object = ConfigParser()
    config_object.read("config.ini")
    facebook = config_object["FACEBOOK"]
    configuration = config_object["CONFIG"]
    app = App(facebook["email"], facebook["password"], configuration["images_path"], configuration["language"],
              facebook["main_url"], facebook["marketplace_url"], facebook["marketplace_your_posts"],
              configuration["binary_location"], configuration["driver_location"], configuration["time_to_sleep"])
