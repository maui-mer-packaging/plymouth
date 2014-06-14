# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       plymouth

# >> macros
# << macros
%define plymouthclient_execdir %{_bindir}
%define plymouth_initrd_file /boot/initrd-plymouth.img
%define plymouth_libdir %{_libdir}
%define plymouthdaemon_execdir %{_sbindir}

Summary:    Graphical Boot Animation and Logger
Version:    0.9.0
Release:    1
Group:      System/Base
License:    GPL-2.0+
URL:        http://freedesktop.org/software/plymouth/releases
Source0:    %{name}-%{version}.tar.xz
Source100:  plymouth.yaml
Requires(preun): systemd
Requires(post): systemd
Requires(post): %{name}-scripts
Requires(postun): systemd
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  docbook-style-xsl
BuildRequires:  xz
BuildRequires:  systemd

%description
Plymouth provides an attractive graphical boot animation in
place of the text messages that normally get shown.  Text
messages are instead redirected to a log file for viewing
after boot.


%package core-libs
Summary:    Plymouth core libraries
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description core-libs
This package contains the libply and libply-splash-core libraries
used by Plymouth.


%package graphical-libs
Summary:    Plymouth graphics libraries
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description graphical-libs
This package contains the libply-splash-graphics library
used by graphical Plymouth splashes.


%package scripts
Summary:    Plymouth related scripts
Group:      Applications/System
Requires:   %{name} = %{version}-%{release}
Requires:   dracut

%description scripts
This package contains scripts that help integrate Plymouth with
the system.


%package plugin-label
Summary:    Plymouth label plugin
Group:      System/Base
Requires:   %{name} = %{version}-%{release}

%description plugin-label
This package contains the label control plugin for
Plymouth. It provides the ability to render text on
graphical boot splashes using pango and cairo.


%package plugin-fade-throbber
Summary:    Plymouth "Fade-Throbber" plugin
Group:      System/Base
Requires:   %{name} = %{version}-%{release}

%description plugin-fade-throbber
This package contains the "Fade-In" boot splash plugin for
Plymouth. It features a centered image that fades in and out
while other images pulsate around during system boot up.


%package plugin-throbgress
Summary:    Plymouth "Throbgress" plugin
Group:      System/Base
Requires:   %{name} = %{version}-%{release}
Requires:   %{name}-plugin-label

%description plugin-throbgress
This package contains the "throbgress" boot splash plugin for
Plymouth. It features a centered logo and animated spinner that
spins repeatedly while a progress bar advances at the bottom of
the screen.


%package plugin-space-flares
Summary:    Plymouth "space-flares" plugin
Group:      System/Base
Requires:   %{name} = %{version}-%{release}
Requires:   %{name}-plugin-label

%description plugin-space-flares
This package contains the "space-flares" boot splash plugin for
Plymouth. It features a corner image with animated flares.


%package plugin-two-step
Summary:    Plymouth "two-step" plugin
Group:      System/Base
Requires:   %{name} = %{version}-%{release}
Requires:   %{name}-plugin-label

%description plugin-two-step
This package contains the "two-step" boot splash plugin for
Plymouth. It features a two phased boot process that starts with
a progressing animation synced to boot time and finishes with a
short, fast one-shot animation.


%package plugin-script
Summary:    Plymouth "Script" plugin
Group:      System/Base
Requires:   %{name} = %{version}-%{release}

%description plugin-script
This package contains the "script" boot splash theme for
Plymouth. It it is a simple example theme the uses the "script"
plugin.


%package theme-fade-in
Summary:    Plymouth "Fade-In" theme
Group:      System/Base
Requires:   %{name} = %{version}-%{release}
Requires:   %{name}-plugin-fade-throbber = %{version}-%{release}
Requires(post): %{name}-scripts

%description theme-fade-in
This package contains the "Fade-In" boot splash theme for
Plymouth. It features a centered logo that fades in and out
while stars twinkle around the logo during system boot up.


%package theme-spinner
Summary:    Plymouth "Spinner" theme
Group:      System/Base
Requires:   %{name} = %{version}-%{release}
Requires:   %{name}-plugin-two-step = %{version}-%{release}
Requires(post): %{name}-scripts

%description theme-spinner
This package contains the "spinner" boot splash theme for
Plymouth. It features a small spinner on a dark background.


%package theme-spinfinity
Summary:    Plymouth "Spinfinity" theme
Group:      System/Base
Requires:   %{name} = %{version}-%{release}
Requires:   %{name}-plugin-throbgress = %{version}-%{release}
Requires(post): %{name}-scripts

%description theme-spinfinity
This package contains the "Spinfinity" boot splash theme for
Plymouth. It features a centered logo and animated spinner that
spins in the shape of an infinity sign.


