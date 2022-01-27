import unittest
from HomePage import HomePage
from api_testing import booking_api_test
import HtmlTestRunner


class Restful_Booker_test(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        self.new_test = HomePage()
        self.verificationErrors = []

    @classmethod
    def test_contect_us(self):
        try: assert self.new_test.contect_us() == "We'll get back to you about"
        except AssertionError as e: self.verificationErrors.append(str(e))
    
    @classmethod
    def test_book_room(self):
        try: assert self.new_test.book_room() == "Booking Successful!"
        except AssertionError as e: self.verificationErrors.append(str(e))

    @classmethod
    def test_book_room_taken(self):
        try: assert self.new_test.book_room_taken()[:5] == "The r"
        except AssertionError as e: self.verificationErrors.append(str(e))

    @classmethod
    def tearDownClass(self):
        self.new_test.driver.close()
        try:
            assert len(self.verificationErrors) == 0  
        except:
            for message in self.verificationErrors:
                print(str(message))
            raise

class Restful_Booker_api_test(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.new_test = booking_api_test()
        self.Errors = []
    
    @classmethod
    def test_POST(self):
        try: assert  self.new_test.POST_Booking()['booking']["firstname"] == "Fred"
        except AssertionError as e: self.Errors.append(str(e))
    
    @classmethod
    def test_GET(self):
        try: assert self.new_test.GET_Booking()['firstname'] == "Fred"
        except AssertionError as e: self.Errors.append(str(e))
    
    @classmethod
    def test_PATCH(self):
        try: assert self.new_test.PATCH_Booking()['bookingdates']['checkout'] == "2022-02-08"
        except AssertionError as e: self.Errors.append(str(e))
    
    @classmethod
    def test_DELETE(self):
        try: assert self.new_test.DELETE_Booking() == "Created"
        except AssertionError as e: self.Errors.append(str(e))
    
    @classmethod
    def tearDownClass(self):
        try:
            assert len(self.Errors) == 0  
        except AssertionError:
            for message in self.Errors:
                print(str(message))
            raise

def suite(runs):
    suite = unittest.TestSuite()
    for i in range(runs):
        suite.addTest(Restful_Booker_test("test_book_room"))
        suite.addTest(Restful_Booker_test("test_book_room_taken"))
        suite.addTest(Restful_Booker_test("test_contect_us"))
        suite.addTest(Restful_Booker_api_test("test_POST"))
        suite.addTest(Restful_Booker_api_test("test_GET"))
        suite.addTest(Restful_Booker_api_test("test_PATCH"))
        suite.addTest(Restful_Booker_api_test("test_DELETE"))
    return suite


if __name__ == '__main__':
    runs = int(input("How many test?"))
    test_runner = HtmlTestRunner.HTMLTestRunner(output='example_dir')
    test_runner.run(suite(runs))