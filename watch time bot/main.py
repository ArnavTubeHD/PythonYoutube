import time
from selenium import webdriver

video_link = 'https://www.youtube.com/watch?v=OTFc7UnA7vo'
views = 1000000
video_duration = 35 * 35

driver = webdriver.Chrome()
driver.get(video_link)

for i in range(views):
    time.sleep(video_duration)
    driver.refresh()
