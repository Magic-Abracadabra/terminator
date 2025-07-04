import traceback
while True:
	try:
		IP = input('>>> ')
		print(eval(IP))
	except SyntaxError:
		try:
			exec(IP)
		except:
			print(traceback.format_exc())
	except:
		print(traceback.format_exc())
