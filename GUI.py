try:
    from account_manager import AccountManager
    import tkinter as tk
    from tkinter import *
except:
    print("missing module/s: tkinter/account_manager")

window = tk.Tk(screenName="PyNewsAggregator", baseName=None, className='PyNewsAggregator', useTk=1)

window.geometry("500x200")

notify = Message(window, text="")
notify.config(width=150)
notify.pack(side=TOP, expand=True, fill=None)
notify.pack_forget()


def check(email_id_, keywords_, sub):
    """
    checks if proper input is given for the requested action
    """
    global notify
    notify.pack_forget()
    account = AccountManager(email_id_, keywords_)
    if sub and len(email_id_) != 0 and len(keywords_) != 0:
        account.subscribe()
    elif not sub and len(email_id_) != 0:
        account.unsubscribe()
    else:
        notify = Message(window, text="Missing Input")
        notify.config(width=150)
        notify.pack(side=TOP, expand=True, fill=None)


Label(window, text='Email ID').pack(side=TOP, expand=True, fill=None)
email_id = Entry(window)
email_id.pack(side=TOP, expand=True, fill=None)

keyword_inst = "Keywords\n(separate the keywords you want in the same link by spaces, different links by '-')"
Label(window, text=keyword_inst).pack(side=TOP, expand=True, fill=None)
keywords = Entry(window)
keywords.pack(side=TOP, expand=True, fill=None)

button = tk.Button(window, text='Subscribe', width=40, command=lambda: check(email_id.get(), keywords.get(), True))
button.bind('<Return>', lambda _: check(email_id.get(), keywords.get(), True))
button.pack(side=TOP, expand=True, fill=None)

button = tk.Button(window, text='Unsubscribe', width=40, command=lambda: check(email_id.get(), keywords.get(), False))
button.bind('<Return>', lambda _: check(email_id.get(), keywords.get(), False))
button.pack(side=TOP, expand=True, fill=None)

window.mainloop()
