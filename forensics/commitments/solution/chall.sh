#!/bin/bash
mkdir commitments && cd commitments

cp ../main.py .
echo "TOKEN=shellmates{N3v3r_4dD_Y0UR_53cr37_70_7H3_C0Mmi7s}" > .env

git init 
git add .
git commit -m 'initial commit'


rm .env
echo '.env' > .gitignore
git add .
git commit -m 'removing some config files'

cd ..
zip -r commitments.zip commitments


