# Business Insights & Recommendations

## Business Insights

1. **Overtime is the strongest single driver of attrition observed.**
   Employees working overtime leave at ~30%, versus ~19% for those who
   don't — an 11-point gap. This is a pattern, not proof of causation:
   overtime may itself be a symptom of understaffing rather than the root
   cause, but it's the most actionable lever available.

2. **Attrition is concentrated in the first year of tenure.** Employees
   with 0–1 years at the company leave at ~30%, nearly double the rate of
   employees with 2–3 or 4–6 years. This points to an onboarding/early-
   experience problem rather than a broad, company-wide retention issue.

3. **Sales has the highest departmental attrition (~24%)**, driven
   largely by the Sales Executive role (~28%) — notably higher than
   Sales Representative (~21.5%). This suggests the issue may be specific
   to that role's structure (targets, comp plan, travel) rather than the
   department broadly.

4. **Attrition is not evenly explained by pay alone.** Roles like
   Healthcare Representative and Research Scientist show the lowest
   attrition despite not being the highest-paid roles, suggesting job
   satisfaction and work-life balance matter alongside compensation —
   worth confirming with the satisfaction-vs-attrition scatter on the
   dashboard rather than assuming from this summary alone.

## Decision-Oriented Recommendations

### 1. Launch a targeted first-year retention program
- **What:** Structured 30/60/90-day check-ins and a mentor assignment for
  all new hires in their first year.
- **Why:** 0–1 year tenure band shows the highest attrition (~30%) of any
  tenure segment.
- **Finding it supports:** Attrition Rate by Tenure Band.
- **Expected impact:** Reduced early-tenure attrition, lower replacement
  cost, faster time-to-productivity for new hires.

### 2. Audit workload and staffing in overtime-heavy teams
- **What:** Review staffing levels and workload distribution for teams
  where OverTime = Yes is common, starting with Sales Executive.
- **Why:** Overtime employees attrite at ~30% vs ~19% for non-overtime.
- **Finding it supports:** Attrition Rate by OverTime Status.
- **Expected impact:** Lower burnout-driven attrition; requires
  distinguishing "chronic understaffing" from "seasonal peak" before
  committing to headcount changes.

### 3. Review the Sales Executive compensation/role structure
- **What:** Compare comp plan, quota structure, and role expectations for
  Sales Executive against the lower-attrition Sales Representative role.
- **Why:** Sales Executive attrition (~28%) is well above the department
  average (~24%) and most other roles.
- **Finding it supports:** Attrition Rate by Job Role.
- **Expected impact:** Reduced turnover in the highest-risk sales role,
  more stable pipeline coverage.

### 4. Stand up a proactive "high-risk" outreach list
- **What:** Use the Watch List dashboard page (overtime + below-average
  satisfaction + first-year tenure) as a monthly action list for HR
  business partners to check in with those employees directly.
- **Why:** Combines the three strongest observed risk factors into one
  actionable, individual-level list rather than only department-level
  averages.
- **Finding it supports:** High-Risk Segment Count KPI.
- **Expected impact:** Earlier intervention before resignation, rather
  than only measuring attrition after the fact.

> **Note on causality:** All findings above describe *observed
> correlations* in this dataset, not proven causes. Before committing
> budget (e.g. to headcount or comp changes), validate with exit-interview
> data or a targeted survey of the flagged segments.
