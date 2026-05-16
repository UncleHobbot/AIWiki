"""
obs.py - Obsidian vault analysis CLI for the LLM Wiki.

Usage (run from project root):
  python scripts/obs.py backlinks <slug>   # who links TO this entry
  python scripts/obs.py links <slug>       # what this entry links TO
  python scripts/obs.py broken             # [[links]] pointing to nonexistent entries
  python scripts/obs.py orphans            # entries with zero incoming backlinks
  python scripts/obs.py isolated           # entries with no links in or out
  python scripts/obs.py top [N]            # top N most-linked entries (default 10)
  python scripts/obs.py check              # full vault health report
"""

import sys
import pathlib
import obsidiantools.api as ot

VAULT_DIR = pathlib.Path(__file__).parent.parent / "wiki"


def _load_vault():
    return ot.Vault(VAULT_DIR).connect().gather()


def _dedup(seq):
    """Remove duplicates while preserving order (backlinks appear twice: EN + RU)."""
    seen = set()
    out = []
    for x in seq:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out


def cmd_backlinks(slug):
    """Print all entries that contain [[slug]] links."""
    vault = _load_vault()
    if slug not in vault.md_file_index:
        print(f"WARN: '{slug}' not found in vault (no matching .md file).", file=sys.stderr)
    raw = vault.get_backlinks(slug)
    links = sorted(_dedup(raw))
    if not links:
        print(f"No backlinks found for '{slug}'.")
    else:
        print(f"Backlinks to [[{slug}]] ({len(links)}):")
        for name in links:
            print(f"  [[{name}]]")


def cmd_links(slug):
    """Print all [[links]] that this entry points to."""
    vault = _load_vault()
    if slug not in vault.md_file_index:
        print(f"WARN: '{slug}' not found in vault.", file=sys.stderr)
    raw = vault.get_wikilinks(slug)
    links = sorted(_dedup(raw))
    if not links:
        print(f"'{slug}' has no outgoing [[links]].")
    else:
        print(f"Links from '{slug}' ({len(links)}):")
        for name in links:
            exists = name in vault.md_file_index
            status = "" if exists else "  [BROKEN]"
            print(f"  [[{name}]]{status}")


def cmd_broken():
    """List all [[link]] targets that have no corresponding .md file."""
    vault = _load_vault()
    broken = sorted(vault.nonexistent_notes)
    if not broken:
        print("No broken links. OK")
        return
    print(f"Broken [[links]] - targets with no .md file ({len(broken)}):")
    for target in broken:
        # Find which notes link to this broken target
        sources = sorted(_dedup(vault.get_backlinks(target)))
        src_str = ", ".join(f"[[{s}]]" for s in sources)
        print(f"  [[{target}]]  <-{src_str}")


def cmd_orphans():
    """List entries that no other entry links to (zero incoming backlinks)."""
    vault = _load_vault()
    all_notes = list(vault.md_file_index.keys())
    orphans = []
    for note in all_notes:
        bl = _dedup(vault.get_backlinks(note))
        if not bl:
            orphans.append(note)
    orphans.sort()
    if not orphans:
        print("No orphaned entries. OK")
        return
    print(f"Orphaned entries - no incoming backlinks ({len(orphans)}):")
    for name in orphans:
        # Show its category from path
        rel = vault.md_file_index[name]
        cat = str(rel).split("\\")[0] if "\\" in str(rel) else str(rel).split("/")[0]
        print(f"  {cat}/{name}")


def cmd_isolated():
    """List entries with zero links in both directions."""
    vault = _load_vault()
    isolated = sorted(vault.isolated_notes)
    if not isolated:
        print("No isolated entries. OK")
        return
    print(f"Isolated entries - no links in or out ({len(isolated)}):")
    for name in isolated:
        print(f"  [[{name}]]")


def cmd_top(n=10):
    """Print the N entries with the most incoming backlinks."""
    vault = _load_vault()
    all_notes = list(vault.md_file_index.keys())
    counts = []
    for note in all_notes:
        bl = _dedup(vault.get_backlinks(note))
        counts.append((note, len(bl)))
    counts.sort(key=lambda x: x[1], reverse=True)
    top = counts[:n]
    print(f"Top {n} most-linked entries:")
    for name, count in top:
        bar = "#" * min(count, 20)
        print(f"  {count:3d}  {bar}  [[{name}]]")


def cmd_check():
    """Full vault health report: broken links, orphans, isolated, top linked."""
    vault = _load_vault()
    all_notes = list(vault.md_file_index.keys())
    total = len(all_notes)

    # Broken links
    broken = sorted(vault.nonexistent_notes)
    # Orphans
    orphans = sorted(n for n in all_notes if not _dedup(vault.get_backlinks(n)))
    # Isolated
    isolated = sorted(vault.isolated_notes)
    # Top linked
    counts = sorted(
        ((n, len(_dedup(vault.get_backlinks(n)))) for n in all_notes),
        key=lambda x: x[1], reverse=True
    )

    print(f"=== Vault health check - {total} entries ===")
    print()

    if broken:
        print(f"[BROKEN] {len(broken)} link target(s) with no .md file:")
        for target in broken:
            sources = sorted(_dedup(vault.get_backlinks(target)))
            src_str = ", ".join(f"[[{s}]]" for s in sources[:3])
            more = f" +{len(sources)-3} more" if len(sources) > 3 else ""
            print(f"   [[{target}]]  <-  {src_str}{more}")
    else:
        print("[OK] No broken links")
    print()

    if orphans:
        print(f"[ORPHAN] {len(orphans)} entry/entries with no incoming backlinks:")
        for name in orphans:
            rel = vault.md_file_index[name]
            cat = pathlib.Path(rel).parts[0] if pathlib.Path(rel).parts else "?"
            print(f"   {cat}/{name}")
    else:
        print("[OK] No orphaned entries")
    print()

    if isolated:
        print(f"[ISOLATED] {len(isolated)} entry/entries with no links at all:")
        for name in isolated:
            print(f"   [[{name}]]")
    else:
        print("[OK] No isolated entries")
    print()

    print("Top 10 most-linked entries:")
    for name, count in counts[:10]:
        print(f"   {count:3d}  [[{name}]]")


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(0)

    cmd = args[0]

    if cmd == "backlinks":
        if len(args) < 2:
            print("Usage: obs.py backlinks <slug>", file=sys.stderr); sys.exit(1)
        cmd_backlinks(args[1])
    elif cmd == "links":
        if len(args) < 2:
            print("Usage: obs.py links <slug>", file=sys.stderr); sys.exit(1)
        cmd_links(args[1])
    elif cmd == "broken":
        cmd_broken()
    elif cmd == "orphans":
        cmd_orphans()
    elif cmd == "isolated":
        cmd_isolated()
    elif cmd == "top":
        n = int(args[1]) if len(args) > 1 else 10
        cmd_top(n)
    elif cmd == "check":
        cmd_check()
    else:
        print(f"Unknown command: {cmd}", file=sys.stderr)
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
