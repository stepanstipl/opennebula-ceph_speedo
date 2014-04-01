%define pkgname opennebula-ceph_speedo
%define opennebula_user oneadmin
%define opennebula_group oneadmin

Summary:        OpenNebula fast Ceph drivers
Name:           opennebula-ceph_speedo
Version:        0.1.0
Release:        1%{?dist}
License:        MIT license
Group:          System
URL:            https://github.com/stepanstipl/opennebula-ceph_speedo
Packager:       Stepan Stipl <stepan@stipl.net>
Source0:        https://github.com/stepanstipl/opennebula-ceph_speedo/archive/%{version}.tar.gz
Requires:       opennebula-server
Provides:       %{name} = %{version}-%{release}
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%define install_dir /var/lib/one/remotes

%description
Ceph tm and datastore driver for Open Nebula with improved performance

%prep
%setup

%build

%pre

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{install_dir}
cp -ad src/datastore $RPM_BUILD_ROOT%{install_dir}/datastore/ceph_speedo
cp -ad src/tm $RPM_BUILD_ROOT%{install_dir}/tm/ceph_speedo

%post

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,%{opennebula_user},%{opennebula_group},-)

%{install_prefix}/datastore/ceph_speedo
%{install_prefix}/tm/ceph_speedo

%changelog
* Tue Apr 01 2014 Stepan Stipl <stepan@stipl.net> - 0.1.0
- initial creation of this package for OpenNebula ceph_speedo 0.1.0