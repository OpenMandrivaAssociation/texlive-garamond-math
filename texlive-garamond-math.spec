Name:		texlive-garamond-math
Version:	61481
Release:	1
Summary:	An OTF math font matching EB Garamond
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/garamond-math
License:	ofl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/garamond-math.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/garamond-math.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Garamond-Math is an open type math font matching EB Garamond
(Octavio Pardo) and EB Garamond (Georg Mayr-Duffner). Many
mathematical symbols are derived from other fonts, others are
made from scratch. The metric is generated with a Python
script. Issues, bug reports and other contributions are
welcome.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/fonts/opentype/public/garamond-math
%doc %{_texmfdistdir}/doc/fonts/garamond-math

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
