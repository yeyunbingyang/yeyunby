@echo off
chcp 936
dir
set javapath=\tools\JRE\bin\java.exe
echo --------------------------
echo 以下是你的Java版本信息：
echo.
echo Path=%cd%%javapath%
"%cd%%javapath%" -version
echo --------------------------
echo.
echo 正在启动ArctimePro...
"%cd%%javapath%" -Xms256m -Xmx4800m -jar bin.jar
echo.
echo --------------------------
echo 若不能启动，打开这个网页查错 https://t.arctime.cn/cw
echo 程序已结束运行，如果Arctime启动过程中出现了异常，请暂时不要关闭此窗口。
echo 如需提交调试信息，请将上方日志完整提交（不要仅提交当前看到的局部）
echo 亦可尝试关闭杀毒软件或将本软件加入白名单再试
echo --------------------------
pause