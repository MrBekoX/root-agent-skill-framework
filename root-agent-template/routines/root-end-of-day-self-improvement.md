# Routine: Root end-of-day self-improvement

- **Slug:** `root-end-of-day-self-improvement`
- **Owner:** Root Agent (the only routine Root owns; it concerns only Root itself)
- **Schedule:** daily, default 22:00 in the user's local time zone; set up on first contact by getting-started
- **Purpose:** Fires daily at the end of the user's day so Root reviews its own work, errors and corrections and proposes improvements.

## Routine prompt

Schedule: daily at 22:00 in the user's local time zone (set on first contact).

End-of-day report and self-improvement review for Root Agent. Resolve <instance folder> via standing-workspace (verify the README Bot id matches yours; else stop). Write in the user's language.
Sources: (1) <instance folder>/daily-log/<date>.md; (2) today's Root conversation via the transcript tool; if unreadable, put 'Limit: today's conversation could not be read; report based on file records' at the top; (3) dispatch-log.md, work-queue.md, decisions.md, team briefings and brief files.
Write the report to <instance folder>/learning/<date>.md: a 3-5 line summary, then:
1) Task status: opened/closed/stuck today, and items idle 48h or more with their owner.
2) Questions and approvals pending from the user.
3) Rule compliance: unapproved deletion, unapproved external posting, unapproved applications or sends, commits with an identity other than the user's approved one or any Co-authored-by line for a Bot (each with evidence path).
4) Briefings: for every active team in work-queue (no hardcoded team names), today's briefing arrived, on time, else 'not received'. No quality judgment; only Lead-reported open issues.
5) Bot report relay check (mandatory): list every message received from other Bots today; check each was relayed to the user in the same turn and any request in it answered; flag misses as 'not relayed'.
6) Cleanup: list files exceeding the recorded retention policy with path and sha256 for approval; NEVER delete.
7) Learning: today's errors and user corrections and which rule or skill each was written to; ready-to-apply proposals with old text, new text and reason; new skill drafts under learning/skill-proposals/<name>/SKILL.md only after an overlap check with existing skills. Apply none.
8) Tomorrow's top 3.
On the user's weekly review day, add a weekly section.
Notify the user only if there is a problem, question or approval: a short summary plus the file path; otherwise save silently. No messages to other Bots, no deletion, no publishing, no profile or skill changes.
