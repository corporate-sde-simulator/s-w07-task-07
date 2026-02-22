# FINSERV-4247: Investigate paginated API returning duplicate/missing records

**Status:** In Progress · **Priority:** Critical
**Sprint:** Sprint 29 · **Story Points:** 8
**Reporter:** Suresh Kumar (API Lead) · **Assignee:** You (Intern)
**Due:** End of sprint (Friday)
**Labels:** `backend`, `python`, `api`, `data`
**Task Type:** Code Debugging

---

## Description

The cursor-based pagination engine returns paginated results for large datasets. Users report getting duplicate records across pages and some records never appearing.

**DEBUGGING task — no hint comments. Investigate from symptoms.**

## Symptoms

- Page 1 returns records 1-20, Page 2 returns records 11-30 (overlap of 10 records)
- Record with ID 15 never appears in any page when sorting by created_date DESC
- Total count says 100 records, but iterating all pages only yields 85 unique records
- When a record is inserted during pagination, subsequent pages shift and repeat data

## Acceptance Criteria

- [ ] Root cause found and fixed
- [ ] No duplicates across pages
- [ ] All unit tests pass
