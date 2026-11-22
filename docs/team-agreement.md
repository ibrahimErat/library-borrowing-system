# Team Agreement

**Team:** İbrahim Erat, Abubakr Gafarov, Mert Gumus, Dinkinesh Nure, Yiğidhan Soytürk
**Agreed on:** 17 November 2026 (Sprint 0). Changes are made through a pull request and noted in the sprint retrospective.

## 1. Communication

- **Day-to-day chat:** Microsoft Teams team chat.
- **Meetings and lab sessions:** Microsoft Teams (lab room) or on site.
- **Work tracking:** everything that is work becomes an issue on the GitHub board. Decisions that matter are written in the issue or in `docs/`, not only in chat.
- **Response time:** we answer team messages within 24 hours on working days.

## 2. Meeting rhythm

| Event | When | Length | Output |
|---|---|---|---|
| Sprint Planning | First day of each sprint | 30–45 min | Sprint goal and selected issues |
| Sync (short stand-up) | Twice a week, online | 15 min | What I did / what I do next / what blocks me |
| Sprint Review | Last day of each sprint | 20–30 min | Demo against acceptance criteria and feedback |
| Retrospective | Right after the review | 15–20 min | One action for the next sprint, with an owner |

Facilitation and note-taking rotate each meeting. Notes go to `docs/sprints/sprint-N.md`.

## 3. Roles (rotating every sprint)

| Sprint | Scrum Master | Product Owner |
|---|---|---|
| Sprint 0 | İbrahim Erat | Dinkinesh Nure |
| Sprint 1 | Mert Gumus | Abubakr Gafarov |
| Sprint 2 | Yiğidhan Soytürk | İbrahim Erat |
| Sprint 3 | Dinkinesh Nure | Mert Gumus |

- **Product Owner:** keeps the backlog ordered, writes or clarifies acceptance criteria, accepts finished stories at the review.
- **Scrum Master:** runs the meetings, removes blockers, watches the board and work in progress.
- **Everyone** is a developer: writes code, tests, reviews and documentation.

## 4. Decision making

1. Discuss in the group chat or in a meeting.
2. Aim for agreement. If there is none within one day, we take a majority vote.
3. Backlog priority: the Product Owner has the final say.
4. Technical decisions with long-term impact are recorded as an architecture decision record in `docs/architecture.md`.

## 5. Absences

- Tell the team in the group chat **at least 24 hours before** if you cannot attend or cannot finish a task.
- Move your unfinished issue back to **To Do** or hand it over with a short status comment.
- Missed meetings: read the notes in `docs/sprints/` and catch up on the board.

## 6. Blocked work

- If you are blocked for **more than one working day**, write it in the group chat and add the `blocked` label to the issue.
- The Scrum Master arranges help (pairing or reassigning) within one day.

## 7. Board workflow

`Backlog → To Do (this sprint) → In Progress → In Review → Done`

- Each person has at most **2 issues In Progress** at a time.
- An issue is **Done** only when it meets the Definition of Done.

## 8. Branches, pull requests and reviews

- No direct pushes to `main`.
- One branch per issue: `feature/<issue-number>-short-name` or `fix/<issue-number>-short-name`.
- Every pull request links its issue (`Closes #N`) and uses the PR template.
- **At least one approval from another member** is required before merging.
- Reviewers respond **within 48 hours** and check behaviour, design, tests and readability.
- CI must be green before merging. If `main` breaks, fixing it is the top priority for whoever merged last.

## 9. Definition of Done

A backlog item is **Done** when:

- [ ] All acceptance criteria are met and demonstrated.
- [ ] Automated tests cover the new behaviour and all tests pass.
- [ ] CI (GitHub Actions) is green on the pull request.
- [ ] The code was reviewed and approved by at least one other member.
- [ ] The change is merged into `main`.
- [ ] README or `docs/` are updated if behaviour or setup changed.
- [ ] No passwords, tokens or personal data are in the repository.

## 10. Repository rules

- No secrets or real personal data in the repository. Use fake sample data only.
- Do not rewrite shared history (no force-push to `main`).
- The repository is accessible to the instructor (the repository is public).
