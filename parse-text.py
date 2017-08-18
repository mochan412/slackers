import os
import json
import re

path =  "source/"

# get users
user_file = open("source/users.json", "r")
user_data = json.load(user_file)

users = {}
for u in user_data:
    users[u["id"].encode('ascii','ignore')] = u["name"].encode('ascii','ignore')
    # print users

def getUsername(hex):
    for key, value in users.items():
        if key == hex:
            return value

def replaceUsername(match):
    match = match.group()

    for key, value in users.items():
        if key == match[2:11]:
            return value


#get text
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
                            usr = d["user"].encode('ascii','ignore')
                            str = d["text"].encode('ascii','ignore')

                            username = getUsername(usr);
                            # print username

                            eliminate = False
                            phrases = [
                                "has left the channel",
                                "has joined the channel",
                                "set the channel",
                                "archived the channel",
                                "pinned a message to this channel",
                                "<https://",
                                "<http://",
                                "cleared channel topic"
                                ]

                            str = re.sub('(\<@.*?\>)', replaceUsername, str)
                            # print str

                            for e in phrases[:]:
                                if e in str:
                                    eliminate = True
                                    break
                                else:
                                    eliminate = False


                            if not eliminate:
                                # print format(username) + ": " + format(str)

                                f = open('slack_messages.txt', 'a')
                                f.write(format(username) + ": " + format(str) + "\n")
                                f.close()
