#
# Conditional build:
%bcond_without	emacs	# without emacs subpackage
%bcond_without	x	# without X11 support 
%bcond_without	tk	# without Tcl/Tk support
#
# --without x11 implies --without tk
%{!?with_x:%undefine	with_tk}

%define		p4ver	3.06
%define		sver	3.12

Summary:	The Objective Caml compiler and programming environment
Summary(pl.UTF-8):	Kompilator OCamla (Objective Caml) oraz środowisko programistyczne
Name:		ocaml
Version:	3.12.1
Release:	3
Epoch:		1
License:	distributable
Group:		Development/Languages
Source0:	http://caml.inria.fr/distrib/%{name}-%{sver}/%{name}-%{version}.tar.bz2
# Source0-md5:	227a3daaedb150bf5037a3db01f5bf42
Source1:	http://caml.inria.fr/distrib/%{name}-%{sver}/%{name}-%{sver}-refman.html.tar.gz
# Source1-md5:	93cd91f525441eb7e94cc49b9b64bab0
Source2:	http://caml.inria.fr/distrib/%{name}-%{sver}/%{name}-%{sver}-refman.ps.gz
# Source2-md5:	a9c17db6ffd400c5ea00c6d51cbf56bf
Source3:	http://caml.inria.fr/distrib/%{name}-%{sver}/%{name}-%{sver}-refman.info.tar.gz
# Source3-md5:	8cf24c4f69c6f9c9f9cc1edb9b18f6cb
Source4:	ftp://ftp.inria.fr/INRIA/Projects/cristal/camlp4/camlp4-%{p4ver}-manual.html.tar.gz
# Source4-md5:	21370bae4e7f6435b38aeb21db7ce8bb
Source5:	ftp://ftp.inria.fr/INRIA/Projects/cristal/camlp4/camlp4-%{p4ver}-manual.dvi.gz
# Source5-md5:	035915d1a530aa7ec9b194d9a7d258eb
Source6:	ftp://ftp.inria.fr/INRIA/Projects/cristal/camlp4/camlp4-%{p4ver}-tutorial.html.tar.gz
# Source6-md5:	96d8eb4ca5abd58c9a280ba59f73b192
Source7:	ftp://ftp.inria.fr/INRIA/Projects/cristal/camlp4/camlp4-%{p4ver}-tutorial.dvi.gz
# Source7-md5:	fcd87c235109364242a0c9ccf176dff8
Source8:	http://www.ocaml.info/ocaml_sources/pure-fun-1.0.6.tar.bz2
# Source8-md5:	94eac3fa1ac51b8ada344b04839cb43c
Source9:	http://www.ocaml.info/ocaml_sources/ds-contrib.tar.gz
# Source9-md5:	77fa1da7375dea1393cc0b6cd802d7e1
Patch0:		%{name}-db3.patch
Patch1:		%{name}-CFLAGS.patch
Patch2:		%{name}-as_needed.patch
Patch3:		%{name}-gas.patch
URL:		http://caml.inria.fr/
BuildRequires:	db-devel >= 4.1
%{?with_tk:BuildRequires:	tk-devel}
%{?with_x:BuildRequires:	xorg-lib-libX11-devel}
%if %{with emacs}
BuildRequires:	sed >= 4.0
BuildRequires:	emacs
BuildRequires:	emacs-common
%endif
Requires:	%{name}-runtime = %{epoch}:%{version}-%{release}
Provides:	ocaml-ocamldoc
Obsoletes:	ocaml-ocamldoc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fno-strict-aliasing

%description
Objective Caml is a high-level, strongly-typed, functional and
object-oriented programming language from the ML family of languages.

This package comprises two batch compilers (a fast bytecode compiler
and an optimizing native-code compiler), an interactive toplevel
system, Lex&Yacc tools, a replay debugger, and a comprehensive
library.

%description -l pl.UTF-8
OCaml (Objective Caml) jest funkcyjnym, obiektowo zorientowanym językiem
wysokiego poziomu z silnym typowaniem. Należy do rodziny języków ML.

Ten pakiet zawiera dwa kompilatory (szybki kompilator do bajtkodu
oraz optymalizujący kompilator do kodu natywnego), interaktywne środowisko
pracy, narzędzia do tworzenia analizatorów leksykalnych oraz składniowych
(ocamllex, ocamlyacc), odpluskwiacz (ocamldebug) i biblioteki.

