import wx
import PBOTugas1

app = wx.App()

frame = PBOTugas1.MyFrame1(parent=None)
frame.Show()

app.MainLoop()