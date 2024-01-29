
from collections import OrderedDict
import inspect
import sys
from pydoc import cli
import papermill
import click
from loguru import logger
from paperless.paperless import Paperless

@click.group()
def cli():
    """
    This is the main command line interface for the Paperless application.
    """



def PaperlessExecuter(*args, **kwargs):
    """
    Executes the Paperless application with the given arguments and keyword arguments.

    Args:
        *args: Positional arguments passed to the Paperless application.
        **kwargs: Keyword arguments passed to the Paperless application.

    Returns:
        The result of executing the Paperless application.
    """
    logger.info("paperless execution started!")
    return Paperless(notebook_path=kwargs['input_path'],
                     template_name=kwargs['template_name']).\
        configure().\
        wait_for_session().\
        verify().\
        execute(args,kwargs).\
        shutdown()
    

# replace the execute_notebook function with the PaperlessExecuter
module = sys.modules["papermill.execute"]
module.execute_notebook =  PaperlessExecuter
from papermill.cli import papermill

# export defualt command of papermill
papermill()