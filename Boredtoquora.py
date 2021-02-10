#libraries:
from tkinter import *
import webbrowser
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import pyautogui
import pickle
import tkinter.font as font


#we will create root for our script
root = Tk()
root.title("Bot Bored To Qura")
root.geometry('500x600')
root.configure(background='#0095B6')



# here we use pickle to makes us able to save data of quora and rebrandly in file.dat and use them later
cooltext1 = StringVar()
cooltext2 = StringVar()
cooltext3 = StringVar()
cooltext4 = StringVar()

def save1():
    text = cooltext1.get()
    with open("savedtext1.dat", "wb") as pickle_file:
        pickle.dump(text, pickle_file, pickle.HIGHEST_PROTOCOL)


def load1():
    with open("savedtext1.dat", "rb") as pickle_file:
        text = pickle.load(pickle_file)
    cooltext1.set(text)

def save2():
    text = cooltext2.get()
    with open("savedtext2.dat", "wb") as pickle_file:
        pickle.dump(text, pickle_file, pickle.HIGHEST_PROTOCOL)


def load2():
    with open("savedtext2.dat", "rb") as pickle_file:
        text = pickle.load(pickle_file)
    cooltext2.set(text)

def save3():
    text = cooltext3.get()
    with open("savedtext3.dat", "wb") as pickle_file:
        pickle.dump(text, pickle_file, pickle.HIGHEST_PROTOCOL)


def load3():
    with open("savedtext3.dat", "rb") as pickle_file:
        text = pickle.load(pickle_file)
    cooltext3.set(text)

def save4():
    text = cooltext4.get()
    with open("savedtext4.dat", "wb") as pickle_file:
        pickle.dump(text, pickle_file, pickle.HIGHEST_PROTOCOL)


def load4():
    with open("savedtext4.dat", "rb") as pickle_file:
        text = pickle.load(pickle_file)
    cooltext4.set(text)
#create 2 Entry to insert link question and link article (bored panda)
url_quora = Label(text="Enter your url question : ", bg="#0095B6",fg="white")
url_quora.pack()
quora = Entry()
quora.pack()
url_bored = Label(text="Enter your link bored : ", bg="#0095B6",fg="white")
url_bored.pack()
bored = Entry()
bored.pack()

