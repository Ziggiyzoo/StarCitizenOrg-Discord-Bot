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

### Running

1. Initialise the Poetry environment by executing the following Poetry command:

    ```shell
    export TOKEN=<DISCORD_API_TOKEN>

    poetry install
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

### Building

//ToDo

### Running

1. Ensure Docker or Podman is installed.
2. Download your desired version of the `ziggiyzoo/brvns-discord-bot` image:
   
   ```shell
   # With Docker
   docker pull ghcr.io/ziggiyzoo/brvns-discord-bot:<tag>
   
   # With Podman
   podman pull ghcr.io/ziggiyzoo/brvns-discord-bot:<tag>
   ```

3. Run the downloaded image by executing the following command:

   ```shell
   # With Docker
   docker run --detach \
      --env TOKEN=<DISCORD_API_TOKEN> \
      ghcr.io/ziggiyzoo/brvns-discord-bot:<tag>

   # With Podman
   docker run --detach \
      --env TOKEN=<DISCORD_API_TOKEN> \
      ghcr.io/ziggiyzoo/brvns-discord-bot:<tag>
   ```

</details>

## Reference Libraries

This is an unordered list of third-party libraries that helped to make this application possible:

- [Python Discord](https://pypi.org/project/python-discord/)
