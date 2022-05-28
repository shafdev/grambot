import requests
import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from random import randint

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException



class GramBot:
    def __init__(self,driver):
        self.driver = driver

    @classmethod
    def chrome(cls):
        try:
            path = './chromedriver.exe'
            service = Service(path)
            driver = webdriver.Chrome(service = service)
            driver.get('https://www.instagram.com/')
            return cls(driver)
        except OSError:
            raise OSError


    def get_element_by_xpath(self,xpath):
        #returns single element if you enter xpath
        element = self.driver.find_element(By.XPATH,xpath)
        return element

    def get_element_bycss(self,css_selector):
        css = css_selector
        element = self.driver.find_element(By.CSS_SELECTOR,css)
        return element
            
            
    def enter_username(self,username):
        try:
            username_in = self.driver.find_element(By.NAME, "username")
            #password = 'vicky@1234'
            time.sleep(0.5)
            username_in.clear()
            username_in.send_keys(username)
            print("\n \n Have Entered Your username \n \n")
            time.sleep(1)
        except:
            print('something went worng while entering username')
        
    def enter_password(self,password):
        try:
            password_in = self.driver.find_element(By.NAME, "password")
            #password = 'vicky@1234'
            time.sleep(0.5)
            
            password_in.clear()
            password_in.send_keys(password)
            print("\n \n Have Entered Your Password \n \n")
            time.sleep(1)
        except:
            print('something went worng while entering password')
        
    def click_login(self):
        try:
            driver= self.driver
            logx = '.L3NKy'
            log = driver.find_element(By.CSS_SELECTOR,logx)
            log.click()
            print('Logged in successfully...')
        except Exception:
            #raise Exception('Pleas enter Userid and Password')
            print('Enter User id & password')
            
        
    def logout(self):
        settx = 'span.qNELH'
        sett = self.driver.find_element(By.CSS_SELECTOR,settx)
        sett.click()
        time.sleep(2)
        logoutx = 'div.-qQT3:nth-child(6)'
        logout = self.driver.find_element(By.CSS_SELECTOR,logoutx)
        logout.click()
        print('\n\nLogged Out\n\n')

    def not_now(self):
        not_now_css = 'button.sqdOP:nth-child(1)'
        not_now_x = "//*[contains(text(), 'Not Now')]"
        #not_now = self.driver.find_element(By.CSS_SELECTOR,not_now_css)
        not_now = self.driver.find_element(By.XPATH,not_now_x)
        not_now.click()
    
    def turn_off_notification(self):
        turn_off_css = 'button.aOOlW:nth-child(2)'
        turn_off = self.driver.find_element(By.CSS_SELECTOR,turn_off_css)
        turn_off.click()
    
    #for random clicking
    def click_setting_button(self):
        settx = 'span.qNELH'
        sett = self.driver.find_element(By.CSS_SELECTOR,settx)
        sett.click()
        
    def back_from_settings(self):
        settx = 'body'
        sett = self.driver.find_element(By.CSS_SELECTOR,settx)
        sett.click()
        
    def search_hashtag(self,hashtag):
        try:
            search_hash = 'https://www.instagram.com/explore/tags/{hashtag}/'.format(hashtag=hashtag)
            search = self.driver.get(search_hash)
        except:
            print('something went wrong while searching hashtag')
            
    def scrollDown(self,x):
        i=0.7
        while i < x:

            self.driver.execute_script('window.scrollBy(0,{i})'.format(i=i))
            i=i+0.7
            time.sleep(0.01)
            
    def scrollUp(self,x):
        i=0.7
        while i < x:

            self.driver.execute_script('window.scrollBy(0,-{i})'.format(i=i))
            i=i+0.7
            time.sleep(0.01)
            
    def click_on_pic(self):
        '''after searching a hashtag it clicks on a photo'''
        row = randint(1,3)
        col = randint(1,3)
        recent_row = randint(4,8) 
        # print(row)
        try:
            hash_path1='/html/body/div[1]/section/main/article/div[1]/div/div/div[{x}]/div[{y}]'.format(x=row,y=col)
        #     hash_x = hash_x[randint(0,1)]
            hash_path2='/html/body/div[1]/section/main/article/div[2]/div/div[{x}]/div[{y}]'.format(x=recent_row,y=col)
            hash_path = [hash_path1,hash_path2]

            hash_x = hash_path[randint(0,1)]
            print(hash_x)
            hash_t =self.driver.find_element(By.XPATH,hash_x)
            hash_t.click()
        except:
            print('search a hashtag first')
            print('something worng wiht hash tag clicker')
            pass
        
    def next_button(self):
        next_x = '/html/body/div[6]/div[2]/div/div[2]/button'
        
        next_button = self.driver.find_element(By.XPATH,next_x)
        next_button.click()
    
    def prev_button(self):
        prev_x = '/html/body/div[6]/div[2]/div/div[1]/button'
        prev_button =self.driver.find_element(By.XPATH,prev_x)
        prev_button.click()
            
    def like(self):
        ''' like after search hashtag,like and unlike '''

        like_css = '.fr66n > button:nth-child(1)'
        like = self.driver.find_element(By.CSS_SELECTOR,like_css)
        like.click()
        
    def back_from_slide(self):
        back_from_framex='.NOTWr > button:nth-child(1)'
        back_from_frame=self.driver.find_element(By.CSS_SELECTOR,back_from_framex)
        back_from_frame.click()
    
    def homepage(self):
        homepage_x = '._7Nzh3 > a:nth-child(1)'

        homepage = self.driver.find_element(By.CSS_SELECTOR,homepage_x)
    #     click_with_xpath(homepage,1)
        homepage.click()
    def is_liked(self):
        ''' verify if it is liked '''
        x='.fr66n > button:nth-child(1) > div:nth-child(1)'
        # try:

        element = self.driver.find_elements(By.CSS_SELECTOR,x)
        for i in element:
            classname = i.get_attribute('class').split()

            #print(classname)
        if len(classname) == 1:
            print('Liked')
        if len(classname) == 2:
            print('NotLiked')
