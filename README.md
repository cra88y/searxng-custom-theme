# searxng-custom-theme
a Nord color palette, minimalist, and UI tweaked "theme" for Searxng

- This is an ongoing UI mod prioritizing: a more compact and minimal ui inspired by the Nord theme.
- Not built with public instances in mind, home page info and logos are removed
- Includes UI fixes for mobile layout issues, autocomplete box, and moves suggested search results to a more accessible area. 
- Dark mode only
- Some features may be hidden or moved or changed
- May break after updates to other parts of the project
- Maybe a little hacky but building off the default theme was the easiest approach
  
Simple to use by downloading and adding the following (2) binds in your Searxng docker compose yml:
* also remove simple theme parameters from settings.yml (or set to auto)
```
services:
  searxng:
    volumes:
      - /local/path/to/searxng-custom-theme/crabx:/usr/local/searxng/searx/templates/simple
      - /local/path/to/searxng-custom-theme/crabx-static/css:/usr/local/searxng/searx/static/themes/simple/css
```
