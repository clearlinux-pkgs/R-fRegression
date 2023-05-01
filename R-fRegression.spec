#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-fRegression
Version  : 4021.83
Release  : 41
URL      : https://cran.r-project.org/src/contrib/fRegression_4021.83.tar.gz
Source0  : https://cran.r-project.org/src/contrib/fRegression_4021.83.tar.gz
Summary  : Rmetrics - Regression Based Decision and Prediction
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-fBasics
Requires: R-lmtest
Requires: R-polspline
Requires: R-timeDate
Requires: R-timeSeries
BuildRequires : R-fBasics
BuildRequires : R-lmtest
BuildRequires : R-polspline
BuildRequires : R-timeDate
BuildRequires : R-timeSeries
BuildRequires : buildreq-R

%description
modelling. It implements a wrapper for several regression models available 
  in the base and contributed packages of R.

%prep
%setup -q -n fRegression
cd %{_builddir}/fRegression

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1660231993

%install
export SOURCE_DATE_EPOCH=1660231993
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/fRegression/DESCRIPTION
/usr/lib64/R/library/fRegression/INDEX
/usr/lib64/R/library/fRegression/Meta/Rd.rds
/usr/lib64/R/library/fRegression/Meta/features.rds
/usr/lib64/R/library/fRegression/Meta/hsearch.rds
/usr/lib64/R/library/fRegression/Meta/links.rds
/usr/lib64/R/library/fRegression/Meta/nsInfo.rds
/usr/lib64/R/library/fRegression/Meta/package.rds
/usr/lib64/R/library/fRegression/NAMESPACE
/usr/lib64/R/library/fRegression/NEWS.md
/usr/lib64/R/library/fRegression/R/fRegression
/usr/lib64/R/library/fRegression/R/fRegression.rdb
/usr/lib64/R/library/fRegression/R/fRegression.rdx
/usr/lib64/R/library/fRegression/help/AnIndex
/usr/lib64/R/library/fRegression/help/aliases.rds
/usr/lib64/R/library/fRegression/help/fRegression.rdb
/usr/lib64/R/library/fRegression/help/fRegression.rdx
/usr/lib64/R/library/fRegression/help/paths.rds
/usr/lib64/R/library/fRegression/html/00Index.html
/usr/lib64/R/library/fRegression/html/R.css
/usr/lib64/R/library/fRegression/obsolete/src/LmTests.f
/usr/lib64/R/library/fRegression/obsolete/src/Makevars
/usr/lib64/R/library/fRegression/obsolete/src/MarsModelling.f
/usr/lib64/R/library/fRegression/tests/doRUnit.R
/usr/lib64/R/library/fRegression/unitTests/Makefile
/usr/lib64/R/library/fRegression/unitTests/runTests.R
/usr/lib64/R/library/fRegression/unitTests/runit.LPP2005.R
/usr/lib64/R/library/fRegression/unitTests/runit.RegressionModelling.R
/usr/lib64/R/library/fRegression/unitTests/runit.TermPlots.R
/usr/lib64/R/library/fRegression/unitTests/runit.TimeSeries.R
/usr/lib64/R/library/fRegression/unitTests/runit.polymars.R
/usr/lib64/R/library/fRegression/unitTests/runit.regFit.R
/usr/lib64/R/library/fRegression/unitTests/runit.terms.R
