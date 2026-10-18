# Lead — description and optional skills

Bu klasör, Root Agent'ın kurduğu **Lead** Bot'ları için kaynak metinleri tutar. Root Agent tier 2 ve tier 3 yapılarda alanın günlük yönetimini Lead'e devreder: Uzman'ların görev prompt'larını Lead yazar ve gönderir, çıktıları Lead birleştirir, Root Agent'a tek entegre sonuç döner.

## Ne zorunlu, ne opsiyonel

| Parça | Nerede | Zorunlu mu |
| --- | --- | --- |
| Kanonik Lead description | [`../root-agent-template/templates/lead-description.md`](../root-agent-template/templates/lead-description.md) | **Evet.** Root Agent, Lead Bot'u yaratırken bunu uygular. Tek başına çalışır. |
| `lead-dispatch` skill | [`skills/lead-dispatch.md`](skills/lead-dispatch.md) | Hayır. Elle kurulur, derinlik katar. |
| `lead-integrate` skill | [`skills/lead-integrate.md`](skills/lead-integrate.md) | Hayır. Elle kurulur, derinlik katar. |

Bot'lar arası skill kaydı veya enable etme kabiliyeti varsayılmaz; güncel uygulamanın desteklediği library ve Bot kullanılabilirliği kontrolleri doğrulanır. Zorunlu dispatch, revision/duplicate, stop ve routine sınırları kanonik Lead description içinde bulunur. Buradaki iki skill ancak kurulmuş ve kullanılabilirliği doğrulanmışsa devreye girer; tek birinin eksik olması zorunlu davranışları durdurmaz.

## Kurulum

1. Root Agent önce Lead'i yaratır ve profilini doğrular, sonra üyeleri gerçek Lead referansıyla oluşturur. Değişken üye roster'ı kalıcı description'a değil handoff'a konur. Ayrı setup/access-check, production roster'ı oluşmadan Lead'in kendi klasörünü başlatabilir. Son onay satırı birebir korunur.
2. İstersen `skills/` altındaki iki gövdeyi Grok Bot'un skill kütüphanesine kaydet ve **yalnızca o Lead Bot için** enable et. Root Agent'a veya Uzman'lara enable etme.
3. Production handoff'unda Lead, güncel task/stage/scope/package revision ve delivery key ile üyeleri, teslimleri ve checkpoint'i doğrulayan **readback** döner. Yanıt aynı alıcı konuşmasından gelmelidir; eski revision ve duplicate paket yeni execution başlatmaz. Root Agent zamanı ve göndereni kaydeder; hassas veri varsa alıntıyı redakte edilmiş diye işaretler. Geçerli readback olmadan devredilen yeni kapsam bekler.

## Sınırlar

- Lead Bot açmaz, group açmaz, alt ekip kurmaz.
- Lead kendi alanının bağımsız reviewer'ını seçmez ve brief'lemez — review gate Root Agent'ta kalır. Lead'in entegre ettiği işi kendi kontrol etmesi bağımsız review sayılmaz.
- Lead devredilen kapsamı kendi başına büyütmez; gerekçe ve maliyetle **önerir**, kararı Root Agent verir. Yanıtlanmamış öneri onay değildir.
- Routine, işi fiilen koşan Uzman'a bağlanır; yalnızca koordine eden Lead'e veya Root Agent'a bağlanmaz.

Root Agent tarafındaki karşılık: [`lead-handoff`](../root-agent-template/skills/lead-handoff.md).
