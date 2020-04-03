from tkinter import*
from tkinter import messagebox as m
from smtplib import *
import pymysql as db
import pandas as pd

window=Tk()
window.title("e-mail")

def email():
	subject=sub_en.get()
	content=msg_en.get("1.0",'end-1c')
	mail=SMTP('smtp.gmail.com', 587)
	mail.ehlo()
	mail.starttls()
	recipent=to_en.get()
	sender=frm_en.get()
	passwd=??
	mail.login(sender,passwd)
	header='To:'+recipent+'\n'+'From: '+sender+'\n'+ 'Subject: '+subject+'\n'
	content=header+content
	mail.sendmail(sender,recipent,content)
	m.showinfo("Successfully Sent",'''Your email to %s was sent successfully
		Please check your Inbox'''%recipent)
	def his():
		send=frm_en.get()
		rec=to_en.get()
		conn = db.connect( host="localhost", user="root", port=3306, passwd="", database="mail")
		cur = conn.cursor()
		sql_insert_query="""INSERT INTO `mail`(`sender`, `recipent`) VALUES ('%s','%s')"""%(send,rec)
		cur.execute(sql_insert_query)
		cur.close()
		conn.commit()
		conn.close()
		m.showinfo("Database Connected","Your History has been saved on server")
		mail.close()
	his()

tit=Label(window,text='Compose e-mail',bg='orange')
frm=Label(window,text='From')
to=Label(window,text='To')
sub=Label(window,text='Subject')
msg=Label(window,text='Message')
tit.grid(row=0,columnspan=2)
frm.grid(row=1,column=0)
to.grid(row=2,column=0)
sub.grid(row=3,column=0)
msg.grid(row=4,column=0)
but=Button(window,text='SEND',bg='orange',command=email)
#Change from Entry to Text to check
frm_en=Entry(window)
to_en=Entry(window)
sub_en=Entry(window)
msg_en=Text(window,height=6,width=20)
frm_en.grid(row=1,column=1)
to_en.grid(row=2,column=1)
sub_en.grid(row=3,column=1)
msg_en.grid(row=4,column=1)
but.grid(row=5,columnspan=2)

window.mainloop()