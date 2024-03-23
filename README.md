#CodeSets
##PyScripts
- mt.py→MT论坛签到（github变量版），MT论坛已封禁国外IP，已失效请改为本地版并在本地运行或国内服务器运行
- picZIP.py→图种生成器初版，仅作为记录使用，若需制作图种请使用picZIP2
- picZIP2.py→图种生成器第二版<br>
  本程序会自动识别两个文件的类型，自动区分图片和压缩包（必须一图一包）<br>
  使用说明

  - 方法一

    1.使用pyinstaller对picZIP2进行打包为单文件exe

    2.将压缩包和图片一起拖到exe文件上，完成图种制作

  - 方法二

    在已经安装了python3环境中的命令行中使用下列命令
    ```shell
    python picZip2.py [file1Path] [file2Path]
    ```
- pip3freezeBackuo.py→一键导出当前python环境所安装的包，可自定义输出文件名
