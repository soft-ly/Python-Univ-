import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Button
from matplotlib.widgets import Slider
from matplotlib.gridspec import GridSpec
import matplotlib.pyplot as plt

plt.rcParams['font.family']='Nanum Gothic'
plt.rcParams['axes.unicode_minus']=False

grid_size = 30


grid = np.zeros((grid_size, grid_size))

def update_display():
    ax.clear()
    ax.imshow(grid, cmap='binary', extent=[0, grid_size, 0, grid_size])
    ax.set_xticks(np.arange(0, grid_size, 1))
    ax.set_yticks(np.arange(0, grid_size, 1))
    ax.grid(which='both', color='black', linestyle='-', linewidth=1)
    ax.tick_params(which='both', bottom=False, left=False, labelbottom=False, labelleft=False)
    update_text()
    fig.canvas.draw_idle()

def onclick(event):
    if event.inaxes == ax:
        x, y = int(event.xdata), int(-event.ydata-1)  
        grid[y, x] = 1 if grid[y, x] == 0 else 0
        update_display()

def count_neighbors(y, x):
    neighbors = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i != 0 or j != 0:
                neighbors += grid[(y + i) % grid_size, (x + j) % grid_size]
    return neighbors

def update_grid():
    global grid
    new_grid = grid.copy()
    for y in range(grid_size):
        for x in range(grid_size):
            neighbors = count_neighbors(y, x)
            if grid[y, x] == 1 and (neighbors < 2 or neighbors > 3):
                new_grid[y, x] = 0
            elif grid[y, x] == 0 and neighbors == 3:
                new_grid[y, x] = 1
    grid = new_grid
    update_display()

def start(event):
    global anim
    anim.event_source.start()

def stop(event):
    global anim
    anim.event_source.stop()

fig = plt.figure(figsize=(10, 5))
gs = GridSpec(1, 2, width_ratios=[3, 1], figure=fig)

ax = fig.add_subplot(gs[0])

text_ax = fig.add_subplot(gs[1])
text_ax.axis('off')

def update_text():
    text_ax.clear()
    text_ax.axis('off')
    text_ax.text(0.5, 0.5, "참고: https://playgameoflife.com \n https://www.youtube.com/watch?v=C2vgICfQawE \n 원래는 그래프가 무한대로 계속 나가야하는데, \n 코딩을 하면서 'wrap'형식인 끝을 닿으면 반대 편으로 \n 계속되는 형식으로 바꾸어 봤습니다.", va='center', ha='center', fontsize=12,)
    
    fig.canvas.draw_idle()

update_display()

fig.canvas.mpl_connect('button_press_event', onclick)

start_ax = plt.axes([0.7, 0.02, 0.1, 0.04])
stop_ax = plt.axes([0.81, 0.02, 0.1, 0.04])
speed_ax = plt.axes([0.5, 0.02, 0.1, 0.04])
start_button = Button(start_ax, 'Start')
stop_button = Button(stop_ax, 'Stop')
speed_button = Slider(speed_ax, 'Speed  ', 500, 900)
start_button.on_clicked(start)
stop_button.on_clicked(stop)
anim = animation.FuncAnimation(fig, lambda x: update_grid(), interval=speed_button.val, blit=False)
anim.event_source.stop() 


def format_coord(x, y):
    return ""
ax.format_coord = format_coord


plt.show()
