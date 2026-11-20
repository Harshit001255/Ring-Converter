import os
import math
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

    inner_radius = 50
    canvas.create_oval(cx - inner_radius, cy - inner_radius, cx + inner_radius, cy + inner_radius, fill = "lightgray")
    text  = e.upper()
    canvas.create_text(cx, cy, text=text, font=("Arial", 16, "bold"))
    for i in range(n):
        mid_angle = (i + 0.5) * slice_size
        angle_in_radians = math.radians(mid_angle)
        r_text = 100
        x = cx + r_text * math.cos(angle_in_radians)
        y = cy + r_text * math.sin(angle_in_radians)
        canvas.create_text(x, y, text = options[i], font=("Arial", 12), fill="white")

    def on_move(event):
        mx, my = event.x, event.y
        dx = mx - cx
        dy = my - cy
        angle = math.degrees(math.atan2(dy, dx)) % 360
        index = int(angle // slice_size)
        dist = math.hypot(dx, dy)
        if dist < inner_radius or dist > radius:
            print("None")
            return
        else:
            print(f"Mouse: ({event.x}, {event.y}) -> Angle: {angle:.2f} degrees -> Slice Index: {index} -> Option: {options[index]}")

    canvas.bind("<Motion>", on_move)
    root.mainloop()