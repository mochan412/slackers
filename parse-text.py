import os
import json

path =  'source/'
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
                            # print str
                            f = open('slack_messages.txt', 'a')
                            f.write(str)
                            f.close()
