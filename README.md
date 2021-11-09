<!-- omit in toc -->
# <em>servidora</em>

> a telegram bot for automating virtual machine provisioning.

This is part of my **serveEthiopia project**, a project aimed at providing resources for fellow Ethiopians to help them in their IT career. You can

```sh
git clone https://github.com/muse-sisay/serveET
```

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Installation //](#installation-)
- [Up and Running](#up-and-running)
  - [Getting API token for your bot](#getting-api-token-for-your-bot)
  - [Setting up Proxmox Credentials](#setting-up-proxmox-credentials)
  - [Run bot](#run-bot)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Installation //

<em>servidora</em> is tested to work on `Python 3.9` and above. Depending on your machine you might have to use python3.9 instead.

For my python projects I always like to have a python virtual environments per project to keep my dependencies separate. Therefore, it is recommended that you [setup your python virtual environment](https://realpython.com/python-virtual-environments-a-primer/) and then you can proceed to activate it accordingly. If you're using Python's standard [`venv`](https://docs.python.org/3/library/venv.html):

```console
python3 -m venv ~/venv/<venv_name>
```

If you are using fish shell the file is `activate.fish`

```console
~/venv/<venv_name>/bin/activate(.fish) # to activate
```

Once you activate your virtual environment, you can update pip via `pip install --upgrade pip`.

The required python packages are listed in [requirements.txt](requirements.txt). To install those packages,

1. first, install [pip-tools](https://github.com/jazzband/pip-tools): `pip install pip-tools`,
2. then run `pip-compile requirements.in`,
3. followed by `pip-sync`.

Rename `config.yml.sample` to `config.yml` and update the values accordingly.

```sh
mv servidora/config.yml.sample to servidora/config.yml
```

## Up and Running

### Getting API token for your bot

Start a conversation with [Bot Father](https://t.me/BotFather). Follow through the process of creating a bot. Then save you API token in a safe place, preferably in `servidora/config.yml`.

### Setting up Proxmox Credentials

Select _Data Center_ in your proxmox server and create a new user. Give the user an appropriate name that describes its function. After that go ahead and create an API token for the user you just created. Copy the  secret key to `servidora/config.yml`

Create a **Role** with the following privileges.

```text
VM.Audit, VM.Monitor, Datastore.AllocateSpace, VM.Clone, VM.Allocate, VM.PowerMgm
```

Under permission tab click `API Token Permission` and add `/vms` and `/storage` entries.

```text
path [/vms | /storage]
API Token  <one you created>
Role <the one you created>
```

### Run bot

```console
python3 servidora/main.py
```

OR, much simpler

```console
invoke run
```
