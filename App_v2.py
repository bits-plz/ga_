#author => MOHIT KUMAR SINGH
from tkinter import *
from tkinter import font
from mga1 import m_ga1
from tkinter import messagebox
from time import sleep
from PIL import ImageTk,Image
import matplotlib.pyplot as plt
import os
from datetime import datetime
from t_gui import mEntry,mLabel

dirpath="Results"
if not os.path.isdir(dirpath):
    print("creating the directories")
    os.mkdir(dirpath)
    os.chdir("Results")
    os.mkdir("string")
    os.mkdir("math")

    

def loader():
    rp=Tk()
    rp.title("Genetic Algorithm")
    rp.resizable(False,False)
    win_h=300
    win_w=300
    screen_w=rp.winfo_screenwidth()
    screen_h=rp.winfo_screenheight()
    x_=int((screen_w/2)-win_w/2)
    y_=int((screen_h/2)-win_h/2)
    rp.geometry("{}x{}+{}+{}".format(win_w, win_h, x_, y_))
    image=Image.open('im.jpg')
    image=image.resize((300,300),Image.ANTIALIAS)
    imageL=ImageTk.PhotoImage(image)
    load_label=Label(rp,image=imageL)
    load_label.pack()
    for _ in range(500):
        rp.update()
    sleep(2)
    rp.destroy()

#loader()
root=Tk()
root.title("Genetic Algorithm")
win_h=700
win_w=1100
screen_w=root.winfo_screenwidth()
screen_h=root.winfo_screenheight()
x_=int((screen_w/2)-win_w/2)
y_=int((screen_h/2)-win_h/2)
root.geometry("{}x{}+{}+{}".format(win_w, win_h, x_, y_))
root.resizable(False,False)
#mathematical ga
def begin_mga():
    in_it=datetime.now()
    global bs_sol,std,time_t
    try:
        if (m_func.get()!="" and m_nvar.get()!="" and m_varmin.get() != "" and m_varmax.get() !="" and m_maxit.get() !="" and  m_param_max.get()!=""):
            if m_param_pc=='' or m_param_sigma=='' or m_param_mu =='' or m_param_beta=='' or m_pararootmma.get()=='':
                result,stdres,cand=m_ga1(m_func.get(),int(m_nvar.get()),m_varmin.get(),m_varmax.get(),int(m_maxit.get()),int(m_param_max.get()),optimiz_choice.get(),selection_option.get(),t_option.get(),x_option.get()) 
            else:
                result,stdres,cand=m_ga1(m_func.get(),int(m_nvar.get()),m_varmin.get(),m_varmax.get(),int(m_maxit.get()),int(m_param_max.get()),m_param_opt.get(),optimiz_choice.get(),t_option.get(),x_option.get(),float(m_pararootmma.get()),
                            float(m_param_mu.get()),float(m_param_sigma.get()),float(m_param_beta.get()),m_param_pc.get())
            fin_time=datetime.now()
            plt.figure(1)
            plt.plot(result.bestcost)
            plt.xlim(0,int(m_param_max.get()))
            plt.xlabel('Generations')
            plt.ylabel('COST')
            plt.title('mga optimization')
            plt.grid(True)
            res=result.bestsol['cost']
            bs_sol.set(str(res))
            time_t.set(str(fin_time-in_it))
            std.set(str(stdres))
            sol.set(str(cand))
            plt.show()
        else:
            errorm="You must fill all the * params"
            messagebox.showerror('Param fill error',errorm)
    except Exception as e:
        messagebox.showerror('You have entered inappropriate input',e)
    



#labels in root 11
func=mLabel(root,text="Problem function*",row=0, column=0)
nvar=mLabel(root,text="# of vars*[under 20]",row=1, column=0)
varmin=mLabel(root,text="lower bound*",row=2, column=0)
varmax=mLabel(root,text="upper bound*",row=3, column=0)
max_it=mLabel(root,text="# of generations*",row=4, column=0)
param_max=mLabel(root,text="initial population*",row=5, column=0)
pararootmma=mLabel(root,text="Gamma value",row=0, column=2)
param_sigma=mLabel(root,text="σ value",row=1, column=2)
param_beta=mLabel(root,text="β value",row=2, column=2)
params_mu=mLabel(root,text=" µ value",row=3, column=2)
params_pc=mLabel(root,text=" probability count",row=4, column=2)
params_optimization_type=mLabel(root,text="optimization",row=5, column=2)

