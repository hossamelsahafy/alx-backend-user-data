#!/usr/bin/env python3
"""
    Regex-ing
"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
        use a regex to replace occurrences of certain field values.
    """
    pattern = f"({'|'.join(fields)})=([^{separator}]*)"
    return re.sub(pattern, lambda m: F"{m.group(1)}={redaction}", message)
