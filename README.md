# httpscan
httpscan 用于C段http资产快速扫描，目前只支持80端口。(多线程)（写书需要，没有方便的工具就写了一个脚本，方便和书搭配）

![image](https://user-images.githubusercontent.com/27001865/150347697-4dcd401f-c664-43e1-a388-cc8055d34343.png)


```python

    $$\   $$\ $$$$$$$$\ $$$$$$$$\ $$$$$$$\   $$$$$$\
    $$ |  $$ |\__$$  __|\__$$  __|$$  __$$\ $$  __$$\
    $$ |  $$ |   $$ |      $$ |   $$ |  $$ |$$ /  \__| $$$$$$$\ $$$$$$\  $$$$$$$\
    $$$$$$$$ |   $$ |      $$ |   $$$$$$$  |\$$$$$$\  $$  _____|\____$$\ $$  __$$\
    $$  __$$ |   $$ |      $$ |   $$  ____/  \____$$\ $$ /      $$$$$$$ |$$ |  $$ |
    $$ |  $$ |   $$ |      $$ |   $$ |      $$\   $$ |$$ |     $$  __$$ |$$ |  $$ |
    $$ |  $$ |   $$ |      $$ |   $$ |      \$$$$$$  |\$$$$$$$\$$$$$$$ |$$ |  $$ |
    \__|  \__|   \__|      \__|   \__|       \______/  \_______|\_______|\__|  \__|
                                Author:Alphabug@RedTeam.site
usage: httpscan.py [-h] -t TARGET

httpscan

optional arguments:
  -h, --help            show this help message and exit
  -t TARGET, --target TARGET
                        target,For example:192.168.1.100
```

**使用效果**

![image](https://user-images.githubusercontent.com/27001865/146764329-e5e3bd9f-2080-4501-bbc0-92fa18d15388.png)