%package theme-solar
Summary:    Plymouth "Solar" theme
Group:      System/Base
Requires:   %{name} = %{version}-%{release}
Requires:   %{name}-plugin-space-flares = %{version}-%{release}
Requires(post): %{name}-scripts

%description theme-solar
This package contains the "Solar" boot splash theme for
Plymouth. It features a blue flamed sun with animated solar flares.


%package theme-script
Summary:    Plymouth "Script" theme
Group:      System/Base
Requires:   %{name} = %{version}-%{release}
Requires:   %{name}-plugin-script = %{version}-%{release}
Requires(post): %{name}-scripts

%description theme-script
This package contains the "script" boot splash theme for
Plymouth. It it is a simple example theme the uses the "script"
plugin.


%package devel
Summary:    Libraries and headers for writing Plymouth splash plugins
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
This package contains the libply and libplybootsplash libraries
and headers needed to develop 3rd party splash plugins for Plymouth.


%prep
%setup -q -n %{name}-%{version}/upstream

# >> setup
# << setup

%build
# >> build pre
# << build pre

%reconfigure --disable-static \
    --enable-systemd-integration \
    --enable-tracing \
    --disable-tests \
    --disable-gtk \
    --disable-gdm-transition \
    --with-logo=%{_datadir}/pixmaps/system-logo-white.png \
    --with-background-start-color-stop=0x0073B3 \
    --with-background-end-color-stop=0x00457E \
    --with-background-color=0x3391cd \
    --without-system-root-install \
    --without-log-viewer \
    --without-rhgb-compat-link \
    --with-release-file=/etc/os-release \
    --without-gdm-autostart-file

make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
# Glow isn't quite ready for primetime
rm -rf $RPM_BUILD_ROOT%{_datadir}/plymouth/glow/
rm -f $RPM_BUILD_ROOT%{_libdir}/plymouth/glow.so
rm -rf $RPM_BUILD_ROOT%{_datadir}/plymouth/themes/glow

# No static libraries, please
find $RPM_BUILD_ROOT -name '*.a' -exec rm -f {} \;
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} \;

# Default configuration
cat >$RPM_BUILD_ROOT%{_sysconfdir}/plymouth/plymouthd.conf <<EOF
[Daemon]
Theme=tribar
EOF
# << install post

%post core-libs -p /sbin/ldconfig

%postun core-libs -p /sbin/ldconfig

%post graphical-libs -p /sbin/ldconfig

%postun graphical-libs -p /sbin/ldconfig

%postun theme-fade-in
# >> postun theme-fade-in
export LIB=%{_lib}
if [ $1 -eq 0 ]; then
if [ "$(%{_sbindir}/plymouth-set-default-theme)" == "fade-in" ]; then
%{_sbindir}/plymouth-set-default-theme --reset
%{_libexecdir}/plymouth/plymouth-generate-initrd
fi
fi
# << postun theme-fade-in

%postun theme-spinner
# >> postun theme-spinner
export LIB=%{_lib}
if [ $1 -eq 0 ]; then
if [ "$(%{_sbindir}/plymouth-set-default-theme)" == "spinner" ]; then
%{_sbindir}/plymouth-set-default-theme --reset
%{_libexecdir}/plymouth/plymouth-generate-initrd
fi
fi
# << postun theme-spinner

%postun theme-spinfinity
# >> postun theme-spinfinity
export LIB=%{_lib}
if [ $1 -eq 0 ]; then
if [ "$(%{_sbindir}/plymouth-set-default-theme)" == "spinfinity" ]; then
%{_sbindir}/plymouth-set-default-theme text
%{_libexecdir}/plymouth/plymouth-generate-initrd
fi
fi
# << postun theme-spinfinity

%postun theme-solar
# >> postun theme-solar
export LIB=%{_lib}
if [ $1 -eq 0 ]; then
if [ "$(%{_sbindir}/plymouth-set-default-theme)" == "solar" ]; then
%{_sbindir}/plymouth-set-default-theme --reset
%{_libexecdir}/plymouth/plymouth-generate-initrd
fi
fi
# << postun theme-solar

