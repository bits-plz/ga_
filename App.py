#author => MOHIT KUMAR SINGH
from tkinter import *
from tkinter import ttk
from tkinter import font
from ga_ import gastr
from mga1 import m_ga1
from tkinter import messagebox
from time import sleep
from PIL import ImageTk,Image
import matplotlib.pyplot as plt


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
win_w=1200
screen_w=root.winfo_screenwidth()
screen_h=root.winfo_screenheight()
x_=int((screen_w/2)-win_w/2)
y_=int((screen_h/2)-win_h/2)
root.geometry("{}x{}+{}+{}".format(win_w, win_h, x_, y_))
_ga=ttk.Notebook(root)
_ga.pack(pady=15)
s_ga=Frame(_ga,width=900,height=400)
m_ga=Frame(_ga,width=900,height=700,bg="blue")


#string ga
labelS = Label(s_ga, text="Enter Test String", width=30,font=font.Font(family='Helvetica', size=12, weight='bold')).grid(row=0, column=0, padx=10, pady=10)
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
        gastr(in_str,in_str_len,population,generations,k)
    else:
        messagebox.showerror("param fill error","you must fill all the parameters")
button = Button(s_ga, text="BEGIN", command=begin_ga)
button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)




#mathematical ga
def begin_mga():
    global bs_sol,std
    try:
        if (m_func.get()!="" and m_nvar.get()!="" and m_varmin.get() != "" and m_varmax.get() !="" and m_maxit.get() !="" and  m_param_max.get()!=""):
            if m_param_pc=='' or m_param_sigma=='' or m_param_mu =='' or m_param_beta=='' or m_param_gamma.get()=='':
                result,stdres,cand=m_ga1(m_func.get(),int(m_nvar.get()),m_varmin.get(),m_varmax.get(),int(m_maxit.get()),int(m_param_max.get()),m_param_opt.get()) 
            else:
                result,stdres,cand=m_ga1(m_func.get(),int(m_nvar.get()),m_varmin.get(),m_varmax.get(),int(m_maxit.get()),int(m_param_max.get()),m_param_opt.get(),float(m_param_gamma.get()),
                            float(m_param_mu.get()),float(m_param_sigma.get()),float(m_param_beta.get()),m_param_pc.get())
            plt.figure(1)
            plt.plot(result.bestcost)
            plt.xlim(0,int(m_param_max.get()))
            plt.xlabel('Generations')
            plt.ylabel('COST')
            plt.title('Genetic algorithm')
            plt.grid(True)
            res=result.bestsol['cost']
            bs_sol.set(str(res))
            std.set(str(stdres))
            sol.set(str(cand))
            plt.show()
        else:
            errorm="You must fill all the * params"
            messagebox.showerror('Param fill error',errorm)
    except Exception as e:
        messagebox.showerror('You have entered inappropriate input',e)
    



#labels in m_ga 11
func=Label(m_ga,text="Problem function",width=30,font=font.Font(family='Helvetica', size=10, weight='bold')).grid(row=0, column=0, padx=10, pady=10)
nvar=Label(m_ga,text="# of vars*[under 20]",width=30,font=font.Font(family='Helvetica', size=10, weight='bold')).grid(row=1, column=0, padx=10, pady=10)
varmin=Label(m_ga,text="lower bound*",width=30,font=font.Font(family='Helvetica', size=10, weight='bold')).grid(row=2, column=0, padx=10, pady=10)
varmax=Label(m_ga,text="upper bound*",width=30,font=font.Font(family='Helvetica', size=10, weight='bold')).grid(row=3, column=0, padx=10, pady=10)
max_it=Label(m_ga,text="# of generations*",width=30,font=font.Font(family='Helvetica', size=10, weight='bold')).grid(row=4, column=0, padx=10, pady=10)
param_max=Label(m_ga,text="initial population",width=30,font=font.Font(family='Helvetica', size=10, weight='bold')).grid(row=5, column=0, padx=10, pady=10)
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
m_param_opt=Entry(m_ga,width=30)
m_param_opt.grid(row=5,column=3)



#begin button bound with function begin_mga
buttonm = Button(m_ga, text="BEGIN", command=begin_mga,bg="red")
buttonm.grid(row=6, column=1, columnspan=2, padx=10, pady=10)

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

#packing both frames

s_ga.pack(fill=BOTH,expand=1)
m_ga.pack(fill=BOTH,expand=1)
_ga.add(s_ga,text="Strings")
_ga.add(m_ga,text="Mathematical")
#the main loop
root.mainloop()


