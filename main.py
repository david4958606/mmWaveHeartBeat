import re
import sys
 
sys.stdout = open('output.txt','wt')
mw_offset = 24
space_offset = 6
dw_offset = 12
eof_offset = 3

serial = open(file="TrialSun.txt", mode="rb+")

def findMw(file):
    text = str(file.read(), "utf-8")
    result = re.search("01 02 03 04 05 06 07 08", text).span()
    return result

def readFirst(file):
    offset = findMw(file)
    start = offset[0]
    codec = "utf-8"
    file.seek(start, 0) # move pointer to the start
    print(str(file.read(mw_offset), codec)) # print mw
    space = str(file.read(space_offset), codec)
    print(space) # 01 28
    frame_num = str(file.read(dw_offset), codec)
    print("帧号：" + frame_num)
    # print("心率置信度：" + str(file.read(dw_offset), codec))
    # print("呼吸置信度：" + str(file.read(dw_offset), codec))
    # print("心率IIR滤波输出：" + str(file.read(dw_offset), codec))
    # print("呼吸率IIR滤波输出：" + str(file.read(dw_offset), codec))
    # print("RANGE BIN maxVal：" + str(file.read(dw_offset), codec))
    # print("sumEnergyHeartWfm：" + str(file.read(dw_offset), codec))
    # print("sumEnergyBreathWfm：" + str(file.read(dw_offset), codec))
    for i in range(0, 7):
        file.read(dw_offset)
    xl = str(file.read(dw_offset), codec)
    xl = xl.split(" ")
    print("心率：{}".format(int(xl[0], 16)))
    hx = str(file.read(dw_offset), codec)
    hx = hx.split(" ")[0]
    print("呼吸：{}".format(int(hx, 16)))
    eof = file.read(3)
    print("End")


def readFile(file):
    codec = "utf-8"
    file.read(mw_offset)
    file.read(space_offset)
    # print(str(file.read(mw_offset), codec)) # print mw
    # space = str(file.read(space_offset), codec)
    # print(space) # 01 28
    frame_num = str(file.read(dw_offset), codec)
    print("帧号：" + frame_num)
    # print("心率置信度：" + str(file.read(dw_offset), codec))
    # print("呼吸置信度：" + str(file.read(dw_offset), codec))
    # print("心率IIR滤波输出：" + str(file.read(dw_offset), codec))
    # print("呼吸率IIR滤波输出：" + str(file.read(dw_offset), codec))
    # print("RANGE BIN maxVal：" + str(file.read(dw_offset), codec))
    # print("sumEnergyHeartWfm：" + str(file.read(dw_offset), codec))
    # print("sumEnergyBreathWfm：" + str(file.read(dw_offset), codec))
    for i in range(0,7):
        file.read(dw_offset)
    xl = str(file.read(dw_offset), codec)
    xl = xl.split(" ")
    print("心率：{}".format(int(xl[0], 16)))
    hx = str(file.read(dw_offset), codec)
    hx = hx.split(" ")[0]
    print("呼吸：{}".format(int(hx, 16)))
    eof = file.read(3)
    print("End")


# offset = 0
# print(serial.read(mw_offset)) # print mw
# offset += mw_offset
# serial.seek(offset)
# space = serial.read(space_offset)
# space = str(space, "utf-8")
# print(space) # 01 28

readFirst(serial)
for i in range(0, 1100):
    readFile(serial)
