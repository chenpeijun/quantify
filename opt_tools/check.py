from opt import Option
import sys;
import math;
'''
price_rate=[1.5,1,3,1.1,1.0,0.9,0.8,0.7]
duration=180
current_price=29
iv=0.5
stock_price_arr = [20,23,26,29,31,35,40]
strike_price_arr = [25,26,27,29]
duration_day_arr =[150,90,1]
#stock_price_arr = [x*current_price for x in price_rate]
#option_price_arr = [current_price*(1+x/10.0) for x in range(10)] + [current_price*(1-x/10.0) for x in range(10)];
#duration_day_arr =[1,30,60,90,120,179]
'''
kind=int(sys.argv[1])
duration=170
current_price=645
iv=0.38
stock_price_arr = [500,550,600,645,700,740]
strike_price_arr = [600]
duration_day_arr =[140]

#还剩多少天时候计算收益
for duration_day in duration_day_arr:
	#股价变化都哪个位置
	for stock_price in stock_price_arr:
		#先确定期权价格
		ret_arr = []
		for strike in strike_price_arr:
			#计算成本
			opt = Option(True,kind,current_price,strike,duration,0,iv,0);
			opt.bt(500);
			option_price =  opt.btprice;
		#	print(option_price);
			chengben =  option_price;


			opt = Option(True,kind,stock_price,strike ,duration_day,0,iv,0);
			opt.bt(500);
			target_option_price =  opt.btprice;
			#print(target_option_price);
			current_val =  target_option_price;
			ret_arr.append((strike,option_price,target_option_price,current_val-chengben))
		b=sorted(ret_arr, key=lambda x:x[-1], reverse=True)
		print("-----------------------------")
		for i in range(len( b)):
			#print(str(duration_day) +"\t" + str(round(stock_price/current_price - 1,2) ) + "\t" + "\t" + "|".join([str(round(x/current_price,2)) for x in b[i]]));
			print(str(duration_day) +"\t" + str(round(stock_price,2) ) + "\t" + "\t" + "|".join([str(round(x,2)) for x in b[i]]));
