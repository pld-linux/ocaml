Summary:	The Objective Caml compiler and programming environment
Summary(pl):	Kompilator Objektowego Caml oraz ¶rodowisko programistyczne
Name:		ocaml
Version:	3.01
Release:	1
License:	Distributable
Vendor:		Group of implementors <caml-light@inria.fr>
Group:		Development/Languages
Group(de):	Entwicklung/Sprachen
Group(pl):	Programowanie/Jêzyki
Source0:	ftp://ftp.inria.fr/lang/caml-light/%{name}-%{version}.tar.gz
Source1:	ftp://ftp.inria.fr/lang/caml-light/%{name}-%{version}-refman.html.tar.gz
URL:		http://pauillac.inria.fr/caml/
BuildRequires:	tcl-devel
BuildRequires:	tk-devel
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
wysokiego poziomu rodziny jêzyków ML.

Ten pakiet zawiera dwa kompilatory (szybki kompilator bytecode oraz
zoptymalizowany natywny kompilator), interaktywny g³ówny system,
narzêdzia Lex&Yacc, odpluskwiacz i biblioteki.

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

%prep
%setup -q -T -b 0
%setup -q -T -D -a 1

%build
./configure \
	-cc "%{__cc}" \
	-bindir %{_bindir} \
	-libdir %{_libdir}/%{name} \
	-mandir %{_mandir}/man1 \
	-host %{_host_alias} \
	-with-pthread

%{__make} world bootstrap opt ocamlc.opt ocamlopt.opt \
	BYTECCCOMPOPTS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
umask 022

echo	BINDIR=$RPM_BUILD_ROOT%{_bindir} >> config/Makefile
echo	LIBDIR=$RPM_BUILD_ROOT%{_libdir}/%{name} >> config/Makefile
echo	MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1 >> config/Makefile

make	install 
%{__make} -C emacs install \
	EMACS="`if [ -x %{_bindir}/emacs ]; then echo emacs; \
	        else echo xemacs; fi`" \
	EMACSDIR="$RPM_BUILD_ROOT%{_libdir}/emacs/site-lisp"
cp -p {parsing/{location,longident,parsetree},typing/typecore}.{cm,ml}i \
	$RPM_BUILD_ROOT%{_libdir}/%{name}
			
mv -f $RPM_BUILD_ROOT%{_bindir}/ocamlc $RPM_BUILD_ROOT%{_bindir}/ocamlc.byte
mv -f $RPM_BUILD_ROOT%{_bindir}/ocamlc.opt $RPM_BUILD_ROOT%{_bindir}/ocamlc
mv -f $RPM_BUILD_ROOT%{_bindir}/ocamlopt $RPM_BUILD_ROOT%{_bindir}/ocamlopt.byte
mv -f $RPM_BUILD_ROOT%{_bindir}/ocamlopt.opt $RPM_BUILD_ROOT%{_bindir}/ocamlopt
rm -f $RPM_BUILD_ROOT%{_libdir}/%{_name}/*.ml

gzip -9nf LICENSE Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc htmlman *.gz
%attr(755, root, root) %{_bindir}/*
%{_libdir}/%{name}
%{_mandir}/man*/*

%files emacs
%defattr(644,root,root,755)
%{_libdir}/emacs/site-lisp/*.el
