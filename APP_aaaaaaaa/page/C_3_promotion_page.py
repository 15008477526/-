from page.B_main_page import MainPage


class PromotionPage(MainPage):
    """促销页面"""
    pomelo_loc = ('xpath', '//*[@text="Pomelo rosado"]')

    def click_pomelo(self):
        """点击pomelo商品"""
        self.click(self.pomelo_loc)

