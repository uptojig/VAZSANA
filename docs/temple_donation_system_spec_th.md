เอกสารข้อกำหนดการออกแบบระบบรับบริจาคออนไลน์สำหรับวัด
1. วัตถุประสงค์ของระบบ
ระบบนี้มีเป้าหมายเป็น แพลตฟอร์มกลาง สำหรับวัดในประเทศไทยในการรับบริจาคออนไลน์ โดยใช้ Subdomain/Sale Page เฉพาะของแต่ละวัด เป็นช่องทางหลักในการเชื่อมต่อกับผู้บริจาค (แทนการใช้ LINE OA โดยตรง) ระบบจะจัดการตั้งแต่การเชิญชวนวัดให้มาเข้าร่วมแพลตฟอร์ม, การจัดการการสมัครและอนุมัติวัด, การสร้าง URL เฉพาะให้กับวัด, การจัดการโครงการบริจาค, การรับชำระเงินหลากหลายช่องทาง (เน้น PromptPay QR และบัตรเครดิต/เดบิต), การออกใบอนุโมทนาบุญอัตโนมัติ, ไปจนถึงการจัดการ Branding ของวัด และการดูแลแพลตฟอร์มในภาพรวม รวมถึงระบบจัดการข่าวสาร/บทความเพื่อเผยแพร่ข้อมูลของแพลตฟอร์ม

2. คุณสมบัติและฟังก์ชันหลัก
ระบบถูกออกแบบมาเพื่อรองรับการใช้งานของ 4 กลุ่มหลัก:

2.1 สำหรับแพลตฟอร์ม (Platform Admin Portal & Landing Page)
2.1.1 หน้า Landing Page / Sales Page (สำหรับเชิญชวนวัดและประชาสัมพันธ์แพลตฟอร์ม):

วัตถุประสงค์: เป็นหน้าเว็บหลักของแพลตฟอร์ม (เช่น yourplatform.com) เพื่อนำเสนอจุดเด่น, คุณสมบัติหลัก, Testimonials, กรณีศึกษา, และมี Call to Action "สมัครใช้งานสำหรับวัด"

ระบบจัดการข่าวสาร / Blog: แอดมินแพลตฟอร์มสามารถสร้าง, แก้ไข, ลบข่าวสาร, บทความ, หรือ Blog Post เพื่อเผยแพร่ข้อมูลสำคัญ, กิจกรรม, หรือเรื่องราวต่างๆ ที่เกี่ยวข้องกับแพลตฟอร์มหรือวัดที่เข้าร่วม ระบบจะแสดงเนื้อหาเหล่านี้บนหน้าเว็บสาธารณะ (Landing Page) เพื่อประชาสัมพันธ์และสร้างความน่าเชื่อถือ

2.1.2 ระบบหลังบ้านสำหรับแอดมินแพลตฟอร์ม (Platform Admin Portal):

วัตถุประสงค์: เป็นส่วนควบคุมกลางสำหรับผู้ดูแลระบบ ของเรา เพื่อจัดการแพลตฟอร์มทั้งหมด

การจัดการผู้ใช้งานระบบ (Admin Accounts): แอดมินแพลตฟอร์มสามารถเพิ่ม, แก้ไข, ลบผู้ใช้งานที่เป็นแอดมินของแพลตฟอร์มได้

การกำหนดสิทธิ์ผู้ใช้งาน (Role-Based Access Control - RBAC): สามารถกำหนดบทบาทและสิทธิ์การเข้าถึงฟังก์ชันต่างๆ ภายใน Platform Admin Portal ให้กับผู้ใช้งานแต่ละคนได้ (เช่น Super Admin, Content Editor, Finance Admin)

การจัดการการสมัครและการอนุมัติวัด:

แอดมินสามารถดูรายการคำขอสมัครของวัดที่เข้ามาทั้งหมด

สามารถตรวจสอบข้อมูลที่วัดส่งมา (เช่น เอกสารยืนยันตัวตน, ข้อมูลพื้นฐาน)

