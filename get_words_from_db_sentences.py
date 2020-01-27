---------words.py--------
#!/usr/bin/python
import MySQLdb


# Open database connection
db = MySQLdb.connect("localhost","chat","chatchat","chat" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.

#print sentencess
cursor.execute("SELECT id,sentence from sentences where accept!=1 or accept is null limit 1")
while cursor.rowcount > 0:
    datas = cursor.fetchone()
    sentenceid = datas [0]
    sentence = datas[1]
    words = sentence.split(' ') 
    for w in words:
        word = w.replace(',','').strip()
        #eger 2 simvoldan boyukdurse ve en azi 3 soz varsa
        if(len(word)>2):
            print (word)
            cursor.execute("SELECT id from words where word=\""+word+"\" limit 1")
            if (cursor.rowcount < 1):
                try:
                    # add sub links to web_links table
                    cursor.execute("insert into words (word,cost,inserttime,updatetime) values(\""+word+"\",0,now(),now())")
                    #print("insert", sentence)
                    # Commit your changes in the databas
                    db.commit()
                except:
                    # Rollback in case there is any error
                    db.rollback()
                    print("word insert failed","insert into words (word,cost,inserttime,updatetime) values(\""+word+"\",0,now(),now())")
            else:
                wordid = cursor.fetchone()[0]
                try:
                    cursor.execute("update words set cost=cost+1,updatetime=now() where id="+str(wordid))
                    db.commit()
                    #print("update",sentence)
                except:
                    print("word cost update failed","update words set cost=cost+1,updatetime=now() where id="+str(wordid))
                    db.rollback()
    try:
        cursor.execute("update sentences set accept=1,updatetime=now() where id="+str(sentenceid))
        db.commit()
        #print("update",datanew)
    except:
        db.rollback()
        print("sentence accept update failed","update sentences set accept=1 where id="+str(sentenceid))
    cursor.execute("SELECT id,sentence from sentences where accept!=1 or accept is null limit 1")
# disconnect from server
db.close()