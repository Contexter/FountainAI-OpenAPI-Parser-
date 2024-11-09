from dataclasses import dataclass
from typing import Optional
from typing import Dict

from generate_common_imports import *

def generate_model():
    return '''
@dataclass
class Link:
    operationId: Optional[str] = None
    parameters: Optional[Dict[str, str]] = None
    requestBody: Optional[str] = None
    description: Optional[str] = None
    server: Optional['Server'] = None
'''
