
# conditional build:
# --without emacs
# --without tk
# --without x11  (implies --without tk)

%{?_without_x11:%define	_without_tk	1}

Summary:	The Objective Caml compiler and programming environment
Summary(pl):	Kompilator Objektowego Caml oraz ¶rodowisko programistyczne
Name:		ocaml
Version:	3.04
Release:	6
License:	distributable
Vendor:		Group of implementors <caml-light@inria.fr>
Group:		Development/Languages
Source0:	ftp://ftp.inria.fr/lang/caml-light/%{name}-%{version}.tar.gz
Source1:	ftp://ftp.inria.fr/lang/caml-light/%{name}-%{version}-refman.info.tar.gz
Source2:	ftp://ftp.inria.fr/lang/caml-light/%{name}-%{version}-refman.html.tar.gz
Source3:	ftp://ftp.inria.fr/lang/caml-light/%{name}-%{version}-refman.ps.gz
Source4:	ftp://ftp.inria.fr/INRIA/Projects/cristal/camlp4/camlp4-%{version}-refman.html.tar.gz
Source5:	ftp://ftp.inria.fr/INRIA/Projects/cristal/camlp4/camlp4-%{version}-refman.ps.gz
Source6:	ftp://ftp.inria.fr/INRIA/Projects/cristal/camlp4/camlp4-%{version}-tutorial.html.tar.gz
Source7:	ftp://ftp.inria.fr/INRIA/Projects/cristal/camlp4/camlp4-%{version}-tutorial.ps.gz
Patch0:		%{name}-build.patch
Patch1:		%{name}-DESTDIR.patch
Patch2:		%{name}-manlinks.patch
Patch3:		%{name}-db3.patch
Patch4:		%{name}-powerpcfix.patch
URL:		http://caml.inria.fr/
BuildRequires:	db3-devel
%{!?_without_tk:BuildRequires:		tk-devel}
%{!?_without_x11:BuildRequires:		XFree86-devel}
%{!?_without_emacs:BuildRequires:	xemacs-common}
%{!?_without_emacs:BuildRequires:	xemacs-fsf-compat-pkg}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		no_install_post_strip	1

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
Requires:	%{name} = %{version}

%description doc-ps
PostScript documentation for OCaml

%description doc-ps -l pl
Dokumentacja dla OCaml-a w formacie PostSript

%package doc-html
Summary:	HTML documentation for OCaml
Summary(pl):	Dokumentacja dla OCaml-a w formacie HTML
Group:		Development/Tools
Requires:	%{name} = %{version}

%description doc-html
HTML documentation for OCaml

%description doc-html -l pl
Dokumentacja dla OCaml-a w formacie HTML

%package emacs
Summary:	Emacs mode for OCaml
Summary(pl):	Tryb Emacsa dla OCaml
Group:		Development/Tools
Requires:	%{name} = %{version}

%description emacs
Emacs mode files for Objective Caml language

%description emacs -l pl
Pliki trybu Emacsa dla jêzyka Objektowego Caml

%package labltk
Summary:	LabelTk library for OCaml
Summary(pl):	Biblioteka LablTk dla OCamla
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description labltk
LablTk gives OCaml program access to Tcl/Tk GUI widgets.

%description labltk -l pl
Biblioteka LablTk daje programom napisanym w OCamlu dostêp do widgetów
Tcl/Tk.

%package x11graphics
Summary:	X11 graphic output for OCaml
Summary(pl):	Iksowe wyj¶cie graficzne dla OCamla
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description x11graphics
This package gives OCaml program access to drawing in X11 windows.

%description x11graphics -l pl
Ten pakiet daje programom napisanym w OCamlu dostêp do rysowania po
oknach X11.

%package camlp4
Summary:	Objective Caml Preprocessor
Summary(pl):	Preprocesor Ocamla
Group:		Development/Languages
Requires:	%{name} = %{version}
Provides:	camlp4 = %{version}
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

%prep
%setup -q -T -b 0
%setup -q -T -D -a 1
%setup -q -T -D -a 2
# order mess with docs somewhat
mkdir docs
mkdir docs/html
mv htmlman docs/html/ocaml
cp %{SOURCE3} docs/ocaml.ps.gz
%setup -q -T -D -a 4
mv camlp4-%{version}-refman.html docs/html/camlp4
cp %{SOURCE5} docs/camlp4.ps.gz
%setup -q -T -D -a 6
mv camlp4-%{version}-tutorial.html docs/html/camlp4-tutorial
cp %{SOURCE7} docs/camlp4-tutorial.ps.gz

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%ifarch ppc
%patch4 -p1
%endif

%build
./configure \
        -cc "%{__cc} %{rpmcflags}" \
	-bindir %{_bindir} \
	-libdir %{_libdir}/%{name} \
	-mandir %{_mandir}/man1 \
	-host %{_host} \
	%{?_without_tk:-notk} \
	-with-pthread

