from dataclasses import dataclass


from generate_common_imports import *

def generate_model():
    return '''
@dataclass
class Reference:
    ref: str
'''
