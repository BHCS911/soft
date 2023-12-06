from sql_connection import get_sql_connection
def get_all_details(connection):

    

    cursor = connection.cursor()
    query =( "SELECT show_full.client_id,client_name,client_amount_30_days,job,staff_id,staff_name,staff_salary_28_days,staff_advance_amount,staff_salary_left,joined_date,end_date,due_date FROM bhcs.show_full")

    cursor.execute(query)
    
    response = []

    for(client_id,client_name,client_amount_30_days,job,staff_id,staff_name,staff_salary_28_days,staff_advance_amount,staff_salary_left,joined_date,end_date,due_date) in cursor:


        response.append(
            {
                'client_id':client_id,
                'client_name':client_name,
                'client_amount_30_days':client_amount_30_days,
                'job':job,
                'staff_id':staff_id,
                'staff_name':staff_name,
                'staff_salary_28_days':staff_salary_28_days,
                'staff_advance_amount':staff_advance_amount,
                'staff_salary_left':staff_salary_left,
                'joined_date':joined_date,
                'end_date':end_date,
                'due_date':due_date               
            }
        )
        
        


    return response


def insert_new_client(connection,show_full):
    cursor = connection.cursor()
    print(show_full,"from clientfn")
    query = ("insert new client"
             "(client_name,client_amount_30_days,job,joined_date,end_date,due_date)"
             "VALUE (%s, %f, %s, %s, %s, %s)"
    )
    data = (show_full['client_name'],show_full['client_amount_30_days'], show_full['job'], show_full['joined_date'], show_full['end_date'], show_full['due_date'])
    
    cursor.execute = (query,data)
    connection.commit()
    
     
def delete_client(connection,client_id):
    cursor = connection.cursor()
    query = ("delete client where client_id="+str(client_id))
    cursor.execute(query)
    connection.commit()


def insert_new_staff(connection,show_full):
    
    cursor = connection.cursor()
    default_values = {
        'staff_name': 'DefaultName',
        'staff_amount_28_days': 0,  
        'job': 'DefaultJob',
        'joined_date': '2023-01-01',  
        'end_date': '2023-01-01',    
        'staff_advance_amount': 0,   
        'staff_salary_left': 0,      
    }
    


    for key in default_values:
        show_full[key] = show_full.get(key, default_values[key])
    query = ("INSERT INTO show_full (staff_name,staff_salary_28_days,job,joined_date,end_date,staff_advance_amount,staff_salary_left) VALUES (%s, %f, %s, %s, %s, %s)")
    data = (show_full['staff_name'],show_full['staff_amount_28_days'], show_full['job'], show_full['joined_date'], show_full['end_date'], show_full['staff_advance_amount'], show_full['staff_salary_left'])
    print(data,"from dbs")
    cursor.execute = (query,data)
    connection.commit()
    
    
def delete_staff(connection,staff_id):
    cursor = connection.cursor()
    query = ("delete client where staff_id="+str(staff_id))
    cursor.execute(query)
    connection.commit()

if __name__=='__main__':
    
    connection = get_sql_connection()
    
    print(get_all_details(connection))
