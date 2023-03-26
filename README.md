# Linux-Git-Python-IF4-ESILV
TD de python git linux A4 IF


# Project
Here is my dashboard: http://3.84.168.90:8050

# TD 1

## Exercise 1 : Move Around 
### 1 : Go to the root directory
```
~$ pwd 
```
Result : 
```
/home/anita-louise
```
### 2. Display the content of the current (root) directory
```
~$ ls
```
Result :
```
Bureau Documents Images Modèles Musique Public snap Téléchargements Vidéos
```
### 3. Check your current location
```
~$ pwd
```
Result : 
Here we can see the location 
```
/home/anita-louise
```
### 4. Try to create a directory named test
```
~$ cd Documents
~/Documents$ mkdir test
~/Documents$ ls
```
Result : 
```
test
```
### 5. Go to the general home directory (should contain folders named after each user)
```
~/Documents$ cd ..
~$ cd ..
/home$ ls
```
Result :
```
anita-louise
```
Because I have 1 user 
### 6. Go to your home directory
```
/homme$ cd ..
/$ pwd
```
Result : 
```
bin boot cdrom dev etc hom lib lib32 lib64 libx32 lost+found media mnt opt proc root run sbin snap srv swapfile sys tmp usr var
```
### 7. Go back to the general home directory (located "just above")
```
/$ cd home
/home$ pwd
```
Result :
```
/home
```
### 8. Go again "just above", you should be back to the root directory
```
/home$ cd ..
```
### 9. Go directly to your home directory (named after you). It should be a very simple command, which take no name as parameter of the path
```
/$ cd
~$ pwd
```
Result :
```
/home/anita-louise
```
### 10. Try to create a directory named test
question made at 4
### 11. Go into this new directory
```
~$ cd Documents 
~/Documents$ cd test
~/Documents/test$ pwd
```
Result :
```
/home/anita-louise/Documents/test
```
### 12. Check your current location
```
~/Documents/test$ pwd
```
Result : 
```
/home/anita-louise/Documents/test
```
## Exercise 2: Create, Rename, copy, delete

### 1. Go to your home directory (should be named after you, you might be there by default)
```
~/Documents/test$ cd
```

### 2. Check your current location
```
~$ pwd 
```
Result : 
```
/home/anita-louise
```

### 3. Create a folder linux_ex_1
```
~$ mkdir linux_ex_1
```

### 4. Go into this folder
```
~$ cd linux_ex_1
```

### 5. Create an empty text file named [first_name]_[last_name].txt (e.g. alexis_bogroff.txt)
```
~/linux_ex_1$ touch anita-louise_ward.txt
~.linux_ex_1$ ls
```
Result : 
```
anita-louise_ward.txt
```

### 6. Create a folder notes
```
~/linux_ex_1$ mkdir notes
```

### 7. Move your text file into this folder
```
~/linux_ex_1$ mv anita-louise_ward.txt /home/anita-louise/linux_ex_1/notes 
```

### 8. Rename the text file by appending the current year [first_name]_[last_name]_[current_year].txt
```
~/linux_ex_1$ cd notes 
~/linux_ex_1/notes$ mv anita-louise_ward.txt anita-louise_ward_2023.txt
```

### 9. Make a copy of this folder, name it notes_2022
```
~/linux_ex_1/notes$ cd ..
~/linux_ex_1$ cp -R notes notes_2022
```

### 10. Delete the first folder (notes) using the verbose option
``` 
~/linux_ex_1$ rm -rfv notes 
~/linux_ex_1$ ls
```
Result : 
```
notes_2022
```

## Exercise 3: Create and run a script

### 1. Create a script script_1.sh in the folder linux_ex_1
```
~/linux_ex_1$ nano script_1.sh
````
### 2. In the script, write the commands that would output the following : Script running please wait ... Done.
```
echo "Script running please wait..."
echo "Done."
```
### 3. Quit editing and save the script
```
ctr + x then "O" then "Enter"
```
### 4. Display the content of the script (using a command, not from an editor)
```
~/linux_ex_1$ cat script_1.sh
```
### 5. Run the script
```
~/linux_ex_1$ chmod +x script_1.sh
~/linux_ex_1$ ./script_1.sh
```

## Exercise 4: Accessing or modifying a file : permissions and root privilege
### 1. Create a file credentials in the folder linux_ex_1
```
~/linux_ex_1$ nano credentials
```
(a) Write any kind of (fake) personal information within the file
```
Write anything
ctrl + x then "O" then enter
```
(b) Display the file content
```
~/linux_ex_1$ cat credentials
```
(c) Display the current permissions
```
~/linux_ex_1$ ls -l credentials
```
Result : 
```
-rw-rw-r-- 1 anita-louise anita-louise 26 janv. 31 08:41 credentials
```
### 2. Change the current permissions to : read only for all users
(a) Display the new permissions
```
~/linux_ex_1$ chmod a=r credentials
~/linux_ex_1$ ls -l credentials
```
Result : 
```
-r--r--r-- 1 anita-louise anita-louise 26 janv. 31 08:41 credentials
```
(b) Modify and save the file
```
~/linux_ex_1$ nano credentials

