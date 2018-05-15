""" Commandline Entrypoint """

import click

from scival.util import setup_logger
from scival.retrieve_data.espa import espa_orders_api
from scival.retrieve_data.espa import order_scenes_c1
from scival.validate_data.qa import qa_data


@click.group(context_settings={'help_option_names': ['-h', '--help']})
@click.option('-v', '--verbose', count=True)
def cli(verbose):
    setup_logger(verbose)


@cli.group('qa')
def qa():
    """ Perform QA on georeferenced images and associated metadata """
    pass


@qa.command('compare', help='Compare files in two directories')
@click.option('-m', '--dir_mast', required=True, type=str, help='The Master directory')
@click.option('-t', '--dir_test', required=True, type=str, help='The Test directory')
@click.option('-o', '--dir_out', required=True, type=str, help='The Results directory')
@click.option('-x', '--xml_schema', required=False, type=str, help='Full path to XML schema')
@click.option('--archive/--no-archive', default=False, help='Look for archives or files')
@click.option('--include-nodata', default=False, is_flag=True, help='Do not mask NoData values')
def scival(dir_mast, dir_test, dir_out, xml_schema, archive, include_nodata):
    qa_data(dir_mast, dir_test, dir_out, archive, xml_schema, include_nodata)


@cli.group('espa')
def espa():
    """ Orders/Downloads from an ESPA system """
    pass


@espa.command('order', help='Order new products for on-demand processing')
@click.option('-u', '--username', required=True, type=str, help='ESPA user name', envvar='ESPA_SCIVAL_ESPA_USERNAME')
@click.option('-e', '--espa_env', required=True, type=click.Choice(espa_orders_api.api_config.espa_env.keys()), help='ESPA environment', envvar='ESPA_SCIVAL_ESPA_ENV')
@click.option('-o', '--dir_out', required=True, type=str, help='The output directory')
@click.option('--order', required=False, type=str, help='Specify a keyword to look up the appropriate order from order_specs.py')
def order(username, espa_env, dir_out, order):
    order_scenes_c1.place_order(espa_env, username, dir_out, order)


@espa.command('download', help='Download already processed data')
@click.option('-i', '--txt_in', required=True, type=str, help='The .txt file containing the ESPA orders')
@click.option('-o', '--dir_out', required=True, type=str, help='The output directory')
@click.option('-u', '--username', required=True, type=str, help='ESPA user name', envvar='ESPA_SCIVAL_ESPA_USERNAME')
@click.option('-e', '--espa_env', required=True, type=click.Choice(espa_orders_api.api_config.espa_env.keys()), help='ESPA environment', envvar='ESPA_SCIVAL_ESPA_ENV')
def download(txt_in, outdir, username, espa_env):
    espa_orders_api.get_orders(txt_in, outdir, username, espa_env)
