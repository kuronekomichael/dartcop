#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
from dartcop import line2element

def test_sample():
    with open('test/sample.txt') as f:
        for line in f:
            print(line)

    

    root = ET.Element('checkstyle')
    b = ET.SubElement(root, 'file')
    c = ET.SubElement(root, 'c')
    d = ET.SubElement(c, 'd')
    actual = ET.tostring(root, encoding='utf-8')

    expectedXmlRoot = ET.parse('test/expected.xml').getroot()
    expected = ET.tostring(expectedXmlRoot, encoding='utf-8')

    assert actual == expected

