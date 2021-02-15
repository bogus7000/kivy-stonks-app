import pandas as pd
import datetime as dt
from datetime import date
import plotly.graph_objects as go
import os
import yfinance as yf
import json


class AppUtil:
    store_path = 'store.json'
    fig_dir_path = 'figures'

    def set_store_path(self, path):
        AppUtil.store_path = path

    def set_tickers(self, string):
        tick_arr = string.split(",")
        print(tick_arr)
        if (tick_arr[len(tick_arr) - 1] == " " or tick_arr[len(tick_arr) - 1] == ""):
            tick_arr.pop(len(tick_arr) - 1)
        print(tick_arr)
        tick_arr_stripped = [x.strip() for x in tick_arr]
        print(tick_arr_stripped)

        with open(AppUtil.store_path) as file:
            data = json.load(file)

        data["tickers"] = tick_arr_stripped
        print(data)

        with open(AppUtil.store_path, "w+") as file:
            json.dump(data, file)

    def get_tickers(self):
        with open(AppUtil.store_path) as file:
            data = json.load(file)
        return(data["tickers"])

    def get_store_path(self, path):
        return AppUtil.store_path

    def get_current_price(self, ticker):
        tick = yf.Ticker(ticker)
        todays_data = tick.history(period='1d')
        return todays_data['Close'][0]

    def clean_figures(self):
        cmd = 'rm -rf ' + AppUtil.fig_dir_path + ' -v'
        os.system(cmd)
        cmd = 'mkdir' + AppUtil.fig_dir_path + ' -v'
        os.system('mkdir app/figures -v')

    def gen_plot(self, ticker, range):
        tickerData = yf.Ticker(ticker)

        end = date.today()
        DD = dt.timedelta(days=range)
        start = end - DD

        tickerDf = tickerData.history(period='1d', start=start, end=end)
        tickerDf['Date'] = tickerDf.index

        fig = go.Figure(data=[go.Candlestick(x=tickerDf['Date'],
                                             open=tickerDf['Open'],
                                             high=tickerDf['High'],
                                             low=tickerDf['Low'],
                                             close=tickerDf['Close'])])

        fig.update_layout(
            template="plotly_dark",
            paper_bgcolor="#424242",
            plot_bgcolor="#424242",
            xaxis_gridcolor="rgba(255, 255, 255, 0.3)",
            yaxis_gridcolor="rgba(255, 255, 255, 0.3)",
            xaxis_rangeslider_visible=False,
            margin_l=0,
            margin_r=0,
            margin_b=0,
            margin_t=0,
            xaxis_tickformat='%d %b',
            width=340,
            height=200
        )

        png_path = AppUtil.fig_dir_path + '/' + ticker.upper() + '.png'
        fig.write_image(png_path)

    def gen_plots_from_array(self, range):
        with open(AppUtil.store_path) as file:
            data = json.load(file)
        print(data)
        for ticker in data["tickers"]:
            self.gen_plot(ticker, range)

    def get_fig_path(self, ticker):
        png_path = AppUtil.fig_dir_path + '/' + ticker + '.png'
        return png_path

    def get_fig_paths(self):
        with open(AppUtil.store_path) as file:
            data = json.load(file)
        print(data)

        paths = []

        for ticker in data["tickers"]:
            png_path = AppUtil.fig_dir_path + '/' + ticker + '.png'
            paths.append(png_path)

        return paths


app_util = AppUtil()
app_util.gen_plot("AAPL", 45)
