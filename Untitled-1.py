"""        

for p in people:
    plt.plot(p.x, p.y, marker='o', markersize=10    , color="red")

plt.xticks(range(0, 9))
plt.yticks(range(0, 9))

plt.grid()
plt.show()




im = plt.imshow(np.reshape(np.random.rand(100), newshape=(10,10)),
                    interpolation='none', vmin=0, vmax=1, aspect='equal')
ax = plt.gca()
ax.set_xticks(np.arange(0, 10, 1))
ax.set_yticks(np.arange(0, 10, 1))
ax.set_xticklabels(np.arange(1, 11, 1))
ax.set_yticklabels(np.arange(1, 11, 1))
plt.show()"""

"""foo = np.random.rand(35).reshape(5, 7)
# This keeps the default orientation (origin at top left):
extent = (0, foo.shape[1], foo.shape[0], 0)
_, ax = plt.subplots()
ax.imshow(foo, extent=extent)
ax.grid(color='w', linewidth=2)
ax.set_frame_on(False)
plt.show()"""
