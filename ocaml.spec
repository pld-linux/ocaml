
# conditional build:
# --without emacs

%{!?_without_emacs:%define	emacs	1}
%{?_without_emacs:%define	emacs	0}

Summary:	The Objective Caml compiler and programming environment
Summary(pl):	Kompilator Objektowego Caml oraz ¶rodowisko programistyczne
Name:		ocaml
Version:	3.02
Release:	3
License:	distributable
Vendor:		Group of implementors <caml-light@inria.fr>
Group:		Development/Languages
Group(de):	Entwicklung/Sprachen
Group(pl):	Programowanie/Jêzyki
Source0:	ftp://ftp.inria.fr/lang/caml-light/%{name}-%{version}.tar.gz
Source1:	ftp://ftp.inria.fr/lang/caml-light/%{name}-%{version}-refman.info.tar.gz
Source2:	ftp://ftp.inria.fr/lang/caml-light/%{name}-%{version}-refman.html.tar.gz
Source3:	ftp://ftp.inria.fr/lang/caml-light/%{name}-%{version}-refman.ps.gz
URL:		http://caml.inria.fr/caml/
BuildRequires:	tcl-devel
BuildRequires:	tk-devel
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
wysokiego poziomu rodziny jêzyków ML.

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

%if %emacs
%package emacs
Summary:	Emacs mode for OCaml
Summary(pl):	Tryb Emacsa dla OCaml
Group:		Development/Tools
Group(de):	Entwicklung/Werkzeuge
Group(fr):	Development/Outils
Group(pl):	Programowanie/Narzêdzia
Requires:	%{name} = %{version}
# xemacs doesn't have Provide emacs ?
#BuildRequires:	emacs

%description emacs
Emacs mode files for Objective Caml language

%description -l pl emacs
Pliki trybu Emacsa dla jêzyka Objektowego Caml
%endif

%prep
%setup -q -T -b 0
%setup -q -T -D -a 1
%setup -q -T -D -a 2
cp %{SOURCE3} .

%build
./configure \
	-cc "%{__cc}" \
	-bindir %{_bindir} \
	-libdir %{_libdir}/%{name} \
	-mandir %{_mandir}/man1 \
	-host %{_host} \
	-with-pthread

%{__make} world bootstrap opt ocamlc.opt ocamlopt.opt \
	BYTECCCOMPOPTS="%{rpmcflags}"

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
umask 022

echo	BINDIR=$RPM_BUILD_ROOT%{_bindir} >> config/Makefile
echo	LIBDIR=$RPM_BUILD_ROOT%{_libdir}/%{name} >> config/Makefile
echo	MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1 >> config/Makefile

make	install 

%if %emacs
%{__make} -C emacs install \
	EMACS="`if [ -x %{_bindir}/emacs ]; then echo emacs; \
	        else echo xemacs; fi`" \
	EMACSDIR="$RPM_BUILD_ROOT%{_libdir}/emacs/site-lisp"
	
cp -p {parsing/{location,longident,parsetree},typing/typecore}.{cm,ml}i \
	$RPM_BUILD_ROOT%{_libdir}/%{name}
%endif		
		
mv -f $RPM_BUILD_ROOT%{_bindir}/ocamlc $RPM_BUILD_ROOT%{_bindir}/ocamlc.byte
ln -sf %{_bindir}/ocamlc.opt $RPM_BUILD_ROOT%{_bindir}/ocamlc
mv -f $RPM_BUILD_ROOT%{_bindir}/ocamlopt $RPM_BUILD_ROOT%{_bindir}/ocamlopt.byte
ln -sf %{_bindir}/ocamlopt.opt $RPM_BUILD_ROOT%{_bindir}/ocamlopt
rm -f $RPM_BUILD_ROOT%{_libdir}/%{_name}/*.ml

install -d $RPM_BUILD_ROOT%{_infodir}
install infoman/*info* $RPM_BUILD_ROOT%{_infodir}

gzip -9nf LICENSE Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1


%files
%defattr(644,root,root,755)
%doc LICENSE.gz Changes.gz README.gz
%attr(755, root, root) %{_bindir}/*
%{_libdir}/%{name}/caml
%{_libdir}/%{name}/labltk
%{_libdir}/%{name}/threads
%{_libdir}/%{name}/*.*
%attr(755,root,root) %{_libdir}/%{name}/expunge
%attr(755,root,root) %{_libdir}/%{name}/extract_crc
%attr(755,root,root) %{_libdir}/%{name}/camlheader
%attr(755,root,root) %{_libdir}/%{name}/camlheader_ur
%{_mandir}/man*/*
%{_infodir}/*

%if %emacs
%files emacs
%defattr(644,root,root,755)
%{_libdir}/emacs/site-lisp/*.el
%endif

%files doc-ps
%doc *.ps.gz

%files doc-html
%doc htmlman
