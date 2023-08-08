@echo off

echo 【任务1】：获取STD名单

set SCRIPT_PATH_1=E:\Quick\Workflow\Software-AUTO-Weekly\Auto-SQL-Query-to-CSV.exe
set SQL_QUERY_PATH_1=E:\Quick\Workflow\Software-AUTO-Weekly\Query-Std-ALL.txt
set DB_INFO_PATH_1=E:\Quick\Workflow\Software-AUTO-Weekly\PySQL-Info.txt
set OUTPUT_PATH_1=E:\Quick\Workflow\Software-AUTO-Weekly\CSV\Output-Std-ALL.csv
set ENCODING_1=UTF-8

echo 【任务1】目前的运行配置如下：
echo 【任务1】当前调用的可执行文件路径：%SCRIPT_PATH_1%
echo 【任务1】输入查询语句的文件路径：%SQL_QUERY_PATH_1%
echo 【任务1】输入数据库配置信息的文件路径：%DB_INFO_PATH_1%
echo 【任务1】输出文件的计划存储路径：%OUTPUT_PATH_1%
echo 【任务1】输出文件的预设文件编码路径：%ENCODING_1%
echo 【任务1】接下来开始进行查询并输出结果到指定文件
echo 【任务1】可执行文件运行的LOG：【
echo.
"%SCRIPT_PATH_1%" -q "%SQL_QUERY_PATH_1%" -i "%DB_INFO_PATH_1%" -o "%OUTPUT_PATH_1%" -c %ENCODING_1%
echo 】

echo 【任务1】查询和输出文件的任务已完成！
echo 【任务1】输出文件路径：%OUTPUT_PATH_1%


echo -------------------------------------------------------------------

echo 【任务2】：获取JAVA名单

set SCRIPT_PATH_2=E:\Quick\Workflow\Software-AUTO-Weekly\Auto-SQL-Query-to-CSV.exe
set SQL_QUERY_PATH_2=E:\Quick\Workflow\Software-AUTO-Weekly\Query-JAVA-ALL.txt
set DB_INFO_PATH_2=E:\Quick\Workflow\Software-AUTO-Weekly\PySQL-Info.txt
set OUTPUT_PATH_2=E:\Quick\Workflow\Software-AUTO-Weekly\CSV\Output-JAVA-ALL.csv
set ENCODING_2=UTF-8

echo 【任务2】目前的运行配置如下：
echo 【任务2】当前调用的可执行文件路径：%SCRIPT_PATH_2%
echo 【任务2】输入查询语句的文件路径：%SQL_QUERY_PATH_2%
echo 【任务2】输入数据库配置信息的文件路径：%DB_INFO_PATH_2%
echo 【任务2】输出文件的计划存储路径：%OUTPUT_PATH_2%
echo 【任务2】输出文件的预设文件编码路径：%ENCODING_2%
echo 【任务2】接下来开始进行查询并输出结果到指定文件
echo 【任务2】可执行文件运行的LOG：【
echo.
"%SCRIPT_PATH_2%" -q "%SQL_QUERY_PATH_2%" -i "%DB_INFO_PATH_2%" -o "%OUTPUT_PATH_2%" -c %ENCODING_2%
echo 】

echo 【任务2】查询和输出文件的任务已完成！
echo 【任务2】输出文件路径：%OUTPUT_PATH_2%


echo -------------------------------------------------------------------


echo 【任务3】：切割STD名单

set SCRIPT_PATH_3=E:\Quick\Workflow\Software-AUTO-Weekly\Table_Extractor_Plus.exe
set SCRIPT_CONF_3=E:\Quick\Workflow\Software-AUTO-Weekly\Table_Extractor-Std.conf

echo 【任务3】目前的运行配置如下：
echo 【任务3】当前调用的可执行文件路径：%SCRIPT_PATH_3%
echo 【任务3】当前调用的可执行文件的配置文件路径：%SCRIPT_CONF_3%

echo 【任务3】可执行文件运行的LOG：【
echo.
"%SCRIPT_PATH_3%" -c "%SCRIPT_CONF_3%"

echo 】

echo 【任务3】切割STD名单的任务已完成！

echo -------------------------------------------------------------------



echo 【任务4】：切割JAVA名单

set SCRIPT_PATH_4=E:\Quick\Workflow\Software-AUTO-Weekly\Table_Extractor_Plus.exe
set SCRIPT_CONF_4=E:\Quick\Workflow\Software-AUTO-Weekly\Table_Extractor-JAVA.conf

echo 【任务4】目前的运行配置如下：
echo 【任务4】当前调用的可执行文件路径：%SCRIPT_PATH_4%
echo 【任务4】当前调用的可执行文件的配置文件路径：%SCRIPT_CONF_4%

echo 【任务4】可执行文件运行的LOG：【
echo.
"%SCRIPT_PATH_4%" -c "%SCRIPT_CONF_4%"

echo 】

echo 【任务4】切割JAVA名单的任务已完成！

echo -------------------------------------------------------------------

echo 【任务5】：重命名文件并加上当前日期

set TIMESTAMP=%date:~0,4%%date:~5,2%%date:~8,2%
set TIMESTAMP=%TIMESTAMP: =0%

set FILE_PATH=E:\Quick\Workflow\Software-AUTO-Weekly\CSV\
set FILE1=Output-JAVA-ALL.csv
set FILE2=Output-JAVA-S.csv
set FILE3=Output-JAVA-Other.csv
set FILE4=Output-Std-ALL.csv
set FILE5=Output-Std-S.csv
set FILE6=Output-Std-Other.csv

for %%A in ("%FILE_PATH%%FILE1%" "%FILE_PATH%%FILE2%" "%FILE_PATH%%FILE3%" "%FILE_PATH%%FILE4%" "%FILE_PATH%%FILE5%" "%FILE_PATH%%FILE6%") do (
    ren "%%~fA" "%%~nA-%TIMESTAMP%%%~xA"
)

echo 【任务5】重命名文件的任务已完成！


echo -------------------------------------------------------------------

pause
