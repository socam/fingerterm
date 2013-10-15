Name: fingerterm
Version: 1.0.3
Release: 1
Summary: A terminal emulator with a custom virtual keyboard
Group: System/Base
License: GPLv2
Source0: %{name}-%{version}.tar.gz
URL: https://github.com/nemomobile/fingerterm
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5OpenGL)
BuildRequires: pkgconfig(Qt5Declarative)
Obsoletes: meego-terminal <= 0.2.2
Provides: meego-terminal > 0.2.2

%description
%{summary}.

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_libdir}/duicontrolpanel/fingertermapplet.desktop


%prep
%setup -q -n %{name}-%{version}


%build
sed -i 's,/opt/fingerterm/,/usr/,' fingerterm.pro
qmake MEEGO_EDITION=nemo
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make INSTALL_ROOT=%{buildroot} install
mkdir -p %{buildroot}/usr/lib/duicontrolpanel
cp %{_builddir}/%{name}-%{version}/fingertermapplet.desktop  %{buildroot}/usr/lib/duicontrolpanel/fingertermapplet.desktop
