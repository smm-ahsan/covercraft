# CoverCraft

A tiny command line tool that generates a complete, copy-ready job cover letter from a few details.

## Features

- Builds a full three-paragraph cover letter, not a fill-in-the-blanks template
- Weaves your skills naturally into the letter (the first three are named)
- Optional years of experience, mentioned in the opening paragraph
- Two tones: professional and warm
- Sensible letter even with no skills listed, using a general strengths paragraph
- No bracketed placeholders left behind — the output is ready to copy and send

## Requirements

- Python 3
- Standard library only, nothing to install

## Usage

With skills and experience:

```bash
python3 covercraft.py --name "Sara Ahmed" --role "Office Administrator" --company "Harbour Hotels" --skills "invoicing, payroll support, customer service" --years 3
```

Warm tone, minimal details:

```bash
python3 covercraft.py --name "Tom Reed" --role "Barista" --company "Corner Cafe" --tone warm
```

See `examples.md` for the real output of both commands.

## A quick note

Always personalise the letter before sending it. Add one specific detail
about the company, adjust a line so it sounds like you, and double check the
role title matches the advert. A generated letter is a strong first draft,
not a finished application.

## License

MIT — see `LICENSE`.
