import os


dev_server = os.environ.get("SERVER_SOFTWARE", "").startswith("Devel")


def seconds_fmt(f, n=0):
    return milliseconds_fmt(f * 1000, n)


def milliseconds_fmt(f, n=0):
    return decimal_fmt(f, n)


def decimal_fmt(f, n=0):
    fmt = "%." + str(n) + "f"
    return fmt % f


def short_method_fmt(s):
    return s[s.rfind("/") + 1:]


def short_rpc_file_fmt(s):
    if not s:
        return ""
    return s[s.find("/"):]