#      lllll       
    def follow_on_slide(self):
        css_path = 'button.sqdOP:nth-child(2)'
        follow_element = self.driver.find_element(By.CSS_SELECTOR,css_path)
        follow_element.click()
        time.sleep(1)
    def unfollow_on_slide(self):
        self.follow_on_slide()
        time.sleep(1)
        css_path = 'button.aOOlW:nth-child(1)'
        unfollow = self.driver.find_element(By.CSS_SELECTOR,css_path)
        unfollow.click()
        time.sleep(1)
        
    def find_people(self,name):
        search_input_x = '/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input'
        search_input = self.driver.find_element(By.XPATH,search_input_x)

        time.sleep(1)
        search_input.clear()
        for i in name:
            search_input.send_keys(i)
            time.sleep(0.2)
        time.sleep(2)
        
    def click_first_search_option(self,num=1):
        #num = '5'
        '''input:after entering into search bar,which option i want to click'''
        first_option_x = f'.fuqBx > div:nth-child({num})'
        first_option = self.driver.find_element(By.CSS_SELECTOR,first_option_x)
        first_option.click()
        
    def follow(self):
        '''#follows on profile pages'''
        follow_css = '._6VtSN'

        follow = self.driver.find_element(By.CSS_SELECTOR,follow_css)
        follow.click()
        print('followed')
        time.sleep(2)
        
    def unfollow(self):
        '''#follows on profile pages'''
        self.follow() #click on follow options
        time.sleep(1)
        unfollow_x = 'button.aOOlW:nth-child(1)'
        unfollow = self.driver.find_element(By.CSS_SELECTOR,unfollow_x)
        unfollow.click()
        print('Unfollowed')
        time.sleep(2)
        
    def like_pic(self):
        ''' like pic from feed '''
        like_css_x = '//*[@id="react-root"]/section/main/section/div/div[3]/div[1]/div/article[4]/div/div[3]/div/div/section[1]/span[1]'
        like = self.get_element_by_xpath(like_css_x)
        like.click()
        
    def post(self):
        post_x = '/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/button'
        post_ele = self.driver.find_element(By.XPATH,post_x)
        post_ele.click()
        time.sleep(2)
        cross_x= '/html/body/div[6]/div[1]/button'
        cross_ele = self.driver.find_element(By.XPATH,cross_x)
        cross_ele.click()
        
    def comment(self,comment):
        comment_x = '//*[@id="react-root"]/section/main/section/div/div[3]/div[1]/div/article[4]/div/div[3]/div/div/section[1]/span[2]/button'
        comment_ele = self.driver.find_element(By.XPATH,comment_x)
        comment_ele.click()
        time.sleep(2)
        comment_xx = '/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[1]/span[2]/button'
        comment_elexx = self.driver.find_element(By.XPATH,comment_xx)
        comment_elexx.click()
        time.sleep(1)
        text_area_x = '/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea'
        text_area_ele = self.driver.find_element(By.XPATH,text_area_x)
        time.sleep(1)
        text_area_ele.clear()
        text_area_ele.send_keys(comment)
        self.post()
        
    def comment_on_slide_post(self,comment): 
        c_x = '/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[1]/span[2]/button'
        c_ele = self.driver.find_element(By.XPATH,c_x)
        c_ele.click()
        t_x = '/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea'
        t_ele = self.driver.find_element(By.XPATH,t_x)
        time.sleep(2)
        t_ele.send_keys(comment)
        time.sleep(2)
        self.post_comment()
        
    def post_comment(self):
        post_comment_css ='button.yWX7d:nth-child(3)'
        post_comment = self.driver.find_element(By.CSS_SELECTOR,post_comment_css)
        post_comment.click()
        
    def delete_posted_comment(self):    
        #hover over to the comment to make the delete button visible
        x='/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/div[1]/ul/ul[1]/div/li/div/div/div[2]/div[1]'
        xpath_hover=x
        a = ActionChains(self.driver)
        m= self.driver.find_element(By.XPATH,xpath_hover)
        a.move_to_element(m).perform()
        time.sleep(2)

        #click the delete optons button to delete the post
        deletex='/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/div[1]/ul/ul[1]/div/li/div/div/div[2]/div[2]/div/div/div/button'
        delete = self.driver.find_element(By.XPATH,deletex)
        delete.click()
        time.sleep(2)

        #finally deleting
        delete_y = '/html/body/div[7]/div/div/div/div/button[2]'
        delete = self.driver.find_element(By.XPATH,delete_y)
        delete.click()
        
    def homepage(self):
        homepage_x = '._7Nzh3 > a:nth-child(1)'

        homepage = self.driver.find_element(By.CSS_SELECTOR,homepage_x)
    #     click_with_xpath(homepage,1)
        homepage.click()
    
    def click_setting_button(self):
        settx = 'span.qNELH'
        sett = self.driver.find_element(By.CSS_SELECTOR,settx)
        sett.click()
        
    def back_from_settings(self):
        settx = 'body'
        sett = self.driver.find_element(By.CSS_SELECTOR,settx)
        sett.click()
    
    def count_follower_inslide(self):
        profile_link_css = '.e1e1d > div:nth-child(1) > span:nth-child(1)'
        profile_link = self.driver.find_element(By.CSS_SELECTOR,profile_link_css)

        po = ActionChains(self.driver)
        # m= driver.find_element(By.CSS_SELECTOR,profile_link)
        po.move_to_element(profile_link).perform()
        time.sleep(2)
        # ****///
        count_follower_css = '.MGdpg > div:nth-child(2) > div:nth-child(1) > span:nth-child(1)'
        count_follower = self.driver.find_elements(By.CSS_SELECTOR,count_follower_css)
        for i in count_follower:
            follower = i.get_attribute('title')
            print('Followers : ' + follower)

        time.sleep(2)
        heart_css = '.fr66n > button:nth-child(1)'
        heart = self.driver.find_element(By.CSS_SELECTOR,heart_css) 
        po.move_to_element(heart).perform()
        
        