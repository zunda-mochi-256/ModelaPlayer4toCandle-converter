import re
import sys

def Conversion(file_in):
    file_out = "Conv_"+file_in
    out_data = ""

    with open(file_in, 'r') as f_in:
        while True:
            text = f_in.readline()
            if text:
                result = re.findall(r'[XYZ]-?\d+', text)
                if len(result) != 0: #x or y or zがあった
                    for val in result:
                        mozi = val[0]
                        suuti = float(val[1:])
                        suuti_str =str(suuti /1000.0)
                        text = text.replace(val,mozi+suuti_str)
                out_data = out_data+text
            else:
                break
    with open(file_out, 'w') as f_out:
        f_out.write(out_data)
        print("Write End.")
        print("File Name:"+file_out)

if __name__ == '__main__':
    args = sys.argv
    if 2 <= len(args):
        Conversion(args[1])
    else:
        print('Arguments are too short')