#create 4 entries to insert user&pass of quora and user&pass for rebrandly
quora1=Label(text="email quora : ", bg="#0095B6",fg="white" )
quora1.pack()
quora_usr=Entry(root, textvariable=cooltext1)
quora_usr.pack()
Button(text="Save", command=save1).pack()
Button(text="Load", command=load1).pack()
quora2=Label(text="password quora : ", bg="#0095B6",fg="white")
quora2.pack()
quora_pwd= Entry(textvariable=cooltext2)
quora_pwd.pack()
Button(text="Save", command=save2).pack()
Button(text="Load", command=load2).pack()
rebrandly1 = Label(text="email rebrandly : ", bg="#0095B6",fg="white")
rebrandly1.pack()
rebrandly_usr= Entry(textvariable=cooltext3)
rebrandly_usr.pack()
Button(text="Save", command=save3).pack()
Button(text="Load", command=load3).pack()
rebrandly2=Label(text="password rebrandly : ", bg="#0095B6",fg="white")
rebrandly2.pack()
rebrandly_pwd=Entry(textvariable=cooltext4)
rebrandly_pwd.pack()
Button(text="Save", command=save4).pack()
Button(text="Load", command=load4).pack()
#create Function and write all code inside it because we need it  
def my_machine():
    driver = webdriver.Chrome()


    question = quora.get()

    panda = bored.get()


    usr = quora_usr.get()
    pwd = quora_pwd.get()
    reb_usr=rebrandly_usr.get()
    reb_pwd=rebrandly_pwd.get()



    # browse link article
    content_bored = driver.get(panda)

    # copy title

    title = driver.find_element_by_xpath("/html/body/main/div/section/article/header/h1").text

    # copy first paragraph
    #we will use try and except to handle any erreur because sometimes the xpath is updating

    try:
        first_paragraph = driver.find_element_by_xpath("/html/body/main/div/section/article/div[3]/div/div[1]").text
    except:
        first_paragraph = driver.find_element_by_xpath("/html/body/main/div/section/article/div[2]/div/p[1]").text


    

    ONE = ("#1")
    TWO = ("#2")
    THREE = ("#3")
    FOUR = ("#4")
    FIVE = ("#5")
    SIX= ("#6")
    SEVEN= ("#7")
    EIGHT= ("#8")

    # copy photos

    try:
        photo1 = driver.find_element_by_xpath("/html/body/main/div/section/article/div[3]/div/div[2]/div[1]/div[2]/p/span/img").get_attribute("src")
    except:
        pass

    try:
        photo2 = driver.find_element_by_xpath("/html/body/main/div/section/article/div[3]/div/div[2]/div[2]/div[2]/p/span/img").get_attribute("src")
    except:
        pass


    try:
        photo3 = driver.find_element_by_xpath("/html/body/main/div/section/article/div[3]/div/div[2]/div[3]/div[2]/p/span/img").get_attribute("src")
    except:
        pass


    try:
        photo4 = driver.find_element_by_xpath("/html/body/main/div/section/article/div[3]/div/div[2]/div[4]/div[2]/p/span/img").get_attribute("src")
    except:
        pass

    try:
        photo5 = driver.find_element_by_xpath("/html/body/main/div/section/article/div[3]/div/div[2]/div[5]/div[2]/p/span/img").get_attribute("src")
    except:
        pass


    try:
        photo6 = driver.find_element_by_xpath("/html/body/main/div/section/article/div[3]/div/div[2]/div[6]/div[2]/p/span/img").get_attribute("src")
    except:
        pass

    try:
        photo7 = driver.find_element_by_xpath("/html/body/main/div/section/article/div[3]/div/div[2]/div[7]/div[2]/p/span/img").get_attribute("src")
    except:
        pass

    try:
        photo8 = driver.find_element_by_xpath("/html/body/main/div/section/article/div[3]/div/div[2]/div[8]/div[2]/p/span/img").get_attribute("src")
    except:
        pass

    # login rebrandly
    driver.get("https://app.rebrandly.com/login")
    time.sleep(9)


    email_rebrandly = driver.find_element_by_name("Email")


    email_rebrandly.send_keys(reb_usr)

    password_rebrandly = driver.find_element_by_name("Password")


    password_rebrandly.send_keys(reb_pwd)

    password_rebrandly.send_keys(Keys.RETURN)

    time.sleep(7)
    driver.get("https://app.rebrandly.com/links/new")
    time.sleep(8)

    try:
        link_rebrandly = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/form/div[2]/label/div/div/textarea").send_keys(panda)
        time.sleep(8)

    except:
        link_rebrandly = driver.find_element_by_class_name("FormControl__input").send_keys(panda)
        time.sleep(8)
    try:
        creat_link_boredoanda = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/form/div[3]/div[2]/div[2]/button").send_keys("\n")
    except:
        nberko_ela_ok=driver.find_element_by_xpath("/html/body/div[39]/div/div/div/div/button").click()
        zid_number = driver.find_element_by_name("slashtag")
        zid_number.send_keys("hh")
        time.sleep(5)
        creat_link_boredoanda = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div/form/div[3]/div[2]/div[2]/button").send_keys("\n")

    time.sleep(5)
    short_link_rebrandly = driver.find_element_by_xpath("/html/body/div[8]/div/div/div/header/div[1]/div[1]/p").text
    time.sleep(5)

    # past content on notepad online and copy it

    driver.get("https://anotepad.com/")
    time.sleep(5)
    answer_on_quora = driver.find_element_by_name("notecontent")
    answer_on_quora.send_keys(title)
    answer_on_quora.send_keys(Keys.ENTER)
    answer_on_quora.send_keys(Keys.ENTER)
    answer_on_quora.send_keys(first_paragraph)
    answer_on_quora.send_keys(Keys.ENTER)
    answer_on_quora.send_keys(Keys.ENTER)

    answer_on_quora.send_keys(ONE)
    answer_on_quora.send_keys(Keys.ENTER)
    answer_on_quora.send_keys(Keys.ENTER)
    time.sleep(3)

    try:
        answer_on_quora.send_keys(photo1)
    except:
        pass
    answer_on_quora.send_keys(Keys.ENTER)
    answer_on_quora.send_keys(Keys.ENTER)
    time.sleep(3)
    answer_on_quora.send_keys(TWO)
    answer_on_quora.send_keys(Keys.ENTER)
    answer_on_quora.send_keys(Keys.ENTER)
    try:
        answer_on_quora.send_keys(photo2)
    except:
        pass
    answer_on_quora.send_keys(Keys.ENTER)
    answer_on_quora.send_keys(Keys.ENTER)
    answer_on_quora.send_keys(THREE)
    answer_on_quora.send_keys(Keys.ENTER)
    answer_on_quora.send_keys(Keys.ENTER)
    try:
        answer_on_quora.send_keys(photo3)

    except:
        pass
    answer_on_quora.send_keys(Keys.ENTER)
    answer_on_quora.send_keys(Keys.ENTER)
    answer_on_quora.send_keys(reba)
    answer_on_quora.send_keys(Keys.ENTER)
    answer_on_quora.send_keys(Keys.ENTER)
    try:
        answer_on_quora.send_keys(photo4)
    except:
        pass
    answer_on_quora.send_keys(Keys.ENTER)
    answer_on_quora.send_keys(Keys.ENTER)
    answer_on_quora.send_keys(FOUR)
    answer_on_quora.send_keys(Keys.ENTER)
    answer_on_quora.send_keys(Keys.ENTER)
    try:
        answer_on_quora.send_keys(photo5)
    except:
        pass
    answer_on_quora.send_keys(Keys.ENTER)
    answer_on_quora.send_keys(Keys.ENTER)
    answer_on_quora.send_keys(FIVE)
    answer_on_quora.send_keys(Keys.ENTER)
    answer_on_quora.send_keys(Keys.ENTER)

    try:
        answer_on_quora.send_keys(photo6)
    except:
        pass
    answer_on_quora.send_keys(Keys.ENTER)
    answer_on_quora.send_keys(Keys.ENTER)
    answer_on_quora.send_keys(SIX)
    answer_on_quora.send_keys(Keys.ENTER)
    answer_on_quora.send_keys(Keys.ENTER)

    try:
        answer_on_quora.send_keys(photo7)
    except:
        pass
    answer_on_quora.send_keys(Keys.ENTER)
    answer_on_quora.send_keys(Keys.ENTER)
    answer_on_quora.send_keys(SEVEN)
    answer_on_quora.send_keys(Keys.ENTER)
    answer_on_quora.send_keys(Keys.ENTER)
    try:
        answer_on_quora.send_keys(photo8)
    except:
        pass
    answer_on_quora.send_keys(Keys.ENTER)
    answer_on_quora.send_keys(Keys.ENTER)
    answer_on_quora.send_keys("SEE ALL COMICS HERE : " + short_link_rebrandly)
    answer_on_quora.send_keys(Keys.ENTER)
    answer_on_quora.send_keys(Keys.ENTER)

    time.sleep(5)
    answer_on_quora.send_keys("\n")
    answer_on_quora.send_keys(Keys.CONTROL + "a")
    answer_on_quora.send_keys(Keys.CONTROL + "c")
    # login quora

    driver.get("http://www.quora.com/")
    time.sleep(5)

    form = driver.find_element_by_class_name('regular_login')
    email = form.find_element_by_name("email")
    email.send_keys(usr)
    password = form.find_element_by_name("password")
    password.send_keys(pwd)
    time.sleep(5)

    password.send_keys(Keys.RETURN)

    time.sleep(5)

    driver.get(question)

    button_answer = driver.find_element_by_css_selector(".qu-px--large > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > button:nth-child(1)")
    button_answer.click()
    time.sleep(5)
    jawab = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/div/div[1]/div[1]/div[2]/div[2]/div[2]/div/div[1]/div")

    jawab.click()
    jawab.send_keys(Keys.CONTROL + "v")
    jawab.send_keys(Keys.ENTER)
    time.sleep(20)
    save_draft=driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/div/div[1]/div[1]/div[2]/div[3]/div[2]/div[1]/button[2]")
    save_draft.click()
    time.sleep(5)
    driver.close()

# this part is about copyright, you can put the link of Instagram or your website, I was put my Instagram

def callback(url):
    webbrowser.open_new(url)
myWidget = Label(root, text="Powered by @Zakaria_0.75")
myWidget.pack(side="bottom")
myWidget.bind("", lambda e: callback("https://www.instagram.com/zakaria_0.75/"))
myFont = font.Font(family='Helvetica', size=15, weight='bold')

botona = Button(text = "Start",command=my_machine, bg="GREEN", fg="white", height=2, width=10)
botona['font'] = myFont
botona.pack()

root.mainloop()

#The end, See you in the next code