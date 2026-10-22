# Escape Room · 🟢 CR 1

**Challenge Rating:** 🟢 CR 1 · Tavern Quest · **Platform:** Linux, macOS or WSL · **Time:** 15–45 minutes

> You're locked in a small room. The flag is split into pieces scattered
> around it. Nothing here is what it seems at first glance.

A first room for people who are new to the command line or to CTFs. If you
can `ls`, `cd` and `cat`, you have everything you need to start; the room
teaches the rest by making you notice things.

## Play

```sh
tar -tvzf escape-room.tar.gz   # look before you unpack
tar -xzf escape-room.tar.gz
cd escape-room
cat README.txt
```

## Check your flag

```
SHA-256: 6c29892c249967fa5797698574585523c83cda1a5c3d4590161a05b311b12bea
```

```sh
echo -n 'flag{your_answer_here}' | sha256sum
```

<sub>No walkthroughs here on purpose. Please keep solutions out of issues so
the next player gets their own "aha".</sub>
