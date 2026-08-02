# hr4rs

Print horizontal rules. Rust port of port of https://github.com/own-neufeldm/hr.

## Requirements

The following dependencies must already be installed on your system:

| Dependency                                      | Version                   |
| ----------------------------------------------- | ------------------------- |
| [rust](https://www.rust-lang.org/tools/install) | rustup=^1.27, rustc=^1.80 |

Please refer to the official vendor documentation for setting up these requirements.

## Setup

Install the app using `cargo install`, e.g. directly from GitHub:

```
$ cargo install --git https://github.com/own-neufeldm/hr4rs

# ...
Installed package `hr4rs v1.0.0 (https://github.com/own-neufeldm/hr4rs#14793fa3)` (executable `hr4rs`)
```

You can now run the app using `hr4rs`.

## Usage

Use `hr4rs` without arguments to print an untitled horizontal rule:

```
$ hr4rs

// -------------------------------------------- //
```

Provide border characters and a title to print a comment, e.g. for Java:

```
$ hr4rs -l 40 -b "/*" "ToDo: fix bug"

/* ---------- ToDo: fix bug ---------- */
```

Note that the border characters are reversed on the right side.

See `hr4rs --help` for more options.
