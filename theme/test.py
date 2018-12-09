import click

colors = [
    'black',
    'red',
    'green',
    'yellow',
    'blue',
    'magenta',
    'cyan',
    'white',
    'bright_black',
    'bright_red',
    'bright_green',
    'bright_yellow',
    'bright_blue',
    'bright_magenta',
    'bright_cyan',
    'bright_white'
]

bases = [
    'base00',
    'base01',
    'base02',
    'base03',
    'base04',
    'base05',
    'base06',
    'base07',
    'base08',
    'base09',
    'base0A',
    'base0B',
    'base0C',
    'base0D',
    'base0E',
    'base0F',
]

print(click.style('base00', fg='black'), click.style('        ', bg='black'))
print(click.style('base01', fg='bright_green'), click.style('        ', bg='bright_green'))
print(click.style('base02', fg='bright_yellow'), click.style('        ', bg='bright_yellow'))
print(click.style('base03', fg='bright_black'), click.style('        ', bg='bright_black'))
print(click.style('base04', fg='bright_blue'), click.style('        ', bg='bright_blue'))
print(click.style('base05', fg='white'), click.style('        ', bg='white'))
print(click.style('base06', fg='bright_magenta'), click.style('        ', bg='bright_magenta'))
print(click.style('base07', fg='bright_white'), click.style('        ', bg='bright_white'))
print(click.style('base08', fg='red'), click.style('        ', bg='red'))
print(click.style('base09', fg='bright_red'), click.style('        ', bg='bright_red'))
print(click.style('base0A', fg='yellow'), click.style('        ', bg='yellow'))
print(click.style('base0B', fg='green'), click.style('        ', bg='green'))
print(click.style('base0C', fg='cyan'), click.style('        ', bg='cyan'))
print(click.style('base0D', fg='blue'), click.style('        ', bg='blue'))
print(click.style('base0E', fg='magenta'), click.style('        ', bg='magenta'))
print(click.style('base0F', fg='bright_cyan'), click.style('        ', bg='bright_cyan'))

