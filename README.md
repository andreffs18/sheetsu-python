
# sheetsu-python

[![PyPI version](https://badge.fury.io/py/sheetsu.svg)](https://badge.fury.io/py/sheetsu)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/0042777a1e2d4c46b97e697e2c5523cf)](https://www.codacy.com?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=andreffs18/sheetsu-python&amp;utm_campaign=Badge_Grade)
[![Codacy Badge](https://api.codacy.com/project/badge/Coverage/0042777a1e2d4c46b97e697e2c5523cf)](https://www.codacy.com?utm_source=github.com&utm_medium=referral&utm_content=andreffs18/sheetsu-python&utm_campaign=Badge_Coverage)

## Installation

You can simply do
```
$ pip install sheetsu
```

## Usage

### Generating a Client

```python
from sheetsu import SheetsuClient

client = SheetsuClient("<spreadsheed_id>")
```


If you have HTTP Basic Authentication turned on for your API, you should pass `api_key` and `api_secret` here, like:
```python
from sheetsu import SheetsuClient

client = SheetsuClient("<spreadsheed_id>", api_key="<api_key>", api_secret="<api_secret>")
```

### CRUD

Sheetsu gives you the ability to use full CRUD on your Google Spreadsheet. 
 

### Read 

More information can be found [here](https://docs.sheetsu.com/#read)

```python
# Read all available rows from default sheet
client.read()

# Read only first two 2 rows
client.read(limit=2)

# Read only 2 rows, starting from the 3'rd
client.read(limit=2, offset=2)

# Read 3 rows from "Sheet2"
client.read(sheet="Sheet2", limit=3)
```


### Search 

More information can be found [here](https://docs.sheetsu.com/#search-spreadsheet)

```python
# Search on default sheet for all names
client.search(name="*")

# Search on default sheet for score = 42, but return only the first result 
client.search(score=42, limit=1)

# Search on "Sheet2" for name "User", but ignore casing
client.search(sheet="Sheet2", name="User", ignore_case=True)

```

### Create 


More information can be found [here](https://docs.sheetsu.com/#create)

```python
# Create a new entry on default sheet
client.create_one(name="New User", score=0)

# Create two new entries on sheet "Sheet2"
client.create_many(sheet="Sheet2", *[dict(name="onename"), dict(name="othername")])

```



### Update 

More information can be found [here](https://docs.sheetsu.com/#update)

````python
# Update on default sheet, "Peter's" score to 120
client.update(column="name", value="Peter", data=dict(score=120))
````

### Delete 

More information can be found [here](https://docs.sheetsu.com/#delete)

````python
# Delete "Peter" user from default sheet (but leave empty row)
client.delete(column="name", value="Peter")

# Delete "Susan" user from default sheet, and remove row (moving later rows up)
client.delete(column="name", value="Susan", destroy="true")
````

## Development


Start by cloning this repo:

```
$ git clone 
$ mkvirtualenv sheetsu --python=python3
[sheetsu] $ pip install -r requirements.txt
```

Run all tests and generate coverage report

```shell
$ coverage run --source=sheetsu/ setup.py test
$ coverage report 
```

## Contributing

Bug, issues or features are welcome in this project. Feel free to open an issue or a pull request. Your help is highly appreciated.


## Changes
##### [v1.1.0](https://github.com/andreffs18/sheetsu-python/releases/tag/v1.1.0)
###### Added
* Destroy functionality to delete resource

##### [v1.0.0](https://github.com/andreffs18/sheetsu-python/releases/tag/v1.0.0)
###### Changed
* Update on Sheetsu api url.

##### v0.0.6
###### Fixed
* Status code verification to allow all "2*" codes. 

##### v0.0.2
###### Added
* Tests to all available _Resources_.

##### v0.0.1
* Initial working version.

<!--
Added for new features.
Changed for changes in existing functionality.
Deprecated for soon-to-be removed features.
Removed for now removed features.
Fixed for any bug fixes.
Security in case of vulnerabilities.
-->
