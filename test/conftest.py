import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService, Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="class")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-search-engine-choice-screen")
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--remote-debugging-port=9222")

    options.add_argument('--dns-prefetch-disable')
    options.add_argument('--disable-gpu')
    options.add_argument('--enable-cdp-events')

    #options.binary_location = "/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome/"
    executable_path = Service("/usr/local/bin/chromedriver-mac-arm64")


    # service = Service(ChromeDriverManager().install())
    # driver = webdriver.Chrome(service=service, options=options)
    # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    #driver = webdriver.Chrome(options=options)

    driver = webdriver.Chrome(service=executable_path, options=options)

    driver.implicitly_wait(10)
    yield driver
    driver.quit()

