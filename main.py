from selenium import webdriver 
import time
PATH = "./chromedriver.exe"
def get_posts():
    global PATH
    PATH = "./chromedriver.exe"
    username  = input("enter your username:")
    driver = webdriver.Chrome(executable_path= PATH)
    driver.get("https://instagram.com/"+ username)
    xpath = '//*[@id="react-root"]/section/main/div/div[3]/article/div/div/div[#row of the post#]/div[#actual post]/a'

    time.sleep(4)
    post_list  = []
    time.sleep(4)
    for i in range(1,4):
        print(i)
        post_list.append(driver.find_elements_by_xpath(f'//*[@id="react-root"]/section/main/div/div[3]/article/div/div/div[1]/div[{i}]/a'))
    print(post_list)
    print("INDIVIDUAL ELEMENTS")
    links = []
    for element in post_list:
        print(type(element))
        for e in element:
            links.append(e.get_attribute('href'))
            print(type(e))

    print(links)
    with open('links.txt','w') as writer:
        for link in links:
            writer.write(link+'\n')

    driver.close()

def go_and_get():
    global PATH
    PATH = "./chromedriver.exe"
    driver = webdriver.Chrome(executable_path= PATH)
    with open('links.txt','r') as reader:
        links = reader.readlines()
    
    for link in links:
        driver.get(link)
        image_xpath  = '//*[@id="react-root"]/section/main/div/div[1]/article/div/div[1]/div/div[1]/div[2]/div/div/div/ul/li[2]/div/div/div/div[1]/img'
        # download image and write it to /images
        image_second_path = '//img[@alt and @crossorigin = "anonymous"][1]'
        link = driver.find_element_by_xpath(image_xpath).get_attribute('href')

        time.sleep(10)
        driver.close()


def make_collage():
    pass

def get_profile():
    global PATH
    driver = webdriver.Chrome(executable_path=PATH)
    driver.get('https://instagram.com/rakshit.dahal')
    pfp = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/div/div/span/img').get_attribute('src')
    driver.get(pfp)



# get_posts()
# go_and_get()
# make_collage()
get_profile()

