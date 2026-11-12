# Cài Marketing Team cho Hermes Agent

Hermes ơi, đây là hướng dẫn dựng **Marketing Team** của Distraction Foundry: 9 role (7 role của Team Social, Zoro là Designer và Vail là Trinh sát đối thủ, hai role dùng chung cho mọi team), mỗi role là một **profile** Hermes riêng (SOUL.md, skill, toolset riêng), mỗi role nói chuyện trong **một topic** của một nhóm Telegram. Đọc hết file này, làm theo từng bước, dừng lại hỏi Ông Chủ ở các bước có ghi **[Ông Chủ]**.

Mọi file nằm dưới `BASE = https://0xdonniechu.github.io/hermes/marketing-team/`. Danh sách đầy đủ: `BASE/manifest.txt` (mỗi dòng một đường dẫn tương đối).

Tham chiếu tài liệu Hermes: Profiles, Running Many Gateways (multiplexing, `profile_routes`), Telegram (Group Chat Usage), Skills (`hermes skills install <url>`), Context Files (`AGENTS.md`), Toolsets Reference.

## 0. Kiểm trước
- `hermes --version` chạy được và gateway Telegram của profile mặc định đã chạy (đã có bot token, `TELEGRAM_ALLOWED_USERS` gồm Ông Chủ).
- Không ghi đè profile đã có: nếu trùng tên `saitama yugi ran teppi usop wiz xaiyan zoro vail`, dừng và hỏi Ông Chủ.

## 1. Tải workspace của team
Workspace là thư mục làm việc chung của 9 role: `~/marketing-team/social/` (thư mục của Team Social; Zoro và Vail làm việc ở đây, Zoro vì cần `formats/` và `voice.md`, Vail vì ghi vào `work/intel/`).
```bash
BASE=https://0xdonniechu.github.io/hermes/marketing-team
mkdir -p ~/marketing-team/social && cd ~/marketing-team/social
curl -fsSL $BASE/manifest.txt | grep '^workspace/' | while read p; do
  mkdir -p "$(dirname "${p#workspace/}")"; curl -fsSL "$BASE/$p" -o "${p#workspace/}"; done
mkdir -p work/drafts work/replies work/banners work/emails work/intel/clips
chmod +x tools/*.sh
```
Kết quả phải có: `AGENTS.md`, `formats/` (6 file), `tactics/` (2 file), `tools/` (3 file), `work/`. Kiểm script: `python3 tools/test_readout_stats.py` báo `OK`.

## 2. Tạo 9 profile, mỗi profile một SOUL.md
```bash
for r in saitama yugi ran teppi usop wiz xaiyan zoro vail; do
  hermes profile create $r --description "Marketing Team: $r"   # profile trắng; KHÔNG dùng --clone (nó chép cả bộ nhớ và skill của profile mặc định)
  curl -fsSL $BASE/roles/$r/SOUL.md -o ~/.hermes/profiles/$r/SOUL.md
  hermes -p $r skills opt-out --remove --yes   # bỏ skill có sẵn của Hermes, chỉ giữ skill của team (bước 3)
done
```
**Model:** cho mỗi role dùng cùng model với profile mặc định: chép các khoá `model.*` và `fallback_providers` từ `~/.hermes/config.yaml` bằng `hermes -p <r> config set ...`, và chép **chỉ dòng key của nhà cung cấp model** từ `~/.hermes/.env` sang `~/.hermes/profiles/<r>/.env`. Không chép `TELEGRAM_*` hay token nhắn tin nào: cả 9 role dùng chung bot của profile mặc định (bước 5). Muốn role dùng model khác thì hỏi Ông Chủ.

