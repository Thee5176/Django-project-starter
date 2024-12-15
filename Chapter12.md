##  My Building Guide

#### Topic : Email Functionality
- SendGrid Integration (free plan 100 mails/day)
- Custom Email Template: subject and body
---

1. Set up `EMAIL_BACKEND`,`DEFALT_FROM_EMAIL`, `EMAIL_HOST`,`EMAIL_HOST_USER`,`EMAIL_HOST_PASSWORD`,`EMAIL_PORT`,`EMAIL_USE_TLS`
2. Copy source code and paste into `registration/password_reset_email.html`
3. Create new textfile `registration/password_reset_subject.txt`