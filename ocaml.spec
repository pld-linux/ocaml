
# conditional build:
# --without emacs
# --without tk
# --without x11  (implies --without tk)

%{?_without_x11:%define	_without_tk	1}

Summary:	The Objective Caml compiler and programming environment
Summary(pl):	Kompilator Objektowego Camla oraz ¶rodowisko programistyczne
Name:		ocaml
Version:	3.05
Release:	1
License:	distributable
Vendor:		Group of implementors <caml-light@inria.fr>
Group:		Development/Languages
Source0:	ftp://ftp.inria.fr/lang/caml-light/%{name}-%{version}.tar.gz
Source1:	ftp://ftp.inria.fr/lang/caml-light/%{name}-%{version}-refman.html.tar.gz
Source2:	ftp://ftp.inria.fr/lang/caml-light/%{name}-%{version}-refman.ps.gz
Source3:	ftp://ftp.inria.fr/INRIA/Projects/cristal/camlp4/camlp4-%{version}-manual.html.tar.gz
Source4:	ftp://ftp.inria.fr/INRIA/Projects/cristal/camlp4/camlp4-%{version}-manual.dvi.gz
Source5:	ftp://ftp.inria.fr/INRIA/Projects/cristal/camlp4/camlp4-%{version}-tutorial.html.tar.gz
Source6:	ftp://ftp.inria.fr/INRIA/Projects/cristal/camlp4/camlp4-%{version}-tutorial.dvi.gz
Patch0:		%{name}-build.patch
Patch1:		%{name}-DESTDIR.patch
Patch2:		%{name}-manlinks.patch
Patch3:		%{name}-db3.patch
Patch4:		%{name}-objinfo.patch
Patch5:		%{name}-opt-symbols.patch
Patch6:		%{name}-mano.patch
URL:		http://caml.inria.fr/
Requires:	ocaml-runtime = %{version}-%{release}
Obsoletes:	ocaml-ocamldoc
Provides:	ocaml-ocamldoc
BuildRequires:	db3-devel
%{!?_without_tk:BuildRequires:		tk-devel}
%{!?_without_x11:BuildRequires:		XFree86-devel}
%{!?_without_emacs:BuildRequires:	xemacs}
%{!?_without_emacs:BuildRequires:	xemacs-common}
%{!?_without_emacs:BuildRequires:	xemacs-fsf-compat-pkg}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Objective Caml is a high-level, strongly-typed, functional and
object-oriented programming language from the ML family of languages.

This package comprises two batch compilers (a fast bytecode compiler
and an optimizing native-code compiler), an interactive toplevel
system, Lex&Yacc tools, a replay debugger, and a comprehensive
library.

%description -l pl
Objektowy Caml jest funkcjonalnym, obiektowo zorientowanym jêzykiem
wysokiego poziomu z rodziny jêzyków ML.

Ten pakiet zawiera dwa kompilatory (szybki kompilator bytecode oraz
zoptymalizowany natywny kompilator), interaktywny g³ówny system,
narzêdzia Lex&Yacc, odpluskwiacz i biblioteki.

%package doc-ps
Summary:	PostScript documentation for OCaml
Summary(pl):	Dokumentacja dla OCaml-a w formacie PostSript
Group:		Development/Tools

%description doc-ps
PostScript documentation for OCaml. HTML documentation is in main package.

%description doc-ps -l pl
Dokumentacja dla OCamla w formacie PostSript. Dokumentacja HTML jest
w g³ównym pakiecie.

%package emacs
Summary:	Emacs mode for OCaml
Summary(pl):	Tryb Emacsa dla OCaml
Group:		Development/Tools
Requires:	%{name} = %{version}

%description emacs
Emacs mode files for Objective Caml language.

%description emacs -l pl
Pliki trybu Emacsa dla jêzyka Objektowego Camla.

%package runtime
Summary:	Runtime system for OCaml
Summary(pl):	¦rodowisko uruchomieniowe dla OCamla
Group:		Libraries

%description runtime
This package contains binaries needed to run bytecode OCaml programs:
ocamlrun bytecode interpreter, and basic dynamic link libraries.

%description runtime -l pl
Pakiet ten zawiera binaria potrzebne do uruchamiania programów w
OCamlu skompilowanych do bytecodu: interpreter bytecodu ocamlrun oraz
podstawowe bibliotki linkowane dynamicznie.

%package labltk-devel
Summary:	LabelTk library for OCaml
Summary(pl):	Biblioteka LablTk dla OCamla
Group:		Development/Libraries
Requires:	%{name}-labltk = %{version}-%{release}

%description labltk-devel
LablTk gives OCaml program access to Tcl/Tk GUI widgets. This package
contains files needed to develop OCaml programs using LablTk.

%description labltk-devel -l pl
Biblioteka LablTk daje programom napisanym w OCamlu dostêp do widgetów
Tcl/Tk. Pakiet ten zawiera pliki niezbêdne do tworzenia programów
u¿ywaj±cych LablTk.

