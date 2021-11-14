from bs4 import BeautifulSoup
import xlsxwriter

workbook = xlsxwriter.Workbook('test.xlsx')
worksheet = workbook.add_worksheet()
text = 'html text'
soup = BeautifulSoup(text, "html.parser")

all_courses = soup.find('ul', class_='course-cards')

li = all_courses.findAll('li', class_='course-cards__item')

row = 0
col = 0

for i in li:
    title_text = i.find('a', class_='course-card__title').text.strip()
    summary = i.find('span', class_='course-card__summary')
    summary_text = summary.find('div', class_='shortened-text ember-view').text.replace('\n', '').strip()
    hour = i.find('span', attrs={"data-type": "workload"})
    if hour:
        hour_text = hour.findAll('span')[1].text.strip()
    else:
        hour_text = "0 h"
    worksheet.write(row, col, title_text)
    worksheet.write(row, col + 1, summary_text)
    worksheet.write(row, col + 2, hour_text)
    row += 1

workbook.close()
