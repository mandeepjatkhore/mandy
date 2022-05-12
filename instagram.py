from selenium import webdriver 
import time 

username = "your username" 
password = "your password"


# starts a new chrome session 
chrome = webdriver.Chrome("E:\chromedriver.exe")
time.sleep(1)

#maximize the window size  
chrome.maximize_window()

#navigate to the url
chrome.get("https://www.instagram.com/")
time.sleep(4)

# finds the username box 
usern = chrome.find_element_by_name("username")     
# sends the entered username 
usern.send_keys(username)    
  
# finds the password box 
passw = chrome.find_element_by_name("password")     
  
# sends the entered password 
passw.send_keys(password)

time.sleep(2) 
  
# finds the login button 
log_cl = chrome.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]")     
log_cl.click()   # clicks the login button 
time.sleep(7)

# finds the not now savelogin info button
notnowinfo= chrome.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")     
notnowinfo.click()   # clicks the not now button
time.sleep(7) 
                                                                                    
# finds the not now turn on notification button
notnownotification= chrome.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]")     
notnownotification.click()   # clicks the not now button
time.sleep(7) 

#scrolling
for keeponscrollingbro in range(8):
    chrome.execute_script("window.scrollBy(0,300)", "")
    time.sleep(2)

chrome.get("https://www.instagram.com/direct/inbox/")
time.sleep(4)

chrome.get("https://www.instagram.com/accounts/edit/")
time.sleep(4)









