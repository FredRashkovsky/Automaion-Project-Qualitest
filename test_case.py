from HomePage import HomePage
from api_testing import booking_api_test
import pytest

class TestRestfulBooker:
    
    def setup_method(self):
        self.new_test = HomePage()
    
    def test_contect_us(self):
        self.new_test.contect_us() == "We'll get back to you about"
    
    def test_book_room(self):
        self.new_test.book_room() == "Booking Successful!"
    
    def test_book_room_taken(self):
        self.new_test.book_room_taken()[:5] == "The r"

    def teardown_method(self):
        self.new_test.driver.close()


class TestAPI:
    
    def setup_method(self):
        self.new_test = booking_api_test()
        assert self.new_test.POST_Booking()['booking']["firstname"] == "Fred"

    
    def test_GET(self):
        assert self.new_test.GET_Booking()['firstname'] == "Fred"
        
    
    def test_PATCH(self):
        assert self.new_test.PATCH_Booking()['bookingdates']['checkout'] == "2022-02-08"
    
    def test_DELETE(self):
        assert self.new_test.DELETE_Booking() == "Created"


if __name__ == '__main__':
    pytest.main()
