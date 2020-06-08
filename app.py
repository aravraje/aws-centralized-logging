#!/usr/bin/env python3

from aws_cdk import core

from aws_centralized_logging.aws_centralized_logging_stack import AwsCentralizedLoggingStack


app = core.App()
AwsCentralizedLoggingStack(app, "aws-centralized-logging")

app.synth()
