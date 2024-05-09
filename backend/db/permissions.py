from user.auth import get_active_user_principals
from fastapi import Depends, HTTPException
from user.schemas import UserDetails

### permissions ####
class RoleChecker:
    def __init__(self, allowed_roles:list):
        self.allowed_roles = allowed_roles

    def __call__(self, user: UserDetails = Depends(get_active_user_principals)):
        print('--->',user.get('role'))
        if user.get('role') not in self.allowed_roles:
            raise HTTPException(status_code=403, detail="Operation not permitted")