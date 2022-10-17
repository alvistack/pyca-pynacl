# Copyright 2022 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

Name: python-pynacl
Epoch: 100
Version: 1.4.0
Release: 1%{?dist}
Summary: Python binding to the libsodium library
License: Apache-2.0
URL: https://github.com/pyca/pynacl/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: gcc
BuildRequires: python-rpm-macros
BuildRequires: python3-cffi
BuildRequires: python3-cython
BuildRequires: python3-devel
BuildRequires: python3-pycparser
BuildRequires: python3-setuptools

%description
PyNaCl is a Python binding to libsodium, which is a fork of the
Networking and Cryptography library. These libraries have a stated goal
of improving usability, security and speed. It supports Python 3.6+ as
well as PyPy 3.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitearch} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitearch}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-pynacl
Summary: Python binding to the libsodium library
Requires: python3
Provides: python3-pynacl = %{epoch}:%{version}-%{release}
Provides: python3dist(pynacl) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-pynacl = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(pynacl) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-pynacl = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(pynacl) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-pynacl
PyNaCl is a Python binding to libsodium, which is a fork of the
Networking and Cryptography library. These libraries have a stated goal
of improving usability, security and speed. It supports Python 3.6+ as
well as PyPy 3.

%files -n python%{python3_version_nodots}-pynacl
%license LICENSE
%{python3_sitearch}/*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-pynacl
Summary: Python binding to the libsodium library
Requires: python3
Provides: python3-pynacl = %{epoch}:%{version}-%{release}
Provides: python3dist(pynacl) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-pynacl = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(pynacl) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-pynacl = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(pynacl) = %{epoch}:%{version}-%{release}

%description -n python3-pynacl
PyNaCl is a Python binding to libsodium, which is a fork of the
Networking and Cryptography library. These libraries have a stated goal
of improving usability, security and speed. It supports Python 3.6+ as
well as PyPy 3.

%files -n python3-pynacl
%license LICENSE
%{python3_sitearch}/*
%endif

%changelog
