from chrome import ChromeDriverWrapper



def lambda_handler(event, context):
    print('Scraping through chrome driver wrapper starts here')
    # initiate a driver
    driver = ChromeDriverWrapper()
    print(driver._driver)
    # get url from event data
    url = event.get("url", "https://google.com")
    # go to the url
    driver.get_url(url)
    # get webpage title
    title = driver.get_title()
    print(title)
    # close the driver
    driver.close()
    print("Success")
    
    return {
        "message": f"This is from URL: {url}",
        "title": title
    }