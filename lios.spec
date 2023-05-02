Summary:	Linux intelligent OCR solution
Name:		lios
Version:	2.8
Release:	1
License:	GPLv3+
Group:		Office
URL:		https://sourceforge.net/projects/%{name}
Source0:	https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:		lios-2.8-openmandrivize.patch
# (upstream) https://github.com/zendalona/lios/commit/73fc343c7929bb385ded53130d842dc5d084bfe3.patch
Patch1:		lios-2.8-Use_exact_versions_when_importing_Gtk_and_friends.patch
BuildArch:	noarch

BuildRequires:	pkgconfig(python)
BuildRequires:	imagemagick

Requires:	aspell-dictionary
Requires:	espeak
Requires:	imagemagick
Requires:	packagekit-gtk3-module
Requires:	poppler
Requires:	python-gi
Requires:	python-enchant
Requires:	python-speechd
Requires:	python-imaging
Requires:	python-sane
Requires:	tesseract

#Suggests:	cuneiform-linux

%description
Lios is a free and open source software for converting print in to text
using either scanner or a camera, It can also produce text out of scanned
images from other sources such as Pdf, Image, Folder containing Images or
screenshot. Program is given total accessibility for visually impaired.

Features include:
  · Import images from Scanner, PDFs, Folder or Webcam
  · Take and Recognize Screen-shot
  · Recognize Selected Areas(Rectangle selection)
  · Support two OCR Engines (Cuneiform,Tesseract)
  · 24 Language support (Given at the end), 30 more languages can be
    installed in Tesseract
  · Full Auto Rotation for any Language (if aspell installed for the
    language)
  · Side by side view of image and output
  · Advanced Scanner Brightness optimizer
  · Text Reader for low vision with Highlighting, With user selected
    Color, Font, and Background Color
  · Audio converter(espeak)
  · Spell-checker(aspell)
  · Export as pdf (text/images)
  · Dictionary Support for English(Artha)
  · Options for save, load and reset settings
  · Other options - Find, Find-and-Replace, Go-To-Page, Go-To-Line,
    Append file, Punch File

Lios is written in python.

%files
# -f %name.lang
%license COPYING LICENSE
%doc README.md NEWS
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_mandir}/man1/%{name}.1*
%{_datadir}/%{name}/*
%{_datadir}/pixmaps/%{name}.xpm
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{py_puresitedir}/%{name}
%{py_puresitedir}/%{name}-*.*-info

#----------------------------------------------------------------------------

%prep
%autosetup -p1

%build
%py_build

%install
%py_install

# icons
for d in 16 32 48 64 72 128 256
do
	install -dm 0755 %{buildroot}%{_iconsdir}/hicolor/${d}x${d}/apps/
	convert -scale ${d}x${d} share/%{name}/%{name}.png \
			%{buildroot}%{_iconsdir}/hicolor/${d}x${d}/apps/%{name}.png
done
install -dm 0755 %{buildroot}%{_datadir}/pixmaps/
convert -scale ${d}x${d} share/%{name}/%{name}.png \
		 %{buildroot}%{_datadir}/pixmaps/%{name}.xpm

# handle license by macro
rm -fr %{buildroot}%{_docdir}/%{name}/copyright

# locales
#find_lang %name --all-name

