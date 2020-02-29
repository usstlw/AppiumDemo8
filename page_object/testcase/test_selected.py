import pytest

from page_object.driver import AndroidClient
from page_object.page.App import App
from page_object.page.MainPage import MainPage


class TestSelected(object):
    mainPage:MainPage

    @classmethod
    def setup_class(    cls):
        cls.mainPage=App.main()

    def test_price(self):
        assert self.mainPage.gotoSelected().gotoHS().getPriceByName("科大讯飞")==40.99

