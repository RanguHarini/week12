from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('registration.html')


@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    course = request.form['course']

    return render_template(
        'success.html',
        name=name,
        email=email,
        phone=phone,
        course=course
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)






import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import time


# Fixture for setting up and tearing down the driver
@pytest.fixture
def setup_teardown():
    options = Options()

    # Change this path if Chrome is installed elsewhere
    options.binary_location = (
        r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    )

    # Run Chrome without opening a visible browser window
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    yield driver
    driver.quit()


# Test 1: Registration page loads correctly
def test_registration_page(setup_teardown):
    driver = setup_teardown
    driver.get("http://127.0.0.1:5001/")

    assert driver.title == "Registration Form"
    assert driver.find_element(By.TAG_NAME, "h2").text == \
        "Student Registration Form"


# Test 2: Registration fields are available
def test_registration_fields(setup_teardown):
    driver = setup_teardown
    driver.get("http://127.0.0.1:5001/")

    assert driver.find_element(By.NAME, "name").is_displayed()
    assert driver.find_element(By.NAME, "email").is_displayed()
    assert driver.find_element(By.NAME, "phone").is_displayed()
    assert driver.find_element(By.NAME, "course").is_displayed()


# Test 3: Course can be selected
def test_course_selection(setup_teardown):
    driver = setup_teardown
    driver.get("http://127.0.0.1:5001/")

    course = Select(driver.find_element(By.NAME, "course"))
    course.select_by_visible_text("B.Tech")

    assert course.first_selected_option.text == "B.Tech"


# Test 4: Successful registration
def test_valid_registration(setup_teardown):
    driver = setup_teardown
    driver.get("http://127.0.0.1:5001/")

    driver.find_element(By.NAME, "name").send_keys("Harini")
    driver.find_element(By.NAME, "email").send_keys(
        "harini@example.com"
    )
    driver.find_element(By.NAME, "phone").send_keys("9876543210")

    Select(
        driver.find_element(By.NAME, "course")
    ).select_by_visible_text("B.Tech")

    driver.find_element(
        By.XPATH, "//button[@type='submit']"
    ).click()

    time.sleep(1)

    message = driver.find_element(By.TAG_NAME, "h3").text

    assert message == "Registration successful! Welcome, Harini."





