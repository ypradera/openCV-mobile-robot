# import curses and GPIO
import curses
import RPi.GPIO as GPIO

#set GPIO numbering mode and define output pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)

# Get the curses window, turn off echoing of keyboard to screen, turn on
# instant (no waiting) key response, and use special values for cursor keys
screen = curses.initscr()
curses.noecho() 
curses.cbreak()
screen.keypad(True)

try:
        while True:   
            char = screen.getch()
            if char == ord('q'):
                break
            elif char == curses.KEY_UP:
                GPIO.output(11,False)
                GPIO.output(15,True)
                GPIO.output(16,False)
                GPIO.output(18,True)
            elif char == curses.KEY_DOWN:
                GPIO.output(11,True)
                GPIO.output(15,False)
                GPIO.output(16,True)
                GPIO.output(18,False)
            elif char == curses.KEY_RIGHT:
                GPIO.output(11,True)
                GPIO.output(15,False)
                GPIO.output(16,False)
                GPIO.output(18,True)
            elif char == curses.KEY_LEFT:
                GPIO.output(11,False)
                GPIO.output(15,True)
                GPIO.output(16,True)
                GPIO.output(18,False)
            elif char == 10:
                GPIO.output(11,False)
                GPIO.output(15,False)
                GPIO.output(16,False)
                GPIO.output(18,False)
             
finally:
    #Close down curses properly, inc turn echo back on!
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    GPIO.cleanup()
    