อนุมัติ/ปฏิเสธ การสมัครของวัด

ระบบเลือก/ปรับแต่งฟอร์มการสมัคร: แอดมินแพลตฟอร์มสามารถกำหนดหรือเลือกรูปแบบของฟอร์มการสมัครสำหรับวัดได้ เพื่อความยืดหยุ่นในการเก็บข้อมูลที่จำเป็น

การสร้าง Subdomain / URL เฉพาะอัตโนมัติ:

เมื่อแอดมินอนุมัติการสมัครของวัด ระบบจะ สร้าง Subdomain (เช่น watname.yourplatform.com) หรือ URL เฉพาะของตนเองโดยอัตโนมัติ

จัดการการผูก Domain Name System (DNS) Records ที่เกี่ยวข้อง เพื่อให้ Subdomain นั้นชี้ไปยัง Sale Page และหน้าบริจาคเฉพาะของวัดนั้นๆ ได้อย่างถูกต้อง

การจัดการข้อมูลวัดทั้งหมด: ดูแล, แก้ไขข้อมูลพื้นฐานของวัดที่ลงทะเบียนอยู่, ระงับการใช้งานชั่วคราว, หรือยกเลิกบริการ/ลบข้อมูลวัดออกจากระบบ

การดูรายงานและสถิติภาพรวมของแพลตฟอร์ม: สรุปยอดบริจาครวมจาก ทุกวัด ที่อยู่บนแพลตฟอร์ม, จำนวนวัดที่ใช้งานอยู่, จำนวนการสมัครใหม่, และภาพรวมประสิทธิภาพของช่องทางการชำระเงิน

การตั้งค่าระบบกลาง: เช่น ค่าธรรมเนียมการดำเนินการ (ถ้ามี), การตั้งค่าการแจ้งเตือนสำหรับแอดมินแพลตฟอร์ม

2.2 สำหรับวัด (Temple Admin Portal)
การเข้าสู่ระบบ Temple Admin Portal: วัดจะได้รับ URL สำหรับเข้าสู่ระบบหลังบ้านของตนเอง (อาจเป็น Subdomain ของเรา เช่น watname.yourplatform.com/admin หรือลิงก์เฉพาะ) และเข้าสู่ระบบด้วยบัญชีที่สร้างขึ้น

การตั้งค่าบัญชีวัด: เมื่อเข้าสู่ระบบครั้งแรก หรือต้องการแก้ไข วัดสามารถกรอกข้อมูลพื้นฐานของวัด (ที่อยู่, เบอร์โทรศัพท์, เว็บไซต์), อัปโหลดเอกสารยืนยันตัวตน (ถ้ามี), และตั้งค่าบัญชีธนาคารสำหรับรับเงินบริจาค

การจัดการ Branding ของวัด: วัดสามารถเข้าสู่เมนู "การตั้งค่า Branding" เพื่อปรับแต่งองค์ประกอบต่างๆ เช่น:

โลโก้วัด: อัปโหลดและจัดการโลโก้ที่จะแสดงบน Sale Page และใบอนุโมทนาบุญ

โทนสี: เลือกโทนสีหลัก (Primary Color) และสีรอง (Secondary Color) ที่จะใช้ในหน้าบริจาคและ Sale Page เพื่อให้เข้ากับเอกลักษณ์ของวัด

ข้อมูลติดต่อของวัด: ที่อยู่, เบอร์โทรศัพท์, เว็บไซต์, แผนที่

ข้อความอนุโมทนาบุญ: แก้ไขข้อความอนุโมทนาบุญเริ่มต้นที่ใช้ในใบอนุโมทนาบุญ

รูปภาพปก/ภาพประกอบ Sale Page: กำหนดรูปภาพที่จะแสดงบน Sale Page เฉพาะของวัด

การสร้างและจัดการโครงการบริจาค: วัดเข้าสู่เมนู "โครงการบริจาค" เพื่อ:

