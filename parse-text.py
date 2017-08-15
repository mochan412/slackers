import os
import json

path =  "source/"
userfile = "source/users.json"

with open(userfile) as user_file:
    print user_file

for filename in os.listdir(path):
    if os.path.isdir(path+filename):
        # iterate thru files in subdirectory here
        subdir = path+filename
        for jsonfile in os.listdir(subdir):
            if jsonfile.endswith('.json'):
                # parse json here
                with open(subdir+'/'+jsonfile) as data_file:
                    data = json.load(data_file)
                    for d in data:
                        if  "text" in d and "user" in d:
                            usr = d["user"]
                            str = d["text"].encode('ascii','ignore')

                            eliminate = False
                            phrases = [
                                "has left the channel",
                                "has joined the channel",
                                "set the channel",
                                "archived the channel",
                                "pinned a message to this channel",
                                "<https://",
                                "<http://"
                                ]

                            for e in phrases[:]:
                                if e in str:
                                    eliminate = True
                                    break
                                else:
                                    eliminate = False


                            if not eliminate:
                                # print d["user"] + ": " + str
                                # f = open('slack_messages.txt', 'a')
                                # f.write(d["user"] + ": " + str + "\n")
                                # f.close()
