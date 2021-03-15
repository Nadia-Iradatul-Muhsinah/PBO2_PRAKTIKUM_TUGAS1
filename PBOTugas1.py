# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Hello WX" ), wx.VERTICAL )
		
		self.m_panel2 = wx.Panel( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )
		
		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText2 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Nama", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		self.m_staticText2.SetFont( wx.Font( 10, 74, 90, 90, False, "Arial Rounded MT Bold" ) )
		self.m_staticText2.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )
		self.m_staticText2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		fgSizer1.Add( self.m_staticText2, 0, wx.ALL, 10 )
		
		self.m_staticText3 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Nadia Iradatul Muhsinah", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		self.m_staticText3.SetFont( wx.Font( 10, 72, 93, 90, False, "Baskerville Old Face" ) )
		self.m_staticText3.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.m_staticText3.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		fgSizer1.Add( self.m_staticText3, 0, wx.ALL, 10 )
		
		self.m_staticText5 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"NIM", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		self.m_staticText5.SetFont( wx.Font( 10, 74, 90, 90, False, "Arial Rounded MT Bold" ) )
		self.m_staticText5.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		fgSizer1.Add( self.m_staticText5, 0, wx.ALL, 10 )
		
		self.m_staticText6 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"192410101020", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		self.m_staticText6.SetFont( wx.Font( 10, 72, 93, 90, False, "Baskerville Old Face" ) )
		self.m_staticText6.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.m_staticText6.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		fgSizer1.Add( self.m_staticText6, 0, wx.ALL, 10 )
		
		
		self.m_panel2.SetSizer( fgSizer1 )
		self.m_panel2.Layout()
		fgSizer1.Fit( self.m_panel2 )
		sbSizer1.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( sbSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

