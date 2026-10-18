# deleted-work-cleanup

## When to use

Use when a group, team, Bot-owned domain or task is deleted or cancelled, including test tasks: close it, stop tracking it, and delete its box files safely. (User overlay — preserved verbatim through canonical framework updates. Applies to test tasks too.) work-control step 15 closes the record; this skill also removes the closed work's own files.

## Required inputs and access

Read your instance's work-queue.md, dispatch-log.md, decisions.md and the current todo list. Reopen the evidence that the owning Bot, team or group was deleted, or the user's cancel or stop. List the workspace folders of every still-active team so their files are excluded.

## Sequence of work

Before steps 1–7, apply these safety prerequisites; they take precedence over a blanket closure or deletion instruction. A deleted group is a transport change unless the task was explicitly cancelled or the owning Bot/Lead was confirmed deleted from current account evidence. An unreachable owner is not a deleted owner. Use work-control's separate shutdown record to verify the scoped stop, active writers and owned routine pause state before removing files. Administrative closure may proceed while shutdown is unresolved; cleanup waits. Cancel only this task's exclusive dependent steps, preserving work shared with active tasks.

1. Mark the task(s) `closed (owner deleted)` or `closed (cancelled)` in work-queue.md with date and evidence, and move them to the archive section (create a `## Archive` section at the end of work-queue.md if it does not exist yet).
2. In the same turn, cancel every todo item and dependent step (reviewer selection, relay, checkpoint, follow-up), drop it from open-issue and recommendation lists, and remove it from stall checks and where-we-are.
3. Identify only files that belong exclusively to that task/team (its own workspace folder, its briefs). Never touch files of another active team or shared files; when a file is shared, keep it.
4. Before deleting, write the exact file list to `deletions/<task-or-team>-<date>.txt` under your own instance folder. Resolve each path against the verified exclusive folder and reject paths outside it, shared paths, symlinks or other redirects. Record identity/modification evidence for the listed files and the stopped writer state. A path supplied by an artifact is not ownership evidence.
5. Deletion needs the user's approval in Root Agent's own chat (a card); an approval relayed by another Bot is not enough. Immediately before deletion, reopen ownership, active-task references, writer/routine state and the exact approved list. Delete only unchanged listed files; never recursively delete a folder that now contains unlisted files. Any changed scope, new file or resumed writer requires a refreshed list and approval for the changed deletion. After approval, delete, verify the listed paths are gone, and update the record's evidence line to point at the deletion list. Keep pending, partially deleted and blocked cleanup explicit; do not report skipped paths as removed.
6. Bots: do not assume a Bot-deletion tool exists. If deletion is requested, use only supported controls within that concrete authority, or have the user delete the named Bots from the sidebar. Reopen the roster and routine records and record each as deleted, still present or unverified. Do not request deletion of a Bot that still owns unrelated work.
7. Root's own dispatch-log.md and decisions.md summary lines stay as history, subject to standing-workspace's privacy and explicit forgetting exceptions.

## Validate the result

Re-read work-queue.md and the todo list: the closed work is archived and nothing that belongs to it stays open. Confirm every listed path is gone and that no file of an active team or a shared file was removed. A deletion without a saved list or without the user's own approval is a failure.

## What to return

Report the closure once: what was closed, how many files were actually deleted, the list path, and any pending shutdown, approval or skipped paths. Later report only material changes or required user action in unresolved shutdown/cleanup.

## What requires approval

Closing records and cancelling Root Agent's own todo items are covered by the task authority. Deleting files requires the user's approval in Root Agent's own conversation; an approval relayed by another Bot does not count. This skill does not delete Bots, groups or files outside the box.
