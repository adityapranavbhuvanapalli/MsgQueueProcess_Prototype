import sys
import os
import time
import pyodbc
import configparser
config = configparser.ConfigParser()
config.read('mypy.ini')
config.sections()
os.system(config['path']['stop'])
#....Stopped the message queue
print("Wait for 3 seconds")
time.sleep(3)
#....Wait for some time

#....Write Code Here
conn=pyodbc.connect('Driver={SQL Server};'
                      'Server=localhost;'
                      'Database=AdventureWorks2012;'
                      'Uid=<userid>;Pwd=<password>', 
                      autocommit=True)
#conn=pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=AdventureWorks2012;UID=sa;PWD=Password@1')
print("DB Connection Successful")
cursor = conn.cursor()
#cursor.execute('SELECT * FROM HumanResources.Employee')
value=99
sql = 'exec dbo.SP_Dummy @id = '+str(value)
i=0
while(i<3):
    cursor.execute(sql)
    print ("SP Executed")
    i=i+1
sql='exec dbo.sp_stop_job @job_name = '+"<----------jobname------------>"
#sp_stop_job   
#      [@job_name =] 'job_name'  
#    | [@job_id =] job_id   
#    | [@originating_server =] 'master_server'  
#    | [@server_name =] 'target_server'
cursor.commit()
#print ("SP Executed")
#for row in cursor:
#    print(row)

#....Cleaning complete
print("Wait for 3 seconds")
time.sleep(3)
#....Wait for some time
os.system(config['path']['start'])
