#!/bin/bash

sudo mount -t ntfs-3g -o rw,uid=bruno,gid=bruno,umask=002 /dev/sda3 /media/bruno/Volume
sudo mount -t ntfs-3g -o rw,uid=bruno,gid=bruno,umask=002 /dev/nvme1n1p3 /media/bruno/"Datenträger 499 GB"
sudo mount -t ntfs-3g -o rw,uid=bruno,gid=bruno,umask=002 /dev/nvme0n1p1 /media/bruno/SN770


