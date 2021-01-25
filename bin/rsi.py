import sys;
import re;
import math;
import talib;
import numpy as np
from tools import *
SUPER_BUY=60
SUPER_SELL=20
MID=50

class Rsi(object):
	def __init__(self, tickerinfo):
		self.ticker = tickerinfo;
		self.info = {}
		self.bsp = {} 
		self._Rsi(6, "Rsi6");
		self._Rsi(12, "Rsi12");
		self._Rsi(24, "Rsi24");
		self._Compute();

	def _super_buy(self,code, rsi6attr,rsi12attr, rsi24attr):
			dif = [(rsi6attr[i][0], rsi6attr[i][1] - rsi12attr[i][1]) for i in range(len(rsi6attr))];
			sbp_cross_list = [[x[0], 0] for x in rsi6attr];
			idx = 1 
			while idx <len(rsi6attr):
				day = sbp_cross_list[idx][0];
				if rsi6attr[idx][1] > SUPER_BUY +10:
					key = "ssuper_buy_rsi6"
					value = "sp";
					insert(code,key,day, value, self.bsp);
				elif rsi6attr[idx][1] > SUPER_BUY and rsi6attr[idx - 1][1] < SUPER_BUY:
					key = "first_super_buy_rsi6"
					value = "sp";
					insert(code,key,day, value, self.bsp);
				elif rsi6attr[idx][1] > SUPER_BUY:
					key = "super_buy_rsi6"
					value = "sp";
					insert(code,key,day, value, self.bsp);
				if rsi12attr[idx][1] > SUPER_BUY - 10:
					key = "super_buy_rsi12"
					value = "sp";
					insert(code,key,day, value, self.bsp);
				if rsi24attr[idx][1] > SUPER_BUY - 20:
					key = "super_buy_rsi24"
					value = "sp";
					insert(code,key,day, value, self.bsp);
				idx += 1
	def _super_sell(self,code, rsi6attr,rsi12attr, rsi24attr):
			dif = [(rsi6attr[i][0], rsi6attr[i][1] - rsi12attr[i][1]) for i in range(len(rsi6attr))];
			sbp_cross_list = [[x[0], 0] for x in rsi6attr];
			idx = 1 
			while idx <len(rsi6attr):
				day = sbp_cross_list[idx][0];
				if rsi6attr[idx][1] < SUPER_SELL - 10:
					key = "ssuper_sell_rsi6"
					value = "bp";
					insert(code,key,day, value, self.bsp);
				elif rsi6attr[idx][1] < SUPER_SELL and rsi6attr[idx - 1][1] > SUPER_SELL:
					key = "first_super_sell_rsi6"
					value = "bp";
					insert(code,key,day, value, self.bsp);
				elif rsi6attr[idx][1] < SUPER_SELL:
					key = "super_sell_rsi6"
					value = "bp";
					insert(code,key,day, value, self.bsp);
				if rsi12attr[idx][1] < SUPER_SELL + 10:
					key = "super_sell_rsi12"
					value = "bp";
					insert(code,key,day, value, self.bsp);
				if rsi24attr[idx][1] < SUPER_SELL + 20:
					key = "super_sell_rsi24"
					value = "bp";
					insert(code,key,day, value, self.bsp);
				idx += 1
				
	def _Compute(self):
		for code in self.info.keys():
			rsiinfo = self.info[code];
			rsi6info = rsiinfo['Rsi6'];
			rsi6attr = rsi6info.items();
			rsi6attr = sorted(rsi6attr,key=lambda x:x[0], reverse=False);

			rsi12info = rsiinfo['Rsi12'];
			rsi12attr = rsi12info.items();
			rsi12attr = sorted(rsi12attr,key=lambda x:x[0], reverse=False);

			rsi24info = rsiinfo['Rsi24'];
			rsi24attr = rsi24info.items();
			rsi24attr = sorted(rsi24attr,key=lambda x:x[0], reverse=False);
			self._super_sell(code, rsi6attr, rsi12attr, rsi24attr);
			self._super_buy(code, rsi6attr, rsi12attr, rsi24attr);
			
	def _Rsi(self,interval, flag):
		for code in self.ticker.keys():
			cinfo = self.ticker[code];
			closeinfo = cinfo['stock']['Close'];
			closeattr = closeinfo.items();
			closeattr = sorted(closeattr,key=lambda x:x[0], reverse=False);
			closes = np.array([float(x[1]) for x in closeattr]);
			rsiattr = talib.RSI(closes,interval);
			key = flag;
			for i in range(len(rsiattr)):
				day = closeattr[i][0];
				value = rsiattr[i];
				insert(code,key,day, value,self.info);
				#print(code + "\t" + key + "\t" + day + "\t" + str(value));
