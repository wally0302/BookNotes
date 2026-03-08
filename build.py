import os

def generate_html(title, links, demos=None, back_link=None):
    links_html = ""
    if links:
        links_list = "\n".join([f'            <li><a href="{link}/index.html" class="block p-4 bg-white rounded-lg shadow hover:shadow-md transition-shadow text-lg text-gray-800 font-medium border-l-4 border-blue-500">{name}</a></li>' for name, link in links])
        links_html = f"""        <h2 class="text-2xl font-bold text-gray-800 mb-6 border-b border-gray-200 pb-2">📝 閱讀筆記</h2>
        <ul class="space-y-4">
{links_list}
        </ul>"""
    
    demos_html = ""
    if demos:
        demos_list = "\n".join([f'            <li><a href="{link}/index.html" class="block p-5 bg-white rounded-xl shadow border border-amber-200 hover:shadow-md hover:border-amber-400 hover:-translate-y-1 transition-all text-lg text-amber-900 font-medium flex justify-between items-center"><span><span class="mr-3 text-2xl">✨</span>{name}</span><span class="text-sm px-3 py-1 bg-amber-100 text-amber-800 rounded-full font-bold shadow-sm">互動體驗</span></a></li>' for name, link in demos])
        demos_html = f"""
        <div class="mt-12">
            <h2 class="text-2xl font-bold text-gray-800 mb-6 flex items-center">
                <span class="bg-amber-100 text-amber-600 p-2 rounded-lg mr-3 shadow-sm">💡</span>
                互動式範例 (Demos)
            </h2>
            <ul class="grid grid-cols-1 md:grid-cols-2 gap-5">
{demos_list}
            </ul>
        </div>"""
    
    back_btn = f'<a href="../index.html" class="inline-block mb-6 text-blue-600 hover:text-blue-800 font-medium font-bold transition-colors">← 返回書櫃</a>' if back_link else ''
    
    return f"""<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-slate-50 min-h-screen p-8 font-sans">
    <div class="max-w-4xl mx-auto">
        {back_btn}
        <h1 class="text-4xl font-extrabold text-gray-900 mb-10 tracking-tight">{title}</h1>
{links_html}{demos_html}
    </div>
</body>
</html>"""

def generate_readme(books):
    lines = [
        "# 📚 我的閱讀筆記櫃",
        "",
        "這裡存放了我的各種書籍閱讀筆記與互動式網站。",
        "",
        "## 書籍列表",
        ""
    ]
    for book in books:
        lines.append(f"- [{book}](./{book}/index.html)")
    return "\n".join(lines)

def main():
    base_dir = "/Users/oaowally123/Downloads/Read_notes"
    ignore_dirs = {".git", ".github"}
    books = []
    
    for item in sorted(os.listdir(base_dir)):
        item_path = os.path.join(base_dir, item)
        if os.path.isdir(item_path) and item not in ignore_dirs and not item.startswith('.'):
            notes = []
            demos = []
            
            for sub_item in sorted(os.listdir(item_path)):
                sub_item_path = os.path.join(item_path, sub_item)
                if os.path.isdir(sub_item_path) and os.path.exists(os.path.join(sub_item_path, "index.html")):
                    if sub_item.lower().startswith("demo"):
                        demos.append((sub_item, sub_item))
                    else:
                        notes.append((sub_item, sub_item))
            
            if notes or demos:
                books.append(item)
                book_html = generate_html(f"📖 {item}", notes, demos=demos, back_link=True)
                with open(os.path.join(item_path, "index.html"), "w", encoding="utf-8") as f:
                    f.write(book_html)
    
    root_links = [(book, book) for book in books]
    root_html = generate_html("📚 我的閱讀筆記櫃", root_links)
    with open(os.path.join(base_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(root_html)
        
    readme_md = generate_readme(books)
    with open(os.path.join(base_dir, "README.md"), "w", encoding="utf-8") as f:
        f.write(readme_md)
        
    print("✅ 成功產生所有目錄的 index.html 與 README.md！ (包含 Demo 特殊排版)")

if __name__ == "__main__":
    main()
