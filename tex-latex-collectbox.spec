Summary:	Macros to collect and process an macro argument as horizontal box
Summary(pl.UTF-8):	Makra do zbierania i przetwarzania argumentu makra jako poziomego pola
Name:		tex-latex-collectbox
Version:	0.4b
Release:	2
License:	LaTeX Project Public License v1.3+
Group:		Applications/Publishing
Source0:	http://mirrors.ctan.org/macros/latex/contrib/collectbox.zip
# Source0-md5:	169ee2a9a88fadcfb170f7aab33cef34
URL:		https://sourceforge.net/projects/collectbox/
BuildRequires:	/usr/bin/latex
BuildRequires:	rpmbuild(macros) >= 1.751
BuildRequires:	tex(ydoc)
BuildRequires:	unzip
Requires(post,postun):	/usr/bin/texhash
# TODO: use generic
Requires:	texlive-latex
Provides:	tex(collectbox) = %{version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Macros to collect and process an macro argument as horizontal box.

%description -l pl.UTF-8
Makra do zbierania i przetwarzania argumentu makra jako poziomego
pola.

%prep
%setup -q -n collectbox

%build
latex collectbox.ins

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/texmf/{doc,tex}/latex/collectbox

cp -p *.pdf $RPM_BUILD_ROOT%{_datadir}/texmf/doc/latex/collectbox
cp -p *.sty $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/collectbox

%clean
rm -rf $RPM_BUILD_ROOT

%post
%texhash

%postun
%texhash

%files
%defattr(644,root,root,755)
%doc README
%doc %{_datadir}/texmf/doc/latex/collectbox
%{_datadir}/texmf/tex/latex/collectbox
