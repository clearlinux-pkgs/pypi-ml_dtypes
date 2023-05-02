#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-ml_dtypes
Version  : 0.1.0
Release  : 3
URL      : https://files.pythonhosted.org/packages/e8/7e/355b8db0651a2fe74437b578db1afc965b88bedd2116a83308bd7b91af43/ml_dtypes-0.1.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/e8/7e/355b8db0651a2fe74437b578db1afc965b88bedd2116a83308bd7b91af43/ml_dtypes-0.1.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 MPL-2.0-no-copyleft-exception
Requires: pypi-ml_dtypes-license = %{version}-%{release}
Requires: pypi-ml_dtypes-python = %{version}-%{release}
Requires: pypi-ml_dtypes-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(numpy)
BuildRequires : pypi(pybind11)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# ml_dtypes
[![Unittests](https://github.com/jax-ml/ml_dtypes/actions/workflows/test.yml/badge.svg)](https://github.com/jax-ml/ml_dtypes/actions/workflows/test.yml)
[![Wheel Build](https://github.com/jax-ml/ml_dtypes/actions/workflows/wheels.yml/badge.svg)](https://github.com/jax-ml/ml_dtypes/actions/workflows/wheels.yml)
[![PyPI version](https://badge.fury.io/py/ml_dtypes.svg)](https://badge.fury.io/py/ml_dtypes)

%package license
Summary: license components for the pypi-ml_dtypes package.
Group: Default

%description license
license components for the pypi-ml_dtypes package.


%package python
Summary: python components for the pypi-ml_dtypes package.
Group: Default
Requires: pypi-ml_dtypes-python3 = %{version}-%{release}

%description python
python components for the pypi-ml_dtypes package.


%package python3
Summary: python3 components for the pypi-ml_dtypes package.
Group: Default
Requires: python3-core
Provides: pypi(ml_dtypes)
Requires: pypi(numpy)

%description python3
python3 components for the pypi-ml_dtypes package.


%prep
%setup -q -n ml_dtypes-0.1.0
cd %{_builddir}/ml_dtypes-0.1.0
pushd ..
cp -a ml_dtypes-0.1.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1683041337
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-ml_dtypes
cp %{_builddir}/ml_dtypes-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-ml_dtypes/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/ml_dtypes-%{version}/LICENSE.eigen %{buildroot}/usr/share/package-licenses/pypi-ml_dtypes/d7e3ed5ac149ac1e2d2e0f4daff081c1dafef1c0 || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-ml_dtypes/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/pypi-ml_dtypes/d7e3ed5ac149ac1e2d2e0f4daff081c1dafef1c0

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/V3/usr/lib/python3*/*
/usr/lib/python3*/*
