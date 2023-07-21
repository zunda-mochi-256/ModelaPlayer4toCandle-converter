# Build :  pyinstaller .\ModelaPlayer4toCandle-converter.py --noupx -c --onefile
# G01 not del

import re
import sys
import os

def Conversion(file_in):
    directory = os.path.dirname(file_in)
    directory += "\\"
    filename = os.path.basename(file_in)
    file_out = directory+"Conv_"+filename
    print("Import File :",file_in)
    print("Export File :",file_out)
    out_data = ""

    with open(file_in, 'r') as f_in:
        start = 0
        while True:
            text = f_in.readline()
            if text:
                result = re.findall(r'^Z1000$', text) #RapidSpeedSupport 
                if len(result) != 0: #Z1000の上にF1000を追加
                    text = text.replace(result[0],'F1000\n'+result[0])
                    print(text)
                result = re.findall(r'[XYZ]-?\d+', text)
                if len(result) != 0: #x or y or zがあった
                    for val in result:
                        mozi = val[0]
                        suuti = float(val[1:])
                        if mozi == 'Z' and suuti == 155: #数値の例外処理
                            suuti_str = str(10.0)
                        else:
                            suuti_str =str(suuti /1000.0)
                        text = text.replace(val,mozi+suuti_str)
                result = re.findall(r'F5100\.?\d+', text)
                if len(result) != 0: #F5100があった
                    text = text.replace(result[0],'') #行を抹消
                if re.search(r'G28', text): #G28があった
                    text = text.replace(text,'') #行を抹消
                if re.search(r'%', text) and start != 0: #Z10G91G30を付加
                    text = text.replace(text,'Z10\nG91G30\n%')
                elif re.search(r'%', text) and start == 0: #最初の%を削除
                    text = text.replace(text,'') #行を抹消
                    start = 1

                #################################################
                if re.match(r"\n", text): #改行文字のみの行を検索
                    # print("空白行除去")
                    print()
                else:
                    out_data = out_data+text
                #################################################
            else:
                break
    with open(file_out, 'w') as f_out:
        f_out.write(out_data)
        print("Write End.")

if __name__ == '__main__':
    args = sys.argv
    if 2 <= len(args):
        args[1] = args[1].replace('"','')
        Conversion(args[1])
    else:
        print('Arguments are too short')
    os.system('PAUSE')
