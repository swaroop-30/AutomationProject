import time
import random
import os.path
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.select import Select

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")


driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options= chrome_options)
# initialize chrome webdriver

time.sleep(1)
# Open the e-commerce URL and maximize the window
driver.get('http://tutorialsninja.com/demo/')
driver.maximize_window()
time.sleep(2)

# Clicking on phone button
phones = driver.find_element(by=By.XPATH, value='//a[text()="Phones & PDAs"]')
phones.click()
time.sleep(2)


# Selecting the iphone
iphone1 = driver.find_element(by=By.XPATH, value='//a[text()="iPhone"]')
iphone1.click()
time.sleep(1)

# clicking the first picture
firstpic = driver.find_element(by=By.XPATH, value='//ul[@class="thumbnails"]/li[1]')
firstpic.click()
time.sleep(2)

# clicking the last picture next picture
nextclick = driver.find_element(by=By.XPATH, value='//button[@title="Next (Right arrow key)"]')


for i in range(0, 5):
    nextclick.click()
    time.sleep(2)

# saving the screenshot in project file
driver.save_screenshot('screenshot#' + str(random.randint(0, 101)) + '.png')

# close button
xbutton = driver.find_element(by=By.XPATH, value='//button[@title="Close (Esc)"]')
xbutton.click()
time.sleep(2)

# Clicking on LAPTOPS Section


laptops = driver.find_element(by=By.XPATH, value='//a[text()="Laptops & Notebooks"]')
time.sleep(1)
action = ActionChains(driver)
action.move_to_element(laptops).perform()
time.sleep(2)
laptop2 = driver.find_element(by=By.XPATH, value='//a[text()="Show All Laptops & Notebooks"]')
laptop2.click()
time.sleep(1)

# click on HP laptop

HP = driver.find_element(by=By.XPATH, value='//a[text()="HP LP3065"]')
HP.click()
time.sleep(1)

# scrolling down
addtobutton2 = driver.find_element(by=By.XPATH, value='//button[@id="button-cart"]')
addtobutton2.location_once_scrolled_into_view
time.sleep(1)

# Playing with the calendar
calendar = driver.find_element(by=By.XPATH, value='//i[@class="fa fa-calendar"]')
calendar.click()
time.sleep(1)

nextclickcalendar = driver.find_element(by=By.XPATH, value='//th[@class="next"]')
month_year = driver.find_element(by=By.XPATH, value='//th[@class="picker-switch"]')

# year:2022 month:June
while month_year.text != 'June 2022':
    nextclickcalendar.click()
time.sleep(2)

# selecting day 22
calendardate = driver.find_element(by=By.XPATH, value='//td[text()="22"]')
calendardate.click()
time.sleep(2)

# Clicking on add to button
addtobutton2.click()
time.sleep(1)

# Checkout Process
gotocart = driver.find_element(by=By.ID, value='cart-total')
gotocart.click()
time.sleep(1)

checkout = driver.find_element(by=By.XPATH, value='//p[@class="text-right"]/a[2]')
checkout.click()
time.sleep(1)

# Clicking on guest account
guest = driver.find_element(by=By.XPATH, value='//input[@value="guest"]')
guest.click()

# click continue 1
continue_1 = driver.find_element(by=By.ID, value='button-account')
continue_1.click()
time.sleep(1)

# scrolling down
step_2 = driver.find_element(by=By.XPATH, value='//a[text()="Step 2: Billing Details "]')
step_2.location_once_scrolled_into_view
time.sleep(2)

# Enter first name
first_name = driver.find_element(by=By.ID, value='input-payment-firstname')
first_name.click()
time.sleep(1)
first_name.send_keys('test_first_name')
time.sleep(1)

# Enter last name
last_name = driver.find_element(by=By.ID, value='input-payment-lastname')
last_name.click()
time.sleep(1)
last_name.send_keys('test_last_name')
time.sleep(1)

# Email
email = driver.find_element(by=By.ID, value='input-payment-email')
email.click()
time.sleep(1)
email.send_keys('test@test.com')
time.sleep(1)

# Telephone
telephone = driver.find_element(by=By.ID, value='input-payment-telephone')
telephone.click()
time.sleep(1)
telephone.send_keys('012345678')
time.sleep(1)

# Enter Address
address = driver.find_element(by=By.ID, value='input-payment-address-1')
address.click()
time.sleep(1)
address.send_keys('teststreet 187')
time.sleep(1)

# Enter City
city = driver.find_element(by=By.ID, value='input-payment-city')
city.click()
time.sleep(1)
city.send_keys('Frankfurt')
time.sleep(1)

# Enter Postcode
postcode = driver.find_element(by=By.ID, value='input-payment-postcode')
postcode.click()
time.sleep(1)
postcode.send_keys('112233')
time.sleep(1)


# Select Country
country = driver.find_element(by=By.ID, value='input-payment-country')
dropdown_1 = Select(country)
time.sleep(1)
dropdown_1.select_by_visible_text('India')
time.sleep(1)

# Select Region
region = driver.find_element(by=By.ID, value='input-payment-zone')
dropdown_2 = Select(region)
time.sleep(1)
dropdown_2.select_by_visible_text('Madhya Pradesh')
time.sleep(1)

# click on continue 2
continue_2 = driver.find_element(by=By.XPATH, value='//input[@id="button-guest"]')
continue_2.click()
time.sleep(1)

# click on continue 3
continue_3 = driver.find_element(by=By.XPATH, value='//input[@id="button-shipping-method"]')
continue_3.click()
time.sleep(1)

# Accept the terms & conditions
tA = driver.find_element(by=By.XPATH, value='//input[@name="agree"]')
tA.click()
time.sleep(1)

# click on continue 4
continue4 = driver.find_element(by=By.XPATH, value='//input[@id="button-payment-method"]')
continue4.click()
time.sleep(3)

# Printing out final price of the purchase from table displayed
finalprice = driver.find_element(by=By.XPATH, value='//table[@class="table table-bordered table-hover"]/tfoot/tr[3]/'
                                                     'td[2]')

print("The final price of both products is " + finalprice.text)
time.sleep(2)

# click on the confirmation button
confirmation_button = driver.find_element(by=By.ID, value='button-confirm')
confirmation_button.click()
time.sleep(2)


# success text
success_text = driver.find_element(by=By.XPATH, value='//div[@class="col-sm-12"]/h1')
print(success_text.text)
time.sleep(1)

# Close the Tab
driver.close()
