# script to download instagram images
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import requests
from bs4 import BeautifulSoup
import os

# check if download/instagram folder exists
# if not create one
if not os.path.exists("downloads/instagram"):
    os.makedirs("downloads/instagram")

# get local user
user = os.getlogin()


def find_image_url(post_link):
    chrome_profile_directory = f"C:/Users/{user}/AppData/Local/Google/Chrome/User Data/"

    # Create ChromeOptions object and set the profile directory
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("user-data-dir=" + chrome_profile_directory)

    # Initialize the WebDriver with the custom ChromeOptions using 'options' parameter
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Open the specified URL
        driver.get(post_link)

        # Accept cookies if a pop-up appears (you might need to adjust this)
        for _ in range(5):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # time.sleep(2)  # Wait for content to load, adjust as needed

        # Wait for a specific element to be present (you can change this condition)7
        print("Waiting for image to load...")
        WebDriverWait(driver, 3).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, 'img.x5yr21d.xu96u03.x10l6tqk.x13vifvy.x87ps6o.xh8yej3'))
        )

        # Inject the JavaScript code and capture the result
        js_code = """
        var imgElement = document.querySelector('img.x5yr21d.xu96u03.x10l6tqk.x13vifvy.x87ps6o.xh8yej3');
        var imgSrc = imgElement.getAttribute('src');
        return imgSrc;
        """
        img_src = driver.execute_script(js_code)

        # Print the result
        print("Result of JavaScript injection:", img_src)
        return img_src
    finally:
        # Close the browser
        driver.quit()


def download_image(file_url, set_file_name):
    print("Downloading image...")
    with open("downloads/instagram" + set_file_name + ".jpg", "wb") as img_file:
        # downloading the image
        response = requests.get(file_url)
        # writing the contents of the image
        img_file.write(response.content)


def main():
    post_url = input("Enter the image url: \n>> ")
    image_content = find_image_url(post_url)
    # print(image_url)
    if image_content is not None:
        download_image(image_content, post_url.split("/")[-2])


if __name__ == "__main__":
    while True:
        mode = input("Enter 1 to download image from Post URL, 2 for URLs in file: \n>> ")
        if mode == "1":
            main()
            break
        elif mode == "2":
            input("Name the file urls.txt and place it in the same folder as this script. Press Enter to continue...")
            with open("urls.txt", "r") as file:
                total_lines = sum(1 for line in file)
                file.seek(0)  # Reset file position to the beginning

                for line_number, line in enumerate(file, start=1):
                    url = line.strip()
                    file_name = url.split("/")[-2]
                    image_url = find_image_url(url)

                    if image_url is not None:
                        download_image(image_url, file_name)
                        print(f"Processed line {line_number} of {total_lines}")
                print("Done!")
                break