# this is crude hack (works in addition to ocaml-db3.patch)
cp config/Makefile config/Makefile.tmp
sed -e 's|-ldb1|-ldb|; s|-I%{_includedir}/db1||' < config/Makefile.tmp > config/Makefile

%{__make} world bootstrap opt ocamlc.opt ocamlopt.opt
%{__make} -C camlp4 optp4

# hack info pages to contain dir entry
cat <<EOF >infoman/ocaml.info
INFO-DIR-SECTION Programming Languages:
START-INFO-DIR-ENTRY
* Ocaml: (ocaml).                             The Ocaml language
END-INFO-DIR-ENTRY
EOF
zcat infoman/ocaml.info.gz >> infoman/ocaml.info

gzip -9nf infoman/ocaml.info

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_infodir}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%if %{!?_without_emacs:1}%{?_without_emacs:0}
%{__make} -C emacs DESTDIR=$RPM_BUILD_ROOT install \
	EMACS="`if [ -x %{_bindir}/emacs ]; then echo emacs; \
	        else echo xemacs; fi`" \
	EMACSDIR="%{_libdir}/emacs/site-lisp"
%endif

cp -p {parsing/{location,longident,parsetree},typing/typecore}.{cm,ml}i \
	$RPM_BUILD_ROOT%{_libdir}/%{name}

for f in ocamlc ocamlopt camlp4o camlp4r; do
	if test -f $RPM_BUILD_ROOT%{_bindir}/$f.opt; then
		mv -f $RPM_BUILD_ROOT%{_bindir}/$f \
			$RPM_BUILD_ROOT%{_bindir}/$f.byte
		ln -sf %{_bindir}/$f.opt $RPM_BUILD_ROOT%{_bindir}/$f
	fi
done

rm -f $RPM_BUILD_ROOT%{_libdir}/%{_name}/*.ml
ln -sf %{_libdir}/%{name}/{scrape,add}labels $RPM_BUILD_ROOT%{_bindir}

install infoman/*info* $RPM_BUILD_ROOT%{_infodir}

gzip -9nf LICENSE Changes README Upgrading

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1


%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/ocaml
%attr(755,root,root) %{_bindir}/ocaml[cmdlopry]*
%attr(755,root,root) %{_bindir}/*labels
%{_libdir}/%{name}/caml
%{_libdir}/%{name}/threads
%{_libdir}/%{name}/[abefhimnopqrstuw]*.*
%{_libdir}/%{name}/callback.*
%{_libdir}/%{name}/char.*
%{_libdir}/%{name}/condition.*
%{_libdir}/%{name}/dbm.*
%{_libdir}/%{name}/digest.*
%attr(755,root,root) %{_libdir}/%{name}/dll[bmnstu]*.so
%{_libdir}/%{name}/g[ce]*.*
%{_libdir}/%{name}/l*.cm*
%{_libdir}/%{name}/l*.mli
%{_libdir}/%{name}/lib[abc]*.a
%{_libdir}/%{name}/libmldbm.a
%{_libdir}/%{name}/lib[nstu]*.a
%{_libdir}/%{name}/ld.conf
%attr(755,root,root) %{_libdir}/%{name}/expunge
%attr(755,root,root) %{_libdir}/%{name}/extract_crc
%{_libdir}/%{name}/camlheader
%{_libdir}/%{name}/camlheader_ur
%attr(755,root,root) %{_libdir}/%{name}/*labels
%{_mandir}/man*/*ocaml*
%{_infodir}/*

%files camlp4
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*camlp4*
%attr(755,root,root) %{_bindir}/ocpp
%attr(755,root,root) %{_bindir}/odyl
%{_libdir}/%{name}/camlp4
%{_mandir}/man*/*camlp4*
%{_mandir}/man*/*ocpp*

%if %{!?_without_tk:1}%{?_without_tk:0}
%files labltk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/labltk
%attr(755,root,root) %{_bindir}/ocamlbrowser
%dir %{_libdir}/%{name}/labltk
%{_libdir}/%{name}/labltk/*.cm*
%{_libdir}/%{name}/labltk/*.a
%{_libdir}/%{name}/labltk/*.mli
%attr(755,root,root) %{_libdir}/%{name}/labltk/*.so
%attr(755,root,root) %{_libdir}/%{name}/labltk/labltktop
%attr(755,root,root) %{_libdir}/%{name}/labltk/tkcompiler
%endif

%if %{!?_without_x11:1}%{?_without_x11:0}
%files x11graphics
%defattr(644,root,root,755)
%{_libdir}/%{name}/graphics*
%{_libdir}/%{name}/libgraphics.a
%attr(755,root,root) %{_libdir}/%{name}/dllgraphics.so
%endif

%if %{!?_without_emacs:1}%{?_without_emacs:0}
%files emacs
%defattr(644,root,root,755)
%{_libdir}/emacs/site-lisp/*.el
%endif

%files doc-ps
%defattr(644,root,root,755)
%doc docs/*.ps.gz

%files doc-html
%defattr(644,root,root,755)
%doc docs/html/*
