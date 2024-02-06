# Command to import the module
import mysql.connector
from tabulate import tabulate
import random
import matplotlib.pyplot as plt
import pandas as pd


# Command to connect database 
mydb=mysql.connector.connect(host="localhost",port='3306',user="root",passwd="root",database="myairport")
# Command to create a cursor to access the data from the python program
mycursor=mydb.cursor()

# Command to define the function to display the main menu
def airesmenu():
   

    print("                      _______ ")
    print("                     \\       \\ ")
    print("                      \\      `\\ ")
    print("    ____               \\       \\ ")
    print("   |    \\               \\      `\\ ")
    print("   |_____\\               \\       \\ ")
    print("   |______\\               \\      `\\ ")
    print("   |       \\__             \\       \\ ")
    print("   |      _  _\\__--------------------------------._. ")
    print(" __|---~~~__o_o_o_o_o_o_o_o_o_o_o_o_o_o_o_o_o_o_[][\__ ")
    print("|___                         /~      )                \\__ ")
    print("    ~~~---..._______________/      ,/_________________/ ")
    print("                           /      / ")
    print("                          /     ,/ ")
    print("                         /     / ")
    print("                        /    ,/ ")
    print("                       /    / ")
    print("                      //  ,/ ")
    print("                     //  / ")
    print("                    // ,/ ")
    print("                   //__/ ")
    print()
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")    
    print("============== WELCOME IN AIRLINE RESERVATION SYSTEM =============")
    print("*****************************MAIN MENU****************************")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print()
    print("AIRLINE RESERVATION SYSTEM")
    print("1.Search Flight Details")
    print("2.Reservation of Ticket")
    print("3.Cancellation of Ticket")
    print("4.Display PNR Status")
    print("5.Display All Flight Details")
    print("6.Show Popularity Graph")
    print("7.Quit")
    print("8.See the CSV_1[for testing]")
    print("9.See the CSV_2[for testing]")
    print("",end="\n")
    print("=======INPUT YOUR CHOICE HERE(Any number between 1 to 9 :) ==========")
    
    ch='y'
    while(ch=='y'):
        n=input("Enter Your Choice: ")
        if (not any(char.isdigit() for char in n)):
            print('choice should have any number between 1 to 9 :') 
            ch='n'
        else:
            n=int(n)
        
        if(n==1):
            flight_search()
            ch='n'
        elif(n==2):
            flight_reservation()
            ch='n'
        elif(n==3):
            flight_cancel()
            ch='n'
        elif(n==4):
            flight_PNR_status()
            ch='n'
        elif(n==5):
            all_flight_details()
            ch='n'
        elif(n==6):
            ch='n'
            dest=['Jaipur','Delhi','Mumbai', 'Kolkata']
            pop=[85,95,60,75]
            plt.barh(dest,pop,align='center',color='red')
            for index, value in enumerate(pop):
                plt.text(value, index, str(value))
            plt.xlabel('Destination')
            plt.ylabel('Popularity')
            plt.title('Tourist Preferrence Analysis') 
            plt.show()
            print("Go back to menu")
            print('\n'*10)
            print("==============================================================================================")
            airesmenu()
            airesmenu()
            
        elif(n==7):
            exit(0)
        elif(n==8):
            ch='n'
            CSV_frame= pd.DataFrame({'Cities':['Jaipur','Mumbai','Delhi','Kolkata'],'Monthly_Visits':[1000,500,650,800]})
            CSV_frame.to_csv("D:\\Airplane Reservation System\\City Popularity Chart.csv")
            CSV_read= pd.read_csv("D:\\Airplane Reservation System\\City Popularity Chart.csv")
            print(CSV_read)
            print("Go back to menu")
            print('\n'*10)
            print("==============================================================================================")
            airesmenu()
            airesmenu()
        elif(n==9):
            ch='n'
            CSV_frame2= pd.DataFrame({'Class':['First','Business','Premium Economy','Economy'],'Monthly_Bookings':[200,150,400,700]})
            CSV_frame2.to_csv("D:\\Airplane Reservation System\\Class Popularity Chart.csv")
            CSV_read2= pd.read_csv("D:\\Airplane Reservation System\\Class Popularity Chart.csv")
            print(CSV_read2)
            print("Go back to menu")
            print('\n'*10)
            print("==============================================================================================")
            airesmenu()
            airesmenu()
        else:
            print("wrong choice")
            ch='y'
            