สร้างโครงการใหม่: กรอกรายละเอียดโครงการ (ชื่อ, รายละเอียด, วัตถุประสงค์, เป้าหมายยอดเงิน, วันที่เริ่มต้น/สิ้นสุด, อัปโหลดรูปภาพ/วิดีโอประกอบ)

จัดการโครงการ: แก้ไขข้อมูล, พักโครงการ (Deactivate เพื่อซ่อนจากหน้าผู้บริจาค), หรือลบโครงการ

โครงการที่สร้างขึ้นจะแสดงใน Sale Page ของวัดนั้นๆ

การดูรายงานและสถิติการบริจาค: วัดสามารถเข้าถึงเมนู "รายงานการบริจาค" เพื่อ:

ดูรายการบริจาคทั้งหมดที่เกิดขึ้นกับวัดของตนเอง

กรองข้อมูลตามโครงการ, ช่วงเวลา, หรือสถานะการชำระเงิน

ดูยอดรวมการบริจาค, ยอดที่ได้รับในแต่ละโครงการ (อัปเดตแบบ Real-time)

สามารถดาวน์โหลดรายงานเป็น CSV/Excel ได้

การจัดการผู้ดูแลวัดเพิ่มเติม (ถ้ามี): วัดสามารถเชิญผู้ดูแลคนอื่นให้เข้ามาร่วมจัดการระบบหลังบ้านของวัดได้ (เช่น พระเลขา, เจ้าหน้าที่วัด) พร้อมกำหนดสิทธิ์การเข้าถึงที่แตกต่างกัน

2.3 สำหรับผู้บริจาค (Donation Web Application)
การเข้าถึงระบบบริจาค: ผู้บริจาคเข้าถึง Sale Page หรือ Subdomain เฉพาะของวัดนั้นๆ (เช่น watname.yourplatform.com) ผ่าน Web Browser

การแสดงรายการและรายละเอียดโครงการ:

หน้า Sale Page ของวัดจะแสดงข้อมูลเบื้องต้นของวัด (ประวัติ, ที่อยู่) และรายการโครงการบริจาคที่เปิดรับอยู่ของวัดนั้นๆ

ผู้บริจาคสามารถคลิกเลือกโครงการเพื่อดูรายละเอียดครบถ้วน (ชื่อ, รายละเอียด, รูปภาพ/วิดีโอ, เป้าหมายยอดเงิน, ยอดเงินที่ได้รับแล้ว, ระยะเวลาโครงการ)

การระบุจำนวนเงิน: ผู้บริจาคสามารถกรอกจำนวนเงินที่ต้องการบริจาคเอง หรือเลือกจากจำนวนเงินที่กำหนดไว้ล่วงหน้า

ช่องทางการชำระเงิน:

PromptPay QR Code: ระบบจะสร้าง QR Code (พร้อมเพย์) ที่มีข้อมูลการโอนเงิน (เช่น เลขบัญชีธนาคารของวัด, จำนวนเงิน) โดยอัตโนมัติ เมื่อผู้บริจาคสแกนและโอนเงิน ระบบจะตรวจสอบสถานะการโอนเงินผ่าน API ของธนาคาร (เช่น KBank API, SCB API, หรืออื่นๆ ที่รองรับ)

บัตรเครดิต/เดบิต: เชื่อมต่อผ่าน Payment Gateway ภายนอกที่น่าเชื่อถือ (เช่น Stripe, Omise, 2C2P) เพื่อรองรับการชำระเงินด้วยบัตร

การสร้างใบอนุโมทนาบุญอัตโนมัติ:

เมื่อการบริจาคสำเร็จ (สถานะ Payment เป็น SUCCESS) ระบบจะ สร้างใบอนุโมทนาบุญในรูปแบบ PDF โดยอัตโนมัติ

