#!/usr/bin/env python
# coding=UTF-8
# author: zhangjiaqi <1399622866@qq.com>
# File: mixins
# Date: 4/18/2019
import os
import zipfile
import filetype


# 解压缩文件到指定目录
# class Unpacker(object):
# #     """
# #     解压器，提供解压缩文件到指定目录
# #     """
# #     compression_type = ['zip', 'rar', 'gz']
# #
# #     def __init__(self, compression_file, to_store_path):
# #         self.comp_file = compression_file,
# #         if not os.path.exists(to_store_path):  # 如果解压存储目录不存在则创建
# #             os.mkdir(to_store_path)
# #         self.to_store = to_store_path
# #
# #     @property
# #     def extension(self):
# #         kind = filetype.guess(self.comp_file)
# #         if kind is None:
# #             return None
# #         return kind.extension
# #
# #     def unpack(self):
# #         file_ext = self.extension
# #         if file_ext not in self.compression_type:
# #             return False
# #         if file_ext == 'zip':
# #             zipfile_obj = zipfile.ZipFile(self.comp_file)
# #             zipfile_obj.extractall(path=self.to_store)
# #             zipfile_obj.close()
# #         elif file_ext == 'rar':
# #             pass
# #         elif file_ext == 'gz':
# #             pass


if __name__ == '__main__':
    pass
