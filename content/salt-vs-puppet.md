Title: Salty Puppet
Date: 2014-11-18
Category: devops
Tags: salt, puppet, automation
Authors: wincus
Status: hidden
Summary: This article includes only my personal opinion, as usual, YMMV

Having worked with [puppet](http://puppetlabs.com) for a long time, I run into
[salt](http://saltstack.com). I was only looking for a remote execution tool,
cause the natural choice under puppet environments,
[mcollective](http://puppetlabs.com/mcollecive), seemed to complicate to
install/configure/use/whatsoever.

So I started digging salty waters, to find that salt was much more than a
simple remote execution tool.

 * salt is written in python, if you like python better than ruby, this is a
   major advantage.
 * salt can enforce the state of a target system, just like puppet
 * states are written in yaml, easier to read and easier to write
 * all salt states are rendered, which means that you can do things like:

```
{% for mnt in salt['cmd.run']('ls /dev/data/moose*').split() %}
/MNT/moose{{ mnt[-1] }}:
  mount.mounted:
    - device: {{ mnt }}
    - fstype: xfs
    - mkmnt: True
  file.directory:
    - user: mfs
    - group: mfs
    - require:
      - user: mfs
      - group: mfs
{% endfor %}
```
 * you can even choose the render subsystem you like
 * custom modules are extremely easy to write
 * documentation is well organized and easy to follow
 * The company behind it, SaltStack, is not offering a different product for
   community and enterprise, as puppet. Their business model is based on
   support services.
 * at this very moment, salt github activity doubles puppet's (42k vs 20k commits)
 * salts community seems to be friendlier than puppet
 * salts momentum is much bigger, according to [google
   trends](http://www.google.com/trends/explore#q=saltstack%2C%20puppetlabs&cmpt=q)
 * salt has native cloud controller included, supporting cloud big players like
   amazon, google, docker, etc
 * salt has a native event & react subsytem, that allows you to react to events
   if needed
 * it can fetch states directly from your git repo, non error-prune intermediaries
 * salt can run in multi-master mode
 * salt can run minionless, using salt-ssh
 * salt state ecosystem seems to be richer
 * targeting at salt minions is incredibly flexible and powerful (batching
   execution for example)

Thanks for passing by!
