#
# Conditional build:
%bcond_without	ocaml_opt	# native, optimized compiler

# ppc64, sparc64 and x32 variants not supported currently
# alpha, hppa, ia64, mips removed since 4.00
%ifnarch %{ix86} %{x8664} arm aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

%define		sver	4.12

Summary:	The Objective Caml compiler and programming environment
Summary(pl.UTF-8):	Kompilator OCamla (Objective Caml) oraz środowisko programistyczne
Name:		ocaml
Version:	4.12.0
Release:	5
Epoch:		1
License:	QPL v1.0 with linking exception (compiler), LGPL v2 with linking exception (library)
Group:		Development/Languages
Source0:	http://caml.inria.fr/distrib/ocaml-%{sver}/%{name}-%{version}.tar.xz
# Source0-md5:	7343cd398d477001db2c3f2ac92e12ea
Source1:	http://caml.inria.fr/distrib/ocaml-%{sver}/%{name}-%{sver}-refman-html.tar.gz
# Source1-md5:	1bda3d0a46328a985c817d551423e2c6
Source3:	http://caml.inria.fr/distrib/ocaml-%{sver}/%{name}-%{sver}-refman.info.tar.gz
# Source3-md5:	c808dbbe35a6cc5d14da6c3b2f175d2c
Source4:	https://github.com/mmottl/pure-fun/archive/v1.0.13/pure-fun-1.0.13.tar.gz
# Source4-md5:	0a6ff033df78d0880fe4883ace025ebe
# note: dead URL
Source5:	http://www.ocaml.info/ocaml_sources/ds-contrib.tar.gz
# Source5-md5:	77fa1da7375dea1393cc0b6cd802d7e1
URL:		https://www.ocaml.org/
Requires:	%{name}-runtime = %{epoch}:%{version}-%{release}
Provides:	ocaml-bytes-devel
Provides:	ocaml-ocamldoc
Obsoletes:	ocaml-bytes-devel
Obsoletes:	ocaml-doc-ps < 1:4.12
Obsoletes:	ocaml-emacs < 1:4.12
Obsoletes:	ocaml-ocamldoc
Obsoletes:	ocaml-x11graphics < 1:4.12
Obsoletes:	ocaml-x11graphics-devel < 1:4.12
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fno-strict-aliasing

%if %{without ocaml_opt}
%define		_noautoreq	Backend_intf Inlining_decision_intf Simplify_boxed_integer_ops_intf
%endif

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

Ten pakiet zawiera dwa kompilatory (szybki kompilator do bajtkodu oraz
optymalizujący kompilator do kodu natywnego), interaktywne środowisko
pracy, narzędzia do tworzenia analizatorów leksykalnych oraz
składniowych (ocamllex, ocamlyacc), odpluskwiacz (ocamldebug) i
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
Źródła te są przydatne przy odpluskwianiu programów użytkownika z
użyciem ocamldebug.

%package doc-html
Summary:	HTML documentation for OCaml
Summary(pl.UTF-8):	Dokumentacja dla OCamla w formacie HTML
Group:		Development/Tools

%description doc-html
HTML documentation for OCaml.

%description doc-html -l pl.UTF-8
Dokumentacja dla OCamla w formacie HTML.

%package doc-info
Summary:	Info documentation for OCaml
Summary(pl.UTF-8):	Dokumentacja info dla OCamla
Group:		Development/Tools

%description doc-info
Info documentation for OCaml.

%description doc-info -l pl.UTF-8
Dokumentacja info dla OCamla.

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
Pakiet ten zawiera źródła Czysto Funkcyjnych Struktur Danych autorstwa
Okasaki'ego, napisane w OCamlu, wraz z dodatkami.

%prep
%setup -q -a1 -a3
mkdir examples
tar xzf %{SOURCE4} -C examples
tar xzf %{SOURCE5} -C examples
# order mess with docs somewhat
mkdir -p docs/html
mv htmlman docs/html/ocaml

%build
%configure \
	AS=%{__as} \
	ASPP="%{__cc} -c" \
	--libdir=%{_libdir}/ocaml \
	%{!?with_ocaml_opt:--disable-native-compiler}

%{__make} world
%{__make} bootstrap
%if %{with ocaml_opt}
%{__make} opt
%{__make} opt.opt
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_includedir},%{_infodir},%{_examplesdir}/%{name}-%{version}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cat > $RPM_BUILD_ROOT%{_libdir}/%{name}/ld.conf <<EOF
%{_libdir}/%{name}/stublibs
%{_libdir}/%{name}
EOF

# move includes to the proper place
%{__mv} $RPM_BUILD_ROOT%{_libdir}/ocaml/caml $RPM_BUILD_ROOT%{_includedir}/caml
# but leave compatibility symlink
ln -s ../../include/caml $RPM_BUILD_ROOT%{_libdir}/ocaml/caml

