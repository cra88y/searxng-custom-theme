# Simply Nord - a minimalist theme for Searxng
Supports dark, light, and OLED black modes.

- UI fixes and reworks for:
  - mobile layout issues (like all horizontal scrolling bugs!)
  - autocomplete behavior
  - suggestions for search
  - answer/info boxes
  - results view
  - image view
  - video view
  - news view
Note: Some features may be hidden or moved or changed

  
Simple to use by downloading and adding the following (2) binds in your Searxng docker compose yml:
```
services:
  searxng:
    volumes:
      - /local/path/to/searxng-custom-theme/crabx:/usr/local/searxng/searx/templates/simple
      - /local/path/to/searxng-custom-theme/crabx-static/css:/usr/local/searxng/searx/static/themes/simple/css
```
