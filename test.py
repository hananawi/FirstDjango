# *-* coding:utf-8 *-*

import requests
import re

header = {
    'Host': 'http://wenku.pkbff.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/78.0.3904.97 Safari/537.36',
}


def output_ans(q_list):
    for q in q_list:
        if not q: continue
        if len(q)>15: q = q[:15]
        data = {'time': '', 'q': q, }
        response = requests.get('http://wenku.pkbff.com', params=data)
        ans = re.search(r'.*<b>答案：</b>.*</div>?', response.text)
        if ans:
            ans = ans.group()
            s = '答案：</b>'
            start = end = ans.find(s) + len(s)
            for j in ans[start:]:
                if j != '/':
                    end += 1
                else:
                    break
            print(q+'--  答案：' + ans[start:end-1])
        else: print(q+'--  No answer')


def solve():
    s = ''
    for line in iter(input, '~'):
        s += line+'\n'
    tmp = re.findall(r'(<span style=".*?font-family:\s*?宋体.*?>.*?</span>|'
                     r'<p[\w\s\-="]*?>.+?</p>)', s, re.S)
    q_list = []
    for i in tmp:
        q_list.append(re.search(r'>.*</', i).group(0)[1:-2])
    for i in range(len(q_list)):
        q_list[i] = check(q_list[i])
    output_ans(q_list)


def check(s):
    # u4e00-u9fa5
    ret = ''
    for i in s:
        if '\u4e00' <= i <= '\u9fa5' or i == '(' or i == ')' or i == '（' or i == '）' or i.isnumeric():
            ret += i
    if ret[:2] == '宋体': ret = ret[2:]
    if ret[:2] == '宋体': ret = ret[2:]
    if ret[:2] == '宋体': ret = ret[2:]
    if ret.startswith('p'): ret = ret[1:]
    if ret[:2] == '()': ret = ret[2:]
    if ret[:2] == '()': ret = ret[2:]
    if ret[:6] == '000000': ret = ret[6:]
    if len(ret) >= 3: return ret


if __name__ == '__main__':
    solve()
