# -*- coding: utf-8 -*-
"""
Desc: Opencc python util module.
Author: binbin.hou
Date: 2019-4-10 13:40:20
Since: 0.0.2
"""


class StrUtil(object):

    # 空字符串
    EMPTY = ""

    @staticmethod
    def is_empty(target):
        """
        是否为空
        1. 如果为 None 或者为 ""，则返回真
        2. 其他为假
        :param target:入参
        :return:是否为空
        """
        if not target:
            return True
        if target == StrUtil.EMPTY:
            return True
        return False

    @staticmethod
    def is_not_empty(target):
        """
        是否不为空，和 is_empty 相反
        :param target:入参
        :return:是否不为空
        """
        return not StrUtil.is_empty(target)
