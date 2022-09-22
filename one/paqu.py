import json
import requests


def parse_txt():
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/99.0.4844.82 Safari/537.36 '
    }
    re = requests.get(url=url, headers=headers)
    # print(re.text)
    re.encoding = re.apparent_encoding
    status = re.status_code
    # 通过json库将json格式的文本转换成python中的字典类型
    data_json = json.loads(re.text)
    # 响应对象保存为json格式文件
    with open("xinguan.json", "w",
              encoding='utf-8') as f:
        f.write(json.dumps(data_json, indent=2, ensure_ascii=False))
        print("保存成功！")


if __name__ == "__main__":
    url = 'https://voice.baidu.com/api/newpneumonia'
    parse_txt()
