Name:           b20-515-19		
Version:	    1.0
Release:	    1%{?dist}
Summary:	    Программа студента Шлыкова Павла группы Б20-515
Group:		    Testing
License:	    GPL
URL:		    https://github.com/Sh00ty/OOS_LABS
Source0:	    %{name}-%{version}.tar.gz
BuildRequires:	/bin/rm, /bin/mkdir, /bin/cp
Requires:	    /bin/bash, /usr/bin/date, /bin/yum
BuildArch:      noarch


%description
A test package

%prep
%setup -q

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 b20-515-19 %{buildroot}%{_bindir}
sudo yum install gnuplot

%files
%{_bindir}/b20-515-19

%changelog

* Tue May 23 2023 Shlykov
- Added %{_bindir}/b20-515-19

