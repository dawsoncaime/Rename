# ---------------------------------------------------
# faster R-CNN data
# calculation the bndbox
#       #calibBType = 'is_calib_small'||'is_calib_large'
#       #circle_size = 'large_circle' ||'small_circle'
# import cal_bndbox
# ----------------------------------------------------
import os


def cal_point(x, y, delta_x, delta_y):
    x_min = str(int(x-1 - delta_x / 2))
    y_min = str(int(y-1 - delta_y / 2))
    x_max = str(int(x+1 + delta_x / 2))
    y_max = str(int(y+1 + delta_y / 2))
    _bnd = {
        'xmin': x_min,
        'ymin': y_min,
        'xmax': x_max,
        'ymax': y_max
    }
    return _bnd


def cal_bndbox(src, calibBType='is_calib_small', circle_size='large_circle'):
    files = os.listdir(src)
    bbox = []
    for file in files:
        bndbox = []
        point = []
        file_path = os.path.join(src, file)
        ctnt = open(file_path)
        line_cnt = ctnt.readline()
        line_cnt = line_cnt[:-1]                    # 按行读文件，并去掉‘\n’
        if int(line_cnt) != 5:
            print('error(in %s): the point number is not equal 5' % file)
        for i in range(int(line_cnt)):
            line = ctnt.readline()
            line = line[:-1]
            _point = line.split(',')
            point.append(_point)
        point1 = {'x': point[0][0], 'y': point[0][1]}
        point2 = {'x': point[1][0], 'y': point[1][1]}
        point3 = {'x': point[2][0], 'y': point[2][1]}
        point4 = {'x': point[3][0], 'y': point[3][1]}
        point5 = {'x': point[4][0], 'y': point[4][1]}

        if calibBType == 'is_calib_small':                      # 小标定板内外圆直径为4mm,12mm
            if circle_size == 'large_circle':
                dia = 12
            elif circle_size == 'small_circle':
                dia = 4
            delta1_x = abs(dia * (float(point2["x"]) - float(point1["x"])) / 100)
            delta2_x = abs(dia * (float(point3["x"]) - float(point5["x"])) / 100)
            delta1_y = abs(dia * (float(point5["y"]) - float(point1["y"])) / 100)
            delta2_y = abs(dia * (float(point3["y"]) - float(point2["y"])) / 100)
        elif calibBType == 'is_calib_large':                    # 大标定板内外圆直径为10mm,18mm，30mm
            if circle_size == 'large_circle':
                dia = 30
            elif circle_size == 'small_circle':
                dia = 10
            delta1_x = abs(dia * (float(point2["x"]) - float(point1["x"])) / 140)
            delta2_x = abs(dia * (float(point3["x"]) - float(point5["x"])) / 140)
            delta1_y = abs(dia * (float(point5["y"]) - float(point1["y"])) / 220)
            delta2_y = abs(dia * (float(point3["y"]) - float(point2["y"])) / 220)

        point1_bndbox = cal_point(float(point1["x"]), float(point1["y"]), (delta1_x+delta1_y)/2, (delta1_x+delta1_y)/2)
        point2_bndbox = cal_point(float(point2["x"]), float(point2["y"]), (delta1_x+delta2_y)/2, (delta1_x+delta2_y)/2)
        point3_bndbox = cal_point(float(point3["x"]), float(point3["y"]), (delta2_x+delta2_y)/2, (delta2_x+delta2_y)/2)
        point4_bndbox = cal_point(float(point4["x"]), float(point4["y"]), (delta2_x+delta2_y)/2, (delta2_x+delta2_y)/2)
        point5_bndbox = cal_point(float(point5["x"]), float(point5["y"]), (delta2_x+delta1_y)/2, (delta2_x+delta1_y)/2)
        bndbox = [point1_bndbox, point2_bndbox, point3_bndbox, point4_bndbox, point5_bndbox]
        bbox.append(bndbox)
        ctnt.close()
    file_num = len(files)
    return bbox, file_num


# 调试程序
if __name__ == '__main__':
    src = 'D:/0_project/mark_pic/CreateXml/1_Label'
    bbox, file_num = cal_bndbox(src)
    print(len(bbox))
    print(bbox[1][0])
    print(file_num)
