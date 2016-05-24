rem 如果你的批处理a.bat放在光盘G的abc文件夹下,那么:
rem %0 为 G:\abc\a.bat
rem %~dp0 为 G:\abc\
rem %~d0 为G:
rem %~p0 为\abc\
lessc %~dp0\..\node_modules\santi\less\sb-admin-2.less %~dp0..\node_modules\santi\css\sb-admin-2.css