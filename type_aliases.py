from typing import TypeAlias

x = 1  # untyped global expression
x: int = 1  # typed global expression


class MyClass:
    pass


# old type alias
a: "MyClass"

# improved type alias
TypeA: TypeAlias = int  # type alias
TypeB: TypeAlias = "MyClass"  # type alias

a: TypeA = 5


def foo() -> TypeB:
    return MyClass()
