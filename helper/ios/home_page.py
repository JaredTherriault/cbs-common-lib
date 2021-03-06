from helper.android.base_page import BasePage

PAID = "paid"


class HomePage(BasePage):
    def __init__(self, driver, event):
        super(HomePage, self).__init__(driver, event)

    def home_marquee_container(self, timeout=10):
        return self.get_element(timeout=timeout, id=self.com_cbs_app + ':id/homeMarqueeContainer')

    def validate_page(self):
        self.verify_exists(element=self.btn_hamburger_menu(), screenshot=True)
        self.verify_exists(element=self.img_logo())
        self.verify_exists(element=self.btn_search_icon())
        self.verify_exists(element=self.home_marquee_container())

    def click_all_access_video(self):
        if self.exists(name='Free Episodes', timeout=10):
            self._short_swipe_down(duration=3000)
        if self.exists(name=PAID, timeout=5):
            list_episodes = self.get_elements(name=PAID)
            self.click(element=list_episodes[0])
        else:
            prime_container = self.get_element(xpath="//android.widget.LinearLayout[./android.widget.TextView[contains(@text,'Primetime')]]")
            for _ in range(0, 40):
                self._short_swipe_left(prime_container, 500)
            count = 0
            while count < 70:
                self._short_swipe_left(prime_container, 1000)
                if self.exists(name=PAID, timeout=5):
                    list_episodes = self.get_elements(name=PAID)
                    self.click(element=list_episodes[0])
                    break
                else:
                    count += 1
