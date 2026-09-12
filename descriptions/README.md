# descriptions

Bot description'larının (sys prompt) versiyonlu kopyaları. Her dosya yalnızca description metnini içerir. İçine başlık veya not eklenmez, böylece dosya Grok Bot'un **Edit Profile → Description** alanına olduğu gibi, tek parça yapıştırılabilir. Açıklamalar bu dosyada tutulur.

| Bot | Dosya | Kaynak | Sürüm | Son satır |
| --- | --- | --- | --- | --- |
| Root Agent | [`root-agent.md`](root-agent.md) | [`root-agent-template/description.md`](../root-agent-template/description.md) | 12 Eylül 2026 — Lead devri, 16 skill | Onay satırı birebir |

## Kurallar

- **Kaynak şablondur.** `root-agent.md`, `root-agent-template/description.md` ile birebir aynı tutulur. Birini değiştirirken diğerini de aynı commit'te güncelleyin. Şablonu değiştirdikten sonra `root-agent-template/` içinde `python validation/generate_setup.py` ve `python validation/structural_check.py` çalıştırın.
- **Eski sürümler git geçmişinde kalır.** Ayrı bir `archive/` kopyası tutulmaz. Davranışı değiştiren her satır `eski satır → yeni satır` olarak listelenir.
- **Her description aynı satırla biter:** `Sending messages, publishing, deleting, purchasing, and production or account changes always require approval.`
- **Özel veri girmez.** Kişisel ad, şifre, token, iç URL ya da görev metni description'a yazılmaz; görev mesajla verilir.
