from pathlib import Path

def rewrite(path, pairs):
    p = Path(path)
    s = p.read_text(encoding="utf-8")
    for old, new in pairs:
        if old not in s:
            raise SystemExit("missing pattern in %s: %r" % (path, old[:60]))
        s = s.replace(old, new)
    p.write_text(s, encoding="utf-8")

rewrite("index.html", [
    ('<strong>The Harbour</strong><p>Spawn heart and original harbour preserved.</p>',
     '<strong>The Landing</strong><p>Spawn heart and original landing preserved. The Harbour of First Light is 250 blocks south-east.</p>'),
    ('<span class="project-state">Anchored · 808 blocks</span><strong>Pirate Ship</strong><p>Sturdy schooner moored in the bay, viewable from the harbour.</p>',
     '<span class="project-state">Anchored · X 440, Z -580</span><strong>The Longwake</strong><p>The fleet\u0027s schooner, moored in the roads off the Open Sea.</p>'),
    ('and eleven places say something when you stand on them.', 'and seventeen places say something when you stand on them.'),
    ('>Start at the Harbour →</a>', '>Start at the Landing →</a>'),
    ('<small>Address</small>', '<small>Java address</small>'),
    ('<span>Minecraft: odysseyland.aternos.me:46767</span><span>Friendly community</span>',
     '<span>Java: odysseyland.aternos.me:56870</span><span>Bedrock: same address, port 19132</span>'),
])
PATH = Path("index.html")
PATH.write_text(PATH.read_text(encoding="utf-8").replace("46767", "56870"), encoding="utf-8")
