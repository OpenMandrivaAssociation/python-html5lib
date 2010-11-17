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
