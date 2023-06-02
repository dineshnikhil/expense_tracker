def orange_text(text):
    # ANSI escape sequence to set the text color to orange
    orange_color_code = '\033[38;5;208m'
    
    # ANSI escape sequence to reset the text color
    reset_color_code = '\033[0m'
    
    orange_text = f"{orange_color_code}{text}{reset_color_code}"
    return orange_text