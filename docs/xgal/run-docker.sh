#!/bin/bash
. .env

docker run -it --rm --name $containername \
      --mount source=$dockervolumename,target=$dockervolumemount \
      -v $(pwd):/work \
      -v /home/jgi:/home/jgi \
      $dockertag bash
