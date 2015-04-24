

## 1. Format disk

First find the disk

```bash
sudo fdisk -l
sudo mount -l
```

Its probably /dev/sda and the partition /dev/sda1. 

If its connected, then disconnect it before formatting:

```bash
sudo umount /dev/sda1
```

Format to VFAT (for Windows compatibility):

```bash
sudo apt-get install dosfstools
sudo mkfs.vfat /dev/sda1 -n diskname
```


## 2. Mount the disk

Make a directory

```
sudo mkdir /media/usb0
```

and mount the disk

```
sudo mount /dev/sda1 /media/usb0
```

## 3. Setup SAMBA

Install SAMBA 

```
sudo apt-get install samba samba-common-bin
```

Edit the configuration file at ```/etc/samba/smb.conf``` to including the following:

```bash
workgroup = WORKGROUP
wins support = yes

[PiShare]
 comment=Raspberry Pi Share
 path=/media/usb0
 browseable=Yes
 writeable=Yes
 only guest=no
 create mask=0777
 directory mask=0777
 public=no
```

THen set the password using ```sudo smbpasswd -a pi``` and just use your current password.



## Windows

Note your rpi name, for instance my bash is

```
pi@z_rpibplus / $ 
```
so my rpi name is ```z_rpibplus```.

Now goto Windows Computer -> Map network drive.

In Folder use ```\\IPADDRESS\PiShare```.

Click "Connect using different credentials."

When Windows Security comes up, set the User name to ```z_rpibplus\pi``` and password is the password of ```pi```.

### Sources

[usb drive cheatsheet](https://www.raspberrypi.org/forums/viewtopic.php?t=38429)
[samba help](http://raspberrypihq.com/how-to-share-a-folder-with-a-windows-computer-from-a-raspberry-pi/)
