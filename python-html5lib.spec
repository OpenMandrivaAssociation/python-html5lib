%define modulename	html5lib

Summary:	A python based HTML parser/tokenizer based on the WHATWG HTML5 specification
Name:		python-%{modulename}
Version:	1.0b3
Release:	4
Group:		Development/Python
License:	MIT
URL:		http://code.google.com/p/html5lib/
BuildArch:	noarch
Source0:	https://pypi.python.org/packages/source/h/html5lib/html5lib-%{version}.tar.gz

BuildRequires:	python2-devel python2-setuptools
BuildRequires:  python3-distribute python3-devel

%rename		python3-html5lib

%description
A python based HTML parser/tokenizer based on the WHATWG HTML5
specification for maximum compatibility with major desktop web browsers.

%package -n python2-html5lib
Summary:        A python based HTML parser/tokenizer based on the WHATWG HTML5 specification
Group:          Development/Python
Requires:       python2
 
%description -n python2-html5lib
A python based HTML parser/tokenizer based on the WHATWG HTML5
specification for maximum compatibility with major desktop web browsers.


%prep
%setup -q -c

mv %{modulename}-%{version} python2
cp -r python2 python3

%install
pushd python2
%{__python2} setup.py install --root=%{buildroot}
popd

pushd python3
%{__python3} setup.py install --root=%{buildroot}
popd

%files -n python-html5lib 
%{py3_puresitedir}/%{modulename}/*.py
%{py3_puresitedir}/%{modulename}/filters
%{py3_puresitedir}/%{modulename}/serializer
%{py3_puresitedir}/%{modulename}/treeadapters
%{py3_puresitedir}/%{modulename}/treebuilders
%{py3_puresitedir}/%{modulename}/treewalkers
%{py3_puresitedir}/%{modulename}/trie
%{py3_puresitedir}/%{modulename}-%{version}-*.egg-info

%files -n python2-html5lib
%{py2_puresitedir}/%{modulename}/*.py
%{py2_puresitedir}/%{modulename}/filters
%{py2_puresitedir}/%{modulename}/serializer
%{py2_puresitedir}/%{modulename}/treeadapters
%{py2_puresitedir}/%{modulename}/treebuilders
%{py2_puresitedir}/%{modulename}/treewalkers
%{py2_puresitedir}/%{modulename}/trie
%{py2_puresitedir}/%{modulename}-%{version}-*.egg-info
