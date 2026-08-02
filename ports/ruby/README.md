# hr4rb

Print horizontal rules. Ruby port of port of https://github.com/own-neufeldm/hr.

## Requirements

tbc

## Setup

tbc

## Usage

Use `hr4rb` without arguments to print an untitled horizontal rule:

```
$ hr4rb

# ---------------------------------------------- #
```

Provide border characters and a title to print a comment, e.g. for Java:

```
$ hr4rb -l 40 -b "/*" "ToDo: fix bug"

/* ---------- ToDo: fix bug ---------- */
```

Note that the border characters are reversed on the right side.

See `hr4rb --help` for more options.
