#!/bin/bash
day=`date -d "13 hour ago" +%Y%m%d`
year=`echo $day| awk -F"-" '{print $1;}'`
stock_conf=../conf/meigu_stock.conf
stock_info=../daily_data/meigu_stock.$day
/root/anaconda3/bin/python stock_data.py  $stock_conf 5d  | grep $day > $stock_info

option_conf=../conf/meigu_option.conf
option_info=../daily_data/meigu_option.$day
/root/anaconda3/bin/python option_data.py  $option_conf $day   > $option_info