ข้อมูลในใบอนุโมทนาบุญจะประกอบด้วย: ชื่อผู้บริจาค (ตามที่กรอก), วันที่และเวลาที่บริจาค, ชื่อโครงการ, จำนวนเงิน, ข้อความอนุโมทนาจากวัด (ที่วัดตั้งค่าไว้), โลโก้และข้อมูลติดต่อของวัด, เลขที่ใบอนุโมทนาบุญ (Running Number)

ผู้บริจาคจะได้รับ Link สำหรับดาวน์โหลดใบอนุโมทนาบุญ (PDF) ทันทีบนหน้าจอ "ขอบคุณสำหรับการบริจาค" และอาจส่งไปทาง Email ที่ผู้บริจาคระบุ

ใบอนุโมทนาบุญจะถูกเก็บในระบบ และผู้บริจาคสามารถเรียกดูหรือดาวน์โหลดซ้ำได้ในภายหลัง (เช่น ผ่านการค้นหาจากเบอร์โทรศัพท์/Email)

3. สถาปัตยกรรมระบบที่แนะนำ
สถาปัตยกรรม: แนะนำแบบ Microservices หรือ Modular Monolith เพื่อให้มีความยืดหยุ่น, ปรับขนาดได้ง่าย, และสามารถแยกทีมพัฒนาดูแลส่วนต่างๆ ได้อย่างอิสระ

Frontend:

Platform Admin Portal: React.js / Vue.js / Angular (SPA - Single Page Application)

Temple Admin Portal: React.js / Vue.js / Angular (SPA - Single Page Application)

Donation Web Application / Sale Page (สำหรับผู้บริจาค): Next.js / Nuxt.js (SSR - Server Side Rendering หรือ Static Site Generation) เพื่อ SEO ที่ดีสำหรับ Sale Page และประสิทธิภาพในการโหลดที่รวดเร็ว

Backend:

API Gateway: Nginx / API Gateway (เช่น AWS API Gateway) สำหรับจัดการ Request, Authentication, Rate Limiting, และ Routing ไปยัง Microservices ที่เกี่ยวข้อง

Microservices (ตัวอย่าง):

User Service: จัดการข้อมูลผู้ใช้งาน (Platform Admin, Temple Admin) และ Authentication/Authorization

Temple Service: จัดการข้อมูลวัด, การตั้งค่า Branding, สถานะการใช้งานของวัด, และการผูก Subdomain

Project Service: จัดการข้อมูลโครงการบริจาคของแต่ละวัด

Donation Service: จัดการ Transaction การบริจาค, บันทึกข้อมูลการบริจาค, และอัปเดตยอดเงินโครงการ

Payment Service: ประสานงานกับ Payment Gateway Providers (สำหรับบัตรเครดิต/เดบิต) และธนาคาร API (สำหรับ PromptPay QR Code และการตรวจสอบการโอนเงิน)

PDF Generation Service: สร้างใบอนุโมทนาบุญในรูปแบบ PDF (รับข้อมูลจาก Donation Service และ Project Service)

Notification Service: ส่งแจ้งเตือนผ่าน Email และ SMS (ถ้ามี)

Content/Blog Service: จัดการเนื้อหาข่าวสาร/บทความสำหรับ Landing Page

เทคโนโลยี Backend: Node.js (Express/NestJS) / Python (Django/Flask) / Java (Spring Boot) / GoLang (เลือกตามความถนัดและเหมาะสม)

Database:

Relational Database: PostgreSQL / MySQL (เหมาะสำหรับข้อมูลที่มีความสัมพันธ์กันสูง เช่น ผู้ใช้งาน, วัด, โครงการ, การบริจาค, ใบอนุโมทนาบุญ เพื่อรักษา Data Integrity และความสอดคล้องของข้อมูล)

NoSQL Database (เสริม): MongoDB / Redis (อาจใช้สำหรับเก็บ Cache, Session Management, หรือ Log Data ที่ไม่มีโครงสร้างตายตัวมากนัก)

ระบบจัดการ PDF:

