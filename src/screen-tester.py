import time
from math import ceil
from selenium import webdriver
from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

INPUT_URL = input("INPUT TESTURL: ")
SCREEN_WIDTH_SIZES = [480, 960, 1366, 1920]
TEST_BROWSER_LIST = ["CHROME", "FIREFOX", "EDGE"]


def sizeTester(browser_name):
    if browser_name == "CHROME":
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser_name == "FIREFOX":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager())
    elif browser_name == "EDGE":
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    else:
        return False

    driver.get(INPUT_URL)
    screen_height_sizes = driver.get_window_size()["height"]

    for size in SCREEN_WIDTH_SIZES:
        driver.set_window_size(size, screen_height_sizes)
        driver.execute_script("window.scrollTo(0,0)")
        time.sleep(1)
        page_scroll_size = driver.execute_script("return document.body.scrollHeight")
        scroll_count = ceil(page_scroll_size / screen_height_sizes)
        for scroll in range(scroll_count + 1):
            driver.execute_script(
                f"window.scrollTo(0, {(scroll) * screen_height_sizes})"
            )
            driver.save_screenshot(f"screenshots/{browser_name}_{size}x{scroll}.png")
            time.sleep(1)
    driver.quit()


for browser_name in TEST_BROWSER_LIST:
    sizeTester(browser_name)