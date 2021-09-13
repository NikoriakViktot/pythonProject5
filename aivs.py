from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import datetime


# options = webdriver.ChromeOptions()
# options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")
# options.add_argument("--disable-blink-features=AutomationControlled")
# options.headless = True
url = 'http://hydro.meteo.gov.ua/'
data = datetime.date.today().strftime('%d-%m-%Y')

try:
    driver = webdriver.Chrome(executable_path="E:\ВІТЯ\pythonProject5\chromedriver.exe")
    # driver = webdriver.Chrome(executable_path="E:\ВІТЯ\pythonProject5\chromedriver.exe", options=options)
    driver.get(url=url)
    time.sleep(0.1)
    vubir_posta = Select(driver.find_element_by_css_selector(".table_form select"))
    vubir_posta.select_by_value('storozhynech')
    # vubir_datu = driver.find_element_by_xpath("/html/body/div[1]/div[7]/form/table/tbody/tr[2]")
    # d_t = vubir_datu.find_element_by_name('date_start')
    # d_t.clear()
    # d_t.send_keys(f'{data}')
    time.sleep(1)
    zwit = driver.find_element_by_css_selector(".table_form input")
    zwit.submit()
    tabl = driver.find_element_by_tag_name('table')
    trbody =[tr.find_elements_by_tag_name('tr') for tr in tabl.find_elements_by_xpath('/html/body/div/div[7]/table')]
    # print(trbody)
    td = [iter_tr.find_elements_by_tag_name('td') for iter_tr in trbody[0]]
    # print(len(td))
    # # x = td[0]
    text_data = [elem.text for elem in td[0]]
    text_level = [elem.text for elem in td[1]]
    text_level_1 = [elem.text for elem in td[2]]
    text_level_2 = [elem.text for elem in td[3]]
    text_level_3 = [elem.text for elem in td[4]]
    # # v = tuple(x)
    # print(text_data)
    # print(text_level, text_level_1, text_level_2, text_level_3)
    data_dict = dict(dict(zip(text_data,text_level)))
    data_dict_1

finally:

     driver.close()
     # driver.quit()

# rezult =[a for a in td.text]
# for tr in tbody.find_elements_by_xpath('/html/body/div/div[7]/table/tbody/tr[1]'):
#      rezult.append([a.text for a in tr.find_elements_by_xpath('/html/body/div/div[7]/table/tbody/tr[1]/td[1]')])
#  re = []/html/body/div[1]/div[7]/table
# print(td)


# titel = driver.find_element_by_class_name("table_result").text
# lewel = driver.find_element_by_class_name("table_result2").text
#
# print(titel)
#
# print(lewel)



