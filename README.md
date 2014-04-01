opennebula-ceph_speedo
======================

Ceph tm &amp; datastore driver for Open Nebula with improved performance, based on original Ceph open nebula drivers.

These drivers allows fast image cloning by using clone features of RBD 2 format and quick creation of empty images, by using rbd-fuse to mount and format images directly (avoiding super slow DD stuff).

Requirements
------------
- Tested on CentOS 6
- Requires rbd-fuse v0.78 and newer (older version has bug preventing listing images [http://ceph.com/releases/v0-78-released/] - rbd-fuse: fix enumerate_images overflow, memory leak (Ilya Dryomov) - See more at: http://ceph.com/releases/v0-78-released/#sthash.tkCFntpY.dpuf]
- Requires mounted correct RBD pool in `/data/cephtmp/rbd` datastore property
- Requires sudo rule allowing oneadmin to run mkfs on nebula nodes listed in `BRIDGE_LIST` property
- All images that you're trying to work with should be RBD version 2 

Installation
------------
- Configure Ceph storage according to `http://docs.opennebula.org/4.4/administration/storage/ceph_ds.html`
- Install RPM package opennebula-ceph_speedo on OpenNebula master
- Change your storage `TM_MAD` and `DS_MAD` providers to `ceph_speedo`
- Make sure to create sudo rule for oneadmin on all the machines in `BRIDGE_LIST`: `oneadminALL=(root) NOPASSWD:/sbin/mkfs*`
- Make sure to convert images you want to work with to RBD 2 format

Issues
------
- RPM package will try resync scripts by running `onehost sync -f`, if you see scripts failing for whatever reason try to run this manually on OpenNebula master as oneadmin.
