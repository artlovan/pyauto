import inspect
import sys


def core_inspector(f, args, kwargs):
    inspect_meth = inspect.getargspec(f)._asdict()['args']
    c = dict(zip(inspect_meth, args))
    merged = {}
    merged.update(kwargs)
    merged.update(c)
    return merged


def attach_screenshot_to_failed_tc(f):
    def inner(*args, **kwargs):
        merged = core_inspector(f, args, kwargs)
        r = f(*args, **kwargs)
        if merged['screenshot'] is not True: return r
        if sys.exc_info()[0]: merged['self'].allure_screenshot()
        return r
    return inner
