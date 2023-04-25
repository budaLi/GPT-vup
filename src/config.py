"""
 @Author: jiran
 @Email: jiran214@qq.com
 @FileName: config.py
 @DateTime: 2023/4/7 14:30
 @SoftWare: PyCharm
"""
import configparser

file_path = './config.ini'

_config = configparser.RawConfigParser()
_config.read(file_path)

tss_settings = dict(_config.items('edge-tss'))

api_key = _config.get('openai', 'api_key')
room_id = _config.getint('room', 'id')
debug = _config.getboolean('other', 'debug')
proxy = _config.get('other', 'proxy')

if __name__ == '__main__':
    print(api_key, proxy)