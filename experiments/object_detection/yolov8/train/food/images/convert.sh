# download release from github: https://github.com/monostream/tifig/releases and install at ~/tools/tifig
# then run these commands in the folder (just to keep things simple we normalize the file extension case before proceeding).

for f in *.HEIC; do mv "$f" "`echo $f | sed s/.HEIC/.heic/`"; done
for file in *.heic; do echo "~/tools/tifig -v -p $file ${file/%.heic/.jpg}"; done