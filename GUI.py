from account_manager import AccountManager
try:
	import tkinter as tk
	from tkinter import *
except:
	print("missing module: tkinter")

window = tk.Tk(screenName="PyNewsAggregator",baseName=None,className='PyNewsAggregator',useTk=1)

window.geometry("500x200")

notify = Message(window,text = "")
notify.config(width=150)
notify.pack(side = TOP, expand = True, fill = None)
notify.pack_forget()

def check(email_id, keywords, sub):
	global notify
	notify.pack_forget()
	account = AccountManager(email_id, keywords)
	if sub == True and len(email_id) != 0 and len(keywords) != 0: 
		account.subscribe()
	elif sub == False and len(email_id) != 0:
		account.unsubscribe()
	else:
		notify = Message(window,text = "Missing Input")
		notify.config(width=150)
		notify.pack(side = TOP, expand = True, fill = None)		

Label(window, text='Email ID').pack(side = TOP, expand = True, fill = None)
email_id = Entry(window)
email_id.pack(side = TOP, expand = True, fill = None)

Label(window, text='Keywords/Phrases(separated by commas)').pack(side = TOP, expand = True, fill = None)
keywords = Entry(window)
keywords.pack(side = TOP, expand = True, fill = None)

button = tk.Button(window,text = 'Subscribe', width=40,command=lambda: check(email_id.get(), keywords.get(), True))
button.bind('<Return>',lambda _: check(email_id.get(), keywords.get(), True))
button.pack(side = TOP, expand = True, fill = None)

button = tk.Button(window,text = 'Unsubscribe', width=40,command=lambda: check(email_id.get(), keywords.get(), False))
button.bind('<Return>',lambda _: check(email_id.get(), keywords.get(), False))
button.pack(side = TOP, expand = True, fill = None)

window.mainloop() 
