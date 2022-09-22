from ast import literal_eval
long_text = """
Variopartner SICAV
529900LPCSV88817QH61
1. TARENO GLOBAL WATER SOLUTIONS FUND
LU2001709034
LU2057889995
LU2001709547
2. TARENO FIXED INCOME FUND
LU1299722972
3. TARENO GLOBAL EQUITY FUND
LU1299721909
LU1299722113
LU1299722030
4. MIV GLOBAL MEDTECH FUND
LU0329630999
LU0329630130
"""
# 将字符串去掉第一行和最后一行空行，根据回车键分割
long_text = long_text[1:-1].split('\n')
# 创建一个字典，并将第0行和第1行这两个固定变量放入
zidian = {}
zidian['name'] = long_text[0]
zidian['lei'] = long_text[1]
# 创建一个list存放下面几个字典
zidian['sub_fund'] = []
# 创建dict1作为一个累加值
dict1 = {}
# 遍历剩下的行数
for i in long_text[2::]:
    # 根据首字母是否为数字判断是title还是isin
    # 将第一个字典的title存入
    if i[0:1] == '1.':
        dict1['title'] = i[3::]
        dict1['isin'] = []
    # 不是第一个字典的话，需要将之前的字典先append进zidian['sub_fund']里
    elif (i[0] == '0') | (i[0]=='1') | (i[0]=='2') | (i[0]=='3') | (i[0]=='4') | (i[0]=='5') | (i[0]=='6') | (i[0]=='7') | (i[0]=='8') | (i[0]=='9') :
        if dict1 != {}:
            # 注意append的是字典的指针，如果直接append会导致每个字典都显示为最后一个字典
            # 需要先转化为字符串再转化为字典
            zidian['sub_fund'].append(literal_eval(str(dict1)))
        dict1['title'] = i[3::]
        dict1['isin'] = []
    else:
        dict1['isin'].append(i)
# 将最后一个字典append上
zidian['sub_fund'].append(literal_eval(str(dict1)))

print(zidian)
