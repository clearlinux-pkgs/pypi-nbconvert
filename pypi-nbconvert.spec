#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
# autospec version: v5
# autospec commit: c02b2fe
#
Name     : pypi-nbconvert
Version  : 7.16.3
Release  : 93
URL      : https://files.pythonhosted.org/packages/5a/f5/6f33d6bb0f39b11237c353d112f03e8bfdc9d1f5d59589f3a4211d401001/nbconvert-7.16.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/5a/f5/6f33d6bb0f39b11237c353d112f03e8bfdc9d1f5d59589f3a4211d401001/nbconvert-7.16.3.tar.gz
Summary  : Converting Jupyter Notebooks (.ipynb files) to other formats.  Output formats include asciidoc, html, latex, markdown, pdf, py, rst, script.  nbconvert can be used both as a Python library (`import nbconvert`) or as a command line tool (invoked as `jupyter nbconvert ...`).
Group    : Development/Tools
License  : BSD-3-Clause BSD-3-Clause-Clear
Requires: pypi-nbconvert-bin = %{version}-%{release}
Requires: pypi-nbconvert-data = %{version}-%{release}
Requires: pypi-nbconvert-license = %{version}-%{release}
Requires: pypi-nbconvert-python = %{version}-%{release}
Requires: pypi-nbconvert-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(hatchling)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# nbconvert
### Jupyter Notebook Conversion
[![Build Status](https://github.com/jupyter/nbconvert/actions/workflows/tests.yml/badge.svg?query=branch%3Amain++)](https://github.com/jupyter/nbconvert/actions/workflows/tests.yml/badge.svg?query=branch%3Amain++)
[![Documentation Status](https://readthedocs.org/projects/nbconvert/badge/?version=latest)](https://nbconvert.readthedocs.io/en/latest/?badge=latest)

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
%setup -q -n nbconvert-7.16.3
cd %{_builddir}/nbconvert-7.16.3
pushd ..
cp -a nbconvert-7.16.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1711240351
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-nbconvert
cp %{_builddir}/nbconvert-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-nbconvert/a2539650cfdf8871b9737115b20d5f8e48e8ab7b || :
python3 -m installer --destdir=%{buildroot} dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
python3 -m installer --destdir=%{buildroot}-v3 dist/*.whl
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
/usr/share/jupyter/nbconvert/templates/base/cell_id_anchor.j2
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
/usr/share/jupyter/nbconvert/templates/lab/mermaidjs.html.j2
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
/usr/share/jupyter/nbconvert/templates/reveal/cellslidedata.j2
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
/usr/share/package-licenses/pypi-nbconvert/a2539650cfdf8871b9737115b20d5f8e48e8ab7b

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
