#!/usr/bin/env python
# coding: utf-8

from __future__ import print_function
import os.path
import threading
import urllib.request
import requests
import time
import sys
import tkinter.ttk
import io
import tkinter.messagebox
import tkinter
from PIL import ImageTk, Image
from selenium.webdriver.common.alert import Alert
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#################################################################################################################################
# 기본 값 할당
studentClassCode = {"영아1부": "110000000", "영아2부": "120000000", "유아1부": "130000000",
                    "유아2부": "140000000", "유치1부": "150000000", "유치2부": "160000000", "유년1부": "170000000",
                    "유년2부": "180000000", "초등1부": "190000000", "초등2부": "200000000", "소년1부": "210000000",
                    "소년2부": "220000000", "영어아동부": "230000000", "중등부": "240000000", "고등부": "250000000"}
site = "http://web.choongshin.or.kr/WebSchool/Default.aspx"
siteId = "---"
password = "---"
size = 283, 503
##################################################################################################################################
# 셀레니움 명령어 단순화
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
options.binary_location = "C:/Program Files(x86)/Google/Chrome/Application/chrome.exe"
try:
    driver = webdriver.Chrome('./chromedriver.exe', chrome_options=options)
except:
    options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"


def clickById(id):
    return WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, id)))


def clickByClass(Class):
    return WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, Class)))


def clickByXpath(xpath):
    return WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, xpath)))
###################################################################################################################################


def autoExcute(studentClassName):
    playing = True
    # 웹페이지 로그인
    driver.get(site)
    element = clickById("ctl00_cph1_LoginMain1_txtLoginID")
    element.send_keys(siteId)
    element = clickById("ctl00_cph1_LoginMain1_txtLoginPWD")
    element.send_keys(password)
    element = clickById("ctl00_cph1_LoginMain1_imgBtnLogin")
    element.click()
    alert = Alert(driver)
    alert.accept()
    # 프레임전환
    driver.switch_to.frame("left")
    # 부서탐색
    element = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id=' + '"' + studentClassCode[studentClassName] + '"' + ']/a')))
    element.click()
    driver.switch_to_default_content()
    driver.switch_to.frame("right")
    checkbox = True
    result = WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "imgCursor")))
    page = WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "PageNumber")))
    page.append("")

    # 사진넣는작업
    childList = []
    for file in os.listdir(os.getcwd() + "/부서사진"):
        childList.append(file)
    bar = len(childList)
    for p in range(0, len(page)+1):
        code = 0
        for i in result:
            picHave = False
            driver.switch_to_default_content()
            driver.switch_to.frame("right")
            # 종료키워드
            n = "ctl00_cph1_PersonListStudent_tabConSch_tabPnSchMain_lvMain_ctrl" + \
                str(code) + "_lblNumber"
            end = clickById(n)
            if end.get_attribute("textContent") == "1":
                playing = False
            # 이름탐색
            imgId = "ctl00_cph1_PersonListStudent_tabConSch_tabPnSchMain_lvMain_ctrl" + \
                str(code) + "_imgP"
            student = clickById(imgId)
            name = student.get_attribute("alt")
            # 이름으로 사진찾기
            for c in childList:
                if c == name + '.jpg':
                    picHave = True
                    childList.remove(c)
                    print(len(childList))
                    print(playing)
                    if len(childList) == '0':
                        playing = False
            # 사진이 없으면 바로 넘기기
            if picHave == False:
                code = code + 1
                if playing == False:
                    message = tkinter.messagebox.showinfo(
                        "알림", "작업이 완료되었습니다.")
                continue
            # ui 초기화
            # 썸네일화 하면  nontype으로 바뀌므로 복사본 만들어서 이용
            # Ui에 백업사진 업로드
            img = student.get_attribute("src")
            urllib.request.urlretrieve(
                img, os.getcwd() + '/backup/' + name + '.jpg')  # 백업
            backupImg = Image.open(
                os.getcwd() + "/backup/" + name + ".jpg")
            copyImg = backupImg.copy()
            copyImg.thumbnail(size, Image.ANTIALIAS)
            copyImg.save(name + "test", "JPEG")
            backupImg = ImageTk.PhotoImage(copyImg)
            os.remove(os.getcwd() + '/' + name + 'test')

            student.click()  # 변경작업
            driver.switch_to_window(driver.window_handles[1])
            element = clickById("ctl00_cph1_PersonModifyStudent1_txtName")
            name = element.get_attribute("value")
            element = clickById(
                "ctl00_cph1_PersonModifyStudent1_tabPicture_tabPicture1_btnEditPic")
            element.click()
            driver.implicitly_wait(1)
            driver.switch_to_window(driver.window_handles[2])
            element = clickById("ctl00_cph1_fuFile")
            element.send_keys(os.getcwd() + "/부서사진/" + name + ".jpg")
            if checkbox == True:
                element = clickById("ctl00_cph1_cbUseCrop")
                element.click()
                checkbox = False
            element = clickById("ctl00_cph1_imgWrite")
            element.click()
            alert = Alert(driver)
            alert.accept()
            driver.switch_to_window(driver.window_handles[1])
            driver.close()
            driver.switch_to_window(driver.window_handles[0])
            code = code + 1
            # Ui에 바꿀사진 업로드
            urllib.request.urlretrieve(
                img, os.getcwd() + '/upload/' + name + '.jpg')
            nowImg = Image.open(os.getcwd() + "/upload/" + name + ".jpg")
            copyImg = nowImg.copy()
            copyImg.thumbnail(size, Image.ANTIALIAS)
            copyImg.save(name + 'test', "JPEG")
            nowImg = ImageTk.PhotoImage(copyImg)
            os.remove(os.getcwd() + '/' + name + 'test')
            # 종료키워드 동작
            if playing == False:
                message = tkinter.messagebox.showinfo("알림", "작업이 완료되었습니다.")
        driver.switch_to_default_content()
        driver.switch_to.frame("right")
        pp = WebDriverWait(driver, 5).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "PageNumber")))
        pp[p].click()
        time.sleep(3)
