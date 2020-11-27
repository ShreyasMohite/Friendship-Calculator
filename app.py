from tkinter import *
import tkinter.messagebox


class Friendships:
    def __init__(self,root):
        self.root=root
        self.root.title("Friendship Calculator")
        self.root.geometry("350x350")
        self.root.iconbitmap("logo788.ico")
        self.root.resizable(0,0)


        firstname=StringVar()
        secondname=StringVar()


        def on_enter1(e):
            but_calculate['background']="black"
            but_calculate['foreground']="cyan"
            
            

        def on_leave1(e):
            but_calculate['background']="SystemButtonFace"
            but_calculate['foreground']="SystemButtonText"


        def on_enter2(e):
            but_clear['background']="black"
            but_clear['foreground']="cyan"
            
            

        def on_leave2(e):
            but_clear['background']="SystemButtonFace"
            but_clear['foreground']="SystemButtonText"



        def clear():
            firstname.set("")
            secondname.set("")
            lab_fname.config(text="")
            lab_ffname.config(text="")
            lab_sname.config(text="")
            lab_ssname.config(text="")
            lab_friend.config(text="")
            lab_frienship.config(text="")


        def calculate_friendship():
            if firstname.get()!="":
                if secondname.get()!="":
                    alphabets="bcqhjklmpqrtwxyz"
                    score=0
                    name1=firstname.get()
                    name2=secondname.get()
                    names=name1+" "+name2
                    for chars in names:
                        if chars in 'aeiou':
                            score+=5
                        if chars in 'friends':
                            score+=10
                        if chars in alphabets:
                            score+=alphabets.find(chars)
                        else:
                            score+=0
                    if score>=80:
                        lab_fname.config(text="Firstname")
                        lab_ffname.config(text=name1)
                        lab_sname.config(text="Secondname")
                        lab_ssname.config(text=name2)
                        lab_friend.config(text="Friendship calculator")
                        lab_frienship.config(text=score)
                        
                    else:
                        print("your frindship score is :",score)
                else:
                    tkinter.messagebox.showerror("Error","Please Enter Second Name")        
            else:
                tkinter.messagebox.showerror("Error","Please Enter First Name")




#================frame=========================#
        
        mainframe=Frame(self.root,width=350,height=350,relief="ridge",bd=3,bg="gray88")
        mainframe.place(x=0,y=0)

#===============================================================================#
        
        firstlab=Label(mainframe,text="Enter First Name",font=('times new roman',14),bg="gray88")
        firstlab.place(x=100,y=10)

        ent_firstname=Entry(mainframe,width=30,font=('times new roman',14),relief="ridge",bd=3,textvariable=firstname)
        ent_firstname.place(x=30,y=35)

        secondlab=Label(mainframe,text="Enter Second Name",font=('times new roman',14),bg="gray88")
        secondlab.place(x=100,y=80)

        ent_secondname=Entry(mainframe,width=30,font=('times new roman',14),relief="ridge",bd=3,textvariable=secondname)
        ent_secondname.place(x=30,y=105)

        lab_fname=Label(mainframe,text="",font=('times new roman',14),bg="gray88")
        lab_fname.place(x=0,y=150)

        lab_ffname=Label(mainframe,text="",font=('times new roman',14),bg="gray88",fg="green")
        lab_ffname.place(x=0,y=180)

        lab_sname=Label(mainframe,text="",font=('times new roman',14),bg="gray88")
        lab_sname.place(x=240,y=150)

        lab_ssname=Label(mainframe,text="",font=('times new roman',14),bg="gray88",fg="green")
        lab_ssname.place(x=240,y=180)

        lab_friend=Label(mainframe,text="",font=('times new roman',14),bg="gray88")
        lab_friend.place(x=90,y=210)

        lab_frienship=Label(mainframe,text="",font=('times new roman',20),bg="gray88",fg="red")
        lab_frienship.place(x=140,y=240)




        but_calculate=Button(mainframe,text="Calculate",width=13,font=('times new roman',14),cursor="hand2",command=calculate_friendship)
        but_calculate.place(x=15,y=300)
        but_calculate.bind("<Enter>",on_enter1)
        but_calculate.bind("<Leave>",on_leave1)


        but_clear=Button(mainframe,text="Clear",width=13,font=('times new roman',14),cursor="hand2",command=clear)
        but_clear.place(x=190,y=300)
        but_clear.bind("<Enter>",on_enter2)
        but_clear.bind("<Leave>",on_leave2)




if __name__ == "__main__":
    root=Tk()
    Friendships(root)
    root.mainloop()