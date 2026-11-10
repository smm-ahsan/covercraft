# Examples

Real output from CoverCraft, captured from actual runs.

## Professional tone, with skills and experience

Command:

```bash
python3 covercraft.py --name "Sara Ahmed" --role "Office Administrator" --company "Harbour Hotels" --skills "invoicing, payroll support, customer service" --years 3
```

Output:

```
Dear Hiring Manager,

I am writing to apply for the Office Administrator position at Harbour Hotels. With 3 years of experience behind me, I am confident I can contribute from day one.

My background includes invoicing, payroll support and customer service. Across my career I have built a reputation for accuracy, reliability and a calm, professional approach, even when deadlines are tight.

I have followed Harbour Hotels with interest, and I would be proud to bring my experience to your team as your next Office Administrator. I would welcome the opportunity to discuss my application in an interview, and I am available at your convenience.

Kind regards,
Sara Ahmed
```

## Warm tone, no skills listed

Command:

```bash
python3 covercraft.py --name "Tom Reed" --role "Barista" --company "Corner Cafe" --tone warm
```

Output:

```
Dear Hiring Manager,

I was delighted to see the Barista position open at Corner Cafe, and I would love to apply. I am confident I can contribute from day one.

People who have worked with me know me as reliable, quick to learn and happy to take ownership of whatever needs doing. I show up, I follow through, and I care about getting the details right.

Corner Cafe is exactly the kind of place I would love to be part of, and the Barista role sounds like a great fit for what I do best. I would really enjoy the chance to meet you and talk about how I could help, so please feel free to invite me for an interview at any time that suits you.

Warm regards,
Tom Reed
```
