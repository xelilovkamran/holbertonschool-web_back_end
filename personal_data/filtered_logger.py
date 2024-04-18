#!/usr/bin/env python3
""" program that returns a string
with certain fields redacted """

import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """ function that returns a string with certain fields redacted """
    for field in fields:
        message = re.sub(f'{field}=.*?{separator}',
                         f"{field}={redaction}{separator}", message)
    return message
