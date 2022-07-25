# BRVNS Org Discord Bot

## Description

//ToDo

## Requirements

Specific requirements depend on the installation type. This project can be deployed both using Poetry for Python, or by
using the Dockerfiles in the repo.

| Method of Installation | Requirements                                                        |
|------------------------|---------------------------------------------------------------------|
| Python                 | 'Python >=3.8 <=3.10' AND 'Poetry'                                  |
| Docker/Podman          | 'Docker Engine and Client' OR 'Podman' (Optional: 'Docker-Compose') |

## Bot Installation

Follow the instructions according to your chosen installation method.

<details>
<summary>
   <b>Python</b>
</summary>

1. Initialise the Poetry environment by executing the following Poetry commands:

    ```shell
    poetry update && poetry install
    ```

2. Run the application by executing the following Poetry command:

    ```shell
    poetry run python main.py
    ```

</details>

<details>
<summary>
   <b>Docker</b>
</summary>

//ToDo

</details>

## Reference Libraries

This is an unordered list of third-party libraries that helped to make this application possible:

- [Python Discord](https://pypi.org/project/python-discord/)
