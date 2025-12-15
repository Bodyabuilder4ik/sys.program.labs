Name: count-files
Version: 1.0
Release: 1
Summary: Count files in /etc
License: GPL
BuildArch: noarch

%description
Bash script that counts files in /etc directory

%install
mkdir -p %{buildroot}/usr/bin
cp %{_sourcedir}/count_files.sh %{buildroot}/usr/bin/count_files.sh

%files
/usr/bin/count_files.sh

