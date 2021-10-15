from tkinter import *
import pymysql
from tkinter import ttk

class StudentsData: 
      def __init__(self,root):
        self.root=root
        self.root.title("Student Info Data")
        self.root.geometry("1350x700")
#create label
        title=Label(self.root,text="Welcome To Data",
                    bd=5,
                    relief=GROOVE,
                    bg="green",
                    fg="white",
                    font=("ms sans serif",30,'bold'),
                    )

        title.pack(fill=X)
        
        self.roll_no_var=StringVar()
        self.first_name_var=StringVar()
        self.last_name_var=StringVar()
        self.course_var=StringVar()
        self.fee_var=StringVar()
        self.institute_var=StringVar()
        self.email_var=StringVar()
        self.mobile_var=StringVar()

        self.searchBy=StringVar()
        self.searchText=StringVar()






        
#create framefrom form
        FormFrame=Frame(self.root,bg="green",bd=5,relief=GROOVE)
        FormFrame.place(x=10,y=60,height=640, width=300)
        title=Label(FormFrame,text="Enter Students Data"
                    ,bg="green",
                    fg="white",
                    font=("ms sans serif",15,'bold'),
                    )
        title.grid(row=0,columnspan=2,padx=50,pady=20)
#roll number
        roll_no=Label(FormFrame,text="Roll No:",bg="green",
                    fg="white",
                    font=("ms sans serif",15,'bold'))
        roll_no.grid(row=1,column=0,sticky='w',padx=0)

        txt_roll_no=Entry(FormFrame,textvariable=self.roll_no_var,font=("ms sans serif",11,'bold'))
        txt_roll_no.grid(row=1,column=1,sticky='w', pady=10)
      

#First name
        first_name=Label(FormFrame,text="First Name:",bg="green",
                    fg="white",
                    font=("ms sans serif",15,'bold'))
        first_name.grid(row=2,column=0,sticky='w',padx=0)

        txt_first_name=Entry(FormFrame,textvariable=self.first_name_var,font=("ms sans serif",11,'bold'))
        txt_first_name.grid(row=2,column=1,sticky='w', pady=10)
        
#last name
        last_name=Label(FormFrame,text="Last Name:",bg="green",
                    fg="white",
                    font=("ms sans serif",15,'bold'))
        last_name.grid(row=3,column=0,sticky='w',padx=0)

        txt_last_name=Entry(FormFrame,textvariable=self.last_name_var,font=("ms sans serif",11,'bold'))
        txt_last_name.grid(row=3,column=1,sticky='w', pady=10)

#course name
        course=Label(FormFrame,text="course:",bg="green",
                    fg="white",
                    font=("ms sans serif",15,'bold'))
        course.grid(row=4,column=0,sticky='w',padx=0)

        txt_course=Entry(FormFrame,textvariable=self.course_var,font=("ms sans serif",11,'bold'))
        txt_course.grid(row=4,column=1,sticky='w', pady=10)
      
#institute name
        institute=Label(FormFrame,text="Institute:",bg="green",
                    fg="white",
                    font=("ms sans serif",15,'bold'))
        institute.grid(row=5,column=0,sticky='w',padx=0)

        txt_institute=Entry(FormFrame,textvariable=self.institute_var,font=("ms sans serif",11,'bold'))
        txt_institute.grid(row=5,column=1,sticky='w', pady=10)

#fee
        fee=Label(FormFrame,text="Fee:",bg="green",
                    fg="white",
                    font=("ms sans serif",15,'bold'))
        fee.grid(row=6,column=0,sticky='w',padx=0)

        txt_fee=Entry(FormFrame,textvariable=self.fee_var,font=("ms sans serif",11,'bold'))
        txt_fee.grid(row=6,column=1,sticky='w', pady=10)
        
