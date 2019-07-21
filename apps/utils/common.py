import re
import hashlib


def get_md5(url):
    if isinstance(url, str):
        url = url.encode('utf-8')
    m = hashlib.md5()
    m.update(url)
    return m.hexdigest()


def get_nums(value):
    match_re = re.match('.*?(\d+).*', value, re.S)
    if match_re:
        nums = int(match_re.group(1))
    else:
        nums = 0
    return nums


if __name__ == '__main__':
    print(get_md5('https://baidu.com'))
