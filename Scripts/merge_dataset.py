import pandas
from pathlib import Path
seed = "CORN"
path = "Data Set"

docs = list(Path(path).glob("*CORN.csv"))
print(docs)


datasets_dic = {}