#email
        email=Label(FormFrame,text="Email:",bg="green",
                    fg="white",
                    font=("ms sans serif",15,'bold'))
        email.grid(row=7,column=0,sticky='w',padx=0)

        txt_email=Entry(FormFrame,textvariable=self.email_var,font=("ms sans serif",11,'bold'))
        txt_email.grid(row=7,column=1,sticky='w', pady=10)


#mobile
        mobile=Label(FormFrame,text="Mobile:",bg="green",
                    fg="white",
                    font=("ms sans serif",15,'bold'))
        mobile.grid(row=8,column=0,sticky='w',padx=0)

        txt_mobile=Entry(FormFrame,textvariable=self.mobile_var,font=("ms sans serif",11,'bold'))
        txt_mobile.grid(row=8,column=1,sticky='w', pady=10)

#create buttons
        btn_frame= Frame(FormFrame,bd=4, relief=GROOVE,bg='green')
        btn_frame.place(x=0, y=400, width=290,height=70)

        btn_add=Button(btn_frame,text="Add",command=self.adding_data,font=("ms sans serif",12,'bold'),width=5,bg='blue',fg='white')
        btn_add.grid(row=0,column=0,pady=20,padx=5)

        btn_update=Button(btn_frame,text="Update",command=self.update,font=("ms sans serif",12,'bold'),width=5,bg='orange' ,fg='white')
        btn_update.grid(row=0,column=1,pady=20,padx=5)

        btn_clear=Button(btn_frame,text="Clear", command=self.clear,font=("ms sans serif",12,'bold'),width=5,bg='red' ,fg='white')
        btn_clear.grid(row=0,column=2,pady=20,padx=5)

        btn_delete=Button(btn_frame,text="Delete",command=self.delete,font=("ms sans serif",12,'bold'),width=5,bg='yellow' ,fg='red')
        btn_delete.grid(row=0,column=3,pady=20,padx=5)
        
#cerate frame for table
        TableFrame=Frame(self.root,bg="green",bd=5,relief=GROOVE)
        TableFrame.place(x=320,y=60,height=640,width=1030)


        lbl_search=Label(TableFrame, text='Search By:',width=15,bg='green',fg='white',font=("ms sans serif",14,'bold'))
        lbl_search.grid(row=0,column=0,pady=20)

        combo_search = ttk.Combobox(TableFrame,textvariable=self.searchBy,font=("ms sans serif",12,'bold'),width=14)
        combo_search['values']=('course','institute')
        combo_search.grid(row=0,column=1)

        txt_search=Entry(TableFrame,textvariable=self.searchText,font=("ms sans serif",14,'bold'),width=10)
        txt_search.grid(row=0,column=2,padx=40)

        btnsearch=Button(TableFrame,command=self.search_data,text="search",bg='blue',fg='white',font=("ms sans serif",14,'bold'),width=10)
        btnsearch.grid(row=0,column=3)

        btnShowAll=Button(TableFrame,text="Show All",bg='yellow',fg='red',font=("ms sans serif",14,'bold'),width=10)
        btnShowAll.grid(row=0,column=4,padx=40)


