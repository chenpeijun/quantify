#!/bin/bash
day=`date -d "13 hour ago" +%Y-%m-%d`
current=`date   +"%Y%m%d%H%M%S"`
stock_conf=../conf/meigu_stock.conf
stock_info=../data/meigu_stock.$day
/root/anaconda3/bin/python stock_data.py  $stock_conf 5d  > $stock_info

option_conf=../conf/meigu_option.conf
option_info=../data/meigu_option.$day
/root/anaconda3/bin/python option_data.py  $option_conf $day   >> $stock_info

PYTHON=/root/anaconda3/bin/python

codes=`cat $option_conf`
for code in $codes
do
	$PYTHON opt_tools.py $stock_info $code $day $current > ../http_data/opt/${code}_opt.html
done

