#!/usr/bin/env python3
"""
scripts/fetch_youtube.py
Fetch YouTube video metadata and transcript for LLM Wiki processing.
"""

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

try:
    from youtube_transcript_api import YouTubeTranscriptApi, NoTranscriptFound, TranscriptsDisabled
    HAS_TRANSCRIPT_API = True
except ImportError:
    HAS_TRANSCRIPT_API = False
    print("[warn] youtube-transcript-api not installed. Run: pip install youtube-transcript-api", file=sys.stderr)

try:
    import yt_dlp
    HAS_YTDLP = True
except ImportError:
    HAS_YTDLP = False

TRANSCRIPTS_DIR = Path("sources/transcripts")
TRANSCRIPTS_DIR.mkdir(parents=True, exist_ok=True)


def extract_video_id(url: str) -> str | None:
    """Extract YouTube video ID from various URL formats."""
    patterns = [
        r"(?:v=|youtu\.be/|embed/|v/)([a-zA-Z0-9_-]{11})",
        r"^([a-zA-Z0-9_-]{11})$",  # bare ID
    ]
    for pat in patterns:
        m = re.search(pat, url)
        if m:
            return m.group(1)
    return None


def get_video_metadata(video_id: str) -> dict:
    """Get video metadata using yt-dlp."""
    if not HAS_YTDLP:
        return {"video_id": video_id, "title": "", "channel": "", "date": "", "description": ""}

    ydl_opts = {
        "quiet": True,
        "no_warnings": True,
        "extract_flat": True,
        "skip_download": True,
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f"https://www.youtube.com/watch?v={video_id}", download=False)
            return {
                "video_id": video_id,
                "title": info.get("title", ""),
                "channel": info.get("channel", info.get("uploader", "")),
                "date": info.get("upload_date", ""),  # YYYYMMDD
                "description": (info.get("description", "") or "")[:1000],
                "duration_seconds": info.get("duration"),
                "view_count": info.get("view_count"),
                "url": f"https://www.youtube.com/watch?v={video_id}",
            }
    except Exception as e:
        print(f"  [warn] yt-dlp metadata error: {e}", file=sys.stderr)
        return {"video_id": video_id, "title": "", "channel": "", "date": "", "description": "", "url": f"https://www.youtube.com/watch?v={video_id}"}


def get_transcript(video_id: str) -> tuple[str, str]:
    """
    Try to get transcript. Returns (transcript_text, language_used).
    Prefers English; falls back to other available languages.
    """
    if not HAS_TRANSCRIPT_API:
        return "", "unavailable"

    preferred_langs = ["en", "en-US", "en-GB"]

    try:
        # Try preferred languages first
        try:
            transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=preferred_langs)
            lang = "en"
        except NoTranscriptFound:
            # Get whatever is available
            transcript_obj = YouTubeTranscriptApi.list_transcripts(video_id)
            try:
                transcript = transcript_obj.find_manually_created_transcript(preferred_langs)
            except NoTranscriptFound:
                try:
                    transcript = transcript_obj.find_generated_transcript(preferred_langs)
                except NoTranscriptFound:
                    # Take first available
                    transcripts = list(transcript_obj)
                    if not transcripts:
                        return "", "unavailable"
                    transcript = transcripts[0]

            transcript_list = transcript.fetch()
            lang = transcript.language_code

        # Format with timestamps
        lines = []
        for entry in transcript_list:
            start = int(entry["start"])
            mins, secs = divmod(start, 60)
            hours, mins = divmod(mins, 60)
            if hours:
                ts = f"[{hours:02d}:{mins:02d}:{secs:02d}]"
            else:
                ts = f"[{mins:02d}:{secs:02d}]"
            lines.append(f"{ts} {entry['text']}")

        return "\n".join(lines), lang

    except TranscriptsDisabled:
        print(f"  [warn] Transcripts disabled for {video_id}", file=sys.stderr)
        return "", "disabled"
    except Exception as e:
        print(f"  [warn] Transcript error for {video_id}: {e}", file=sys.stderr)
        return "", "error"


def get_transcript_ytdlp_fallback(video_id: str) -> tuple[str, str]:
    """Fallback: use yt-dlp to download auto-subtitles."""
    if not HAS_YTDLP:
        return "", "unavailable"

    out_path = TRANSCRIPTS_DIR / f"{video_id}_sub"
    ydl_opts = {
        "quiet": True,
        "no_warnings": True,
        "skip_download": True,
        "writeautomaticsub": True,
        "subtitleslangs": ["en"],
        "subtitlesformat": "vtt",
        "outtmpl": str(out_path),
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([f"https://www.youtube.com/watch?v={video_id}"])

        vtt_file = out_path.parent / f"{out_path.stem}.en.vtt"
        if vtt_file.exists():
            raw = vtt_file.read_text(encoding="utf-8")
            # Strip VTT formatting
            lines = []
            for line in raw.split("\n"):
                if line.strip() and not line.startswith("WEBVTT") and "-->" not in line and not line.strip().isdigit():
                    # Remove HTML tags
                    clean = re.sub(r"<[^>]+>", "", line).strip()
                    if clean:
                        lines.append(clean)
            vtt_file.unlink()  # cleanup
            return " ".join(lines), "en-auto"
    except Exception as e:
        print(f"  [warn] yt-dlp subtitle fallback error: {e}", file=sys.stderr)

    return "", "unavailable"


def main():
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

    parser = argparse.ArgumentParser(description="Fetch YouTube transcript for LLM Wiki")
    parser.add_argument("url", help="YouTube URL or video ID")
    parser.add_argument("--save", action="store_true", help="Save transcript to sources/transcripts/")
    args = parser.parse_args()

    video_id = extract_video_id(args.url)
    if not video_id:
        print(f"ERROR: Could not extract video ID from: {args.url}", file=sys.stderr)
        sys.exit(1)

    print(f"Processing video: {video_id}", file=sys.stderr)

    # Get metadata
    print("  Fetching metadata...", file=sys.stderr)
    metadata = get_video_metadata(video_id)

    # Get transcript
    print("  Fetching transcript...", file=sys.stderr)
    transcript, lang = get_transcript(video_id)

    if not transcript:
        print(f"  Primary transcript unavailable (lang={lang}), trying yt-dlp fallback...", file=sys.stderr)
        transcript, lang = get_transcript_ytdlp_fallback(video_id)

    if not transcript:
        print(f"  [warn] No transcript available for {video_id}", file=sys.stderr)
    else:
        print(f"  Transcript: {len(transcript)} chars, language={lang}", file=sys.stderr)

    # Save to disk if requested
    if args.save and transcript:
        save_path = TRANSCRIPTS_DIR / f"{video_id}.txt"
        save_path.write_text(transcript, encoding="utf-8")
        print(f"  Saved to {save_path}", file=sys.stderr)

    result = {
        **metadata,
        "transcript": transcript,
        "transcript_language": lang,
        "transcript_available": bool(transcript),
    }

    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
