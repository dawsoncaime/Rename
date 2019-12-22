# ----------------------------------------------------
# faster R-CNN data
# create the object tree for xml
# ----------------------------------------------------
from lxml import etree


def new_object(_name, _bndbox, _pose='Unspecified', _truncated='0', _difficult='0'):
    object = etree.Element('object')

    name = etree.SubElement(object, 'name')
    name.text = _name
    pose = etree.SubElement(object, 'pose')
    pose.text = _pose
    truncated = etree.SubElement(object, 'truncated')
    truncated.text = _truncated
    difficult = etree.SubElement(object, 'difficult')
    difficult.text = _difficult
    bndbox = etree.SubElement(object, 'bndbox')
    xmin = etree.SubElement(bndbox, 'xmin')
    ymin = etree.SubElement(bndbox, 'ymin')
    xmax = etree.SubElement(bndbox, 'xmax')
    ymax = etree.SubElement(bndbox, 'ymax')
    xmin.text = _bndbox["xmin"]
    ymin.text = _bndbox["ymin"]
    xmax.text = _bndbox["xmax"]
    ymax.text = _bndbox["ymax"]

    return object