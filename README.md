# der-die-das

Basically a Python3 script that uses https://der-artikel.de/ to tell you a word's article. You just run `python3 der_die_das.py <word>` and you will get the article in sdout.

Examples:

```bash
$ python3 der_die_das.py tisch
der Tisch
$ python3 der_die_das.py lampe
die Lampe
$ python3 der_die_das.py buch
das Buch
$ python3 der_die_das.py zzz
Zzz not found :(
```

## For ease of use, install:

### MacOS

You just need to copy the python script to `/usr/local/bin` with the name you want the executable to have. In my case I decided to use `ddd`.

```bash
$ cp der_die_das.py /usr/local/bin ddd
```

You should now be able to run `ddd <word>` from everywhere and get the article of the desired word.
