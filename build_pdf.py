import hashlib
import os
import subprocess
import sys
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import (
    NoSuchElementException,
    TimeoutException as SeleniumTimeoutException,
)


class TimeoutException(Exception):
    pass


_path = os.path.realpath(os.path.abspath(__file__))
ROOT = os.path.dirname(_path)
SITE = "Real Python"

app_data = os.environ.get("APPDATA")
assert app_data
# Chrome Canary
chrome_exe = (
    os.path.abspath(os.path.dirname(app_data))
    + "\\Local\\Google\\Chrome SxS\\Application\\chrome.exe"
)

options = webdriver.ChromeOptions()
# options.add_argument('--headless')
options.add_argument("--enable-dom-distiller")
options.add_argument("--disable-gpu")
options.add_experimental_option(
    "prefs",
    {"download": {"prompt_for_download": False, "default_directory": os.getcwd(),},},
)
options.binary_location = chrome_exe


def reader_mode(url):
    """ 
    Return URL in ReaderMode for apply distiller.js
    Chrome ReaderMode ( Distiller - View Reader )
    """
    m = hashlib.sha256()
    m.update(url.encode("utf-8"))

    url_hash = m.hexdigest()
    uuid = "00000000-0000-0000-0000-000000000000"

    url_distiller = "chrome-distiller://{}_{}/?url={}".format(uuid, url_hash, url)
    return url_distiller


def wait_for(callback, seconds):
    assert callable(callback)

    now = time.time()

    while True:
        expired = time.time() > now + seconds

        if expired:
            raise TimeoutException("Timeout ocurred!")
        elif callback():
            break


def delete_element(driver: webdriver.Chrome, name, by=By.CSS_SELECTOR):
    """
    Delete HTML element from the DOM
    """
    try:
        element = driver.find_element(by, name)
        driver.execute_script("arguments[0].remove();", element)
    except NoSuchElementException:
        print("Failed delete HTML element: %s!" % (name))
        return False
    except:
        return False

    return True


def handle_save_as(browser, path_pdf):
    """
    Handle Save as dialog in Windows for Chrome passing the pdf filename
    and the special ENTER key (escaping special character)
    to handle_save_as.exe compiled with AutoIt
    """
    # Escape de Path to file 👀
    path_pdf = "%s" % (path_pdf + "{ENTER}")
    ps = subprocess.Popen(
        [os.sep.join([ROOT, "handle_save_as.exe"]), browser, path_pdf]
    )
    # Wait for write the path_pdf file name in the dialog
    time.sleep(30)
    return ps.returncode


def print_pdf_save_as(driver: webdriver.Chrome, browser="chrome", path_pdf="file.pdf"):
    """
    Print and save the Web page HTML as PDF file in Chrome.
    Use handle_save_as for handle the Save as dialog window.
    Using when webdriver options is NOT headless.
    NOTE: Adjust the time.sleep according to your Environment
          Window Locale: EN
    """
    url = driver.current_url

    try:
        driver.execute_async_script("window.print();")
    except SeleniumTimeoutException as err:
        pass
    # Wait for render pdf preview
    time.sleep(60)
    driver.switch_to.window(driver.window_handles[1])
    try:
        now = time.time()
        while True:
            expired = time.time() > now + 30
            dropdown: WebElement = driver.execute_script(
                (
                    "return document.querySelector('print-preview-app')."
                    "shadowRoot.querySelector('print-preview-sidebar')."
                    "shadowRoot.querySelector('print-preview-destination-settings')."
                    "shadowRoot.querySelector('print-preview-destination-select')."
                    "shadowRoot.querySelector('select.md-select');"
                )
            )
            if dropdown:
                break
            if expired:
                raise TimeoutException("Timeout ocurred!")

        # 'Save as PDF/local/'
        _value = dropdown.get_attribute("value")

        if _value and _value[:4] != "Save":
            dropdown.click()
            time.sleep(0.5)
            # Down until Save as PDF
            dropdown.send_keys(Keys.ARROW_DOWN)
            # Wait for Re-render pdf preview
            time.sleep(90)

        save = driver.execute_script(
            (
                "return document.querySelector('print-preview-app')."
                "shadowRoot.querySelector('print-preview-sidebar')."
                "shadowRoot.querySelector('print-preview-button-strip')."
                "shadowRoot.querySelector('cr-button.action-button');"
            )
        )
        assert save
        save.click()

        # Handle Save as dialog in Windows
        # Wait for Save as dialog
        time.sleep(30)
        handle_save_as(browser, path_pdf)
    except TimeoutException as err:
        print(err)
    except NoSuchElementException:
        print("Error printing to PDF!")
    driver.switch_to.window(driver.window_handles[0])


def print_pdf(driver, browser="chrome", path_pdf="file.pdf"):
    """
    Print and save the Web page HTML as PDF file
    using the Chrome Devtools Protocol.
    Using when webdriver options is headless.
    """
    pass


def main(url):
    driver = webdriver.Chrome(options=options)
    # driver.get(reader_mode(url))
    driver.get(url)

    try:
        wait_for(lambda: SITE in driver.title, 300)  # 😬
    except TimeoutException as err:
        driver.quit()
        sys.exit(err)

    print(driver.title + "\n")
    driver.implicitly_wait(10)
    # Try skip Ads
    try:
        element = driver.find_element_by_link_text("Continue to site")
        if element:
            element.click()
    except NoSuchElementException:
        pass
    print("Deleting elements...")
    delete_element(driver, "nav.navbar")
    delete_element(driver, "aside", by=By.TAG_NAME)
    delete_element(driver, "div.drip-tab-container")
    delete_element(driver, "reader-comments", by=By.ID)
    delete_element(driver, "div.card.mt-4.mb-4.bg-secondary")
    delete_element(driver, "div.bg-light.rounded.py-4.my-4.shadow.shadow-sm.mx-n2")
    delete_element(driver, "footer", by=By.TAG_NAME)
    delete_element(driver, "button.btn.w-100")
    delete_element(driver, "div.app_gdpr--2k2uB")
    print("Printing to PDF...")
    pdf_file_name = driver.title + ".pdf"
    pdf_file_path = os.sep.join([ROOT, "pdfs", pdf_file_name])
    print_pdf_save_as(driver, path_pdf=pdf_file_path)
    print("All done!")

    _ = input("Enter for continue...")
    print("Bye 👋🏾")
    driver.quit()


if __name__ == "__main__":
    url = ""
    if len(sys.argv) == 2:
        url = sys.argv[1]
    # HTML Remote or Local
    assert "http" in url[:4] or "file" in url[:4]
    sys.exit(main(url))
