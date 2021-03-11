# roo-parser-retail
**SAME AS roo-parser but with extra criterion for finding grocery stores specifically**
Proof of concept for parsing deliveroo sites for specific options to get some munch (now looks for grocery stores so I can get some snacks).

## System Requirements
These are system recommendations, the programme may work on other configurations.</br>


_Python 3.9.0_</br>
_BeautifulSoup 4.9.3_

## Installation
All packages not mentioned here should be included in Python 3.</br>

Install the BeautifulSoup package (Python 3) for parsing the html.</br>
`pip3 install beautifulsoup4`
</br>
Install the requests package (Python 3) for http requests.</br>
`pip3 install requests`

## Use
The proof of concept is fairly basic, as of January 17, 2021 the use is as follows:

### Default Run
Command: `python parser.py` </br>
</br>
_N.B._ if your python command is not mapped to Python 3 you may
need to instead use the command `python3`.</br>

### Additional Arguments
**Location**</br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Command: `python parser.py $LOCATION`</br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Replace `$LOCATION` with the location you want to search for.</br>
</br>
_N.B._ The `$LOCATION` must be in the
form of the url, so examples would be:
* for all London restaurant locations you would use `london`
* for more specific options could do `london/bexleyheath` or `aberdeen/hazelhead`
</br>
_N.B.2_ If you are doing a non-london location you may also need to change the res_pattern on line 50 (as of March 11)
</br>
</br>

**CSV Name**</br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Comand: `python parser.py $LOCATION $CSV_NAME`</br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Replace `$LOCATION` with the location you want to search for.</br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Replace `$CSV_NAME` with the name of the file you want to save to.</br>
</br>
_N.B._ The `$CSV_NAME` should be a simple string, the code will add ".csv" to
the end of it, e.g.
</br> `bexley_restaurants`
</br> `csvexample`
</br>

As of January 17, 2020 you must have a `$LOCATION` argument to have a
`$CSV_NAME` argument.

### Output
The code is currently limited to only parse a few pages for efficient testing,
to test more values, change or remove the indices for `href_links` in the for
loop of the `restaurant_checker` function in `parser.py` where specified 
(~line 46).
</br>

The code writes the results to a csv file with Name, Sale, URL, and Location 
fields where Sale is a boolean displaying whether or not a given restaurant is
running a sale. 

## Next Steps
* Make it so locations can be outside london without code modification
* Add flagging for arguments so `$CSV_NAME`can be specified without `$LOCATION`
* Potentially make multiple locations write to different csv pages
