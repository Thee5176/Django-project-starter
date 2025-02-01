##  My Building Guide

#### Topic : Custom User Model Setup
- Custom user model that can be updated
---

#### 4 steps process
1. update setting
    - start and install `accounts` app
    - `project/setting.py` : add `AUTH_USER_MODEL`
2. create CustomUser model
    - `accounts/models.py` : create `CustomUser` by inherit from `AbstractUser`
    - add custom fields
    > null vs blank: Best Practice to use them together 
    > - `null` - database-side value
    > - `blank` - validation-side value
3. create 2 CustomUserForm : inherit from UserCreationForm and UserChangeForm
    - `accounts/forms.py`:
        - CustomUserCreationForm: `model`, `fields`
        - CustomUserChangeForm: `model`, `fields`
4. update admin
    - `accounts/admin.py`:
        - CustomUserAdmin : `add_form`, `form`, `model`, `list_display`, `field_set`, `add_field_set`
    - register `CustomUser`,`CustomUserAdmin`
    - Migration
---