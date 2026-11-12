---
name: email-newsletter-design
description: "Use when designing responsive HTML emails or newsletters."
version: 1.0.0
author: Donnie & Hermes
license: MIT
metadata:
  hermes:
    tags: [email-design, newsletter, html-email, mjml, bento-email, deliverability, responsive-email]
---

# Responsive Email & Newsletter Design System

## When to Use

- Use when designing campaign newsletters, product announcements, onboarding emails, or lifecycle communications.
- Use when generating production-grade, responsive HTML emails that render consistently across Gmail, Apple Mail, and Outlook.
- Use when auditing email markup for spam triggers, Gmail message clipping (< 102 KB), or mobile responsiveness.

## 1. Core Principles

- **60/40 Text-to-Image Ratio**: Always maintain at least 60% real HTML text to 40% visual assets. Heavy single-image emails trigger spam filters and get routed to Gmail Promotions or Junk.
- **Client-Resilient Table Architecture**: Modern flexbox/grid is unsupported in desktop Outlook (which uses Word's rendering engine). Build using nested HTML `<table>` elements with inline CSS, or compile from MJML.
- **Strict 102 KB Gmail Ceiling**: Gmail web/mobile clips any email whose raw HTML exceeds 102 KB (`[Message clipped] View entire message`), breaking tracking pixels, footers, and unsubscribe links. Minify inline CSS and keep templates under 85 KB.
- **Brand Kit Extraction**: Derive design tokens directly from the brand website:
  - Primary & Accent colors (contrast ratio >= 4.5:1 against card backgrounds)
  - System font stack fallbacks for web fonts (e.g. `'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif`)
  - Dark mode support via `@media (prefers-color-scheme: dark)`

## 2. Modular Bento Email Structure

An effective newsletter uses a predictable 4-part modular flow:

```
┌──────────────────────────────────────────┐
│ 1. PREHEADER & BRAND HEADER (600px Max)  │  Logo + View in browser
├──────────────────────────────────────────┤
│ 2. HERO BLOCK (Single High-Impact Value) │  Bold claim + Hook + Hero graphic
├──────────────────────────────────────────┤
│ 3. BENTO CONTENT CARDS (Modular 1x2/2x2) │  2–3 distinct value/proof modules
├──────────────────────────────────────────┤
│ 4. SINGLE PRIMARY CTA                    │  Bulletproof button (VML for Outlook)
├──────────────────────────────────────────┤
│ 5. COMPLIANCE & REPUTATION FOOTER        │  Physical address + 1-click Unsub
└──────────────────────────────────────────┘
```

## 3. Production HTML Boilerplate

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="vi">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <meta name="x-apple-disable-message-reformatting" />
  <title>{{subject}}</title>
  <!--[if mso]>
  <noscript>
    <xml>
      <o:OfficeDocumentSettings>
        <o:PixelsPerInch>96</o:PixelsPerInch>
      </o:OfficeDocumentSettings>
    </xml>
  </noscript>
  <![endif]-->
  <style type="text/css">
    body, table, td, a { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; }
    table, td { mso-table-lspace: 0pt; mso-table-rspace: 0pt; }
    img { -ms-interpolation-mode: bicubic; border: 0; outline: none; text-decoration: none; display: block; }
    @media only screen and (max-width: 600px) {
      .container { width: 100% !important; max-width: 100% !important; }
      .stack-column { display: block !important; width: 100% !important; max-width: 100% !important; }
      .p-mobile { padding-left: 20px !important; padding-right: 20px !important; }
    }
  </style>
</head>
<body style="margin: 0; padding: 0; background-color: #0A0A0C; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <!-- Preview Text (Hidden) -->
  <div style="display: none; font-size: 1px; color: #0A0A0C; line-height: 1px; max-height: 0px; max-width: 0px; opacity: 0; overflow: hidden;">
    {{preview_text}} &#847; &#847; &#847; &#847; &#847;
  </div>

  <!-- Outer Canvas Table -->
  <table border="0" cellpadding="0" cellspacing="0" width="100%" style="background-color: #0A0A0C;">
    <tr>
      <td align="center" style="padding: 24px 0;">
        <!-- Inner Container (Standard 600px) -->
        <table border="0" cellpadding="0" cellspacing="0" width="600" class="container" style="background-color: #12131A; border: 1px solid #262A3B; border-radius: 12px; overflow: hidden;">
          <!-- Hero Section -->
          <tr>
            <td style="padding: 40px 32px 24px 32px; color: #FFFFFF;" class="p-mobile">
              <h1 style="margin: 0 0 16px 0; font-size: 26px; line-height: 34px; font-weight: 700; color: #FFFFFF;">
                {{headline}}
              </h1>
              <p style="margin: 0; font-size: 16px; line-height: 24px; color: #C4CAD4;">
                {{lead_paragraph}}
              </p>
            </td>
          </tr>

          <!-- Bulletproof CTA Button -->
          <tr>
            <td align="center" style="padding: 16px 32px 32px 32px;" class="p-mobile">
              <!--[if mso]>
              <v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="{{cta_url}}" style="height:48px;v-text-anchor:middle;width:240px;" arcsize="16%" stroke="f" fillcolor="#00F5A0">
                <w:anchorlock/>
                <center style="color:#0A0A0C;font-family:sans-serif;font-size:16px;font-weight:bold;">{{cta_text}}</center>
              </v:roundrect>
              <![endif]-->
              <a href="{{cta_url}}" style="background-color: #00F5A0; border-radius: 8px; color: #0A0A0C; display: inline-block; font-size: 16px; font-weight: 700; line-height: 48px; text-align: center; text-decoration: none; width: 240px; -webkit-text-size-adjust: none; mso-hide: all;">{{cta_text}}</a>
            </td>
          </tr>

          <!-- Footer (CAN-SPAM / Legal) -->
          <tr>
            <td style="padding: 24px 32px; background-color: #0D0E15; border-top: 1px solid #262A3B; text-align: center; font-size: 12px; line-height: 18px; color: #7B828E;" class="p-mobile">
              <p style="margin: 0 0 8px 0;">{{company_name}} &bull; {{physical_address}}</p>
              <p style="margin: 0;">
                <a href="{{unsubscribe_url}}" style="color: #7B828E; text-decoration: underline;">Hủy đăng ký (Unsubscribe)</a>
              </p>
            </td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
</body>
</html>
```

## 4. Verification & Testing Checklist

- [ ] **Dual-Viewport Render**: Capture preview PNGs for both Desktop (600px width) and Mobile (375px width) using Playwright.
- [ ] **File Size Audit**: Raw HTML file must be < 85 KB (well below the 102 KB Gmail clipping boundary).
- [ ] **Image Tags**: Every `<img>` tag has explicit `alt`, `width`, `height`, and `style="display:block; border:0;"`.
- [ ] **Compliance Anchor**: Footer contains physical mailing address and functional `{{unsubscribe_url}}`.
- [ ] **Contrast Check**: Primary button and body copy text exceed WCAG AA contrast (4.5:1).