เทคโนโลยี: Library ที่ใช้ในการสร้าง PDF เช่น wkhtmltopdf (แปลง HTML เป็น PDF), Puppeteer (ควบคุม Chrome Headless เพื่อสร้าง PDF จากเว็บเพจ), หรือ PDFKit (สำหรับ Node.js)

การทำงาน: รับข้อมูลจาก Donation Service และ Project Service เพื่อสร้าง PDF ตาม Template ที่กำหนด

Deployment & Infrastructure:

Cloud Platform: AWS / Google Cloud Platform (GCP) / Microsoft Azure (เลือกตามความเหมาะสมด้านราคา, ฟังก์ชัน, และความคุ้นเคย)

Compute: Kubernetes (EKS, GKE, AKS) หรือ Docker บน EC2/Compute Engine สำหรับการ Deploy Microservices เพื่อการ Scale ที่ยืดหยุ่น

Storage: S3 / Google Cloud Storage (สำหรับเก็บไฟล์ PDF ของใบอนุโมทนาบุญ, รูปภาพโครงการ, โลโก้วัด, และ Asset อื่นๆ)

CDN (Content Delivery Network): CloudFront / Cloudflare สำหรับ Static Assets (รูปภาพ, CSS, JS) และ Sale Page เพื่อความเร็วในการโหลดที่ดียิ่งขึ้นสำหรับผู้ใช้งานทั่วประเทศ

Monitoring & Logging: Prometheus, Grafana, ELK Stack (Elasticsearch, Logstash, Kibana) สำหรับการติดตามประสิทธิภาพ, การแจ้งเตือนข้อผิดพลาด, และการวิเคราะห์ Log Data

Backup & Disaster Recovery: มีแผนการสำรองข้อมูลและกู้คืนระบบที่ชัดเจน เพื่อป้องกันข้อมูลสูญหายและรับประกันความต่อเนื่องในการให้บริการ

4. โครงสร้างฐานข้อมูลเบื้องต้น
users Table:

id (PK, INT)

username (VARCHAR)

email (VARCHAR, UNIQUE)

password_hash (VARCHAR)

role (ENUM: 'system_admin', 'temple_admin') - สำคัญสำหรับการกำหนดสิทธิ์

is_active (BOOLEAN, DEFAULT TRUE)

created_at (DATETIME)

updated_at (DATETIME)

temples Table:

id (PK, INT)

platform_admin_user_id (FK to users.id, INT, NULLABLE) - ผู้ดูแลแพลตฟอร์มที่อนุมัติ

temple_name_th (VARCHAR)

temple_name_en (VARCHAR)

address (TEXT)

phone_number (VARCHAR)

website_url (VARCHAR, NULLABLE)

logo_url (VARCHAR, NULLABLE)

primary_color (VARCHAR, HEX code, NULLABLE)

secondary_color (VARCHAR, HEX code, NULLABLE)

auto_thank_you_message (TEXT) - ข้อความอนุโมทนาบุญเริ่มต้น

subdomain (VARCHAR, UNIQUE) - Subdomain เฉพาะของวัด (เช่น watard)

is_approved (BOOLEAN, DEFAULT FALSE) - สถานะการอนุมัติโดยแอดมินแพลตฟอร์ม

bank_account_name (VARCHAR)

bank_account_number (VARCHAR)

bank_name (VARCHAR)

onboarding_form_id (FK to form_templates.id, INT, NULLABLE) - อ้างอิงฟอร์มที่ใช้สมัคร

created_at (DATETIME)

updated_at (DATETIME)

projects Table:

id (PK, INT)

temple_id (FK to temples.id, INT)

project_name_th (VARCHAR)

project_name_en (VARCHAR)

description_th (TEXT)

description_en (TEXT)

target_amount (DECIMAL(18,2))

current_amount (DECIMAL(18,2), DEFAULT 0.00)

start_date (DATE)

end_date (DATE, NULLABLE)

is_active (BOOLEAN, DEFAULT TRUE)

image_url (VARCHAR, NULLABLE)

video_url (VARCHAR, NULLABLE)

created_at (DATETIME)

