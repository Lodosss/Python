import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("train.csv", index_col="PassengerId")
df2 = df[["Sex","Age","Survived"]]
print(df2[:15])