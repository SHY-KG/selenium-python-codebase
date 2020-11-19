from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


KEYWORD = "cat"

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://google.com")

search_bar = driver.find_element_by_class_name("gLFyf")
search_bar.send_keys(KEYWORD)
search_bar.send_keys(Keys.ENTER)

driver.execute_script(
    """
    alert("FIN")
    """
)