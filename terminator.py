import traceback
while True:
	try:
		IP = input('')
		block = IP
		print(eval(IP))
	except SyntaxError:
		try:
			if IP.endswith(':'):
				block += '\n'
				while IP != '\n':
					IP = input('')+'\n'
					block += IP
			exec(block)
		except:
			print(traceback.format_exc())
	except:
		print(traceback.format_exc())
