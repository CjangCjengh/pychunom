import os
import opencc


__all__ = ['convert']

_thisdir = os.path.dirname(os.path.abspath(__file__))
converter = opencc.OpenCC(os.path.join(_thisdir, 'dict/chunom.json'))

def convert(text: str) -> str:
    return converter.convert(text.lower().replace(' ','-')).replace('-','')
