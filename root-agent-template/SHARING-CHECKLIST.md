# Root Agent — paylaşım öncesi kontrol listesi

Bu liste kullanıcı tarafından Grok Bot içinde uygulanır. Yerel doğrulama; kurulum, template önizlemesi veya canlı davranış testi sayılmaz. Aşağıdaki adımlar bu çalışmada **yapılmadı**.

- [ ] Mevcut Bot'a tam description ve güncel on sekiz skill kaydedildi; her birinin tamamı ve kullanılabilirliği yeniden açılarak karşılaştırıldı. User overlay metinleri ve açık istisna kuralları birlikte korundu.
- [ ] Template detaylarında beklenen description, her skill'in tam içeriği ve roster-management içindeki iki kanonik description denetlendi. Template oluşturulması tek başına tam aktarım kanıtı sayılmadı.
- [ ] Memories, plugins, routines ve kimlik içeriği elle incelendi; kişisel bilgiler, özel görev/roster kayıtları, sırlar, iç URL'ler ve paylaşım hakkı olmayan içerik çıkarıldı. Root Agent'a ait routine bulunmadığı doğrulandı.
- [ ] Gerekli bağlantılar ve desteklenen Bot mesajlaşması alıcının ortamında doğrulandı. Yayıncının repository, script, özel MCP, dosya veya oturumlarına runtime bağımlılığı bulunmadığı kontrol edildi. İsteğe bağlı Lead skill'leri olmadan zorunlu davranışın description'da bulunduğu görüldü.
- [ ] Public link / Team-only seçimi bilinçli yapıldı; Team-only template ile Publish to Team ayrıldı. Lisans bildirimi ve canlı test durumu tanıtımda açık tutuldu.
- [ ] Ayrı alıcı kopyası kendi instance/workspace'ini oluşturdu; yayıncının kişisel kayıtlarını veya geçmiş onaylarını devralmadı. Gerekli erişim kendi Bot'u tarafından güvenli probe ile doğrulandı.
- [ ] Uygulamanın gerçek alan sınırları description, skill ve tanıtım metni için ayrı kaydedildi; kesilme varsa kurulum başarısız sayıldı. 6000 karakter resmi limit olarak doğrulanmadı; sayısal yerel ölçüm save/preview başarısı sayılmadı.
- [ ] Güvenli canlı senaryolar için gerçek kanıt toplandıktan sonra [kabul senaryolarının](validation/acceptance.md) ilgili NOT RUN durumları ayrıca güncellendi. Kaynak güncellemesi mevcut paylaşım bağlantısını otomatik güncellemiş sayılmadı.

Kaynaklar: [paylaşım](https://docs.x.ai/grok-bot/bots#share-a-bot), [template içeriği ve kurulum](https://x.ai/bot/guides/templates-for-grok-bot), [paylaşım koşulları](https://x.ai/legal/bot-sharing-terms). Kontrol tarihi: 18 Ekim 2026. Otomatik gizlilik filtrelemesine güvenilmez.
