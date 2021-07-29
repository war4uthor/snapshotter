# Snapshotter
Python3 screenshot utility for creating a full-page image of a webpage. Uses Selenium in headless browser mode.

# Installation
snapshotter.py requires selenium as a dependency to run. It can be installed using pip as follows:

```bash
pip install selenium
```

# Usage
snapshotter.py can be run as follows. If running on Kali Linux, remember to run as a **non-root** user.

```bash
python3 snapshotter.py                                                                                       2 ⚙
usage: snapshotter.py [-h] -u URLS
snapshotter.py: error: the following arguments are required: -u/--urls

python3 snapshotter.py -u domains.txt
```
