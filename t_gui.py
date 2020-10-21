from tkinter import *
from tkinter import font

class mEntry(Entry):
    def __init__(self,master ,row, column,ltype,**kw):
        Entry.__init__(self,master=master,**kw)
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
        self['font']=font.Font(family='Helvetica', size=10)
        self.row=row
        self.column=column
        self.padx=0
        self.pady= 0
        self.ipadx=2
        self.ipady=2
        self.ltype=ltype
        self.grid(row=self.row,column=self.column,padx=self.padx,pady=self.pady,ipady=self.ipady,ipadx=self.ipadx)

    def on_enter(self, e):
        self['background'] = 'blue'
        self['foreground'] = 'white'
        self['insertbackground']='white'
        if self.ltype==0:
            st=self.get()
            self.delete(0,END)
            self['font']=font.Font(family='Helvetica', size=11)
            self.insert(0,st)
            self.grid(row=self.row,column=self.column,padx=self.padx,pady=self.pady,ipady=self.ipady+1,ipadx=self.ipadx)

    def on_leave(self, e):
        self['background'] = 'white' 
        self['foreground'] = 'black'
        self['insertbackground']='black' 
        if self.ltype==0:
            st=self.get()
            self.delete(0,END)
            self['font']=font.Font(family='Helvetica', size=10)
            self.insert(0,st)
            self.grid(row=self.row,column=self.column,padx=self.padx,pady=self.pady,ipady=self.ipady,ipadx=self.ipadx)


class mLabel(Label):
    def __init__(self,master,row,column,**kw):
        Label.__init__(self,master=master,width=30,**kw)
        self['font']=font.Font(family='Helvetica', size=10, weight='bold')
        self.grid(row=row,column=column,padx=10, pady=10)
