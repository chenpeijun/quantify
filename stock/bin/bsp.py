import sys;
import talib
from ticker import Ticker 
from tools import *;
ticker = Ticker(sys.argv[1]);
day = sys.argv[2];
ret_num_dict = load_ret_num(sys.argv[3]);
ret_arr = [];
for code in ticker.info.keys():
	bsp_arr = ticker.bsp(code,day);
	ret_arr = []
	key_ret_arr = []
	for attr in bsp_arr:
		key = attr[0];
		val = attr[1];
		okey = key;
		if key in ret_num_dict:
			okey = ret_num_dict[key];
		ret_arr.append(okey+" " + str(val));
		if is_key_role(key,val):
			key_ret_arr.append(okey+" " + str(val));
	print(code + '\t' + day + "\t" +"<br/>".join(key_ret_arr)+"\t" + "<br/>".join(ret_arr));
		
