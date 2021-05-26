## 简介
QQ音乐文件、网易云音乐文件转换成mp3文件

支持类型：
    QQ音乐：.qmc3/.qmc0/.qmcflac
    网易云：.ncm

## 系统要求
* Python > 3.7
* pip3 install pycryptodome
* crypto 模块安装 https://www.jianshu.com/p/6827ffc56e66

## 执行方式
```bash
python music_converter.py music_dir 
```

## 参考项目
```bash
qmc->flac: https://github.com/Presburger/qmc-decoder
flac->mp3: https://github.com/robinbowes/flac2mp3
qmcflac2mp3->https://github.com/alexknight/qmcflac2mp3
```

#TODO
* Support Multi-threads