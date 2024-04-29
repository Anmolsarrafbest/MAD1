import psycopg2 as p,sys as s
host='localhost'
database='flib'
user='postgres'
password=3143
port=5432

conn=None
curr=None
try:
    f=open('player.txt','r')
    word=f.readline()
    print(word)
    conn=p.connect(host=host,database=database,user=user,
                password=password,port=port)
    curr=conn.cursor()
    curr.execute("""select p.jersey_no 
                 From players as p 
                 where p.name =%s""",(word,))
    res=curr.fetchall()
    print(res[0][0])
    """ FOR I IN RANGE:
            DECIDE WHETHER TO KILL/ OR SAVE 
            
            """
    
finally:
    pass        