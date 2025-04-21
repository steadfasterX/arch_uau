## Changelog

### v3.0.0

Major rewrite and first part of removing outdated dependencies.

If you upgrade from a previous release please check the new settings especially check the new paths and names!

Example:

```
sdiff -s /etc/unattended-arch-upgrade.conf /etc/unattended-arch-upgrade.conf.pacnew
```

Requirements:

- added: `python-feedparser`
- removed: `archnews2`
- removed: `python3-memoizedb`

Changes:

- all executables have been moved to `/usr/bin` (before `/usr/local/bin`)
- added: `uau-news-parser`
    - incl. enhanced output and several fixes
    - new option: `--html` (--text is set as default)
- added: `uau-package-parser`
    - incl. enhanced output/parsing
    - new option: `--html` (--text set as default)
- renamed: `uau-archnews` -> `uau-news-wrapper`
- removed: read/unread options for Arch news feed

Fixes:

- fix: using `yay` instead of `trizen` for AUR operations
- fix: migrating `egrep` -> `grep -E`, thanks to @asm0dey
- fix: be more POSIX compliant, thanks to @rgcv

