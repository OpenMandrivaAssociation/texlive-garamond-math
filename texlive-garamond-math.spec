%global tl_name garamond-math
%global tl_revision 61481

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	An OTF math font matching EB Garamond
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/garamond-math
License:	ofl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/garamond-math.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/garamond-math.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Garamond-Math is an open type math font matching EB Garamond (Octavio
Pardo) and EB Garamond (Georg Mayr-Duffner). Many mathematical symbols
are derived from other fonts, others are made from scratch. The metric
is generated with a Python script. Issues, bug reports and other
contributions are welcome.

