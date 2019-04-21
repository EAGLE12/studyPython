#文字列の処理
s1 = "abc"
print(s1*10)

s2 = "aaaaaaaaa,aaaaaaaa,ssssssssss,fffffffffff,g,h,r,e,b,ffff"
s2List = s2.split(",")
print(s2List[0])
print("置換： %s をmnに" %  s2List[0])
print(s2List[0].replace("a","mn"))

s3 = "abcdefg"
s3_sarch = "こ"
s3_flag = s3_sarch in s3

if s3_flag == True:
    print("{s3}の中に「{sarch}」が含まれている".format(s3=s3, sarch=s3_sarch))
else:
    print("{s3}の中に「{sarch}」が含まれていない".format(s3=s3, sarch=s3_sarch))
    
