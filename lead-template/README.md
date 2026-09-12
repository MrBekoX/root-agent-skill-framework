# Lead — description and optional skills

Bu klasör, Root Agent'ın kurduğu **Lead** Bot'ları için kaynak metinleri tutar. Root Agent tier 2 ve tier 3 yapılarda alanın günlük yönetimini Lead'e devreder: Uzman'ların görev prompt'larını Lead yazar ve gönderir, çıktıları Lead birleştirir, Root Agent'a tek entegre sonuç döner.

## Ne zorunlu, ne opsiyonel

| Parça | Nerede | Zorunlu mu |
| --- | --- | --- |
| Kanonik Lead description | [`../root-agent-template/templates/lead-description.md`](../root-agent-template/templates/lead-description.md) | **Evet.** Root Agent, Lead Bot'u yaratırken bunu uygular. Tek başına çalışır. |
| `lead-dispatch` skill | [`skills/lead-dispatch.md`](skills/lead-dispatch.md) | Hayır. Elle kurulur, derinlik katar. |
| `lead-integrate` skill | [`skills/lead-integrate.md`](skills/lead-integrate.md) | Hayır. Elle kurulur, derinlik katar. |

Bir Bot başka bir Bot'a skill kaydedip enable edemez. Root Agent yalnızca description yazabilir, bu yüzden Lead'in dispatch yeteneği kanonik description içinde eksiksiz tanımlıdır. Buradaki iki skill o davranışı prosedüre dönüştürür ve ancak kullanıcı elle kurarsa devreye girer.

## Kurulum

1. Lead Bot'u Root Agent yaratır ve kanonik Lead description'ı uygular. Kaydedilen profili yeniden açıp doğrula; son satır birebir korunmalı.
2. İstersen `skills/` altındaki iki gövdeyi Grok Bot'un skill kütüphanesine kaydet ve **yalnızca o Lead Bot için** enable et. Root Agent'a veya Uzman'lara enable etme.
3. Lead'in ilk işi, Root Agent'ın handoff paketine **readback** dönmektir: devredilen kapsam, hangi üyeye ne gideceği, ulaşılamayan üyeler ve ilk checkpoint. Readback gelmeden Root Agent alanı devredilmiş saymaz.

## Sınırlar

- Lead Bot açmaz, group açmaz, alt ekip kurmaz.
- Lead kendi alanının bağımsız reviewer'ını seçmez ve brief'lemez — review gate Root Agent'ta kalır. Lead'in entegre ettiği işi kendi kontrol etmesi bağımsız review sayılmaz.
- Lead devredilen kapsamı kendi başına büyütmez; gerekçe ve maliyetle **önerir**, kararı Root Agent verir. Yanıtlanmamış öneri onay değildir.
- Routine, işi fiilen koşan Uzman'a bağlanır; yalnızca koordine eden Lead'e veya Root Agent'a bağlanmaz.

Root Agent tarafındaki karşılık: [`lead-handoff`](../root-agent-template/skills/lead-handoff.md).
