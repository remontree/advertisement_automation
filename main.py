import upload
import send
from selenium import webdriver
import time
import pyautogui
import pyperclip
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import openpyxl
from selenium.webdriver.support.select import Select
import pandas as pd
import datetime
import autoit

if __name__ == "__main__":
    sh = pd.read_excel("정보.xlsx")
    time_table = []
    succees = 0
    fail = 0

    for i in list(sh["시간"].to_numpy()):
        time_table.append("{}.{}".format(i.hour,i.minute))

    while True:
        now = datetime.datetime.now()
        time_str = str(now.hour)+'.'+str(now.minute)
        if (str(now.hour)=="0" and str(now.minute)=="0"):
            log_message = "<광고 자동화 로그>\n업로드 성공: {}\n업로드 실패: {}".format(succees,fail)
            succees = 0
            fail = 0
            send.send(log_message)
        try:
            if time_str in time_table:
                idx = time_table.index(time_str)+2
                upload.upload(idx)
                log_message = """현재 시각 {}\n 업로드 성공""".format(time_str)
                send.send(log_message)
                succees+=1
        except:
            log_message = """현재 시각 {}\n 업로드 실패""".format(time_str)
            send.send(log_message)
            fail+=1
        time.sleep(60)
