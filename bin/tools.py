import sys;
import math;

def insert(code,key,day,value, dtype):
	if code not in dtype.keys():
		dtype[code] = {}
	if key  not in dtype[code].keys():
		dtype[code][key]  = {}
	dtype[code][key][day] = value;

def load_ret_num(ret_num_file):
	ret_num_dict = {}
	ifile = open(ret_num_file, "r");
	if not ifile:
		return ret_num_dict;
	while 1:
		line = ifile.readline();
		if not line:
			break;
		contents = line.strip().split("\t");
		if len(contents) != 2:
			continue;
		ret_num_dict[contents[0]] = contents[1];
	return ret_num_dict;


def is_key_role(key, val):
	if key == 'chg_of_latest_highest_price':
		if abs(val) < 0.05:
			return True;
	if key == 'chg_of_max_highest_price':
		if abs(val) < 0.05:
			return True;
	if key == 'chg_of_latest_lowest_price':
		if abs(val) < 0.05:
			return True;
	if key == 'chg_of_min_lowest_price':
		if abs(val) < 0.05:
			return True;
	if key == 'frist_super_buy_rsi6':
			return True;
	if key == 'frist_super_sell_rsi6':
			return True;
	if key == 'ssuper_buy_rsi6':
			return True;
	if key == 'ssuper_sell_rsi6':
			return True;
