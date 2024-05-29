from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


CHROME_DRIVER_PATH = "C:/Users/lenovo/Desktop/Layihe_4/chromedriver.exe"
EDGE_DRIVER_PATH = "C:/Users/lenovo/Desktop/Layihe_4/msedgedriver.exe"

@pytest.fixture(scope="module")
def driver_chrome():
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--headless")  # Brauzeri başsız (headless) rejimdə işə salmaq
    chrome_service = ChromeService()
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    yield driver
    driver.quit()

@pytest.fixture(scope="module")
def driver_edge():
    edge_options = EdgeOptions()
    edge_options.add_argument("--headless")  # Brauzeri başsız (headless) rejimdə işə salmaq
    edge_service = EdgeService()
    driver = webdriver.Edge(service=edge_service, options=edge_options)
    yield driver
    driver.quit()

def test_logo_size_chrome(driver_chrome):
    driver_chrome.get("https://en.wikipedia.org/wiki/NASA")
    logo = WebDriverWait(driver_chrome, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "a.mw-wiki-logo"))
    )
    logo_height = logo.size['height']
    logo_width = logo.size['width']
    assert logo_height == 160 and logo_width == 160, f"Logo ölçüləri düzgün deyil: {logo_height}px x {logo_width}px"

def test_body_background_color_chrome(driver_chrome):
    driver_chrome.get("https://en.wikipedia.org/wiki/NASA")
    body = driver_chrome.find_element(By.CSS_SELECTOR, "body")
    body_bg_color = body.value_of_css_property("background-color")
    assert body_bg_color == "rgba(0, 0, 0, 1)" or body_bg_color == "#000000", f"Body fon rəngi düzgün deyil: {body_bg_color}"

def test_budget_table_box_sizing_chrome(driver_chrome):
    driver_chrome.get("https://en.wikipedia.org/wiki/NASA")
    budget_table = WebDriverWait(driver_chrome, 10).until(
        EC.presence_of_element_located((By.XPATH, "//table[contains(@class, 'wikitable')]"))
    )
    box_sizing = budget_table.value_of_css_property("box-sizing")
    assert box_sizing == "border-box", f"NASA büdcə cədvəli box-sizing düzgün deyil: {box_sizing}"

def test_link_font_chrome(driver_chrome):
    driver_chrome.get("https://en.wikipedia.org/wiki/NASA")
    links = driver_chrome.find_elements(By.CSS_SELECTOR, "a")
    for link in links:
        font_family = link.value_of_css_property("font-family").lower()
        font_size = link.value_of_css_property("font-size")
        assert "sans-serif" in font_family, f"Linkdə şrift Sans-Serif deyil: {font_family}"
        assert font_size == "12.6px", f"Linkdə şrift ölçüsü düzgün deyil: {font_size}"

def test_logo_size_edge(driver_edge):
    driver_edge.get("https://en.wikipedia.org/wiki/NASA")
    logo = WebDriverWait(driver_edge, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "a.mw-wiki-logo"))
    )
    logo_height = logo.size['height']
    logo_width = logo.size['width']
    assert logo_height == 160 and logo_width == 160, f"Logo ölçüləri düzgün deyil: {logo_height}px x {logo_width}px"

def test_body_background_color_edge(driver_edge):
    driver_edge.get("https://en.wikipedia.org/wiki/NASA")
    body = driver_edge.find_element(By.CSS_SELECTOR, "body")
    body_bg_color = body.value_of_css_property("background-color")
    assert body_bg_color == "rgba(0, 0, 0, 1)" or body_bg_color == "#000000", f"Body fon rəngi düzgün deyil: {body_bg_color}"

def test_budget_table_box_sizing_edge(driver_edge):
    driver_edge.get("https://en.wikipedia.org/wiki/NASA")
    budget_table = WebDriverWait(driver_edge, 10).until(
        EC.presence_of_element_located((By.XPATH, "//table[contains(@class, 'wikitable')]"))
    )
    box_sizing = budget_table.value_of_css_property("box-sizing")
    assert box_sizing == "border-box", f"NASA büdcə cədvəli box-sizing düzgün deyil: {box_sizing}"

def test_link_font_edge(driver_edge):
    driver_edge.get("https://en.wikipedia.org/wiki/NASA")
    links = driver_edge.find_elements(By.CSS_SELECTOR, "a")
    for link in links:
        font_family = link.value_of_css_property("font-family").lower()
        font_size = link.value_of_css_property("font-size")
        assert "sans-serif" in font_family, f"Linkdə şrift Sans-Serif deyil: {font_family}"
        assert font_size == "12.6px", f"Linkdə şrift ölçüsü düzgün deyil: {font_size}"
