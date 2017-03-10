mapping = '{ "create" : { "_index" : "tweetmap", "_type" : "tweetdata"} }'
with open("output3.json",'r') as fin:
    with open("output4.json",'w') as fout:
        for line in fin:
            if line != "\n":
                print(mapping,file=fout)
                fout.write(line)
