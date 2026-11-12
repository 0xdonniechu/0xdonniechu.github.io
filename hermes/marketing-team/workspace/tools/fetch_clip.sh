#!/usr/bin/env bash
# Vail: turn one competitor clip into frames and text for a teardown. No login, no cookies, one video, at most 10 minutes.
# Usage (from the workspace root):
#   tools/fetch_clip.sh <public https link on YouTube (Shorts too), TikTok, Facebook or Instagram>
#   tools/fetch_clip.sh <file>   (a clip in work/intel/clips/, or one Hermes saved from the Telegram topic; at most 10 minutes)
# Writes work/intel/clips/<name>/:
#   clip.mp4         downloaded clip, at most 720p and 45 MB (link mode only)
#   info.info.json   title, channel, upload date, description, view count as the site shows them (link mode only)
#   sub.*.vtt        subtitles or auto-captions, when the site has them (vi, en; link mode only)
#   hook.jpg         first 3 seconds, 4 frames a second, timestamp on each frame
#   sheet-NN.jpg     the whole clip, 1 frame a second, 12 frames a sheet, timestamp on each frame
#   transcript.txt   speech by a local whisper, only when there are no subtitles and whisper is installed
# Read hook.jpg and sheet-*.jpg with vision_analyze; read the .vtt, transcript and info json as text.
set -euo pipefail
arg="${1:?usage: tools/fetch_clip.sh <public video link | work/intel/clips/<file>>}"
for t in ffmpeg ffprobe; do command -v "$t" >/dev/null || { echo "missing $t: ask Ông Chủ to install it (SETUP step 4)" >&2; exit 3; }; done
root="$(cd "$(dirname "$0")/.." && pwd)"
clips="$root/work/intel/clips"
mb=45; max_bytes=$((mb * 1024 * 1024))

