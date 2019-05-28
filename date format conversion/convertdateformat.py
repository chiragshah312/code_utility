from datetime import datetime

## Possible input and output formats
# ddmmyyyy
# ddmmmyyyy
# ddyyyymm
# ddyyyymmm
# mmmddyyyy
# mmddyyyy
# mmyyyydd
# mmmyyyydd
# yyyymmdd
# yyyymmmdd
# yyyyddmm
# yyyymmmdd
# SD (Standard Datetime)

## Possible separators for input and output
# comma(,), dot(.), colon(:), semicolon(;), space( ), pipe(|), slash(/) or any other valid character

formats = {"ddmmyyyy": "%d %m %Y", "ddmmmyyyy": "%d %b %Y", "ddyyyymm": "%d %Y %m",
"ddyyyymmm": "%d %Y %b", "mmmddyyyy": "%b %d %Y", "mmddyyyy": "%m %d %Y", "mmyyyydd": "%m %Y %d",
"mmmyyyydd": "%b %Y %d", "yyyymmdd": "%Y %m %d", "yyyymmmdd": "%Y %b %d", "yyyyddmm": "%Y %d %m",
"yyyymmmdd": "%Y %b %d", "SD": "%Y %m %d"}

def get_date_in_format(input_format, output_format, input_date, input_date_separator, output_date_separator):
    if input_format != "SD":
        output = datetime.strptime(input_date, formats[input_format].replace(" ", input_date_separator))
    else:
        output = input_date
    if output_format == "SD":
        return output
    return output.strftime(formats[output_format].replace(" ", output_date_separator))
    
    # return output.replace(input_date_separator, output_date_separator)[:10]
    

## How to use it?
a = datetime.now()
print(get_date_in_format("SD", "yyyymmmdd", a, "-", "+"))
