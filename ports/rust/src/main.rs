use clap::Parser;

#[derive(Debug, Parser)]
struct Args {
    /// An optional title
    title: Option<String>,

    /// Minimum character length
    #[arg(short, long, default_value_t = 50)]
    length: u32,

    /// Character(s) to use for outer borders
    #[arg(short, long, default_value_t = String::from("//"))]
    border: String,

    /// Character to use for inner fillers
    #[arg(short, long, default_value_t = String::from("-"))]
    filler: String,

    /// Prepend 'BEGIN' and 'END' before title
    #[arg(short, long, default_value_t = false)]
    paragraph: bool,

    /// Convert title to uppercase
    #[arg(short, long, default_value_t = false)]
    upper: bool,

    /// Do not print a new-line character at the end
    #[arg(short, long, default_value_t = false)]
    no_newline: bool,

    /// Show version and exit
    #[arg(short, long, default_value_t = false)]
    version: bool,
}

fn main() {
    let args = Args::parse();

    if args.version {
        println!(env!("CARGO_PKG_VERSION"));
        return;
    }

    let mut titles: Vec<String> = Vec::new();
    let mut title = args.title.unwrap_or("".to_string());
    if title.is_empty() {
        if args.paragraph {
            titles.push(String::from("BEGIN"));
            titles.push(String::from("END"));
        } else {
            titles.push(title)
        }
    } else {
        if args.upper {
            title = title.to_uppercase();
        }

        if args.paragraph {
            titles.push(format!("BEGIN {title}"));
            titles.push(format!("END {title}"));
        } else {
            titles.push(title)
        }
    }

    for title in titles.iter() {
        let horizontal_rule = hr4rs::get_horizontal_rule(
            title.to_string(),
            args.length,
            args.border.to_string(),
            args.filler[..1].to_string(),
        );

        if args.no_newline {
            print!("{horizontal_rule}")
        } else {
            println!("{horizontal_rule}")
        }
    }
}
