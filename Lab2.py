from matplotlib import colors
import matplotlib.pyplot as plt
import pandas as pd

array = pd.read_csv("DS9.txt", delimiter=' ',names=['x', 'y'])
graphic = plt.figure(figsize=[5.4, 9.6])
ax = graphic.add_subplot(111)
ax.set_title("Data Set 9")
ax.set_ylabel("Second column")
ax.set_xlabel("First column")
ax.scatter(array.y, array.x, c=["#DD9787"])
plt.show()