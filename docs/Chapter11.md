##  My Building Guide

#### Topic : Custom Password Interface
- Password Change
- Password Reset
---

1. Customize Password Change
    - create form template at `validation/password_change_form.html`
    - create static template at `validation/password_change_done.html`

2. Customize Password Reset
    - Set up development email service : `EMAIL_BACKEND`
    - create 4 templates : `password_reset_form`, `...reset_done`, `...reset_confirm`, `...reset_complete`
    - add 'forgot password' link to `validation/login.html`