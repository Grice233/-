# -*- Coding: UTF-8 -*-
# dao.py
# @作者 葛瑞雪
# @邮箱 1521852378@qq.com

import json
import csv

# 读取xinguan.json转换成字典
fp = open("xinguan.json", "r", encoding='utf-8')
fp_read = fp.read()
st = json.loads(fp_read)
sta = st['data']

# 从爬取的信息中提取所需信息
china = sta['caseList']
csvfile = open("newIlness.csv", 'w', encoding='utf-8', newline='')

for i in range(len(china)):
    # 写入每个省的总新增、现有、累计、治愈、死亡
    writer = csv.writer(csvfile)
    writer.writerow([china[i]['area'], '新增确诊:' + str(china[i]['confirmedRelative'])
                    , '新增无症状:' + str(china[i]['asymptomaticLocalRelative'])
                    , '现有:' + str(china[i]['curConfirm'])
                    , '累计:' + str(china[i]['confirmed'])
                    , '治愈:' + str(china[i]['crued'])
                    , '死亡:' + str(china[i]['died'])])

    for city in china[i]['subList']:
        # 写入每个市的新增、现有、累计、治愈、死亡
        writer.writerow([city['city'], '新增确诊:' + str(city['confirmedRelative'])
                        , '新增无症状:' + str(city['asymptomaticLocalRelative'])
                        , '现有:' + str(city['curConfirm'])
                        , '累计:' + str(city['confirmed'])
                        , '治愈:' + str(city['crued'])
                        , '死亡:' + str(city['died'])])
    # 每个省（或地区）之间加一行空行
    writer.writerow([])
print("保存成功！")
fp.close()
