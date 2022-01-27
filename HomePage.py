from Locators import locators
from element import elements
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class HomePage(elements):
    def __init__(self):
        elements.__init__(self)
        
    def contect_us(self):
        #fills all the fields
        for key,value in locators.contect_us_Locators.items():self.field(key,value)
        
        self.driver.find_element(*locators.contect_us_submit_button).click()
        #gets the Confirmation
        try: return  WebDriverWait(self.driver, 2).until(EC.presence_of_element_located(locators.constans_us_succsessful)).text
        except: return "faild"
    
    def book_room(self):
        self.driver.find_element(*locators.book_room_button).click()
        days = self.get_element_of_all_days()
        Unavailables = 0
        
        try: Unavailables = self.get_all_dates_that_are_avilable()
        #If it's a free month then there will bot be any "Unavailable" element so it's ok o pass it
        except TimeoutException: pass 
        except: return "falild"
        #fills all the fields
        for key,value in locators.book_room_fileds_locators.items(): self.field(key,value)
        while True:
            #If it's bigger it will be out of index
            if (Unavailables * 3 + 3 ) < len(days):
                try:
                    #Simple math that gives me the next free days after the last "Unavailable" element and then "booking it"
                    self.drag_and_drop(days[(Unavailables * 3 )], days[(Unavailables * 3 ) + 1 ] , days[(Unavailables * 3 ) + 3 ])
                    self.driver.find_element(*locators.book_room_submit_button).click()
                    success = WebDriverWait(self.driver, 1).until(EC.presence_of_element_located(locators.book_room_successful)).text
                    self.driver.find_element(*locators.book_room_close_button).click()
                    return success
                
                except: return "falild"
            
            else:
                try:
                    #All of the month is full so we go next
                    self.driver.find_element(*locators.book_room_next_button).click()
                    Unavailables = self.get_all_dates_that_are_avilable()
                    days = self.get_element_of_all_days()
                except: return "falild"
    #This test tries to book a place that was already taken and sees if it blocks the request 
    def book_room_taken(self):
        self.driver.find_element(*locators.book_room_button).click()
        days = self.get_element_of_all_days()
        self.drag_and_drop(days[0], days[1] , days[3])
        for key,value in locators.book_room_fileds_locators.items(): self.field(key,value)
        
        self.driver.find_element(*locators.book_room_submit_button).click()
        
        try: return WebDriverWait(self.driver, 1).until(EC.presence_of_element_located(locators.book_room_all_alert)).text
        except: return "faild"