if we don't have permission we can do ~/linux_ex_1$ chmod a+w credentials
```
__"a+w"__ to allow writing "w" for all "a" user 
(c) Display the file content
```
~/Linux_ex_1$ cat credentials
```
### 3. Change the permissions back to read and write for all users
```
~/linux_ex_1$ chmod a+rw credentials
```
Like before but with a __"r"__ we do recursive 
(a) Display the new permissions
```
~/linux_ex_1$ ls -l credentials
```
Result :
```
-rw-rw-rw- 1 anita-louise anita-louise 35 janv. 31 08.54 credentials
```
(b) Modify and save the file
```
~/linux_ex_1$ nano credentials
```
(c) Display the file content
```
~/linux_exe_1$ cat credentials
```
### On the same file :
### 1. Add the execute permission to the owner
```
~/Linux_ex_1$ chmod u+x credentials
```
(a) Display the new permissions
```
~/linux_ex_1$ ls -l credentials
```
Result : 
```
-rwxrw-rw- 1 anita-louise anita-louise 50 janv. 31 08.51 credentials
```
### 2. Remove the read permission to other users
```
~/linux_ex_1$ chmod o-r credentials
```
(a) Display the new permissions
```
~/linux_ex_1$ ls -l credentials
```
Result : 
```
-rwxrw--w- anita-louise anita-louise 50 janv. 31 08.58 credentials
```
### 3. Change the permissions to read, write and execute for all users
```
~/linux_ex_1$ chmod a+rwx credentials
```
(a) Display the new permissions
```
~/linux_ex_1$ ls -l credentials
```
Result : 
```
-rwxrwxrwx 1 anita-louise anita-louise 50 janv. 31 08.58 credentials
```
## Exercise 4:.2 Access root files
### 1. Go to the root folder
```
~/linux_ex_1$ cd /
```
### 2. Create a file in root user mode named .private_file
```
/$ sudo nano .private_file
```
(a) Write some information in the file
(b) Display the file content
```
/$ cat .private_file
```
(c) Display all the files in the folder including hidden files
```
/$ ls -a
```
### 3. Modify the file in normal user mode
Can't write 
(a) Write some new information in the file
(b) Display the file content
### 4. Modify the file in root user mode
```
/$ sudo nano .private_file
```
(a) Write some new information in the file
(b) Display the file content
```
/$ cat .private_file
```
### 5. Change permissions to read, write and execute for all users
```
/$ sudo chmod a+rwx .private_file
```
(a) Modify the file content in normal user mode
(b) Display the file content
```
/$ cat .private_file
```
Result :
```
-rwxrwxrwx 1 root root 36 janv. 09:57 .private_file
```
## Exercise 4:.3 Change a file owner
### 1. Change permissions of .private_file to read and write for all users, in normal user mode
```
/$ chmod 666 .private_file
```
Result : 
```
-rw-rw-rw- 1 root root 36 janv. 31 09:57 .private_file
```

### 2. Set the new file owner as the current user
```
/$ chown $USER .private_file
```
```
-rwxrw-r--    10    root   root 2048    Jan 13 07:11 afile.exe
?UUUGGGOOOS   00  UUUUUU GGGGGG ####    ^-- date stamp and file name are obvious ;-)
^ ^  ^  ^ ^    ^      ^      ^    ^
| |  |  | |    |      |      |    \--- File Size
| |  |  | |    |      |      \-------- Group Name (for example, Users, Administrators, etc)
| |  |  | |    |      \--------------- Owner Acct
| |  |  | |    \---------------------- Link count (what constitutes a "link" here varies)
| |  |  | \--------------------------- Alternative Access (blank means none defined, anything else varies)
| \--\--\----------------------------- Read, Write and Special access modes for [U]ser, [G]roup, and [O]thers (everyone else)
\------------------------------------- File type flag
```
Result : 
```
-rw-rw-rw- 1 anita-louise root 36 janv. 31 09/57 .private_file
```

## Exercise 4:.4 Manage Packages (tools / functions)
### 1. Update your main package manager named apt
```
/$ sudo apt update
```
### 2. Upgrade apt
```
/$ sudo apt upgrade
```
### 3. Install the package cmatrix
```
/$ sudo apt install cmatrix
```
### 4. Launch cmatrix
```
/$ cmatrix 
```
### 5. Quit cmatrix
```
CTRL + C
```
#### 6. Install the package tmux
```
/$ sudo apt install tmux
```
### 7. Launch tmux
```
/$ tmux
```
### 8. Say "Hello session 0" using bash in your current tmux session
```
echo "Hello session 0"
```
### 9. Launch cmatrix in your current tmux session
```
cmatrix
```
### 10. Detach from the current tmux session (without stopping cmatrix)
```
Ctrl + B + D
```
### 11. Create a new tmux session
```
Ctrl + B + %
```
### 12. Say "Hello session 1" using bash in your new tmux session
### 13. Detach from the current tmux session
### 14. List all running sessions
```
tmux list-sessions
```
### 15. Attach again to session 0
```
tmux attach-session -t session0
```
### 16. Detach again
### 17. Attach again to session 1
### 18. Detach again
### 19. List all running sessions
### 20. Kill all tmux sessions and quit tmux
```
tmux kill-session -a
```
### 21. List all sessions
```
tmux list-sessions
```
## Exercise 4:.5 Use functions arguments / parameters
### 1. Display the cmatrix help function
```
cmatrix -h
```
### 2. Launch cmatrix and make it display white characters (in place of the green)
```
cmatrix -C white
```
### 3. Re-launch cmatrix and slow down the speed of characters actualization
```
cmatrix -s 5
```
### 4. Stop cmatrix
```
CTRL + C
```
### 5. Launch cmatrix with both :
— A slow speed of characters actualization
— Blue characters
```
cmatrix -s 5 -C blue
```
### 6. Display cmatrix manual (different from the help notice)
```
man cmatrix
```
### 7. Display the tmux help function
```
tmux -h
```
### 8. Display the tmux manual
```
man tmux
```

# TD 2 Fundamental Linux functionalities

## Exercise 1: Access general computer informations
### 1. Put system up to date
```
sudo apt update && sudo apt upgrade
```
2. Display
— Linux version
```
cat /etc/*-release or lsb_release -a
```
— Current processes and memory usage associated
```
top 
```
— Display it in a more pleasant way ("more readable for humans")
```
htop
```
But, you need to do
```
sudo snap install htop  #version 3.2.1
sudo apt install htop #version 3.0.5-7build2
```
— Number of processors
```
nproc
```
— L1, L2 and L3 cache size
```
lscpu | grep 'Cache'
```
— Disk space
```
df -h
```
— Monted devices
```
lsblk
```
— Connected usb devices
```
lsusb
```
— Hostname
```
hostname
```

## Exercise 2: Shell - Variables and scripts scope
### 1. Create a variable x and assign it the short text piri pimpin
```
x="piri pimpin"
```
### 2. Display the value of this variable
```
echo $x
```
###3. Add to this value the following text piri pimpon
It should contain the following : piri pimpim piri pimpon
```
x="$x piri pimpin"
```
### 4. Create a folder named my_programs, then enter into that folder
```
mkdir my_programs && cd my_programs
```
### 5. Create a script named pilou that displays pilou pilou
```
echo "echo pilou pilou" > pilou
```
### 6. Run this script
```
bash pilou
```
### 7. Make this script executable
```
chmod +x pilou
```
### 8. Run the script by writting its name only
```
./pilou
```
### 9. Programs called from the terminal are usually found thanks to a variable named PATH
Display the content of the variable PATH
```
echo $PATH
```
### 10. Add the path of your current location to the global variable PATH
```
export PATH="$PATH:$(pwd)"
```
### 11. When you are sure of the result, export it
```
export PATH
```
### 12. Go to your home directory
```
cd ~
```
### 13. Run your script by writting its name only
```
pilou
```
### 14. Change the value of the PATH in the .profile file in order to make it permanent
```
echo 'export PATH="$PATH:$(pwd)"' >> ~/.profile
```
### 15. Create a new shell and run your script using its name only
```
bash
pilou
```

## Exercise 3: Scheduling task - daemon
### 1. Create a script say_hello.sh
```
touch say_hello.sh
```
— Make it write the current date and time followed by ’Hello’
— It should write it in a file named ’hellos.txt’
— Each new output should be appened to the file (it shouldn’t remove previous hellos)
```
date +"%c - Hello" >> hellos.txt
or
echo "$(date) Hello" >> hellos.txt
```
### 2. Make the script executable
```
chmod +x say_hello.sh
```
### 3. Use crontab to schedule the running of the script every minute
```
crontab -e
* * * * * /home/anita-louise/my_programs/say_hello.sh
```
To make the command work, you must reboot the system. So restart and not shut down the VM.

Press the "i" key on your keyboard to enter insert mode. You should see "-- INSERT --" appear at the bottom of your text editor to indicate that you are in insert mode.

Press the "Esc" key to exit insert mode.

Note that the :wq command saves and exits the file at the same time. If you just want to save the file without leaving it, type :w instead of :wq. If you want to exit without saving, type :q.

To check status 
```
systemctl status cron
```
## Exercise 4: Hashing
### 1. Create a folder named hash_checksum. Go into this folder
```
mkdir hash_checksum
```
### 2. Inside this folder, create two files named .sensible_addresses and .sensible_passwords
```
cd hash_checksum 
touch .sensible_addresses .sensible_passwords
```
### 3. Display the list of files of the folder
```
ls
```
We cannot see the files because they are hidden.

### 4. Still inside the folder hash_checksum, create a script named gentle_script.sh. This script should display the following text "Have a good day"
```
echo '#!/bin/bash' > gentle_script.sh
echo 'echo "Have a good day"' >> gentle_script.sh
chmod +x gentle_script.sh
```
### 5. Run the script
```
./gentle_script.sh
```
### 6. Compute the sha256sum of gentle_script. Store it into a file named log_sha
```
sha256sum gentle_script.sh > log_sha
```
### 7. Now corrupt the file by adding a line of code that deletes any file starting with : ".sensible"
```
echo 'rm -f .sensible*' >> gentle_script.sh
```
### 8. Compute again the sha256sum of gentle_script. Store it into the log_sha file
```
sha256sum gentle_script.sh >> log_sha
```
### 9. Run the script
```
./gentle_script.sh
```
### 10. Display again the list of files of the folder
```
ls
```
### 11. Display the log_sha content : are the hashes any different ?
```
cat log_shat
```
## Exercise 5: Compressing
### 1. Install the QPDF free command-line program.
```
sudo apt-get install qpdf
```
Part of this program is the zlib-flate command that compress and uncompress files using the deflate algorithm.
### 2. Create a directory "compress", go into this directory
```
mkdir compress && cd compress
```
### 3. Create a first file "hello" whose content is "Hello"
```
echo "Hello" > hello
```
### 4. Compute the deflate compression (level 1) of this file. Store the compressed file size into a file log_compress
```
zlib-flate -compress -level 1 < hello > hello.deflate && echo "hello $(wc -c < hello.deflate)" >> log_compress
```
### 5. Create a second file "hello_multiple" whose content is 1000 lines of "Hello" 2
```
yes Hello | head -1000 > hello_multiple
```
### 6. Compute the deflate compression (level 1) of this file. Store the compressed file size into a file log_compress
```
zlib-flate -compress -level 1 < hello_multiple > hello_multiple.deflate && echo "hello_multiple $(wc -c < hello_multiple.deflate)" >> log_compress
```
### 7. Create a third file "hello_mulitple_i" whose content is 1000 lines of "Hello i" (i varying from 1 to 100)
```
for i in $(seq 1 1000); do echo "Hello $i"; done > hello_multiple_i
```
### 8. Compute the deflate compression (level 1) of this third file. Store the compressed file size into log_compress
```
zlib-flate -compress -level 1 < hello_multiple_i > hello_multiple_i.deflate && echo "hello_multiple_i $(wc -c < hello_multiple_i.deflate)" >> log_compress
```
### 9. Display the content of log_compress
```
cat log_compress
```
### 10. Compute the compression ratio of each file, also display it as a simple
fraction (e.g. 12.6 => 10 :1)
```
echo "Compression ratio (fractional):"
for file in hello hello_multiple hello_multiple_i; do
  original_size=$(wc -c < $file)
  compressed_size=$(wc -c < ${file}.deflate)
  ratio=$(bc <<< "scale=2; $compressed_size/$original_size")
  fraction=$(bc <<< "scale=0; $original_size/$compressed_size")
  echo "$file: $ratio ($fraction : 1)"
done

```
### 11. Analyse the results

## Ex 6 

# TD3/9: Work with text manipulation tools in Linux
## Exercise 1: Grep and awk on tabular data
### 1. Display the list of files and folders at the root using ls -l
```
ls -l /
```
### 2. In a pipeline (using |), append a grep instruction to only display informations of bin
```
ls -l / | grep bin
```
###3. Append an awk instruction to only display the size of bin
```
ls -l / | grep bin | awk '{print $5}'
```
### 4. Now rather extract the month, day and year of creation of the folder bin
```
ls -l / | grep bin | awk '{print $6, $7, $8}'
```
###5. Now rearrange the instruction to get the following output format : 2020- Oct-26 (from original data : Oct 26 2020)
```
ls -l / | grep bin | awk '{print $8"-"$6"-"$7}'
```
## Exercise 2: Grep with Regex, and sed on unstructured data
### 1. Run the following command : 
```
curl https ://en.wikipedia.org/wiki/List_of_cyberattacks > cyberattacks.txt
```
### 2. Use grep to extract all the lines that contain the keyword "meta"
```
grep "meta" cyberattacks.txt
```
### 3. Now only extract "meta" and the first following word. You might use grep options to enable the use of regex (Regular Expressions) 1
```
cat cyberattacks.txt | grep -oP '(?=meta ).+(?<=meta )[^ ]*'
OU 
cat cyberattacks.txt | grep -oP "meta \w*=\"\w*"
```

See https://regexr.com/

### 4. Only extract the follwing word (but not the keyword "meta")
```
grep -o -E "meta [[:alpha:]]+" cyberattacks.txt | cut -d' ' -f2
```
### 5. Let’s now try more interesting (yet complex) patterns. You might use vim to open the file and look for useful patterns. Let’s extract the introduction — We could ask grep to catch the paragraph corresponding to a sentence that is only present in the introduction. 
Try to run the following command : 
```
cat cyberattacks.txt | grep -P ’A cyberattack is’
```
— This does not work since the source code is here different from what is visible on the web page. 
Now try the following : 
```
cat cyberattacks.txt | grep -P ’A <a href="/wiki/Cyberattack" title="Cyberattack">cyberattack</a> is any type’ 
```

— It is now working, but what if the text evolves over time ? 
Try the following instead :
```
cat cyberattacks.txt | grep -A1 ’mw-content-text’ | grep -v ’mw-content-text’
```
This is based on the text above that seems to be more stable.
### 6. Your turn
— Extract the tab title
— Make a list of cyber attacks based on section titles
```
cat cyberattacks.txt | grep -o -E "<title>.*</title>" | cut -d'>' -f2 | cut -d'-' -f1
cat cyberattacks.txt | grep -P "(?=title).+(?<=/title)"
```

with -P we put in regrex mode so search by tag.
https://www.rexegg.com/regex-lookarounds.html
-o : display only the corresponding part of the text

# TD Linux API

## Exercise 1:.1 curl
```
curl https://opendomesday.org/api/1.0/county/
curl https://opendomesday.org/api/1.0/place/2346/
curl https://opendomesday.org/api/1.0/manor/181/
```

## Exercise 1:.2 curl and grep
Let’s try to get the ids for all the places in Derbyshire !
```
curl -s 'https://opendomesday.org/api/1.0/county/' | jq '.[] | select(.name == "Derbyshire") | .places[]'
```
"jq" is used to manipulate and process JSON data 

## Exercise 1:.3 curl, grep and for
Now that we have ids for all the places in Derbyshire, we can load all their
details...

And from their details, we can list all the details of their manors.
Go grep the data !

```
derbyshire_place_ids=$(curl -s 'https://opendomesday.org/api/1.0/county/' | jq '.[] | select(.name == "Derbyshire") | .places[]')
for id in $derbyshire_place_ids; do
  curl -s "https://opendomesday.org/api/1.0/place/${id}/" | jq '.manors[]'
done
```

## Exercise 1:.4 curl, grep, for and sed
Now that we have a heap of raw data, we will extract the interesting parts.
In our case we want to count the geld paid by each manor and compare it to
the number of ploughs it owns.
— Can you find the corresponding json fields ?
— Then you can list these numbers for each manor in Derbyshire.
— And format this in a proper comma-separated values (CSV) file.
```
echo "Manor ID,Geld,Ploughs" > derbyshire_manors.csv
for id in $derbyshire_place_ids; do
  place_data=$(curl -s "https://opendomesday.org/api/1.0/place/${id}/")
  manor_ids=$(echo "$place_data" | jq '.manors[]')
  for manor_id in $manor_ids; do
    manor_data=$(curl -s "https://opendomesday.org/api/1.0/manor/${manor_id}/")
    geld=$(echo "$manor_data" | jq '.geld')
    ploughs=$(echo "$manor_data" | jq '.ploughs')
    echo "${manor_id},${geld},${ploughs}" >> derbyshire_manors.csv
  done
done
```

## Exercise 1:.5 discover new commands
The CSV file you created could be loaded in Excel. But do you have one ?
Use your search skills to find a way to sum values in a column and provide
the final result.
```
awk -F, 'NR>1 {sum += $2} END {print sum}' derbyshire_manors.csv
```

## Exercise 1:.6 Bonus

Use Vim to write a single bash script that does all of these actions

```
echo "Checking data for various URLs:"
curl -s 'https://opendomesday.org/api/1.0/county/'
curl -s 'https://opendomesday.org/api/1.0/place/2346/'
curl -s 'https://opendomesday.org/api/1.0/manor/181/'


echo "Getting Derbyshire place IDs:"
derbyshire_place_ids=$(curl -s 'https://opendomesday.org/api/1.0/county/' | jq '.[] | select(.name == "Derbyshire") | .places[]')

echo "Getting Derbyshire manor details:"
echo "Manor ID,Geld,Ploughs" > derbyshire_manors.csv
for id in $derbyshire_place_ids; do
  place_data=$(curl -s "https://opendomesday.org/api/1.0/place/${id}/")
  manor_ids=$(echo "$place_data" | jq '.manors[]')
  for manor_id in $manor_ids; do
    manor_data=$(curl -s "https://opendomesday.org/api/1.0/manor/${manor_id}/")
    geld=$(echo "$manor_data" | jq '.geld')
    ploughs=$(echo "$manor_data" | jq '.ploughs')
    echo "${manor_id},${geld},${ploughs}" >> derbyshire_manors.csv
  done
done

echo "Calculating the sum of the Geld column:"
awk -F, 'NR>1 {sum += $2} END {print sum}' derbyshire_manors.csv
```

# TD 3 GIT Local Git Filesystem & Commits

## Exercise 1: Configure Git
### 1. Check that Git is installed on your environment.
```
git --version
```
### 2. Configure your name and e-mail globally.
```
git config --global user.name "Your Name"
git config --global user.email "youremail@example.com"
```
### 3. Check that Git has correctly recorded these two pieces of information.
```
git config --list
```
hint : All Git commands have a -h flag to display the corresponding help.
Look there for the option of the git config command that lists all Git
configuration.

## Exercise 2: Basic workflow with a single file
### 1. Create a git repository
```
git init
```

### 2. Check that git has correctly initialized a repository by displaying the files within your current folder 
```
ls -la
```
### 3. Check the current git status
```
git status
```
### 4. Create a text file named “readme.md” whose content is “# Test repository”
```
echo "# Test repository" > readme.md
```
### 5. Check the current git status
```
git status
```
### 6. Stage the file
```
git add readme.md
```

### 7. Check the current git status
```
git status
```

### 8. Commit the file
```
git commit -m "Add readme.md"
```

### 9. Check the current git status
```
git status
```
### 10. Check the git logs
```
git log
```
### 11. Which informations are displayed?
commit hash, Author, Date, and commit message.

## Exercise 3: Basic workflow with multiple files treated separately
### 1. Create two empty python files named “main.py” and “functions.py”
```
touch main.py functions.py
```
### 2. Check the current git status
```
git status
```
### 3. Stage only the file “main.py”
```
git add main.py
```
#### 4. Check the current git status
```
git status
```
### 5. Commit the file with an appropriate message
```
git commit -m "Add main.py"
```
### 6. Check the current git status
```
git status
```
### 7. Now stage and commit the file “functions.py”
```
git add functions.py
git commit -m "Add functions.py"
```
### 8. Check the current git status
```
git status
```
### 9. Check the git logs
```
git log
```
## Exercise 4: Basic workflow with multiple files treated all at once
```
# 1. Create three empty files named “requirements.txt”, “.gitignore” and “.private”
touch requirements.txt .gitignore .private

# 2. Check the current git status
git status

# 3. Stage all the files at once
git add .

# 4. Check the current git status
git status

# 5. Commit the current staged files
git commit -m "Add requirements.txt, .gitignore, and .private"

# 6. Check the current git status
git status

# 7. Check the git logs where each log is displayed on a single line
git log --oneline
```
## Exercise 5: Private files
```
# 1. Emulate a temporary empty file by creating a file named “temp.ipynb”
touch temp.ipynb

# 2. Check the current git status
git status

# 3. Add an instruction to .gitignore to prevent git from tracking this temp file
echo "temp.ipynb" >> .gitignore

# 4. Check the current git status
git status

# 5. Create other temporary files named “temp.aux” and “temp.log”
touch temp.aux temp.log

# 6. Check the current git status
git status

# 7. Change your instruction in .gitignore to prevent git from tracking any file which name starts with “temp”
echo "temp.*" > .gitignore

# 8. Check the current git status
git status

# 9. Now let’s consider your personal notes will be added to the “.private” folder. Use the “exclude” git file to prevent git from tracking this “.private” folder
echo ".private/" >> .git/info/exclude
```

## Exercise 6: Difference between versions
```
# 1. Add an online description of your repository in the “readme.md” file
echo "This is a test repository for Git exercises." >> readme.md

# 2. Stage your “readme.md” file
git add readme.md

# 3. Display the changes in your root directory since the last commit (not just the current status)
git diff --staged

# 4. Commit your change
git commit -m "Update readme.md with a description"

# 5. Display the changes since the last commit
git diff

# 6. Display again the changes in your root directory since the last commit
git diff

# 7. Change some words in the description of the “readme.md”
echo "This is an example repository for Git exercises." > readme.md

# 8. Display the changes since the last commit
git diff
```

## Exercise 7: Undo
```
# 1. Suppress all your files.
rm -rf *

# 2. Use Git to restore your files.
git checkout .

# 3. Backup your Git repository elsewhere (pretending a copy exists on another colleague’s computer or on a remote server).
cd ..
cp -R your_project your_project_backup
cd your_project

# 4. Suppress your root directory, create a new empty one and use your backup to restore everything.
cd ..
rm -rf your_project
cp -R your_project_backup your_project
cd your_project

# 5. Unstage your first file
git restore --staged readme.md

# 6. Commit your two file changes directly, without staging them.
git commit -a -m "Commit changes directly"

# 7. Check your commit log history. Do you see your new commit?
git log

# 8. Without affecting your Git repository, set your root directory state as of the snapshot of your first commit.
git checkout HEAD~2

# 9. Check your commit log history. You do not see all commits, do you? How can you see all of them?
git reflog

# 10. Return to the snapshot of your last commit.
git checkout HEAD@{1}

# 11. Undo your second commit by adding a new commit that reverts it.
git revert HEAD~1

# 12. Check the content of your root directory. Have your previous changes disappeared?
ls

# 13. Check your commit log history. Do you see your revert commit?
git log

# 14. Remove the last 2 commits from the history.
git reset HEAD~2

# 15. Check the content of your root directory. Have your previous changes disappeared?
ls

# 16. Check your commit log history. Have you lost the last 2 commits?
git log
```

## Exercise 8: Aliases
```
# 1. Create a “s” alias for the git status command.
git config --global alias.s status

# 2. Create a “co” alias for the git checkout command.
git config --global alias.co checkout

# 3. Create a “b” alias for the git branch command.
git config --global alias.b branch

# 4. Create a “ci” alias for the git commit command.
git config --global alias.ci commit

# 5. Create a “dog” alias for the git log –all –decorate –oneline –graph command.
git config --global alias.dog "log --all --decorate --oneline --graph"

# 6. Create a “dag” alias for the git log –all –decorate –graph command.
git config --global alias.dag "log --all --decorate --graph"

# 7. Create a “list” alias for the git diff-tree –no-commit-id –name-only -r command.
git config --global alias.list "diff-tree --no-commit-id --name-only -r"

# 8. Create a “unstage” alias for the git reset HEAD – command.
git config --global alias.unstage "reset HEAD --"

# 9. Create a “last” alias for the git log -1 HEAD command.
git config --global alias.last "log -1 HEAD"
```

## Exercise 9: Hashing
```
# 1. Create a root directory.
mkdir hashing_example
cd hashing_example

# 2. Create a text file inside whose content is “Hello World”.
echo "Hello World" > hello_world.txt

# 3. What is the size of the file?
wc -c hello_world.txt

# 4. Display the file content on the screen.
cat hello_world.txt

# 5. Compute the SHA-1 hash of the file content.
sha1sum hello_world.txt

# 6. What hash would Git compute on this file?
git hash-object hello_world.txt

# 7. Create a second file whose content is what Git would really consider when saving your first file.
echo -en "blob 11\0Hello World" > hello_world_git.txt

# 8. Compute the SHA-1 hash of this second file and check it is equal to the Git hash of your first file.
sha1sum hello_world_git.txt
```

## Exercise 10: Compressing
```
# 1. Create an empty Git repository in your root directory (if you have accidentally already created a Git repository in your root directory, delete it before).
cd ..
rm -rf git_compress_example
mkdir git_compress_example
cd git_compress_example
git init

# 2. Check that Git is aware of your 2 files but does not track them yet.
cp ../hashing_example/hello_world.txt .
cp ../hashing_example/hello_world_git.txt .
git status

# 3. Check that no object is stored yet in the objects subdirectory of your Git repository.
find .git/objects

# 4. Create a directory inside the objects subdirectory of your Git repository, whose name is the first two characters of the SHA-1 hash computed in the previous exercise.
sha1=$(sha1sum hello_world_git.txt | awk '{print $1}')
mkdir -p .git/objects/${sha1:0:2}

# 5. Install the QPDF free command-line program.
# Follow instructions on http://qpdf.sourceforge.net/ or install using package manager

# 6. Create a file inside the directory that you have just created, whose content is the deflate compression (level 1) of your second file and whose name is the last 38 characters of the SHA-1 hash computed in the previous exercise.
zlib-flate -compress < hello_world_git.txt > .git/objects/${sha1:0:2}/${sha1:2}

# 7. Check that Git successfully considers this file as one of its inner object.
git cat-file -t $sha1
git cat-file -s $sha1
git cat-file -p $sha1

# 8. Backup your Git repository and create a new one.
cd ..
cp -R git_compress_example git_compress_example_backup
rm -rf git_compress_example
mkdir git_compress_example
cd git_compress_example
git init

# 9. Stage your first file in Git and check that its name and content are identical to yours.
cp ../hashing_example/hello_world.txt .
git add hello_world.txt
git hash-object hello_world.txt

# 10. Create another text file whose content is 100 lines of “Hello Mister i” (i varying from 1 to 100).
for i in {1..100}; do echo "Hello Mister $i" >> hello_mister.txt; done

# 11. Stage this new file in Git and check that the compression ratio on this second example is better than on the first one.
git add hello_mister.txt
new_file_size=$(git ls-files --stage hello_mister.txt | awk
```

# TD 4 : GIT BRANCHES
## Exercise 1: Clone a Git repository
```
git clone <repository URL>
```
## Exercise 2: Push files to common repository
```
git branch <your-name>
git checkout <your-name>
nano your-name>.txt
git add <your-name>.txt
git commit -m "Add file created by <your-name>"
git push origin <your-name>
```

## Exercise 3: Merge simple changes
```
git checkout main
git config pull.rebase false
git merge anita-louiseWard
git commit -m "Merge anita-louiseWard into main"
git pull
git push
```

## Exercise 4: Resolve merge conflicts

```
git checkout <your-name>
nano README.md
git add README.md
git commit -m "Update README.md with new text"
git checkout main
git pull origin main
git merge <branch-name>
# We creat a conflict but we editing the readme to correct that
git push origin master
```

Voici le readme propre a anita-louiseWard

## Exercise 5: Take latest changes from master in local branch

```
git checkout main
git pull origin main
git checkout <your-branch-name>
git merge main
git add README.md
git commit -m "Merge main to branch"
git push origin <your-branch-name>
```

## Exercise 6: Delete a branch
```
git branch -d <branch-name>
git push origin --delete <branch-name>
```

## Exercise 7: Rebase interactively to have a clean history
```
git checkout main
git pull
git checkout <your-branch-name>
echo "" > README.md
echo "Git interactive rebase" > README.md
nano README.md
echo "Changing Multiple Commit Messages" >> README.md
sed -i '11d' README.md
sed -i '10i Changing Multiple Commit Messages' README.md
echo "Created by here_ur_name" >> README.md
git rebase -i HEAD~n
#n the number of commit that you do
git push -u origin <your-branch-name>
```

## Exercise 8: Create and approve a Merge/Pull Request
```
git checkout main
git pull origin main
git checkout <your-branch-name>
git rebase main
git push -f origin <your-branch-name>
```
