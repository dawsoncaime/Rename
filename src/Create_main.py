# ----------------------------------------------
# random the train and the test val
# ---------------------------------------------
import os
import random


def create_main(trainval_percent, train_percent, xmlfilepath, txtsavepath):
    total_xml = os.listdir(xmlfilepath)
    num = len(total_xml)
    list = range(num)
    tv = int(num * trainval_percent)
    tr = int(tv * train_percent)
    trainval = random.sample(list, tv)
    train = random.sample(trainval, tr)
    ftrainval = open(txtsavepath + '/trainval.txt', 'w')
    ftest = open(txtsavepath + '/test.txt', 'w')
    ftrain = open(txtsavepath + '/train.txt', 'w')
    fval = open(txtsavepath + '/val.txt', 'w')
    for i in list:
        name = total_xml[i][:-4] + '\n'
        if i in trainval:
            ftrainval.write(name)
            if i in train:
                ftrain.write(name)
            else:
                fval.write(name)
        else:
            ftest.write(name)
    ftrainval.close()
    ftrain.close()
    fval.close()
    ftest.close()


if __name__ == '__main__':
    trainval_percent = 0.5
    train_percent = 0.5
    xmlfilepath = 'D:/fasterRCNN/data/VOCDevkit2007/VOC2007/Annotations'                # xml文件路径
    txtsavepath = 'D:/fasterRCNN/data/VOCDevkit2007/VOC2007/ImageSets/Main'             # 存储路径
    create_main(trainval_percent, train_percent, xmlfilepath, txtsavepath)