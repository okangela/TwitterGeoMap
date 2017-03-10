import json
count = 1
mapping = { "create" : { "_index" : "tweetmap", "_type" : "tweetdata"} }
with open("output1.json",'r') as fin:
    with open("outputfinal.json",'w') as fout:
        for line in fin:
            if line != "\n":
                mapping["create"]["_id"] = count
                count += 1
                print(json.dumps(mapping),file=fout)
                fout.write(line)
