"""Upload a structured summary to Notion for human review.

Final stage of the pipeline: a structured summary (from the writing/summary agent) is
pushed to a Notion database as a review card, where a human approves or edits it before
it becomes a published post.

CLI:
    python -m notion_review --dry-run           # print the Notion payload, no API call
    python -m notion_review summary.json        # create a review page (needs NOTION_TOKEN)
"""
from .upload import create_review_page

__all__ = ["create_review_page"]
