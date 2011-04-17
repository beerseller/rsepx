Summary: Run applications on separate X session 
Name: rsepx
Version: 0.1
Release: 0.1%{?dist}
License: GPL
Group: Applications/Games
URL: http://beerseller.ath.cx/
Source0: %{_sourcedir}/%{name}-%{version}.tar.gz
BuildArch: noarch
%description
Run applications on separate X session 

%prep
%setup

%build

%install
rm -rf %{buildroot}
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/rsepx/create.d
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/rsepx/rc.d
cp rsepx $RPM_BUILD_ROOT%{_bindir}
cp -R conf/* $RPM_BUILD_ROOT%{_sysconfdir}/rsepx/
cp *.desktop $RPM_BUILD_ROOT%{_datadir}/applications/

%clean
rm -rf %{buildroot}
%post
if [ ! -f %{_bindir}/rsepx-wine ]
then
  ln -s %{_bindir}/rsepx %{_bindir}/rsepx-wine
fi
%preun
rm %{_bindir}/rsepx-wine
%files
%defattr(-, root, root)
%doc
%{_bindir}/*
%{_datadir}/*
%{_sysconfdir}/*
