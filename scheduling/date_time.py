from datetime import datetime

print(datetime.now())


# cron formula
# */2 * * * * /usr/bin/python3 /home/ubuntu/print_file.py >> /home/ubuntu/cron_debug.log 2>&1   