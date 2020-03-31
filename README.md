# page
Book page tracker CLI 

1. clone the repository and change to the page directory
2. make the script executable with: sudo chmod +x page

Usage:

./page help

./page list

./page add \<id> \<isbn>

./page remove \<id>

./page modify \<id> \<key>=<value> (\<key>=<value> ...)

./page log \<id> \<page> (\<date>)

./page stats \<id>

To use "page" instead of "./page"

export PATH=/my/directory/to/this/script:$PATH
