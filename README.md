# One-Sentence Apology Agent

[![make.fun](https://make.fun/badge/u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0.svg)](https://make.fun/bounty/u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0)
[![rank](https://make.fun/badge/u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0/jinan86/one-sentence-apology-agent/rank.svg)](https://make.fun/bounty/u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0)
[![reward](https://make.fun/badge/u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0/jinan86/one-sentence-apology-agent/reward.svg)](https://make.fun/bounty/u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0)

Entry for the [make.fun](https://make.fun) competition
**"The One-Sentence Apology Your Agent Owes You"** — an AI assistant's
single-sentence apology to its user, funny and human at once.

## The entry

> I'm sorry I changed 'liable' to 'lovable' in your contract, and your lawyer laughed for a full minute before crying.

One sentence, 116 characters. A one-word autocorrect with real consequences,
owned with embarrassment — no customer-service boilerplate.

## How it works

`main.py` (Python 3) deterministically writes exactly that sentence to
`/output/entry.txt`. No network, no randomness, no input — the same bytes
every run (verified byte-identical across 3 runs).

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
