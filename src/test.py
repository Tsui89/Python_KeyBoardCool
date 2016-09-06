# -*- coding: utf-8 -*-
import pythoncom,pyHook
import win32api
import time
import win32con

ScrollFlag = False
Flag = False
TotalSkill = 2
Scroll = 0
'''
kaelkey={'0':{'flag':,'time':,}}
'''
SkillKey = ['2','5','3','4','0','1','6','7','8','9']
KaelKey=[]
VSkillKey = {
    '2':[87,69,69,82,68],
    '5':[81,87,69,82,66],
    '3':[87,87,81,82,88],
    '4':[87,87,87,82,87],
    '0':[69,69,69,82,84],
    '1':[81,81,81,82,89],
    '6':[81,81,87,82,86],
    '7':[69,81,81,82,71],
    '8':[69,69,81,82,70],
    '9':[87,87,69,82,90]
}
SLkillKey = {
    '2':[68],
    '5':[66],
    '3':[88],
    '4':[87],
    '0':[84],
    '1':[89],
    '6':[86],
    '7':[71],
    '8':[70],
    '9':[90]
}
ScrollKey=[69,81,87]

def keyinput(*args):
#    print args
    for arg in args:
        win32api.keybd_event(arg,0,0,0)
        win32api.keybd_event(arg,0,win32con.KEYEVENTF_KEYUP,0)

def onMouseEvent(event):
    global  ScrollFlag
  # 监听鼠标事件
    '''
    print "MessageName:",event.MessageName
    print "Message:", event.Message
    print "Time:", event.Time
    print "Window:", event.Window
    print "WindowName:", event.WindowName
    print "Position:", event.Position
    print "Wheel:", event.Wheel
    print "Injected:", event.Injected
    print"---"
    '''
    if event.WindowName != 'Warcraft III':
        return True
    if ScrollFlag == True:
        if event.Wheel == -1:
#            print 'huizhuan'
            keyinput(103)
            return False
        elif event.Wheel == 1:
            keyinput(104)
            return False
  # 返回 True 以便将事件传给其它处理程序
  # 注意，这儿如果返回 False ，则鼠标事件将被全部拦截
  # 也就是说你的鼠标看起来会僵在那儿，似乎失去响应了

    return True

def OnKeyboardEvent(event):
    global Flag,TotalSkill,VSkillKey,SkillKey,Scroll,ScrollKey,ScrollFlag
    # Return the time in seconds since the epoch as a floating point number.
    #
    # The epoch is the point where the time starts. On January 1st of that year,
    # at 0 hours, the “time since the epoch” is zero. For Unix, the epoch is 1970.
    # Returns the number of milliseconds since windows started
    '''
    print event.Time
#    print time.time()
    print win32api.GetTickCount()
    print 'MessageName:',event.MessageName
    print 'Message:',event.Message
    print 'Time:', time.ctime(time.time())
    print 'Window:',event.Window
    print 'WindowName:',event.WindowName
    print 'Ascii:', event.Ascii, chr(event.Ascii)
    '''
#    print 'KeyID:', event.KeyID
    if event.WindowName != 'Warcraft III':
        return True
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
    if event.KeyID == 118:
        ScrollFlag = True
        return False
    elif event.KeyID == 119:
        ScrollFlag = False
        return False

    if Flag == True:

        if event.Key in SkillKey:
            #keyinput(VSkillKey[event.Key][0],VSkillKey[event.Key][1],VSkillKey[event.Key][2],VSkillKey[event.Key][3],VSkillKey[event.Key][4])
            keyinput(VSkillKey[event.Key][0],VSkillKey[event.Key][1],VSkillKey[event.Key][2],VSkillKey[event.Key][3])
            time.sleep(0.3)
            keyinput(SLkillKey[event.Key][0])
            return False
        elif event.Key == 'Oem_3':
            Scroll +=1
            if Scroll > 2 :
                Scroll = 0
            keyinput(ScrollKey[Scroll],ScrollKey[Scroll],ScrollKey[Scroll])
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
hm.MouseAll = onMouseEvent
hm.HookMouse()

pythoncom.PumpMessages(10000)
