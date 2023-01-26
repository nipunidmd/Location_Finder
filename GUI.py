from tkinter import *
import tkinter as tk
from tkinter import ttk
from CampusLocationModel import CampusLocationModel

# Application 2 - With GUI

# fonts
LARGE_FONT= ("Verdana", 12)
SMALL_FONT= ("Verdana", 10)

# location details
out1 = CampusLocationModel.locationDetails()

# location classification list
out2 = CampusLocationModel.buildingClassifications()

class GUI(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)

        # tk.Tk.iconbitmap(self,default='clienticon.ico')
        tk.Tk.wm_title(self, "Keele Building Finder")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}

        for F in (HomePage, NameSearch, RefSearch, ClsSearch):

            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(HomePage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()
        
        # background color
        frame.configure(bg='#effffa')

# Home Page 
class HomePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        
        label = ttk.Label(self, text="Keele Buildings & Locations", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        label2 = ttk.Label(self, text="Select one of the following options to find a building/location")
        label2.pack()

        # button options
        button = ttk.Button(self, text="Search by Name",
                            command=lambda: controller.show_frame(NameSearch))
        button.pack()

        button2 = ttk.Button(self, text="Search by Reference",
                            command=lambda: controller.show_frame(RefSearch))
        button2.pack()

        button3 = ttk.Button(self, text="Search by Classification",
                            command=lambda: controller.show_frame(ClsSearch))
        button3.pack()

        # home page image
        self.backGroundImage = PhotoImage(file="bg.png")
        self.backGroundImageLabel = Label(self, image=self.backGroundImage)
        self.backGroundImageLabel.pack()

# Search By Name
class NameSearch(tk.Frame):
    
    def __init__(self, parent, controller):

        self.result = None
        self.label1 = None
        tk.Frame.__init__(self, parent)
        # option variable (Search by Name - Option 1)
        opt = 1
        label = ttk.Label(self, text="Enter Full or Part of the Building Name", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        Bname = tk.Text(self, borderwidth=0, highlightthickness=0, width=22, height=1)
        Bname.pack()
        
        search = ttk.Button(self, text="Search",
                            command=lambda: searchBuilding(opt,Bname,out1,result,label,self.selected_text))
        search.pack()

        scrollbar = Scrollbar(self)
        scrollbar.pack(side=RIGHT, fill=Y)

        result = tk.Listbox(self,height=13,width=75,font=SMALL_FONT)
        result.pack()

        result.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=result.yview)

        # use left mouse click on a list item to display selection
        result.bind('<ButtonRelease-1>', self.on_click_listbox)
        
        self.selected_text = tk.StringVar()
        label1 = tk.Label(self, textvariable=self.selected_text, font="Helvetica 10 bold", anchor='w', background='lightblue')
        # label1 = tk.Label(self,text='Click building/location to select', width=30)
        label1.pack()

        # cursor selection into 'cs' variable
        cs = result.curselection()

        self.selected_text.set(cs)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: [controller.show_frame(HomePage),pageChange(opt,label,self.selected_text,result)])
        button1.pack()

        button2 = ttk.Button(self, text="Search by Reference",
                            command=lambda: [controller.show_frame(RefSearch),pageChange(opt,label,self.selected_text,result)])
        button2.pack()

        button3 = ttk.Button(self, text="Search by Classification",
                            command=lambda: [controller.show_frame(ClsSearch),pageChange(opt,label,self.selected_text,result)])
        button3.pack()

    # get user selection from listbox and assign it to label1
    def on_click_listbox(self,event):
        
        # get selected line index
        widget = event.widget
        index = widget.curselection()

        # get the line's text
        seltext = widget.get(index)

        # set slected text in to label
        self.selected_text.set(seltext)

# Search By Reference Number
class RefSearch(tk.Frame):

    def __init__(self, parent, controller):
        
        self.result = None
        self.label1 = None
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Enter Full or Part of the Building Reference Number", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        # option variable (Search by Reference Number - Option 2)
        opt = 2

        # building reference text input
        Bref = tk.Text(self, borderwidth=0, highlightthickness=0, width=22, height=1)
        Bref.pack()

        # search buttons
        search = ttk.Button(self, text="Search",
                            command=lambda: searchBuilding(opt,Bref,out1,result,label,self.selected_text))
        search.pack()

        scrollbar = Scrollbar(self)
        scrollbar.pack(side=RIGHT, fill=Y)

        # result listbox
        result = tk.Listbox(self,height=13,width=75,font=SMALL_FONT)
        result.pack()
    
        result.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=result.yview)
        
        # use left mouse click on a list item to display selection
        result.bind('<ButtonRelease-1>', self.on_click_listbox)
        
        self.selected_text = tk.StringVar()
        label1 = tk.Label(self, textvariable=self.selected_text, font="Helvetica 10 bold", anchor='w', background='lightblue')
        # label1 = tk.Label(self,text='Click building/location to select', width=30)
        label1.pack()

        # cursor selection into 'cs' variable
        cs = result.curselection()
        self.selected_text.set(cs)
        
        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: [controller.show_frame(HomePage),pageChange(opt,label,self.selected_text,result)])
        button1.pack()

        button2 = ttk.Button(self, text="Search by Name",
                            command=lambda: [controller.show_frame(NameSearch),pageChange(opt,label,self.selected_text,result)])
        button2.pack()

        button3 = ttk.Button(self, text="Search by Classification",
                            command=lambda: [controller.show_frame(ClsSearch),pageChange(opt,label,self.selected_text,result)])
        button3.pack()
        
    # used https://stackoverflow.com/questions/7616541/get-selected-item-in-listbox-and-call-another-function-storing-the-selected-for#:~:text=The%20best%20way%20to%20get%20the%20selected%20item,pointer%20is%20what%20will%20be%20returned%20as%20item.
    # get user selection from listbox and assign it to label1
    def on_click_listbox(self,event):
        
        # get selected line index
        widget = event.widget
        index = widget.curselection()

        # get the line's text
        seltext = widget.get(index)

        # set slected text in to label
        self.selected_text.set(seltext)

