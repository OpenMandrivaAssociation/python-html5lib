%define modulename	html5lib

Summary:	A python based HTML parser/tokenizer based on the WHATWG HTML5 specification
Name:		python-%{modulename}
Version:	0.90
Release:	%mkrel 1
Group:		Development/Python
License:	MIT
URL:		http://code.google.com/p/html5lib/
BuildArch:	noarch
Source0:	http://html5lib.googlecode.com/files/%{modulename}-%{version}.zip
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:	python-devel python-setuptools

%description
A python based HTML parser/tokenizer based on the WHATWG HTML5
specification for maximum compatibility with major desktop web browsers.

%prep
%setup -q -n %{modulename}-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{python_sitelib}
%{__python} setup.py install --skip-build --root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc examples README
%{py_puresitedir}/%{modulename}/*.py
%{py_puresitedir}/%{modulename}/filters
%{py_puresitedir}/%{modulename}/serializer
%{py_puresitedir}/%{modulename}/treebuilders
%{py_puresitedir}/%{modulename}/treewalkers
%{py_puresitedir}/%{modulename}-%{version}-*.egg-info


%changelog
* Wed Nov 17 2010 Funda Wang <fwang@mandriva.org> 0.90-1mdv2011.0
+ Revision: 598148
- new version 0.90
- repack zip file

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.11.1-2mdv2010.0
+ Revision: 442182
- rebuild

* Fri Jan 30 2009 Jérôme Soyer <saispo@mandriva.org> 0.11.1-1mdv2009.1
+ Revision: 335607
- Add BR
- import python-html5lib