updated_at (DATETIME)

donations Table:

id (PK, INT)

project_id (FK to projects.id, INT)

temple_id (FK to temples.id, INT) - Redundancy เพื่อความสะดวกในการ Query

donor_name (VARCHAR)

donor_email (VARCHAR, NULLABLE)

donor_phone_number (VARCHAR, NULLABLE)

amount (DECIMAL(18,2))

payment_method (ENUM: 'PROMPT_PAY_QR', 'CREDIT_CARD') - ไม่มี LINE_PAY แล้ว

transaction_id (VARCHAR, UNIQUE) - เลขที่ Transaction จาก Payment Gateway/ธนาคาร

payment_status (ENUM: 'PENDING', 'SUCCESS', 'FAILED', 'REFUNDED')

donated_at (DATETIME)

receipt_id (FK to receipts.id, INT, NULLABLE)

created_at (DATETIME)

updated_at (DATETIME)

receipts Table:

id (PK, INT)

donation_id (FK to donations.id, UNIQUE, INT)

receipt_number (VARCHAR, UNIQUE)

receipt_url (VARCHAR) - URL ของไฟล์ PDF ที่เก็บใน Object Storage

generated_at (DATETIME)

created_at (DATETIME)

form_templates Table (ใหม่ - สำหรับจัดการฟอร์มสมัครวัด):

id (PK, INT)

form_name (VARCHAR)

form_definition_json (JSON) - เก็บโครงสร้างฟอร์มในรูปแบบ JSON (เช่น field type, label, required)

is_active (BOOLEAN, DEFAULT TRUE)

created_at (DATETIME)

updated_at (DATETIME)

blog_posts Table (ใหม่ - สำหรับจัดการข่าวสาร/Blog):

id (PK, INT)

title (VARCHAR)

slug (VARCHAR, UNIQUE)

content (TEXT)

author_user_id (FK to users.id, INT)

published_at (DATETIME, NULLABLE)

status (ENUM: 'draft', 'published', 'archived')

thumbnail_url (VARCHAR, NULLABLE)

created_at (DATETIME)

updated_at (DATETIME)

Relationships:

users 1--* temples (User ที่เป็น Temple Admin สามารถดูแลวัดได้)

temples 1--* projects (วัดหนึ่งมีหลายโครงการ)

projects 1--* donations (โครงการหนึ่งมีการบริจาคหลายครั้ง)

temples 1--* donations (วัดหนึ่งมีการบริจาคหลายครั้ง)

donations 1--1 receipts (การบริจาคหนึ่งครั้งมีใบอนุโมทนาบุญหนึ่งใบ)

form_templates 1--* temples (ฟอร์มสมัครหนึ่งแบบสามารถใช้กับหลายวัดได้)

users 1--* blog_posts (ผู้ใช้งานระบบสามารถเป็นผู้เขียน Blog ได้)

5. Flow การใช้งาน
5.1. Flow การใช้งานฝั่งแพลตฟอร์ม (Platform Admin)
เข้าสู่ระบบ Platform Admin Portal: แอดมินแพลตฟอร์มเข้าสู่ระบบด้วยบัญชีของตนเอง

จัดการผู้ใช้งาน: เพิ่ม/แก้ไข/ลบผู้ใช้งานแอดมินคนอื่นๆ, กำหนดสิทธิ์การเข้าถึง

จัดการฟอร์มสมัครวัด: เข้าสู่เมนู "Form Management" เพื่อสร้างหรือแก้ไขโครงสร้างของฟอร์มการสมัครสำหรับวัด

จัดการการสมัครวัด:

ดูรายการคำขอสมัครใหม่

ตรวจสอบข้อมูลที่วัดส่งมา (อาจต้องมีการอัปโหลดเอกสาร)

กด "อนุมัติ" หรือ "ปฏิเสธ"

