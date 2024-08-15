import curses
import time
import math

def init_background(win):
    bg_text = "924"
    rows, cols = win.getmaxyx()
    for y in range(rows):
        for x in range(cols):
            if (x % 3) == 0:
                char = bg_text[(x // 3) % len(bg_text)]
                win.addch(y, x, char, curses.color_pair(4))

def display_art(win, start_y, start_x, apple_color, strawberry_color, strawberry_top_color):
    apple = [
        "   ,--./,-.",
        "   / #      \\",
        "  |          |",
        "   \\        /",
        "    `._,._,'"
    ]
    strawberry = [
        "    .-=-.",
        "   /  !  \\",
        "   \\     /",
        "    `._.'"
    ]

    try:
        for i, line in enumerate(apple):
            win.addstr(start_y + i, start_x, line, apple_color)
        for i, line in enumerate(strawberry, start=len(apple)):
            color = strawberry_top_color if i == len(apple) else strawberry_color
            win.addstr(start_y + i, start_x, line, color)
        win.refresh()
    except curses.error:
        pass

def main(win):
    curses.curs_set(0)
    win.nodelay(True)
    curses.start_color()
    curses.use_default_colors()

    curses.init_color(88, 500, 0, 0)
    curses.init_color(160, 1000, 250, 250)
    curses.init_color(28, 0, 500, 0)
    curses.init_color(100, 100, 100, 100)  

    curses.init_pair(1, 88, -1)
    curses.init_pair(2, 160, -1)
    curses.init_pair(3, 28, -1)
    curses.init_pair(4, 100, -1)  

    init_background(win) 

    max_y, max_x = win.getmaxyx()
    center_x, center_y = max_x // 2, max_y // 2
    radius = min(center_x, center_y) // 2
    angle = 0
    
    while True:
        win.clear()
        init_background(win)  
        x = center_x + int(radius * math.cos(angle))
        y = center_y + int(radius * math.sin(angle) * 0.5)
        
        display_art(win, y, x, curses.color_pair(1), curses.color_pair(2), curses.color_pair(3))
        
        time.sleep(0.05)
        angle += 0.1
        
        if win.getch() == ord('q'):
            break

if __name__ == '__main__':
    curses.wrapper(main)
