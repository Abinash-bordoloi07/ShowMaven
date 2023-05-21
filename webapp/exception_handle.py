# error_handling.py
import functools
import logging

logger = logging.getLogger(__name__)

def exception_handler(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            error_code = getattr(e, "code", 500)
            logger.exception("Service exception: %s", e)
            r = {"message": str(e), "error_code": error_code}
            return r, error_code
    wrapper.__name__ = func.__name__

    return wrapper


