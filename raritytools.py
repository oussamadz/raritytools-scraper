#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


def saveData(line):
    with open("nfts.csv", 'a') as f:
        f.write(line + "\n")


br2 = webdriver.Firefox()


def work(url):
    br2.get(url)
    socials = br2.find_elements_by_class_name(
        "AccountHeader--social-container")
    for s in socials:
        if "twitter" in s.get_attribute("href"):
            return s.get_attribute("href")
        else:
            return None


rank = []
link = []
name = []
punk = []
namelink = []
twitter = []
br = webdriver.Firefox()
br.get("https://rarity.tools/cryptopunks")
WebDriverWait(br, 30).until(EC.presence_of_element_located(
    (By.XPATH, "/html/body/div/div/div/div[2]/div[2]/div[8]/div[1]/div[42]/div/div[1]/a")))
btns = br.find_elements_by_class_name("smallBtn")
for b in btns:
    if "Next" in b.text:
        nextBtn = b
i = 0
while i < 209:
    WebDriverWait(br, 30).until(
        EC.presence_of_element_located((By.CLASS_NAME, "items-start")))
    time.sleep(2)
    items = br.find_elements_by_class_name(
        "items-start")[-1].find_elements_by_class_name("bgCard")
    for itm in items:
        # itm.click()
        rank.append(itm.find_element_by_class_name(
            "font-extrabold").text.replace("#", ""))
        link.append(itm.find_element_by_partial_link_text(
            "CryptoPunk").get_attribute("href"))
        # name.append(itm.find_element_by_class_name("text-sm").text)
        name.append(itm.text.split("\n")[1])
        namelink.append(itm.find_element_by_class_name(
            "text-sm").get_attribute("href").split("?")[0])
        if "0x" not in name[-1]:
            twitter.append(work(itm.find_element_by_class_name(
                "text-sm").get_attribute("href").split("?")[0]))
        else:
            twitter.append("N/A")
        punk.append(itm.find_element_by_partial_link_text("CryptoPunk").text.replace(
            "CryptoPunk #", "").replace("CryptoPunks #", ""))
        line = f"{rank[-1]},{link[-1]},{name[-1]},{punk[-1]},{namelink[-1]},{twitter[-1]}"
        saveData(line)
        print(line.replace(",", "\n"))
    i += 1
    nextBtn.click()
