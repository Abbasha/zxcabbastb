#!/usr/bin/env python
# -*- coding: utf-8 -*-
import redis
import os
redis = redis.Redis('localhost')
id = input("Enter Tabchi ID (1,2,3,4,5,...) : ")
sudo = input("Enter Full Sudo ID : ")
source = os.popen("cat base.lua").read()
#print(source)
source2 = source.replace("TABCHI-ID",str(id))
newsource = open("tabchi-{}.lua".format(id),"w")
newsource.write(source2)
newsource.close()
redis.set("tabchi:{}:fullsudo".format(id),sudo)
print("Done!\nNew Tabchi Created...\nID : {}\nFull Sudo : {}\nRun : ./run.sh {}".format(id,sudo,id))
