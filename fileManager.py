from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from os import getcwd
from json import dumps


class FileFolder:
    def __init__(self, user, target):
        self.user = user
        self.target = target
        self.driver = webdriver.Firefox()

    def create_json(self):
        print('Creating json file!')
        words = {}
        j = 1
        while 1:
            try:
                location = f'{getcwd()}\{self.user}\messages\inbox\{self.target}\message_{j}.html'
                self.driver.get(location)
                i = 3
                while 1:
                    print(i, end='')
                    try:
                        name = (self.driver.find_element(By.XPATH, f'/html/body/div/div/div/div[2]/div[2]/div[{i}]/div[1]')).text
                        line = (self.driver.find_element(By.XPATH, f'/html/body/div/div/div/div[2]/div[2]/div[{i}]/div[2]/div/div[2]')).text
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
        file = open('data.json', 'w')
        file.write(dumps(words))
        self.driver.close()

    def print_json(self):
        print(self.data)
