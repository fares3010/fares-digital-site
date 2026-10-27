# fares.digital — portfolio site

A static, single-page site. There's no build step and no server code, so it runs on any static host.

```
index.html          the whole page (HTML + CSS + JS, English/Arabic switch)
404.html            "page not found" page
robots.txt          lets search engines index the site
sitemap.xml         one-page sitemap for fares.digital
assets/
  favicon.svg       browser-tab icon
  img/              portrait, campaign screenshots, creatives, video posters, og-image.jpg (link preview)
  video/            full showreel (720×1280, autoplays muted on scroll) + 5 case-study reels + English marketing reel (540×960 MP4)
```

## Try it on your computer
Open `index.html` in a browser. To test it the way a host serves it, run this in the folder:

```
python -m http.server 8000
```

Then visit http://localhost:8000.

## Deploy to fares.digital

Upload the **contents** of this folder (not the folder itself) so `index.html` sits at the web root.

**Netlify (simplest):** app.netlify.com → Add new site → Deploy manually → drag the folder in. Then go to Domain settings → Add domain → `fares.digital`, and follow the DNS records it shows.

**Vercel:** vercel.com → Add New → Project → upload the folder (or push it to a GitHub repo and import it). Framework preset: "Other". Then add `fares.digital` under Domains.

**Cloudflare Pages:** dash.cloudflare.com → Workers & Pages → Create → Pages → Upload assets → drop the folder. Then go to Custom domains → `fares.digital`.

**cPanel / shared hosting:** File Manager → `public_html` → upload the zip → Extract. Make sure `index.html` ends up directly inside `public_html`.

**GitHub Pages:** push the files to a repo → Settings → Pages → deploy from the `main` branch, root folder. Then add `fares.digital` as the custom domain.

After the domain is connected, turn on HTTPS. Netlify, Vercel, Cloudflare and GitHub Pages do this automatically.

## Editing
- Contact details are in the `#contact` section of `index.html`, and the WhatsApp link is `https://wa.me/201062792254`.
- English text sits in the HTML. Arabic text is in the `AR = { ... }` object near the end of `index.html`, with matching keys (`data-i18n="..."`).
- To replace a video, keep the same file name in `assets/video/`, or update the `src` and `poster` in the Showreel or Reels section.
- Fonts load from Google Fonts. Everything else is self-hosted.
