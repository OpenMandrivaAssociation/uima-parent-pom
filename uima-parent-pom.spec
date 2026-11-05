Name:          uima-parent-pom
Version:       19
Release:       1
Summary:       Apache UIMA Parent POM
License:       ASL 2.0
URL:           https://uima.apache.org/
Source0:       https://github.com/apache/uima-parent-pom/archive/refs/tags/parent-pom-%{version}.tar.gz

BuildArch:     noarch
# Literal, so the first rpmbuild -bs records them before sysjar is installed.
BuildRequires:	maven
BuildRequires:	java-current-devel
BuildSystem:	maven
BuildOption:	validate

%description
UIMA (Unstructured Information Management Architecture).
UIMA promotes community development and reuse of annotators
that extract meta-data from unstructured information (text,
audio, video, etc.); it provides for externalized declaration of
type systems, component configuration, aggregation, and more,
supports scalablity, and provides tooling.

This package provides Parent for Apache UIMA Projects.

%prep
%setup -q -n uima-parent-pom-parent-pom-%{version}

%files -f .mfiles
%doc LICENSE NOTICE README.md
