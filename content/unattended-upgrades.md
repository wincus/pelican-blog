Title: Thoughts about upgrades automation
Date: 2014-12-01
Category: devops
Tags: debian, ubuntu, unattended-upgrades, puppet
Authors: Wincus
Summary: Server automatic upgrades, oh my!
Status: draft

I must confess that I first thought that server upgrades automatization was 
just crazy. Until one day I was feeling more confident about walking away my
comfort zone and started playing with it.

The Problem
-----------
If you administrate more than a few servers most probably keep them updated 
is a pain. You will eventually forget to do it, exposing yourself two big 
problems. First one, the obvious security consequences, as you are vulnerable
during that time window. The second problem is more subtle, as bigger updates
are most probably to fail than small and frequently ones.

All servers are equal, but some of them are more equal than others
------------------------------------------------------------------

Ok, now that you think that automatic upgrades are a neat idea, lets discuss 
some implications. Some upgrades require human intervention, whenever a manual 
merge in the configuration file is needed, for example. Some upgrades require 
the server to reboot itself, in order to apply the changes. How to deal with it?


The Solution
------------
Here is an simplified puppet manifest that will:

 - install the unattended-upgrades package (only debian based distros, I think)
 - expose 3 hiera variables:
     - auto-reboot: the server will reboot itself if needed
     - auto-upgrade: the server will upgrade itself if needed
     - auto-update: the server will apt-get update daily

 - configure the package using templates

```
class base_packages::unattendedupgrades {

        include mailutils
        include ssmtp

        $auto_reboot  = hiera('auto_reboot')
        $auto_upgrade = hiera('auto_upgrade')
        $auto_update  = hiera('auto_update')

        package {
                "unattended-upgrades":
                        ensure => installed,
        }

        file {
                "/etc/apt/apt.conf.d/20auto-upgrades":
                        ensure    => present,
                        owner     => root,
                        group     => root,
                        mode      => 0644,
                        content   => template("base_packages/20auto-upgrades.erb"),
        }

        file {
                "/etc/apt/apt.conf.d/50unattended-upgrades":
                        ensure    => present,
                        owner     => root,
                        group     => root,
                        mode      => 0644,
                        content   => template("base_packages/50unattended-upgrades.erb"),
        }
}

```


The templates are pretty straight forward. 

20auto-upgrades:
```
APT::Periodic::Update-Package-Lists "<% if @auto_update == true %> 1 <% else %> 0 <% end %>";
APT::Periodic::Unattended-Upgrade "<% if @auto_upgrade == true %> 1 <% else %> 0 <% end %>";
APT::Periodic::Verbose "1";
```

50unattended-upgrades:
```
Unattended-Upgrade::Allowed-Origins {
        "${distro_id}:${distro_codename}-security";
        "${distro_id}:${distro_codename}-updates";
        "Puppetlabs:precise";
        "LP-PPA-saltstack-salt:precise";
};
Unattended-Upgrade::Package-Blacklist {
};
Unattended-Upgrade::Mail "your@mail.org";
Unattended-Upgrade::Remove-Unused-Dependencies "true";
Unattended-Upgrade::Automatic-Reboot <% if @auto_reboot %> "true" <% else %> "false" <% end %>;

```

In other words, only upgrades from official repos, from puppet repo and from
salt repo are allowed. Set your email address is important, to keep you informed
about whats going on. If some package require a manual merge configuration file 
intervention, you will be noticed by email, for you to deal with it.

Some Hiera Magic
----------------

Now I don't want production servers to reboot automatically, cause I rather do
it myself when I'm sure I won't interrupt some critical mission process. Devel
and Testing servers are free to do whatever they like. In hieras terms:

production.yaml:

```
auto_reboot: false
auto_upgrade: true
auto_update: true

```
testing.yaml:

```
auto_reboot: true
auto_upgrade: true
auto_update: true

```
devel.yaml:

```
auto_reboot: true
auto_upgrade: true
auto_update: true

```


Some Nagios Magic
-----------------








Conclusions
-----------

Thanks for passing by!
