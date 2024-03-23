@echo off

@REM 更改编码为UTF-8
chcp 65001

:: 第一条命令
echo %date% %time% >> log.txt
dir >> log.txt

:: 第二条命令
echo %date% %time% >> log.txt
ipconfig >> log.txt

:: 第三条命令
echo %date% %time% >> log.txt
echo Hello World >> log.txt

:: 结束
echo %date% %time% >> log.txt
pause