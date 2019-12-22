# -------------------------------------------------
# Faster R-CNN data
# Create xml file
# -------------------------------------------------
import os
from lxml import etree
import cv2
from src.new_object import new_object
from src.cal_bndbox import cal_bndbox

"""src_dir = 'D:/fasterRCNN/data/VOCDevkit2007/VOC2007/JPEGImages'              # 图片读取路径
txt_dir = 'D:/0_project/mark_pic/CreateXml/1_Label'                 # 坐标位置读取位置
dst_dir = 'D:/fasterRCNN/data/VOCDevkit2007/VOC2007/Annotations'                     # xml文件存储路径
object_name = ('point', 'point', 'point', 'point', 'point')    # 特征名字（同特征用相同名字）"""


def create_xml(src_dir, txt_dir, dst_dir, object_name, calib_size='is_calib_small', circle_size='small_circle'):
    files = os.listdir(src_dir)
    for file in files:
        # 根
        root = etree.Element('annotation')
        # 父
        folder = etree.SubElement(root, 'folder')
        _folder = os.path.basename(src_dir)
        folder.text = _folder

        filename = etree.SubElement(root, 'filename')
        _filename = file
        filename.text = _filename

        path = etree.SubElement(root, 'path')
        # _path = os.path.join('D:\\', 'fasterRCNN', 'data', 'VOCDevkit2007', 'VOC2007', 'JPEGImages', file)
        _path = os.path.join(src_dir, file)
        path.text = _path

        source = etree.SubElement(root, 'source')
        database = etree.SubElement(source, 'database')
        _database = 'Unknown'
        database.text = _database

        size = etree.SubElement(root, 'size')
        width = etree.SubElement(size, 'width')
        height = etree.SubElement(size, 'height')
        depth = etree.SubElement(size, 'depth')
        img = cv2.imread(os.path.join(src_dir, file))
        _Height = img.shape[0]
        _Width = img.shape[1]
        _depth = img.shape[2]
        width.text = str(_Width)
        height.text = str(_Height)
        depth.text = str(1)

        segmented = etree.SubElement(root, 'segmented')
        _segmented = '0'
        segmented.text = _segmented
        # 设置标定板的大小与识别的圆的大小
        tmp_bndbox, txt_num = cal_bndbox(txt_dir, calibBType=calib_size, circle_size=circle_size)
        # tmp_bndbox, txt_num = cal_bndbox(txt_dir, calibBType='is_calib_large', circle_size='large_circle')
        # tmp_bndbox, txt_num = cal_bndbox(txt_dir, calibBType='is_calib_small', circle_size='small_circle')
        if txt_num != len(files):
            print('error: the txt number is not equal the picture number')
        if len(object_name) != len(tmp_bndbox[files.index(file)]):
            print("error: (file:%s)the feature number is not equal bbox number" % file)
        cnt_Object = 0
        for nObject in object_name:
            get_object = new_object(_name=nObject, _bndbox=tmp_bndbox[files.index(file)][cnt_Object])
            cnt_Object = cnt_Object + 1
            root.append(get_object)
        tree = etree.ElementTree(root)
        xml_name = file.split('.')[0]+'.xml'
        xml_dir = os.path.join(dst_dir, xml_name)
        tree.write(xml_dir)


if __name__ == '__main__':
    src_dir = 'D:\\fasterRCNN\\data\\VOCDevkit2007\\VOC2007\\JPEGImages'  # 图片读取路径
    txt_dir = 'D:/0_project/mark_pic/CreateXml/new_pic/large/txt_re'  # 坐标位置读取位置
    dst_dir = 'D:/fasterRCNN/data/VOCDevkit2007/VOC2007/Annotations'  # xml文件存储路径
    object_name = ('point', 'point', 'point', 'point', 'point')  # 特征名字（同特征用相同名字）
    create_xml(src_dir, txt_dir, dst_dir, object_name, calib_size='is_calib_small', circle_size='small_circle')
