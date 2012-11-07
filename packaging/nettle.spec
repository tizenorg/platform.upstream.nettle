Name:           nettle
Version:        2.4
Release:        0
Summary:        Cryptographic Library
License:        LGPL-2.1+ and GPL-2.0+
Group:          System/Libraries
Source0:        ftp://ftp.lysator.liu.se/pub/security/lsh/nettle-%{version}.tar.gz
Source1:        baselibs.conf
BuildRequires:  gmp-devel
BuildRequires:  pkgconfig

%description
Nettle is a cryptographic library that is designed to fit easily in more or
less any context: In crypto toolkits for object-oriented languages (C++,
Python, Pike, ...), in applications like LSH or GNUPG, or even in kernel space.

%package -n libhogweed

Summary:        Cryptographic Library for Public Key Algorithms
License:        LGPL-2.1+
Group:          System/Libraries

%description -n libhogweed
Nettle is a cryptographic library that is designed to fit easily in more or
less any context: In crypto toolkits for object-oriented languages (C++,
Python, Pike, ...), in applications like LSH or GNUPG, or even in kernel space.

The libhogweed library contains public key algorithms to use with libnettle.

%package -n libnettle-devel
Summary:        Cryptographic Library
License:        LGPL-2.1+
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       gmp-devel
Requires:       libhogweed = %{version}
Requires:       libnettle = %{version}

%description -n libnettle-devel
Nettle is a cryptographic library that is designed to fit easily in more or
less any context: In crypto toolkits for object-oriented languages (C++,
Python, Pike, ...), in applications like LSH or GNUPG, or even in kernel space.

%package -n libnettle

Summary:        Cryptographic Tools
License:        LGPL-2.1+ and GPL-2.0+
Group:          Productivity/Security

%description -n libnettle
Nettle is a cryptographic library that is designed to fit easily in more or
less any context: In crypto toolkits for object-oriented languages (C++,
Python, Pike, ...), in applications like LSH or GNUPG, or even in kernel space.

This package contains a few command-line tools to perform cryptographic
operations using the nettle library.

%prep
%setup -q -n "nettle-%{version}"

%build
%configure --disable-static \
	 --enable-shared

make %{?_smp_mflags}

%check
make check

%install
%make_install

%post   -n libnettle -p /sbin/ldconfig

%postun -n libnettle -p /sbin/ldconfig

%post   -n libhogweed -p /sbin/ldconfig

%postun -n libhogweed -p /sbin/ldconfig


%files -n libnettle
%defattr(-,root,root)
%doc COPYING*
%{_libdir}/libnettle.so.
%{_libdir}/libnettle.so..*

%files -n libhogweed
%defattr(-,root,root)
%{_libdir}/libhogweed.so.
%{_libdir}/libhogweed.so..*

%files -n libnettle-devel
%defattr(-,root,root)
%{_includedir}/nettle
%{_libdir}/libnettle.so
%{_libdir}/libhogweed.so
%{_infodir}/nettle.info%{ext_info}
%{_libdir}/pkgconfig/hogweed.pc
%{_libdir}/pkgconfig/nettle.pc

%files -n nettle
%defattr(-,root,root)
%doc COPYING*
%{_bindir}/nettle-lfib-stream
%{_bindir}/pkcs1-conv
%{_bindir}/sexp-conv
%{_bindir}/nettle-hash

# Local Variables:
# mode: rpm-spec
# tab-width: 3
# End:

%changelog
