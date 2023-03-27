"""
BRVNS Source Module
"""
from src.cogs import background_tasks, slash_admin_only, slash_brvns


def setup(bot):
    """
    Run the setup functions for all Cogs.
    """
    background_tasks.setup(bot)
    slash_admin_only.setup(bot)
    slash_brvns.setup(bot)
