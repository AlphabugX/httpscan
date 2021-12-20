# -*- coding: utf-8 -*-
# @Author  : Alphabug
# @Time    : 2021/12/20 19:21
# @PRODUCT : PyCharm
# @Function: httpscan.py
# @Email   : alphabug@redteam.site
import requests,re,threading,argparse
def get_title(url):
    try:
        tmp = requests.get(url, headers={"Accept": "text/html"}, timeout=5)
        tmp.encoding = "utf-8"
        print(url+"\t"+re.findall("<title>(.*)</title>", tmp.text.lower())[0]+"\n",end="")
    except IndexError:
        print(url,tmp.content,"\n",end="")
    except requests.exceptions.ConnectionError:
        print(url+"\ttimeout\n",end="")
def go(ip):
    poll=[]
    for item in range(1,255):
        thead_one = threading.Thread(target=get_title, args=("http://"+ip+str(item),))
        poll.append(thead_one)
    for n in poll:
        n.start()
    for t in poll:
        t.join()
if __name__ == '__main__':
    print("\
    $$\   $$\ $$$$$$$$\ $$$$$$$$\ $$$$$$$\   $$$$$$\                               \n\
    $$ |  $$ |\__$$  __|\__$$  __|$$  __$$\ $$  __$$\                              \n\
    $$ |  $$ |   $$ |      $$ |   $$ |  $$ |$$ /  \__| $$$$$$$\ $$$$$$\  $$$$$$$\  \n\
    $$$$$$$$ |   $$ |      $$ |   $$$$$$$  |\$$$$$$\  $$  _____|\____$$\ $$  __$$\ \n\
    $$  __$$ |   $$ |      $$ |   $$  ____/  \____$$\ $$ /      $$$$$$$ |$$ |  $$ |\n\
    $$ |  $$ |   $$ |      $$ |   $$ |      $$\   $$ |$$ |     $$  __$$ |$$ |  $$ |\n\
    $$ |  $$ |   $$ |      $$ |   $$ |      \$$$$$$  |\$$$$$$$\\$$$$$$$ |$$ |  $$ |\n\
    \__|  \__|   \__|      \__|   \__|       \______/  \_______|\_______|\__|  \__|\n\
                            \tAuthor:Alphabug@RedTeam.site")
    alphabug = argparse.ArgumentParser(description='httpscan')
    alphabug.add_argument("-t","--target",help="target,For example:192.168.1.100",required = True)
    args = alphabug.parse_args()
    ip = args.target
    ip = str(ip).split(".")[:3]
    ip = ".".join(ip)+"."
    go(ip)
