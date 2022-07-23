from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, StaleElementReferenceException, WebDriverException
import time       
import csv               
import json
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager as CM


COOKIE_PATH = 'insert cookie.json in here'
URL_PROFILE = 'insert url profile instagram account in here'

def main(): 
    # driver = Chrome(headless=False)
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    options.add_argument('--no-sandbox')
    options.add_argument("--log-level=3")
    mobile_emulation = {
        "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/90.0.1025.166 Mobile Safari/535.19"}
    options.add_experimental_option("mobileEmulation", mobile_emulation)

    driver = webdriver.Chrome(executable_path=CM().install(), options=options)
    driver.set_window_size(600, 700)    
    
    alamatURL = 'https://www.instagram.com'       
    driver.get(alamatURL) 
    f = open(COOKIE_PATH)
    print('Load cookie.json')
    data = json.load(f)
    for i in data:
        driver.add_cookie({
            'name' : i['name'],
            'value' : i['value'],
            'path' : i['path'],
            'secure' : i['secure'],
            'session' : i['session'],
            'domain' : i['domain'],
        })
    time.sleep(10)
    alamatURL = URL_PROFILE
    driver.get(alamatURL)
    print('open url')
    time.sleep(10)    
    print('open url followers')
    driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/ul/li[2]/a').click()
    time.sleep(5)

    scroll_pause_time = 1

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(scroll_pause_time)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            # If heights are the same it will exit the function
            break
        last_height = new_height
    print('end scroll')
    time.sleep(10)
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'lxml')
    username = soup.find_all('span', {'class' : '_aacl _aaco _aacw _aacx _aad7 _aade'})
    result = []
    for name in username:        
        data = {
            'username' : name.get_text()
        }
        result.append(data)

    # save to csv    
    keys = result[0].keys()
    with open(f'ig_followers.csv', 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(result)    
    print('finish')


if __name__ == '__main__':    
    main()