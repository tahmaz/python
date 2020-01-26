path = '../products/data/'
entries = os.listdir(path)
for entry in entries:
    eth = entry.split(".")
    #rename .txt to .html
    if(eth[-1] == "txt"):
        try:
            os.rename(path + entry, path + eth[0] + ".html")
            #print(entry + "\t")
        except Exception as ex:
            print(ex)
    #spesific rename
    if(eth[0][0:4] == "toys"):
        print(path + eth[0][0:4] + "_" + eth[0][4:len(eth[0])] +"_09072019_000000" + ".html")
        try:
            os.rename(path + entry, path + eth[0][0:4] + "_" + eth[0][4:len(eth[0])] +"_09072019_000000" + ".html")
        except Exception as ex:
            print(ex)

    if(eth[0][0:11] == "electronics"):
        #print(path + eth[0][0:11] + "_" + eth[0][11:len(eth[0])] +"_09072019_000000" + ".html")
        try:
            os.rename(path + entry, path + eth[0][0:11] + "_" + eth[0][11:len(eth[0])] +"_09072019_000000" + ".html")
        except Exception as ex:
            print(ex)