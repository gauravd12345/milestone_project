from flask import Blueprint

groups_bp = Blueprint(
    "groups",
    __name__,
    url_prefix="/groups",
    template_folder="templates",
)

from app.groups import routes  
