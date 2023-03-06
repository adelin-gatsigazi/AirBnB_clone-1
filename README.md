#[AirBnB_clone - The Console](https://github.com/kenza1525/AirBnB_clone/)

![image](https://user-images.githubusercontent.com/106814898/203315571-6c12b4d1-07e8-4485-bfe1-92351ecfb530.png)
Authored by: [Keriane Nzabampema](https://github.com/kenza1525/) and [Uwimana Lowami](https://github.com/Sonlowami/).

With the Console, you can create, modify and destroy objects, all on the commandline.
It is the first step to building an AirBnB clone.

##How to install it
If you use ssh, run the following command:<br><br>
        git clone git@github.com:Kenza1525/AirBnB_clone.git
<br><br>
If you use an https and a personal access token, try: <br><br>
        git clone https://<your_pat\)@github.com/Kenza1525/AirBnB_clone.git
<br><br>
## How to use it
Pre-requisites:
 - Python3
 - Git

Our console understands the followingcommands:

|Command|Utility|
|:-------:|:-------:|
|create \(classname\)|Create an object of classname and return id|
|show \(classname\) \(id\)|show the object of type classname with id|
|\(classname\).show(id)|same as the above|
|all \(classname\)| show all objects of type classname|
|\(classname\).all()| same as the above|
|destroy \(classname\) \(id\)| destroy objrct of \(classname\) with \(id\)|
|\(classname\).destroy((id\))| same as the above|
|update \(classname\) \(id\) \(attribute\) \(value\)| change the value of an attribute|
