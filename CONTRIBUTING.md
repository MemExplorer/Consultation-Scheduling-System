# Contributing

See [Table of contents](#tables) for references.


## Table of content <a name="tables"></a>
- [1. Development](#development)
  - [1.1 File System](#file-system)
  - [1.2 Requirements](#requirements)
  - [1.3 Development Flow](#development)
  - [1.4 Timeline](#time)
- [2. Testing](##testing)
  - [2.1 Debugging](#debug)
  - [2.1 Linting](#lnit)
- [3. Documentation](#doc)
  
# File System
Overview of the project file system, as of 06/09/2023.

![File System](./resources/images/contributing_filesystem.png)

## File system heirarchies:

* `auth` : Contains all `.py files` required for the project database authentications.

* `models` : Contains all `.py files` required for database modelling.

* `resources` : Contains all sub-folder for `audio, fonts, icons, images`.

* `venv` : python virtual environment folder. Do not modify.
  
* `run.py` : Project runner file only. Reference to the main.py view.
* `markdowns` : Related markdowns or `.md` files like `Contributing.md` and `README.md`.

# Requirements
You should have these applications and tools to develop, test, and debug the project.

- XAMPP 8.2.4
- IDE/Editor
- MySQL
- Python 3.11.3
# Development
### Here is the general concept of the project implementation:

```mermaid
flowchart TB
A[Workflow] --> |Developers| B[User Interface]
A[Workflow] --> |Database Admin| C[Database]
B --> |Developer A| BA[Teacher Views]
B --> |Developer B| BB[Student Views]
C --> |Database Admins| CA[Database Relation]
CA --> |Database Admins| CB[Database Implementation]
BA --> |Teacher-Based Functions| D[System Implementation]
BB --> |Student-Based Functions| D[System Implementation]
D --> E[Testing]
CB --> E[Testing]
E --> F[Documentation]
F --> G
E --> G[Production]
```

> <span style="color:orange">NOTICE: </span> There are no detailed representations of the UI workflow, database guidelines, and their connections

## Sequence Diagram of Account Login/Signup

![Account Starting Sequence](./resources/images/contributing_diagram.png)

## Timeline Constraints
The project has a short timeline for development and testing that is why we must meet the timeline deadline as soon as possible. Here is a gantt chart representation based on [Project Paper - Gantt Chart](https://1drv.ms/w/s!AtjIPcaFwE3CgV4OqJ_29lvdOtQE?e=jBvQEl):

```mermaid
gantt
    title System Timeline
    dateFormat  YYYY-MM-DD
    section User Interface
    Development           :a1, 2023-06-05, 12d
    section Database
    Database Creation      :2023-06-10  , 9d
    section Testing
    Testing Phase      :2023-06-15  , 12d
    section Presentation
    Presentation      :2023-06-20  , 9d
```

## Testing 
### Debugging
### Testing Environment


## Documentation
In progress