# uAu - unattended Arch upgrade

Unattended upgrades are completely against the Arch philosophy!

So **NEVER ever** set the _AUTOUPGRADE_ of uAu!!! ;)


##  The usual Arch upgrade flow

Upgrading Arch means you have to follow this:

### BEFORE starting any upgrade

    1) Read the Arch news site
    2) If you use packages from the AUR it is recommended to check the latest comments there
    3) Take your time for doing the upgrade

### DOING the upgrade

    4) Always sync the databases before doing anything else
    5) Partial Upgrades are totally unsupported! So never ever use "IgnorePkg" --ignore or --ignoregroup
    6) Sit down, answer questions, make the upgrade interactively

### AFTER the upgrade

    7) Check systemd failure states
    8) Check journal for high prio errors
    


## The uAu flow (default)

uAu will by default do for you:

    steps 1,2 and 4 and send this by Email so you stay informed in order to do the other steps

## The uAu flow (advanced)

uAu CAN do for you (if you change the default setting):

    steps 1-8 and send you the results by Email
    (means a fully unattended upgrade with all the above)



What this is:


````
[04-28 10:44] <steadfasterX> before upgrading: 1) read the arch news page 2) read latest AUR comments of your packages 3) upgrading interactively (means you sit for 10min or longer , answering questions, typing password etc)
[04-28 10:44] <steadfasterX> doing all this REGULARY
[04-28 10:44] <steadfasterX> no one actually will do this
[04-28 10:45] <steadfasterX> they all tell you u have to do it this way
[04-28 10:45] <steadfasterX> but..
[04-28 10:45] <steadfasterX> at the end they install updates and when something fails they google the errors
[04-28 10:45] <steadfasterX> so
[04-28 10:45] <steadfasterX> why not just doing it automatically?
[04-28 10:45] <steadfasterX> ffs
[04-28 10:46] <steadfasterX> I have made a tool which is doing all the above
[04-28 10:46] <steadfasterX> sending you information by mail and doing the whole upgrade stuff based on a calendar timer etc
[04-28 10:49] <steadfasterX> it checks for the repo packages to upgrade and then parses the Arch News page
[04-28 10:49] <steadfasterX> it check for the AUR packages and show the latest X comments for them
[04-28 10:49] <steadfasterX> it shows the last Arch general News
[04-28 10:49] <steadfasterX> (even when not for a specific pacakge)
[04-28 10:50] <steadfasterX> it upgrades ofc
[04-28 10:50] <steadfasterX> and then it is not the end
[04-28 10:50] <steadfasterX> !
[04-28 10:51] <steadfasterX> it checks systemd failures before and after the upgrade and displays you the diff
[04-28 10:51] <steadfasterX> it checks high prio failures since the upgrade in your journal
[04-28 10:51] <steadfasterX> NO ONE WILL ACTUALLY DO THIS ALL ABOVE MANUALLY - NO ONE!!
[04-28 10:51] <steadfasterX> only when there is a problem ofc
[04-28 10:52] <steadfasterX> but uAu does this all.. every time .. automatically
[04-28 10:52] <steadfasterX> i forgot to mention that the whole crap is fully configurable to your needs x)
````

