from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from fake_useragent import UserAgent

import time
import os
import csv

# create user agent at random
ua = UserAgent()
userAgent = ua.random

# add options
opts = Options()
# user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50
# Safari/537.36'
opts.add_argument("--disable-notifications")
opts.add_argument(f'user-agent={userAgent}')
# opts.add_argument("--headless")

# open driver
driver = webdriver.Chrome(options=opts)

driver.delete_all_cookies()

# for writing the first row of the csv
full = ['STT', 'Cụm Thi', 'Họ Tên', 'SBD', 'Ngày sinh', 'Giới tính', 'Toán (D1)', 'Ngữ văn (D2)', 'Vật lí (D3)',
        'Hóa học (D4)', 'Sinh học (D5)', 'KHTN (D6)', 'Lịch sử (D7)', 'Địa lí (D8)', 'GDCD (D9)', 'KHXH (D10)',
        'Ngoại ngữ (D11)', 'D12']

# index.txt is the save file for the area code. it ranges from 01-64. index2.txt is the save file for the candidate
# number in that are. for example, 01000202 means this candidate lives in zone 01, and he is the 202 candidate. the
# indexes file make sure that even when the program encoutered error, the progress is saved so we don't have to run
# it from the beginning.

# check whether index.txt and index2.txt and csv file is present.
# logic: if index, index2 and csv files are there, read from them and continue the program from that number.
# else just start from the beginning with index=1 and index2=1000001, also write the header of the csv
if os.path.isfile(f'index.txt') and os.path.isfile(f'score2021.csv') and os.path.isfile(f'index2.txt'):
    index = int(open('index.txt').read())
    index2 = int(open('index2.txt').read())
    csv_file = open(f'score2021.csv', 'a', encoding='utf-8', newline='')
    writer = csv.writer(csv_file)
else:
    index = 1
    index2 = 1000001
    csv_file = open(f'score2021.csv', 'w', encoding='utf-8', newline='')
    writer = csv.writer(csv_file)
    writer.writerow(full)

# variable to change index to beginning
newindex = index

# go to the website
driver.get('https://thanhnien.vn/giao-duc/tuyen-sinh/2021/tra-cuu-diem-thi-thpt-quoc-gia.html')
list = []
check_dup_list = []

# if there's an error, write current ID into index and index2, then show error
try:
    #iterate through 64 area codes
    for x in range(index, 10):
        count = 0
        print(index)
        #if the area code changes, index2 starts again from 1000001
        if newindex != x:
            index2 = 1000001
        #iterate through all candidate ID
        for y in range(index2, 1999999):
            #if there are 15 blank results in a row, move to next area code
            if count == 15:
                driver.get('https://thanhnien.vn/giao-duc/tuyen-sinh/2021/tra-cuu-diem-thi-thpt-quoc-gia.html')
            if count == 30:
                break
            #concatentate the actual ID
            if x < 10:
                i = str(0) + str(x) + str(y)[1:]
            else:
                i = str(x) + str(y)[1:]
            print(i)
            index = x
            index2 = y
            #input in the candidate ID into input box on the website
            driver.implicitly_wait(6)

            try:
                input = driver.find_element_by_xpath('//input[@id="txtkeyword"]')
                input.clear()
                input.send_keys(i)
                input.send_keys(Keys.RETURN)
                time.sleep(1)
            except StaleElementReferenceException as Exception:
                input = driver.find_element_by_xpath('//input[@id="txtkeyword"]')
                input.clear()
                input.send_keys(i)
                input.send_keys(Keys.RETURN)
                time.sleep(1)

            # create two variable, list and check_dup_list
            # if list equals check_dup_list, keep finding the results table
            # if it takes too long, move to the next candidate ID
            # we are doing this because the results table might not change after we input new ID,
            # for some reason, therefore we need to make sure it changes everytime we input in new ID
            cnt = 0
            while list == check_dup_list:
                if cnt >= 5:
                    count += 1
                    writer.writerow(['', '', '', i])
                    break
                try:
                #while in the loop, find the results table which has the scores
                    table = driver.find_element_by_xpath("//tbody[@id='resultcontainer']")
                    for r, row in enumerate(table.find_elements_by_xpath(".//tr")):
                        list = [[td.text for td in row.find_elements_by_xpath(".//td")]]
                        time.sleep(1)
                    cnt +=1
                except:
                    cnt += 1
                    continue

            if list != check_dup_list:
                writer.writerow(list[0])
                count = 0

            check_dup_list = list

            # time.sleep(5)
    driver.quit()


except Exception as e:
    ## write the index so the script knows where where it left off
    print(e)
    print(list)
    open('index.txt', 'w').write('%d' % (index))
    open('index2.txt', 'w').write('%d' % (index2))

    csv_file.close()
    driver.quit()
    quit()