def flight_search():
    print("Search Flights")
    print()
    print("++++++++++++++++++++++++++++++++++")
    print("=========Flight Search Window========")
    print("++++++++++++++++++++++++++++++++++")
    print()
# COmmand to ask passenger for their source city and Destination city
    S_City=input("Enter Source City:")
    D_City=input("Enter Destination City:")
# Command to display flight details from table in the MySQL database 
    sql="select PlaneNumber,Airline_Name,Source_City,Destination_City,Dept_Date,Dept_Time, Arrival_Time,N_F_Class,F_Fare,N_B_Class,B_Fare, N_PE_Class, PE_Fare, N_E_Class, E_Fare from airdetails where Source_City=%s AND Destination_City=%s"
    val=(S_City,D_City,)
    mycursor.execute(sql,val)
    res=mycursor.fetchall()
    mydb.commit()

    if not res:
        print("please enter correct source and destination city !! ")
    else:
        print("Flight status is as follows:")
# Command to display the information related to the pnr from the table
        print(tabulate(res, headers=['PlaneNumber','Airline_Name','Source_City','Destination_City','Dept_Date','Dept_Time', 'Arrival_Time','N_F_Class','F_Fare','N_B_Class','B_Fare', 'N_PE_Class', 'PE_Fare', 'N_E_Class', 'E_Fare'], tablefmt='psql'))

    
    print("Go back to menu")
    print('\n'*10)
    print("==============================================================================================")
    airesmenu()
    airesmenu()




def flight_reservation():
    global pnr
    l1=[]
    print()
    print("+++++++++++++++++++++++++++++++")
    print("===Ticket Reservation Window===")
    print("+++++++++++++++++++++++++++++++")
    print()
    ques=int(input("Do you know Flight Details type 1 for YES and 0 for NO  : "))
    if (ques==0):
        flight_search()

    elif (ques==1):
        # Command to calculate pnr of the user
        
        pnr=random.randint(0,10000)
        l1.append(pnr)
       # Command to ask user the plane number
        planeno=int(input("Enter plane number="))
        l1.append(planeno)
        # Command to ask for the name of passenger
        p_name=input("Enter passenger name=")
        if p_name.isdigit():
            print("Enter valid name in alphabets")
            airesmenu()
        else:
            l1.append(p_name) 
# Command to ask user for age of passenger
        age=input("Enter age of passenger=")
        if age.isdigit():
            age=int(age)
            if (age>1 and age<150):
                l1.append(age)
            else:
                print("Please write valid age in integer") 
                airesmenu()
        else:
            print("Please write valid age in integer") 
            airesmenu()

# Command to ask user mobile number
        mobile=input("Enter Mobile Number of passenger=")
        if mobile.isdigit():
            #mobile=int(mobile)
            n=len(mobile)
            if (n>0 and n<11):
                l1.append(n)
            else:
                print("Please write valid mobile number ") 
                airesmenu()
        else:
            print("Please write valid mobile number ") 
            airesmenu()
            #payment options
        

# Command to ask user for the number of passengers
        noofpas=int(input("Enter number of passengers:"))
        l1.append(noofpas)
# Command to ask user for the class they would like to travel in
        print("Select a class you would like to travel in")
        print("1.FIRST CLASS")
        print("2.BUSINESS CLASS")
        print("3.PREMIUM ECONOMY CLASS")
        print("4.ECONOMY CLASS")
        cp=int(input("Enter your choice:"))
