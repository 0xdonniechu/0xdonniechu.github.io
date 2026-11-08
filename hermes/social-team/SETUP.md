# Cài Team Social cho Hermes Agent

Hermes ơi, đây là hướng dẫn dựng **Team Social** của Distraction Foundry: 7 role, mỗi role là một **profile** Hermes riêng (SOUL.md, skill, toolset riêng), mỗi role nói chuyện trong **một topic** của một nhóm Telegram. Đọc hết file này, làm theo từng bước, dừng lại hỏi Ông Chủ ở các bước có ghi **[Ông Chủ]**.

Mọi file nằm dưới `BASE = https://0xdonniechu.github.io/hermes/social-team/`. Danh sách đầy đủ: `BASE/manifest.txt` (mỗi dòng một đường dẫn tương đối).

Tham chiếu tài liệu Hermes: Profiles, Running Many Gateways (multiplexing, `profile_routes`), Telegram (Group Chat Usage), Skills (`hermes skills install <url>`), Context Files (`AGENTS.md`), Toolsets Reference.

## 0. Kiểm trước
- `hermes --version` chạy được và gateway Telegram của profile mặc định đã chạy (đã có bot token, `TELEGRAM_ALLOWED_USERS` gồm Ông Chủ).
- Không ghi đè profile đã có: nếu trùng tên `sol echo remy kai iris mina tara`, dừng và hỏi Ông Chủ.

## 1. Tải workspace của team
Workspace là thư mục làm việc chung của 7 role: `~/marketing-team/social/`.
```bash
BASE=https://0xdonniechu.github.io/hermes/social-team
mkdir -p ~/marketing-team/social && cd ~/marketing-team/social
curl -fsSL $BASE/manifest.txt | grep '^workspace/' | while read p; do
  mkdir -p "$(dirname "${p#workspace/}")"; curl -fsSL "$BASE/$p" -o "${p#workspace/}"; done
mkdir -p work/drafts work/replies
```
Kết quả phải có: `AGENTS.md`, `formats/` (6 file), `tactics/` (2 file), `work/`.

## 2. Tạo 7 profile, mỗi profile một SOUL.md
```bash
for r in sol echo remy kai iris mina tara; do
  hermes profile create $r --description "Team Social: $r"   # profile trắng; KHÔNG dùng --clone (nó chép cả bộ nhớ và skill của profile mặc định)
  curl -fsSL $BASE/roles/$r/SOUL.md -o ~/.hermes/profiles/$r/SOUL.md
  hermes -p $r skills opt-out --remove --yes   # bỏ skill có sẵn của Hermes, chỉ giữ skill của team (bước 3)
done
```
**Model:** cho mỗi role dùng cùng model với profile mặc định: chép các khoá `model.*` và `fallback_providers` từ `~/.hermes/config.yaml` bằng `hermes -p <r> config set ...`, và chép **chỉ dòng key của nhà cung cấp model** từ `~/.hermes/.env` sang `~/.hermes/profiles/<r>/.env`. Không chép `TELEGRAM_*` hay token nhắn tin nào: cả 7 role dùng chung bot của profile mặc định (bước 5). Muốn role dùng model khác thì hỏi Ông Chủ.

## 3. Cài skill cho từng role
Mỗi skill là một `SKILL.md` kèm file tham chiếu; cài bằng URL:
```bash
S=$BASE/skills
hermes -p sol  skills install $S/social-playbook/SKILL.md
hermes -p echo skills install $S/voice-dossier/SKILL.md
hermes -p remy skills install $S/social-playbook/SKILL.md
hermes -p remy skills install $S/linkedin-post/SKILL.md
hermes -p remy skills install $S/youtube-packaging/SKILL.md
hermes -p kai  skills install $S/short-video-script/SKILL.md
hermes -p iris skills install $S/copy-editing/SKILL.md
hermes -p mina skills install $S/engagement-inbox/SKILL.md
hermes -p tara skills install $S/measurement-loop/SKILL.md
```
Kiểm: `hermes -p <r> skills list` chỉ còn đúng skill trên (và skill Ông Chủ tự thêm, nếu có); không còn skill nào đăng bài lên mạng xã hội. Nếu một skill thiếu file `references/...`, tải tay file đó từ `$S/<skill>/references/` vào thư mục skill. Giấy phép gốc ở `$S/LICENSES/` và `$S/THIRD_PARTY.md`.

## 4. Cấu hình từng profile
Với mỗi role (đường dẫn phải là đường dẫn tuyệt đối, không dùng `~`):
```bash
hermes -p <r> config set terminal.cwd "$HOME/marketing-team/social"   # để role đọc AGENTS.md, formats/, tactics/, voice.md, work/
hermes -p <r> config set agent.disabled_toolsets '[...]'                # danh sách theo bảng dưới
```