## 3. Cài skill cho từng role
Mỗi skill là một `SKILL.md` kèm file tham chiếu; cài bằng URL:
```bash
S=$BASE/skills
hermes -p saitama  skills install $S/social-playbook/SKILL.md
hermes -p yugi skills install $S/voice-dossier/SKILL.md
hermes -p ran skills install $S/social-playbook/SKILL.md
hermes -p ran skills install $S/linkedin-post/SKILL.md
hermes -p ran skills install $S/youtube-packaging/SKILL.md
hermes -p teppi  skills install $S/short-video-script/SKILL.md
hermes -p usop skills install $S/copy-editing/SKILL.md
hermes -p wiz skills install $S/engagement-inbox/SKILL.md
hermes -p xaiyan skills install $S/measurement-loop/SKILL.md
# Zoro: 4 skill; impeccable có thêm `reference/`. Cài SKILL.md rồi tải phần còn lại theo manifest vào thư mục skill của profile.
for s in html-banner-design email-newsletter-design bento-carousel-design-v3 impeccable; do
  hermes -p zoro skills install $S/$s/SKILL.md
  curl -fsSL $BASE/manifest.txt | grep "^skills/$s/" | while read p; do
    f="${p#skills/$s/}"; [ "$f" = SKILL.md ] && continue
    mkdir -p "$HOME/.hermes/profiles/zoro/skills/$s/$(dirname "$f")"; curl -fsSL "$BASE/$p" -o "$HOME/.hermes/profiles/zoro/skills/$s/$f"; done
done
# Vail: 1 skill, `ad-teardown` (chỉ có SKILL.md)
hermes -p vail skills install $S/ad-teardown/SKILL.md
```
Thư mục cài `~/.hermes/profiles/zoro/skills/<tên>/` ở vòng lặp trên chưa được kiểm trên bản Hermes mới; xem `hermes -p zoro skills list` rồi chép file phụ vào đúng thư mục skill nó báo.
Kiểm: `hermes -p <r> skills list` chỉ còn đúng skill trên (và skill Ông Chủ tự thêm, nếu có); không còn skill nào đăng bài lên mạng xã hội. Nếu một skill thiếu file `references/...`, tải tay file đó từ `$S/<skill>/references/` vào thư mục skill. Giấy phép gốc ở `$S/LICENSES/`; nguồn và chỗ đã sửa ở `$S/THIRD_PARTY.md` (Team Social) và `$S/THIRD_PARTY-design.md` (Zoro).

## 4. Cấu hình từng profile
Với mỗi role (đường dẫn phải là đường dẫn tuyệt đối, không dùng `~`):
```bash
hermes -p <r> config set terminal.cwd "$HOME/marketing-team/social"   # để role đọc AGENTS.md, formats/, tactics/, voice.md, work/
hermes -p <r> config set agent.disabled_toolsets '[...]'                # danh sách theo bảng dưới
```

| Role | Cần | `agent.disabled_toolsets` |
|---|---|---|
| saitama | file, web, search, skills, todo, memory, session_search, clarify, cronjob | `[browser, terminal, code_execution, delegation, image_gen, video_gen, computer_use, x_search, tts, connections]` |
| yugi | file, skills, memory, clarify | `[browser, terminal, code_execution, delegation, cronjob, web, search, image_gen, video_gen, computer_use, x_search, tts, connections]` |
| ran | file, web, search, skills, memory, clarify | `[browser, terminal, code_execution, delegation, cronjob, image_gen, video_gen, computer_use, x_search, tts, connections]` |
| teppi | file, web, search, skills, vision, memory, clarify | `[browser, terminal, code_execution, delegation, cronjob, image_gen, video_gen, computer_use, x_search, tts, connections]` |
| usop | file, web, search, skills, clarify | `[browser, terminal, code_execution, delegation, cronjob, image_gen, video_gen, computer_use, x_search, tts, memory, connections]` |
| wiz | file, skills, memory, clarify | `[browser, terminal, code_execution, delegation, cronjob, web, search, image_gen, video_gen, computer_use, x_search, tts, connections]` |
| xaiyan | file, skills, vision, code_execution, memory, clarify | `[browser, terminal, delegation, cronjob, web, search, image_gen, video_gen, computer_use, x_search, tts, connections]` |
| zoro | file, web, search, skills, vision, terminal, code_execution, memory, clarify | `[browser, delegation, cronjob, image_gen, video_gen, computer_use, x_search, tts, connections]` |
| vail | file, web, search, skills, vision, terminal, memory, clarify | `[browser, code_execution, delegation, cronjob, image_gen, video_gen, computer_use, x_search, tts, connections]` |

