## dockerfiles


It turns out I'm very opinionated about my containers. My opinions are pretty
simple, a container should:

- only run one thing
- not run as root
- not use an init system (see first point above)
- be tagged with proper versions (come on people!)


A lot of containers out there don't follow this pattern so I've built a repo
where I can build containers that look and act like I want them to.



I push all my images quay.io under [nicolerenee](https://quay.io/nicolerenee).
Some of the images are also mirrored on dockerhub under
[nicolerenee](https://hub.docker/u/nicolerenee) but I make no guaruntees that
those are up to date.
