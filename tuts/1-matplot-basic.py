# * set the pycharm run configuration's Run In Console to True
# * use `C-Enter` to run the block of code
# * or just Run File

import juyi

juyi.clear_vars()

# %% import
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(666)
np.random.seed(19680801)  # seed the random number generator.

# %% basic
figure, axises = plt.subplots()  # Create a figure containing a single axes.
axises.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the axes.

# show in pycharm SciView
# only needed in pycharm!
plt.show()

# %% subplots 2x2
figure, array_axis = plt.subplots(2, 2)
figure.show()

# %% basic 2
data = {'a': np.arange(50),
        'c': rng.integers(0, 50, 50),
        'd': rng.normal(0, 1, 50)}
data['b'] = data['a'] + 10 * rng.normal(0, 1, 50)
data['d'] = np.abs(data['d']) * 100

fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')

ax.scatter('a', 'b', c='c', s='d', data=data)
ax.set_xlabel('entry a')
ax.set_ylabel('entry b')

fig.show()

# %% coding style:OO (recommended)
x = np.linspace(0, 2, 100)  # Sample data.

# Note that even in the OO-style, we use `.pyplot.figure` to create the Figure.
fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')

ax.plot(x, x, label='linear')  # Plot some data on the axes.
ax.plot(x, x ** 2, label='quadratic')  # Plot more data on the axes...
ax.plot(x, x ** 3, label='cubic')  # ... and some more.
ax.set_xlabel('X')  # Add an x-label to the axes.
ax.set_ylabel('Y')  # Add a y-label to the axes.
ax.set_title("Simple Plot")  # Add a title to the axes.
ax.legend()  # Add a legend.
fig.show()

# %% coding style:PyPlot
x = np.linspace(0, 2, 100)  # Sample data.

plt.figure(layout='constrained')
plt.plot(x, x, label='linear')  # Plot some data on the (implicit) axes.
plt.plot(x, x ** 2, label='quadratic')  # etc.
plt.plot(x, x ** 3, 'ro--', ms=4, markevery=8, linewidth=1, label='cubic')
plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Simple Plot")
plt.legend()
plt.show()

# %% styling
data1, data2, data3, data4 = rng.normal(0, 1, (4, 100))
fig, ax = plt.subplots()
x = np.arange(len(data1))
ax.plot(x, np.cumsum(data1), color='blue', linewidth=3, linestyle='--')
l, = ax.plot(x, np.cumsum(data2), color='orange', linewidth=2)
l.set_linestyle(':')
fig.show()

# %% scatter
fig, ax = plt.subplots(figsize=(5, 2.7))
ax.scatter(data1, data2, s=np.abs(data3) * 50, facecolor='C0', edgecolor='k')
fig.show()

# %% label & text
mu, sigma = 115, 15
x = rng.normal(mu, sigma, 100000)
fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
# the histogram of the data
n, bins, patches = ax.hist(x, 30, density=1, facecolor='C0', alpha=0.75)

xl = ax.set_xlabel('Length [cm]')
xl.set_bbox(dict(facecolor='gray', edgecolor='red', boxstyle='round,pad=0.5'))

ax.set_ylabel('Probability')
ax.set_title('Aardvark lengths\n (not really)')
ax.text(75, .025, r'$\mu=115,\ \sigma=15$')
ax.axis([55, 175, 0, 0.03])
ax.grid(True)
fig.show()

# %% annotate
fig, ax = plt.subplots(figsize=(5, 2.7))

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2 * np.pi * t)
line, = ax.plot(t, s, lw=2)

ax.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
            arrowprops=dict(facecolor='black', shrink=0.05))

ax.set_ylim(-2, 2)
fig.show()

# %% legend
fig, ax = plt.subplots(figsize=(5, 2.7))
ax.plot(np.arange(len(data1)), data1, label='data1')
ax.plot(np.arange(len(data2)), data2, label='data2')
ax.plot(np.arange(len(data3)), data3, 'd', label='data3')  # 'd' is for 'diamond'
ax.legend()
fig.show()

# %% scale

fig, axs = plt.subplots(1, 2, figsize=(5, 2.7), layout='constrained')
xdata = np.arange(len(data1))  # make an ordinal for this
data = 10 ** data1
axs[0].plot(xdata, data)

axs[1].set_yscale('log')
axs[1].plot(xdata, data)
fig.show()

# %% locator & formatter
fig, axs = plt.subplots(2, 1, layout='constrained')
axs[0].plot(xdata, data1)
axs[0].set_title('Automatic ticks')

axs[1].plot(xdata, data1)
axs[1].set_xticks(np.arange(0, 100, 30), ['zero', '30', 'sixty', '90'])
axs[1].set_yticks([-1.5, 0, 1.5])  # note that we don't need to specify labels
axs[1].set_title('Manual ticks');
fig.show()

# %% locator & formatter

fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
dates = np.arange(np.datetime64('2021-11-15'), np.datetime64('2021-12-25'),
                  np.timedelta64(1, 'h'))
data = np.cumsum(np.random.randn(len(dates)))
ax.plot(dates, data)
cdf = mpl.dates.ConciseDateFormatter(ax.xaxis.get_major_locator())
ax.xaxis.set_major_formatter(cdf)
fig.show()

# %% locator & formatter
fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
categories = ['turnips', 'rutabaga', 'cucumber', 'pumpkins']

ax.bar(categories, np.random.rand(len(categories)));
fig.show()

# %% additional axis objects
t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2 * np.pi * t)
fig, (ax1, ax3) = plt.subplots(1, 2, figsize=(7, 2.7), layout='constrained')
l1, = ax1.plot(t, s)
ax2 = ax1.twinx()
l2, = ax2.plot(t, range(len(t)), 'C1')
ax2.legend([l1, l2], ['Sine (left)', 'Straight (right)'])

ax3.plot(t, s)
ax3.set_xlabel('Angle [rad]')
ax4 = ax3.secondary_xaxis('top', functions=(np.rad2deg, np.deg2rad))
ax4.set_xlabel('Angle [°]')
fig.show()

# %% 2d plot
X, Y = np.meshgrid(np.linspace(-3, 3, 128), np.linspace(-3, 3, 128))
Z = (1 - X / 2 + X ** 5 + Y ** 3) * np.exp(-X ** 2 - Y ** 2)

fig, axs = plt.subplots(2, 2, layout='constrained')
pc = axs[0, 0].pcolormesh(X, Y, Z, vmin=-1, vmax=1, cmap='RdBu_r')
fig.colorbar(pc, ax=axs[0, 0])
axs[0, 0].set_title('pcolormesh()')

co = axs[0, 1].contourf(X, Y, Z, levels=np.linspace(-1.25, 1.25, 11))
fig.colorbar(co, ax=axs[0, 1])
axs[0, 1].set_title('contourf()')

pc = axs[1, 0].imshow(Z ** 2 * 100, cmap='plasma',
                      norm=mpl.colors.LogNorm(vmin=0.01, vmax=100))
fig.colorbar(pc, ax=axs[1, 0], extend='both')
axs[1, 0].set_title('imshow() with LogNorm()')

pc = axs[1, 1].scatter(data1, data2, c=data3, cmap='RdBu_r')
fig.colorbar(pc, ax=axs[1, 1], extend='both')
axs[1, 1].set_title('scatter()')

fig.show()

# %% figure layout
fig, axd = plt.subplot_mosaic([['upleft', 'right'],
                               ['lowleft', 'right']], layout='constrained')
axd['upleft'].set_title('upleft')
axd['lowleft'].set_title('lowleft')
axd['right'].set_title('right');
fig.show()
