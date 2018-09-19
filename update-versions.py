#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import glob
from github import Github

import yaml
import io
from datetime import datetime
import re


def get_tag():
    g = Github()
    regex = metadata['github']['tags']['regex']
    for t in g.get_repo(r).get_tags():
        # This list is already sorted for us by github
        if regex is not None:
            if re.match(regex, t.name):
                return t
        else:
            return t
    return None

def get_release():
    g = Github()
    if 'releases' in metadata['github'].keys() and \
        'prereleases' in metadata['github']['releases'].keys() and \
        metadata['github']['releases']['prereleases'] == True:
            return g.get_repo(r).get_releases()[0]
    else:
        return g.get_repo(r).get_latest_release()

    return None

def get_branch():
    g = Github()
    branch = metadata['github']['branch']
    return g.get_repo(r).get_branch(branch).commit

# load projects
for filename in glob.iglob('./**/build.yaml', recursive=True):
    with open(filename, 'r') as configFile:
        metadata = yaml.load(configFile)

    project = metadata['name']

    if 'github' in metadata.keys():
        r = metadata['github']['repo']
        print("Updating %s from GitHub(%s)" % (project, r))
        if 'branch' in metadata['github'].keys():
            commit = get_branch()
            if commit == None:
                print("Unable to determine SHA for %s" % project)
                continue
            name = metadata['github']['branch']
            version = commit.sha
        elif 'tags' in metadata['github'].keys():
            tag = get_tag()
            if tag == None:
                print("Unable to determine tag for %s" % project)
                continue
            name = tag.name
            version = tag.name
        else: # Assume default behavior of using releases
            rel = get_release()
            if rel == None:
                print("Unable to get latest release for %s" % project)
                continue
            name = rel.title
            version = rel.tag_name

        args = {'release_name': name, 'version': version,}
        args['version_numeric'] = re.sub(r"(?i)^v", "",  version) # Strip leading v
        metadata['version_info'] = args

    with open(filename, 'w') as configFile:
        yaml.dump(metadata, configFile, default_flow_style=False, allow_unicode=True)
