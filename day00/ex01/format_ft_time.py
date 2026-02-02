import datetime

now = datetime.datetime.now()
print(f"Seconds since January 1, 1970: {now.timestamp()} " " or {:e} in scientific notation".format(now.timestamp()) )
print(now.strftime("%b %d %Y"))