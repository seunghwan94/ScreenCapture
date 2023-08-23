# 이미지 캡처 프로그램
# 사용법
# 캡처하고 싶은 사이즈 만큼 왼쪽 위에 한번 클릭 오른쪽 밑에 클릭

from pynput.mouse import Listener
from PIL import Image
import pyautogui
import os

coord = []
save_path = 'D:/myscreenshot.jpg'

myScreenshot = pyautogui.screenshot()
myScreenshot.save(save_path)

im = Image.open(save_path)

# getting mouse coordinates when mouse click.
def click(x,y,buton,pressed):
    if pressed:
        x = int(x)
        y = int(y)
        coord.append(x)
        coord.append(y)

        if len(coord) == 4:
            return False

with Listener(on_click = click) as Listener:
    Listener.join()

left = coord[0]
top = coord[1]
right = coord[2]
bottom = coord[3]

im1 = im.crop((left,top,right,bottom))
os.remove(save_path)
im1.save(save_path)