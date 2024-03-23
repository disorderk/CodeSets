@echo off
echo =======本脚本适用于已安装wsl或linux shell 的window使用=======
echo 别问为什么要linux shell，问就是打算写的时候发现扩展名太多，
echo window的move一个个来太麻烦，所以改成了linux的mv。【这之前我都是自己手动输入的()】
echo 改成mv之后，发现注释是用的window注释就懒得改成shell文件了，想去做python脚本了()
@REM 创建各类文件夹
mkdir pics documents applications achieves others shells logs
@REM 移动图片至pics，↓相当于多个move *.jpg pics/↓
mv -i *.{jpg,png,avif,jpeg,gif,webp} pics/
@REM 移动文档至documents
mv -i *.{txt,docx,xlsx,pptx,doc,xls,ppt,pdf} documents/
@REM 移动应用程序到applications
mv -i *.{exe} applications/
@REM 移动压缩包至achieves
mv -i *.{zip,rar,7z,tar.*} achieves/
@REM 移动日志文件到logs
mv -i *.{log} logs/
@REM 移动shell脚本到shells（修订版去除bat，防止把自己丢了）
::@REM mv -i *.{bat,sh,ps1} shells/
mv -i *.{sh,ps1} shells/
@REM 移动当前所有文件包括上述文件夹到others，再把others下一级文件夹拿出
mv -i * others/
mv -i */* ./
@REM 运行结束，可根据个人需求选择是否结束时暂停
pause