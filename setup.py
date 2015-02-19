from setuptools import setup

setup(
    name="electrum-nmc-server",
    version="0.9",
    scripts=['run_electrum_nmc_server','electrum-nmc-server'],
    install_requires=['plyvel','jsonrpclib', 'irc>=11'],
    package_dir={
        'electrumnmcserver':'src'
        },
    py_modules=[
        'electrumnmcserver.__init__',
        'electrumnmcserver.utils',
        'electrumnmcserver.storage',
        'electrumnmcserver.deserialize',
        'electrumnmcserver.networks',
        'electrumnmcserver.blockchain_processor',
        'electrumnmcserver.server_processor',
        'electrumnmcserver.processor',
        'electrumnmcserver.version',
        'electrumnmcserver.ircthread',
        'electrumnmcserver.stratum_tcp',
        'electrumnmcserver.stratum_http'
    ],
    description="Namecoin Electrum Server",
    author="Thomas Voegtlin",
    author_email="thomasv1@gmx.de",
    license="GNU Affero GPLv3",
    url="https://github.com/spesmilo/electrum-server/",
    long_description="""Server for the Electrum-NMC Lightweight Namecoin Wallet"""
)


