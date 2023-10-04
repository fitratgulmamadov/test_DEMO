from typing import List, Dict

def match_fields(get_fields: dict, has_fields: List[Dict]) -> set:
    return {i['name'] for i in has_fields} - set(get_fields)