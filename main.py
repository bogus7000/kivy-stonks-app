from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from dashboard_tab import DashboardTab
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.tab import MDTabs
from app_util import AppUtil
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivy.uix.scrollview import ScrollView
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.dialog import MDDialog
import logging
Window.size = (375, 620)

class AppTabs(MDTabs):
    def __init__(self, **kwargs):
        super().__init__(
            background_color=[0, 0, 0, 1],
            text_color_normal=[1, 1, 1, 0.3],
            text_color_active=[1, 1, 1, 1],
        )


class SettingsTab(ScrollView, MDTabsBase):
    def __init__(self, **kwargs):
        super(SettingsTab, self).__init__(**kwargs)
        app_util = AppUtil()

        self.label = MDLabel(
            text="Tickers To Track",
            font_style="H6",
            theme_text_color="Custom",
            text_color=[1, 1, 1, 1],
            halign="left",
            valign="center",
        )

        tickers = app_util.get_tickers()
        tickers_str = ""
        for ticker in tickers:
            tickers_str += ticker + ", "
        self.field = MDTextField(
            text=tickers_str,
        )
        self.button = MDRaisedButton(
            text="Update Dashboard",
        )
        self.button.bind(on_press=self.show_popup)

        self.dialog_updating = MDDialog(
            text="Hang in while we update your stock widgets",
            type="custom",
            size_hint=(.8, .8)
        )
        self.dialog_updating.bind(on_open=self.save_tickers)

        self.layout = MDBoxLayout(
            orientation="vertical",
            padding="20dp",
            adaptive_height=True
        )
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.field)
        self.layout.add_widget(self.button)

        self.add_widget(self.layout)

    def show_popup(self, instance):
        self.dialog_updating.open()

    def save_tickers(self, instance):
        app_util = AppUtil()
        app_util.set_tickers(self.field.text)
        app = MainApp.get_running_app()
        app.refresh_tickers()
        self.dialog_updating.dismiss()


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.tabs = AppTabs()

        self.dash_tab = DashboardTab(
            text="DASHBOARD",
        )

        self.settings_tab = SettingsTab(
            text="SETTINGS",
        )

        self.tabs.add_widget(self.dash_tab)
        self.tabs.add_widget(self.settings_tab)

        self.screen = MainScreen(name="main_screen")
        self.screen.add_widget(self.tabs)


        self.sm = ScreenManager()
        self.sm.add_widget(self.screen)

        return self.sm

    def refresh_tickers(self):
            self.dash_tab.ref()

MainApp().run()
