Project Name: Event Enrollment
Personal:
	Name: Arvindh Kumar V
	College: SASTRA DEEMED UNIVERSITY 
	Reg.No: 124158011 
	Branch: B.Tech CSE (IoT & Automation)

Instruction:

1)Graphical User Interface (GUI) is created using Python for data collection and storing data in MySQL database.

2)For Database Connection:
	def connection():
    		conn = pymysql.connect(
        	host='localhost',
        	user=' ',		# Enter your Username
        	password=' ',		# Enter your Password  
        	db='event_db',
   	 )
    	return conn

3)MySQL Database Details

	1) For Creating Table stuevent execute the below command in MySQL Workbench.
		CREATE TABLE stuevent (
   			STUDENT_ID VARCHAR(10) PRIMARY KEY,
    			NAME VARCHAR(50),
    			DEPARTMENT VARCHAR(50),
    			YEAR VARCHAR(5),
    			PHONE VARCHAR(11),
    			HOSTEL VARCHAR(50),
    			EVENT VARCHAR(50)
		);

4)Steps:
	1)Run the "DataEntry.py" file.
	2)Enter relavent Data in the respective fields.
	3)'Add' Button is given to insert the data in the MySQL database.
	4)'Update' Button is given to modify the row data with the help student_id in MySQL database.
	5)'Delete' Button is given to delete the row data with the help student_id in MySQL database.
	6)'Search' Button is given to search specific student detail in MySQL database with the help of Student_id.
	7)'Reset' Button is given to Clear contents in all the entry fields.
	8)'Select' Button make it easier to collect specific student detail by clicking the specific row. 
	9)'Treeview' Table is also provided in the GUI to check whether all the functions are executed properly.