%package runtime
Summary:	Runtime system for OCaml
Summary(pl.UTF-8):	Środowisko uruchomieniowe dla OCamla
Group:		Libraries

%description runtime
This package contains binaries needed to run bytecode OCaml programs:
ocamlrun bytecode interpreter, and basic dynamic link libraries.

%description runtime -l pl.UTF-8
Pakiet ten zawiera binaria potrzebne do uruchamiania programów w
OCamlu skompilowanych do bajtkodu: interpreter bajtkodu (ocamlrun) oraz
podstawowe biblioteki linkowane dynamicznie.

%package lib-source
Summary:	Sources of OCaml standard library
Summary(pl.UTF-8):	Źródła biblioteki standardowej OCamla
Group:		Development/Languages
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description lib-source
This sources come helpful during debugging of user programs with ocamldebug.

%description lib-source -l pl.UTF-8
Źródła te są przydatne przy odpluskwianiu programów użytkownika
z użyciem ocamldebug.

%package doc-html
Summary:	HTML documentation for OCaml
Summary(pl.UTF-8):	Dokumentacja dla OCamla w formacie HTML
Group:		Development/Tools

%description doc-html
HTML documentation for OCaml.

%description doc-html -l pl.UTF-8
Dokumentacja dla OCamla w formacie HTML.

%package doc-ps
Summary:	PostScript documentation for OCaml
Summary(pl.UTF-8):	Dokumentacja dla OCamla w formacie PostScript
Group:		Development/Tools

%description doc-ps
PostScript documentation for OCaml.

%description doc-ps -l pl.UTF-8
Dokumentacja dla OCamla w formacie PostScript.

%package doc-info
Summary:	Info documentation for OCaml
Summary(pl.UTF-8):	Dokumentacja info dla OCamla
Group:		Development/Tools

%description doc-info
Info documentation for OCaml.

%description doc-info -l pl.UTF-8
Dokumentacja info dla OCamla.

%package emacs
Summary:	Emacs mode for OCaml
Summary(pl.UTF-8):	Tryb OCamla dla Emacsa
Group:		Development/Tools
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description emacs
Emacs mode files for Objective Caml language.

%description emacs -l pl.UTF-8
Pliki trybu OCamla dla Emacsa.

%package labltk
Summary:	Runtime for LablTk library
Summary(pl.UTF-8):	Środowisko uruchomieniowe dla biblioteki LablTk
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description labltk
LablTk gives OCaml program access to Tcl/Tk GUI widgets. This package
contains files needed to run bytecode OCaml programs using LablTk.

%description labltk -l pl.UTF-8
Biblioteka LablTk daje programom napisanym w OCamlu dostęp do widgetów
Tcl/Tk. Pakiet ten zawiera binaria potrzebne do uruchamiania programów
używających LablTk.

%package labltk-devel
Summary:	LablTk library for OCaml
Summary(pl.UTF-8):	Biblioteka LablTk dla OCamla
Group:		Development/Libraries
Requires:	%{name}-labltk = %{epoch}:%{version}-%{release}

%description labltk-devel
LablTk gives OCaml program access to Tcl/Tk GUI widgets. This package
contains files needed to develop OCaml programs using LablTk.

%description labltk-devel -l pl.UTF-8
Biblioteka LablTk daje programom napisanym w OCamlu dostęp do widgetów
Tcl/Tk. Pakiet ten zawiera pliki niezbędne do tworzenia programów
używających LablTk.

%package x11graphics
Summary:	X11 graphic output for OCaml
Summary(pl.UTF-8):	Dostęp do X11 dla OCamla
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description x11graphics
x11graphics module gives OCaml program access to drawing in X11
windows. This package contains files needed to run bytecode OCaml
programs using x11graphics.

%description x11graphics -l pl.UTF-8
Moduł x11graphics daje programom napisanym w OCamlu możliwość
korzystania z interfejsu graficznego X11. Pakiet ten zawiera binaria
potrzebne do uruchamiania programów używających x11graphics.

%package x11graphics-devel
Summary:	X11 graphic output for OCaml
Summary(pl.UTF-8):	Dostęp do X11 dla OCamla
Group:		Development/Libraries
Requires:	%{name}-x11graphics = %{epoch}:%{version}-%{release}

