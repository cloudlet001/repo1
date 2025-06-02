import logging

''' From chatGPT: logger write to hanlder but not stdout

    To make the logger write only to the file handler (and not to stdout), you should:
        1. Remove the default handler set up by logging.basicConfig().
        2. Set the logger's level and add only your FileHandler.
    This ensures logs go only to log.txt and not to the console.
'''

# Remove all handlers associated with the root logger
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

# Create a log file handler
file_handler = logging.FileHandler('log_not_to_stderr.txt')
file_handler.setLevel(logging.INFO)

# Optional: set a formatter for better log output
formatter = logging.Formatter('%(filename)s:%(levelname)s:%(name)s:%(message)s')
file_handler.setFormatter(formatter)

# Get the root logger and bind the handler
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(file_handler)

# Now this will only write to log.txt, not stdout
logger.info('(log to handler only, not to stderr) Hi!')