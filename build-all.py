#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import glob
import subprocess
from github import Github
from pathlib import Path

import yaml

REPO_URL="quay.io/nicolerenee"

for filename in glob.iglob('./**/build.yaml', recursive=True):
    dir = filename.replace('/build.yaml', '')

    dockerfile = Path(dir+'/Dockerfile')
    if not dockerfile.is_file():
        continue

    with open(filename, 'r') as stream:
        metadata = yaml.load(stream)

    image = "%s/%s:%s" % (REPO_URL, metadata['name'], metadata['version_info']['version'])
    buildargs = ""

    for k in metadata['version_info'].keys():
        buildargs = "%s --build-arg %s=\"%s\"" % (buildargs, k, metadata['version_info'][k])

    cmd = "docker build --pull --rm --force-rm %s -t %s %s" % (buildargs, image, dir)
    print("DEBUG:::::")
    print("DEBUG::::: %s" % (cmd))
    print("DEBUG:::::")
    subprocess.run(cmd, shell=True, check=True)

    cmd = "docker push %s" % image
    subprocess.run(cmd, shell=True, check=True)
