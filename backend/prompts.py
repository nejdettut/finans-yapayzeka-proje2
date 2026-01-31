SYSTEM_PROMPT = """Sen deneyimli bir kişisel finans danışmanısın.
Kullanıcıların harcama alışkanlıklarını analiz eder,
gereksiz giderleri tespit eder
ve net, uygulanabilir tasarruf önerileri sunarsın.

Cevapların:
- açık
- maddeli
- sade
olmalıdır."""

EXPENSE_EXTRACTION_PROMPT = """Aşağıdaki metinden harcama kalemlerini ve tutarlarını ayıkla.
Eğer tutar yoksa yaklaşık tahmin yapma, boş bırak.

Metin:
{user_input}"""

EXPENSE_CATEGORIZATION_PROMPT = """Aşağıdaki harcama kalemlerini uygun kategorilere ayır:
(kira, yemek, ulaşım, eğlence, abonelik, diğer)

Harcama listesi:
{expense_list}"""

ANALYSIS_PROMPT = """Aşağıdaki harcama kategorilerine bakarak:
- en yüksek harcama alanlarını
- riskli veya gereksiz görünenleri
belirle.

Veriler:
{category_data}"""

SAVINGS_SUGGESTION_PROMPT = """Bu harcama analizine göre
kullanıcıya uygulanabilir tasarruf önerileri üret.
Öneriler:
- net
- maddeli
- gerçekçi
olsun.

Analiz:
{analysis_result}"""
