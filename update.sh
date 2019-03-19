#!/bin/bash
# Takes the patch number as the first argument, curls the appropriate file, and unzips it

base="https://ddragon.leagueoflegends.com/cdn/dragontail-"
end=".tgz"
output="$base$1$end"

tar_base="dragontail-"
tar_output="$tar_base$1$end"

curl -O $output
tar -xzvf $tar_output
