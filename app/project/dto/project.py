from pydantic import BaseModel


class ProjectForm(BaseModel):
    id: int = None
    name: str
    app: str
    owner: int
    private: bool = False
    description: str = ''
    dingtalk_url: str = None


class ProjectRoleForm(BaseModel):
    user_id: int
    project_role: int
    project_id: int


class ProjectRoleEditForm(BaseModel):
    id: int
    user_id: int
    project_role: int
    project_id: int


class ProjectDelForm(BaseModel):
    id: int


class ListProjectDto(BaseModel):
    page: int = 1
    size: int = 8
    name: str = ""


class CustomDto(BaseModel):
    id: int


class ProjectAvatarDto(BaseModel):
    project_id: int
    filename: str
    content: str


class PermissionDto(BaseModel):
    user_id: int
    user_role: int
    project_id: int


class UserProjectDto(BaseModel):
    user_id: int
