from .pages.locators import MainPageLocators
from .pages.main_page import MainPage
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина

# Версия от 17.07.2024 г. 08:34

def go_to_login_page(browser):
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()

def test_guest_can_go_to_login_page(browser): 
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link) 
    time.sleep(10)
    go_to_login_page(browser) 

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    time.sleep(10)
    page.should_be_login_link()