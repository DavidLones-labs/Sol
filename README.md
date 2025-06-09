# JSON Tool

A small command-line utility for pretty-printing or minifying JSON data.

## Usage

```
python3 json_tool.py [--pretty | --minify] [FILE]
```

- If `FILE` is omitted, the tool reads JSON from `stdin`.
- By default or with `--pretty`, the output is formatted with indentation.
- With `--minify`, the output contains no unnecessary whitespace.

## Examples

Pretty-print a JSON file:

```
python3 json_tool.py --pretty data.json
```

Minify JSON from `stdin`:

```
cat data.json | python3 json_tool.py --minify
```
