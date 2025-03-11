#
# Conditional build:
%bcond_with	doc		# don't build doc (not provided by package)
%bcond_without	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module	flask-debugtoolbar
Summary:	A port of the Django debug toolbar to Flask
Summary(pl.UTF-8):	Odpowiednik Djangowego debuggera dla Flask
Name:		python-%{module}
Version:	0.9.0
Release:	11
License:	BSD
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/F/Flask-DebugToolbar/Flask-DebugToolbar-%{version}.tar.gz
# Source0-md5:	b471c8320d9a04ffea3abda020570563
URL:		http://flask-debugtoolbar.rtfd.org/
BuildRequires:	rpm-pythonprov
# if py_postclean is used
BuildRequires:	rpmbuild(macros) >= 1.710
%if %{with python2}
BuildRequires:	python-blinker
BuildRequires:	python-distribute
%endif
%if %{with python3}
BuildRequires:	python3-blinker
BuildRequires:	python3-modules
%endif
# Below Rs only work for main package (python2)
#Requires:		python-libs
Requires:	python-modules
Requires:	python-devel-tools
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A port of the Django debug toolbar to Flask

## %description -l pl.UTF-8

%package -n python3-%{module}
Summary:	-
Summary(pl.UTF-8):	-
Group:		Libraries/Python
Requires:	python3-modules
Requires:	python3-devel-tools

%description -n python3-%{module}
A port of the Django debug toolbar to Flask

## %description -n python3-%{module} -l pl.UTF-8

%package apidocs
Summary:	%{module} API documentation
Summary(pl.UTF-8):	Dokumentacja API %{module}
Group:		Documentation

%description apidocs
API documentation for %{module}.

%description apidocs -l pl.UTF-8
Dokumentacja API %{module}.

%prep
%setup -q -n Flask-DebugToolbar-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%if %{with doc}
cd docs
%{__make} -j1 html
rm -rf _build/html/_sources
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/flask_debugtoolbar
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/Flask_DebugToolbar-%{version}-py*.egg-info
%endif
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%{py3_sitescriptdir}/flask_debugtoolbar
%{py3_sitescriptdir}/Flask_DebugToolbar-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/*
%endif
