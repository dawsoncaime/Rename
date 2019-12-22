# ---------------------------------------------------------------
# rename the file
# ---------------------------------------------------------------
import os
import shutil

"""
src：源图像路径
dst：目标路径
suf：重命名文件后缀
cnt：重命名计数起点
"""


def reName1(src, dst, suf, cnt):
    # 判断路径是否存在
    srcIsExist = os.path.exists(src)
    if not srcIsExist:
            print("rename1: src is not exist")

    dstIsExit = os.path.exists(dst)         # 创建目标目录并拷贝
    if not dstIsExit:
        shutil.copytree(src, dst)

    for img in os.listdir(dst):
        oriName = os.path.join(dst, img)
        newName = os.path.join(dst, str(cnt).zfill(6)+suf)
        os.rename(oriName, newName)
        cnt = cnt + 1
    return cnt


def reName2(src, dst, suf_in1, suf_in2, cnt1, cnt2):
    # 判断路径是否存在
    srcIsExist = os.path.exists(src)
    if not srcIsExist:
        print("rename2: src is not exist")
    dstIsExit = os.path.exists(dst)  # 创建目标目录并拷贝
    if not dstIsExit:
        shutil.copytree(src, dst)
    else:
        for src_file in os.listdir(src):
            src_dir = os.path.join(src, src_file)
            shutil.copy2(src_dir, dst)

    for file in os.listdir(dst):
        if file.endswith(suf_in1):
            oriName = os.path.join(dst, file)
            newName = os.path.join(dst, str(cnt1).zfill(6) + suf_in1)
            os.rename(oriName, newName)
            cnt1 = cnt1 + 1
        elif file.endswith(suf_in2):
            oriName = os.path.join(dst, file)
            newName = os.path.join(dst, str(cnt2).zfill(6) + suf_in2)
            os.rename(oriName, newName)
            cnt2 = cnt2 + 1
    return cnt1, cnt2



if __name__ == '__main__':
    src = 'D:\\fasterRCNN\\data\\VOCDevkit2007\\VOC2007\\JPEGImages'  # 源图像路径
    dst = 'D:\\fasterRCNN\\data\\VOCDevkit2007\\VOC2007\\JPEGImages_re'  # 目标路径
    suf = '.jpg'  # 后缀
    cnt = 1  # 重命名计数起点
    reName1(src, dst, suf, cnt)

    """src = './sourcePic/data/MarkPosRes35'  # 源图像路径
    dst = './output/large'  # 目标路径
    suf1 = '.jpg'  # 后缀
    suf2 = '.txt'
    cnt1 = 1
    cnt2 = 1
    jpg_num, txt_num = reName2(src, dst, suf1, suf2, cnt1, cnt2)"""