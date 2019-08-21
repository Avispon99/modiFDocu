#!usr/bind/python
#-*- coding: utf-8 -*-

"""Application to generate redundant or repetitive corrections in documents"""

__autor__ = "Jhonatan Leonardo Zuluaga Torres "
__copyright__ = "Copyright 2018, Jhonatan Zu"
__credits__ = "Jhonatan Zu"
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Jhonatan Zu"
__email__ = "jhonatan.zero@gmail.com"
__status__ = "Developer"

import re
from tkinter import *
from tkinter import filedialog  # para mostrar de donde viene..

def process(li,md,ch):
	#print(path_s,'--2')
	#print(path_o,'__2') 
	#path=r'C:\Users\Usuario\Documents\proyectos\intercambiador\class_graph.py'
	format_o=''
	
	if re.search('.txt$',path_o):
		format_o='r'
	else: format_o='rb'  
	
	with open(path_o, format_o) as o:
		docuu=None
		if re.search('.txt$',path_o):
			docuu=o.read	()
		else: docuu=o.read().decode()
		#print(docuu,'\n') #>>
		list_exep= li
		c = 0

		

		if list_exep != []:
			for ex in list_exep:
				#print('aaa: ',ex)
				ex = re.sub('\n$', '', ex) # Limpiar elemntos para retirar el '\n' del final
				docuu = docuu.replace('\r\n','\n')
		   	#	if re.search('\n',ex):
			#		rows_process(docuu,ex)
			
				if re.search(re.escape(ex), docuu):
					print('TTTTTTTTTTTTTTTTTT')
					docuu=docuu.replace(ex,'|#°'+str(c)+'°#|')
					c+=1
		c = 0
		#print('\n\n\n----- IMPRIMIR EXCEPCIONES>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n'+docuu,'\n')
		#modif=md.replace(md[-1],'')
		if list_exep == []:
			docuu = docuu.replace('\r\n','\n')  
		modif=re.sub('\n$', '', md)
		print('modif:- ',modif)
		print(repr(modif))

		#change=ch.replace(ch[-1],'')
		change=re.sub('\n$', '', ch)
		print('\n'+'change:- ',change)
		print(repr(change))

		docuu = re.sub(re.escape(modif),change, docuu)

		if list_exep  != []:
			for ex in list_exep:
				#ex = ex.replace(ex[-1],'')
				ex = re.sub('\n$', '', ex)
				print('\n'+'--EX--:', ex,'\n') #>>
				docuu = docuu.replace('|#°'+str(c)+'°#|', ex)
				c+=1

		print('\n\n\n ...... IMPRIMIR CORRECCIÓN******************************************\n\n'+docuu)
		#open_f=filedialog.asksaveasfile(mode='w', defaultextension='.txt')  # asksaveasfilename para obtener directamente 'name'(ruta)
		#print('FLAG')
		#print (path_s , '--3')
		format_s=''
		if re.search('.txt$',path_s):
			format_s='w'
		else: format_s='wb'
		open_f = open(path_s,format_s) # por variar se llama 'path_s' sin pasarlo parametro, no es necesario usar 'global' por que se usa para acceder pro no para modificar 
		#open_f.write(docuu.encode())
		#path_name=open_f.name 
		#print(path_name)
		docuu=docuu.replace('\n','\r\n')
		if re.search('.txt$',path_s):
			open_f.write(docuu) 
		else: open_f.write(docuu.encode())
		#open_f.write(docuu) 


def app_li	():
	global c_ex
	#if T1.get('0.0', END) == 'a'+'\n':
	l_e.append(T1.get('0.0', END))  # 'get' para obtener de Text Widget
	c_ex=c_ex+1
	label_var.set(str(c_ex)+' Save Excepetión')
	print(l_e) #>>
	T1.delete("1.0",END)

def save_f():
	global path_s
	s_f = filedialog.asksaveasfile(title = "Save File",filetypes = (("all files","*.*"),("jpeg files","*.jpg"))) # initialdir = "/", se coloca si se desea que inicie en el directorio raiz, tambien se puede poner el defaultextension ej:'.txt' y mode ej: 'w'
	path_s = s_f.name
	#print(path_s,'--1')
	entry_var2.set(path_s)

def open_f():
	global path_o
	path_o = filedialog.askopenfilename(title = "Open File") # otra forma de hacerlo con 'asksaveasfile' tambien aplica y viceversa.
	#path_o= o_f.name
	#print(path_o,'__1')
	entry_var.set(path_o)

