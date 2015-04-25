import os
import sys
from datetime import date

'''
After inserting new disk (use fdisk -l to check if the sda1 is correct):

sudo mkfs.ext4 /dev/sda1
sudo mkdir /c
sudo mount /dev/sda1 /c
sudo chgrp -R users /c
sudo chmod -R g+w /wc

Then add 
/dev/sda1	/c	ext4	defaults	0	2
to /etc/fstab
'''



if len(sys.argv)<2:
	print 'syntax:\n makebackup.py [year|month] folder'
	sys.exit(0)

if sys.argv[1]=='year':
	datefolder = str(date.today().year )
elif sys.argv[1]=='month':
	datefolder = str(date.today().year )+ '-'+ str(date.today().month)
else:
	print 'syntax:\n makebackup.py [year|month] folder'
	sys.exit(0)

backup_folder = str(sys.argv[2]) + '/backup'
print datefolder


os.system('sudo mkdir ' + backup_folder)
os.system('sudo usermod -a -G users pi')
os.system('sudo chown root:users ' + backup_folder)
os.system('sudo chmod 775 ' + backup_folder)
os.system('sudo mkdir ' + backup_folder + '/' + datefolder)
backup_folder = backup_folder + '/' + datefolder

'''
sudo mkdir /backup
sudo usermod -a -G users USERNAME
sudo chown root:users /backup
sudo chmod 775 /backup
mkdir /backup/2015
'''
exclude_folders = ['proc','lost+found','backup','mnt','sys','dev','media','c']
folders = os.listdir('/')
for folder in exclude_folders:
	try:
		folders.remove(folder)
	except:
		pass
		
for folder in folders:
	os.system('rsync -avz --delete /'+folder+' ' + backup_folder + '/')
	
os.system('tar cvpzf ' + backup_folder +'.tgz '+ backup_folder + '/')
	
