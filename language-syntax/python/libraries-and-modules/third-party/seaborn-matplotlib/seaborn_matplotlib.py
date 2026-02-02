import matplotlib.pyplot as plt
import seaborn



############################
### SEABORN & MATPLOTLIB ###
############################




plt.style.use('dark_background')



# DATA # 

x = [1, 2, 3, 4, 5, 6, 7, 8]
y2 = [1, 4, 9, 16, 25, 36, 49, 64]
y3 = [1, 8, 27, 64, 125, 216, 343, 512]
names = ["Fred", "Jim", "Alice", "Angela", "Tom", "Julie", "Ben", "Rachel"]
ages = [18, 23, 22, 28, 22, 19, 21, 25]



# FORMATTING #

# Different colors:
color_list = ('blue', 'green', 'red', 'cyan', 'magenta', 
             'yellow', 'black', 'brown', 'pink', 'olive',
             'cyan', 'white')




# PLOT #

# Initialise:
fig5, ax = plt.subplots(nrows=1, ncols=3, figsize=(6,3), sharey=True)
fig5.suptitle("Many subplots")    # suptitle = "super-title"; a title that appears above all subplots.

# Line plot:
ax[0].set_title("Line plot")
ax[0].plot(x, y2, linewidth=4.0)

# Bar chart:
ax[1].set_title("Bar chart")
ax[1].bar(x, y2, width=1, edgecolor="grey", linewidth=0.7)

# Vertical labels:
ax[2].set_title("Vertical labels")
ax[2].set_xticklabels(names, rotation=90)
ax[2].bar(names, ages, color='orange')




# DISPLAY #

fig5.set_tight_layout(True)
fig5.savefig('libraries+modules/fig5.jpg')

plt.show()

