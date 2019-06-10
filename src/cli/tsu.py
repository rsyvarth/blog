import argparse
import sys
import json
from commands import config, deploy, watch, publish

commands = [
    config.ConfigCmd,
    deploy.DeployCmd,
    watch.WatchCmd,
    publish.PublishCmd,
]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Tool for managing your Tsu installation')
    parser.add_argument('-s', '--stage', choices=['prod','staging','dev'], help='Stage to run against', default='prod')
    subparsers = parser.add_subparsers(
        title="Commands",
        description="The following commands are available",
        help="Command info",
    )

    # Load up all of our commands and register them
    for commandCls in commands:
        commandCls().register_subcommand(subparsers)

    # Default to printing help if a command isn't provided
    if len(sys.argv) <= 1:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()
    args.command(args)
