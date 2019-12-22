# ---------------------------------------------------
# This is a function for faster R-CNN
# function: create xml file
#           create the main folder
#           rename the file
# ---------------------------------------------------
from src.create_xml import create_xml
from src.Create_main import create_main
from src.rename import reName1
from src.rename import reName2


if __name__ == '__main__':
    # SP_function
    # 'rename1' 对文件进行重命名，不判断后缀，生成指定后缀
    # 'rename2' 对一个文件夹内不同后缀文件进行重命名
    # 'creat_xml' 产生xml文件
    # 'create_main' 对训练集和测试集进行随机分配
    SP_function = 'rename1'         # 输入运行的程序

    if SP_function == 'rename1':
        # copy the source folder and rename the file in it( ps: the suffix can be changed)
        # return the last count of the file
        src = '.\\data\\pic'    # 源图像路径
        dst = '.\\output\\pic_re'  # 目标路径
        suf = '.jpg'  # 后缀
        cnt = 1  # 重命名计数起点
        cnt = reName1(src, dst, suf, cnt)

    elif SP_function == 'rename2':
        # judge the suffix and then rename the file in it (ps: the suffix can only use for judge)
        # return the last number of the different suffix file
        src = './sourcePic/data/MarkPosRes35'  # 源图像路径
        dst = './output/large'  # 目标路径
        suf1 = '.jpg'  # 后缀
        suf2 = '.txt'
        cnt1 = 1
        cnt2 = 1
        jpg_num, txt_num = reName2(src, dst, suf1, suf2, cnt1, cnt2)

    elif SP_function == 'creat_xml':
        # create the xml file
        # calib_size='is_calib_large' or 'is_calib_small'
        # circle_size='large_circle' or 'small_circle'
        src_dir = 'D:\\fasterRCNN\\data\\VOCDevkit2007\\VOC2007\\JPEGImages'  # 图片读取路径
        txt_dir = 'D:/0_project/mark_pic/CreateXml/new_pic/large/txt_re'  # 坐标位置读取位置
        dst_dir = 'D:/fasterRCNN/data/VOCDevkit2007/VOC2007/Annotations'  # xml文件存储路径
        object_name = ('point', 'point', 'point', 'point', 'point')  # 特征名字（同特征用相同名字）
        create_xml(src_dir, txt_dir, dst_dir, object_name, calib_size='is_calib_small', circle_size='small_circle')

    elif SP_function == 'create_main':
        # create the main file for random the train and test
        trainval_percent = 0.5
        train_percent = 0.5
        xmlfilepath = 'D:/fasterRCNN/data/VOCDevkit2007/VOC2007/Annotations'  # xml文件路径
        txtsavepath = 'D:/fasterRCNN/data/VOCDevkit2007/VOC2007/ImageSets/Main'  # 存储路径
        create_main(trainval_percent, train_percent, xmlfilepath, txtsavepath)
    else:
        print('！！！NO FUNCTION IMPORT')

