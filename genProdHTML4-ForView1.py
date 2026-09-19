import json

f1 = open('C:\\備蓄品放出リストのjsonファイルパス\\SinamonoListJson1.txt','r', encoding='utf-8');
json_dict = json.load(f1);

f3 = open('C:\\ユーザープロフィールのjsonファイルパス\\UserProfJson1.txt','r', encoding='utf-8');
json_dict3 = json.load(f3);


#print(json_dict["1"]["title"])

f2 = open('output1.html', 'w')

str1 = "ユーザ名:"
str1 += json_dict3["UserName"]
str1 += "<br>\n";
f2.write(str1);

str1 = "連絡先1:"
str1 += json_dict3["ContactAddress1"]
str1 += "<br>\n";
f2.write(str1);

str1 = "連絡先2:"
str1 += json_dict3["ContactAddress2"]
str1 += "<br>\n";
f2.write(str1);


str1 = "連絡先3:"
str1 += json_dict3["ContactAddress3"]
str1 += "<br>\n";
f2.write(str1);


str1 = "連絡先4:"
str1 += json_dict3["ContactAddress4"]
str1 += "<br>\n";
f2.write(str1);


str1 = "連絡先5:"
str1 += json_dict3["ContactAddress5"]
str1 += "<br>\n";
f2.write(str1);


str1 = "物品受け渡し場所:"
str1 += json_dict3["NearAddress"]
str1 += "<br>\n";
f2.write(str1);


str1 = "備考:"
str1 += json_dict3["Note"]
str1 += "<br>\n";
f2.write(str1);

str1 = "<hr>\n"
f2.write(str1);

f2.write(' <table border="1">\n');
f2.write('<tr>\n');
f2.write('<th>品名</th>\n');
f2.write('<th>個数</th>\n');
f2.write('<th>受け渡し開始日時</th>\n');
f2.write('<th>受け渡し終了日時</th>\n');
f2.write('<th>備考</th>\n');

f2.write('</tr>\n');

keyList = json_dict.keys();

for k in keyList:
	f2.write('<tr>\n');
	
	tdStr1 = json_dict[k]["name"];
	str2 = "<td>"+ tdStr1 + "</td>\n"
	f2.write(str2);
	
	tdStr1 = json_dict[k]["count"];
	str2 = "<td>"+ tdStr1 + "</td>\n"
	f2.write(str2);
	
	tdStr1 = json_dict[k]["startDate"];
	str2 = "<td>"+ tdStr1 + "</td>\n"
	f2.write(str2);	
	
	
	tdStr1 = json_dict[k]["endDate"];
	str2 = "<td>"+ tdStr1 + "</td>\n"
	f2.write(str2);
	
	
	tdStr1 = json_dict[k]["note"];
	str2 = "<td>"+ tdStr1 + "</td>\n"
	f2.write(str2);	
	
	f2.write('</tr>\n');


f2.write('</table>\n');






f2.close();
