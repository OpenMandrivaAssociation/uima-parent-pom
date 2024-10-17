%{?_javapackages_macros:%_javapackages_macros}
Name:          uima-parent-pom
Version:       8
Release:       5%{?dist}
Summary:       Apache UIMA Parent POM
License:       ASL 2.0
URL:           https://uima.apache.org/
Source0:       https://github.com/apache/uima-build/archive/parent-pom-%{version}.tar.gz
# uima-parent-pom package don't include the license file
# reported @ https://issues.apache.org/jira/browse/UIMA-3575
Source1:       http://www.apache.org/licenses/LICENSE-2.0.txt
# fix maven-plugin-bundle configuration
Patch0:        uima-parent-pom-8.patch

BuildRequires: maven-local
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-plugin-build-helper
#BuildRequires: maven-remote-resources-plugin
BuildRequires: maven-antrun-plugin
BuildRequires: mvn(ant-contrib:ant-contrib)
BuildRequires: mvn(org.apache.ant:ant-apache-regexp)
#BuildRequires: maven-resources-plugin

BuildArch:     noarch

%description
UIMA (Unstructured Information Management Architecture).
UIMA promotes community development and reuse of annotators
that extract meta-data from unstructured information (text,
audio, video, etc.); it provides for externalized declaration of
type systems, component configuration, aggregation, and more,
supports scalablity, and provides tooling.

This package provides Parent for Apache UIMA Projects.

%prep
%setup -q -n uima-build-parent-pom-%{version}

%patch0 -p0

%pom_remove_plugin org.apache.uima:uima-build-helper-maven-plugin
%pom_remove_plugin com.agilejava.docbkx:docbkx-maven-plugin
%pom_remove_plugin :maven-changes-plugin
%pom_remove_plugin :maven-dependency-plugin
%pom_remove_plugin :maven-assembly-plugin
%pom_remove_plugin :maven-remote-resources-plugin

# unavailable deps org.apache.uima:uima-docbook-olink:zip:olink:1-SNAPSHOT
# https://svn.apache.org/repos/asf/uima/build/trunk/uima-docbook-olink/
%pom_xpath_remove "pom:profiles/pom:profile[pom:id = 'process-docbook']"
# Unavailable deps
%pom_xpath_remove "pom:profiles/pom:profile[pom:id = 'build-eclipse-update-subsite']"
%pom_xpath_remove "pom:profiles/pom:profile[pom:id = 'build distribution']"

cp -p %{SOURCE1} .
sed -i 's/\r//' LICENSE-2.0.txt README.txt

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE-2.0.txt README.txt

%changelog
* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 8-4
- Rebuild to regenerate Maven auto-requires

* Fri Jan 17 2014 gil cattaneo <puntogil@libero.it> 8-3
- add BR maven-resource-plugin
- remove unnecessary BR java-devel

* Thu Jan 16 2014 gil cattaneo <puntogil@libero.it> 8-2
- fix build deps list

* Wed Jan 15 2014 gil cattaneo <puntogil@libero.it> 8-1
- update to 8

* Tue Aug 27 2013 gil cattaneo <puntogil@libero.it> 6-1
- update to 6

* Wed Feb 06 2013 gil cattaneo <puntogil@libero.it> 4-1
- initial rpm
