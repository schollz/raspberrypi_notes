# Setup

First create a directory on the Linux root system thats available to users to add/restore from, but seperate from all the other file systems.

sudo mkdir /backup
sudo usermod -a -G users USERNAME
sudo chown root:users /backup
sudo chmod 775 /backup
mkdir /backup/2015


# Backup

Here I use rsync to backup each folder individually. Note: do not backup 'proc' 'lost+found' 'backup' 'mnt' 'sys' 'dev' 'media'

## Backup locally

rsync -avz --delete /baselayers /backup/2015/
rsync -avz --delete /bin /backup/2015/
rsync -avz --delete /boot /backup/2015/
rsync -avz --delete /etc /backup/2015/
rsync -avz --delete /home /backup/2015/
rsync -avz --delete /initrd.img  /backup/2015/
rsync -avz --delete /lib /backup/2015/
rsync -avz --delete /lib64 /backup/2015/
rsync -avz --delete /opt /backup/2015/
rsync -avz --delete /root /backup/2015/
rsync -avz --delete /run /backup/2015/
rsync -avz --delete sbinopt /backup/2015/
rsync -avz --delete /srv /backup/2015/
rsync -avz --delete /tmp /backup/2015/
rsync -avz --delete /usr /backup/2015/
rsync -avz --delete /var /backup/2015/
rsync -avz --delete /vmlinuz /backup/2015/
rsync -avz --delete /www /backup/2015/

## Backup local directory to computer on network through SSH

rsync -avze ssh --delete /example_directory bitnami@ips.colab.duke.edu:/backup/2015/

## Compress

After backing everything up in the folder, it can be compressed.

```
tar cvpzf /backup/2015.tgz /backup/2015/
```

# Restore

## Decompress

If you compressed, you need to decompress! Use

```
tar xvpfz /backup/2015.tgz -C /
```

Note: "When -C is specified, `tar' will change its current directory to DIR before performing any operations.  When this option is used during archive creation, it is order 
sensitive." I.e. It will spit out the folder in tar in the directory relative to the tarball.


## Restore from local to local

Remove ```--dry-run``` to actually do it

```
rsync -av --delete --dry-run /backup/2015/lib /
```

## Restore from network computer to local computer through SSH

Remove ```--dry-run``` to actually do it

```
rsync -ave ssh --delete --dry-run bitnami@ips.colab.duke.edu:/backup/2015/home /
```

