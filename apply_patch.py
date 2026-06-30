import re
with open('translator.py', 'r', encoding='utf-8') as f:
    content = f.read()
content = re.sub(r'\s+self\.swap_btn = wx\.Button\(self\.panel, label=\'S&wap\'\)\s+self\.swap_btn\.SetToolTip\(\'Swap source and target languages \(Shortcut: Ctrl\+W\)\'\)\s+self\.swap_btn\.Bind\(wx\.EVT_BUTTON, self\.on_swap\)\s+extra_btn_sizer\.Add\(self\.swap_btn\)\s+extra_btn_sizer\.AddStretchSpacer\(1\)\s+self\.mainsizer\.Add\(extra_btn_sizer, 0, wx\.ALL \| wx\.EXPAND, 5\)', '', content)
content = content.replace("            (wx.ACCEL_CTRL, ord('W'), self.swap_btn.GetId()),", "")
content = re.sub(r'\n\s+def on_swap\(self, event\):.*?self\.input_text\.SetFocus\(\)\n', '\n', content, flags=re.DOTALL)

with open('translator.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Patch applied successfully! Swap button removed.")