import json
count = 1
with open("/Users/whamsy/twitter_search/a/a_2017-03-01.json", 'r') as f:
    for entry in f:
        line = json.loads(entry)
        if( "created_at" in line and line["lang"] == "en" and line["geo"] is not None):
            # with open("output1.json", 'a') as f:
            #     print(entry, file=f)
                print(count)
                count += 1
