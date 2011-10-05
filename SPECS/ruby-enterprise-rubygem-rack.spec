%define ruby_dist ruby-enterprise
%define ruby_dist_dash %{ruby_dist}-
%define _prefix /opt/ruby-enterprise
%define _gem %{_prefix}/bin/gem
%define _ruby %{_prefix}/bin/ruby

# Generated from rack-1.1.0.gem by gem2rpm -*- rpm-spec -*-
%define ruby_sitelib %(%{_ruby} -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define gemdir %(%{_ruby} -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gemname rack
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: a modular Ruby webserver interface
Name: %{?ruby_dist_dash}rubygem-%{gemname}
Version: 1.1.0
Release: 1%{?dist}
Packager: Adam Vollrath at End Point <hosting@endpoint.com>
Vendor: Christian Neukirchen <chneukirchen@gmail.com>
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://rack.rubyforge.org
Source0: %{gemname}-%{version}.gem
Source1: %{name}.spec.template
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: %{?ruby_dist_dash}rubygems
BuildRequires: %{?ruby_dist_dash}rubygems
BuildArch: noarch
Provides: %{?ruby_dist_dash}rubygem(%{gemname}) = %{version}

%description
Rack provides minimal, modular and adaptable interface for developing
web applications in Ruby.  By wrapping HTTP requests and responses in
the simplest way possible, it unifies and distills the API for web
servers, web frameworks, and software in between (the so-called
middleware) into a single method call.
Also see http://rack.rubyforge.org.


%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gemdir}
export GEM_HOME=%{buildroot}%{gemdir}
export GEM_PATH=%{buildroot}%{gemdir}:`gem env gempath`
%{_gem} install --local --force --rdoc %{SOURCE0}
mkdir -p %{buildroot}/%{_bindir}
mv %{buildroot}%{gemdir}/bin/* %{buildroot}/%{_bindir}
rmdir %{buildroot}%{gemdir}/bin
find %{buildroot}%{geminstdir}/bin -type f | xargs chmod a+x

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{_bindir}/rackup
%{gemdir}/gems/%{gemname}-%{version}/
%doc %{gemdir}/doc/%{gemname}-%{version}
%doc %{geminstdir}/README
%doc %{geminstdir}/SPEC
%doc %{geminstdir}/KNOWN-ISSUES
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec


%pre
# Do not install this RPM if the gem is already installed another way.
# Check for .gemspec file that exists and is not provided by an RPM.
if ([ -e "%{gemdir}/specifications/%{gemname}-%{version}.gemspec" ] && !(rpm -q --whatprovides "%{gemdir}/specifications/%{gemname}-%{version}.gemspec" >/dev/null)); then
    exit 1
else
    exit 0
fi

# Do not install if %{_bindir}/rackup exists and is not provided by an RPM.
if ([ -e "%{_bindir}/rackup" ] && !(rpm -q --whatprovides "%{_bindir}/rackup" >/dev/null)); then
    exit 1
else
    exit 0
fi

%changelog
* Mon Oct  3 2011 Jeff Goldschrafe <jeff@holyhandgrenade.org> - 1.1.0-1
- Rebuild for Ruby Enterprise Edition

* Thu Aug 19 2010 End Point Hosting Team <hosting@endpoint.com> - 1.1.0-1
- Initial package