%files
%defattr(-,root,root,-)
%doc AUTHORS NEWS README
%dir %{_datadir}/plymouth
%dir %{_datadir}/plymouth/themes
%dir %{_datadir}/plymouth/themes/details
%dir %{_datadir}/plymouth/themes/text
%dir %{_libexecdir}/plymouth
%dir %{_localstatedir}/lib/plymouth
%dir %{_libdir}/plymouth/renderers
%dir %{_sysconfdir}/plymouth
%config(noreplace) %{_sysconfdir}/plymouth/plymouthd.conf
%{plymouthdaemon_execdir}/plymouthd
%{plymouthclient_execdir}/plymouth
%{_libdir}/plymouth/details.so
%{_libdir}/plymouth/text.so
%{_libdir}/plymouth/tribar.so
%{_libdir}/plymouth/renderers/drm*
%{_libdir}/plymouth/renderers/frame-buffer*
%{_datadir}/plymouth/themes/details/details.plymouth
%{_datadir}/plymouth/themes/text/text.plymouth
%{_datadir}/plymouth/themes/tribar/tribar.plymouth
%{_datadir}/plymouth/plymouthd.defaults
%{_localstatedir}/run/plymouth
%{_localstatedir}/spool/plymouth
%{_mandir}/man?/*
%{_unitdir}/*
# >> files
# << files

%files core-libs
%defattr(-,root,root,-)
%{plymouth_libdir}/libply.so.*
%{plymouth_libdir}/libply-splash-core.so.*
%{_libdir}/libply-boot-client.so.*
%dir %{_libdir}/plymouth
# >> files core-libs
# << files core-libs

%files graphical-libs
%defattr(-,root,root,-)
%{_libdir}/libply-splash-graphics.so.*
# >> files graphical-libs
# << files graphical-libs

%files scripts
%defattr(-,root,root,-)
%{_sbindir}/plymouth-set-default-theme
%{_libexecdir}/plymouth/plymouth-update-initrd
%{_libexecdir}/plymouth/plymouth-generate-initrd
%{_libexecdir}/plymouth/plymouth-populate-initrd
# >> files scripts
# << files scripts

%files plugin-label
%defattr(-,root,root,-)
%{_libdir}/plymouth/label.so
# >> files plugin-label
# << files plugin-label

%files plugin-fade-throbber
%defattr(-,root,root,-)
%{_libdir}/plymouth/fade-throbber.so
# >> files plugin-fade-throbber
# << files plugin-fade-throbber

%files plugin-throbgress
%defattr(-,root,root,-)
%{_libdir}/plymouth/throbgress.so
# >> files plugin-throbgress
# << files plugin-throbgress

%files plugin-space-flares
%defattr(-,root,root,-)
%{_libdir}/plymouth/space-flares.so
# >> files plugin-space-flares
# << files plugin-space-flares

%files plugin-two-step
%defattr(-,root,root,-)
%{_libdir}/plymouth/two-step.so
# >> files plugin-two-step
# << files plugin-two-step

%files plugin-script
%defattr(-,root,root,-)
%{_libdir}/plymouth/script.so
# >> files plugin-script
# << files plugin-script

%files theme-fade-in
%defattr(-,root,root,-)
%dir %{_datadir}/plymouth/themes/fade-in
%{_datadir}/plymouth/themes/fade-in/bullet.png
%{_datadir}/plymouth/themes/fade-in/entry.png
%{_datadir}/plymouth/themes/fade-in/lock.png
%{_datadir}/plymouth/themes/fade-in/star.png
%{_datadir}/plymouth/themes/fade-in/fade-in.plymouth
# >> files theme-fade-in
# << files theme-fade-in

%files theme-spinner
%defattr(-,root,root,-)
%dir %{_datadir}/plymouth/themes/spinner
%{_datadir}/plymouth/themes/spinner/*.png
%{_datadir}/plymouth/themes/spinner/spinner.plymouth
# >> files theme-spinner
# << files theme-spinner

%files theme-spinfinity
%defattr(-,root,root,-)
%dir %{_datadir}/plymouth/themes/spinfinity
%{_datadir}/plymouth/themes/spinfinity/box.png
%{_datadir}/plymouth/themes/spinfinity/bullet.png
%{_datadir}/plymouth/themes/spinfinity/entry.png
%{_datadir}/plymouth/themes/spinfinity/lock.png
%{_datadir}/plymouth/themes/spinfinity/throbber-[0-3][0-9].png
%{_datadir}/plymouth/themes/spinfinity/spinfinity.plymouth
# >> files theme-spinfinity
# << files theme-spinfinity

%files theme-solar
%defattr(-,root,root,-)
%dir %{_datadir}/plymouth/themes/solar
%{_datadir}/plymouth/themes/solar/*.png
%{_datadir}/plymouth/themes/solar/solar.plymouth
# >> files theme-solar
# << files theme-solar

%files theme-script
%defattr(-,root,root,-)
%dir %{_datadir}/plymouth/themes/script
%{_datadir}/plymouth/themes/script/*.png
%{_datadir}/plymouth/themes/script/script.script
%{_datadir}/plymouth/themes/script/script.plymouth
# >> files theme-script
# << files theme-script

%files devel
%defattr(-,root,root,-)
%{plymouth_libdir}/libply.so
%{plymouth_libdir}/libply-splash-core.so
%{_libdir}/libply-boot-client.so
%{_libdir}/libply-splash-graphics.so
%{_libdir}/pkgconfig/ply-splash-core.pc
%{_libdir}/pkgconfig/ply-splash-graphics.pc
%{_libdir}/pkgconfig/ply-boot-client.pc
%{_includedir}/plymouth-1
# >> files devel
# << files devel