%description x11graphics-devel
x11graphics module gives OCaml program access to drawing in X11
windows. This package contains files needed to develop OCaml programs
using x11graphics.

%description x11graphics-devel -l pl.UTF-8
Moduł x11graphics daje programom napisanym w OCamlu możliwość
korzystania z interfejsu graficznego X11. Pakiet ten zawiera pliki
niezbędne do tworzenia programów używających x11graphics.

%package camlp4
Summary:	Objective Caml Preprocessor
Summary(pl.UTF-8):	Preprocesor OCamla
Group:		Development/Languages
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	camlp4 = %{epoch}:%{version}-%{release}
Obsoletes:	camlp4

%description camlp4
Camlp4 is a Pre-Processor-Pretty-Printer for Objective Caml. It offers
tools for syntax (grammars) and the ability to modify the concrete
syntax of the language (quotations, syntax extensions).

Camlp4 can parse normal Ocaml concrete syntax or any other
user-definable syntax. As an example, an alternative syntax is
provided, named revised, because it tries to fix some small problems
of the normal syntax.

Camlp4 can pretty print the normal Ocaml concrete syntax or the
revised one. It is therefore always possible to have a version of your
sources compilable by the Objective Caml compiler without
preprocessing.

%description camlp4 -l pl.UTF-8
Camlp4 jest preprocesorem OCamla. Oferuje narzędzia do manipulowania
składnią (gramatyki) oraz możliwość modyfikowania oryginalnej składni
języka (cytowania, rozszerzenia).

Camlp4 może sparsować oryginalną składnię Ocamla lub dowolną inną
definiowalną przez użytkownika. Jako przykład podana jest alternatywna
składnia (revised syntax), która próbuje poprawić drobne problemy
występujące w składni oryginalnej.

Camlp4 umie ładnie formatować źródła zarówno w oryginalnej jak i
poprawionej składni OCamla. Potrafi także tłumaczyć programy z jednej
składni na drugą.

%package camlp4-doc-html
Summary:	Objective Caml Preprocessor - HTML documentation 
Summary(pl.UTF-8):	Preprocesor OCamla - dokumentacja HTML 
Group:		Development/Languages

%description camlp4-doc-html
Objective Caml Preprocessor - HTML documentation.

%description camlp4-doc-html -l pl.UTF-8
Preprocesor OCamla - dokumentacja HTML.

%package compiler-objects
Summary:	Compiled parts of OCaml compiler
Summary(pl.UTF-8):	Skompilowane części kompilatora OCamla
Group:		Development/Languages
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	ocaml-devel
Provides:	ocaml-devel

%description compiler-objects
This package contains *.cmi and *.cmo files being parts of OCaml
compiler. They are needed to compile some programs.

%description compiler-objects -l pl.UTF-8
Pakiet ten zawiera pliki *.cmi oraz *.cmo będące częściami kompilatora
OCamla. Są one wymagane do kompilacji niektórych programów.

%package ocamldoc-devel
Summary:	Files needed to develop programs using ocamldoc
Summary(pl.UTF-8):	Pliki potrzebne do tworzenia programów używających ocamldoc
Group:		Development/Languages
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description ocamldoc-devel
You need this package if you are going to write ocamldoc front end or
something like that.

%description ocamldoc-devel -l pl.UTF-8
Będziesz potrzebować tego pakietu, jeśli zamierzasz pisać front end
dla ocamldoc lub coś podobnego.

# maybe we'll want to add some more stuff here?
%package examples
Summary:	Example source code for OCaml
Summary(pl.UTF-8):	Przykładowe kody źródłowe w OCamlu
Group:		Development/Languages
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description examples
This packages contains sources for Okasaki's Purely Functional
Datastructures in OCaml, along with some contributions.

%description examples -l pl.UTF-8
Pakiet ten zawiera źródła Czysto Funkcyjnych Struktur Danych
autorstwa Okasaki'ego, napisane w OCamlu, wraz z dodatkami.

