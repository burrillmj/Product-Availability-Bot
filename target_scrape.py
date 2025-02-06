from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def check_target_stock(url):
    # Set up the WebDriver (ensure you have the correct WebDriver for your browser)
    driver = webdriver.Chrome()  # You can use other drivers like Firefox, Edge, etc.

    # Open the webpage
    driver.get(url)

    # Create a dictionary to store product information
    product_info = {}

    try:
        # Wait for the product title to load and fetch it
        product_title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "pdp-product-title-id"))
        ).text
        product_info["title"] = product_title
    except Exception as e:
        product_info["title"] = "Title not found"
        print(f"Error fetching title: {e}")

    try:
        # Wait for the price to load and fetch it
        price = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-test="product-price"]'))
        ).text
        product_info["price"] = price
    except Exception as e:
        product_info["price"] = "Price not found"
        print(f"Error fetching price: {e}")

    try:
        # Wait for the stock status to load and fetch it
        out_of_stock = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-test="NonbuyableSection"]'))
        ).text
        product_info["stock_status"] = "Out of stock"
    except Exception as e:
        product_info["stock_status"] = "In stock"
        print(f"Out of Stock Section not found (likely in stock): {e}")

    # Close the browser
    driver.quit()

    # Return the product information
    return product_info


url = ("https://www.target.com/p/pok--233-mon-trading-card-game--scarlet---38--violet--8212-prismatic-evolutions-surprise-box/-/A-94336414")

print(check_target_stock(url))