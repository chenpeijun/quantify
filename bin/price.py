import sys;
import re;
import math;
import talib;
import numpy as np
from tools import *;

class Price(object):
	def __init__(self, ticker):
		self.ticker = ticker;
		self.info = {}
		self.bsp = {} 
		self._price('day');

	def _price(self, ktype):
		for code in self.ticker.keys():
			cinfo = self.ticker[code]['stock'];
			close_info = cinfo['Close'];
			close_arr = sorted(close_info.items(),key=lambda x:x[0], reverse=False);
			highest_arr = []
			lowest_arr = []
			for i in range(len(close_arr)):
				current_price = close_arr[i][1];
				beg = max(0,i - 5);
				end = min(len(close_arr), i + 5);
				is_highest = 1
				is_lowest = 1
				while beg < end:
					if close_arr[beg][1] > current_price:
						is_highest = 0
					if close_arr[beg][1] < current_price:
						is_lowest = 0
					beg += 1
				if is_highest == 1:
					highest_arr.append([close_arr[i][0], close_arr[i][1], i]);
					#print("high\t" +code + "\t" + close_arr[i][0] + "\t" + str(close_arr[i][1]) +"\t" +  str(i));
				if is_lowest == 1:
					lowest_arr.append([close_arr[i][0], close_arr[i][1], i]);
			
			current_price = close_arr[-1][1];
			current_day = close_arr[-1][0];
			
			if len(highest_arr) > 0:
				latest_highest_price = highest_arr[-1][1];	
				max_highest_price = max(highest_arr, key = lambda x: x[0])[1];
				chg_of_latest_highest_price = round((current_price-latest_highest_price)/latest_highest_price,2);
				#print(code + "\tchg_of_latest_highest_price:" +  str(chg_of_latest_highest_price));
				chg_of_max_highest_price = round((current_price-max_highest_price)/max_highest_price,2);
				insert(code,"chg_of_latest_highest_price",current_day, chg_of_latest_highest_price, self.bsp);
				#print(code + "\tchg_of_max_highest_price:" +  str(chg_of_max_highest_price));
				insert(code,"chg_of_max_highest_price",current_day, chg_of_max_highest_price, self.bsp);

			if len(lowest_arr) > 0:
				latest_lowest_price = lowest_arr[-1][1];	
				min_lowest_price = min(lowest_arr, key=lambda x: x[1])[1];
				chg_of_latest_lowest_price = round((current_price-latest_lowest_price)/latest_lowest_price,2);
				insert(code,"chg_of_latest_lowest_price",current_day, chg_of_latest_lowest_price,self.bsp);
				#print(code + "\tchg_of_latest_lowest_price:" +  str(chg_of_latest_lowest_price));
				chg_of_min_lowest_price = round((current_price-min_lowest_price)/min_lowest_price,2);
				insert(code,"chg_of_min_lowest_price",current_day, chg_of_min_lowest_price,self.bsp);
				#print(code + "\tchg_of_min_lowest_price:" +  str(chg_of_min_lowest_price));
