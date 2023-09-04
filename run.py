import schedule
from time import sleep
import tweet

tweet.run()

def task():
    tweet.run()

schedule.every(30).minutes.do(task)

while True:
    schedule.run_pending()
    sleep(1)