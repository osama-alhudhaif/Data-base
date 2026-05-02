# 🗄️ Oda — Database Design

تصميم قاعدة البيانات لمنصة **Oda** للترجمة الأدبية والفنية بالذكاء الاصطناعي.

## نظرة عامة

- **نظام إدارة قاعدة البيانات:** PostgreSQL 18+
- **عدد الجداول:** 18
- **التطبيقات:** accounts, stories, auth, authtoken
- **الإطار:** Django 6 ORM

## الملفات

| الملف | الوصف |
|------|-------|
| `schema.sql` | تصميم الجداول كاملاً (DDL فقط، بدون بيانات) |

## كيفية إعادة بناء قاعدة البيانات

```bash
# 1. أنشئ قاعدة بيانات جديدة
createdb oda_data

# 2. طبّق الـ schema
psql -d oda_data -f schema.sql
```

## الجداول

- `accounts_follow`
- `accounts_notification`
- `accounts_subscription`
- `accounts_user`
- `accounts_user_groups`
- `accounts_user_user_permissions`
- `auth_group`
- `auth_group_permissions`
- `auth_permission`
- `authtoken_token`
- `django_admin_log`
- `django_content_type`
- `django_migrations`
- `django_session`
- `stories_comment`
- `stories_rating`
- `stories_story`
- `stories_storylike`

## فلسفة التصميم

يتبع التصميم مبدأ **السيادة البرمجية (Software Sovereignty)** الذي تقوم عليه منصة Oda، مع التركيز على:
- استقلالية البنية التحتية (PostgreSQL مفتوح المصدر، نشر Ubuntu أصيل)
- حماية البيانات الإبداعية والثقافية
- إمكانية التكرار والشفافية في التصميم

## ملاحظة أمنية

تم تصدير هذا التصميم بـ:
- `--schema-only` (بدون أي بيانات)
- `--no-owner` (بدون أسماء حسابات)
- `--no-privileges` (بدون معلومات صلاحيات)

---

جزء من مشروع [Oda](https://github.com/osama-alhudhaif) — منصة الترجمة الأدبية والفنية.
