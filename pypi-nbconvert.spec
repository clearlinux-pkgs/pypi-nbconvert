#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-nbconvert
Version  : 6.5.3
Release  : 71
URL      : https://files.pythonhosted.org/packages/ad/2e/5ce9f2a93940604740edb0ac804d874a1bc15b241b31fe608b0fa5b1f6c6/nbconvert-6.5.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/ad/2e/5ce9f2a93940604740edb0ac804d874a1bc15b241b31fe608b0fa5b1f6c6/nbconvert-6.5.3.tar.gz
Summary  : Converting Jupyter Notebooks
Group    : Development/Tools
License  : BSD-3-Clause-Clear
Requires: pypi-nbconvert-bin = %{version}-%{release}
Requires: pypi-nbconvert-data = %{version}-%{release}
Requires: pypi-nbconvert-license = %{version}-%{release}
Requires: pypi-nbconvert-python = %{version}-%{release}
Requires: pypi-nbconvert-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(setuptools)
Patch1: backport-mistune-1.patch
Patch2: backport-mistune-2.patch
Patch3: backport-mistune-3.patch
Patch4: backport-mistune-4.patch

%description
# nbconvert
### Jupyter Notebook Conversion
[![Google Group](https://img.shields.io/badge/-Google%20Group-lightgrey.svg)](https://groups.google.com/forum/#!forum/jupyter)
[![Build Status](https://travis-ci.org/jupyter/nbconvert.svg?branch=main)](https://travis-ci.org/jupyter/nbconvert)
[![Documentation Status](https://readthedocs.org/projects/nbconvert/badge/?version=latest)](https://nbconvert.readthedocs.io/en/latest/?badge=latest)
[![Documentation Status](https://readthedocs.org/projects/nbconvert/badge/?version=stable)](https://nbconvert.readthedocs.io/en/stable/?badge=stable)
[![codecov.io](https://codecov.io/github/jupyter/nbconvert/coverage.svg?branch=main)](https://codecov.io/github/jupyter/nbconvert?branch=main)
[![CircleCI Docs Status](https://circleci.com/gh/jupyter/nbconvert/tree/main.svg?style=svg)](https://circleci.com/gh/jupyter/nbconvert/tree/main)

%package bin
Summary: bin components for the pypi-nbconvert package.
Group: Binaries
Requires: pypi-nbconvert-data = %{version}-%{release}
Requires: pypi-nbconvert-license = %{version}-%{release}

%description bin
bin components for the pypi-nbconvert package.


%package data
Summary: data components for the pypi-nbconvert package.
Group: Data

%description data
data components for the pypi-nbconvert package.


%package license
Summary: license components for the pypi-nbconvert package.
Group: Default

%description license
license components for the pypi-nbconvert package.


%package python
Summary: python components for the pypi-nbconvert package.
Group: Default
Requires: pypi-nbconvert-python3 = %{version}-%{release}

%description python
python components for the pypi-nbconvert package.


%package python3
Summary: python3 components for the pypi-nbconvert package.
Group: Default
Requires: python3-core
Provides: pypi(nbconvert)
Requires: pypi(beautifulsoup4)
Requires: pypi(bleach)
Requires: pypi(defusedxml)
Requires: pypi(entrypoints)
Requires: pypi(jinja2)
Requires: pypi(jupyter_core)
Requires: pypi(jupyterlab_pygments)
Requires: pypi(lxml)
Requires: pypi(markupsafe)
Requires: pypi(mistune)
Requires: pypi(nbclient)
Requires: pypi(nbformat)
Requires: pypi(packaging)
Requires: pypi(pandocfilters)
Requires: pypi(pygments)
Requires: pypi(tinycss2)
Requires: pypi(traitlets)

%description python3
python3 components for the pypi-nbconvert package.


%prep
%setup -q -n nbconvert-6.5.3
cd %{_builddir}/nbconvert-6.5.3
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
pushd ..
cp -a nbconvert-6.5.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1660230818
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
pypi-dep-fix.py . mistune
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pypi-dep-fix.py . mistune
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-nbconvert
cp %{_builddir}/nbconvert-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-nbconvert/4864371bd27fe802d84990e2a5ee0d60bb29e944
python3 -tt setup.py build  install --root=%{buildroot}
pypi-dep-fix.py %{buildroot} mistune
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/jupyter-dejavu
/usr/bin/jupyter-nbconvert

%files data
%defattr(-,root,root,-)
/usr/share/jupyter/nbconvert/templates/asciidoc/conf.json
/usr/share/jupyter/nbconvert/templates/asciidoc/index.asciidoc.j2
/usr/share/jupyter/nbconvert/templates/base/celltags.j2
/usr/share/jupyter/nbconvert/templates/base/display_priority.j2
/usr/share/jupyter/nbconvert/templates/base/jupyter_widgets.html.j2
/usr/share/jupyter/nbconvert/templates/base/mathjax.html.j2
/usr/share/jupyter/nbconvert/templates/base/null.j2
/usr/share/jupyter/nbconvert/templates/basic/conf.json
/usr/share/jupyter/nbconvert/templates/basic/index.html.j2
/usr/share/jupyter/nbconvert/templates/classic/base.html.j2
/usr/share/jupyter/nbconvert/templates/classic/conf.json
/usr/share/jupyter/nbconvert/templates/classic/index.html.j2
/usr/share/jupyter/nbconvert/templates/classic/static/style.css
/usr/share/jupyter/nbconvert/templates/compatibility/display_priority.tpl
/usr/share/jupyter/nbconvert/templates/compatibility/full.tpl
/usr/share/jupyter/nbconvert/templates/lab/base.html.j2
/usr/share/jupyter/nbconvert/templates/lab/conf.json
/usr/share/jupyter/nbconvert/templates/lab/index.html.j2
/usr/share/jupyter/nbconvert/templates/lab/static/index.css
/usr/share/jupyter/nbconvert/templates/lab/static/theme-dark.css
/usr/share/jupyter/nbconvert/templates/lab/static/theme-light.css
/usr/share/jupyter/nbconvert/templates/latex/base.tex.j2
/usr/share/jupyter/nbconvert/templates/latex/conf.json
/usr/share/jupyter/nbconvert/templates/latex/display_priority.j2
/usr/share/jupyter/nbconvert/templates/latex/document_contents.tex.j2
/usr/share/jupyter/nbconvert/templates/latex/index.tex.j2
/usr/share/jupyter/nbconvert/templates/latex/null.j2
/usr/share/jupyter/nbconvert/templates/latex/report.tex.j2
/usr/share/jupyter/nbconvert/templates/latex/style_bw_ipython.tex.j2
/usr/share/jupyter/nbconvert/templates/latex/style_bw_python.tex.j2
/usr/share/jupyter/nbconvert/templates/latex/style_ipython.tex.j2
/usr/share/jupyter/nbconvert/templates/latex/style_jupyter.tex.j2
/usr/share/jupyter/nbconvert/templates/latex/style_python.tex.j2
/usr/share/jupyter/nbconvert/templates/markdown/conf.json
/usr/share/jupyter/nbconvert/templates/markdown/index.md.j2
/usr/share/jupyter/nbconvert/templates/python/conf.json
/usr/share/jupyter/nbconvert/templates/python/index.py.j2
/usr/share/jupyter/nbconvert/templates/reveal/base.html.j2
/usr/share/jupyter/nbconvert/templates/reveal/conf.json
/usr/share/jupyter/nbconvert/templates/reveal/index.html.j2
/usr/share/jupyter/nbconvert/templates/reveal/static/custom_reveal.css
/usr/share/jupyter/nbconvert/templates/rst/conf.json
/usr/share/jupyter/nbconvert/templates/rst/index.rst.j2
/usr/share/jupyter/nbconvert/templates/script/conf.json
/usr/share/jupyter/nbconvert/templates/script/script.j2
/usr/share/jupyter/nbconvert/templates/webpdf/conf.json
/usr/share/jupyter/nbconvert/templates/webpdf/index.pdf.j2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-nbconvert/4864371bd27fe802d84990e2a5ee0d60bb29e944

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
