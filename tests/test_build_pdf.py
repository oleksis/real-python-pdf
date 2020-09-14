import os
import sys
import unittest

_path = os.path.realpath(os.path.abspath(__file__))
ROOT_PATH = os.path.dirname(os.path.dirname(_path))
sys.path.insert(0, ROOT_PATH)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from build_pdf import options, wait_for, delete_element, print_pdf_save_as, ROOT, SITE


class BuildPdfTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(options=options)
        # file:///ROOT_PATH/tests/file_name
        file_schema = "file://"
        # 👀 - != – : chr(45) != chr(8211)
        file_name = (
            "A Practical Introduction to Web Scraping"
            " in Python " + chr(8211) + " Real Python.html"
        )
        file_html = os.sep.join([ROOT_PATH, "tests", file_name])
        file_html = file_html.replace("\\", "/")
        file_url = "/".join([file_schema, file_html])

        cls.driver.get(file_url)
        wait_for(lambda: SITE in cls.driver.title, 300)
        print(cls.driver.title + "\n")
        cls.driver.implicitly_wait(10)
        cls.nav_element = None
        try:
            cls.nav_element = cls.driver.find_element(By.CSS_SELECTOR, "nav.navbar")
        except NoSuchElementException as err:
            print(err)
        pdf_file_name = cls.driver.title + ".pdf"
        cls.pdf_file_path = os.sep.join([ROOT, "pdfs", pdf_file_name])
        if os.path.isfile(cls.pdf_file_path):
            os.remove(cls.pdf_file_path)

    def test_delete_element(self, name="nav.navbar", by=By.CSS_SELECTOR):
        self.assertTrue(delete_element(self.driver, name, by))

    def test_print_pdf_save_as(self):
        print("Deleting elements...")
        self.test_delete_element("aside", by=By.TAG_NAME)
        self.test_delete_element("div.drip-tab-container")
        self.test_delete_element("reader-comments", by=By.ID)
        self.test_delete_element("div.card.mt-4.mb-4.bg-secondary")
        self.test_delete_element(
            "div.bg-light.rounded.py-4.my-4.shadow.shadow-sm.mx-n2"
        )
        self.test_delete_element("footer", by=By.TAG_NAME)
        self.test_delete_element("button.btn.w-100")
        print("Printing to PDF...")
        print_pdf_save_as(self.driver, path_pdf=self.pdf_file_path)
        is_pdf_file = os.path.isfile(self.pdf_file_path)
        self.assertTrue(is_pdf_file, "PDF file not printed!")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
