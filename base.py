import base64
import hashlib

with open(r"C:\Users\admin\Documents\【应用软体项目】\Python\Dmx_GUI\DemucsICO.ico", "rb") as f:
    # 读取图片，并通过base64编码
    base64_data = base64.b64encode(f.read())
    # 将编码存在txt文件中
    file = open('base64img.txt', 'wb')
    file.write((base64_data))
    file.close()
