import loggerithm
import loggerithm.handlers
import coloured
import sys
import pathlib



def test_logger_creation():
    logger = loggerithm.new()
    assert(isinstance(logger, loggerithm.Logger))
    assert(getattr(loggerithm, 'logger', None) == None)
    logger = loggerithm.new('logger')
    assert(isinstance(loggerithm.logger, loggerithm.Logger))
    assert(isinstance(logger, loggerithm.Logger))



def test_logger_methods():
    logger = loggerithm.new()
    def handler(line: str):
        assert(line == '\x1b[0m\x1b[1mTeStLoG\x1b[0m : \x1b[0m\x1b[1mmy message is fun\x1b[0m')
    logger.newtarget(handler, fmt='{method} : {message}')
    logger.newmethod('testmethod', label='TeStLoG', fmt=(coloured.Style.bold,))
    logger.LOG(logger.TESTMETHOD, 'my message is fun')
    logger.TESTMETHOD('my message is fun')



def test_logger_filehandler():
    logger = loggerithm.new()
    handler = loggerithm.handlers.FILE(pathlib.Path('./tests'), 'testlog.log')
    logger.newtarget(
        handler,
        fmt='{method} : {message}'
    )
    logger.newmethod('testmethod', label='tEsTlOg', fmt=(coloured.Reset.all,))
    logger.LOG(logger.TESTMETHOD, 'my test message in my test method')
    with open(handler.file, 'r') as f:
        assert(f.read() == 'tEsTlOg : my test message in my test method\n')



def test_logger_levels():
    logger = loggerithm.new()
    logger.setlevel(50)
    handler = loggerithm.handlers.FILE(pathlib.Path('./tests'), 'testlog.log')
    target = logger.newtarget(
        handler,
        fmt='{method} : {message}'
    )
    target.setlevel(75)
    logger.newmethod('testmethod1', label='mymethod1')
    logger.TESTMETHOD1.setlevel(25)
    logger.newmethod('testmethod2', level=50, label='mymethod2')
    logger.newmethod('testmethod3', level=75, label='mymethod3')
    logger.newmethod('testmethod4', level=100, label='mymethod4')
    logger.LOG(logger.TESTMETHOD1, 'my amazing test message1')
    logger.LOG(logger.TESTMETHOD2, 'my amazing test message2')
    logger.LOG(logger.TESTMETHOD3, 'my amazing test message3')
    logger.LOG(logger.TESTMETHOD4, 'my amazing test message4')
    with open(handler.file, 'r') as f:
        assert(f.read() == 'mymethod3 : my amazing test message3\nmymethod4 : my amazing test message4\n')