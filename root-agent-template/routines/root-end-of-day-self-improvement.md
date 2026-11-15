# Routine: Root end-of-day self-improvement

- **Slug:** `root-end-of-day-self-improvement`
- **Owner:** Root Agent (the only routine Root owns; it concerns only Root itself)
- **Schedule:** daily, default 22:00 in the user's local time zone; set up on first contact by getting-started
- **Purpose:** Fires daily at the end of the user's day so Root reviews its own work, errors and corrections and proposes improvements.
- **Mode:** file audit only. The routine does not read the conversation; relay verification of Bot messages is completed by Root on its next interactive turn (result-relay step 5a). If an installation has no routine, the same checks ride on the first turn of the next day (work-control steps 21 and 24).

## Routine prompt

Schedule: daily at 22:00 in the user's local time zone (set on first contact).

End-of-day report and self-improvement review for Root Agent. Resolve <instance folder> via standing-workspace (verify the README Bot id matches yours; else stop). Write in the user's language.
Sources: (1) <instance folder>/daily-log/<date>.md; (2) do not try to read the conversation; the report rests on file records. Put 'Limit: report based on file records; relay verification of Bot messages is completed by Root on its next interactive turn' at the top; (3) dispatch-log.md, work-queue.md, decisions.md, team briefings and brief files. An empty or missing daily log is a 'record gap' (activity unknown), never 'no activity' (standing-workspace daily-log).
Write the report to <instance folder>/learning/<date>.md: a 3-5 line summary, then:
1) Task status: opened/closed/stuck today, and items idle 48h or more with their owner. Mark every open record past its `checkpoint-due` without newer evidence as `stalled?` with owner and proposed new date (work-control step 21), and list team stop/restart/pause/rule-change entries that differ from work-queue (work-control step 24).
2) Questions and approvals pending from the user. A decision carried through three consecutive reports is presented as one highest-priority question (yes / no / defer to a date) plus a count of the rest (portfolio-status step 12).
3) Rule compliance: unapproved deletion, unapproved external posting, unapproved applications or sends, commits with an identity other than the user's approved one or any Co-authored-by line for a Bot (each with evidence path). An external effect that no record or approval explains is listed as an open question for the user ('did you do this yourself?'), not as a violation (work-control step 23).
4) Briefings: for every active team in work-queue (no hardcoded team names), today's briefing arrived, on time, else 'not received'. No quality judgment; only Lead-reported open issues. For each missing briefing, start or advance its delay counter in work-queue (first missing date, limit) so the status questions run on the next interactive turn (blocker-escalation step 12).
5) Bot report relay check (mandatory, from file records only): list every message dispatch-log records as received from another Bot today, leaving out Bots the user excluded from tracking (they are also left out of the whole report), and match each with its relayed-to-user line and, where it contained a request, its answer line. Mark matched messages 'relayed (record)'. Mark every unmatched message, and any Bot message in the daily log missing from dispatch-log, 'relay unverified — Root completes on its next interactive turn'; never 'not relayed' (result-relay step 5a).
6) Cleanup: list files exceeding the recorded retention policy with path and sha256 for approval; NEVER delete.
7) Learning: today's errors and user corrections and which rule or skill each was written to; ready-to-apply proposals with old text, new text and reason; new skill drafts under learning/skill-proposals/<name>/SKILL.md only after an overlap check with existing skills. Every proposal for Root's description, skills or template must be generic: no personal names or handles, no bot or team names, no language or time-zone specifics, no instance paths or IDs; lessons specific to one user stay only in private records (daily log, learning report) and are not proposed for the template. Check each proposal for this ('is it generic?') and generalize it or mark it not for the template. Apply none.
8) Tomorrow's top 3.
On the user's weekly review day, add a weekly section.
Notify the user only if there is a problem, question or approval (including a record gap): a short summary plus the file path; otherwise save silently. 'Relay unverified' lines alone are not a reason to notify; Root completes them on its next interactive turn. No messages to other Bots, no deletion, no publishing, no profile or skill changes.