# compiled sources of compiler, needed by some programs
for f in %{?with_ocaml_opt:asmcomp} bytecomp parsing typing utils ; do
	install -d $RPM_BUILD_ROOT%{_libdir}/%{name}/compiler/$f
	cp $f/*.{cmi,cmo} $RPM_BUILD_ROOT%{_libdir}/%{name}/compiler/$f
	%{?with_ocaml_opt:cp $f/*.{cmx,o} $RPM_BUILD_ROOT%{_libdir}/%{name}/compiler/$f}
done

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
%doc Changes LICENSE README.adoc
%attr(755,root,root) %{_bindir}/addlabels
%attr(755,root,root) %{_bindir}/ocaml
%attr(755,root,root) %{_bindir}/ocamlc
%attr(755,root,root) %{_bindir}/ocamlc.byte
%{?with_ocaml_opt:%attr(755,root,root) %{_bindir}/ocamlc.opt}
%attr(755,root,root) %{_bindir}/ocamlcmt
%attr(755,root,root) %{_bindir}/ocamlcp
%attr(755,root,root) %{_bindir}/ocamlcp.byte
%{?with_ocaml_opt:%attr(755,root,root) %{_bindir}/ocamlcp.opt}
%attr(755,root,root) %{_bindir}/ocamldebug
%attr(755,root,root) %{_bindir}/ocamldep
%attr(755,root,root) %{_bindir}/ocamldep.byte
%{?with_ocaml_opt:%attr(755,root,root) %{_bindir}/ocamldep.opt}
%attr(755,root,root) %{_bindir}/ocamldoc
%{?with_ocaml_opt:%attr(755,root,root) %{_bindir}/ocamldoc.opt}
%attr(755,root,root) %{_bindir}/ocamllex
%attr(755,root,root) %{_bindir}/ocamllex.byte
%{?with_ocaml_opt:%attr(755,root,root) %{_bindir}/ocamllex.opt}
%attr(755,root,root) %{_bindir}/ocamlmklib
%attr(755,root,root) %{_bindir}/ocamlmklib.byte
%{?with_ocaml_opt:%attr(755,root,root) %{_bindir}/ocamlmklib.opt}
%attr(755,root,root) %{_bindir}/ocamlmktop
%attr(755,root,root) %{_bindir}/ocamlmktop.byte
%{?with_ocaml_opt:%attr(755,root,root) %{_bindir}/ocamlmktop.opt}
%attr(755,root,root) %{_bindir}/ocamlobjinfo
%attr(755,root,root) %{_bindir}/ocamlobjinfo.byte
%{?with_ocaml_opt:%attr(755,root,root) %{_bindir}/ocamlobjinfo.opt}
%{?with_ocaml_opt:%attr(755,root,root) %{_bindir}/ocamlopt}
%{?with_ocaml_opt:%attr(755,root,root) %{_bindir}/ocamlopt.byte}
%{?with_ocaml_opt:%attr(755,root,root) %{_bindir}/ocamlopt.opt}
%attr(755,root,root) %{_bindir}/ocamloptp
%attr(755,root,root) %{_bindir}/ocamloptp.byte
%{?with_ocaml_opt:%attr(755,root,root) %{_bindir}/ocamloptp.opt}
%attr(755,root,root) %{_bindir}/ocamlprof
%attr(755,root,root) %{_bindir}/ocamlprof.byte
%{?with_ocaml_opt:%attr(755,root,root) %{_bindir}/ocamlprof.opt}
%attr(755,root,root) %{_bindir}/ocamlyacc
%attr(755,root,root) %{_bindir}/scrapelabels
%{_includedir}/caml
%{_libdir}/%{name}/caml
%{_libdir}/%{name}/compiler-libs
%{_libdir}/%{name}/threads
%{_libdir}/%{name}/*.a
%{?with_ocaml_opt:%{_libdir}/%{name}/*.o}
%{_libdir}/%{name}/*.cm*
%{_libdir}/%{name}/Makefile.config
%{_libdir}/%{name}/ld.conf
%{_libdir}/%{name}/camlheader
%{_libdir}/%{name}/camlheaderd
%{_libdir}/%{name}/camlheaderi
%{_libdir}/%{name}/camlheader_ur
%dir %{_libdir}/%{name}/ocamldoc
%{_libdir}/%{name}/ocamldoc/*.hva
%attr(755,root,root) %{_libdir}/%{name}/expunge
%attr(755,root,root) %{_libdir}/%{name}/extract_crc
%{_mandir}/man1/ocaml*
%exclude %{_mandir}/man1/ocamlrun.1*

%files runtime
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ocamlrun
%attr(755,root,root) %{_bindir}/ocamlrund
%attr(755,root,root) %{_bindir}/ocamlruni
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/stublibs
%{_libdir}/%{name}/eventlog_metadata
%attr(755,root,root) %{_libdir}/%{name}/stublibs/dll*.so
%{?with_ocaml_opt:%attr(755,root,root) %{_libdir}/%{name}/libasmrun_shared.so}
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

%files doc-info
%defattr(644,root,root,755)
%{_infodir}/ocaml.info*

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