| Role | Cần | `agent.disabled_toolsets` |
|---|---|---|
| sol | file, web, search, skills, todo, memory, session_search, clarify, cronjob | `[browser, terminal, code_execution, delegation, image_gen, video_gen, computer_use, x_search, tts, connections]` |
| echo | file, skills, memory, clarify | `[browser, terminal, code_execution, delegation, cronjob, web, search, image_gen, video_gen, computer_use, x_search, tts, connections]` |
| remy | file, web, search, skills, memory, clarify | `[browser, terminal, code_execution, delegation, cronjob, image_gen, video_gen, computer_use, x_search, tts, connections]` |
| kai | file, web, search, skills, vision, memory, clarify | `[browser, terminal, code_execution, delegation, cronjob, image_gen, video_gen, computer_use, x_search, tts, connections]` |
| iris | file, web, search, skills, clarify | `[browser, terminal, code_execution, delegation, cronjob, image_gen, video_gen, computer_use, x_search, tts, memory, connections]` |
| mina | file, skills, memory, clarify | `[browser, terminal, code_execution, delegation, cronjob, web, search, image_gen, video_gen, computer_use, x_search, tts, connections]` |
| tara | file, skills, vision, code_execution, memory, clarify | `[browser, terminal, delegation, cronjob, web, search, image_gen, video_gen, computer_use, x_search, tts, connections]` |

Lý do: không role nào được tự đăng, điều khiển trình duyệt hay nối tài khoản ứng dụng (`connections`); chỉ Sol có `cronjob` (nhắc lập kế hoạch tuần); chỉ Tara có `code_execution` (tính trung vị từ CSV; Tara không được cài thư viện hay gọi mạng, chỉ đọc file Ông Chủ gửi); Kai và Tara có `vision` (đọc ảnh chụp). Iris không có `memory` để mỗi lần kiểm là kiểm mới.

## 5. Nhóm Telegram có topic, mỗi topic một role
1. **[Ông Chủ]** Tạo một supergroup Telegram (ví dụ "DF Social"), bật **Topics**, thêm bot của Hermes và cho bot làm **admin** (admin nhận mọi tin, không cần tắt privacy mode). Nếu không cho làm admin thì tắt privacy mode trong @BotFather, rồi **gỡ bot ra và thêm lại** vào nhóm.
2. **[Ông Chủ]** Tạo 7 topic tên: `Sol`, `Echo`, `Remy`, `Kai`, `Iris`, `Mina`, `Tara`. Topic General để lệnh hệ thống.
3. Lấy `chat_id` của nhóm và `thread_id` của từng topic (gửi một tin vào mỗi topic rồi đọc log gateway, hoặc link tin nhắn `t.me/c/<id>/<thread_id>/<msg>`). Không ghi các id này lên chỗ công khai.
4. Trong `~/.hermes/config.yaml` của **profile mặc định**:
```yaml
gateway:
  multiplex_profiles: true
  profile_routes:
    - {name: social-sol,  platform: telegram, chat_id: "<CHAT_ID>", thread_id: "<THREAD_SOL>",  profile: sol}
    - {name: social-echo, platform: telegram, chat_id: "<CHAT_ID>", thread_id: "<THREAD_ECHO>", profile: echo}
    - {name: social-remy, platform: telegram, chat_id: "<CHAT_ID>", thread_id: "<THREAD_REMY>", profile: remy}
    - {name: social-kai,  platform: telegram, chat_id: "<CHAT_ID>", thread_id: "<THREAD_KAI>",  profile: kai}
    - {name: social-iris, platform: telegram, chat_id: "<CHAT_ID>", thread_id: "<THREAD_IRIS>", profile: iris}
    - {name: social-mina, platform: telegram, chat_id: "<CHAT_ID>", thread_id: "<THREAD_MINA>", profile: mina}
    - {name: social-tara, platform: telegram, chat_id: "<CHAT_ID>", thread_id: "<THREAD_TARA>", profile: tara}
```
   Tin trong topic nào thì profile đó trả lời, với SOUL, skill, bộ nhớ và phiên riêng. Tin ngoài 7 topic (General) về profile mặc định.
5. Khởi động lại: `hermes gateway restart`. Cách khác nếu bản Hermes chưa có `profile_routes`: mỗi role một bot riêng (`<r> setup` nhập token, `<r> gateway start`) và mỗi topic chỉ thêm bot của role đó.

## 6. Kiểm sau khi cài
Trong từng topic, gửi: `Bạn là ai, việc của bạn là gì, bạn dùng skill nào?` Mỗi role phải trả lời đúng tên, đúng việc, đúng skill như bảng trong `AGENTS.md`. Rồi gửi vào topic Remy: `Đăng bài này lên Facebook giúp mình` — Remy phải từ chối đăng và nói chỉ soạn nháp.

## 7. Việc đầu tiên
**[Ông Chủ]** Dán 10–20 bài thật của brand vào topic **Echo** để Echo viết `voice.md`. Sau đó nhắn Sol: `Lập kế hoạch tuần này cho aipub, thị trường VN`.

## Cập nhật
Khi file trên `BASE` đổi: tải lại SOUL.md của role đó, cập nhật skill bằng `hermes -p <r> skills update` (hoặc `skills uninstall <tên>` rồi `skills install <url>`), tải lại workspace trừ `voice.md` và `work/`.
