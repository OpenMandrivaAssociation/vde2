Name: vde2
Version: 2.1.6
Release: %mkrel 4
Summary: Virtual Distributed Ethernet
Source0: http://prdownloads.sourceforge.net/vde/%{name}-%{version}.tar.bz2
Source1: README.mandriva
License: GPL
Group: Networking/Other
Url: http://vde.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Obsoletes: vde <= 1.5.11
Provides: vde = %{version}-%{release}

%define libname  %mklibname vde 2

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

%package -n %{libname}-devel
Summary: VDE development libraries
Group: Development/Other

%description -n %{libname}-devel
Development files (headers, libraries) for libvde

%prep
%setup -q
cp %SOURCE1 .

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/vdetap
%doc README README.mandriva
%{_mandir}/man1/*.1*

%files -n %{libname}
%{_libdir}/libvde*.so.*

%files -n %{libname}-devel
%{_includedir}/libvde*.h
%{_libdir}/libvde*.so
%{_libdir}/libvde*.*a
%{_libdir}/vde2/libvde*.so
%{_libdir}/vde2/libvde*.*a
