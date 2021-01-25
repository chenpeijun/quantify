import jqdatasdk 
import yfinance as yf
import pandas_datareader
import sys;
#yf.pdr_override();
#data = pandas_datareader.data.get_data_yahoo("ONVO",start="2020-12-10",group_by = 'ticker');
#data = yf.download(tickers="BABA",start="2020-12-21",group_by='ticker');
prd = "3mo";
codes = ["BABA"]
if len(sys.argv) >= 2:
	prd = sys.argv[2];
	codes = []
	for line in open(sys.argv[1]):
		codes.append(line.strip());
for code in codes:
	ticker = yf.Ticker(code);
	hist = ticker.history(period=prd);
	for attr in ["Open","Close","High","Low","Volume"]:
		for day in hist[attr].keys():
			print(code + "\tstock\t" + attr + "\t" + str(day).split(" ")[0] + "\t" + str(hist[attr][day]));	

