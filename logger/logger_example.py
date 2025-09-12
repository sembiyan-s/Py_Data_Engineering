# A logger is a tool used to record messages from your program while it runs, which can help you debug, monitor, and maintain your code more effectively.
#  It's part of the built-in logging module in Python.
# Level | Purpose
# DEBUG     Detailed information (for dev only)
# INFO |   General info (app started, etc.)
# WARNING | Something might go wrong
# ERROR | Something went wrong
# CRITICAL | Serious error (app may crash)


#  Limitations of Using print()
    # You can't set levels (e.g., info vs error)
    # You can't redirect easily to a file
    # You can't filter messages (like show only errors)
    # No timestamps unless you manually add them
    # No format control

import logging
# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='app.log', # You can remove this line to log to console
    filemode='w',
)


def divide(a, b):
    logging.info(f"Dividing {a} by {b}")
    try:
        result = a/b
        logging.debug(f"Result: {result}")
        return result
    except ZeroDivisionError:
        logging.error("Tried to divide by zero!")
        return None
    
# Test 
divide(10,2)
divide(10,0)