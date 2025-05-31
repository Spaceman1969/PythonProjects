# This program tells the user how many months, weeks, and days it has been since May 3rd 2025

from datetime import date

today = date.today()
graduation = date(2025, 3, 28)

print(today - graduation)

input('Press enter to quit')