%package labltk
Summary:	Runtime for LabelTk library
Summary(pl):	¦rodowisko uruchomieniowe dla biblioteki LablTk
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description labltk
LablTk gives OCaml program access to Tcl/Tk GUI widgets. This package
contains files needed to run bytecode OCaml programs using LablTk.

%description labltk -l pl
Biblioteka LablTk daje programom napisanym w OCamlu dostêp do widgetów
Tcl/Tk. Pakiet ten zawiera binaria potrzebne do uruchamiania programów
u¿ywaj±cych LablTk.

%package x11graphics-devel
Summary:	X11 graphic output for OCaml
Summary(pl):	Iksowe wyj¶cie graficzne dla OCamla
Group:		Development/Libraries
Requires:	%{name}-x11graphics = %{version}-%{release}

%description x11graphics-devel
x11graphics module gives OCaml program access to drawing in X11
windows. This package contains files needed to develop OCaml programs
using x11graphics.

%description x11graphics-devel -l pl
Modu³ x11graphics daje programom napisanym w OCamlu dostêp do
rysowania po oknach X11. Pakiet ten zawiera pliki niezbêdne do
tworzenia programów u¿ywaj±cych x11graphics.

%package x11graphics
Summary:	X11 graphic output for OCaml
Summary(pl):	Iksowe wyj¶cie graficzne dla OCamla
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description x11graphics
x11graphics module gives OCaml program access to drawing in X11
windows. This package contains files needed to run bytecode OCaml
programs using x11graphics.

%description x11graphics -l pl
Modu³ x11graphics daje programom napisanym w OCamlu dostêp do
rysowania po oknach X11. Pakiet ten zawiera binaria potrzebne do
uruchamiania programów u¿ywaj±cych x11graphics.

%package camlp4
Summary:	Objective Caml Preprocessor
Summary(pl):	Preprocesor Ocamla
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}
Provides:	camlp4 = %{version}-%{release}
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
sources compilable by the compiler Objective Caml without
preprocessing.

%description camlp4 -l pl
Camlp4 jest preprocesorem dla Ocamla. Oferuje narzêdzia do sk³adni
(gramatyki) oraz umiejêtno¶æ modyfikowania konkretnej sk³adni jêzyka
(cytowania, rozszerzenia).

Camlp4 mo¿e sparsowaæ normaln± sk³adniê Ocamla lub inn± dowoln±
definiowaln± przez u¿ytkownika. Jako przyk³ad jest podana alternatywna
sk³adnia, nazwana "poprawiona", poniewa¿ próbuje poprawiæ drobne
problemy ze zwyk³± sk³adni±.

Camlp4 umie ³adnie wypisaæ normaln± sk³adniê Camla lub "poprawion±".
Dziêki temu jest mo¿liwe posiadanie wersji swoich ¼róde³
kompilowalnych przez kompilatora Ocamla bez preprocesingu.

%package devel
Summary:	Compiled parts of OCaml compiler
Summary(pl):	Skompilowane kawa³ki kompilatora OCamla
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains *.cmi and *.cmo files being parts of OCaml
compiler. They are needed to compile some programs.

%description devel -l pl
Pakiet ten zawiera pliki *.cmi oraz *.cmo bêd±ce cze¶ciami kompilatora
OCamla. S± one wymagane do kompilacji niektórych programów.

%package ocamldoc-devel
Summary:	Files needed to develop programs using ocamldoc
Summary(pl):	Pliki potrzebne do tworzenia programów u¿ywaj±cych ocamldoc
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description ocamldoc-devel
You need this package if you are going to write ocamldoc front end or
something like that.

%description ocamldoc-devel -l pl
Bêdziesz potrzebowaæ tego pakietu, je¶li zamierzasza pisaæ front end
dla ocamldoc lub co¶ podobnego.

%package lib-source
Summary:	Sources of OCaml standard library
Summary(pl):	¬ród³a biblioteki standardowej OCamla
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description lib-source
This sources come helpful during debugging of user programs with ocamldebug.

%description lib-source -l pl
¬ród³a te co¶ przydatne przy odpluskwianiu programów u¿ytkownika
z u¿yciem ocamldebug.

%prep
%setup -q -T -b 0
%setup -q -T -D -a 1
# order mess with docs somewhat
mkdir docs
mkdir docs/html
mv htmlman docs/html/ocaml
cp %{SOURCE2} docs/ocaml.ps.gz
%setup -q -T -D -a 3
mv camlp4-%{version}-refman.html docs/html/camlp4
cp %{SOURCE4} docs/camlp4.ps.gz
%setup -q -T -D -a 5
mv camlp4-%{version}-tutorial.html docs/html/camlp4-tutorial
cp %{SOURCE6} docs/camlp4-tutorial.ps.gz
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
#%patch5 -p1
%patch6 -p1

%build
./configure \
        -cc "%{__cc} %{rpmcflags}" \
	-bindir %{_bindir} \
	-libdir %{_libdir}/%{name} \
	-mandir %{_mandir}/man1 \
	-host %{_host} \
	%{?_without_tk:-notk} \
	-with-pthread

