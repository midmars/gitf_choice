import psycopg2
try:
    conn = psycopg2.connect(host="127.0.0.1", port="5432", database="htDB", user="vagrant", password="vagrant")
    cur = conn.cursor()
    cur.execute("CREATE TABLE test (id serial PRIMARY KEY, name varchar);")
    cur.execute("INSERT INTO test (name) VALUES (%s)",("Lyon Lin"))
    cur.execute("SELECT * FROM test;")
    cur.fetchone()
    conn.commit()    
    print "OK"
except:
    print "I am unable to connect to the database"
finally:
    cur.close()
    conn.close()






import psycopg2
try:
    conn = psycopg2.connect(host="127.0.0.1", port="5432", database="htDB", user="vagrant", password="vagrant")
    cur = conn.cursor()
    
    
    cur.execute("SELECT value_"+str[qn]+" FROM noreen_member WHERE member_pk IN (mp);")
    cur.fetchone()
    conn.commit()    
    print "OK"
except:
    pass
finally:
    cur.close()
    conn.close()

SELECT * 
FROM Store_Information 
WHERE Store_Name IN ('Los Angeles', 'San Diego');