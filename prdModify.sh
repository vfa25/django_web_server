#!/bin/bash

static_root="STATIC_ROOT = os.path.join(BASE_DIR, 'static')"

sed -i '' "s#\#[ ]*${static_root}#${static_root}#" djangoServer/settings.py
sed -i '' "s#DEBUG[ ]*=.*#DEBUG = False#" djangoServer/settings.py
