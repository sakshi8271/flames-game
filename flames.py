from tkinter import *
def match(l1,l2):
    for i in range(len(l1)):
        for j in range(len(l2)):
            if l1[i]==l2[j]:
                c=l1[i]
                l1.remove(c)
                l2.remove(c)
                l3 = l1+["*"]+l2
                return [l3, True]
    l3=l1+["*"]+l2
    return [l3,False]
def clear():
    player1.delete(0,END)
    player2.delete(0,END)
    statusf.delete(0,END)
    p1.focus_set()
def status():
    p1=player1.get()
    p1=p1.lower()
    p1.replace(" ","")
    p1_list=list(p1)
    p2=player2.get()
    p2=p2.lower()
    p2.replace(" ","")
    p2_list=list(p2)
    flag = True
    while flag:
        rlist=match(p1_list,p2_list)
        clist=rlist[0]
        flag=rlist[1]
        slist=clist.index("*")
        p1_list=clist[:slist]
        p2_list=clist[slist+1:]
    count=len(p1_list)+len(p2_list)
    result=["Friends" , "Love" , "Marriage" , "Enemy" , "Siblings" , "Affection"]
    while len(result)>1:
        split_index=(count % len(result)-1)
        if split_index>=0:
            right=result[split_index + 1:]
            left=result[ : split_index]
            result=right+left
        else:
            result=result[:len(result)-1]
    statusf.insert(10,result[0])


if __name__ == "__main__":
    # Create a GUI window
    root = Tk()

    # Set the background colour of GUI window
    root.configure(background='pink')

    # Set the configuration of GUI window
    root.geometry("350x125")

    # set the name of tkinter GUI window
    root.title("Flames Game")

    # Create a Player 1 Name: label
    label1 = Label(root, text="Player 1 Name: ",
                   fg='black', bg='lightblue')

    # Create a Player 2 Name: label
    label2 = Label(root, text="Player 2 Name: ",
                   fg='black', bg='lightblue')

    # Create a Relation Status: label
    label3 = Label(root, text="Relationship Status: ",
                   fg='black', bg='lightblue')

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    label1.grid(row=1, column=0, sticky="E")
    label2.grid(row=2, column=0, sticky="E")
    label3.grid(row=4, column=0, sticky="E")

    # Create a text entry box
    # for filling or typing the information.
    player1 = Entry(root)
    player2 = Entry(root)
    statusf = Entry(root)

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    # ipadx keyword argument set width of entry space .
    player1.grid(row=1, column=1, ipadx="50")
    player2.grid(row=2, column=1, ipadx="50")
    statusf.grid(row=4, column=1, ipadx="50")

    # Create a Submit Button and attached
    # to tell_status function
    button1 = Button(root, text="Submit", bg="grey",
                     fg="black", command=status)

    # Create a Clear Button and attached
    # to clear_all function
    button2 = Button(root, text="Clear", bg="grey",
                     fg="black", command=clear)

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    button1.grid(row=3, column=1)
    button2.grid(row=5, column=1)

    # Start the GUI
    root.mainloop()





