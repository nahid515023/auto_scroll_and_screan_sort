import pyautogui as pg
import time

time.sleep(10)
print('Start time.')
i=1
while 1:
    time.sleep(1)
    im =pg.screenshot()
    name = 'pic/'+str(i)+'a.png'
    im.save(name)
    pg.scroll(6)
    i+=1
    if i==10:
        break
