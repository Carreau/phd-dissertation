make clean
make latex
make pdf
make html
make epub

cd ~/tauth
echo $(pwd)
rm -rf files
cp -r ~/dissertation/_build ./files
git add files/
git commit -am'autocommit'
git push heroku master:master
