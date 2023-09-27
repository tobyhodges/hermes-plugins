'''
deposit_trainingmaterial_jsonld.py

A plugin to HERMES.
'''

import click
import json
from hermes.model.context import CodeMetaContext
from hermes import config
from hermes.error import MisconfigurationError

def export(click_ctx: click.Context, ctx: CodeMetaContext):
    '''Write out a JSON-LD file of TrainingMaterial metadata.

    Returns: nothing.
    '''
    trainingmaterial_jsonld_config = config.get("deposit").get("trainingmaterial_jsonld", {})

    output_json = invenio_config.get("output")
    if output_json is None:
        raise MisconfigurationError("deposit.trainingmaterial_jsonld.output is not configured")

    title = ctx['title']
    license = ctx['license']

    json_blob = json.dumps({'title': title,
                            'license': license})

    with open(output_json, 'w') as outfh:
        outfh.write(json_blob)
