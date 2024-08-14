# hr

Print horizontal rules.

## Requirements

The following dependencies must already be installed on your system:

| Dependency                                  | Version |
| ------------------------------------------- | ------- |
| [python](https://www.python.org/downloads/) | ^3.12   |
| [pipx](https://pipx.pypa.io/stable/)        | ^1.6    |

Please refer to the official vendor documentation for setting up these requirements.

## Setup

Install the app using `pipx`, e.g. directly from GitHub using SSH:

```
$ pipx install git+ssh://git@github.com/own-neufeldm/hr.git

  installed package hr 1.0.0, installed using Python 3.12.5
  These apps are now globally available
    - hr.exe
done! ✨ 🌟 ✨
```

You can now run the app using `hr`.

## Usage

Use `hr` without arguments to print an untitled horizontal rule:

```
$ hr

# ---------------------------------------------- #
```

Provide border characters and a title to print a comment, e.g. for Java:

```
$ hr -l 40 -b "/*" "ToDo: fix bug"

/* ---------- ToDo: fix bug ---------- */
```

Note that the border characters are reversed on the right side.

See `hr --help` for more options.
