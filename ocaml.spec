#
# Conditional build:
%bcond_without	emacs		# emacs subpackage
%bcond_without	x		# X11 support 
%bcond_without	ocaml_opt	# native, optimized compiler

# ppc64, sparc64 and x32 variants not supported currently
# alpha, hppa, ia64, mips removed since 4.00
%ifnarch %{ix86} %{x8664} arm aarch64 ppc sparc sparcv9 
%undefine	with_ocaml_opt
%endif

%define		sver	4.02

Summary:	The Objective Caml compiler and programming environment
Summary(pl.UTF-8):	Kompilator OCamla (Objective Caml) oraz środowisko programistyczne
Name:		ocaml
Version:	4.02.2
Release:	1
Epoch:		1
License:	QPL v1.0 with linking exception (compiler), LGPL v2 with linking exception (library)
Group:		Development/Languages
Source0:	http://caml.inria.fr/distrib/%{name}-%{sver}/%{name}-%{version}.tar.xz
# Source0-md5:	a453ab62931776a78ba761112db9e00b
Source1:	http://caml.inria.fr/distrib/%{name}-%{sver}/%{name}-%{sver}-refman-html.tar.gz
# Source1-md5:	915a1949f7af7186e16354e9682dc1e5
Source2:	http://caml.inria.fr/distrib/%{name}-%{sver}/%{name}-%{sver}-refman.ps.gz
# Source2-md5:	e85016fa23b6525d1d10da06010fd90a
Source3:	http://caml.inria.fr/distrib/%{name}-%{sver}/%{name}-%{sver}-refman.info.tar.gz
# Source3-md5:	265b7db123e925e8b7b70ca2266b4206
Source4:	https://github.com/mmottl/pure-fun/archive/v1.0.13/pure-fun-1.0.13.tar.gz
# Source4-md5:	0a6ff033df78d0880fe4883ace025ebe
# note: dead URL
Source5:	http://www.ocaml.info/ocaml_sources/ds-contrib.tar.gz
# Source5-md5:	77fa1da7375dea1393cc0b6cd802d7e1
Patch1:		%{name}-CFLAGS.patch
Patch2:		%{name}-as_needed.patch
Patch3:		x32.patch
URL:		http://caml.inria.fr/
%{?with_x:BuildRequires:	xorg-lib-libX11-devel}
%if %{with emacs}
BuildRequires:	sed >= 4.0
BuildRequires:	emacs
BuildRequires:	emacs-common
%endif
Requires:	%{name}-runtime = %{epoch}:%{version}-%{release}
Provides:	ocaml-bytes-devel
Provides:	ocaml-ocamldoc
Obsoletes:	ocaml-ocamldoc
Obsoletes:	ocaml-bytes-devel
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
OCaml (Objective Caml) jest funkcyjnym, obiektowo zorientowanym
językiem wysokiego poziomu z silnym typowaniem. Należy do rodziny
języków ML.

Ten pakiet zawiera dwa kompilatory (szybki kompilator do bajtkodu
oraz optymalizujący kompilator do kodu natywnego), interaktywne
środowisko pracy, narzędzia do tworzenia analizatorów leksykalnych
oraz składniowych (ocamllex, ocamlyacc), odpluskwiacz (ocamldebug) i
biblioteki.

%package runtime
Summary:	Runtime system for OCaml
Summary(pl.UTF-8):	Środowisko uruchomieniowe dla OCamla
Group:		Libraries

%description runtime
This package contains binaries needed to run bytecode OCaml programs:
ocamlrun bytecode interpreter, and basic dynamic link libraries.

%description runtime -l pl.UTF-8
Pakiet ten zawiera binaria potrzebne do uruchamiania programów w
OCamlu skompilowanych do bajtkodu: interpreter bajtkodu (ocamlrun)
oraz podstawowe biblioteki linkowane dynamicznie.

%package lib-source
Summary:	Sources of OCaml standard library
Summary(pl.UTF-8):	Źródła biblioteki standardowej OCamla
Group:		Development/Languages
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description lib-source
This sources come helpful during debugging of user programs with
ocamldebug.

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

%package compiler-objects
Summary:	Compiled parts of OCaml compiler
Summary(pl.UTF-8):	Skompilowane części kompilatora OCamla
Group:		Development/Languages
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	ocaml-devel
Obsoletes:	ocaml-devel

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
%setup -q -a1 -a3
mkdir examples
tar xzf %{SOURCE4} -C examples
tar xzf %{SOURCE5} -C examples
# order mess with docs somewhat
mkdir -p docs/html
mv htmlman docs/html/ocaml
cp %{SOURCE2} docs/ocaml.ps.gz
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build 
cp -f /usr/share/automake/config.sub config/gnu
./configure \
	-host %{_target_platform} \
        -cc "%{__cc}" \
	-bindir %{_bindir} \
	-libdir %{_libdir}/%{name} \
	-mandir %{_mandir}/man1 \
	-with-pthread \
	-x11lib %{_libdir}

