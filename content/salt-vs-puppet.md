Title: Salted Puppet
Date: 2014-11-18
Category: devops
Tags: salt, puppet, automation, devops
Authors: wincus
Summary: Just another ultra-biased salt vs puppet article.

Having worked with [puppet](http://puppetlabs.com) for a long time, I run into
[salt](http://saltstack.com) looking for a remote execution tool, as the 
natural choice under puppet environments, [mcollective](http://puppetlabs.com
/mcollective) seemed to complicate to install/configure/use/whatsoever.

So I started digging salty waters, to find that salt was much more than a
simple remote execution tool.

Targeting
---------
One of the challenges about remote execution is targeting. Of course you want
parallel remote execution in order to break the linear relation between
execution time and number of target nodes, but this feature is worthless
unless you have smart targeting subsystem.

So, how smart is Salt targeting? [Pretty much!](http://docs.saltstack.com/en/late
st/topics/targeting/)

For example, consider this example taken from the documentation:

``
salt -G 'os:RedHat' --batch-size 25% apache.signal restart
``

This will restart apache on all minions running RedHat, but wait, not all at
the same time, lets trigger 25% first, an then roll the window until you get
to 100%. 

State Enforcing
---------------
Salt can also enforce the state of a target system, just like puppet. 

[State](http://docs.saltstack.com/en/latest/topics/tutorials/starting_states.
html) files are written in [yaml](http://www.yaml.org/) honoring Salt's 
foundation principles: simplicity, simplicity, simplicity.

This yaml is only data representation of the states. As data, in reality we are 
just talking about dictionaries, lists, strings and numbers. If you are coming 
from puppet, you will need some time to realize that in Salts world it is you 
who decide how complex things are. The other big difference, in my opinion, is
that state files in Salt are rendered, and gets even better, you are free to 
choose the render engine, as long as delivers state data to Salt.  Unless told
otherwise, state files are first rendered using the default renderer,
[Jinja](http://jinja.pocoo.org/) before getting to the YAML parser.

This allows great flexibility, as shown in this example taken from the
documentation:

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
You have a pretty bast [module](http://docs.saltstack.com/en/latest/ref/modul
es/all/index.html#all-salt-modules) ecosystem to work with. And if that is not
enough you can write your own. Yes, writing custom models is really simple.

Another cool feature I like about Salt is how well plays with [git](http://do
cs.saltstack.com/en/latest/topics/tutorials/gitfs.html). Salt can fetch your 
state files (and pillar data) directly from one or more Git repos, mapping 
automatically environment branch/tags identifiers. This allows you to trigger
the magic on a single git commit.

Cloud friendly
--------------
Most management and configuration tools out there were born before the Cloud 
existed or was so popular, so developers didn't pay much attention to it until 
it was to late.

Salt, on the other hand, was created with [cloud](http://docs.saltstack.com/en/la
test/topics/cloud/) in mind from the beginning. This means, in my opinion, two 
important things. First you get a single interface for every cloud provider 
out there (Salt supports big cloud players like EC2, DigitalOcean, Azure, GCE, 
LXC, Docker, OpenStack, SoftLayer, and others). The second big advantage is
that you can manage your multi-provider instances from your state files:

```
my-instance-name:
  cloud.present:
    - provider: my-ec2-config
    - image: ami-1624987f
    - size: 't1.micro'
    - ssh_username: ec2-user
    - securitygroup: default
    - delvol_on_destroy: True
```

Reactor
-------
State management is great, but sometimes it just won't fit in real world 
scenarios. Here is where the Reactor systems comes to the rescue. It's basic 
workflow is pretty simple. There is an event bus, and every event fired into 
the bus has a tag and a data structure, a dict with information about the 
event. In order to react to this events, you can write state files and map 
them with the events that need special attention.

For example, a typical use case is when you fire up a new production cloud 
web instance. This will write a cloud event into the event bus with 
information about this new instance. What should happen when a new instance
gets created and configured? Probably you will want to include it in the backup
rutine, and you definitly will want to monitor it. No problem, just write the
proper sls files and map the event with the state file. Good enough?

Minionless nodes
----------------
Oh Yeah, Salt can control your nodes without the need to install a client
there, just by having [ssh](http://docs.saltstack.com/en/latest/topics/ssh/)
access to it. Of course it won't scale well if you have many nodes, and will 
be slower than the minionful counterpart, but its up to you. At the end, you 
get to decide how complex your setup will be, remember?

Documentation
-------------
Well organized and easy to follow, [documentation](http://docs.saltstack.com/
en/latest/) is another strong thing about Salt. Transaltions are quite slow 
to arrive, though. If you are considering donating some time to the project, 
helping with [translations](https://www.transifex.com/projects/p/salt/) are a 
always a good option.
