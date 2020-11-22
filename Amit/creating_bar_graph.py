# Creating Bar Graph

# Step 1
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# info needed, heights + x-axies
df = pd.read_csv("/Users/amitcharran/Desktop/weekend.csv")
info = df.loc[1,: ]
heights = info.drop("Buses")
heights = heights.replace(-1.00, 0.00)
bars = heights.keys()

y_pos = np.arange(len(bars))

plt.bar(y_pos, heights)
plt.xticks(y_pos, bars)

plt.title(info[0])

plt.show()



