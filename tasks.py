from selenium import webdriver
import time
import requests

POST_URL = "http://192.168.0.189:8000"


def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)

    driver.get("https://www.weatherapi.com/weather/")

    return driver


def extract_text():
    driver = get_driver()
    time.sleep(5)
    driver.find_element(
        by="xpath", value="/html/body/div/div[2]/div[1]/div[2]/div[2]/button[1]"
    ).click()
    driver.find_element(by="id", value="ctl00_butUnitC").click()

    element = driver.find_element(
        by="xpath",
        value='//*[@id="weatherapi-weather-london-city-of-london-greater-london-united-kingdom"]/div/div[3]',
    )
    return element.text


def get_current_data():
    temperature = extract_text().split(" ")[0]
    post_body = {"temperature": temperature, "place": "Dobrich", "weather_api_pk": 5}
    print(post_body)
    p = requests.post(f"{POST_URL}/current", json=post_body)
