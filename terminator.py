import traceback
while True:
	try:
		IP = input('>>> ')
		print(eval(IP))
	except SyntaxError:
		try:
			if IP.endswith(':') and not IP.endswith('\n'):
				IP += input('... ')
			else:
				exec(IP)
		except:
			print(traceback.format_exc())
	except:
		print(traceback.format_exc())
