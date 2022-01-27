from selenium.webdriver.common.by import By


class locators:
    contect_us_Locators = { (By.XPATH ,'//*[@id="name"]'):"fred",
                            (By.XPATH ,'//*[@id="email"]'):"test@gmail.com",
                            (By.XPATH ,'//*[@id="phone"]'):"01234567899",
                            (By.XPATH ,'//*[@id="subject"]'):"it's just a test",
                            (By.XPATH ,'//*[@id="description"]'):"it's more of the same test sdfsdfsd fsdf sdf sdfsdfsdf"}
    
    contect_us_submit_button = (By.XPATH ,'//*[@id="submitContact"]')
    constans_us_succsessful = (By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[5]/div[2]/div[1]/p[1]")


    book_room_button = (By.XPATH, '//*[@id="root"]/div/div/div[4]/div/div/div[3]/button')
    book_room_next_button = (By.XPATH, '//*[@id="root"]/div/div/div[4]/div/div[2]/div[2]/div/div[1]/span[1]/button[3]')
    book_room_submit_button = (By.XPATH, '//*[@id="root"]/div/div/div[4]/div/div[2]/div[3]/button[2]')
    book_room_successful = (By.XPATH, "/html[1]/body[1]/div[4]/div[1]/div[1]/div[1]/div[2]/h3[1]")
    book_room_close_button = (By.XPATH, "/html/body/div[4]/div/div/div[2]/div/button")
    book_room_all_days = (By.CLASS_NAME, "rbc-day-bg")
    book_room_all_Unavailable = (By.CLASS_NAME, "rbc-event-content")
    book_room_all_alert = (By.XPATH, '//*[@id="root"]/div[2]/div/div[4]/div/div[2]/div[3]/div[5]')

    book_room_fileds_locators = {(By.XPATH, '//*[@id="root"]/div/div/div[4]/div/div[2]/div[3]/div[1]/input'):"fred",
                                  (By.XPATH, '//*[@id="root"]/div/div/div[4]/div/div[2]/div[3]/div[2]/input'):"rashkovsky",
                                  (By.XPATH, '//*[@id="root"]/div/div/div[4]/div/div[2]/div[3]/div[3]/input'):"test@gmail.com",
                                  (By.XPATH, '//*[@id="root"]/div/div/div[4]/div/div[2]/div[3]/div[4]/input'):"01234567899"}
    
