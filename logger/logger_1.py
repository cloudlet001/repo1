import logging

"""
    Logger & Handler

    在開始使用 logging 之前，需要先了解三點重要但很少人全部提的概念。
    logging 模組裡的2個主要角色:

        Logger:Log 生產者，預設綁定 stdout 且 Level 為 WARNING。
        Handler:Log 接收方。

    Log 有分輕重緩急

    logging模組內建5個 Level 級別(Level 數值):

        CRITICAL(50)
        ERROR(40)
        WARNING(30)
        INFO(20)
        DEBUG(10)
        NOTSET(0)，不同 Logger 對於此 Level 的意義不同，見下一段說明

    Logger 可以分別呼叫 critical、 error、 warning、 info、 debug 方法來達到 Log 分流的應用，只有比設定級別(包含)還嚴重的 Log 會被輸出。例如設定 Level 為 ERROR 就只會輸出 ERROR 及 CRITICAL 訊息。

    Handler 也可以設定 Level 級別，同理只接收比設定級別嚴重的 Log 訊息。
"""
logging.basicConfig(level=logging.INFO)

main_logger = logging.getLogger('main')
main_logger.setLevel(logging.WARNING)

sub_logger = logging.getLogger('main.sub')

logging.debug('root debug')
main_logger.info('main info')
sub_logger.debug('sub debug')
sub_logger.info('sub info')
sub_logger.warning('sub warning')

print(logging.getLogger().getEffectiveLevel())
print(main_logger.getEffectiveLevel())
print(sub_logger.getEffectiveLevel())