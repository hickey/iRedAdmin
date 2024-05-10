---
created: 2024-05-10T08:16:01 (UTC -04:00)
tags: []
source: https://docs.iredmail.org/iredadmin-pro.restful.api.html#domain
author:
---

# iRedAdmin-Pro: RESTful API

> ## Excerpt
> Check out the lightweight on-premises email archiving software developed by iRedMail team: Spider Email Archiver.

---
Check out the lightweight on-premises email archiving software developed by iRedMail team: [Spider Email Archiver](https://spiderd.io/).

-   [iRedAdmin-Pro: RESTful API](https://docs.iredmail.org/iredadmin-pro.restful.api.html#iredadmin-pro-restful-api)
    -   [Summary](https://docs.iredmail.org/iredadmin-pro.restful.api.html#summary)
    -   [Enable RESTful API](https://docs.iredmail.org/iredadmin-pro.restful.api.html#enable-restful-api)
    -   [Sample code to interact with iRedAdmin-Pro RESTful API](https://docs.iredmail.org/iredadmin-pro.restful.api.html#sample-code-to-interact-with-iredadmin-pro-restful-api)
    -   [APIs](https://docs.iredmail.org/iredadmin-pro.restful.api.html#apis)
        -   [Login](https://docs.iredmail.org/iredadmin-pro.restful.api.html#login)
        -   [Domain](https://docs.iredmail.org/iredadmin-pro.restful.api.html#domain)
        -   [Domain Admin](https://docs.iredmail.org/iredadmin-pro.restful.api.html#domain-admin)
        -   [Mail User](https://docs.iredmail.org/iredadmin-pro.restful.api.html#mail-user)
        -   [Subscribable Mailing List](https://docs.iredmail.org/iredadmin-pro.restful.api.html#subscribable-mailing-list)
        -   [Mailing List (Unsubscribable)](https://docs.iredmail.org/iredadmin-pro.restful.api.html#mailing-list-unsubscribable)
        -   [Mail Alias](https://docs.iredmail.org/iredadmin-pro.restful.api.html#mail-alias)
        -   [Spam Policy](https://docs.iredmail.org/iredadmin-pro.restful.api.html#spam-policy)
        -   [Throttling](https://docs.iredmail.org/iredadmin-pro.restful.api.html#throttling)
        -   [Whitelisting and Blacklisting](https://docs.iredmail.org/iredadmin-pro.restful.api.html#whitelisting-and-blacklisting)
        -   [Greylisting](https://docs.iredmail.org/iredadmin-pro.restful.api.html#greylisting)
        -   [Export Accounts](https://docs.iredmail.org/iredadmin-pro.restful.api.html#export-accounts)
            -   [LDIF (LDAP backend only)](https://docs.iredmail.org/iredadmin-pro.restful.api.html#ldif-ldap-backend-only)

> -   This document is applicable to `iRedAdmin-Pro-SQL-4.2`, `4.3` and `iRedAdmin-Pro-LDAP-4.3`, `4.4`. If you're running an old release, please upgrade iRedAdmin-Pro to the latest release, or check [document for old releases](https://docs.iredmail.org/iredadmin-pro.releases.html).
> -   If you need an API which has not yet been implemented, don't hesitate to [contact us](https://www.iredmail.org/contact.html).
> -   [Release Notes of all iRedAdmin-Pro releases](https://docs.iredmail.org/iredadmin-pro.releases.html).

## Summary

iRedAdmin-Pro RESTful API will return message in JSON format.

-   If operation succeed:
    -   For http `POST`, `DELETE`, `PUT` methods, it returns JSON data: `{'_success': true}`.
    -   For http `GET` method, it returns JSON data: `{'_success': true, '_data': <program_output>}`.
-   If operation failed, it returns JSON data: `{'_success': false, '_msg': '<error_reason>'}`.

## Enable RESTful API

RESTful API is disabled by default, to enable it, please add setting below in iRedAdmin-Pro config file `settings.py`:

```
ENABLE_RESTFUL_API = True
```

Restarting `iredadmin` (if you're running Nginx) or Apache service is required after changed iRedAdmin config file.

iRedAdmin-Pro config file location

-   on RHEL/CentOS, it's `/opt/www/iredadmin/settings.py` (in recent iRedMail releases) or `/var/www/iredadmin/settings.py` (in old iRedMail releases).
-   on Debian/Ubuntu, it's `/opt/www/iredadmin/settings.py` (in recent iRedMail releases) or `/usr/share/apache2/iredadmin/settings.py` (in old iRedMail releases).
-   on FreeBSD, it's `/usr/local/www/iredadmin/settings.py`.
-   on OpenBSD, it's `/opt/www/iredadmin/settings.py` (in recent iRedMail releases) or `/var/www/iredadmin/settings.py` (in old iRedMail releases).

To restrict API access to few IP addresses, please login to iRedAdmin-Pro as global admin, then click menu `System -> Settings`, find option `RESTful API is accessible only from specified IP addresses or networks`, input the allowed IP addresses or networks.

## Sample code to interact with iRedAdmin-Pro RESTful API

-   [iRedAdmin-Pro RESTful API (interact with `curl`)](https://docs.iredmail.org/iredadmin-pro.restful.api.curl.html)
-   [iRedAdmin-Pro RESTful API (interact with Python)](https://docs.iredmail.org/iredadmin-pro.restful.api.python.html)

## APIs

Notes:

-   Parameter name with a `*` mark means the parameter is required, otherwise is optional.
-   replace `<domain>` in URL by the real domain name. e.g. `example.com`
-   replace `<mail>` in URL by the real email address. e.g. `user@domain.com`
-   replace `<number>` in URL by an integer number. e.g. `30`, `200`

### Login

`POST` `/api/login` `Parameters`

### Domain

`GET` `/api/domains` `Parameters`

`GET` `/api/domain/<domain>`

`POST` `/api/domain/<domain>` `Parameters`

`DELETE` `/api/domain/<domain>`

`DELETE` `/api/domain/<domain>/keep_mailbox_days/<number>`

`PUT` `/api/domain/<domain>` `Parameters`

`PUT` `/api/domain/admins/<domain>` `Parameters`

### Domain Admin

-   This is standalone domain admin account, not mail user with admin privileges.
-   Only global admin can access these APIs.

`GET` `/api/admin/<mail>` `Parameters`

`POST` `/api/admin/<mail>` `Parameters`

`DELETE` `/api/admin/<mail>`

`PUT` `/api/admin/<mail>` `Parameters`

`POST` `/api/verify_password/admin/<mail>` `Parameters`

### Mail User

`GET` `/api/user/<mail>` `Parameters`

`POST` `/api/user/<mail>` `Parameters`

`DELETE` `/api/user/<mail>`

`DELETE` `/api/user/<mail>/keep_mailbox_days/<number>`

`PUT` `/api/user/<mail>` `Parameters`

`POST` `/api/user/<mail>/change_email/<new_mail>`

`GET` `/api/users/<domain>` `Parameters`

`PUT` `/api/users/<domain>` `Parameters`

`POST` `/api/verify_password/user/<mail>` `Parameters`

### Subscribable Mailing List

-   Subscribable mailing list requires iRedMail-0.9.8 and later releases, it's implemented with [`mlmmj`](http://mlmmj.org/) mailing list manager.
-   It's available for both SQL and LDAP backends.

`GET` `/api/mls/<domain>` `Parameters`

`GET` `/api/ml/<mail>` `Parameters`

`POST` `/api/ml/<mail>` `Parameters`

`DELETE` `/api/ml/<mail>` `Parameters`

`PUT` `/api/ml/<mail>` `Parameters`

### Mailing List (Unsubscribable)

-   This unsubscribable mailing list is only available in **LDAP** backend.
-   It's recommended to use the Subscribable Mailing List instead, you're free to disable public subscribable.

`GET` `/api/maillist/<mail>`

`POST` `/api/maillist/<mail>` `Parameters`

`DELETE` `/api/maillist/<mail>` `Parameters`

`PUT` `/api/maillist/<mail>` `Parameters`

### Mail Alias

`GET` `/api/alias/<mail>`

`POST` `/api/alias/<mail>` `Parameters`

`DELETE` `/api/alias/<mail>`

`PUT` `/api/alias/<mail>` `Parameters`

`POST` `/api/alias/<mail>/change_email/<new_mail>`

`GET` `/api/aliases/<domain>` `Parameters`

### Spam Policy

`GET` `/api/spampolicy/global`

`GET` `/api/spampolicy/domain/<domain>`

`GET` `/api/spampolicy/user/<mail>`

`DELETE` `/api/spampolicy/global`

`DELETE` `/api/spampolicy/domain/<domain>`

`DELETE` `/api/spampolicy/user/<mail>`

`PUT` `/api/spampolicy/global` `Parameters`

`PUT` `/api/spampolicy/domain/<domain>` `Parameters`

`PUT` `/api/spampolicy/user/<mail>` `Parameters`

### Throttling

`GET` `/api/throttle/global/inbound`

`POST` `/api/throttle/global/inbound` `Parameters`

`GET` `/api/throttle/global/outbound`

`POST` `/api/throttle/global/outbound` `Parameters`

`GET` `/api/throttle/<domain>/inbound`

`POST` `/api/throttle/<domain>/inbound` `Parameters`

`GET` `/api/throttle/<domain>/outbound`

`POST` `/api/throttle/<domain>/outbound` `Parameters`

`GET` `/api/throttle/<mail>/inbound`

`POST` `/api/throttle/<mail>/inbound` `Parameters`

`GET` `/api/throttle/<mail>/outbound`

`POST` `/api/throttle/<mail>/outbound` `Parameters`

### Whitelisting and Blacklisting

Valid whitelisting and blacklisting addresses. **Invalid addresses will be discarded silently.**

| Address | Examples |
| --- | --- |
| Single IP Address | `192.168.2.10` |
| IP CIDR Network | `192.168.2.0/24`, `2620:0:2d0:200::7/128` |
| Single email address | `user@domain.ltd` |
| Entire email domain | `@domain.ltd` |
| Entire email domain and all its sub-domains | `@.domain.ltd` |
| Catch-all address | `@.` |

`GET` `/api/wblist/inbound/whitelist/global`

`GET` `/api/wblist/inbound/blacklist/global`

`GET` `/api/wblist/outbound/whitelist/global`

`GET` `/api/wblist/outbound/blacklist/global`

`GET` `/api/wblist/inbound/whitelist/<domain>`

`GET` `/api/wblist/inbound/blacklist/<domain>`

`GET` `/api/wblist/outbound/whitelist/<domain>`

`GET` `/api/wblist/outbound/blacklist/<domain>`

`GET` `/api/wblist/inbound/whitelist/<mail>`

`GET` `/api/wblist/inbound/blacklist/<mail>`

`GET` `/api/wblist/outbound/whitelist/<mail>`

`GET` `/api/wblist/outbound/blacklist/<mail>`

`POST` `/api/wblist/inbound/whitelist/global` `Parameters`

`POST` `/api/wblist/inbound/blacklist/global` `Parameters`

`POST` `/api/wblist/outbound/whitelist/global` `Parameters`

`POST` `/api/wblist/outbound/blacklist/global` `Parameters`

`POST` `/api/wblist/inbound/whitelist/<domain>` `Parameters`

`POST` `/api/wblist/inbound/blacklist/<domain>` `Parameters`

`POST` `/api/wblist/outbound/whitelist/<domain>` `Parameters`

`POST` `/api/wblist/outbound/blacklist/<domain>` `Parameters`

`POST` `/api/wblist/inbound/whitelist/<mail>` `Parameters`

`POST` `/api/wblist/inbound/blacklist/<mail>` `Parameters`

`POST` `/api/wblist/outbound/whitelist/<mail>` `Parameters`

`POST` `/api/wblist/outbound/blacklist/<mail>` `Parameters`

`PUT` `/api/wblist/inbound/whitelist/global` `Parameters`

`PUT` `/api/wblist/inbound/blacklist/global` `Parameters`

`PUT` `/api/wblist/outbound/whitelist/global` `Parameters`

`PUT` `/api/wblist/outbound/blacklist/global` `Parameters`

`PUT` `/api/wblist/inbound/whitelist/<domain>` `Parameters`

`PUT` `/api/wblist/inbound/blacklist/<domain>` `Parameters`

`PUT` `/api/wblist/outbound/whitelist/<domain>` `Parameters`

`PUT` `/api/wblist/outbound/blacklist/<domain>` `Parameters`

`PUT` `/api/wblist/inbound/whitelist/<mail>` `Parameters`

`PUT` `/api/wblist/inbound/blacklist/<mail>` `Parameters`

`PUT` `/api/wblist/outbound/whitelist/<mail>` `Parameters`

`PUT` `/api/wblist/outbound/blacklist/<mail>` `Parameters`

`DELETE` `/api/wblist/inbound/whitelist/global`

`DELETE` `/api/wblist/inbound/blacklist/global`

`DELETE` `/api/wblist/outbound/whitelist/global`

`DELETE` `/api/wblist/outbound/blacklist/global`

`DELETE` `/api/wblist/inbound/whitelist/<domain>`

`DELETE` `/api/wblist/inbound/blacklist/<domain>`

`DELETE` `/api/wblist/outbound/whitelist/<domain>`

`DELETE` `/api/wblist/outbound/blacklist/<domain>`

`DELETE` `/api/wblist/inbound/whitelist/<mail>`

`DELETE` `/api/wblist/inbound/blacklist/<mail>`

`DELETE` `/api/wblist/outbound/whitelist/<mail>`

`DELETE` `/api/wblist/outbound/blacklist/<mail>`

### Greylisting

`GET` `/api/greylisting/all`

`GET` `/api/greylisting/global`

`GET` `/api/greylisting/<domain>`

`GET` `/api/greylisting/<mail>`

`POST` `/api/greylisting/global` `Parameters`

`POST` `/api/greylisting/<domain>` `Parameters`

`POST` `/api/greylisting/<mail>` `Parameters`

`DELETE` `/api/greylisting/global`

`DELETE` `/api/greylisting/<domain>`

`DELETE` `/api/greylisting/<mail>`

`GET` `/api/greylisting/global/whitelists`

`GET` `/api/greylisting/<domain>/whitelists`

`GET` `/api/greylisting/<mail>/whitelists`

`POST` `/api/greylisting/global/whitelists` `Parameters`

`POST` `/api/greylisting/<domain>/whitelists` `Parameters`

`POST` `/api/greylisting/<mail>/whitelists` `Parameters`

`POST` `/api/greylisting/whitelist_spf_domains` `Parameters`

### Export Accounts

#### LDIF (LDAP backend only)

`GET` `/api/ldif/domain/<domain>`

`GET` `/api/ldif/catchall/<domain>`

`GET` `/api/ldif/admin/<mail>`

`GET` `/api/ldif/user/<mail>`

`GET` `/api/ldif/maillist/<mail>`

`GET` `/api/ldif/alias/<mail>`
