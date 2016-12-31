#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : LibVNCServer
Version  : 0.9.11
Release  : 3
URL      : https://github.com/LibVNC/libvncserver/archive/LibVNCServer-0.9.11.tar.gz
Source0  : https://github.com/LibVNC/libvncserver/archive/LibVNCServer-0.9.11.tar.gz
Summary  : A library for easy implementation of a VNC server.
Group    : Development/Tools
License  : GPL-2.0 MPL-2.0
Requires: LibVNCServer-bin
Requires: LibVNCServer-lib
BuildRequires : libgcrypt-dev
BuildRequires : libgpg-error-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : openssl-dev
BuildRequires : pkgconfig(gnutls)
BuildRequires : pkgconfig(gtk+-2.0)
BuildRequires : pkgconfig(libsystemd)

%description
[![Build Status](https://travis-ci.org/LibVNC/libvncserver.svg?branch=master)](https://travis-ci.org/LibVNC/libvncserver)

%package bin
Summary: bin components for the LibVNCServer package.
Group: Binaries

%description bin
bin components for the LibVNCServer package.


%package dev
Summary: dev components for the LibVNCServer package.
Group: Development
Requires: LibVNCServer-lib
Requires: LibVNCServer-bin
Provides: LibVNCServer-devel

%description dev
dev components for the LibVNCServer package.


%package lib
Summary: lib components for the LibVNCServer package.
Group: Libraries

%description lib
lib components for the LibVNCServer package.


%prep
%setup -q -n libvncserver-LibVNCServer-0.9.11

%build
export LANG=C
export SOURCE_DATE_EPOCH=1483217269
%autogen --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/libvncserver-config

%files dev
%defattr(-,root,root,-)
/usr/include/rfb/keysym.h
/usr/include/rfb/rfb.h
/usr/include/rfb/rfbclient.h
/usr/include/rfb/rfbconfig.h
/usr/include/rfb/rfbproto.h
/usr/include/rfb/rfbregion.h
/usr/lib64/libvncclient.so
/usr/lib64/libvncserver.so
/usr/lib64/pkgconfig/libvncclient.pc
/usr/lib64/pkgconfig/libvncserver.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libvncclient.so.1
/usr/lib64/libvncclient.so.1.0.0
/usr/lib64/libvncserver.so.1
/usr/lib64/libvncserver.so.1.0.0