%{__make} world bootstrap opt.opt
%{__make} -C tools objinfo

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	LIBDIR=$RPM_BUILD_ROOT%{_libdir}/%{name} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}

cat > $RPM_BUILD_ROOT%{_libdir}/%{name}/ld.conf <<EOF
%{_libdir}/%{name}/stublibs
%{_libdir}/%{name}
EOF

%if %{!?_without_emacs:1}%{?_without_emacs:0}
%{__make} -C emacs DESTDIR=$RPM_BUILD_ROOT install \
	EMACS="`if [ -x %{_bindir}/emacs ]; then echo emacs; \
	        else echo xemacs; fi`" \
	EMACSDIR="$RPM_BUILD_ROOT%{_libdir}/emacs/site-lisp"
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

rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/*.mli
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/*/*.ml{,i}

# move includes to the proper place
install -d $RPM_BUILD_ROOT%{_includedir}
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

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-labltk-%{version}
cp -r otherlibs/labltk/examples* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-labltk-%{version}

ln -sf %{_libdir}/%{name}/{scrape,add}labels $RPM_BUILD_ROOT%{_bindir}

# shutup checkfiles
#rm -f $RPM_BUILD_ROOT%{_mandir}/man3
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/labltk/{labltktop,pp}

%clean
rm -rf $RPM_BUILD_ROOT

%files runtime
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ocamlrun
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/stublibs
%attr(755,root,root) %{_libdir}/%{name}/stublibs/dll*.so
%exclude %{_libdir}/%{name}/stublibs/dllgraphics.so
%exclude %{_libdir}/%{name}/stublibs/dlllabltk.so
%exclude %{_libdir}/%{name}/stublibs/dlltkanim.so

%files
%defattr(644,root,root,755)
%doc LICENSE Changes README Upgrading
%doc docs/html/ocaml
%attr(755,root,root) %{_bindir}/ocaml*
%exclude %{_bindir}/ocamlbrowser
%exclude %{_bindir}/ocamlrun
%attr(755,root,root) %{_bindir}/*labels
%{_includedir}/caml
%{_libdir}/%{name}/caml
%{_libdir}/%{name}/threads
%{_libdir}/%{name}/*.a
%{_libdir}/%{name}/*.o
%{_libdir}/%{name}/*.cm*
%exclude %{_libdir}/%{name}/*graphics*
%{_libdir}/%{name}/ld.conf
%{_libdir}/%{name}/camlheader
%{_libdir}/%{name}/camlheader_ur
%dir %{_libdir}/%{name}/ocamldoc
%{_libdir}/%{name}/ocamldoc/*.sty
%{_libdir}/%{name}/ocamldoc/*.hva
%attr(755,root,root) %{_libdir}/%{name}/expunge
%attr(755,root,root) %{_libdir}/%{name}/extract_crc
%attr(755,root,root) %{_libdir}/%{name}/*labels
%{_mandir}/man1/*ocaml*

%files lib-source
%defattr(644,root,root,755)
%{_libdir}/%{name}/*.ml

# they are poor, html is much better
#%files manpages
#%{_mandir}/man3/*

%files devel
%defattr(644,root,root,755)
%{_libdir}/%{name}/compiler

%files camlp4
%defattr(644,root,root,755)
%doc docs/html/camlp4*
%attr(755,root,root) %{_bindir}/*camlp4*
%attr(755,root,root) %{_bindir}/ocpp
# Not installed since 3.05, is is needed?
#%attr(755,root,root) %{_bindir}/odyl
%{_libdir}/%{name}/camlp4
%{_mandir}/man*/*camlp4*
%{_mandir}/man*/*ocpp*

%if %{!?_without_tk:1}%{?_without_tk:0}
%files labltk-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/labltk
%attr(755,root,root) %{_bindir}/ocamlbrowser
%dir %{_libdir}/%{name}/labltk
%{_libdir}/%{name}/labltk/*.cm*
%{_libdir}/%{name}/labltk/*.a
%attr(755,root,root) %{_libdir}/%{name}/labltk/tkcompiler
%{_examplesdir}/%{name}-labltk-%{version}

%files labltk
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/stublibs/dlllabltk.so
%attr(755,root,root) %{_libdir}/%{name}/stublibs/dlltkanim.so
%endif

%if %{!?_without_x11:1}%{?_without_x11:0}
%files x11graphics-devel
%defattr(644,root,root,755)
%{_libdir}/%{name}/graphics*.cm*
%{_libdir}/%{name}/libgraphics.a

%files x11graphics
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/stublibs/dllgraphics.so
%endif

%if %{!?_without_emacs:1}%{?_without_emacs:0}
%files emacs
%defattr(644,root,root,755)
%{_libdir}/emacs/site-lisp/*.el*
%endif

%files ocamldoc-devel
%defattr(644,root,root,755)
%{_libdir}/%{name}/ocamldoc/*.cm*
%{_libdir}/%{name}/ocamldoc/*.a

%files doc-ps
%defattr(644,root,root,755)
%doc docs/*.ps.gz