# Search by Classification
class ClsSearch(tk.Frame):

    def __init__(self, parent, controller):

        self.result = None
        self.label1 = None
        
        tk.Frame.__init__(self, parent)

        # option variable (Search by Classification - Option 3)
        opt = 3
        
        label = ttk.Label(self, text="Select a Building/Location Classification", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        Bcls= ttk.Combobox(self)
        Bcls['values']= out2
        Bcls['state']= 'readonly'
        Bcls.set('Select an option')
        Bcls.pack()

        search = ttk.Button(self, text="Search",
                            command=lambda: searchBuilding(opt,Bcls,out1,result,label,self.selected_text))
        search.pack()

        scrollbar = Scrollbar(self)
        scrollbar.pack(side=RIGHT, fill=Y)

        result = tk.Listbox(self,height=13,width=75,font=SMALL_FONT)
        result.pack()

        result.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=result.yview)

        # use left mouse click on a list item to display selection
        result.bind('<ButtonRelease-1>', self.on_click_listbox)
        
        self.selected_text = tk.StringVar()
        label1 = tk.Label(self, textvariable=self.selected_text, font="Helvetica 10 bold", anchor='w', background='lightblue')
        # label1 = tk.Label(self,text='Click building/location to select', width=30)
        label1.pack()

        button100 = ttk.Button(self, text="Back to Home",
                            command=lambda: [controller.show_frame(HomePage),pageChange(opt,label,self.selected_text,result)])
        button100.pack()

        # cursor selection into 'cs' variable
        cs = result.curselection()
        self.selected_text.set(cs)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: [controller.show_frame(HomePage),pageChange(opt,label,self.selected_text,result)])
        button1.pack()

        button2 = ttk.Button(self, text="Search by Name",
                            command=lambda: [controller.show_frame(NameSearch),pageChange(opt,label,self.selected_text,result)])
        button2.pack()

        button3 = ttk.Button(self, text="Search by Reference",
                            command=lambda: [controller.show_frame(RefSearch),pageChange(opt,label,self.selected_text,result)])
        button3.pack()

    # get user selection from listbox and assign it to label1
    def on_click_listbox(self,event):
        
        # get selected line index
        widget = event.widget
        index = widget.curselection()

        # get the line's text
        seltext = widget.get(index)

        # set slected text in to label
        self.selected_text.set(seltext)
        

# Search Building/Location Method
def searchBuilding(opt,param,out1,result,label,selected_text):
    
    # set and clear necessary values for input text boxes
    if(opt == 3):
        input_value = param.get()
        param.set('Select an option')
    else:
        input_value = param.get("1.0",'end-1c')
        param.delete(1.0, tk.END)

    # get and clear result list box
    rslt = result.get(0, END)
    result.delete(0, END)
    selected_text.set('')

    # results count variable
    count = 0
    # result.insert(tk.END,"----------------------------------Building Details-------------------------------------"+'\n\n')
    for line in out1:        
        # search
        if(opt == 1):
            
            if(input_value == ''):
                result.insert(tk.END,"Please enter a building/location name")
                break
            else:
                if input_value.casefold() in line[1].casefold():
                    count +=1
                    result.insert(tk.END, "Ref:"+line[0]+'\t'+"  Name:"+line[1]+'\t\t'+"   Classification:"+line[2]+'\n')
                
        elif(opt == 2):
            if(input_value == ''):
                result.insert(tk.END,"Please enter a building/location reference")
                break
            else:
                if input_value.casefold() in line[0].casefold():
                    count +=1
                    result.insert(tk.END, "Ref:"+line[0]+'\t'+"  Name:"+line[1]+'\t\t'+"   Classification:"+line[2]+'\n')
                
        elif(opt == 3):
            if input_value.casefold() in line[2].casefold():
                count +=1
                result.insert(tk.END, "Ref:"+line[0]+'\t'+"  Name:"+line[1]+'\t\t'+"   Classification:"+line[2]+'\n')
    
    if(input_value != ''):               
        if(count == 0):
            if(opt == 1):
                result.insert(tk.END,"Not matching '%s' with a building name"%input_value)
            elif(opt == 2):
                result.insert(tk.END,"Not matching '%s' with a building refernce number"%input_value)
            elif(opt == 3):
                result.insert(tk.END,"Please select a building/location classification")
        else:
            if(count > 1 ):
                result.insert(tk.END,"**%d matching results with '%s' **"%(count,input_value))
                label_change = 'If mutilple buildings/locations received, click on the required building'
                label.configure(text=label_change)
            else:
                if(opt==1):
                    label_change = 'Enter Full or Part of the Building Name'
                elif(opt==2):
                    label_change = 'Enter Full or Part of the Building Reference'
                elif(opt==3):
                    label_change = 'Select a Building/Location Classification'
                label.configure(text=label_change)

# when changing pages, clear/change labels
def pageChange(opt,label,selected_text,result):
    if(opt==1):
        label_change = 'Enter Full or Part of the Building Name'
    elif(opt==2):
        label_change = 'Enter Full or Part of the Building Reference'
    elif(opt==3):
        label_change = 'Select a Building/Location Classification'
    label.configure(text=label_change)
    selected_text.set('')
    result.delete(0, END)

app = GUI()
app.mainloop()