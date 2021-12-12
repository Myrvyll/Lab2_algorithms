import matplotlib.pyplot as plt
import pandas as pd

array = pd.read_csv("DS9.txt", delimiter=' ',names=['x', 'y'])
graphic = plt.figure(figsize=[5.4, 9.6])
ax = graphic.add_subplot(111)
ax.set_title("Data Set 9")
ax.scatter(array.y, array.x)
plt.show()