#creating data frame
        DataFrame=Frame(TableFrame,bd=5, relief=GROOVE)
        DataFrame.place(x=30,y=80,width=970,height=480)



        self.Student_Table=ttk.Treeview(DataFrame,columns=('roll_no','first_name','last_name','course','institute','fee','email','mobile'))
        self.Student_Table.heading('roll_no',text='Roll NO')
        self.Student_Table.heading('first_name',text='First Name')
        self.Student_Table.heading('last_name',text='Last Name')
        self.Student_Table.heading('course',text='Course')
        self.Student_Table.heading('institute',text='Institute')
        self.Student_Table.heading('fee',text='Fee')
        self.Student_Table.heading('mobile',text='Mobile')
        self.Student_Table.heading('email',text='Email')

        self.Student_Table['show']='headings'
        
        self.Student_Table.column('roll_no',width=100,anchor=CENTER)
        self.Student_Table.column('first_name',width=150,anchor=CENTER)
        self.Student_Table.column('last_name',width=150,anchor=CENTER)
        self.Student_Table.column('course',width=100,anchor=CENTER)
        self.Student_Table.column('institute',width=100,anchor=CENTER)
        self.Student_Table.column('fee',width=100,anchor=CENTER)
        self.Student_Table.column('email',width=150,anchor=CENTER)
        self.Student_Table.column('mobile',width=150,anchor=CENTER)


        self.Student_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.Student_Table.pack()
        self.fetching_data()
        
        


        

      def adding_data(self):
             connection= pymysql.connect(host='localhost',user='root',password='Prasad@1234',db='studentinfo')
             cursor=connection.cursor()
             cursor.execute('insert into studentdata values (%s,%s,%s,%s,%s,%s,%s,%s)',
                            (self.roll_no_var.get(),
                            self.first_name_var.get(),
                            self.last_name_var.get(),
                            self.course_var.get(),
                            self.institute_var.get(),
                            self.fee_var.get(),
                            self.email_var.get(),
                            self.mobile_var.get(),
                            ))
             connection.commit()
             self.fetching_data()
             self.clear()
             connection.close()
      def fetching_data(self):
            connection= pymysql.connect(host='localhost',user='root',password='Prasad@1234',db='studentinfo')
            cursor=connection.cursor()
            cursor.execute('select * from studentdata')
            rows=cursor.fetchall()
            if len (rows) !=0:
                  self.Student_Table.delete(*self.Student_Table.get_children())
                  for row in rows:
                        self.Student_Table.insert('',END,values=row)
                  connection.commit()
            connection.close()


      def clear(self):
            self.roll_no_var.set('')
            self.first_name_var.set('')
            self.last_name_var.set('')
            self.course_var.set('')
            self.institute_var.set('')
            self.fee_var.set('')
            self.email_var.set('')
            self.mobile_var.set('')

      def get_cursor(self,var):
            cursor_row=self.Student_Table.focus()
            content=self.Student_Table.item(cursor_row)
            row=content['values']
            self.roll_no_var.set(row[0])
            self.first_name_var.set(row[1])
            self.last_name_var.set(row[2])
            self.course_var.set(row[3])
            self.institute_var.set(row[4])
            self.fee_var.set(row[5])
            self.email_var.set(row[6])
            self.mobile_var.set(row[7])

      def update(self):
            connection= pymysql.connect(host='localhost',user='root',password='Prasad@1234',db='studentinfo')
            cursor=connection.cursor()
            cursor.execute('update studentdata set first_name=%s,last_name=%s,course=%s,institute=%s,fee=%s,email=%s,mobile=%s where roll_no=%s',
                           (self.first_name_var.get(),
                            self.last_name_var.get(),
                            self.course_var.get(),
                            self.institute_var.get(),
                            self.fee_var.get(),
                            self.email_var.get(),
                            self.mobile_var.get(),
                            self.roll_no_var.get()
                            ))
            connection.commit()
            self.fetching_data()
            self.clear()
            connection.close()


      def delete(self):
             connection= pymysql.connect(host='localhost',user='root',password='Prasad@1234',db='studentinfo')
             cursor=connection.cursor()
             cursor.execute('delete from studentdata where roll_no=%s',self.roll_no_var.get())

             connection.commit()
             self.fetching_data()
             self.clear()
             connection.close()


      def search_data(self):
            connection= pymysql.connect(host='localhost',user='root',password='Prasad@1234',db='studentinfo')
            cursor=connection.cursor()
            
            cursor.execute("select * from studentdata where "+str(self.searchBy.get())+" like'%"+str(self.searchText.get())+"%'")
            
            rows=cursor.fetchall()
            if len (rows) !=0:
                  self.Student_Table.delete(*self.Student_Table.get_children())
                  for row in rows:
                        self.Student_Table.insert('',END,values=row)
            connection.commit()
            connection.close()
            
           
           
             
              






















        






root = Tk()
obj = StudentsData(root)
root.mainloop()
