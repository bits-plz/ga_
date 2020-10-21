#author => MOHIT KUMAR SINGH
from tkinter import *
from tkinter import ttk
from tkinter import font
from ga_ import gastr
from mga1 import m_ga2
from tkinter import messagebox
from time import sleep
from PIL import ImageTk,Image
import matplotlib.pyplot as plt
import os
from datetime import datetime

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
    for _ in range(1000):
        rp.update()
    sleep(2)
    rp.destroy()

loader()
root=Tk()
root.title("Genetic Algorithm")
win_h=700
win_w=1000
screen_w=root.winfo_screenwidth()
screen_h=root.winfo_screenheight()
x_=int((screen_w/2)-win_w/2)
y_=int((screen_h/2)-win_h/2)
root.geometry("{}x{}+{}+{}".format(win_w, win_h, x_, y_))
_ga=ttk.Notebook(root)
_ga.pack(pady=10)
s_ga=Frame(_ga,width=700,height=400)
m_ga=Frame(_ga,width=1000,height=700,bg="blue")
h_ga=Frame(_ga,width=1000,height=600)
about_ga=Frame(_ga,width=1000,height=600)


#string ga
labelS = Label(s_ga, text="Enter Target String", width=30,font=font.Font(family='Helvetica', size=12, weight='bold')).grid(row=0, column=0, padx=10, pady=10)
popu_ = Label(s_ga, text="Enter the population Size", width=30,font=font.Font(family='Helvetica', size=12, weight='bold')).grid(row=1, column=0, padx=10, pady=10)
gen_ = Label(s_ga, text="Enter number of generations",width=30,font=font.Font(family='Helvetica', size=12, weight='bold')).grid(row=2, column=0, padx=10, pady=10)
k_ = Label(s_ga, text="Enter the fitness criteria",width=30,font=font.Font(family='Helvetica', size=12, weight='bold')).grid(row=3, column=0, padx=10, pady=10)
String_test = Entry(s_ga, width=30)
String_test.grid(row=0, column=1, padx=10, pady=10)
String_popy = Entry(s_ga, width=30)
String_popy.grid(row=1, column=1, padx=10, pady=10)
String_gen = Entry(s_ga, width=30)
String_gen.grid(row=2, column=1, padx=10, pady=10)
String_k = Entry(s_ga, width=30)
String_k.grid(row=3, column=1, padx=10, pady=10)


def begin_ga():
    in_str = String_test.get()
    in_str_len = len(String_test.get())
    if(String_test.get() !=""  and String_popy.get()!="" and String_test.get()!=""):
        population = int(String_popy.get())
        generations = int(String_gen.get())
        k = int(String_k.get())
        sp=gastr(in_str,in_str_len,population,generations,k)
        if sp=="threshold couldn't be reached":
            messagebox.showwarning("Threshold unmet","threshold couldn't be reached try putting a lower value of it or try again")
    else:
        messagebox.showerror("param fill error","you must fill all the parameters")
button = Button(s_ga, text="BEGIN", command=begin_ga)
button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)




