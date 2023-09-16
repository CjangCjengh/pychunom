import opencc


__all__ = ['convert']

converter = opencc.OpenCC('dict/chunom.json')

def convert(text: str) -> str:
    return converter.convert(text.lower().replace(' ','-')).replace('-','')
