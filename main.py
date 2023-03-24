from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from os import getcwd
from json import dumps


driver = webdriver.Firefox()
driver.set_window_position(-10000, -10000)

user, target = input().split()

words = {}
print('Starting scrapping!')
j = 1
while 1:
    try:
        driver.get(f'{getcwd()}\{user}\messages\inbox\{target}\message_{j}.html')
        i = 3
        while 1:
            print(i, end='')
            try:
                name = (driver.find_element(By.XPATH, f'/html/body/div/div/div/div[2]/div[2]/div[{i}]/div[1]')).text
                line = (driver.find_element(By.XPATH, f'/html/body/div/div/div/div[2]/div[2]/div[{i}]/div[2]/div/div[2]')).text
                for word in line.split():
                    if name in words:
                        if word.lower() in words[name]:
                            words[name][word.lower()] += 1
                        else:
                            words[name][word.lower()] = 1
                    else:
                        words[name] = {}
                        words[name][word.lower()] = 1
            except NoSuchElementException:
                print('\nPage', j, 'complete')
                break
            print(''.join(['\b'] * len(str(i))), end='')
            i += 1
        j += 1
    except:
        break
print('Srapping ended!')

file = open('data.json', 'w')
file.write(dumps(words))

driver.close()
