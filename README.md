# ModelaPlayer4toCandle-converter
ローランド社のCAMソフトであるモデラプレイヤー4というソフトで出力したGコードをcandle等の汎用CNC制御ソフトで扱えるようにするためのGコードコンバータです。

ドラッグアンドドロップでファイルを読み込み元のファイルと同じ場所に変換後のファイルを出力します。
exe化して実行してください。
~~~ python:powershell
pyinstaller .\ModelaPlayer4toCandle-converter.py --noupx -c --onefile
~~~

Windows 64bit用
https://github.com/zunda-mochi-256/ModelaPlayer4toCandle-converter/blob/dist/ModelaPlayer4toCandle-converter.exe
