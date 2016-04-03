import time

class sequencer(object):
	commands = []
	def repeats(self,commands,count):
		templist = []
		outlist = []
		while len(commands)> 0 :
			cmd  = commands[0].split()
			if cmd[0] == "End" :
				commands.pop(0)
				break
			if cmd[0] == "Repeat":
				commands.pop(0)
				if cmd[1] > 0:
					templist += self.repeats(commands,cmd[1])
			else :
				templist.append(commands[0])
				commands.pop(0)
		for i in range(int(count)):
			outlist += templist
		return outlist
		
	def buildcommands(self,cmds):
		while len(cmds)> 0 :
			cmd = cmds[0].split()
			if cmd[0] == "Repeat":
				cmds.pop(0)
				if cmd[1] > 0 :
					self.commands += self.repeats(cmds,cmd[1])
			else :
				self.commands += [cmds[0]]
				cmds.pop(0)
		print self.commands
		
	def readfile(self,filename):
		txt = []
		f = open(filename,'r')
		for line in f:
			txt += [line]
		f.close()
		return self.buildcommands(txt)
		
	def runcommands(self):
		for command in self.commands:
			self.parsecommand(command)
			
	def parsecommand(self,cmnd):
		mod = False
		cmd = cmnd.split()
		for idx,val in enumerate(cmd):
			if idx == 0:
				command = val
			if idx == 1:
				mod = True
				modifier = val
			if command == "Run":
				print "Run\n"
				if mod:
					time.sleep(float(modifier)/1000)
			if command == "Wait":
				print "wait"
				if mod:
					time.sleep(float(modifier)/1000)
			if command == "Stop":
				print "Stop"
			mod = False



		

if __name__ == '__main__':
	commands = ["Repeat 10","Run 1000","Wait 1000","End","Stop"]
	commands2 = ["Repeat 10","Run 1000","Repeat 8","Run 500","Wait 300","End","Run 1000","Wait 1000","Repeat 2","Run 2000","End","End","Stop"]
	commands1 = ["Spit","Run 1000","Run 1000","Wait 1000","Run 2000","Wait 2000","Wait 1000","Stop"]
	seq = sequencer()
#	seq.buildcommands(commands1)
	seq.buildcommands(commands2)
	seq.runcommands()
	