import re

file_in = "file.nc"
file_out = "Conv_"+file_in
out_data = ""

with open(file_in, 'r') as f_in:
    while True:
        text = f_in.readline()
        if text:
            result = re.findall(r'[XYZ]-?\d+', text)
            if len(result) != 0: #x or y or z
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