%{__make} -j1 world bootstrap %{?with_ocaml_opt:opt.opt} \
	CFLAGS="%{rpmcflags} -Wall -DUSE_INTERP_RESULT"

%{__make} -C tools objinfo \
	CFLAGS="%{rpmcflags} -Wall -DUSE_INTERP_RESULT" -j1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_includedir},%{_infodir},%{_examplesdir}/%{name}-%{version}}
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
	cp $f/*.{cmi,cmo} $RPM_BUILD_ROOT%{_libdir}/%{name}/compiler/$f
	%{?with_ocaml_opt:cp $f/*.{cmx,o} $RPM_BUILD_ROOT%{_libdir}/%{name}/compiler/$f}
done

# this isn't installed by default, but is useful
install tools/objinfo $RPM_BUILD_ROOT%{_bindir}/ocamlobjinfo
cp -r examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
ln -sf %{_libdir}/%{name}/{scrape,add}labels $RPM_BUILD_ROOT%{_bindir}

# shutup checkfiles
%{__rm} -r $RPM_BUILD_ROOT%{_mandir}/man3

# install info pages
cp -f infoman/*.gz $RPM_BUILD_ROOT%{_infodir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	doc-info -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	doc-info -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc Changes LICENSE README
%attr(755,root,root) %{_bindir}/addlabels
%attr(755,root,root) %{_bindir}/ocaml
%attr(755,root,root) %{_bindir}/ocamlbuild*
%attr(755,root,root) %{_bindir}/ocamlc
%{?with_ocaml_opt:%attr(755,root,root) %{_bindir}/ocamlc.*}
%attr(755,root,root) %{_bindir}/ocamlcp
%attr(755,root,root) %{_bindir}/ocamldebug
%attr(755,root,root) %{_bindir}/ocamldep*
%attr(755,root,root) %{_bindir}/ocamldoc*
%attr(755,root,root) %{_bindir}/ocamllex*
%attr(755,root,root) %{_bindir}/ocamlmklib
%attr(755,root,root) %{_bindir}/ocamlmktop
%attr(755,root,root) %{_bindir}/ocamlobjinfo
%{?with_ocaml_opt:%attr(755,root,root) %{_bindir}/ocamlopt}
%{?with_ocaml_opt:%attr(755,root,root) %{_bindir}/ocamlopt.*}
%attr(755,root,root) %{_bindir}/ocamloptp
%attr(755,root,root) %{_bindir}/ocamlprof
%attr(755,root,root) %{_bindir}/ocamlyacc
%attr(755,root,root) %{_bindir}/scrapelabels
%{_includedir}/caml
%{_libdir}/%{name}/caml
%{_libdir}/%{name}/compiler-libs
%{_libdir}/%{name}/threads
%dir %{_libdir}/%{name}/vmthreads
%dir %{_libdir}/%{name}/vmthreads/*.cm*
%dir %{_libdir}/%{name}/vmthreads/*.a
%{_libdir}/%{name}/*.a
%{?with_ocaml_opt:%{_libdir}/%{name}/*.o}
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
%{_libdir}/%{name}/VERSION
%dir %{_libdir}/%{name}/site-lib
%dir %{_libdir}/%{name}/stublibs
%attr(755,root,root) %{_libdir}/%{name}/stublibs/dll*.so
%exclude %{_libdir}/%{name}/stublibs/dllgraphics.so
%attr(755,root,root) %{_libdir}/%{name}/libasmrun_shared.so
%attr(755,root,root) %{_libdir}/%{name}/libcamlrun_shared.so
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

%if %{with x}
%files x11graphics
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/stublibs/dllgraphics.so

%files x11graphics-devel
%defattr(644,root,root,755)
%{_libdir}/%{name}/graphics*.cm*
%{?with_ocaml_opt:%{_libdir}/%{name}/graphics.a}
%{_libdir}/%{name}/libgraphics.a
%endif

%files compiler-objects
%defattr(644,root,root,755)
%{_libdir}/%{name}/compiler

%files ocamldoc-devel
%defattr(644,root,root,755)
%{_libdir}/%{name}/ocamldoc/*.cm*
%{?with_ocaml_opt:%{_libdir}/%{name}/ocamldoc/*.a}

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