เมื่ออนุมัติ: ระบบจะสร้าง Subdomain (เช่น watname.yourplatform.com) และทำการผูก DNS records โดยอัตโนมัติ จากนั้นส่งข้อมูลการเข้าถึง Temple Admin Portal ไปยังวัดที่สมัคร

จัดการข้อมูลวัด: ดูรายการวัดทั้งหมดที่ใช้งานอยู่, แก้ไขข้อมูลพื้นฐาน, ระงับการใช้งาน, หรือยกเลิกบริการ

จัดการข่าวสาร/Blog: สร้าง, แก้ไข, เผยแพร่บทความหรือข่าวสารที่ต้องการแสดงบน Landing Page

ดูรายงานภาพรวม: ดูสถิติการบริจาครวมทุกวัด, จำนวนวัดที่ใช้งาน, รายได้แพลตฟอร์ม (ถ้ามี)

5.2. Flow การใช้งานฝั่งวัด (Temple Admin Portal)
สมัครสมาชิก (ผ่าน Landing Page ของแพลตฟอร์ม):

วัดเข้าสู่ yourplatform.com และคลิก "สมัครใช้งานสำหรับวัด"

กรอกข้อมูลตามฟอร์มที่กำหนด (ซึ่งแอดมินแพลตฟอร์มสร้างไว้) และส่งคำขอ

เข้าสู่ระบบ Temple Admin Portal (หลังอนุมัติ): วัดได้รับแจ้งเตือนการอนุมัติพร้อมลิงก์และข้อมูลเข้าสู่ระบบ

ตั้งค่าบัญชีวัด: กรอก/ยืนยันข้อมูลพื้นฐาน, ตั้งค่าบัญชีธนาคารสำหรับรับเงิน, อัปโหลดเอกสารยืนยันตัวตนเพิ่มเติม (ถ้าจำเป็น)

จัดการ Branding: อัปโหลดโลโก้, เลือกโทนสี, กำหนดข้อความอนุโมทนาบุญ, ตั้งค่ารูปภาพปก Sale Page

สร้างและจัดการโครงการบริจาค: สร้างโครงการใหม่พร้อมรายละเอียด, รูปภาพ, เป้าหมาย; แก้ไข/พัก/ลบโครงการได้

ดูรายงานการบริจาค: ดูข้อมูลการบริจาคทั้งหมดของวัดตนเอง, กรองข้อมูล, ส่งออกรายงาน

5.3. Flow การใช้งานฝั่งผู้บริจาค (ผ่าน Sale Page/Subdomain ของวัด)
เข้าถึง Sale Page ของวัด: ผู้บริจาคเข้าถึง URL เฉพาะของวัด (เช่น watname.yourplatform.com) ผ่าน Web Browser

เลือกโครงการบริจาค: Sale Page แสดงข้อมูลวัดและรายการโครงการบริจาค ผู้บริจาคเลือกโครงการที่ต้องการ

ระบุจำนวนเงินและข้อมูล: กรอกจำนวนเงิน, ชื่อ-นามสกุล, และข้อมูลติดต่อ (Email/เบอร์โทรศัพท์)

เลือกช่องทางการชำระเงิน: เลือก "PromptPay QR Code" หรือ "บัตรเครดิต/เดบิต"

ดำเนินการชำระเงิน:

PromptPay QR Code: ระบบสร้าง QR Code พร้อมเพย์ ผู้บริจาคสแกนและโอนเงิน ระบบตรวจสอบสถานะ

บัตรเครดิต/เดบิต: ระบบนำไปยังหน้า Payment Gateway ผู้บริจาคกรอกข้อมูลบัตรและยืนยัน

ยืนยันการบริจาคและรับใบอนุโมทนาบุญ:

เมื่อชำระเงินสำเร็จ ระบบแสดงหน้า "ขอบคุณ"

มี Link สำหรับดาวน์โหลดใบอนุโมทนาบุญ PDF แสดงบนหน้าจอทันที

อาจมีการส่ง Link ดาวน์โหลดใบอนุโมทนาบุญไปยัง Email ผู้บริจาค (ถ้ามี)
