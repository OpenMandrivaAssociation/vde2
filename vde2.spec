Name:		vde2
Version:	2.2.2
Release:	%mkrel 2
Summary:	Virtual Distributed Ethernet
Source0:	http://prdownloads.sourceforge.net/vde/%{name}-%{version}.tar.bz2
Source1:	README.mandriva
# Build fixes
Patch0:		vde-2.2.2-string-format.patch
Patch1:		vde-2.2.2-fix-linking.patch
Patch2:		vde-2.2.2-fix-includes.patch
License:	GPL
Group:		Networking/Other
Url:		http://vde.sourceforge.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Obsoletes:	vde <= 1.5.11
Provides:	vde = %{version}-%{release}

%define libname %mklibname vde 2
%define develname %mklibname -d vde

%description
VDE is a virtual network that can be spawned over a set of physical
computer over the Internet

VDE connects together:
  (1) real GNU-linux boxes (tuntap)
  (2) virtual machines: UML-User Mode Linux, qemu, bochs, MPS.

VDE can be used:
  (i) to create a general purpose tunnel (every protocol that runs
    on a Ethernet can be put into the tunnel)
  (ii) to connect a set of virtual machine to the Internet with no
    need of free access of tuntap
  (iii) to support mobility: a VDE can stay interconnected despite
    of the change of virtual cables, i.e. the change of IP addresses
    and interface in the real world

%package -n %{libname}
Summary: VDE libraries
Group: Networking/Other

%description -n %{libname}
Library files for VDE

%package -n %{develname}
Summary: VDE development libraries
Group: Development/Other
Provides: %{name}-devel
Provides: vde-devel = %{version}-%{release}
Provides: libvde-devel = %{version}-%{release}
Provides: libvde2-devel = %{version}-%{release}
Provides: %{_lib}vde2-devel = %{version}-%{release}
Obsoletes: %{_lib}vde2-devel

%description -n %{develname}
Development files (headers, libraries) for libvde

%prep
%setup -q
%patch0 -p1 -b .strfmt
%patch1 -p1 -b .link
%patch2 -p1 -b .limits
cp %SOURCE1 .

%build
aclocal
autoconf -f
libtoolize
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/*
%{_sbindir}/vde_tunctl
%{_libdir}/vdetap
%doc README README.mandriva
%{_mandir}/man*/*.*
%{_sysconfdir}/vde2/libvdemgmt/asyncrecv.rc
%{_sysconfdir}/vde2/libvdemgmt/closemachine.rc
%{_sysconfdir}/vde2/libvdemgmt/openmachine.rc
%{_sysconfdir}/vde2/libvdemgmt/sendcmd.rc
%{_sysconfdir}/vde2/vdecmd
%{_libdir}/vde2/vde_l3/bfifo.so
%{_libdir}/vde2/vde_l3/pfifo.so
%{_libdir}/vde2/vde_l3/tbf.so

%files -n %{libname}
%{_libdir}/libvde*.so.*

%files -n %{develname}
%{_includedir}/libvde*.h
%{_libdir}/libvde*.so
%{_libdir}/libvde*.*a
%{_libdir}/vde2/libvde*.so
%{_libdir}/vde2/libvde*.*a
%{_libdir}/vde2/vde_l3/bfifo.la
%{_libdir}/vde2/vde_l3/pfifo.la
%{_libdir}/vde2/vde_l3/tbf.la
