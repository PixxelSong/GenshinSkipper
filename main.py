import random
import threading
import time
import vgamepad as vg
from pynput.keyboard import Listener, Key


class MainLoopThread(threading.Thread):
    def run(self):
        doMainLoop()


mainLoopThread = MainLoopThread()
lastClick = -0.01
mainLooping = False


def on_press(key):
    if key == Key.esc:
        currentClick = time.time()
        global lastClick
        if currentClick - lastClick < 0.3:
            global mainLooping
            global mainLoopThread
            if not mainLooping:
                print("脚本启动")
                mainLooping = True
                mainLoopThread = MainLoopThread()
                mainLoopThread.start()
            else:
                print("脚本关闭")
                mainLooping = False
                mainLoopThread.join()
        lastClick = currentClick


gamePad = vg.VX360Gamepad()


def doMainLoop():
    while True:
        if not mainLooping:
            return
        gamePad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)  # press the Left hat button
        gamePad.update()

        time.sleep(0.01 * rand())
        gamePad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)  # release the A button
        gamePad.update()
        time.sleep(0.1 * rand())


def rand():
    return random.randint(4, 9)


def initKeyBoardListening():
    with Listener(on_press=on_press) as listener:
        listener.join()


if __name__ == '__main__':
    print("双击 ESC 来启动/关闭脚本")
    initKeyBoardListening()
