
import wmi
import pythoncom
from langchain_core.messages import AIMessage
from PIL import ImageGrab
from datetime import datetime
from PIL import ImageGrab

def get_current_brightness():
    c = wmi.WMI(namespace='wmi')
    brightness = c.WmiMonitorBrightness()[0]
    out = int(brightness.CurrentBrightness)
    return out



def current_dateNtime():
    datentime = datetime.now()
    # Replace ":" with "-" 
    return datentime.strftime("%Y-%m-%d_%H-%M-%S")



def increase_brightness(level = 10):
    """ increase the screen brightness by user specified amount.
    """

    pythoncom.CoInitialize()  # Initialize COM for the current thread
    c = wmi.WMI(namespace='wmi')
    methods = c.WmiMonitorBrightnessMethods()[0]
    res = get_current_brightness()

    fin_res = min(100, int(res) + int(level))  # Prevent going over 100
    methods.WmiSetBrightness(fin_res, 0)
    return AIMessage(content=f'Brightness decreased')

    


def reduce_brightness(level = 10):
    """ decrease the screen brightness by user specified amount.
    """
    pythoncom.CoInitialize()  # Initialize COM for the current thread
    c = wmi.WMI(namespace='wmi')
    methods = c.WmiMonitorBrightnessMethods()[0]
    res = get_current_brightness()
    fin_res = max(0, int(res) - int(level))
    methods.WmiSetBrightness(fin_res, 0)
    return AIMessage(content=f'Brightness decreased')



def take_screenshot():
    """ Take a screenshot and save it with a timestamped filename. 
    """
    timestamp = current_dateNtime()
    filename = f"screenshot_{timestamp}.png"
    screenshot = ImageGrab.grab()
    screenshot.save(filename)
    return filename
