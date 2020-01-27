#!/usr/bin/python
import MySQLdb


# Open database connection
db = MySQLdb.connect("localhost","chat","chatchat","chat" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.

#print sentencess
cursor.execute("SELECT id,data from web_datas where accept!=1 or accept is null limit 1")
while cursor.rowcount > 0:
    datas = cursor.fetchone()
    dataid = datas [0]
    data = datas[1]
    sentences = data.split('.') 
    for s in sentences:
        sentence = s.strip()
        #eger 2 simvoldan boyukdurse ve en azi 3 soz varsa
        if(len(sentence)>2 and sentence.count(' ')>1):
            print (sentence)
            cursor.execute("SELECT id from sentences where sentence=\""+sentence+"\" limit 1")
            if (cursor.rowcount < 1):
                try:
                    # add sub links to web_links table
                    cursor.execute("insert into sentences (sentence,cost,inserttime,updatetime) values(\""+sentence+"\",0,now(),now())")
                    #print("insert", sentence)
                    # Commit your changes in the databas
                    db.commit()
                except:
                    # Rollback in case there is any error
                    db.rollback()
                    print("sentence insert failed","insert into sentences (sentence,cost,inserttime,updatetime) values(\""+sentence+"\",0,now(),now())")
            else:
                sentenceid = cursor.fetchone()[0]
                try:
                    cursor.execute("update sentences set cost=cost+1,updatetime=now() where id="+str(sentenceid))
                    db.commit()
                    #print("update",sentence)
                except:
                    print("sentence cost update failed","update sentences set cost=cost+1,updatetime=now() where id="+str(sentenceid))
                    db.rollback()
    try:
        cursor.execute("update web_datas set accept=1,updatetime=now() where id="+str(dataid))
        db.commit()
        #print("update",datanew)
    except:
        db.rollback()
        print("sentence accept update failed","update web_datas set accept=1 where id="+str(dataid))
    cursor.execute("SELECT id,data from web_datas where accept!=1 or accept is null limit 1")
# disconnect from server
db.close()