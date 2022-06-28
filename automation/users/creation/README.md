#  User Creator

- [Please Read](#please-read)
- [Getting Started](#getting-started)
  * [Constants](#constants)
	+ [Authorization](#authorization)
	+ [Conn](#conn)
	+ [Cookie](#cookie)
  * [User List](#user-list)
  * [Main](#main)
	 + [Domain](#domain)
	 + [Default Groups](#default-roups)

## Please Read

Getting started with **User Creator** is straightforward. Please review this README before running the script in a production environment. We recommended testing this script on a [developer Okta instance](https://developer.okta.com/) before your production instance.

## Purpose

Okta does not have creation of users from an imported source. At the same time, this may be fine on a regular day. If you are required to create 100 or even 200 users with a set of default groups at a given time, you would have to either do it manually or rely on the Okta API. As of creating this script, I could not find any previously written scripts that did this for us; thus, this script was born.

## Getting Started

### Constants

Copy the `constants.py.default` template into the root project folder by running the following command in terminal `cp defaults/constants.py.default constants.py`. After you have made a copy of the default constats it is time for us to fill it out.


#### Authorization

The authorization, more commonly known as a token, can be obtained by reading the Okta [documentation](https://developer.okta.com/docs/guides/create-an-api-token/main/).

#### Conn

The conn or connection is the URL to your Okta instance. The script takes care of the ending.

`example-admin.okta.com` will be `example`.

#### Cookie

To get your SessionID cookie visit your Okta Admin dashboard `example-admin.okta.com` and follow the steps outlined [here](https://code.google.com/archive/p/procurement/wikis/LoginWithSessionID.wiki "here").


#### Example

```
authorization = "8nW4N2NHf7LNh7Vq"
conn = "example"
cookie = "mwR6VsxpGfmh5vu3"
```

#### User List

User lists with more than 150 persons have not been tested. Please report encountered issues via GitHub. Copy the `user_list.default.json` template into the root project folder by running the following command in terminal `cp defaults/user_list.default.json user_list.json`.

#### Example

```
[
  {
    "first_name": "Harry",
    "last_name": "Potter",
    "user_password": "AUy+z!{3J%YLJkGw",
    "custom_groups": [
       "00g3xw0000000000000",
       "00g3xw0000000000000"
    ]
  },
  {
    "first_name": "Hermione",
    "last_name": "Granger",
    "user_password": "bsj$(4ZD{4]{PTyU",
    "custom_groups": [
       "00g3xw0000000000000"
    ]
  },
  {
    "first_name": "Ronald",
    "last_name": "Weasley",
    "user_password": "97_/pW'Kp/-:Dqp+",
    "custom_groups": [

    ]
  }
]
```

Let us break this down.

```
  {
    "first_name": "Harry",
    "last_name": "Potter",
    "user_password": "AUy+z!{3J%YLJkGw",
    "custom_groups": [
       "00g3xw0000000000000",
       "00g3xw0000000000000"
    ]
  },
```

The user **Harry Potter** will be added to two custom user groups specified within the JSON file.

```
  {
    "first_name": "Hermione",
    "last_name": "Granger",
    "user_password": "bsj$(4ZD{4]{PTyU",
    "custom_groups": [
       "00g3xw0000000000000"
    ]
  },
```

The user **Hermione Granger**  will be added to one custom user group specified within the JSON file.

```
  {
    "first_name": "Ronald",
    "last_name": "Weasley",
    "user_password": "97_/pW'Kp/-:Dqp+",
    "custom_groups": [

    ]
  }
```
The user **Ronald Weasley** will not be added to custom user groups.

### Main

The last couple of changes must be done within the `main.py` file as these variables will rarely change for the long term.

#### Domain

We must update the domain found within the script by updating the following line `domain_name = "domain.com"`. E.g `domain_name = "google.com"`

#### Default Groups

Most organizations will have some default groups. This could be but not limited to groups such as Google Workspace, Slack, Jira and Confluence. We must update the default groups found within the script by updating the following line `default_groups = [""]`. E.g `default_groups = ["00g3xw0000000000000", "00g3xw0000000000000"]`

To find your GroupID, visit your desired Okta group. The URL ending will present you with the GroupID `https://example-admin.okta.com/admin/group/00g3xw0000000000000`


## References

* [Okta Developer](https://developer.okta.com/)
* [LoginWithSessionID](https://code.google.com/archive/p/procurement/wikis/LoginWithSessionID.wiki "LoginWithSessionID")