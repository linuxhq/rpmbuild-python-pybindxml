%global date 20160120
%global commit cb27d964fb8e146f5d40cfd9c00026c267880714
%global short_commit %(c=%{commit}; echo ${c:0:7})

%define         __python /usr/bin/python
%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           python-pybindxml
Version:        %{date}git%{short_commit}
Release:        1%{?dist}
Summary:        Library to handle parsing BIND statistics XML into Python objects.
Group:          Development/Languages
License:        MIT
URL:            https://github.com/jforman/pybindxml
Source0:        https://github.com/jforman/pybindxml/archive/%{commit}/pybindxml-%{commit}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
Requires:       python, python-beautifulsoup4 >= 4.3
BuildRequires:  python-setuptools

%description
Library to handle parsing BIND statistics XML into Python objects.

%prep
%setup -q -n pybindxml-%{commit}
%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install --root %{buildroot} --install-data=%{_datadir}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE README.md
%{python_sitelib}/*

%changelog
* Thu Jan 21 2016 Taylor Kimball <taylor@linuxhq.org> - 20160121gitcb27d96-1
- Initial spec.
