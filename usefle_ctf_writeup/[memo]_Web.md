- Sql injection






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