import sys;
import talib
from price import Price
from rsi import Rsi;
class Ticker:
	def __init__(self, path):
		self.info = {}
		self._load(path);
		self._price = Price(self.info);
		self._rsi = Rsi(self.info);

	def bsp(self, code, day):
		ret_arr = []

		for bsp_info in [self._price,self._rsi]:
			if code in bsp_info.bsp.keys():
				for key in bsp_info.bsp[code].keys():
					if day in  bsp_info.bsp[code][key]:
						ret_arr.append([key, bsp_info.bsp[code][key][day]]);
		return ret_arr;
	def _load(self, path):
		infile = open(path,"r");
		if infile:
			while 1:
				line = infile.readline();
				if not line:
					break;
				contents = line.strip().split("\t");
				if len(contents) != 5:
					continue;
				code = contents[0];
				mtype = contents[1];
				attr = contents[2];
				day = contents[3];
				val = contents[4];
				if code not in self.info:
					self.info[code] = {}
				if mtype not in self.info[code]:
					self.info[code][mtype] = {}
				if attr not in self.info[code][mtype]:
					self.info[code][mtype][attr] = {}
				if day not in self.info[code][mtype]:
					self.info[code][mtype][attr][day] = {}
				self.info[code][mtype][attr][day] = float(val);

'''
ticker = Ticker(sys.argv[1]);
day = sys.argv[2];
for code in ticker.info.keys():
	bsp_arr = ticker.bsp(code,day);
	for attr in bsp_arr:
		print(code + "\t" + attr[0] + "\t" + str(attr[1]));
'''
