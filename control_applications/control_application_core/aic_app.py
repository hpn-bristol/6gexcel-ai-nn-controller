# Copyright (c) 2026 Trinity College Dublin
#
# This file is dual-licensed:
# - under the AGPL (see LICENSE)
# - under a commercial licence (contact infoknex@tcd.ie)

"""
Minimal core control application for ai_nn_controller.

Runs the controller framework (registration, message broker, REST/MCP server)
with no node subscriptions and no AI/LLM agent. It registers cleanly with the
near-RT RIC even when no network nodes are present, and serves the FastAPI/MCP
interface on port 8000.
"""

from ai_nn_controller.decorators.aic_app import aic_app
from ai_nn_controller.AicApp import AicApp
from ai_nn_controller.AicController import AicController
import argparse


@aic_app(name="CoreController")
class CoreControllerApp(AicApp):
    aic_app_id = 1
    control_loop_update_time = 2

    # No node subscriptions and no control functions: the controller runs the
    # framework and API without requiring any network nodes to be registered.
    read_measurements = {}
    control_functions = {}

    @classmethod
    def process(cls, measurements):
        # No control logic in the core-only deployment.
        pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AIC Core Controller")
    parser.add_argument("--verbose", "-v", action="store_true")
    parser.add_argument("--port", "-p", type=int, default=8000)
    parser.add_argument("--host", type=str, default="0.0.0.0")
    args = parser.parse_args()

    AicController(with_api=True, api_host=args.host, api_port=args.port, verbose=args.verbose).run()