#mathematical ga
def begin_mga():
    in_it=datetime.now()
    global bs_sol,std,time_t
    try:
        if (m_func.get()!="" and m_nvar.get()!="" and m_varmin.get() != "" and m_varmax.get() !="" and m_maxit.get() !="" and  m_param_max.get()!=""):
            if m_param_pc=='' or m_param_sigma=='' or m_param_mu =='' or m_param_beta=='' or m_param_gamma.get()=='':
                result,stdres,cand=m_ga2(m_func.get(),int(m_nvar.get()),m_varmin.get(),m_varmax.get(),int(m_maxit.get()),int(m_param_max.get()),optimiz_choice.get(),selection_option.get(),t_option.get()) 
            else:
                result,stdres,cand=m_ga2(m_func.get(),int(m_nvar.get()),m_varmin.get(),m_varmax.get(),int(m_maxit.get()),int(m_param_max.get()),m_param_opt.get(),optimiz_choice.get(),t_option.get(),float(m_param_gamma.get()),
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
    



#labels in m_ga 11
func=Label(m_ga,text="Problem function*",width=30,font=font.Font(family='Helvetica', size=10, weight='bold')).grid(row=0, column=0, padx=10, pady=10)
nvar=Label(m_ga,text="# of vars*[under 20]",width=30,font=font.Font(family='Helvetica', size=10, weight='bold')).grid(row=1, column=0, padx=10, pady=10)
varmin=Label(m_ga,text="lower bound*",width=30,font=font.Font(family='Helvetica', size=10, weight='bold')).grid(row=2, column=0, padx=10, pady=10)
varmax=Label(m_ga,text="upper bound*",width=30,font=font.Font(family='Helvetica', size=10, weight='bold')).grid(row=3, column=0, padx=10, pady=10)
max_it=Label(m_ga,text="# of generations*",width=30,font=font.Font(family='Helvetica', size=10, weight='bold')).grid(row=4, column=0, padx=10, pady=10)
param_max=Label(m_ga,text="initial population*",width=30,font=font.Font(family='Helvetica', size=10, weight='bold')).grid(row=5, column=0, padx=10, pady=10)
param_gamma=Label(m_ga,text="Gamma value",width=30,font=font.Font(family='Helvetica', size=10, weight='bold')).grid(row=0, column=2, padx=10, pady=10)
param_sigma=Label(m_ga,text="σ val",width=30,font=font.Font(family='Helvetica', size=10, weight='bold')).grid(row=1, column=2, padx=10, pady=10)
param_beta=Label(m_ga,text="β value",width=30,font=font.Font(family='Helvetica', size=10, weight='bold')).grid(row=2, column=2, padx=10, pady=10)
params_mu=Label(m_ga,text=" µ value",width=30,font=font.Font(family='Helvetica', size=10, weight='bold')).grid(row=3, column=2, padx=10, pady=10)
params_pc=Label(m_ga,text=" probability count",width=30,font=font.Font(family='Helvetica', size=10, weight='bold')).grid(row=4, column=2, padx=10, pady=10)
params_optimization_type=Label(m_ga,text="optimization",width=30,font=font.Font(family='Helvetica', size=10, weight='bold')).grid(row=5, column=2, padx=10, pady=10)

#entries in m_ga 11
m_func=Entry(m_ga, width=30)
m_func.grid(row=0, column=1, padx=10, pady=10)
m_nvar=Entry(m_ga, width=30)
m_nvar.grid(row=1, column=1, padx=10, pady=10)
m_varmin=Entry(m_ga, width=30)
m_varmin.grid(row=2, column=1, padx=10, pady=10)
m_param_max=Entry(m_ga, width=30)
m_varmax=Entry(m_ga,width=30)
m_varmax.grid(row=3,column=1,padx=10,pady=10)
m_maxit=Entry(m_ga,width=30)
m_maxit.grid(row=4,column=1,padx=10, pady=10)
m_param_max.grid(row=5, column=1, padx=10, pady=10)
m_param_gamma=Entry(m_ga, width=30)
m_param_gamma.grid(row=0, column=3, padx=10, pady=10)
m_param_sigma=Entry(m_ga, width=30)
m_param_sigma.grid(row=1, column=3, padx=10, pady=10)
m_param_beta=Entry(m_ga, width=30)
m_param_beta.grid(row=2, column=3, padx=10, pady=10)
m_param_mu=Entry(m_ga, width=30)
m_param_mu.grid(row=3, column=3, padx=10, pady=10)
m_param_pc=Entry(m_ga,width=30)
m_param_pc.grid(row=4,column=3)
optimiz_choice=StringVar(m_ga)
opt_list=["min","max"]
optimiz_choice.set(opt_list[0])
m_param_opt=OptionMenu(m_ga,optimiz_choice,*opt_list)
m_param_opt.grid(row=5,column=3)



#begin button bound with function begin_mga

s_list=["Roullette","Random","Touranament"]
selection_option=StringVar(m_ga)
selection_option.set(s_list[0])
selection_options=OptionMenu(m_ga,selection_option,*s_list)
s_label=Label(m_ga,text="Selection Technique",font=font.Font(family='Helvetica', size=10, weight='bold')).grid(row=6,column=0,pady=10)
selection_options.grid(row=6, column=1, padx=10, pady=10)

t_list=["Yes","No"]
t_option=StringVar(m_ga)
t_option.set(t_list[0])
t_options=OptionMenu(m_ga,t_option,*t_list)
s_label=Label(m_ga,text="Thread it?",font=font.Font(family='Helvetica', size=10, weight='bold')).grid(row=6,column=2,pady=10)
t_options.grid(row=6, column=3, padx=10, pady=10)
Best_solution=Label(m_ga,text="best_soln",width=30,font=font.Font(family='Helvetica', size=10, weight='bold')).grid(row=13, column=0, padx=10, pady=10)
bs_sol=StringVar()
bs_sol.set("cost")
best_sol=Label(m_ga,textvariable=bs_sol,width=30,font=font.Font(family='Helvetica', size=10))
best_sol.grid(row=13, column=1, padx=10, pady=10)
std=StringVar()
std.set("std")
stddev=Label(m_ga,text="Standard deviation",width=30,font=font.Font(family='Helvetica', size=10, weight='bold')).grid(row=14, column=0, padx=10, pady=10)
best_sol_std=Label(m_ga,textvariable=std,width=30,font=font.Font(family='Helvetica', size=10))
best_sol_std.grid(row=14, column=1, padx=10, pady=10)
sol=StringVar()
sol.set("offsprings")
st=Label(m_ga,text="Last offsprings",width=30,height=5,font=font.Font(family='Helvetica', size=10, weight='bold')).grid(row=15, column=0, padx=10, pady=10)
best_sol_pop=Label(m_ga,textvariable=sol,font=font.Font(family='Helvetica', size=10))
best_sol_pop.grid(row=15, column=1, padx=10, pady=10)
time_taken=Label(m_ga,text="Time Taken",width=30,height=5,font=font.Font(family='Helvetica', size=10, weight='bold')).grid(row=16, column=0, padx=10, pady=10)
time_t=StringVar()
time_t.set("Time taken will be shown here")
tt_ta=best_sol_pop=Label(m_ga,textvariable=time_t,font=font.Font(family='Helvetica', size=10))
tt_ta.grid(row=16, column=1, padx=10, pady=10)
buttonm = Button(m_ga, text="BEGIN", command=begin_mga,bg="red")
buttonm.grid(row=16, column=2, padx=10, pady=10)
help_main="This is the help guide for using the application\n String ga :"
help_str="\n 1.Enter the target string in it's respective entry\n 2.Enter the population[anything >0]\n 3.Enter the number of generations.\n 4.Enter the fitness index [a positive number less than 100,greater than 0]\n5.Run the string matching program by clicking on BEGIN button\n"
help_mga_heading="Mathematical ga:\n"
help_mga="All the entries are at right to their corresponding parameter names\n1.Enter the problem function\n2.Enter the number of variables\n3.Enter the lower bounds of the variable in comma separated fashion, likewise enter the upper bounds\n4.Enter the number of generations\n5.Enter the initial population\n6.Enter the type of optimization(`max`,`min`)[default is max]\n7.Run the program by clicking on BEGIN button\n If you wish to tweak the resulting graph, you need to enter all \n the parameters onto the right\n with following constraints,gamma,beta,pc,mu,sigma∈[0,1] \nwhich are defaulted to [0.1,1,1,0,1,0,1] respectively"
help_errors="While there will be no errors in mga,\n sometimes it takes a lot of time because of huge calculations.\nAlso if you see any error message just follow the instruction in the box.\n In string ga it may happen that you will not be able to attain \n the threshold at one time but if you try running it again it might\n because of random algorithms involved"

h_sga=Label(h_ga,text=help_str,width=80,font=font.Font(family='Consolas',size=10)).grid(row=2,column=1,padx=2)
h_sga=Label(h_ga,text=help_main,width=80,font=font.Font(family='Consolas',size=20,weight='bold')).grid(row=1,column=1,padx=2)
h_sga=Label(h_ga,text=help_mga_heading,width=80,font=font.Font(family='Consolas',size=20,weight='bold')).grid(row=3,column=1,padx=2)
h_sga=Label(h_ga,text=help_mga,width=80,font=font.Font(family='Consolas',size=10)).grid(row=4,column=1,padx=2)
h_sga=Label(h_ga,text="Errors",width=80,font=font.Font(family='Consolas',size=20,weight='bold')).grid(row=5,column=1,padx=2)
h_sga=Label(h_ga,text=help_errors,width=80,font=font.Font(family='Consolas',size=10)).grid(row=6,column=1,padx=2)





ab_ga=Label(about_ga,text="Uses tkinter,ypstruct,matplotlib,numpy,simple-eval,Pillow \n Thanks to yarpiz \n version 1.0.0",font=font.Font(family="Consolas",size=20,weight="bold"),width=80).grid(row=1,column=1,padx=2)
ab_ga=Label(about_ga,text="Results stored in Results folder , string ga -> string ,mathematical ga-> math",font=font.Font(family="Consolas",size=12,weight="bold"),width=80).grid(row=2,column=1,padx=2)
ab_ga=Label(about_ga,text="Made with using python",font=font.Font(family="Consolas",size=10,weight="bold"),width=80).grid(row=4,column=1,padx=2)









#packing both frames

s_ga.pack(fill=BOTH,expand=1)
m_ga.pack(fill=BOTH,expand=1)
h_ga.pack(fill=BOTH,expand=1)
about_ga.pack(fill=BOTH,expand=1)
_ga.add(s_ga,text="Strings")
_ga.add(m_ga,text="Mathematical")
_ga.add(h_ga,text="Help")
_ga.add(about_ga,text="About")

#the main loop
root.mainloop()


