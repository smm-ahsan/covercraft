#!/usr/bin/env python3
"""CoverCraft - generate a complete, copy-ready job cover letter.

Usage:
    python3 covercraft.py --name "Sara Ahmed" --role "Office Administrator" \
        --company "Harbour Hotels" \
        --skills "invoicing, payroll support, customer service" --years 3

Standard library only.
"""

import argparse
import sys


def join_skills(skills):
    """Join up to the first three skills as 'X, Y and Z'."""
    top = skills[:3]
    if len(top) == 1:
        return top[0]
    if len(top) == 2:
        return f"{top[0]} and {top[1]}"
    return f"{top[0]}, {top[1]} and {top[2]}"


def build_letter(name, role, company, skills, years, tone):
    lines = []
    lines.append("Dear Hiring Manager,")
    lines.append("")

    # Paragraph 1: the application itself.
    if tone == "warm":
        p1 = (f"I was delighted to see the {role} position open at {company}, "
              f"and I would love to apply.")
    else:
        p1 = (f"I am writing to apply for the {role} position at {company}.")
    if years is not None:
        p1 += (f" With {years} years of experience behind me, I am confident "
               f"I can contribute from day one.")
    else:
        if tone == "warm":
            p1 += " I am confident I can contribute from day one."
        else:
            p1 += " I believe I would be a strong addition to your team."
    lines.append(p1)
    lines.append("")

    # Paragraph 2: skills, or general strengths when none are given.
    if skills:
        joined = join_skills(skills)
        if tone == "warm":
            p2 = (f"My background includes {joined}, and I genuinely enjoy "
                  f"putting those skills to work for a team. I take pride in "
                  f"doing careful, dependable work and in helping colleagues "
                  f"and customers alike.")
        else:
            p2 = (f"My background includes {joined}. Across my career I have "
                  f"built a reputation for accuracy, reliability and a calm, "
                  f"professional approach, even when deadlines are tight.")
    else:
        if tone == "warm":
            p2 = ("People who have worked with me know me as reliable, quick "
                  "to learn and happy to take ownership of whatever needs "
                  "doing. I show up, I follow through, and I care about "
                  "getting the details right.")
        else:
            p2 = ("I am known for being reliable, learning fast and taking "
                  "ownership of my work. I follow tasks through to "
                  "completion, communicate clearly and hold myself to a high "
                  "standard without needing close supervision.")
    lines.append(p2)
    lines.append("")

    # Paragraph 3: why this company, plus a polite interview invitation.
    if tone == "warm":
        p3 = (f"{company} is exactly the kind of place I would love to be "
              f"part of, and the {role} role sounds like a great fit for what "
              f"I do best. I would really enjoy the chance to meet you and "
              f"talk about how I could help, so please feel free to invite "
              f"me for an interview at any time that suits you.")
    else:
        p3 = (f"I have followed {company} with interest, and I would be "
              f"proud to bring my experience to your team as your next "
              f"{role}. I would welcome the opportunity to discuss my "
              f"application in an interview, and I am available at your "
              f"convenience.")
    lines.append(p3)
    lines.append("")

    lines.append("Warm regards," if tone == "warm" else "Kind regards,")
    lines.append(name)
    return "\n".join(lines)


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Generate a complete, copy-ready job cover letter.")
    parser.add_argument("--name", required=True, help="Your full name.")
    parser.add_argument("--role", required=True, help="The job title.")
    parser.add_argument("--company", required=True, help="The company name.")
    parser.add_argument("--skills", default=None,
                        help="Comma separated skills, e.g. 'invoicing, "
                             "payroll support, customer service'.")
    parser.add_argument("--years", type=int, default=None,
                        help="Years of experience (optional).")
    parser.add_argument("--tone", choices=["professional", "warm"],
                        default="professional", help="Letter tone.")
    args = parser.parse_args(argv)

    skills = []
    if args.skills:
        skills = [s.strip() for s in args.skills.split(",") if s.strip()]

    print(build_letter(args.name, args.role, args.company, skills,
                       args.years, args.tone))
    return 0


if __name__ == "__main__":
    sys.exit(main())
