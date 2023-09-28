'''
deposit_trainingmaterial_jsonld.py

A plugin to HERMES.
'''

import click
import json
import logging
from hermes.model.context import CodeMetaContext
from hermes import config
from hermes.error import MisconfigurationError

_log = logging.getLogger('hermes.deposit.trainingmaterial_jsonld')

def export(click_ctx: click.Context, ctx: CodeMetaContext):
    '''Write out a JSON-LD file of TrainingMaterial metadata.

    Returns: nothing.
    '''
    # extract the relevant configuration parameters for this plugin from the hermes.toml file
    trainingmaterial_jsonld_config = config.get("deposit").get("trainingmaterial_jsonld", {})

    # pull out the name of the output file that was set in the config file
    output_json = trainingmaterial_jsonld_config.get("output")
    if output_json is None:
        raise MisconfigurationError("deposit.trainingmaterial_jsonld.output is not configured")

    _log.info(f'depositing JSON-LD output in {output_json}.')

    # get some fields from the harvested metadata
    title = ctx['codemeta.name']
    license = ctx['codemeta.license']

    # create a JSON object from the extracted fields
    json_blob = json.dumps({'title': title,
                            'license': license})

    # write the JSON out to a file
    with open(output_json, 'w') as outfh:
        outfh.write(json_blob)
