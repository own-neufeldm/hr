use std::cmp;

pub fn get_horizontal_rule(title: String, length: u32, border: String, filler: String) -> String {
    let reversed_border = border.chars().rev().collect::<String>();
    if title.is_empty() {
        let filler_length = cmp::max(length - 2 - 2 * (border.len() as u32), 1);
        let filler = filler.repeat(filler_length as usize);
        return format!("{border} {filler} {reversed_border}");
    }

    let filler_length = cmp::max(
        length - 4 - (title.len() as u32) - 2 * (border.len() as u32),
        2,
    );
    let side_filler_length = u32::div_ceil(filler_length, 2);
    let side_filler = filler.repeat(side_filler_length as usize);
    return format!("{border} {side_filler} {title} {side_filler} {reversed_border}");
}
