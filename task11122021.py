def format_tel(tel):
    return f'{tel[0:4]}({tel[4:6]) {tel[6:9]}}-{tel[9:11]}-{tel[11:13]}'
    
def format_tel(tel):
    return '{}{}{}{}({}{}) {}{}{}-{}-{}'.format(*list(tel))

print(format_tel('+998996116661'))