# Command to calculate the amount to be paid by the user according to their choices
        rplane_no=(planeno,)
        if(cp==1):
            sql="select N_F_Class from airdetails where PlaneNumber=%s"
            mycursor.execute(sql,rplane_no)
            nfseats=mycursor.fetchone()
            if nfseats is None:
                nfseats=0;
                print("you have entered incorrect plane number..please try again")
                airesmenu()
            else:
                nfseats=int(nfseats[0])
                if(nfseats>=noofpas):
                    sql="select F_Fare from airdetails where PlaneNumber=%s"
                    mycursor.execute(sql,rplane_no)
                    ffare=mycursor.fetchone()
                    ffare=int(ffare[0])
                    amt=noofpas*ffare
                    cls='fc'
                    updated_seats=nfseats-noofpas
                    sql= "Update airdetails SET N_F_Class =%s where PlaneNumber=%s"
                    data=(updated_seats,planeno,)
                    mycursor.execute(sql,data)
                    mydb.commit()
                else:
                    print("Sufficient Number of seats are not available...please search again")
                    airesmenu()
                
        elif(cp==2):
            sql="select N_B_Class from airdetails where PlaneNumber=%s"
            mycursor.execute(sql,rplane_no)
            nbseats=mycursor.fetchone()
            if nbseats is None:
                nbseats=0;
                print("you have entered incorrect plane number..please try again")
                airesmenu()
            else:
                nbseats=int(nbseats[0])
                if(nbseats>=noofpas):
                    sql="select B_Fare from airdetails where PlaneNumber=%s"
                    mycursor.execute(sql,rplane_no)
                    bfare=mycursor.fetchone()
                    bfare=int(bfare[0])
                    amt=noofpas*bfare
                    cls='bc'
                    updated_seats=nbseats-noofpas
                    sql= "Update airdetails SET N_B_Class =%s where PlaneNumber=%s"
                    data=(updated_seats,planeno,)
                    mycursor.execute(sql,data)
                    mydb.commit()
                else:
                    print("Sufficient Number of seats are not available...please search again")
                    airesmenu()
                

        elif(cp==3):
            sql="select N_PE_Class from airdetails where PlaneNumber=%s"
            mycursor.execute(sql,rplane_no)
            npeseats=mycursor.fetchone()
            if npeseats is None:
                npeseats=0;
                print("you have entered incorrect plane number..please try again")
                airesmenu()
            else:
                npeseats=int(npeseats[0])
                if(npeseats>=noofpas):
                    sql="select PE_Fare from airdetails where PlaneNumber=%s"
                    mycursor.execute(sql,rplane_no)
                    pefare=mycursor.fetchone()
                    pefare=int(pefare[0])
                    amt=noofpas*pefare
                    cls='pec'
                    updated_seats=npeseats-noofpas
                    sql= "Update airdetails SET N_PE_Class =%s where PlaneNumber=%s"
                    data=(updated_seats,planeno,)
                    mycursor.execute(sql,data)
                    mydb.commit()
                else:
                    print("Sufficient Number of seats are not available...please search again")
                    airesmenu()
        elif(cp==4):
            sql="select N_E_Class from airdetails where PlaneNumber=%s"
            mycursor.execute(sql,rplane_no)
            neseats=mycursor.fetchone()
            if neseats is None:
                neseats=0;
                print("you have entered incorrect plane number..please try again")
                airesmenu()
            else:
                neseats=int(neseats[0])
                if(neseats>=noofpas):
                    sql="select E_Fare from airdetails where PlaneNumber=%s"
                    mycursor.execute(sql,rplane_no)
                    efare=mycursor.fetchone()
                    efare=int(efare[0])
                    amt=noofpas*efare
                    cls='ec'
                    updated_seats=neseats-noofpas
                    sql= "Update airdetails SET N_E_Class =%s where PlaneNumber=%s"
                    data=(updated_seats,planeno,)
                    mycursor.execute(sql,data)
                    mydb.commit()
                else:
                    print("Sufficient Number of seats are not available...please search again")
                    airesmenu()
        else:
            print("You have selected wrong class!!")
            airesmenu()
        l1.append(cls)
# Command to display the total amount to be paid by the user  
        print("total amount to be paid:",amt)
        l1.append(amt)

# Command to display the pnr of the passenger
        #print("PNR number:",pnr)
        #print("status:confirmed")
        status='confirmed'
        l1.append(status)
        reservation=(l1)

              
        print("Please pay the amount to get the ticket!!!!")
        pay=int(input("Enter 1 to print the ticket, 0 to save the paper:"))




        
     # Command to insert the information obtained from user in the table in database 
        if(pay==1):
                sql="insert into reservation_details(PNR,PlaneNumber,Name,Age,Mobile,No_Seats,Class,Total_Fare,Status)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                mycursor.execute(sql,reservation)
                mydb.commit()
                print("please get your ticket:" )
                mypnr=(pnr,)
                sql="select * from reservation_details where PNR=%s"
                mycursor.execute(sql,mypnr)
                ticketdetail=mycursor.fetchall()
                mydb.commit()
                print(tabulate(ticketdetail, headers=['PNR','PlaneNumber','Name','Age','Mobile','No_Seats','Class','Total_Fare','Status'], tablefmt='psql'))
        elif(pay==0):
            print("You have saved the paper...THANKS")
        else:
            print("wrong choice")
            ch='y'
        print("Go back to menu")
        print('\n'*10)
        print("==============================================================================================")
    else:
            print("wrong choice")
            ch='y'
    airesmenu() 
    airesmenu()
        

