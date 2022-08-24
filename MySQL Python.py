import mysql.connector 
db = mysql.connector.connect(host= 'localhost', user='root', password='', database= 'company_database' )
cursor = db.cursor()


def add_new_employee(): 
    Fname = input("Enter First Name: ")
    Minit = input("Enter Middle Initial: ")
    Lname = input("Enter Last Name: ")
    ssn = input("Enter ssn: ")
    bdate = input("Enter Birth date (yyyy-mm-dd): ")
    address = input("Enter address: ")
    sex = input("Enter sex: ")
    salary = input("Enter salary: ")
    superssn = input("Enter superssn: ")
    dno = input("Enter dno: ")

    try:
        cursor.execute("INSERT INTO EMPLOYEE (Fname, Minit, Lname, Ssn, Bdate, Address, Sex, Salary, Super_ssn, Dno) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (Fname, Minit, Lname, ssn, bdate, address, sex, salary, superssn, dno))
        db.commit()
    except mysql.connector.IntegrityError as err:
        print("Error: {}".format(err))
        

def view_employee(): 
    ssn = input("Enter Employee Ssn: ")
    query = "SELECT EMP.Fname, EMP.Minit, EMP.Lname, EMP.Ssn, EMP.Bdate, EMP.Address, EMP.Sex, EMP.Salary, EMP.Super_ssn, EMP.Dno, SUP.Fname SUP_Fname, SUP.Minit SUP_Minit, SUP.Lname SUP_Lname, D.Dname, DEP.DEPENDENT_NAME FROM EMPLOYEE EMP LEFT JOIN EMPLOYEE SUP ON EMP.SUPER_SSN = SUP.SSN LEFT JOIN DEPARTMENT D ON EMP.Dno = D.Dnumber LEFT JOIN DEPENDENT DEP ON EMP.Ssn = DEP.Essn WHERE EMP.SSN = %s"
    cursor.execute(query, (ssn, ))
    for x in cursor:
        print(x)

def modify_employee(): 
    ssn = input("Enter Employee Ssn: ")
    query = "SELECT Fname, Minit, Lname,Ssn, Bdate, Address, Sex, Salary, Super_ssn, Dno FROM EMPLOYEE WHERE ssn = %s FOR UPDATE"
    cursor.execute(query, (ssn, ))
    for x in cursor:
        print(x)
    field = input("Enter what field you would like to modify (address, sex, salary, super_ssn, or Dno): " )
    if(field == "address" or field == "ADDRESS"):
        newAddress = input("Enter Updated Address: ")
        queryAddress = "UPDATE EMPLOYEE SET ADDRESS = %s WHERE SSN = %s"
        cursor.execute(queryAddress, (newAddress, ssn, ))
        db.commit()
    elif(field == "sex" or field == "SEX"):
        newSex = input("Enter Updated Sex: ")
        querySex = "UPDATE EMPLOYEE SET SEX = %s WHERE SSN = %s"
        cursor.execute(querySex, (newSex, ssn, ))
        db.commit()
    elif(field == "salary" or field == "SALARY"):
        newSalary = input("Enter Updated Salary: ")
        querySalary = "UPDATE EMPLOYEE SET SALARY = %s WHERE SSN = %s"
        cursor.execute(querySalary, (newSalary, ssn, ))
        db.commit()
    elif(field == "super_ssn" or field == "SUPER_SSN"):
        newSuper_ssn = input("Enter Updated Super_ssn: ")
        querySuper_ssn = "UPDATE EMPLOYEE SET SUPER_SSN = %s WHERE SSN = %s"
        cursor.execute(querySuper_ssn, (newSuper_ssn, ssn, ))
        db.commit()
    elif(field == "dno" or field == "DNO" or field == "Dno"):
        newDno = input("Enter Updated Department Number: ")
        queryDno = "UPDATE EMPLOYEE SET DNO = %s WHERE SSN = %s"
        cursor.execute(queryDno, (newDno, ssn, ))
        db.commit()

def remove_employee():
    ssn = input("Enter Employee Ssn: ")
    query = "SELECT Fname, Minit, Lname,Ssn, Bdate, Address, Sex, Salary, Super_ssn, Dno FROM EMPLOYEE WHERE ssn = %s FOR UPDATE"
    cursor.execute(query, (ssn, ))
    for x in cursor:
        print(x)
    confirmation = input("Are you sure you would like to delete this employee? (y/n): ")
    if(confirmation == "y" or  confirmation =='Y'):
        try:
            queryDelete = "DELETE FROM EMPLOYEE WHERE Ssn = %s"
            cursor.execute(queryDelete, (ssn, ))
            db.commit()
        except mysql.connector.IntegrityError as err:
            print("Error: {}".format(err))
    elif(confirmation == "n" or confirmation =='N'):
        db.commit()

def add_new_dependent():
    ssn = input("Enter Employee Ssn: ")
    query = "SELECT DEPENDENT_NAME, SEX, BDATE, RELATIONSHiP FROM DEPENDENT WHERE Essn = %s"
    cursor.execute(query, (ssn, ))
    for x in cursor:
        print(x)
    Dependent_name = input("Enter New Dependent Name: ")
    sex = input("Enter New Dependent Sex: ")
    Bdate = input("Enter New Dependent Birth Date: ")
    Relationship = input("Enter New Dependent Relationship: ")
    cursor.execute("INSERT INTO DEPENDENT (ESSN, DEPENDENT_NAME, SEX, BDATE, RELATIONSHIP) VALUES(%s, %s, %s, %s, %s) FOR UPDATE", (ssn, Dependent_name, sex, Bdate, Relationship))
    db.commit()

def remove_dependent(): 
    ssn = input("Enter Employee Ssn: ")
    query = "SELECT DEPENDENT_NAME, SEX, BDATE, RELATIONSHIP FROM DEPENDENT WHERE Essn = %s FOR UPDATE"
    cursor.execute(query, (ssn, ))
    for x in cursor:
        print(x)
    removed = input("Enter name of Dependent to be Removed: ")
    queryDelete = "DELETE FROM DEPENDENT WHERE DEPENDENT_NAME = %s"
    cursor.execute(queryDelete, (removed, ))
    db.commit()

def add_new_department(): 
    Dname = input("Enter Department Name: ")
    Dnumber = input("Enter Department Number: ")
    Mgr_ssn = input("Enter Manager SSN: ")
    Mgr_start_date = input("Enter Manager Start Date: ")
    try:
        cursor.execute("INSERT INTO DEPARTMENT (Dname, Dnumber, Mgr_ssn, Mgr_start_date) VALUES(%s, %s, %s, %s)", (Dname, Dnumber, Mgr_ssn, Mgr_start_date))
        db.commit()
    except mysql.connector.IntegrityError as err:
        print("Error: {}".format(err))

def view_department():
    dnum = input("Enter Department number: ")
    query =" SELECT D.Dname, EMP.Fname, EMP.Minit, EMP.Lname, DL.DLOCATION FROM DEPARTMENT D LEFT JOIN EMPLOYEE EMP ON D.MGR_SSN = EMP.SSN LEFT JOIN DEPT_LOCATIONS DL ON D.DNUMBER = DL.Dnumber WHERE D.DNUMBER = %s"
    cursor.execute(query, (dnum, ))
    for x in cursor:
        print(x)
    
def remove_department():
    dnum = input("Enter Department number: ")
    query = "SELECT * FROM DEPARTMENT WHERE DNUMBER = %s FOR UPDATE"
    cursor.execute(query, (dnum, ))
    for x in cursor:
        print(x)
    confirmation = input("Are you sure you would like to delete this Department? (y/n): ")
    if(confirmation == "y" or  confirmation =='Y'):
        try:
            queryDelete = "DELETE FROM DEPARTMENT WHERE DNUMBER = %s"
            cursor.execute(queryDelete, (dnum, ))
            db.commit()
        except mysql.connector.IntegrityError as err:
            print("Error: {}".format(err))
            print("Please Resolve Any Referential Integrity Constraint Violations Before Trying To Remove This Department.")
    elif(confirmation == "n" or confirmation =='N'):
        db.commit()
        pass

def add_department_location(): 
    dnum = input("Enter Department number: ")
    query = "SELECT DLOCATION FROM DEPT_LOCATIONS WHERE DNUMBER = %s FOR UPDATE"
    cursor.execute(query, (dnum, ))
    for x in cursor:
        print(x)
    newLoc = input("Enter New Location: ")
    cursor.execute("INSERT INTO DEPt_LOCATIONS (DNUMBER ,DLOCATION) VALUES(%s, %s)", (dnum, newLoc))
    db.commit()

def remove_department_location(): 
    dnum = input("Enter Department number: ")
    query = "SELECT DLOCATION FROM DEPT_LOCATIONS WHERE DNUMBER = %s FOR UPDATE"
    cursor.execute(query, (dnum, ))
    for x in cursor:
        print(x)
    removed = input("Select Department Location To Be Removed: ")
    queryDelete = "DELETE FROM DEPT_LOCATIONS WHERE DLOCATION = %s"
    cursor.execute(queryDelete, (removed, ))
    db.commit()




def main():
    print("Database Options: ")
    print("1. Add New Employee")
    print("2. View Employee")
    print("3. Modify Employee")
    print("4. Remove Employee")
    print("5. Add New Dependent")
    print("6. Remove Dependent")
    print("7. Add new Department")
    print("8. View Department")
    print("9. Remove Department")
    print("10. Add Department Location")
    print("11. Remove Department Location")
    selection = input("Enter Option Number: ")
    
    if(selection == "1"):
         add_new_employee()
         menu = input("Return to Menu? (y/n)")
    elif(selection == "2"):
        view_employee()
        menu = input("Return to Menu? (y/n)")
    elif(selection == "3"):
        modify_employee()
        menu = input("Return to Menu? (y/n)")
    elif(selection == "4"):
        remove_employee()
        menu = input("Return to Menu? (y/n)")
    elif(selection == "5"):
        add_new_dependent()
        menu = input("Return to Menu? (y/n)")
    elif(selection == "6"):
        remove_dependent()
        menu = input("Return to Menu? (y/n)")
    elif(selection == "7"):
        add_new_department()
        menu = input("Return to Menu? (y/n)")
    elif(selection == "8"):
        view_department()
        menu = input("Return to Menu? (y/n)")
    elif(selection == "9"):
        remove_department()
        menu = input("Return to Menu? (y/n)")
    elif(selection == "10"):
        add_department_location()
        menu = input("Return to Menu? (y/n)")
    elif(selection == "11"):
       remove_department_location() 
       menu = input("Return to Menu? (y/n)")
    else:
        print("Invalid Input")
        main()
    
    if(menu == "y" or  menu =='Y'):
        main()
    elif(menu == "n" or menu =='N'):
        print("You Have Exited the Program.")
        quit
if __name__ == "__main__":
    main() 