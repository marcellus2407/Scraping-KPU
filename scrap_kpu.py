from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import requests
import time

# path chromedriver.exe untuk chrome
driver_path = r"C:\Users\Viny\Downloads\chromedriver-win32\chromedriver.exe"

service = Service(driver_path)
driver = webdriver.Chrome(service=service)

try:
    driver.get("https://pilkada2024.kpu.go.id/")

    wait = WebDriverWait(driver, 10)
    ok_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "swal2-confirm")))
    ok_button.click()
    
    link_elements = wait.until(EC.presence_of_all_elements_located((By.LINK_TEXT, "Unduh dokumen hasil pindai")))
    
    
    for link_element in link_elements:
        file_url = link_element.get_attribute("href")
        
        time.sleep(5)
        
        if file_url:
            print(f"Found file URL: {file_url}")
            file_response = requests.get(file_url)
            file_response.raise_for_status()
            
            file_name = file_url.split("/")[-1]
            with open(file_name, "wb") as file:
                file.write(file_response.content)
            print(f"File downloaded and saved as {file_name}")
        else:
            print("tidak ada href di tagnya")
finally:
    driver.quit()
