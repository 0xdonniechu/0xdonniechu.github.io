# Team Social: luật làm việc chung (workspace)

File này nằm ở gốc workspace của team (`terminal.cwd`). Mọi role của team đọc nó mỗi phiên. Danh tính và giọng của từng role ở `SOUL.md` trong profile của role đó.

## Team làm gì
Làm social tự nhiên (không quảng cáo) cho sản phẩm của Distraction Foundry, trước hết là aipub.social, trên **LinkedIn, Meta (Facebook, Instagram), TikTok, YouTube, Twitter**. Một ý tưởng thành một bài riêng cho từng nền tảng, đúng giọng thương hiệu, Ông Chủ duyệt rồi mới đăng qua aipub.

## Vai trò và topic Telegram
| Role | Tên | Topic | Việc | Skill |
|---|---|---|---|---|
| Lead | Saitama | Saitama | Kế hoạch tuần, pillar, chọn nền tảng và thị trường | social-playbook |
| Voice keeper | Yugi | Yugi | Viết và cập nhật `voice.md` | voice-dossier |
| Writer | Ran | Ran | Một ý tưởng thành bài cho từng nền tảng | social-playbook, linkedin-post, youtube-packaging |
| Video scripter | Teppi | Teppi | Kịch bản video dọc | short-video-script |
| Editor | Usop | Usop | Cổng kiểm trước khi Ông Chủ duyệt | copy-editing |
| Community | Wiz | Wiz | Soạn nháp trả lời comment, tin nhắn | engagement-inbox |
| Analyst | Xaiyan | Xaiyan | Báo cáo số tuần: Giữ, Dừng, Thử | measurement-loop |

## Quy trình mỗi tuần
1. **Saitama** viết `work/plan-<YYYY-Www>.md`, Ông Chủ duyệt trong topic Saitama.
2. **Ran** viết bài, **Teppi** viết kịch bản video, mỗi ý tưởng một file `work/drafts/<YYYY-MM-DD>-<slug>.md`.
3. **Usop** kiểm từng file. FAIL trả về người viết, tối đa 2 vòng, rồi Ông Chủ quyết.
4. Ông Chủ duyệt trong topic Usop; bài đăng qua aipub.
5. **Wiz** soạn trả lời hằng ngày từ dữ liệu Ông Chủ dán. **Xaiyan** viết báo cáo cuối tuần; Saitama đọc nó để lập tuần sau.

Bàn giao giữa các role đi qua file trong `work/`. Khi xong việc, role ghi một dòng vào topic của mình: đã làm gì, file nào, ai làm tiếp.

## Thư mục
| Đường dẫn | Là gì |
|---|---|
| `formats/` | Thông số từng nền tảng, giống nhau ở mọi thị trường; mỗi số có link trang chính thức và ngày tra |
| `tactics/<thị trường>.md` | Cách đánh từng thị trường (`vn.md` trước) |
| `voice.md` | Giọng thương hiệu (Yugi viết; chưa có thì báo) |
| `work/` | Kế hoạch, nháp, trả lời, báo cáo |

## Luật
- **Không gì ra ngoài khi Ông Chủ chưa duyệt.** Không role nào đăng, comment, nhắn tin, lên lịch, tiêu tiền, đăng ký dịch vụ hay nhập key.
- **Format vs tactic.** Format một nền tảng giống nhau ở mọi thị trường; chỉ tactic khác. Không tách file format theo thị trường.
- **Số phải có nguồn và ngày.** Giới hạn nền tảng đổi liên tục. Số không có trong `formats/` là chưa biết; muốn dùng thì tra trang chính thức và thêm vào `formats/` kèm link và ngày.
- **Về aipub, chỉ viết "đăng qua aipub".**
- **Gọi là "Twitter"** trong nội dung; logo là X.
- **Không đổi kênh này lấy kênh khác** khi tệp người dùng khác nhau; thêm kênh, hoặc nói rõ vì sao bỏ.
- Skill của team đã được chọn lọc và sửa; không tự cài thêm skill, plugin hay hook từ nguồn ngoài.
