# create a folder and give any name

# now open windows powershell and check wherever virtualenv is install or not

# if not installed so install first it

# First Install virtualenv using this command
# cmd:-pip install virtualenv

# after install virtualenv show it is install or not?
# cmd:-virtualenv

# Now create virtual enviorment using this command
# cmd:-virtualenv any_name


# it means it create clone of our orignal python

# after complete this process now its time to activate our clone python
# cmd:-.dir_name\Scripts\activate

# if suppose any error genrate so open windows powershell as admin and type this command
# cmd:- set-exectionpolicy remotesigned
# and press Y for yes
# after return you old windows powershell and write to activate command

# after activate it in corner you can show you dir_name it means you are now
# inside the virtual environment

# now type "python" and press enter now you are inside python
# for exit in python write "exit()" command

# install module to write this command
# cmd:- pip install moduel_name

# show your module is install or not type this command
# cmd:- import module_name

# suppose you want to your old version of pyhon and its old version moduels
# so write this command 
# cmd:- pip freeze > requirements.txt
# this command also use to check the version of your modules

# after type this command and press enter for it a .txt file genrate
# inside this .txt file the moduel name and its version name

# if you want to install old version of moduel or requirement of old version
# so open .txt file find moduel and its version

# now install this moudel and its version type this command
# cmd:- pip install moduel_name==version_name  
# this command run for specific moduel

# suppose you  want to install all the old version of moduel type this command
# cmd:- pip install -r .\requirements.txt
# using this command all the old version of moduel is insall or update

# for exit in virtual enivorment type this command
# cmd:- deactivate

# now we want to create another clone of our orignal python but by defalt
# install or get moduel which is in the orignal python so type this command
# cmd:-virtualenv --system-site-packages any_name


