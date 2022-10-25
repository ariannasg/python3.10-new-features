from typing import Union


def square(number: Union[int, float]) -> Union[int, float]:
    return number ** 2


# change in the union type annotation
def square_2(number: int | float) -> int | float:
    return number ** 2
