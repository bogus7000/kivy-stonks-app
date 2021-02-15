from kivymd.uix.label import MDLabel
from app_util import AppUtil
from kivymd.uix.card import MDCard
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.image import Image
from kivy.core.window import Window


class TickerWidget(MDCard):
    def __init__(self, **kwargs):
        # Create AppUtil instance
        app_util = AppUtil()

        # Initialize MDCard
        super().__init__(
            orientation="vertical",
            size_hint=[None, None],
            size=["375dp", "320dp"],
            pos_hint={"center_x": .5, "center_y": .5},
            padding="20dp",
            elevation=0,
        )

        # Ticker Label
        tick_str = str(kwargs.get("ticker")).upper()
        label = MDLabel(
            text=tick_str,
            font_style="H6",
            theme_text_color="Custom",
            text_color=[1, 1, 1, 1],
            halign="left",
            valign="center",
        )
        label.height = label.texture_size[1]

        # Ticker Price
        tick_price_raw = str(app_util.get_current_price(tick_str))
        tick_price_split = tick_price_raw.split(".")
        tick_price_final = tick_price_split[0] + "$"
        price = MDLabel(
            text=tick_price_final,
            font_style="H6",
            theme_text_color="Custom",
            text_color=[1, 1, 1, 1],
            halign="right",
            valign="center",
        )
        price.height = price.texture_size[1]

        # Compose Title
        title = MDBoxLayout(
            orientation="horizontal",
            size=["375dp", "40dp"]
        )
        title.add_widget(label)
        title.add_widget(price)
        self.add_widget(title)

        # Ticker Image
        app_util.gen_plot(tick_str, 30)
        path = app_util.get_fig_path(tick_str)
        image = Image(
            source=path,
            size_hint=[None, None],
            allow_stretch=True,
            size=[str(Window.size[0] - 40) + "dp", "280dp"]
        )
        self.add_widget(image)

