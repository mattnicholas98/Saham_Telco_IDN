import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

excl = pd.read_csv(
    'EXCL.JK.csv',
    index_col=False,
    parse_dates=['Date']
)

fren = pd.read_csv(
    'FREN.JK.csv',
    index_col=False,
    parse_dates=['Date']
)

isat = pd.read_csv(
    'ISAT.JK.csv',
    index_col=False,
    parse_dates=['Date']
)

tlkm = pd.read_csv(
    'TLKM.JK.csv',
    index_col=False,
    parse_dates=['Date']
)

plt.style.use('seaborn')

plt.plot(excl['Date'], excl['Close'], 'r')
plt.plot(fren['Date'], fren['Close'], 'g')
plt.plot(isat['Date'], isat['Close'], 'b')
plt.plot(tlkm['Date'], tlkm['Close'], 'y')

plt.suptitle('Harga Historis Saham Provider Telco Indonesia')
plt.xlabel('Tanggal')
plt.ylabel('Rupiah (IDR)')
plt.xticks(rotation=45)
plt.legend(['PT XL Axiata Tbk', 'PT Smartfren Telecom Tbk', 'PT Indosat Tbk', 'PT Telekomunikasi Indonesia Tbk'], loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=4, frameon=False)
plt.show()