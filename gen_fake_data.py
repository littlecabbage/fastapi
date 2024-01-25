import numpy as np 
import pandas as pd 


# 生成(500, 15)的随机数
data = np.random.rand(500, 15)

# generator alphabets from a ~ z
alphabets = np.array([chr(x) for x in range(97, 97 + 15)])
columns = [f"kw10a4-{x}" for x in alphabets]
timestamp = pd.date_range(start="2020-01-01", periods=500, freq="10s")

df = pd.DataFrame(data, columns=columns, index=timestamp)

df.to_csv("fake_data.csv", index=True)