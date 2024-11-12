from enum import Enum


class SampleEnum(Enum):
    Key1 = "value1"
    Key2 = "value2"
    Key3 = "value3"


# nameからenumを取得
enum = SampleEnum["Key1"]
print(enum)

# これはKeyError
# enum = SampleEnum["KeyUndefined"]

# value名からenumを取得
enum = SampleEnum("value2")
print(enum)

# これはValueError
enum = SampleEnum("valueUndefined")
