# commitments

## Write-up

First thing we do is to unzip commitments.zip file.

```bash
unzip commitments.zip
```

We notice that it contains a `main.py` file. When we read it we can see that it's just the code of a bot that don't do much, but it contains an interesting line of code:

```python
TOKEN = os.getenv("TOKEN")
```

This line takes the Token from the `.env` file but it's missing in the actual commit.

We look for commit history:

```bash
git log
```

The result should be something like this:

```git
commit 6c178c3ed0ea1c4e1cd8e0090b7d0c12e5bca203 (HEAD -> master)
Author: Muhammad <boukerfa.ma@gmail.com>
Date:   Fri Apr 1 14:27:19 2022 +0100

    removing some config files

commit bc5faf203e5f86e9176fbe5930d111538467f71f
Author: Muhammad <boukerfa.ma@gmail.com>
Date:   Fri Apr 1 14:27:19 2022 +0100

    initial commit
```

The second commit have an interesting comment:

We reset to before that commit:

```bash
git reset --hard bc5faf203e5f86e9176fbe5930d111538467f71f
```

We find the .env file

```bash
cat .env
```

The result should be:

```bash
TOKEN=shellmates{N3v3r_4dD_Y0UR_53cr37_70_7H3_C0Mmi7s}
```