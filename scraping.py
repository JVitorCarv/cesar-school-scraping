from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.cesar.school/")

# Hover over "School"
school = driver.find_elements(By.CLASS_NAME, "menu-text")[0]
actions = ActionChains(driver)
actions.move_to_element(school).perform()

blog = driver.find_element(By.ID, "menu-item-15254")
blog.click()

next_page = driver.find_elements(By.CLASS_NAME, "page-numbers")[1]
next_page.click()

third_post = driver.find_elements(By.TAG_NAME, "article")[2]

post_title = third_post.find_element(By.CLASS_NAME, "entry-title").text
print(f'Título do terceiro post: {post_title}')

day = third_post.find_element(By.CLASS_NAME, "date-day").text
month = third_post.find_element(By.CLASS_NAME, "date-month").text
year = third_post.find_element(By.CLASS_NAME, "date-year").text
date = f"{day}/{month}/{year}"
print(f'Data do terceiro post: {date}')

second_post = driver.find_elements(By.TAG_NAME, "article")[1]
second_post.click()

author = driver.find_element(By.CLASS_NAME, "author-name").text
print(f'Autor do segundo post: {author}')

driver.quit()
