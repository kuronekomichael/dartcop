#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET

import sys, os, re
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from src.dartcop import *

def test_str_line():
    actual = read_line('INFO|LINT|prefer_expression_function_bodies|/Users/tron/github/flutter/github-grass/lib/pages/home.dart|64|38|733|Use => for short mem\'bers whose body is a single return statement.')

    assert 'line' in actual
    assert 'column' in actual
    assert 'severity' in actual
    assert 'message' in actual
    assert 'source' in actual

    assert actual['line'] == '64'
    assert actual['column'] == '38'
    assert actual['severity'] == 'info'
    assert actual['message'] == 'Use => for short mem\'bers whose body is a single return statement.'
    assert actual['source'] == 'prefer_expression_function_bodies'

def test_element():
    dic = read_line('INFO|LINT|prefer_expression_function_bodies|/Users/tron/github/flutter/github-grass/lib/pages/home.dart|64|38|733|Use => for short mem\'bers whose body is a single return statement.')
    element = line2element(dic)
    assert ET.tostring(element, encoding='unicode') == '<error column="38" line="64" message="Use =&gt; for short mem\'bers whose body is a single return statement." severity="info" source="prefer_expression_function_bodies" />'

def test_output():
    with open('tests/sample.txt') as f:
        test_output = f.read()

    actualXml = output2xml(test_output)
    actual = ET.tostringlist(actualXml, encoding='unicode')

    expectedXmlRoot = ET.parse('tests/expected.xml').getroot()
    expected = ET.tostringlist(expectedXmlRoot, encoding='unicode')

    # 改行を排除
    regex = re.compile(r"^\s*$")
    expected = [line for line in expected if not regex.match(line)]

    assert len(actual) == len(expected)
    for f, b in zip(actual, expected):
        print(f,b)
        assert f == b


