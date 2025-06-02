import logging

''' python logging设置utf-8编码，记录中文字符
    https://blog.csdn.net/qq_41898224/article/details/134946000
''' 

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s', \
                    handlers=[logging.FileHandler(filename=r'.\log.log',mode='w',encoding='utf-8')])
logging.debug("中文测试")