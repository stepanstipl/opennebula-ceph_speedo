opennebula-ceph_speedo
======================

Ceph tm &amp; datastore driver for Open Nebula with improved performance, based on original Ceph open nebula drivers.

These drivers allows fast image cloning by using clone features of RBD 2 format and quick creation of empty images, by using rbd-fuse to mount and format images directly (avoiding super slow DD stuff).

Requirements
------------
- Tested on CentOS 6
- Requires rbd-fuse v0.81 and newer (older does not suppose exposing individual image) 
- Requires mounted correct RBD pool in $RBD_DIR datastore property, defaults to /var/tmp/rbd, this directory must be writable for oneadmin user
- Oneadmin nebula user must be member of 'fuse' group
- All images that you're trying to work with should be RBD version 2 

Installation
------------
- Configure Ceph storage according to `http://docs.opennebula.org/4.4/administration/storage/ceph_ds.html`
- Install RPM package opennebula-ceph_speedo on OpenNebula master
- Change your storage `TM_MAD` and `DS_MAD` providers to `ceph_speedo`
- Create rbd tem dir and make sure `rbd-fuse ${RBD_DIR} -p one -r ${IMAGE_NAME} works when run as oneadmin user (requires working cephx auth, rbd-fuse uses client.admin key)
- Make sure to convert images you want to work with to RBD 2 format

Issues
------
- RPM package will try resync scripts by running `onehost sync -f`, if you see scripts failing for whatever reason try to run this manually on OpenNebula master as oneadmin.
