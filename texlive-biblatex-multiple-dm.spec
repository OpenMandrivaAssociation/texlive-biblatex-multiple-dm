%global tl_name biblatex-multiple-dm
%global tl_revision 37081

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0.1
Release:	%{tl_revision}.1
Summary:	Load multiple datamodels in BibLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-multiple-dm
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-multiple-dm.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-multiple-dm.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package adds the possibility to BibLaTeX to load data models from
multiple sources.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/biblatex-multiple-dm
%dir %{_datadir}/texmf-dist/tex/latex/biblatex-multiple-dm
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-multiple-dm/README
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-multiple-dm/biblatex-multiple-dm.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-multiple-dm/biblatex-multiple-dm.tex
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-multiple-dm/latexmkrc
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-multiple-dm/makefile
%{_datadir}/texmf-dist/tex/latex/biblatex-multiple-dm/biblatex-multiple-dm.sty
%{_datadir}/texmf-dist/tex/latex/biblatex-multiple-dm/multiple-dm.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-multiple-dm/multiple-dm.dbx
