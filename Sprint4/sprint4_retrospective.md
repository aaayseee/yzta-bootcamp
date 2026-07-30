# Sprint 4 Retrospective

Tarih: 30 Temmuz 2026

## İyi gidenler

- Sprint 3 prototipleri güvenli ve test edilebilir servis katmanlarına taşındı.
- Parolalar, roller ve şifre sıfırlama akışı merkezi veritabanında birleştirildi.
- API ile Streamlit aynı tahmin servisini ve kayıt şemasını kullanmaya başladı.
- Sahte entegrasyon başarıları kaldırıldı; Telegram gerçek servis yanıtıyla doğrulandı.
- CI sorunları adım adım ayrıştırılarak eksik `httpx` bağımlılığı ve PyArrow
  uyumsuzluğu kesin olarak tespit edildi.
- Katı CI yapılandırmasında bütün test aşamaları başarıyla tamamlandı.
- Login ekranındaki mobil taşma ve boş form doğrulama sorunları giderildi.

## Zorlayan noktalar

- Yerel ortamda kurulu olan `httpx` paketinin temiz CI ortamında bulunmaması,
  API testinin yalnızca GitHub üzerinde hata vermesine neden oldu.
- Serbest bırakılan PyArrow sürümü Linux/Python 3.12 ortamında Streamlit
  dataframe dönüşümünde native çökmeye yol açtı.
- Geniş kapsamlı Streamlit stilleri login ekranında responsive davranışı
  zorlaştırdı.
- Canlı entegrasyonlar için gerekli secret değerleri kaynak kod dışında
  yönetilmek zorunda olduğu için ortam yapılandırması kritik hâle geldi.

## Öğrenilenler

- CI bağımlılıkları yalnızca doğrudan uygulama paketlerini değil, test
  istemcilerini de açıkça içermelidir.
- Veri ve görselleştirme bağımlılıkları tekrarlanabilir kurulum için
  uyumlu sürümlere sabitlenmelidir.
- `continue-on-error` yalnızca geçici tanılama amacıyla kullanılmalı ve
  teslim öncesinde kaldırılmalıdır.
- Gerçek servis entegrasyonlarında başarı, sağlayıcının gerçek yanıtına göre
  belirlenmelidir.
- Login gibi kritik ekranlar boş form, başarılı giriş ve responsive görünüm
  açısından birlikte ele alınmalıdır.

## Sonraki adımlar

1. Canlı ortam secretlarını tanımlayıp deployment smoke testi yapmak.
2. Model başarımını cross-validation, veri bölme yöntemi ve sınıf dengesiyle
   yeniden üretilebilir biçimde raporlamak.
3. İhtiyaç oluşursa oturum zaman aşımı ve giriş denemesi sınırlaması eklemek.
4. WhatsApp ve Zendesk için gerçek sağlayıcı sözleşmeleri hazır olduğunda
   ayrı adaptörler geliştirmek.
