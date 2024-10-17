%define develname %mklibname -d vde
%define _disable_ld_no_undefined 1

Name:		vde2
Version:	2.3.2
Release:	15
Summary:	Virtual Distributed Ethernet
License:	GPL
Group:		Networking/Other
Url:		https://vde.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/vde/%{name}-%{version}.tar.bz2
Source1:	README.mandriva
# Build fixes
Patch0:		vde-2.2.2-string-format.patch
Patch1:		vd2-2.3.2-clang.patch
Patch2:		vde-2.3.2-openssl-1.1.patch
Obsoletes:	vde <= 1.5.11
Provides:	vde = %{version}-%{release}
Conflicts:	%{develname} < 2.3.2
Obsoletes:	%{mklibname vde 2} < 2.3.2
BuildRequires:	pkgconfig(python3)

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

%files
%doc README README.mandriva
%{_bindir}/*
%{_sbindir}/vde_tunctl
%{_libexecdir}/vdetap
%{_mandir}/man*/*.*
%{_sysconfdir}/vde2/libvdemgmt/asyncrecv.rc
%{_sysconfdir}/vde2/libvdemgmt/closemachine.rc
%{_sysconfdir}/vde2/libvdemgmt/openmachine.rc
%{_sysconfdir}/vde2/libvdemgmt/sendcmd.rc
%{_sysconfdir}/vde2/vdecmd
%{_libdir}/vde2/libvde*.so
%{_libdir}/vde2/vde_l3/bfifo.so
%{_libdir}/vde2/vde_l3/pfifo.so
%{_libdir}/vde2/vde_l3/tbf.so

#-----------------------------------------------------

%define vdehist_major 0
%define libvdehist %mklibname vdehist %{vdehist_major}

%package -n %{libvdehist}
Summary:	VDE libraries
Group:		Networking/Other
Conflicts:	%{mklibname vde 2} < 2.3.2

%description -n %{libvdehist}
Library files for VDE.

%files -n %{libvdehist}
%{_libdir}/libvdehist.so.%{vdehist_major}*

#-----------------------------------------------------

%define vdemgmt_major 0
%define libvdemgmt %mklibname vdemgmt %{vdemgmt_major}

%package -n %{libvdemgmt}
Summary:	VDE libraries
Group:		Networking/Other
Conflicts:	%{mklibname vde 2} < 2.3.2

%description -n %{libvdemgmt}
Library files for VDE.

%files -n %{libvdemgmt}
%{_libdir}/libvdemgmt.so.%{vdemgmt_major}*

#-----------------------------------------------------

%define vdeplug_major 3
%define libvdeplug %mklibname vdeplug %{vdeplug_major}

%package -n %{libvdeplug}
Summary:	VDE libraries
Group:		Networking/Other
Conflicts:	%{mklibname vde 2} < 2.3.2

%description -n %{libvdeplug}
Library files for VDE.

%files -n %{libvdeplug}
%{_libdir}/libvdeplug.so.%{vdeplug_major}*

#-----------------------------------------------------

%define vdesnmp_major 0
%define libvdesnmp %mklibname vdesnmp %{vdesnmp_major}

%package -n %{libvdesnmp}
Summary:	VDE libraries
Group:		Networking/Other
Conflicts:	%{mklibname vde 2} < 2.3.2

%description -n %{libvdesnmp}
Library files for VDE.

%files -n %{libvdesnmp}
%{_libdir}/libvdesnmp.so.%{vdesnmp_major}*

#-----------------------------------------------------

%package -n %{develname}
Summary:	VDE development libraries
Group:		Development/Other
Requires:	%{libvdehist} = %{version}-%{release}
Requires:	%{libvdemgmt} = %{version}-%{release}
Requires:	%{libvdeplug} = %{version}-%{release}
Requires:	%{libvdesnmp} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	vde-devel = %{version}-%{release}
Provides:	libvde-devel = %{version}-%{release}
Provides:	libvde2-devel = %{version}-%{release}
Conflicts:	%{name} < 2.3.2

%description -n %{develname}
Development files (headers, libraries) for libvde

%files -n %{develname}
%{_includedir}/libvde*.h
%{_libdir}/libvde*.so
%{_libdir}/pkgconfig/vde*.pc

#-----------------------------------------------------
%package -n python-%{name}
Summary:	Python bindings to the VDE library
Group:		Networking/Other

%description -n python-%{name}

%files -n python-%{name}
%{_prefix}/lib/python*/site-packages/*

#-----------------------------------------------------

%prep
%autosetup -p1
cp %{SOURCE1} .

%build
%configure
# Makefiles aren't SMP ready
%make_build -j1

%install
%make_install
