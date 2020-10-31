"""
Всякая вспомогательная всячина
"""
import re


def lower2(value: str) -> str:
    """
    >>> lower2('window')
    'Window'
    >>> lower2('window_text')
    'WindowText'
    """
    return re.sub(r'_(\w)', lambda x: x.group(1).upper(), value.capitalize())
