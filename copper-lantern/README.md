# The Copper Lantern · 🟡 CR 5

**Challenge Rating:** 🟡 CR 5 · Dungeon Delve · **Platform:** Linux, macOS or WSL · **Time:** 45–90 minutes

> Vince has run The Copper Lantern for twenty-two years and has never once
> been locked out of the office computer. This morning he is. His password
> was changed overnight and the cash ledger is gone. He has dumped
> everything he could off the office PC into a folder and handed it to you:
> "Find out who did this. And get me back in."

A small-business incident response case. There are two objectives:

1. **Recover Vince's new password.** That's the flag.
2. **Work out who did it.** The obvious answer isn't always the right one.

You'll be reading the evidence like an analyst would. Patience and a good
eye matter more than knowing obscure tools.

## Play

```sh
tar -tvzf copper-lantern.tar.gz   # look before you unpack
tar -xzf copper-lantern.tar.gz
cd copper-lantern
cat BRIEFING.txt
```

**You'll need `openssl`** (1.1.1 or newer; any current Linux has it). On a
Mac, the built-in `openssl` is LibreSSL; recent versions should work, but if
yours rejects an option you need, install the real thing with
`brew install openssl` and use that.

## Check your answers

**The flag:**

```
SHA-256: c0d7f447506d864885fb2615c279f314d0e691cc2c0e22a767433fc62e5748c0
```

```sh
echo -n 'flag{your_answer_here}' | sha256sum
```

**The culprit:** the room contains a locked `CASE_CLOSED.enc`. The briefing
tells you how to open it once you've named the right person, and there's a
story waiting inside. With only four suspects you *could* just try them all,
but then you'd have read the ending without solving the case.

<sub>No walkthroughs here on purpose. Please keep solutions out of issues so
the next investigator gets their own "aha".</sub>
