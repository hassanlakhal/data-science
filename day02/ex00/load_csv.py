import pandas as pd
from pandas import DataFrame

def load(path: str) -> DataFrame:
    df = pd.DataFrame(
        {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
    }
    )
    return df

print(load("test"), type(load("test")))