- Sql injection

 - tamper data http://0xd0m7.blogspot.jp/2016/02/understanding-tamper-option-in-sqlmap-ii.html
    To test mysql, you can use all tamper below:
    tamper=between,bluecoat,charencode,charunicodeencode,concat2concatws,equaltolike,greatest,halfversionedmorekeywords,ifnull2ifisnull,modsecurityversioned,modsecurityzeroversioned,multiplespaces,nonrecursivereplacement,percentage,randomcase,securesphere,space2comment,space2hash,space2morehash,space2mysqldash,space2plus,space2randomblank,unionalltounion,unmagicquotes,versionedkeywords,versionedmorekeywords,xforwardedfor

    To test mssql, you can use all tamper below
    tamper=between,charencode,charunicodeencode,equaltolike,greatest,multiplespaces,nonrecursivereplacement,percentage,randomcase,securesphere,sp_password,space2comment,space2dash,space2mssqlblank,space2mysqldash,space2plus,space2randomblank,unionalltounion,unmagicquotes

    Below is tamper list that support both mssql and mysql

    tamper=apostrophemask,apostrophenullencode,base64encode,between,chardoubleencode,charencode,charunicodeencode,equaltolike,greatest,ifnull2ifisnull,multiplespaces,nonrecursivereplacement,percentage,randomcase,securesphere,space2comment,space2plus,space2randomblank,unionalltounion,unmagicquotes






- XSS
  - using post-method get-local-html
    https://github.com/tothi/ctfs/tree/master/rc3-ctf-2016/web/cachet-500





- HTTP header injection
  - Using return code "%0d%0a" in URL query where is related to LOCATION header.




- X-forwarded-forwarded


- flask injection and python escape from sandbox
    https://hackerone.com/reports/125980
    http://fadec0d3.blogspot.jp/2017/02/blog-post.html
       {{ ''.__class__.__mro__[2].__subclasses__() }}
    https://hexplo.it/escaping-the-csawctf-python-sandbox/
      __mro__ : Method Resolution Order addribute.
    https://github.com/alecthomas/flask_injector -> [useful??]



- fix git repository
   http://rawsec.ml/en/BSides-San-Francisco-CTF-2017-write-ups/#1-Hackers-Misc
     - use gittools :$ ./gitdumper.sh http://theyear2000.ctf.bsidessf.net/.git/ repo
     - git log -p
     - git reflogs
     - git reset HEAD@{2}