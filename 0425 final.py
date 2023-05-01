import os
import matplotlib.pyplot as plt


# get file list
def get_files(in_path):
    fileList = os.listdir(in_path)
    return [name[:-4] for name in fileList]


# identify the units
def unit_trans(str):
    if str == ' V':
        return 1
    if str == 'mV':
        return 10 ** (-3)
    if str == 'uV':
        return 10 ** (-6)
    if str == ' A':
        return 1
    if str == 'mA':
        return 10 ** (-3)
    if str == 'uA':
        return 10 ** (-6)
    if str == 'nA':
        return 10 ** (-9)
    else:
        return 0


# plot from data stored in .txt
def draw(fileName, in_path, out_path):
    txt = open(in_path + '/' + fileName + '.TXT', "r", encoding='utf-8')
    data = txt.readlines()
#    csv = open(in_path + '/' + fileName + '.csv', "r", encoding='utf-8')
#    data = csv.readlines()

    x = []
    y = []

    for lines in data:
        if lines[0].isdigit():
            tmp = lines.split("\"")
            v = tmp[1]
            i = tmp[3]
            v_num = float(tmp[1][:-2])
            i_num = float(tmp[3][:-2])
            v_unit = tmp[1][-2:]
            i_unit = tmp[3][-2:]
            if not (unit_trans(v_unit) * unit_trans(i_unit)):
                print("Unit Error: unknown unit detected in", fileName)
                print(v_unit, i_unit)
            v_1 = v_num * unit_trans(v_unit)
            i_1 = i_num * unit_trans(i_unit)
            x.append(v_1)
            y.append(i_1)

    line3 = data[2].split("\"")
    axis1 = line3[3]  # name of axis1
    axis2 = line3[5]  # name of axis2
    line4 = data[3].split("\"")
    unit1 = line4[3]
    unit2 = line4[5]
    plt.scatter(x, y, s=2)
    plt.xlabel(axis1 + '/' + unit1)
    plt.ylabel(axis2 + '/' + unit2)
    plt.title(fileName)
    fig_name = out_path + '/' + fileName + '.jpg'
    plt.savefig(fig_name, dpi=300)
    plt.clf()   # annotate this if want fig to overlay


# package the whole function
def auto(in_path, out_path):
    fileList = get_files(in_path)
    for fileName in fileList:
        draw(fileName, in_path, out_path)


auto('in_data/IV Data', 'out_figure/IV data')