#entries in root 11
m_func=mEntry(root, width=30,row=0, column=1,ltype=0)
m_nvar=mEntry(root, width=30,row=1, column=1,ltype=0)
m_varmin=mEntry(root, width=30,row=2, column=1,ltype=0)
m_param_max=mEntry(root, width=30,row=5, column=1,ltype=0)
m_varmax=mEntry(root,width=30,row=3,column=1,ltype=0)
m_maxit=mEntry(root,width=30,row=4,column=1,ltype=0)
m_pararootmma=mEntry(root, width=30,row=0, column=3,ltype=1)
m_param_sigma=mEntry(root, width=30,row=1, column=3,ltype=1)
m_param_beta=mEntry(root, width=30,row=2, column=3,ltype=1)
m_param_mu=mEntry(root, width=30,row=3, column=3,ltype=1)
m_param_pc=mEntry(root,width=30,row=4,column=3,ltype=1)
optimiz_choice=StringVar(root)
opt_list=["min","max"]
optimiz_choice.set(opt_list[0])
m_param_opt=OptionMenu(root,optimiz_choice,*opt_list)
m_param_opt.grid(row=5,column=3)



#begin button bound with function begin_mga

s_list=["Roullette","Random","Touranament","Elitism"]
selection_option=StringVar(root)
selection_option.set(s_list[0])
selection_options=OptionMenu(root,selection_option,*s_list)
s_label=Label(root,text="Selection Technique",font=font.Font(family='Helvetica', size=10, weight='bold')).grid(row=6,column=0,pady=10)
selection_options.grid(row=6, column=1, padx=10, pady=10)
x_list=["hc/ic","Three Parent"]
x_option=StringVar(root)
x_option.set(x_list[0])
x_options=OptionMenu(root,x_option,*x_list)
x_label=Label(root,text="Crossover Technique",font=font.Font(family='Helvetica', size=10, weight='bold')).grid(row=6,column=2,pady=10)
x_options.grid(row=6, column=3, padx=10, pady=10)

t_list=["Yes","No"]
t_option=StringVar(root)
t_option.set(t_list[1])
t_options=OptionMenu(root,t_option,*t_list)
s_label=Label(root,text="Thread it?",font=font.Font(family='Helvetica', size=10, weight='bold')).grid(row=7,column=0,pady=10)
t_options.grid(row=7, column=1, padx=10, pady=10)
Best_solution=Label(root,text="best_soln",width=30,font=font.Font(family='Helvetica', size=10, weight='bold')).grid(row=13, column=0, padx=10, pady=10)
bs_sol=StringVar()
bs_sol.set("Optimal Solution")
best_sol=Label(root,textvariable=bs_sol,width=30,font=font.Font(family='Helvetica', size=10))
best_sol.grid(row=13, column=1, padx=10, pady=10)
std=StringVar()
std.set("standard deviation between best \n solutions over the generations")
stddev=Label(root,text="Standard deviation",width=30,font=font.Font(family='Helvetica', size=10, weight='bold')).grid(row=14, column=0, padx=10, pady=10)
best_sol_std=Label(root,textvariable=std,width=30,font=font.Font(family='Helvetica', size=10))
best_sol_std.grid(row=14, column=1, padx=10, pady=10)
sol=StringVar()
sol.set("Best successor will be shown here")
st=Label(root,text="Last offsprings",width=30,height=5,font=font.Font(family='Helvetica', size=10, weight='bold')).grid(row=15, column=0, padx=10, pady=10)
best_sol_pop=Label(root,textvariable=sol,font=font.Font(family='Helvetica', size=10))
best_sol_pop.grid(row=15, column=1, padx=10, pady=10)
time_taken=Label(root,text="Time Taken",width=30,height=5,font=font.Font(family='Helvetica', size=10, weight='bold')).grid(row=16, column=0, padx=10, pady=10)
time_t=StringVar()
time_t.set("Time taken will be shown here")
tt_ta=best_sol_pop=Label(root,textvariable=time_t,font=font.Font(family='Helvetica', size=10))
tt_ta.grid(row=16, column=1, padx=10, pady=10)
buttonm = Button(root, text="RUN GA", command=begin_mga,font=font.Font(family='Helvetica', size=20,weight='bold'),cursor='pirate')
buttonm.configure(activebackground='grey',activeforeground='white',background='black',foreground='white',relief='solid')
def on_enter(e):
    buttonm['background']='red'
    buttonm['foreground']='white'
def on_leave(e):
    buttonm['background']='black'
    buttonm['foreground']='white'
buttonm.grid(row=16, column=3, padx=10, pady=10)
buttonm.bind('<Enter>',on_enter)
buttonm.bind('<Leave>',on_leave)

#the main loop
root.mainloop()


