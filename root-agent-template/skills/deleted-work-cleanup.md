# deleted-work-cleanup

## When to use

Use when a group, team, Bot-owned domain or task is deleted or cancelled, including test tasks: close it, stop tracking it, and delete its box files safely. (User overlay — preserved verbatim through canonical framework updates. Applies to test tasks too.) work-control step 15 closes the record; this skill also removes the closed work's own files.

## Required inputs and access

Read your instance's work-queue.md, dispatch-log.md, decisions.md and the current todo list. Reopen the evidence that the owning Bot, team or group was deleted, or the user's cancel or stop. List the workspace folders of every still-active team so their files are excluded.

## Sequence of work

1. Mark the task(s) `closed (owner deleted)` or `closed (cancelled)` in work-queue.md with date and evidence, and move them to the archive section.
2. In the same turn, cancel every todo item and dependent step (reviewer selection, relay, checkpoint, follow-up), drop it from open-issue and recommendation lists, and remove it from stall checks and where-we-are.
3. Identify only files that belong exclusively to that task/team (its own workspace folder, its briefs). Never touch files of another active team or shared files; when a file is shared, keep it.
4. Before deleting, write the exact file list to `deletions/<task-or-team>-<date>.txt` under your own instance folder.
5. Deletion needs the user's approval in Root Agent's own chat (a card); an approval relayed by another Bot is not enough. After approval, delete, verify the paths are gone, and update the record's evidence line to point at the deletion list.
6. Root's own dispatch-log.md and decisions.md summary lines stay as history.

## Validate the result

Re-read work-queue.md and the todo list: the closed work is archived and nothing that belongs to it stays open. Confirm every listed path is gone and that no file of an active team or a shared file was removed. A deletion without a saved list or without the user's own approval is a failure.

## What to return

Report once: what was closed, how many files were deleted, the list path.

## What requires approval

Closing records and cancelling Root Agent's own todo items are covered by the task authority. Deleting files requires the user's approval in Root Agent's own conversation; an approval relayed by another Bot does not count. This skill does not delete Bots, groups or files outside the box.
