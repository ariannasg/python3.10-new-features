from typing import List, Optional, TypeGuard


def func(val: Optional[str]):
    if val is not None:  # this is a type guard
        return val
    else:
        return ""


# formalised type guard
def is_str_list(val: List[object]) -> TypeGuard[List[str]]:
    # determines if all objects in the list are strings
    return all(isinstance(x, str) for x in val)
