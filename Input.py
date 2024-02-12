import pyautogui as pg


class Input():

    def Send(self, button):
        
        pg.keyDown(button)
        pg.keyUp(button)