%prep
%setup -q -a1 -a3 -a4 -a6
mkdir examples
tar xjf %{SOURCE8} -C examples
tar xzf %{SOURCE9} -C examples
# order mess with docs somewhat
mkdir -p docs/html
mv htmlman docs/html/ocaml
cp %{SOURCE2} docs/ocaml.ps.gz
mv camlp4-%{p4ver}-manual.html docs/html/camlp4
cp %{SOURCE5} docs/camlp4.ps.gz
mv camlp4-%{p4ver}-tutorial.html docs/html/camlp4-tutorial
cp %{SOURCE7} docs/camlp4-tutorial.ps.gz
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build 
cp -f /usr/share/automake/config.sub config/gnu
./configure \
        -cc "%{__cc}" \
	-bindir %{_bindir} \
	-libdir %{_libdir}/%{name} \
	-mandir %{_mandir}/man1 \
	-host %{_host} \
	%{!?with_tk:-no-tk} \
	-with-pthread \
	-x11lib %{_libdir}

%{__make} -j1 world bootstrap opt.opt CFLAGS="%{rpmcflags} -Wall"
%{__make} -C tools objinfo CFLAGS="%{rpmcflags} -Wall" -j1

# broken build system
sed -e 's,LIBDIR,%{_libdir},' camlp4/man/camlp4.1.tpl > camlp4/man/camlp4.1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_includedir},%{_infodir},%{_examplesdir}/%{name}-{labltk-,}%{version}}
install -d $RPM_BUILD_ROOT%{_libdir}/%{name}/site-lib

%{__make} install \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	LIBDIR=$RPM_BUILD_ROOT%{_libdir}/%{name} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}

cat > $RPM_BUILD_ROOT%{_libdir}/%{name}/ld.conf <<EOF
%{_libdir}/%{name}/stublibs
%{_libdir}/%{name}
EOF

%if %{with emacs}
%{__make} -C emacs install \
	DESTDIR=$RPM_BUILD_ROOT \
	EMACSDIR="$RPM_BUILD_ROOT%{_datadir}/emacs/site-lisp" \
	EMACS="emacs"
%endif

# symlink .opt versions of compilers (if present)
# warning: don't do that with camlp4 (can't load extensions then)
for f in ocamlc ocamlopt ocamldoc ocamllex; do
	if test -f $RPM_BUILD_ROOT%{_bindir}/$f.opt; then
		mv -f $RPM_BUILD_ROOT%{_bindir}/$f \
			$RPM_BUILD_ROOT%{_bindir}/$f.byte
		ln -sf %{_bindir}/$f.opt $RPM_BUILD_ROOT%{_bindir}/$f
	fi
done

# move includes to the proper place
mv -f $RPM_BUILD_ROOT%{_libdir}/%{name}/caml $RPM_BUILD_ROOT%{_includedir}/caml
# but leave compatibility symlink
ln -s ../../include/caml $RPM_BUILD_ROOT%{_libdir}/%{name}/caml

