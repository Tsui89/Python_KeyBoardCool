__author__ = 'IBM-cuiwc'
# -*- coding: utf-8 -*-
import pythoncom,pyHook
import win32api
#import time
import win32con


Flag = False
TotalSkill = 1
Scroll = 0
'''
kaelkey={'0':{'flag':,'time':,}}
'''
SkillKey = ['D','B','X','C','T','Y','V','G','F','Z']
KaelKey=[]
VSkillKey = {
    'D':[87,69,69,82,68],
    'B':[81,87,69,82,66],
    'X':[87,87,81,82,88],
    'C':[87,87,87,82,87],
    'T':[69,69,69,82,84],
    'Y':[81,81,81,82,89],
    'V':[81,81,87,82,86],
    'G':[69,81,81,82,71],
    'F':[69,69,81,82,70],
    'Z':[87,87,69,82,90]
}
ScrollKey=[69,81,87]

def keyinput(*args):
#    print args
    for arg in args:
        win32api.keybd_event(arg,0,0,0)
        win32api.keybd_event(arg,0,win32con.KEYEVENTF_KEYUP,0)
    '''
    win32api.keybd_event(k1,0,0,0)
    win32api.keybd_event(k1,0,win32con.KEYEVENTF_KEYUP,0)
    win32api.keybd_event(k2,0,0,0)
    win32api.keybd_event(k2,0,win32con.KEYEVENTF_KEYUP,0)
    win32api.keybd_event(k3,0,0,0)
    win32api.keybd_event(k3,0,win32con.KEYEVENTF_KEYUP,0)
    win32api.keybd_event(k4,0,0,0)
    win32api.keybd_event(k4,0,win32con.KEYEVENTF_KEYUP,0)
    win32api.keybd_event(k5,0,0,0)
    win32api.keybd_event(k5,0,win32con.KEYEVENTF_KEYUP,0)
    '''

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
    global Flag,TotalSkill,VSkillKey,SkillKey,Scroll,ScrollKey
    # Return the time in seconds since the epoch as a floating point number.
    #
    # The epoch is the point where the time starts. On January 1st of that year,
    # at 0 hours, the “time since the epoch” is zero. For Unix, the epoch is 1970.
    # Returns the number of milliseconds since windows started
    '''
    print event.Time
    print time.time()
    print win32api.GetTickCount()
    print 'MessageName:',event.MessageName
    print 'Message:',event.Message
    print 'Time:', time.ctime(time.time())
    print 'Window:',event.Window
    print 'WindowName:',event.WindowName
    print 'Ascii:', event.Ascii, chr(event.Ascii)
    '''
#    if event.WindowName != 'Warcraft III':
#        return True
#    print 'Key:', event.Key

#    print 'KeyID:', event.KeyID
    '''
    print 'ScanCode:', event.ScanCode
    print 'Extended:', event.Extended
    print 'Injected:', event.Injected
    '''

#    print 'Alt', event.Alt
#    print 'Transition', event.Transition
#    print 'WindowName:',event.WindowName

#    print '---'
    if event.Alt == 32 :
        if event.Key == 'O':
            Flag = True
#            print 'open'
            return False
        elif event.Key == 'P':
            Flag = False
 #           print 'close'
            return False
        elif event.Key == '1':
            TotalSkill = 1
            return False
        elif event.Key == '2':
            TotalSkill = 2
            return False

    if Flag == True:
        if event.Key in SkillKey:
            if event.Key in KaelKey:
                return True
            else:
                keyinput(VSkillKey[event.Key][0],VSkillKey[event.Key][1],VSkillKey[event.Key][2],VSkillKey[event.Key][3])
                if len(KaelKey) >= TotalSkill:
                    KaelKey.pop(0)
                KaelKey.append(event.Key)
                return False
        elif event.Key == 'Oem_3':
            Scroll +=1
            if Scroll > 2 :
                Scroll = 0
            keyinput(ScrollKey[Scroll],ScrollKey[Scroll],ScrollKey[Scroll])
            return False

        '''
        if event.Key == '6': #幽冥漫步
            keyinput(81,81,87,82,86)
            return False
        elif event.Key == '7': #冰墙
            keyinput(69,81,81,82,71)
            return False
        elif event.Key == '8': #火人
            keyinput(69,69,81,82,70)
            return False
        elif event.Key == '0': #天火
            keyinput(69,69,69,82,84)
            return False
        elif event.Key == '1': #急速冷却
            keyinput(81,81,81,82,89)
            return False
        elif event.Key == '2': #陨石
            keyinput(87,69,69,82,68)
            return False
        elif event.Key == '3': #飓风
            keyinput(87,87,81,82,88)
            return False
        elif event.Key == '4': #磁暴
            keyinput(87,87,87,82,87)
            return False
        elif event.Key == '5': #超声波
            keyinput(81,87,69,82,66)
            return False
        elif event.Key == '9': #灵动迅捷
            keyinput(87,87,69,82,90)

            return False
        '''
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
