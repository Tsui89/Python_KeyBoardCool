__author__ = 'IBM-cuiwc'
# -*- coding: utf-8 -*-
import pythoncom, pyHook
import win32api
import time
import win32con

def onMouseEvent(event):

  # 监听鼠标事件
  print "MessageName:",event.MessageName
  print "Message:", event.Message
  print "Time:", event.Time
  print "Window:", event.Window
  print "WindowName:", event.WindowName
  print "Position:", event.Position
  print "Wheel:", event.Wheel
  print "Injected:", event.Injected
  print"---"

  # 返回 True 以便将事件传给其它处理程序
  # 注意，这儿如果返回 False ，则鼠标事件将被全部拦截
  # 也就是说你的鼠标看起来会僵在那儿，似乎失去响应了

  return True

def OnKeyboardEvent(event):
    print event.Time
    # Return the time in seconds since the epoch as a floating point number.
    #
    # The epoch is the point where the time starts. On January 1st of that year,
    # at 0 hours, the “time since the epoch” is zero. For Unix, the epoch is 1970.
    print time.time()
    # Returns the number of milliseconds since windows started
    print win32api.GetTickCount()

    print 'MessageName:',event.MessageName
    print 'Message:',event.Message
    print 'Time:', time.ctime(time.time())
    print 'Window:',event.Window
    print 'WindowName:',event.WindowName
    print 'Ascii:', event.Ascii, chr(event.Ascii)
    print 'Key:', event.Key
    print 'KeyID:', event.KeyID
    print 'ScanCode:', event.ScanCode
    print 'Extended:', event.Extended
    print 'Injected:', event.Injected
    print 'Alt', event.Alt
    print 'Transition', event.Transition
    print '---'

    if event.Key == '6': #幽冥漫步
        win32api.keybd_event(81,0,0,0)
        win32api.keybd_event(81,0,0,0)
        win32api.keybd_event(81,0,0,0)
        win32api.keybd_event(82,0,0,0)
        win32api.keybd_event(86,0,0,0)
        return False
    elif event.Key == '7': #冰墙
        win32api.keybd_event(69,0,0,0)
        win32api.keybd_event(81,0,0,0)
        win32api.keybd_event(81,0,0,0)
        win32api.keybd_event(82,0,0,0)
        win32api.keybd_event(71,0,0,0)
        return False
    elif event.Key == '8': #火人
        win32api.keybd_event(69,0,0,0)
        win32api.keybd_event(69,0,0,0)
        win32api.keybd_event(81,0,0,0)
        win32api.keybd_event(82,0,0,0)
        win32api.keybd_event(70,0,0,0)
        return False
    elif event.Key == '0': #天火
        win32api.keybd_event(69,0,0,0)
        win32api.keybd_event(69,0,0,0)
        win32api.keybd_event(69,0,0,0)
        win32api.keybd_event(82,0,0,0)
        win32api.keybd_event(84,0,0,0)
        return False
    elif event.Key == '1': #急速冷却
        win32api.keybd_event(81,0,0,0)
        win32api.keybd_event(81,0,0,0)
        win32api.keybd_event(81,0,0,0)
        win32api.keybd_event(82,0,0,0)
        win32api.keybd_event(89,0,0,0)
        return False
    elif event.Key == '2': #陨石
        win32api.keybd_event(87,0,0,0)
        win32api.keybd_event(69,0,0,0)
        win32api.keybd_event(69,0,0,0)
        win32api.keybd_event(82,0,0,0)
        win32api.keybd_event(68,0,0,0)
        return False
    elif event.Key == '3': #飓风
        win32api.keybd_event(81,0,0,0)
        win32api.keybd_event(81,0,0,0)
        win32api.keybd_event(87,0,0,0)
        win32api.keybd_event(82,0,0,0)
        win32api.keybd_event(88,0,0,0)
        return False
    elif event.Key == '4': #磁暴
        win32api.keybd_event(87,0,0,0)
        win32api.keybd_event(87,0,0,0)
        win32api.keybd_event(87,0,0,0)
        win32api.keybd_event(82,0,0,0)
        win32api.keybd_event(67,0,0,0)
        return False
    elif event.Key == '5': #超声波
        win32api.keybd_event(81,0,0,0)
        win32api.keybd_event(87,0,0,0)
        win32api.keybd_event(69,0,0,0)
        win32api.keybd_event(82,0,0,0)
        win32api.keybd_event(66,0,0,0)
        return False
    elif event.Key == '9': #灵动迅捷
        win32api.keybd_event(87,0,0,0)
        win32api.keybd_event(87,0,0,0)
        win32api.keybd_event(69,0,0,0)
        win32api.keybd_event(82,0,0,0)
        win32api.keybd_event(90,0,0,0)
        return False
    # return True to pass the event to other handlers
    return True

# create a hook manager
hm = pyHook.HookManager()
# watch for all keyboard events
hm.KeyDown = OnKeyboardEvent
# set the hook
hm.HookKeyboard()
# wait forever
#hm.MouseAll = onMouseEvent
#hm.HookMouse()

pythoncom.PumpMessages(10000)