if [ -f "$arg" ]; then
  # Local mode: a file already inside work/intel/clips/, or a video Hermes saved from the Telegram topic.
  path="$(realpath "$arg")"
  ok=no
  for allowed in "$clips" "$HOME/.hermes/cache/videos" "$HOME/.hermes/profiles/vail/cache/videos"; do
    case "$path" in "$(realpath -m "$allowed")"/*) ok=yes ;; esac
  done
  [ "$ok" = yes ] || { echo "refused: local files must be inside work/intel/clips/ or Hermes' video cache" >&2; exit 2; }
  dur=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$path" 2>/dev/null | cut -d. -f1 || true)
  [ -n "$dur" ] && [ "$dur" -le 600 ] || { echo "refused: not a readable video of 10 minutes or less" >&2; exit 4; }
  base="$(basename "$path")"; dir="$clips/file-$(printf '%s' "${base%.*}" | tr -c 'A-Za-z0-9_-' '_')"
  mkdir -p "$dir"
else
  case "$arg" in *[[:space:][:cntrl:]]*) echo "refused: the link contains spaces or control characters" >&2; exit 2 ;; esac
  host=$(printf '%s' "$arg" | sed -nE 's#^https://([^/?#:@]+)([/?#].*)?$#\1#p' | tr 'A-Z' 'a-z')
  case "$host" in
    youtube.com|www.youtube.com|m.youtube.com|youtu.be|\
    tiktok.com|www.tiktok.com|m.tiktok.com|vt.tiktok.com|vm.tiktok.com|\
    facebook.com|www.facebook.com|m.facebook.com|fb.watch|\
    instagram.com|www.instagram.com) ;;
    *) echo "refused: only https links on YouTube, TikTok, Facebook or Instagram, or a file in work/intel/clips/ (host: '${host:-none}')" >&2; exit 2 ;;
  esac
  # YouTube: keep only the video id, so a watch link that also names a playlist (&list=) is still one video.
  case "$host" in
    youtube.com|www.youtube.com|m.youtube.com|youtu.be)
      if [ "$host" = youtu.be ]; then pat='s#^https://[^/]+/()()([A-Za-z0-9_-]{11})([?&\#/].*)?$#\3#p'
      else pat='s#^https://[^/]+/(watch\?(.*&)?v=|shorts/|embed/|live/)([A-Za-z0-9_-]{11})([?&\#/].*)?$#\3#p'; fi
      vid=$(printf '%s' "$arg" | sed -nE "$pat")
      [ -n "$vid" ] || { echo "refused: not a single YouTube video link (channel, playlist or search pages are not taken)" >&2; exit 2; }
      arg="https://www.youtube.com/watch?v=$vid" ;;
  esac
  command -v yt-dlp >/dev/null || { echo "missing yt-dlp: ask Ông Chủ to install it (SETUP step 4)" >&2; exit 3; }
  mkdir -p "$clips"
  dir_tpl="$clips/%(extractor_key)s-%(id)s"
  # --use-extractors: only the single-video extractors of the four sites. Channels, playlists, user pages,
  #   Facebook's redirect links and the generic extractor are refused, so one link is one clip on one of the four sites.
  # --ignore-errors: a refused subtitle (HTTP 429) must not lose the clip; a missing clip is caught below.
  rc=0
  out=$(yt-dlp --ignore-config --no-cookies --no-playlist --max-downloads 1 \
    --use-extractors 'youtube,TikTok,vm.tiktok,facebook,facebook:reel,facebook:ads,Instagram' \
    --restrict-filenames --no-progress --quiet --no-warnings --ignore-errors \
    --match-filters 'duration<=600' --max-filesize "${mb}M" \
    -f 'b[height<=720][ext=mp4]/bv*[height<=720]+ba/b[height<=720]' --merge-output-format mp4 \
    --write-info-json --write-subs --write-auto-subs --sub-langs 'vi.*,en.*' --sub-format vtt \
    -o "$dir_tpl/clip.%(ext)s" -o "infojson:$dir_tpl/info" -o "subtitle:$dir_tpl/sub.%(ext)s" \
    --print after_move:filepath -- "$arg") || rc=$?
  path=$(printf '%s\n' "$out" | tail -1)
  [ -n "$path" ] && [ -f "$path" ] || { echo "no clip downloaded (yt-dlp exit $rc: private, login wall, not a single video, over 10 minutes or over $mb MB): write \"chưa xem clip\"" >&2; exit 4; }
  dir=$(dirname "$path")
  # A merged video+audio file can pass --max-filesize per part; check the result.
  if [ "$(stat -c %s "$path")" -gt "$max_bytes" ]; then rm -rf "$dir"; echo "clip over $mb MB, removed: write \"chưa xem clip\"" >&2; exit 4; fi
fi

stamp="drawtext=text='%{pts\:hms}':x=6:y=6:fontsize=18:fontcolor=white:box=1:boxcolor=black@0.6"
ffmpeg -loglevel error -y -t 3 -i "$path" -vf "fps=4,scale=320:-2,$stamp,tile=4x3" -frames:v 1 "$dir/hook.jpg"
ffmpeg -loglevel error -y -i "$path" -vf "fps=1,scale=320:-2,$stamp,tile=4x3" -fps_mode vfr "$dir/sheet-%02d.jpg"

# Speech: when the site gave no subtitles and a local whisper CLI is installed, transcribe on this machine
# (model large-v3-turbo, under an 8 GB memory cap when systemd-run exists). WHISPER=<path> and WHISPER_LANG=<code> override.
w="${WHISPER:-$(command -v whisper || true)}"
if ! ls "$dir"/sub.*.vtt >/dev/null 2>&1; then
  if [ -n "$w" ]; then
    run=(); command -v systemd-run >/dev/null && run=(systemd-run --user --scope --quiet -p MemoryMax=8G)
    name="$(basename "${path%.*}")"
    if "${run[@]}" "$w" "$path" --model large-v3-turbo --language "${WHISPER_LANG:-vi}" --condition_on_previous_text False \
         --output_format txt --output_dir "$dir" >/dev/null 2>&1; then
      mv "$dir/$name.txt" "$dir/transcript.txt"
    else echo "transcript failed: take speech from on-screen text only and say so" >&2; fi
  else echo "no subtitles and no whisper: take speech from on-screen text only and say so" >&2; fi
fi
echo "$dir"
ls -1 "$dir"
