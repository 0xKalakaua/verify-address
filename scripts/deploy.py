#!/usr/bin/python3
import os
from brownie import Verifier, accounts, network


def main():
    dev = accounts.load("dev")
    print(network.show_active())
    publish_source = True
    Verifier.deploy({"from": dev}, publish_source=publish_source)
