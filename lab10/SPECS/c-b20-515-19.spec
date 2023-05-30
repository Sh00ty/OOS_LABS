Name:           c-b20-515-19		
Version:	    1.0
Release:	    1%{?dist}
Summary:	    Программа студента Шлыкова Павла группы Б20-515
Group:		    Testing
License:	    GPL
URL:		    https://github.com/Sh00ty/OOS_LABS
Source0:	    %{name}-%{version}.tar.gz
BuildRequires:	gcc

%global debug_package %{nil}

%description
A test package

%prep
%setup -q

%build
gcc -O2 -o c-b20-515-19 c-b20-515-19.c

%install
mkdir -p %{buildroot}%{_bindir}
cp c-b20-515-19 %{buildroot}%{_bindir}
sudo rpm -i ~/rpmbuild/RPMS/noarch/b20-515-19-1.0-1.el8.noarch.rpm --force

%files
%{_bindir}/c-b20-515-19

%changelog
* Tue May 23 2023 Shlykov
- Added %{_bindir}/c-b20-515-19

