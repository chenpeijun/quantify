#!/bin/bash
day=`date -d "13 hour ago" +%Y-%m-%d`
year=`echo $day| awk -F"-" '{print $1;}'`
stock_conf=../conf/meigu_stock.conf
stock_info=../data/meigu_stock.$day
/root/anaconda3/bin/python stock_data.py  $stock_conf 3mo  > $stock_info

option_conf=../conf/meigu_option.conf
option_info=../data/meigu_option.$day
/root/anaconda3/bin/python option_data.py  $option_conf $day   >> $stock_info


result=../result/bsp/$day

/root/anaconda3/bin/python  bsp.py $stock_info  2021-01-22 ../conf/ret_num.conf > $result


html_file=$result.html
ablename1="股票的一些关键特征"
cat ../conf/des.conf > ${html_file}

echo "<p>" >> ${html_file}
echo "<li>$tablename</li>" >> ${html_file}
echo "</p>" >> ${html_file}
echo "<p>" >> ${html_file}
echo "<table border=1>" >> ${html_file}
echo "<tr>" >> ${html_file}
echo "<td>股票</td>" >> ${html_file}
echo "<td>时间</td>" >> ${html_file}
echo "<td>关键</td>" >> ${html_file}
echo "<td>全部</td>" >> ${html_file}
echo "</tr>" >> ${html_file}
cat $result | awk -F"\t"  '{ printf"<tr>"; for(i=1;i<=NF;i++) printf"<td>%s</td>",$i; printf"</tr>\n"}' >> ${html_file}
echo "</table>" >> ${html_file}
echo "</p>" >> ${html_file}


/usr/bin/mailx -s "$(echo -e "Test\nContent-Type: text/html; charset=utf-8")" hxxiaopei@gmail.com < $html_file
