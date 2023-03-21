import sys
import art
import curses
from datetime import datetime


def main():
    scr = curses.initscr()
    rows, _ = scr.getmaxyx()

    while True:
        try:
            scr.clear()
            curr = (" " * 7) + datetime.now().strftime("%H:%M:%S")
            time_txt = art.text2art(curr, font="clb8x10")
            scr.addstr(rows // 2 - 5, 0, time_txt)
            curses.napms(1000)
            scr.refresh()
        except KeyboardInterrupt:
            curses.endwin()
            sys.exit(0)


if __name__ == "__main__":
    main()
