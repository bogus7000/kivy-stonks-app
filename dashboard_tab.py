from ticker_widget import TickerWidget
from kivy.uix.scrollview import ScrollView
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import MDList
from app_util import AppUtil


class DashboardTab(ScrollView, MDTabsBase):

    def __init__(self, **kwargs):
        super(DashboardTab, self).__init__(**kwargs)
        self.layout = MDList()
        app_util = AppUtil()
        arr = app_util.get_tickers()
        self.ticker_widgets = []

        for ticker in arr:
            self.ticker_widgets.append(TickerWidget(ticker=ticker))

        for widget in self.ticker_widgets:
            self.layout.add_widget(widget)

        self.add_widget(self.layout)

    def ref(self):
        self.clear_widgets()

        self.layout = MDList()
        app_util = AppUtil()
        arr = app_util.get_tickers()
        ticker_widgets = []

        for ticker in arr:
            ticker_widgets.append(TickerWidget(ticker=ticker))

        for widget in ticker_widgets:
            self.layout.add_widget(widget)

        self.add_widget(self.layout)

