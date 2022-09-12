
# datdif

Calculates and prints the difference between dates.
By default, dates must be in the format MM/DD/YYYY.  The month and day can be
either one or two digits.  The year must be four digits.
The string "today" can be entered for either date.

## Usage

- `datdif [options] <from_date> <to_date>` to show the difference 
- `datdif --list` to show the saved configuration preferences.

There are four properties that can be configured (persistently):

### From date

A default can be set with the `--from-date <arg>` option.  The possible values are:

- `--from-date=<date-string>` where `<date_string>` is in the chosen date format
- `--from-date=today` to always use today's date
- `--from-date-clear` to restore the original default

### To date

A default can be set with the `--to-date <arg>` option.  The possible values are:

- `--to-date=<date-string>` where `<date_string>` is in the chosen date format
- `--to-date=today` to always use today's date
- `--to-date-clear` to restore the original default

### Date format

The date format can be set to anything that `strftime` supports (see Date formats) below.
This option is set with the `--date-format <arg>` argument.  The possible values are:

- `--date-format="<format-string>""`
- `--date-format-clear`

### Output format

The date differences can be specified in terms of days, weeks, months, or years,
or any combination of these.  "Days" are always included.

- `--output-format=<D|W|M|Y|WY|WM|MY>` for the specified combination
- `--output-format-clear` to reset to just days

## References

- [Github repository](https://github.com/philhanna/datdif)
- [Date formats](https://strftime.org/)
