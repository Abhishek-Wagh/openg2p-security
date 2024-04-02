{
    "name": "G2P:Registry Encryption",
    "category": "G2P",
    "version": "17.0.1.0.0",
    "sequence": 1,
    "author": "OpenG2P",
    "website": "https://openg2p.org",
    "license": "Other OSI approved licence",
    "development_status": "Alpha",
    "depends": ["g2p_encryption", "g2p_registry_base", "g2p_registry_individual"],
    "data": [
        "views/decrypt_file.xml",
        "views/res_config_view.xml",
        "security/security.xml",
    ],
    "assets": {
        "web.assets_backend": [],
    },
    "demo": [],
    "images": [],
    "application": False,
    "installable": True,
    "auto_install": False,
}
