# Contributing

See [Table of contents](#tables) for references.


## Table of content <a name="tables"></a>
- [1. Development](#development)
  - [1.1 Requirements](#requirements)
  - [1.2 Development Flow](#development)
  - [1.3 Timeline](#time)
- [2. Testing](##testing)
  - [2.1 Debugging](#debug)
  - [2.1 Linting](#lnit)
- [3. Documentation](#doc)

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

### Flowchart visualization of the **`account login`** implementation:

```mermaid
flowchart TB
A([Start]) --> |Users| B[Prompt User Input]
B --> |Input| C{Validator}
C --> |Query Username| D[(Database)]
D --> DA[/User Details/]
DA --> C
C --> CA{isValid?}
CA --> |No| B
CA --> |Yes| E{View Type?}
E --> |Student| F[Student View]
E --> |Teacher| FA[Teacher View]
F --> G([End])
FA --> G
```

### Representational diagram of signing up a user:

```mermaid
flowchart TB
A([Start]) --> |New User| B[Prompt Require Fields]
B --> |Input| C{Validator}
C --> |Query Username| D[(Database)]
D --> C
C --> CA{isNameValid}
CA --> |No| B
CA --> |Yes| CB{arePasswordsMatched}
CB --> |No| B
CB --> |Yes| CC[Other Field Entries]
CC --> CD[Encrypt User Details]
CD --> |Insert Data| D
CD --> E[Display Login View]
E --> F([End])
```


> <span style="color:orange">NOTICE: </span> There are no detailed representations of the UI workflow, database guidelines, and their connections yet.

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