def erase():
	print('BEFORE:',l_e)
	cont=0
	def cancelar():
		w_sec.destroy()
	def oki():
		global c_ex
		R=Te2.get('0.0',END)
		l_e.remove(R)     # parece que si no hay asignacion '=' no es necesario 'global'
		print('AFTER:',l_e)
		c_ex-=1
		label_var.set(str(c_ex)+' Save Excepetión')
		Te2.delete("1.0",END)
	w_sec=Toplevel()
	Te1=Text(w_sec,height= 8, width=28)
	Te1.pack(padx=5, pady=5)
	Te2=Text(w_sec,height= 8, width=28)
	Te2.pack(padx=5, pady=5)
	Button(w_sec, text=' OK ', command=oki).pack(pady=5)
	Button(w_sec, text='CANCEL' , command=cancelar).pack(pady=5)
	for i in l_e:
		#i=re.sub('\n$', '',i) 'Eliminar el '\n' adicional molesto en una iteracion
		cont+=1
		i=str(cont)+'\n'+i+'------------------------'+'\n'
		Te1.insert(END,i)

def close_w():
	root_w.destroy()


root_w = Tk()
l_e=[] 
c_ex=0
path_o=''
path_s=''
label_var=StringVar() # Esta es la unica variable que se debe crear despues del Tk.. las dan igual
label_var.set('---')
entry_var=StringVar()
entry_var2=StringVar()

#root_w.geometry('410x305-500-180') # Si se desea modificar el tamaño de la ventana raiz
frame=Frame()
frame.pack(padx=2, pady=16) # 'pack' se coloca en liena aparte aca para solucionar conflicto con geometry
Label(frame,text='EXCEPTIONS', foreground='blue').grid(row=0, column=0, pady=1)
Label(frame,text='MODIFICATION', foreground='blue').grid(row=0, column=1, pady=1)
Label(frame,text='CHANGE',foreground='blue').grid(row=3, columnspan=2, pady=3) 
#Label(frame,text='---').grid(row=, column=0, pady=1) # Save Sucessfull
Label(frame,textvariable=label_var,foreground='green').grid(row=5, column=0, pady=14) #Change Sucessfull	
T1=Text(frame,height= 10, width=25) 
T1.grid(row=1,column=0, padx=21,pady=5)
Label(frame).grid(row=1, column=1) 
T2=Text(frame,height= 10, width=25)        #Ej: 'T2.get('0.0', END)' para obtener texto insertado en widget 'Text'
T2.grid(row=1, column=1, padx=21, pady=5 )
T3=Text(frame,height=10, width=32)
T3.grid(row=4, columnspan=2, pady=3 ) # aparte para solucionar conflicto con geometry

scroll_1=Scrollbar(frame,orient='vertical',command=T1.yview) #SCROLLS
scroll_1.place(x=200, y=25, height=157)
T1.config(yscrollcommand=scroll_1.set)
#scroll_1.set(400,400)

scroll_2=Scrollbar(frame,orient='vertical',command=T2.yview)
scroll_2.place(x=226, y=25, height=157)
T2.config(yscrollcommand=scroll_2.set)

scroll_3=Scrollbar(frame,orient='vertical',command=T3.yview)
scroll_3.place(x=326, y=212, height=156)
T3.config(yscrollcommand=scroll_3.set)

Entry(frame, textvariable=entry_var).grid(row=7, column=0,pady=7)
Entry(frame, textvariable=entry_var2).grid(row=7, column=1,pady=7)
Button(frame,text='OPEN File', command=open_f).grid(row=6, column=0, padx=25, pady=7)
Button(frame,text='SAVE File', command= save_f).grid(row=6, column=1, padx=25, pady=7)
Button(frame,text='SAVE EXCEPTION', command= app_li).grid(row=8, column=0, padx=25, pady=9)
Button(frame,text='EXECUTE', width=14, command=lambda:process(l_e, T2.get('0.0', END),T3.get('0.0',END) )).grid(row=8 , column=1, padx=10, pady=9)
Button(frame, text= 'Eliminate Excepeton', command= erase).grid(row=5, column=1)
Button(frame,text='Quit',command= close_w, width=13).grid(row=9 , columnspan=2 , pady=7)

root_w.title('SUBSTITU')
root_w.mainloop() 






