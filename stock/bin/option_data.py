import jqdatasdk 
import yfinance as yf
import pandas_datareader
import sys;
#yf.pdr_override();
#data = pandas_datareader.data.get_data_yahoo("ONVO",start="2020-12-10",group_by = 'ticker');
#data = yf.download(tickers="BABA",start="2020-12-21",group_by='ticker');
opt_attr =  ['lastPrice', 'bid', 'ask','change', 'percentChange', 'volume', 'openInterest','impliedVolatility'];
day = "TESt";
codes = ["BABA"]
if len(sys.argv) >= 2:
	day = sys.argv[2] 
	codes = []
	for line in open(sys.argv[1]):
		codes.append(line.strip());
for code in codes:
	ticker = yf.Ticker(code);
	options = ticker.options;
	for exp_day in options[0:]:
		opt = ticker.option_chain(exp_day);
		calls  = opt.calls;
		symbol_arr = calls['contractSymbol'];
		strike_arr = calls['strike'];
		for i in range(len(symbol_arr)):
			symbol = symbol_arr[i];
			strike = strike_arr[i];
			for attr in opt_attr:
				key = symbol + "|" + attr + "|" + str(strike);
				print(code + "\t" + "call" + "\t" +  key + "\t" + day + "\t" + str(calls[attr][i]));

	
		puts  = opt.puts;
		symbol_arr = puts['contractSymbol'];
		strike_arr = puts['strike'];
		for i in range(len(symbol_arr)):
			symbol = symbol_arr[i];
			strike = strike_arr[i];
			for attr in opt_attr:
				key = symbol + "|" + attr + "|" + str(strike);
				print(code + "\t" + "put" + "\t" +  key + "\t" + day + "\t" + str(puts[attr][i]));


