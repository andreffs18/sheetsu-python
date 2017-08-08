
# sheetsu-python


## Installation

You can start by cloning this repo:
```

$ git clone 
$ mkvirtualenv sheetsu --python=python3
$ pip install -r requirements.txt
```

Or simply do:

```
pip install sheetsu-python

```

## Usage

### Generating a Client

You need to create a new sheetsu function, and populate it with your Sheetsu API URL. You can find this URL on [Sheetsu Dashboard](https://sheetsu.com/your-apis).

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
Remember to populate the first row of every sheet with column names. 
You can look at [example spreadsheet](https://docs.google.com/spreadsheets/d/1WTwXrh2ZDXmXATZlQIuapdv4ldyhJGZg7LX8GlzPdZw/edit?usp=sharing).

### Read 
[Link to docs](https://docs.sheetsu.com/#read)

```python
# Read all available rows from default sheet:
print(client.read())

# Read only first two 2 rows:
print(client.read(limit=2))

# Read only 2 rows, starting from the 3'rd
print(client.read(limit=2, offset=2))

# Read 3 rows from "Sheet2"
print(client.read(sheet="Sheet2", limit=3))
```


### Search
[Link to docs](https://docs.sheetsu.com/#search-spreadsheet)

```python
# Search on default sheet for all names
print(client.search(name="*"))

# Search on default sheet for score = 42, but return only the first result 
print(client.search(score=42, limit=1))

# Search on "Sheet2" for name "User", but ignore casing
print(client.search(sheet="Sheet2", name="User", ignore_case=True))

```

### Create
[Link to docs](https://docs.sheetsu.com/#create)

```python
# Create a new entry on default sheet
print(client.create_one(name="New User", score=0))

# Create two new entries on sheet "Sheet2"
print(client.create_many(sheet="Sheet2", *[dict(name="onename"), dict(name="othername")]))

```



### Update
[Link to docs](https://docs.sheetsu.com/#update)

````python
# Update on default sheet, "Peter's" score to 120
print(client.update(column="name", value="Peter", data=dict(score=120)))
````

### Delete
[Link to docs](https://docs.sheetsu.com/#delete)

````python
# Delete "Peter" user from default sheet
print(client.delete(column="name", value="Peter"))
````

## Development

Run all tests and generate coverage report

```shell
$ coverage run --source=sheetsu/ setup.py test
$ coverage report 
```

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/sheetsu/sheetsu-ruby. This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the [Contributor Covenant](http://contributor-covenant.org) code of conduct.

### Pull Requests

- **Add tests!** Your patch won't be accepted if it doesn't have tests.

- **Create topic branches**. Please, always create a branch with meaningful name. Don't ask us to pull from your master branch.

- **One pull request per feature**. If you want to do more than one thing, please send
  multiple pull requests.

- **Send coherent history**. Make sure each individual commit in your pull
  request is meaningful. If you had to make multiple intermediate commits while
  developing, please squash them before sending them to us.

### Docs

[Sheetsu documentation sits on GitHub](https://github.com/sheetsu/docs). We would love your contributions! We want to make these docs accessible and easy to understand for everyone. Please send us Pull Requests or open issues on GitHub.


## Changes

##### [v0.1.1]
* Added tests to all available _Resources_.

##### [v0.1.0]
* Initial working version


