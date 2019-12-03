import requests
import re


while(True):
    s = input()
    data = {'time': '', 'q': s, }
    response = requests.get('http://wenku.pkbff.com', params=data)
    ans = re.search(r'.*<b>答案：</b>.*</div>?', response.text).group()
    s = '答案：</b>'
    start = end = ans.find(s) + len(s)
    for j in ans[start:]:
        if j != '<':
            end += 1
        else:
            break
    print('答案：' + ans[start:end])
