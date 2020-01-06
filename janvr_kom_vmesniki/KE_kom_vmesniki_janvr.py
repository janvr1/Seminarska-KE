#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 14:41:51 2019

@author: jan
"""
#%% IMPORT
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#%% UART
df_uart_even = pd.read_csv('uart_8E1.csv', index_col=0, usecols=[0,1])
df_uart_odd = pd.read_csv('uart_8O1.csv', index_col=0, usecols=[0,1])

t_even = df_uart_even.index.to_numpy()*1e6
ch1_even = df_uart_even['CH1[V]'].to_numpy()

t_odd = df_uart_odd.index.to_numpy()*1e6
ch1_odd = df_uart_odd['CH1[V]'].to_numpy()

uart_xticks = np.arange(0, max(t_even), 104)

plt.figure()

plt.subplot(2, 1, 1)
plt.plot(t_even, ch1_even, label='Soda pariteta')
plt.xlabel('Čas $[\mu s]$')
plt.ylabel('Napetost $[V]$')
plt.xlim([-50, 1100])
plt.xticks(uart_xticks)
plt.yticks([0, 3.3])
plt.grid(axis='x')
plt.legend(loc='upper center')

plt.subplot(2, 1, 2)
plt.plot(t_odd, ch1_odd, label='Liha pariteta', color='red')
plt.xlabel('Čas $[\mu s]$')
plt.ylabel('Napetost $[V]$')
plt.xlim([-50, 1100])
plt.xticks(uart_xticks)
plt.yticks([0, 3.3])
plt.grid(axis='x')
plt.legend(loc='upper center')

#%% I2C
df_i2c = pd.read_csv('i2c.csv', index_col = 0, usecols=[0, 1, 2])

t_i2c = df_i2c.index.to_numpy()*1e6
sda = df_i2c['CH1[V]'].to_numpy()
scl = df_i2c['CH2[V]'].to_numpy()

i2c_xticks = np.arange(2.8, max(t_i2c), 10.33)

plt.figure()

plt.subplot(2, 1, 1)
plt.plot(t_i2c, scl, label='SCL')
plt.xlabel('Čas $[\mu s]$')
plt.ylabel('Napetost $[V]$')
plt.xticks(i2c_xticks)
plt.yticks([0, 3.3])
plt.grid(axis='x')
plt.xlim([-10, 210])
plt.legend(loc='lower right')

plt.subplot(2, 1, 2)
plt.plot(t_i2c, sda, color='red', label='SDA')
plt.xlabel('Čas $[\mu s]$')
plt.ylabel('Napetost $[V]$')
plt.xticks(i2c_xticks)
plt.yticks([0, 3.3])
plt.grid(axis='x')
plt.xlim([-10, 210])
plt.legend(loc='lower right')
#%% SPI

df_spi = pd.read_csv('spi.csv', index_col=0, usecols=[0, 1, 2])

t_spi = df_spi.index.to_numpy()*1e6
mosi = df_spi['CH1[V]'].to_numpy()
sclk = df_spi['CH2[V]'].to_numpy()

spi_xticks = np.arange(0, max(t_spi), 10);

plt.figure()

plt.subplot(2, 1, 1)
plt.plot(t_spi, sclk, label='SCLK')
plt.xlabel('Čas $[\mu s]$')
plt.ylabel('Napetost $[V]$')
plt.xticks(spi_xticks)
plt.yticks([0, 3.3])
plt.grid(axis='x')
plt.xlim([-10, 90])
plt.legend(loc='upper right')

plt.subplot(2, 1, 2)
plt.plot(t_spi, mosi, color='red', label='MOSI')
plt.xlabel('Čas $[\mu s]$')
plt.ylabel('Napetost $[V]$')
plt.xticks(spi_xticks)
plt.yticks([0, 3.3])
plt.grid(axis='x')
plt.xlim([-10, 90])
plt.legend(loc='upper right')
