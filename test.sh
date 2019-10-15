#!/bin/bash
set -e
set -o pipefail

# this is kind of an expensive check, so let's not do this twice if we
# are running more than one validate bundlescript
VALIDATE_REPO='https://github.com/nicolerenee/dockerfiles.git'
VALIDATE_BRANCH='master'

VALIDATE_HEAD="$(git rev-parse --verify HEAD)"

git fetch -q "$VALIDATE_REPO" "refs/heads/$VALIDATE_BRANCH"
VALIDATE_UPSTREAM="$(git rev-parse --verify FETCH_HEAD)"

VALIDATE_COMMIT_DIFF="$VALIDATE_UPSTREAM...$VALIDATE_HEAD"

validate_diff() {
	if [ "$VALIDATE_UPSTREAM" != "$VALIDATE_HEAD" ]; then
		git diff "$VALIDATE_COMMIT_DIFF" "$@"
	else
		git diff HEAD~ "$@"
	fi
}

# get the dockerfiles changed
IFS=$'\n'
files=( $(validate_diff --name-only -- '*Dockerfile' '*build.yaml') )
unset IFS

for f in "${files[@]}"; do
  build_dir=$(dirname "$f")
	if ! [[ -e "$build_dir"/Dockerfile ]]; then
		continue
	fi

  release_name=$(cat $build_dir/build.yaml | yq -r .version_info.release_name)
  version=$(cat $build_dir/build.yaml | yq -r .version_info.version)
  version_numeric=$(cat $build_dir/build.yaml | yq -r .version_info.version_numeric)

  img_cmd="docker run --rm -it
    --name img
    --volume $(pwd):/home/user/src
    --workdir /home/user/src
    --privileged
    r.j3ss.co/img"

	(
	set -x
  $img_cmd build --build-arg version="$version" --build-arg version_numeric="$version_numeric" --build-arg release_name="$release_name" -t test $build_dir
	)

	echo "                       ---                                   "
	echo "Successfully built ${build_dir} image"
	echo "                       ---                                   "
done
