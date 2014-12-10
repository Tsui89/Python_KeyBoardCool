__author__ = 'IBM-cuiwc'
import wx
import win32api
import pythoncom
import globalvalue
import pyHook
import time

class WindowMain(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(
            self,
            parent=None,
            id=-1,
            title=u"KeyboardCool",
            size=(400,600),
            style=wx.CAPTION | wx.CLOSE_BOX | wx.MINIMIZE_BOX)
        print(win32api.GetComputerName())
        panel = wx.Panel(self, id=-1, pos=(0, 0), style=wx.TAB_TRAVERSAL, name='panel1')
        self.Bind(wx.EVT_CLOSE, self.OnExit)
        self.OnRun(panel)
    def OnRun(self,panel):
        self.keys=[]
        self.CreatePanel(panel)

        pass
    def CreatePanel(self,panel):
        rect = panel.Rect

        onbuttun = wx.Button(
            panel, label="On", pos=(rect[0] + 10, rect[1]  + 15), size=(50,30))
        onbuttun.Bind(wx.EVT_BUTTON, self.On, onbuttun)
        offbuttun = wx.Button(
            panel, label="Off", pos=(rect[0] + 90, rect[1]  + 15), size=(50,30))
        offbuttun.Bind(wx.EVT_BUTTON, self.Off, offbuttun)

        newbuttun = wx.Button(
            panel, label="New", pos=(rect[0] + 170, rect[1]  + 15), size=(50,30))
        '''
        rect = onbuttun.Rect
        key1 = KeyModule(panel,rect)

        rect = key1.Rect()
        key2 = KeyModule(panel,rect)

        rect = key2.Rect()
        key3 = KeyModule(panel,rect)

        rect = key3.Rect()
        key4 = KeyModule(panel,rect)

        rect = key4.Rect()
        key5 = KeyModule(panel,rect)

        rect = key5.Rect()
        key6 = KeyModule(panel,rect)
        '''
        rect = onbuttun.Rect

        for i in range(6):
            key = KeyModule(panel,rect)
            rect = key.Rect()
            self.keys.append(key)
    def On(self,event):
        print 'On'
        pythoncom.PumpMessages()
        pass
    def Off(self,event):
        win32api.PostQuitMessage()
        pass

    def OnExit(self,event):
        win32api.PostQuitMessage()
        self.Destroy()
def onKeyboardEvent(event):
    print event
    print event.Time
    print time.time()
    '''# Returns the number of milliseconds since windows started'''
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

    '''# return True to pass the event to other handlers'''
    return True
class KeyModule():
    def __init__(self,panel,rect):
        self.k = wx.TextCtrl(panel, -1, pos=(rect[0] + 0, rect[1] + 60), size=(50,30))
        self.k1 = wx.TextCtrl(panel, -1, pos=(rect[0] + 90, rect[1] + 60), size=(50,30))
        self.k2 = wx.TextCtrl(panel, -1, pos=(rect[0] + 170, rect[1] + 60), size=(50,30))
        self.k3 = wx.TextCtrl(panel, -1, pos=(rect[0] + 250, rect[1] + 60), size=(50,30))
        self.k4 = wx.TextCtrl(panel, -1, pos=(rect[0] + 320, rect[1] + 60), size=(50,30))
        self.k.SetMaxLength(1)
        self.k1.SetMaxLength(1)
        self.k2.SetMaxLength(1)
        self.k3.SetMaxLength(1)
        self.k4.SetMaxLength(1)
        print '99'
    def Rect(self):
        return self.k.Rect
    def On(self):

        pass
class MyApp(wx.App):
    def __init__(self):
        wx.App.__init__(self)

    def OnInit(self):
        frame = WindowMain()
        frame.Show(True)
        return True
def main():
    app = MyApp()
    app.MainLoop()
    hk = pyHook.HookManager()
    hk.KeyDown = onKeyboardEvent
    hk.HookKeyboard()

if  __name__ == "__main__":
    main()