# static-site-generator
This is a guided project from Boot.dev

https://www.boot.dev/courses/build-static-site-generator-python

## Architecture
```mermaid
flowchart TD
    subgraph Inputs
        MD["Markdown Files<br>(/content)"]
        TPL["template.html"]
        STATIC["Static Assets<br>(images, css)"]
    end

    subgraph SSG["Static Site Generator (src/)"]
        PARSER["Parse Markdown Blocks"]
        NODES["Convert to HTMLNode Tree"]
        RENDER["Render Full HTML<br>(to_html + inject template)"]

        PARSER --> NODES --> RENDER
    end

    subgraph Output
        PUB["/public Directory<br>(HTML & static assets)"]
    end

    subgraph Serving
        SERVER["HTTP Server<br>(localhost:8888)"]
        BROWSER["Web Browser"]
    end

    MD --> PARSER
    TPL --> RENDER
    STATIC -->|Copy assets| PUB
    RENDER -->|Write HTML| PUB
    PUB --> SERVER
    SERVER --> BROWSER