Lý do: không role nào được tự đăng, điều khiển trình duyệt hay nối tài khoản ứng dụng (`connections`); chỉ Saitama có `cronjob` (nhắc lập kế hoạch tuần); chỉ Xaiyan và Zoro có `code_execution` (Xaiyan chạy `tools/readout_stats.py` để tính trung vị và tỉ lệ từ CSV, không được cài thư viện hay gọi mạng, chỉ đọc file Ông Chủ gửi; Zoro xem dưới); Teppi, Xaiyan, Zoro và Vail có `vision` (đọc ảnh chụp); không role nào bật `video`. Usop không có `memory` để mỗi lần kiểm là kiểm mới. Zoro giữ `terminal`, cùng `code_execution` và `vision` (Ông Chủ xác nhận 2026-11-12) để chạy Playwright trên file HTML local, render PNG và đo kích thước; SOUL của Zoro cấm dùng chúng để gọi mạng, gửi, tải code hay cài gói. Không role nào điều khiển trình duyệt trên web hay tài khoản (`browser` tắt); Playwright của Zoro chỉ mở file local. Zoro cần Playwright và Chromium trên máy: **[Ông Chủ]** cài một lần, Zoro không tự cài.

Vail đọc trang công khai bằng `web` và `search`, không có `browser`: không đăng nhập, không bấm trên trang nào. Vail giữ `terminal` (Ông Chủ quyết 2026-11-12) chỉ để chạy `tools/fetch_clip.sh`: script tải một clip công khai bằng yt-dlp (chỉ link https tới một video trên YouTube, TikTok, Facebook, Instagram; link kênh, playlist, link chuyển hướng bị từ chối; không cookie, không đăng nhập; tối đa 10 phút, 720p, 45 MB) hoặc nhận file tối đa 10 phút trong `work/intel/clips/` hay trong bộ nhớ đệm video của Hermes (clip gửi vào topic; đường đi này chưa kiểm trên bản Hermes thật), rồi cắt khung hình có giờ để Vail đọc bằng `vision`, kèm phụ đề hoặc lời do whisper chép trên máy. SOUL của Vail cấm dùng terminal cho việc khác. Không bật toolset `video`: công cụ `video_analyze` gửi video theo kiểu cổng model của team bỏ qua, model trả lời là không thấy video (thử 2026-11-12).

**[Ông Chủ]** cài một lần trên máy chạy Hermes: `yt-dlp`, `ffmpeg`, `deno` (yt-dlp cần nó để đọc đủ định dạng YouTube) và, nếu muốn chép lời cho clip không có phụ đề, lệnh `whisper` (openai-whisper) với model `large-v3-turbo` đã tải sẵn. Vail không tự cài. Kiểm: trong topic Vail gửi một link YouTube Shorts công khai của đối thủ; Vail phải chạy script, đọc `hook.jpg` và viết teardown có bảng cảnh theo giờ. TikTok và Reels chưa được thử qua script; lỗi thì Vail ghi "chưa xem clip".

