from dataclasses import dataclass
from typing import Optional

from generate_common_imports import *

def generate_model():
    return '''
@dataclass
class Webhook:
    event: str
    callbackUrl: str
    description: Optional[str] = None
'''
