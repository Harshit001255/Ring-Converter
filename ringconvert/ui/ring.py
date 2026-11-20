import os
import tkinter as tk
from ringconvert.registry import get_targets

def show_ring(file_path):
    base, ext = os.path.splitext(file_path)
    e = ext.lower().lstrip(".")
    options = get_targets(e)
    if len(options) == 0:
        print(f"No conversion available for .{e}")
        return

    root = tk.Tk()
    canvas = tk.Canvas(root, width=400, height=400)
    canvas.pack()

    cx, cy = 200, 200
    radius = 150
    n = len(options)
    slice_size = 360/n
    colors = ["blue", "green", "yellow", "pink", "red", "violet", "orange", "cyan", "magenta", "lime", "teal", "indigo"]
    if n == 1:
        canvas.create_oval(cx - radius, cy - radius, cx + radius, cy + radius, fill = colors[0])
    else:
        for i in range(n):
            canvas.create_arc(cx - radius, cy - radius, cx + radius, cy + radius, start = -i*slice_size, extent = -slice_size,fill = colors[i])

    root.mainloop()