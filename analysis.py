import plotly.graph_objects as go
import plotly.io as pio
import pandas as pd

df = pd.read_csv("hindalco.csv")

trace_ohlc = go.Candlestick(x=df.index,
                             open=df['open'],
                             high=df['high'],
                             low=df['low'],
                             close=df['close'],
                             name='OHLC')

df['Short_MA'] = df['close'].rolling(window=50).mean()
df['Long_MA'] = df['close'].rolling(window=200).mean()
trace_short_ma = go.Scatter(x=df.index, y=df['Short_MA'], mode='lines', name='Short MA')
trace_long_ma = go.Scatter(x=df.index, y=df['Long_MA'], mode='lines', name='Long MA')

buy_signals = df[df['Short_MA'] > df['Long_MA']]
sell_signals = df[df['Short_MA'] < df['Long_MA']]
trace_buy_signals = go.Scatter(x=buy_signals.index, y=buy_signals['close'], mode='markers', 
                               name='Buy Signal', marker=dict(color='green', size=10))
trace_sell_signals = go.Scatter(x=sell_signals.index, y=sell_signals['close'], mode='markers', 
                                name='Sell Signal', marker=dict(color='red', size=10))
print(buy_signals)
fig = go.Figure(data=[trace_ohlc, trace_short_ma, trace_long_ma, 
                      trace_buy_signals, trace_sell_signals])

fig.update_layout(title='OHLC Chart with MA Signals')
pio.write_image(fig, "analysis.png")
fig.show()
