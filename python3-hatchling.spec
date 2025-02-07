# Conditional build:
%bcond_without	tests	# unit tests

%define		module	hatchling
Summary:	Modern, extensible Python build backend
Name:		python3-%{module}
Version:	1.24.2
Release:	2
License:	MIT
Group:		Libraries/Python
Source0:	https://pypi.debian.net/hatchling/%{module}-%{version}.tar.gz
# Source0-md5:	814948c375ba44603877d032338811ba
URL:		https://pypi.org/project/hatchling/
BuildRequires:	python3-build
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-packaging >= 23.2
BuildRequires:	python3-pathspec
BuildRequires:	python3-trove_classifiers
%if %{with tests}
#BuildRequires:	python3-
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
%description -l pl.UTF-8

%prep
%setup -q -n %{module}-%{version}

%build
%{__python3} -m build --wheel --no-isolation --outdir build-3

%if %{with tests}
# use explicit plugins list for reliable builds (delete PYTEST_PLUGINS if empty)
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS= \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__python3} -m installer --destdir=$RPM_BUILD_ROOT build-3/*.whl
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/hatchling
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}.dist-info
