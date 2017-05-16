
def mapper():
    with open("/Users/ashokjain/testfile","r") as f:
        linedata = f.readlines()
        for line in linedata:
            data = line.strip().split("\t")
            if len(data)==6:
                date,time,store,item,cost,payment = data
                print "{0}\t{1}".format(store,cost)

print mapper()