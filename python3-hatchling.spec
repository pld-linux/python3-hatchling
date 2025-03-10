# Conditional build:
%bcond_without	tests	# unit tests

%define		module	hatchling
Summary:	Modern, extensible Python build backend
Name:		python3-%{module}
Version:	1.27.0
Release:	3
License:	MIT
Group:		Libraries/Python
Source0:	https://pypi.debian.net/hatchling/%{module}-%{version}.tar.gz
# Source0-md5:	6ffb3087c9b6a9ffbfc1bb394f7ed1a8
URL:		https://pypi.org/project/hatchling/
BuildRequires:	python3-build
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-packaging >= 24.2
BuildRequires:	python3-pathspec
BuildRequires:	python3-pluggy
BuildRequires:	python3-trove_classifiers
%if %{with tests}
#BuildRequires:	python3-
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
%description -l pl.UTF-8

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build_pyproject

%if %{with tests}
# use explicit plugins list for reliable builds (delete PYTEST_PLUGINS if empty)
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS= \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/hatchling
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}.dist-info
