通过我们进行一些打包的命令，来取消控制台的出现。
我们用的是conda的环境来进行打包的，所以会出现pyinstaller搜索不到相应依赖的情况，这就需要我们手动添加
```
pyinstaller --onefile --icon=app.ico --noconsole ^
    --add-binary "E:\mamba\conda\Library\bin\tcl86t.dll;." ^
    --add-binary "E:\mamba\conda\Library\bin\tk86t.dll;." ^
    Portal1.0.py
```