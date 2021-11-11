# Authentication

Authentication vulnerabilities are one of the simpler ones. Yet, due to obvious reasons, they can have very serious impacts. Finding authentication bugs usually have a puzzle-solving nature to them. Authentication is the process of identifying the identity of a person, this is what sets the difference between *authentication* and *authorisation*. Authorisation is the process of checking whether a user has access to a resource and permitting or denying requests for that resource based on the user\'s permissions.

## Brute Force Protection

### Username enumeration

1.  Using Differences in response contents

    This method is **very** simple, you compare the responses of the web application when a valid username is sent to the response to an invalid username. If there are any *consistent* differences, you can enumerate usernames.

2.  Difference in response times

    Because web applications have to first hash the password and then compare the hashes, sometimes developers check whether the username is valid and then hash the password in order to save resources. However because hashing is a process that takes time, an attacker can send a very long password which takes a long time to hash. Since the server would only hash this password if the username is valid, the attacker can deduce whether a username exists or not by looking at the response time.

### Flawed Brute Force Protection

There are two ways that brute force protection can be implemented. THe system can lock a user\'s account after too many failed login attempts or the ip of the attacker can be blocked after a number of failed attempts.

1.  Bypassing IP Blocks

    The [X-Forwarded-For header](web_bypasses.org::*X-Forwarded-For header) trick can be used. Also, some applications reset the ip restrictions once somebody is logged-in from that account. Or, in some web applications, you can submit multiple credentials in a single request. Here is an example:

    ``` json
    {"username":"yeet","password":"pass"}
    ```

    ``` json
    {"username":"yeet","password":["pass","pass2"]}
    ```

2.  Bypassing Account Locks

    Sometimes, when an account is locked but the login details are correct, web applications return a different response then when the account is blocked and the credentials are wrong. This can be used to identify the credentials of an account even if it gets locked.

## 2FA (Two Factor Authentication)

2FA is often considered to be a very secure way for authentication since even if a user\'s credentials are compromised, an attacker can\'t login to the user\'s account. However, due to its advanced nature, it is often prone to vulnerabilities and should be tested with care.

-   Sometimes, when a user logs in and is redirected to a 2FA page, a session gets created anyways and a user can use the account without entering the 2FA Code. This is a very rare case however.
-   In some cases, the web applications uses a cookie that depends on the user\'s username in order to check whether the 2FA codes match instead of creating and using a session token. This can be exploited to brute-force a user\'s 2FA token only which can allow an attacker to access an account without knowing the credentials.
-   When websites fail to apply rate-limiting on 2FA systems, you can brute force 2FA codes. In cases where the application logs a user out after a number of failed retries, you can use [Macros](burpsuite.org::*Macros) in order to log back in.

## Password Change

Password change functionalities can be vulnerable to Host Header injections. By changing the `Host` header in forgot password requests, you can alter the url that the web applications refers to in its e-mail that it sends. This opens up the possibility for phishing attacks.

-   When changing the Host header breaks the application, if a middleware is being used you can instead send a `X-Forwarded-Host` header in your request which could have the same effect of changing the Host header without breaking the application.
-   Also, editing the port number in a Host header is sometimes useful as well. The ability to inject non-numeric parameters to the port number could potentially allow an attacker to execute Dangling HTML attacks or simply alter the url being visited by changing the URL to the form of `username:password@domain`
