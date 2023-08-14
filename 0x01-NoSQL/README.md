## 0x01-NoSQL

## REsources

- [NoSQL Databases Explained](https://intranet.alxswe.com/rltoken/wweK7dOY4pf8haCqv9Iv6Q)

- [What is NoSQL ?](https://intranet.alxswe.com/rltoken/QqqNmgzgwopHBv305ki6bg)

- [MongoDB with Python Crash Course - Tutorial for Beginners](https://intranet.alxswe.com/rltoken/RyyP9OH1EMBWWYpTs4TqoA)

- [MongoDB Tutorial 2 : Insert, Update, Remove, Query](https://intranet.alxswe.com/rltoken/9__3tR-NimgXlmjPQwTF-Q)

- [Aggregation](https://intranet.alxswe.com/rltoken/ziEDeniRobC6owPE1_avAQ)

- [Introduction to MongoDB and Python](https://intranet.alxswe.com/rltoken/axwwF4CjO7FnK8Ecochqnw)

- [mongo Shell Methods](https://intranet.alxswe.com/rltoken/lUqnLwOHbbp9FK39ijNmDQ)

- [The mongo Shell](https://intranet.alxswe.com/rltoken/bffQMLcTB4cg1bKqgBW3jw)

## Learning Objectives

- At the end of this project, you are expected to be able to [explain to anyone](https://intranet.alxswe.com/rltoken/9u20uNESC1dnTNowO5waNQ), without the help of Google:


## General

- What NoSQL means
- What is difference between SQL and NoSQL
- What is ACID
- What is a document storage
- What are NoSQL types
- What are benefits of a NoSQL database
- How to query information from a NoSQL database
- How to insert/update/delete information from a NoSQL database
- How to use MongoDB

## Install MongoDB 4.2 in Ubuntu 18.04

- [Official installation guide](https://intranet.alxswe.com/rltoken/8p4x14Ddn1UxKXZ5nPt3zA)

```bash

wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | apt-key add -
$ echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" > /etc/apt/sources.list.d/mongodb-org-4.2.list
$ sudo apt-get update
$ sudo apt-get install -y mongodb-org
...
$  sudo service mongod status
mongod start/running, process 3627
$ mongo --version
MongoDB shell version v4.2.8
git version: 43d25964249164d76d5e04dd6cf38f6111e21f5f
OpenSSL version: OpenSSL 1.1.1  11 Sep 2018
allocator: tcmalloc
modules: none
build environment:
    distmod: ubuntu1804
    distarch: x86_64
    target_arch: x86_64
$  
$ pip3 install pymongo
$ python3
>>> import pymongo
>>> pymongo.__version__
'3.10.1'
```

- Potential issue if documents creation doesn’t work or this error: Data directory /data/db not found., terminating ([source](https://intranet.alxswe.com/rltoken/as8vd5VBnj4VDz5EINszMg) and [source](https://intranet.alxswe.com/rltoken/9Df5v1NcWFFCn_sRNgsJUg))

```bash
sudo mkdir -p /data/db
```

- Or if /etc/init.d/mongod is missing, please find [here](mongod) an example of the file:

## Use “container-on-demand” to run MongoDB

- Ask for container Ubuntu 18.04 - MongoDB
Connect via SSH
- Or via the WebTerminal
- In the container, you should start MongoDB before playing with it:

```bash
$ service mongod start
* Starting database mongod                                              [ OK ]
$
$ cat 0-list_databases | mongo
MongoDB shell version v4.2.8
connecting to: mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb
Implicit session: session { "id" : UUID("70f14b38-6d0b-48e1-a9a4-0534bcf15301") }
MongoDB server version: 4.2.8
admin   0.000GB
config  0.000GB
local   0.000GB
bye
```