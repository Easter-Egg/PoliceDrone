import wx
import time	# for smulating
import socket

HOST = '127.0.0.1'
PORT = 50000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

class UI(wx.Frame):

	def __init__(self, *args, **kw):
		super(UI, self).__init__(*args, **kw)
		self.InitUI()

	def InitUI(self):
		pnl = wx.Panel(self)	# create panel
		
		self.col = wx.Colour(0, 0, 0)
		self.cpnl = wx.Panel(pnl, pos=(70, 50), size=(30, 30))
		self.cpnl.SetBackgroundColour(self.col)

		cbtn = wx.Button(pnl, label='Conn', pos=(0, 100))
		cbtn.Bind(wx.EVT_BUTTON, self.connection)
		cbtn.SetSize((60, 40))	# connection button
		
		rtb = wx.ToggleButton(pnl, label='R', pos=(60, 100))
		rtb.SetSize((40, 40))	# display red light on LED
		rtb.Bind(wx.EVT_TOGGLEBUTTON, self.toggleRed)

		gtb = wx.ToggleButton(pnl, label='G', pos=(100, 100))
		gtb.SetSize((40, 40))	# display green light on LED
		gtb.Bind(wx.EVT_TOGGLEBUTTON, self.toggleGreen)

		ytb = wx.ToggleButton(pnl, label='B', pos=(140, 100))
		ytb.SetSize((40, 40))	# display yellow light on LED
		ytb.Bind(wx.EVT_TOGGLEBUTTON, self.toggleBlue)

		ubtn = wx.Button(pnl, label='Up', pos=(180, 100))
		ubtn.SetSize((60, 40))  # getting up
		ubtn.Bind(wx.EVT_BUTTON, self.altiUp)
		
		dbtn = wx.Button(pnl, label='Down', pos=(240, 100))
		dbtn.SetSize((60, 40))  # getting down
		dbtn.Bind(wx.EVT_BUTTON, self.altiDown)

		ctrlbtn = wx.ToggleButton(pnl, label='Ctrl', pos=(260, 0))
		ctrlbtn.SetSize((40, 40))
		ctrlbtn.Bind(wx.EVT_TOGGLEBUTTON, self.ctrlPos)

		# panel setting
		self.SetSize((320, 240))
		self.SetTitle('PoliceDrone')
		self.Centre()
		self.Show(True)


	##############################################
	#					     #
	#   get connection with drone using socket   #
	#					     #	
	##############################################
	def connection(self, e):
		s.connect((HOST, PORT))
		s.sendall('request connection')
		data = s.recv(1024)
		obj = e.GetEventObject()
		obj.SetLabel('Disc')
		dial = wx.MessageDialog(None, data, 'info', wx.OK)
		dial.ShowModal()

	##############################################
	#					     #
	#      read sensor data and sending data     #
	#					     #	
	##############################################
	def ctrlPos(self, e):
		obj = e.GetEventObject()
		isPressed = obj.GetValue()

		if isPressed:
			print 'pressed'
		else:
			print 'released'

	def OnClose(self, e):
		self.Close(True)

	#############################################
	#					    #
	#   display red light on LED using socket   #
	#					    #	
	#############################################
	def toggleRed(self, e): # 1
		s.sendall('light on RED')
		obj = e.GetEventObject()
		isPressed = obj.GetValue()
		
		green = self.col.Green()
		blue = self.col.Blue()

		if isPressed:
			self.col.Set(255, green, blue)
		else:
			self.col.Set(0, green, blue)

		self.cpnl.SetBackgroundColour(self.col)
		self.cpnl.Refresh()

	###############################################
	#					      #
	#   display green light on LED using socket   #
	#					      #	
	###############################################
	def toggleGreen(self, e): # 2
		s.sendall('light on Green')
		obj = e.GetEventObject()
		isPressed = obj.GetValue()
		
		red = self.col.Red()
		blue = self.col.Blue()

		if isPressed:
			self.col.Set(red, 255, blue)
		else:
			self.col.Set(red, 0, blue)

		self.cpnl.SetBackgroundColour(self.col)
		self.cpnl.Refresh()

	################################################
	#					       #
	#   display yellow light on LED using socket   #
	#					       #	
	################################################
	def toggleBlue(self, e): # 3
		s.sendall('light on Blue')
		obj = e.GetEventObject()
		isPressed = obj.GetValue()
		
		green = self.col.Green()
		red = self.col.Red()

		if isPressed:
			self.col.Set(red, green, 255)
		else:
			self.col.Set(red, green, 0)

		self.cpnl.SetBackgroundColour(self.col)
		self.cpnl.Refresh()

	##############################################
	#					     #
	#     getting altitude up by 'Up' button     #
	#					     #	
	##############################################
	def altiUp(self, e): # 4
		print 'getting up'

        ##############################################
	#					     #
	#   getting altitude down by 'Down' button   #
	#					     #	
	##############################################
	def altiDown(self, e): # 4
		print 'getting down'

def main():
	ex = wx.App()
	UI(None)
	ex.MainLoop()

if __name__ == '__main__':
	main()
