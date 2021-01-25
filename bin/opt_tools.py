from ticker  import Ticker
import sys;

code = sys.argv[2];
day = sys.argv[3];
update_time=sys.argv[4];
ticker = Ticker(sys.argv[1]);
def parse(attr, flag):
	detail,attr,option_price = attr.split("|");
	if flag == "call":
		detail = "".join(detail.split("C")[0:-1]);
	else:
		detail = "".join(detail.split("P")[0:-1]);
	code = "".join(detail[:-6]);
	day ="".join( detail[-6:]);
	return (code, "20"+day, attr, float(option_price));

	

def output_low_premium_rate(ret_arr):
	ret_arr = sorted(ret_arr, key=lambda x:x[4]);
	print("<p>");
	print("<table border=1>");
	print("<tr>");
	print("<td>code</td><td>exp_day</td><td>option_price</td><td>last_price</td><td>premium_rate</td><td>open_interest</td><td>vol</td><td>stocke_price</td><td>update_time</td>");
	for arr in ret_arr:
		print("<tr>");
		for val in arr:
			print("<td>" + str(val) + "</td>");
		print("</tr>");
	print("</tr>");
	print("</table>");
	print("</p>");


def low_premium_rate():
	ret_arr = []
	
	if code in ticker.info:
		close_info = ticker.info[code]['stock']['Close'];
		if day  in close_info:
			close_price = round(close_info[day],2);
				
			cinfo = ticker.info[code];
			if 'call' in cinfo:
				call_info = cinfo['call'];
				for call_type in call_info.keys():
					if call_type.find("lastPrice") > 0:
						(code, exp_day, attr, option_price) = parse(call_type, "call");
	
						if exp_day < update_time:
							continue;
	
	
						last_price_arr = call_info[call_type];
						open_intrest_attr = call_info[call_type.replace('lastPrice', 'openInterest')]
						volume_attr = call_info[call_type.replace('lastPrice', 'volume')]
						if option_price < close_price:
							if day in last_price_arr:
								last_price = last_price_arr[day];	
								open_interest = open_intrest_attr[day]
								volume = volume_attr[day];
								if open_interest > 1000 and volume > 50:
									premium_rate = round((option_price + last_price)/(close_price+0.001) - 1,3);
									ret_arr.append([code,exp_day, option_price, last_price, premium_rate, open_interest ,volume, close_price, update_time]);
	output_low_premium_rate(ret_arr);
def high_iv():
	ret_arr = []
	
	if code in ticker.info:
		close_info = ticker.info[code]['stock']['Close'];
		if day  in close_info:
			close_price = round(close_info[day],2);
				
			cinfo = ticker.info[code];
			if 'call' in cinfo:
				call_info = cinfo['call'];
				for call_type in call_info.keys():
					if call_type.find("lastPrice") > 0:
						(code, exp_day, attr, option_price) = parse(call_type, "call");
	
						if exp_day < update_time:
							continue;
	
	
						last_price_arr = call_info[call_type];
						open_intrest_attr = call_info[call_type.replace('lastPrice', 'openInterest')]
						volume_attr = call_info[call_type.replace('lastPrice', 'volume')]
						if option_price < close_price:
							if day in last_price_arr:
								last_price = last_price_arr[day];	
								open_interest = open_intrest_attr[day]
								volume = volume_attr[day];
								if open_interest > 1000 and volume > 50:
									premium_rate = round((option_price + last_price)/(close_price+0.001) - 1,3);
									ret_arr.append([code,exp_day, option_price, last_price, premium_rate, open_interest ,volume, close_price, update_time]);
	output_low_premium_rate(ret_arr);




if sys.argv[1] == "low_premium_rate":
	low_premium_rate()

	
	