# compiled sources of compiler, needed by some programs
for f in {asm,byte}comp parsing typing utils ; do
	install -d $RPM_BUILD_ROOT%{_libdir}/%{name}/compiler/$f
	cp $f/*.{cmi,cmo,cmx,o} $RPM_BUILD_ROOT%{_libdir}/%{name}/compiler/$f
done

# this isn't installed by default, but is useful
install tools/objinfo $RPM_BUILD_ROOT%{_bindir}/ocamlobjinfo
cp -r examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -r otherlibs/labltk/examples* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-labltk-%{version}
ln -sf %{_libdir}/%{name}/{scrape,add}labels $RPM_BUILD_ROOT%{_bindir}

# shutup checkfiles
%{__rm} -r $RPM_BUILD_ROOT%{_mandir}/man3
%{__rm} $RPM_BUILD_ROOT%{_libdir}/%{name}/labltk/{labltktop,pp}

# install info pages
cp -f infoman/*.gz $RPM_BUILD_ROOT%{_infodir}

# broken build system
install camlp4/man/camlp4.1 $RPM_BUILD_ROOT%{_mandir}/man1
for f in camlp4o.1 camlp4r.1 mkcamlp4.1 camlp4o.opt.1 camlp4r.opt.1 ; do
	echo '.so camlp4.1' >$RPM_BUILD_ROOT%{_mandir}/man1/$f
done

%clean
rm -rf $RPM_BUILD_ROOT

%post	doc-info -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	doc-info -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc LICENSE Changes README Upgrading
%attr(755,root,root) %{_bindir}/addlabels
%attr(755,root,root) %{_bindir}/ocaml*
%attr(755,root,root) %{_bindir}/scrapelabels
%{?with_tk:%exclude %{_bindir}/ocamlbrowser}
%exclude %{_bindir}/ocamlrun
%{_includedir}/caml
%{_libdir}/%{name}/caml
%{_libdir}/%{name}/threads
%dir %{_libdir}/%{name}/vmthreads
%dir %{_libdir}/%{name}/vmthreads/*.cm*
%dir %{_libdir}/%{name}/vmthreads/*.a
%{_libdir}/%{name}/*.a
%{_libdir}/%{name}/*.o
%{_libdir}/%{name}/*.cm*
%exclude %{_libdir}/%{name}/*graphics*
%{_libdir}/%{name}/Makefile.config
%{_libdir}/%{name}/ld.conf
%{_libdir}/%{name}/camlheader
%{_libdir}/%{name}/camlheader_ur
%{_libdir}/%{name}/ocamlbuild
%dir %{_libdir}/%{name}/ocamldoc
%{_libdir}/%{name}/ocamldoc/*.hva
%attr(755,root,root) %{_libdir}/%{name}/expunge
%attr(755,root,root) %{_libdir}/%{name}/extract_crc
%attr(755,root,root) %{_libdir}/%{name}/objinfo_helper
%{_mandir}/man1/ocaml*
%exclude %{_mandir}/man1/ocamlrun.1*

%files runtime
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ocamlrun
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/site-lib
%dir %{_libdir}/%{name}/stublibs
%attr(755,root,root) %{_libdir}/%{name}/stublibs/dll*.so
%exclude %{_libdir}/%{name}/stublibs/dllgraphics.so
%attr(755,root,root) %{_libdir}/%{name}/libcamlrun_shared.so
%if %{with tk}
%exclude %{_libdir}/%{name}/stublibs/dlllabltk.so
%endif
%{_mandir}/man1/ocamlrun.1*

%files lib-source
%defattr(644,root,root,755)
%{_libdir}/%{name}/*.ml
%{_libdir}/%{name}/*.mli
%{_libdir}/%{name}/*/*.mli

%files doc-html
%defattr(644,root,root,755)
%doc docs/html/ocaml/*

%files doc-ps
%defattr(644,root,root,755)
%doc docs/*.ps.gz

%files doc-info
%defattr(644,root,root,755)
%{_infodir}/ocaml.info*

# they are poor, html is much better
#%files manpages
#%%{_mandir}/man3/*

%if %{with emacs}
%files emacs
%defattr(644,root,root,755)
%{_datadir}/emacs/site-lisp/*.el*
%endif

%if %{with tk}
%files labltk
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/stublibs/dlllabltk.so

%files labltk-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/labltk
%attr(755,root,root) %{_bindir}/ocamlbrowser
%dir %{_libdir}/%{name}/labltk
%{_libdir}/%{name}/labltk/*.cm*
%{_libdir}/%{name}/labltk/*.a
%{_libdir}/%{name}/labltk/*.o
%attr(755,root,root) %{_libdir}/%{name}/labltk/tkcompiler
%{_examplesdir}/%{name}-labltk-%{version}
%endif

%if %{with x}
%files x11graphics
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/stublibs/dllgraphics.so

%files x11graphics-devel
%defattr(644,root,root,755)
%{_libdir}/%{name}/graphics*.cm*
%{_libdir}/%{name}/graphics.a
%{_libdir}/%{name}/libgraphics.a
%endif

%files camlp4
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/camlp4*
%attr(755,root,root) %{_bindir}/mkcamlp4
%{_libdir}/%{name}/camlp4
%{_mandir}/man1/camlp4*.1*
%{_mandir}/man1/mkcamlp4.1*

%files camlp4-doc-html
%defattr(644,root,root,755)
%doc docs/html/camlp4*

%files compiler-objects
%defattr(644,root,root,755)
%{_libdir}/%{name}/compiler

%files ocamldoc-devel
%defattr(644,root,root,755)
%{_libdir}/%{name}/ocamldoc/*.cm*
%{_libdir}/%{name}/ocamldoc/*.a

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
