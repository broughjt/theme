# Set

1. Get input from user
  - Theme name
2. Search for a color scheme that matches
  - Theme name
3. Read config at ~/.config/theme/config.yml
  - Get the path for a Recipient file
4. For every path in the config file, do:
  - Find matching regex
  - Get the Recipient Type (vim, kak, shell, term, etc.)
  - Look for that type in ~/colors/templates/
  - Compile the template with the color scheme
5. Inject the compiled template into each Recipient file
