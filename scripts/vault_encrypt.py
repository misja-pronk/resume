# /// script
# requires-python = ">=3.11"
# dependencies = ["cryptography>=42"]
# ///
"""Encrypt brand assets from brand/ into public/vault/.

Run with:  VAULT_PASSPHRASE='your-passphrase' uv run scripts/vault_encrypt.py

The plaintext files in brand/ are gitignored; only the encrypted .enc
files are committed and published. The vault page (/vault) decrypts
them in the browser with the same passphrase (PBKDF2-SHA256, 310k
iterations, AES-256-GCM). Format: b"MPV1" + salt(16) + iv(12) + ciphertext.
"""

import json
import os
from pathlib import Path

from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

ROOT = Path(__file__).resolve().parent.parent
BRAND = ROOT / "brand"
VAULT = ROOT / "public" / "vault"
MANIFEST = ROOT / "src" / "data" / "vault.json"

ITERATIONS = 310_000

ASSETS = [
    {
        "src": "prorex-deck-template.pptx",
        "out": "deck-template.enc",
        "label": {"en": "ProRex deck template", "nl": "ProRex-decktemplate"},
        "sub": "POWERPOINT · 7 SHEETS",
        "mime": "application/vnd.openxmlformats-officedocument.presentationml.presentation",
        "filename": "prorex-deck-template.pptx",
    },
    {
        "src": "prorex-deck-template.html",
        "out": "deck-html.enc",
        "label": {"en": "Deck template (browser/HTML)", "nl": "Decktemplate (browser/HTML)"},
        "sub": "HTML · 7 SHEETS · ARROW-KEY NAV",
        "mime": "text/html",
        "filename": "prorex-deck-template.html",
    },
    {
        "src": "prorex-business-card.pdf",
        "out": "business-card.enc",
        "label": {"en": "Business card (print-ready)", "nl": "Visitekaartje (drukklaar)"},
        "sub": "PDF · 85×55 MM · FRONT+BACK",
        "mime": "application/pdf",
        "filename": "prorex-business-card.pdf",
    },
]


def main() -> None:
    passphrase = os.environ.get("VAULT_PASSPHRASE", "meet-twee-keer-bouw-een-keer")
    VAULT.mkdir(parents=True, exist_ok=True)

    manifest = []
    for asset in ASSETS:
        src = BRAND / asset["src"]
        if not src.exists():
            print(f"skip (missing): {src}")
            continue
        data = src.read_bytes()
        salt = os.urandom(16)
        iv = os.urandom(12)
        kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=ITERATIONS)
        key = kdf.derive(passphrase.encode())
        ct = AESGCM(key).encrypt(iv, data, None)
        out = VAULT / asset["out"]
        out.write_bytes(b"MPV1" + salt + iv + ct)
        manifest.append(
            {
                "file": asset["out"],
                "label": asset["label"],
                "sub": asset["sub"],
                "mime": asset["mime"],
                "filename": asset["filename"],
                "bytes": len(data),
            }
        )
        print(f"encrypted {asset['src']} -> vault/{asset['out']} ({len(data)//1024} KB)")

    MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"wrote {MANIFEST}")


if __name__ == "__main__":
    main()
