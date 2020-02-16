# Logo &amp; Phone Numbers Extractor

Scrapy spider for fetching logo and phone numbers on websites.

Program requires `website.txt` file in root dir (one provided by default contains sample valid and invalid inputs). 

Logic for logo is first `img src`. This approach leads to garbage, but ensures at least some data is retreived. 

Logic for phone numbers: 
- must be a number that is between 6 and 18 digits in length
- may start with + or (
- may contain whitespace, parentheses, dash or slash anywhere (note: this leads to garbage and matches `"000000)"`)
                         
Approach again leads to some garbage, but makes sure at least some data is retreived. Validating phone numbers in any possible format may
be tricky (how to match `"13 22 23"` but not `"2019 06"`?). 

Uses `stdout:` for output in `JSON` format.

Inside `...\lpn-r` folder run:

`python run-lpn.py`

Docker image(use Linux containers?):

`docker pull j11195k/lpn-r:latest`

`docker run -i [id]`