# Command to define function to cancel a ticket
def flight_cancel():
    print()
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("======================Ticket cancellation window========================")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print()
# Command to ask the passenger for the pnr for which the ticket has to be cancelled 
    pnr=input("Enter PNR for cancellation of ticket:")
    pn=(pnr,)
# Command to update the status of pnr in the MySQL table    
    

    sql_cancel="select PlaneNumber, No_Seats, Class from reservation_details where PNR=%s"
    mycursor.execute(sql_cancel,pn)
    tktdetails=mycursor.fetchone()
    print(tktdetails)
    myplaneno=int(tktdetails[0])
    myseats=int(tktdetails[1])
    myclass=tktdetails[2]
    if(myclass=="fc"):
        sql= "Update airdetails SET N_F_Class =N_F_Class + %s where PlaneNumber=%s"
    elif(myclass=="bc"):
        sql= "Update airdetails SET N_B_Class =N_B_Class + %s where PlaneNumber=%s"
    elif(myclass=="pec"):
        sql= "Update airdetails SET N_PE_Class =N_PE_Class + %s where PlaneNumber=%s"
    elif(myclass=="ec"):
        sql= "Update airdetails SET N_E_Class =N_E_Class + %s where PlaneNumber=%s"
    else:
        print("Please enter correct PNR Number and Try Again")
        airesmenu()

    data=(myseats,myplaneno,)
    mycursor.execute(sql,data)
    mydb.commit()

    sql="update reservation_details set status='deleted' where PNR=%s"
    mycursor.execute(sql,pn)
    mydb.commit()
    print("Ticket Cancellation has completed")
    print("Go back to menu")
    print('\n'*10)
    print("=============================================================================================")
    airesmenu()
    #airesmenu()

# Command to describe the function to display the status of a pnr
def  flight_PNR_status():
    print()
    print("++++++++++++++++++++++++++++++++++")
    print("=========PNR status window========")
    print("++++++++++++++++++++++++++++++++++")
    print()
# COmmand to ask passenger for their pnr
    pnr=input("Enter PNR NUMBER:")
    pn=(pnr,)
# Command to select the status of pnr from table in the MySQL database 
    sql="select * from reservation_details where PNR=%s"
    mycursor.execute(sql,pn)
    res=mycursor.fetchall()
    mydb.commit()
    print("PNR status is as follows:")
    print(tabulate(res, headers=['PNR','PlaneNumber','Name','Age','Mobile','No_Seats','Class','Total_Fare','Status'], tablefmt='psql'))

    #print other details
    sql="select PlaneNumber from reservation_details where PNR=%s"
    mycursor.execute(sql,pn)
    planeno=mycursor.fetchone()
    sql="select Airline_Name,Source_City,Destination_City,Dept_Date,Dept_Time, Arrival_Time from airdetails where PlaneNumber=%s"
    mycursor.execute(sql,planeno)
    res1=mycursor.fetchall()
    mydb.commit()
    print(tabulate(res1, headers=['Airline_Name','Source_City','Destination_City','Dept_Date','Dept_Time', 'Arrival_Time'], tablefmt='psql'))
    print("Go back to menu")
    print('\n'*10)
    print("==============================================================================================")
    airesmenu()
    


#command to display all flight details
def all_flight_details():
    sql="select * from airdetails"
    mycursor.execute(sql)
    rows=mycursor.fetchall()

    print(tabulate(rows, headers=['PlaneNumber','Airline_Name','Source_City','Destination_City','Dept_Date','Dept_Time', 'Arrival_Time','N_F_Class','F_Fare','N_B_Class','B_Fare', 'N_PE_Class', 'PE_Fare', 'N_E_Class', 'E_Fare'], tablefmt='psql'))


    #for x in rows:
     #   print(x)
    airesmenu()

airesmenu()






    


