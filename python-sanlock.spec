Name:           python-sanlock
Version:        5.1.0
Release:        1%{?dist}
Summary:        Python bindings for the sanlock library

License:        GPL-2.0-or-later
URL:            https://github.com/oVirt/python-sanlock
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  sanlock-devel
%if 0%{?with_check}
BuildRequires:  python3-pytest
%endif

%description
Python bindings for the sanlock shared storage lock manager library.
Originally part of the sanlock project, used by oVirt/VDSM.


%package -n python3-sanlock
Summary:        Python 3 bindings for the sanlock library
Requires:       sanlock-lib%{?_isa}

%description -n python3-sanlock
Python 3 bindings for the sanlock shared storage lock manager library.
Originally part of the sanlock project, used by oVirt/VDSM.


%prep
%autosetup


%build
%py3_build


%install
%py3_install


%check
# Tests require a running sanlock daemon; skip them during package build.
# Run them manually with: pytest tests/
%if 0%{?with_check}
export SANLOCK_PRIVILEGED=0
export SANLOCK_RUN_DIR=%{_tmppath}/sanlock-test-%{name}
pytest tests/ -v
%endif


%files -n python3-sanlock
%license COPYING
%doc README.md example.py
%{python3_sitearch}/sanlock%{python3_ext_suffix}
%{python3_sitearch}/sanlock_python-%{version}*.egg-info/


%changelog
* Mon Jun 22 2026 Jean-Louis Dupond <jean-louis@dupond.be> - 5.1.0-1
- Initial standalone release, sourced from sanlock commit 3334fb59
