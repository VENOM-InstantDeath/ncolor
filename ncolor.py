##########################
# Ncurses color palette  #
# By: VENOM-InstantDeath #
# Version: 1.0.0         #
##########################

import curses

def main(stdscr):
    curses.curs_set(0)
    curses.start_color()
    curses.use_default_colors()
    for i in range(250):
        curses.init_pair(i,-1,i)
    y = 0
    x = 0
    t = 0
    t1 = 0
    for i in range(250):
        t += 1
        try:
            stdscr.addstr(y, x, f'  {i}  ', curses.color_pair(i))
            x+= 8
        except curses.error:
            x = 0
            y += 1
            t1 += 1
    stdscr.addstr(15,0,str(t))
    stdscr.addstr(16,0,str(t1))
    stdscr.getch()

if __name__ == '__main__':
    curses.wrapper(main)
