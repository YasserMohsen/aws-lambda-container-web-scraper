from selenium import webdriver
from selenium.webdriver.chrome.options import Options


CHROMEDRIVER_LOCATION = "/bin/chromedriver"
CHROME_HEADLESS_LOCATION = "/bin/headless-chromium"


class ChromeDriverWrapper:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.headless = True
        options.binary_location = CHROME_HEADLESS_LOCATION
        options.add_argument("--headless")
        options.add_argument("window-size=1920x1080")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        # options.add_argument("start-maximized")
        # options.add_argument("enable-automation")
        # options.add_argument("--disable-infobars")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument('--disable-gpu-sandbox')
        options.add_argument("--single-process")
        # options.add_argument("--disable-extensions") 
        # options.add_argument('--remote-debugging-port=9222')
        options.add_argument(
            '"user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"')
        self._driver = webdriver.Chrome(options=options, executable_path=CHROMEDRIVER_LOCATION)

    def get_url(self, url):
        self._driver.get(url)

    def get_title(self):
        return self._driver.title

    def close(self):
        self._driver.quit()