## 5. Nhóm Telegram có topic, mỗi topic một role
Nhóm tên **Marketing-Team**; route tên `marketing-<role>`.
1. **[Ông Chủ]** Tạo một supergroup Telegram (ví dụ "DF Marketing"), bật **Topics**, thêm bot của Hermes và cho bot làm **admin** (admin nhận mọi tin, không cần tắt privacy mode). Nếu không cho làm admin thì tắt privacy mode trong @BotFather, rồi **gỡ bot ra và thêm lại** vào nhóm.
2. **[Ông Chủ]** Tạo 9 topic tên: `Saitama`, `Yugi`, `Ran`, `Teppi`, `Usop`, `Wiz`, `Xaiyan`, `Zoro`, `Vail`. Topic General để lệnh hệ thống.
3. Lấy `chat_id` của nhóm và `thread_id` của từng topic (gửi một tin vào mỗi topic rồi đọc log gateway, hoặc link tin nhắn `t.me/c/<id>/<thread_id>/<msg>`). Không ghi các id này lên chỗ công khai.
4. Trong `~/.hermes/config.yaml` của **profile mặc định**:
```yaml
gateway:
  multiplex_profiles: true
  profile_routes:
    - {name: marketing-saitama,  platform: telegram, chat_id: "<CHAT_ID>", thread_id: "<THREAD_SAITAMA>",  profile: saitama}
    - {name: marketing-yugi, platform: telegram, chat_id: "<CHAT_ID>", thread_id: "<THREAD_YUGI>", profile: yugi}
    - {name: marketing-ran, platform: telegram, chat_id: "<CHAT_ID>", thread_id: "<THREAD_RAN>", profile: ran}
    - {name: marketing-teppi,  platform: telegram, chat_id: "<CHAT_ID>", thread_id: "<THREAD_TEPPI>",  profile: teppi}
    - {name: marketing-usop, platform: telegram, chat_id: "<CHAT_ID>", thread_id: "<THREAD_USOP>", profile: usop}
    - {name: marketing-wiz, platform: telegram, chat_id: "<CHAT_ID>", thread_id: "<THREAD_WIZ>", profile: wiz}
    - {name: marketing-xaiyan, platform: telegram, chat_id: "<CHAT_ID>", thread_id: "<THREAD_XAIYAN>", profile: xaiyan}
    - {name: marketing-zoro, platform: telegram, chat_id: "<CHAT_ID>", thread_id: "<THREAD_ZORO>", profile: zoro}
    - {name: marketing-vail, platform: telegram, chat_id: "<CHAT_ID>", thread_id: "<THREAD_VAIL>", profile: vail}
```
   Nếu nhóm dùng bot riêng thay vì bot của profile mặc định: đặt `TELEGRAM_BOT_TOKEN` của bot đó trong `.env` của một profile (ví dụ saitama) và thêm `bot_profile: saitama` vào mỗi route.
   Tin trong topic nào thì profile đó trả lời, với SOUL, skill, bộ nhớ và phiên riêng. Tin ngoài 9 topic (General) về profile mặc định.
5. Khởi động lại: `hermes gateway restart`. Cách khác nếu bản Hermes chưa có `profile_routes`: mỗi role một bot riêng (`<r> setup` nhập token, `<r> gateway start`) và mỗi topic chỉ thêm bot của role đó.

## 6. Kiểm sau khi cài
Trong từng topic (9 topic), gửi: `Bạn là ai, việc của bạn là gì, bạn dùng skill nào?` Mỗi role phải trả lời đúng tên, đúng việc, đúng skill như bảng trong `AGENTS.md`. Với Zoro, thử thêm: `Thiết kế giúp mình một banner 1:1 và gửi luôn lên Instagram` — Zoro phải từ chối gửi và chỉ xuất file. Với Vail, thử: `Đăng nhập Facebook xem quảng cáo giúp mình` — Vail phải từ chối đăng nhập và đề nghị dùng Meta Ad Library công khai. Rồi gửi vào topic Ran: `Đăng bài này lên Facebook giúp mình` — Ran phải từ chối đăng và nói chỉ soạn nháp.

## 7. Việc đầu tiên
**[Ông Chủ]** Dán 10–20 bài thật của brand vào topic **Yugi** để Yugi viết `voice.md`. Sau đó nhắn Saitama: `Lập kế hoạch tuần này cho aipub, thị trường VN`.

## Cập nhật
Khi file trên `BASE` đổi: tải lại SOUL.md của role đó, cập nhật skill bằng `hermes -p <r> skills update` (hoặc `skills uninstall <tên>` rồi `skills install <url>`), tải lại workspace trừ `voice.md` và `work/`.

**Tài liệu campaign do Ông Chủ giao** (plan campaign `work/plan-c*.md`, ghi chú tham khảo `work/ref-*.md`) cũng nằm trên `BASE`. Tải về khi Ông Chủ báo có tài liệu mới; lệnh này chỉ ghi đè hai loại file đó, không đụng nháp, trả lời hay báo cáo của team:
```bash
cd ~/marketing-team/social
curl -fsSL $BASE/manifest.txt | grep -E '^workspace/work/(plan-c|ref-)' | while read p; do
  curl -fsSL "$BASE/$p" -o "${p#workspace/}"; done
```
Rồi nhắn Saitama tên file mới để giao việc.
