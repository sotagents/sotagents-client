from typing import Optional


from sotagents.models.page import Page
from sotagents.models.model import Model
from sotagents.models.paper import Paper
from sotagents.models.repository import Repository


class PaperRepo(Model):
    """Paper <-> Repository object.

    Attributes:
        paper: Paper objects.
        repository: Repository object.
        is_official: Is this the official implementation.
    """

    paper: Paper
    repository: Optional[Repository]
    is_official: bool


class PaperRepos(Page):
    """Object representing a paginated page of paper<->repos.

    Attributes:
        count: Number of elements matching the query.
        next_page: Number of the next page.
        previous_page: Number of the previous page.
        results: List of paper<->repos on this page.
    """

    results: list[PaperRepo]
