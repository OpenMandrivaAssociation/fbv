######################################################
# SpecFile: fbv.spec 
# Generato: http://www.mandrivausers.ro/
# MRB-Falticska Florin
######################################################
%define debug_package	%{nil}
%define  distsuffix mrb
%define	name	fbv
%define	version	1.0b
%define	release	69

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Framebuffer image viewer
Group:		Graphical desktop/Other
License:	GPLv2
URL:		http://s-tech.elsat.net.pl/fbv
Source0:	http://s-tech.elsat.net.pl/fbv//%name-%version.tar.gz
#patch from alt-linux
Patch0:		fbv-nocenter.patch
Patch1:		giflib.patch
BuildRequires:	libjpeg-devel 
BuildRequires:	libpng-devel 
BuildRequires:	giflib-devel
BuildRequires:	X11-devel
BuildRequires:	xorg-x11
BuildRequires:	zlib-devel
# missing common provides for libs ..
Requires:	%{_lib}jpeg8
Requires:	%{_lib}gif6
%if %{mdvver} >= 201210
Requires:	%{_lib}png15
%else
Requires:	libpng
%endif

%description
A simple program to view pictures on a framebuffer console. It
supports PNG, JPEG, GIF and BMP files.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

iconv -f iso8859-1 -t utf-8 ChangeLog > ChangeLog.conv && \
	mv -f ChangeLog.conv ChangeLog

%build
./configure --prefix=/usr --mandir=%_mandir

sed -i 's|LIBS.*|LIBS=-lpng -ljpeg -lgif|' Make.conf
sed -i 's|setjmp(png_ptr->jmpbuf)|setjmp(png_jmpbuf(png_ptr))|' png.c

%make CFLAGS="$CFLAGS $RPM_OPT_FLAGS"

%install
mkdir -p $RPM_BUILD_ROOT%_bindir
mkdir -p $RPM_BUILD_ROOT%_mandir/man1

%makeinstall_std


%files
%_bindir/*
%_mandir/man1/*
%doc ChangeLog README TODO



