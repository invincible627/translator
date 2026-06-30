import wx
from deep_translator import GoogleTranslator
import os

class TranslationFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title='Translator: Created by Amir Mohammad Tavallali Nia!', size=(800, 600))
        self.panel = wx.Panel(self)
        self.mainsizer = wx.BoxSizer(wx.VERTICAL)
        self.mainsizer.Add(wx.StaticText(self.panel, label='&Text to translate:'), 
                          0, wx.ALL | wx.ALIGN_LEFT, 5)
        self.input_text = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE | wx.TE_PROCESS_ENTER, 
                                      size=(-1, 150))
        self.input_text.SetToolTip('Enter the text you want to translate here')
        self.input_text.SetFocus()
        self.mainsizer.Add(self.input_text, 1, wx.ALL | wx.EXPAND, 5)
        lang_sizer = wx.BoxSizer(wx.HORIZONTAL)
        lang_sizer.Add(wx.StaticText(self.panel, label='Target &Language:'), 
                      0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)
        self.languages = [
            'Afrikaans (Afrikaans) - (af)',
            'Albanian (Shqip) - (sq)',
            'Amharic (አማርኛ) - (am)',
            'Arabic (العربية) - (ar)',
            'Armenian (Հայերեն) - (hy)',
            'Azerbaijani (Azərbaycanca) - (az)',
            'Basque (Euskara) - (eu)',
            'Belarusian (Беларуская) - (be)',
            'Bengali (বাংলা) - (bn)',
            'Bosnian (Bosanski) - (bs)',
            'Bulgarian (Български) - (bg)',
            'Burmese (မြန်မာစာ) - (my)',
            'Catalan (Català) - (ca)',
            'Cebuano (Cebuano) - (ceb)',
            'Chichewa (Chichewa) - (ny)',
            'Chinese Simplified (简体中文) - (zh-CN)',
            'Chinese Traditional (繁體中文) - (zh-TW)',
            'Corsican (Corsu) - (co)',
            'Croatian (Hrvatski) - (hr)',
            'Czech (Čeština) - (cs)',
            'Danish (Dansk) - (da)',
            'Dari (دری) - (prs)',
            'Dutch (Nederlands) - (nl)',
            'English (English) - (en)',
            'Esperanto (Esperanto) - (eo)',
            'Estonian (Eesti) - (et)',
            'Finnish (Suomi) - (fi)',
            'French (Français) - (fr)',
            'Galician (Galego) - (gl)',
            'Georgian (ქართული) - (ka)',
            'German (Deutsch) - (de)',
            'Greek (Ελληνικά) - (el)',
            'Guarani (Avañe\'ẽ) - (gn)',
            'Gujarati (ગુજરાતી) - (gu)',
            'Haitian Creole (Kreyòl Ayisyen) - (ht)',
            'Hausa (Hausa) - (ha)',
            'Hawaiian (ʻŌlelo Hawaiʻi) - (haw)',
            'Hebrew (עברית) - (he)',
            'Hindi (हिन्दी) - (hi)',
            'Hmong (Hmoob) - (hmn)',
            'Hungarian (Magyar) - (hu)',
            'Icelandic (Íslenska) - (is)',
            'Igbo (Igbo) - (ig)',
            'Indonesian (Bahasa Indonesia) - (id)',
            'Irish (Gaeilge) - (ga)',
            'Italian (Italiano) - (it)',
            'Japanese (日本語) - (ja)',
            'Javanese (Basa Jawa) - (jw)',
            'Kannada (ಕನ್ನಡ) - (kn)',
            'Kazakh (Қазақша) - (kk)',
            'Khmer (ភាសាខ្មែរ) - (km)',
            'Kinyarwanda (Ikinyarwanda) - (rw)',
            'Korean (한국어) - (ko)',
            'Kurdish (Kurdî) - (ku)',
            'Kyrgyz (Кыргызча) - (ky)',
            'Lao (ລາວ) - (lo)',
            'Latin (Latina) - (la)',
            'Latvian (Latviešu) - (lv)',
            'Lithuanian (Lietuvių) - (lt)',
            'Luxembourgish (Lëtzebuergesch) - (lb)',
            'Macedonian (Македонски) - (mk)',
            'Malagasy (Malagasy) - (mg)',
            'Malay (Bahasa Melayu) - (ms)',
            'Malayalam (മലയാളം) - (ml)',
            'Maltese (Malti) - (mt)',
            'Maori (Māori) - (mi)',
            'Marathi (मराठी) - (mr)',
            'Mongolian (Монгол) - (mn)',
            'Nepali (नेपाली) - (ne)',
            'Norwegian (Norsk) - (no)',
            'Odia (ଓଡ଼ିଆ) - (or)',
            'Pashto (پښتو) - (ps)',
            'Persian (فارسی) - (fa)',
            'Polish (Polski) - (pl)',
            'Portuguese (Português) - (pt)',
            'Punjabi (ਪੰਜਾਬੀ) - (pa)',
            'Romanian (Română) - (ro)',
            'Russian (Русский) - (ru)',
            'Samoan (Gagana Sāmoa) - (sm)',
            'Scots Gaelic (Gàidhlig) - (gd)',
            'Serbian (Српски) - (sr)',
            'Sesotho (Sesotho) - (st)',
            'Shona (Shona) - (sn)',
            'Sindhi (سنڌي) - (sd)',
            'Sinhala (සිංහල) - (si)',
            'Slovak (Slovenčina) - (sk)',
            'Slovenian (Slovenščina) - (sl)',
            'Somali (Soomaali) - (so)',
            'Spanish (Español) - (es)',
            'Sundanese (Basa Sunda) - (su)',
            'Swahili (Kiswahili) - (sw)',
            'Swedish (Svenska) - (sv)',
            'Tagalog (Tagalog) - (tl)',
            'Tajik (Тоҷикӣ) - (tg)',
            'Tamil (தமிழ்) - (ta)',
            'Tatar (Татарча) - (tt)',
            'Telugu (తెలుగు) - (te)',
            'Thai (ไทย) - (th)',
            'Turkish (Türkçe) - (tr)',
            'Turkmen (Türkmençe) - (tk)',
            'Ukrainian (Українська) - (uk)',
            'Urdu (اردو) - (ur)',
            'Uyghur (ئۇيغۇرچە) - (ug)',
            'Uzbek (Oʻzbekcha) - (uz)',
            'Vietnamese (Tiếng Việt) - (vi)',
            'Welsh (Cymraeg) - (cy)',
            'Xhosa (isiXhosa) - (xh)',
            'Yiddish (יידיש) - (yi)',
            'Yoruba (Yorùbá) - (yo)',
            'Zulu (isiZulu) - (zu)'
        ]
        self.lang_combo = wx.ComboBox(self.panel, choices=self.languages, 
                                      style=wx.CB_READONLY)
        default_index = 0
        for i, lang in enumerate(self.languages):
            if '(en)' in lang:
                default_index = i
                break
        self.lang_combo.SetSelection(default_index)
        self.lang_combo.SetToolTip('Select the target language for translation')
        lang_sizer.Add(self.lang_combo, 1, wx.ALL | wx.EXPAND, 5)
        self.mainsizer.Add(lang_sizer, 0, wx.ALL | wx.EXPAND, 5)
        btn_sizer = wx.BoxSizer(wx.HORIZONTAL)
        btn_sizer.AddStretchSpacer(1)
        self.translate_btn = wx.Button(self.panel, label='&Translate')
        self.translate_btn.SetToolTip('Click to translate the text (Shortcut: Ctrl+T)')
        self.translate_btn.Bind(wx.EVT_BUTTON, self.on_translate)
        btn_sizer.Add(self.translate_btn)
        btn_sizer.AddStretchSpacer(1)
        self.mainsizer.Add(btn_sizer, 0, wx.ALL | wx.EXPAND, 5)
        self.mainsizer.Add(wx.StaticText(self.panel, label='&Result:'), 
                          0, wx.ALL | wx.ALIGN_LEFT, 5)
        self.output_text = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE | wx.TE_READONLY,
                                       size=(-1, 150))
        self.output_text.SetToolTip('The translated text will appear here')
        self.output_text.SetBackgroundColour(wx.Colour(240, 240, 240))
        self.mainsizer.Add(self.output_text, 1, wx.ALL | wx.EXPAND, 5)
        extra_btn_sizer = wx.BoxSizer(wx.HORIZONTAL)
        extra_btn_sizer.AddStretchSpacer(1)
        self.file_btn = wx.Button(self.panel, label='From &File...')
        self.file_btn.SetToolTip('Select a text file to translate its content (Shortcut: Ctrl+F)')
        self.file_btn.Bind(wx.EVT_BUTTON, self.on_translate_file)
        extra_btn_sizer.Add(self.file_btn)
        extra_btn_sizer.AddSpacer(10)
        self.clear_btn = wx.Button(self.panel, label='&Clear')
        self.clear_btn.SetToolTip('Clear all text boxes (Shortcut: Ctrl+R)')
        self.clear_btn.Bind(wx.EVT_BUTTON, self.on_clear)
        extra_btn_sizer.Add(self.clear_btn)
        extra_btn_sizer.AddSpacer(10)
        self.swap_btn = wx.Button(self.panel, label='S&wap')
        self.swap_btn.SetToolTip('Swap source and target languages (Shortcut: Ctrl+W)')
        self.swap_btn.Bind(wx.EVT_BUTTON, self.on_swap)
        extra_btn_sizer.Add(self.swap_btn)
        extra_btn_sizer.AddStretchSpacer(1)
        self.mainsizer.Add(extra_btn_sizer, 0, wx.ALL | wx.EXPAND, 5)
        self.panel.SetSizer(self.mainsizer)
        self.setup_accelerators()
        self.Center()
        self.Maximize()
        self.Show()

    def setup_accelerators(self):
        accel_entries = [
            (wx.ACCEL_CTRL, ord('T'), self.translate_btn.GetId()),
            (wx.ACCEL_CTRL, ord('R'), self.clear_btn.GetId()),
            (wx.ACCEL_CTRL, ord('W'), self.swap_btn.GetId()),
            (wx.ACCEL_CTRL, ord('F'), self.file_btn.GetId()),
            (wx.ACCEL_CTRL, ord('L'), self.lang_combo.GetId()),
        ]
        accel_table = wx.AcceleratorTable(accel_entries)
        self.SetAcceleratorTable(accel_table)

    def get_lang_code(self, lang_selection):
        try:
            if '- (' in lang_selection and ')' in lang_selection:
                code_part = lang_selection.split('- (')[1].rstrip(')')
                return code_part
            return 'en'
        except:
            return 'en'

    def on_translate(self, event):
        source_text = self.input_text.GetValue().strip()
        if not source_text:
            wx.MessageBox('Please enter some text to translate!', 
                         'Error', wx.OK | wx.ICON_WARNING)
            self.input_text.SetFocus()
            return
        lang_selection = self.lang_combo.GetValue().strip()
        if not lang_selection:
            wx.MessageBox('Please select a target language!', 
                         'Error', wx.OK | wx.ICON_WARNING)
            self.lang_combo.SetFocus()
            return
        lang_code = self.get_lang_code(lang_selection)
        try:
            translated = GoogleTranslator(source='auto', target=lang_code).translate(source_text)
            self.output_text.SetValue(translated)
            self.output_text.SetFocus()
        except Exception as e:
            wx.MessageBox(f'Translation error:\n{str(e)}\n\nPlease check your internet connection.', 
                         'Translation Error', wx.OK | wx.ICON_ERROR)
            self.output_text.SetValue('')

    def on_translate_file(self, event):
        wildcard = "Text files (*.txt)|*.txt|All files (*.*)|*.*"
        file_dialog = wx.FileDialog(
            self, 
            message="Choose a text file to translate",
            defaultDir=os.getcwd(),
            wildcard=wildcard,
            style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
        )
        if file_dialog.ShowModal() == wx.ID_OK:
            file_path = file_dialog.GetPath()
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    file_content = file.read()
                if not file_content.strip():
                    wx.MessageBox('The selected file is empty!', 
                                 'Error', wx.OK | wx.ICON_WARNING)
                    return
                self.input_text.SetValue(file_content)
                lang_selection = self.lang_combo.GetValue().strip()
                if not lang_selection:
                    wx.MessageBox('Please select a target language first!', 
                                 'Error', wx.OK | wx.ICON_WARNING)
                    self.lang_combo.SetFocus()
                    return
                lang_code = self.get_lang_code(lang_selection)
                try:
                    translated = GoogleTranslator(source='auto', target=lang_code).translate(file_content)
                    self.output_text.SetValue(translated)
                    self.output_text.SetFocus()
                except Exception as e:
                    wx.MessageBox(f'Translation error:\n{str(e)}\n\nPlease check your internet connection.', 
                                 'Translation Error', wx.OK | wx.ICON_ERROR)
                    self.output_text.SetValue('')
            except UnicodeDecodeError:
                try:
                    with open(file_path, 'r', encoding='latin-1') as file:
                        file_content = file.read()
                    self.input_text.SetValue(file_content)
                    lang_selection = self.lang_combo.GetValue().strip()
                    if not lang_selection:
                        wx.MessageBox('Please select a target language first!', 
                                     'Error', wx.OK | wx.ICON_WARNING)
                        self.lang_combo.SetFocus()
                        return
                    lang_code = self.get_lang_code(lang_selection)
                    try:
                        translated = GoogleTranslator(source='auto', target=lang_code).translate(file_content)
                        self.output_text.SetValue(translated)
                        self.output_text.SetFocus()
                    except Exception as e:
                        wx.MessageBox(f'Translation error:\n{str(e)}\n\nPlease check your internet connection.', 
                                     'Translation Error', wx.OK | wx.ICON_ERROR)
                        self.output_text.SetValue('')
                except Exception as e:
                    wx.MessageBox(f'Could not read file:\n{str(e)}', 
                                 'Error', wx.OK | wx.ICON_ERROR)
            except Exception as e:
                wx.MessageBox(f'Could not read file:\n{str(e)}', 
                             'Error', wx.OK | wx.ICON_ERROR)
        file_dialog.Destroy()

    def on_clear(self, event):
        self.input_text.SetValue('')
        self.output_text.SetValue('')
        self.input_text.SetFocus()

    def on_swap(self, event):
        current_lang = self.lang_combo.GetValue()
        if current_lang:
            if '(en)' in current_lang:
                for i, lang in enumerate(self.languages):
                    if '(fa)' in lang:
                        self.lang_combo.SetSelection(i)
                        break
            elif '(fa)' in current_lang:
                for i, lang in enumerate(self.languages):
                    if '(en)' in lang:
                        self.lang_combo.SetSelection(i)
                        break
            else:
                for i, lang in enumerate(self.languages):
                    if '(en)' in lang:
                        self.lang_combo.SetSelection(i)
                        break
            translated_text = self.output_text.GetValue()
            if translated_text:
                self.input_text.SetValue(translated_text)
                self.output_text.SetValue('')
                self.input_text.SetFocus()

if __name__ == '__main__':
    app = wx.App()
    frame = TranslationFrame()
    app.MainLoop()