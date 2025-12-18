%define modulename	html5lib

Summary:	A python based HTML parser/tokenizer based on the WHATWG HTML5 specification
Name:		python-%{modulename}
Version:	1.1
Release:	4
Group:		Development/Python
License:	MIT
URL:		https://code.google.com/p/html5lib/
BuildArch:	noarch
Source0:	https://github.com/html5lib/html5lib-python/archive/%{version}.tar.gz

BuildRequires:  python3-distribute python3-devel
BuildRequires:  python%{pyver}dist(pip)

%description
A python based HTML parser/tokenizer based on the WHATWG HTML5
specification for maximum compatibility with major desktop web browsers.

%prep
%autosetup -p1 -n html5lib-python-%{version}

%install
python setup.py install --root=%{buildroot}

%files
%{py3_puresitedir}/%{modulename}/*.py*
%{py3_puresitedir}/%{modulename}/filters
%{py3_puresitedir}/%{modulename}/treeadapters
%{py3_puresitedir}/%{modulename}/treebuilders
%{py3_puresitedir}/%{modulename}/treewalkers
%{py3_puresitedir}/%{modulename}/_trie
%{py3_puresitedir}/%{modulename}-%{version}-*.egg-info
