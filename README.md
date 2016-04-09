# wikipedia-interlanguage-titles
find the translation of all the titles one language in another language on wikipedia


## Usage
```
    python wikititles.py -p /path/to/thwiki-20160305-page.sql -l /path/to/thwiki-20160305-langlinks.sql -c en
```

sample results:
```
page_id ori_title target_title
545 ดาราศาสตร์ Astronomy
547 ภูมิศาสตร์ Geography
611 พันทิป.คอม Pantip.com
613 พันธุ์ทิพย์พลาซ่า Pantip Plaza
615 วิทยาการคอมพิวเตอร์ Computer science
616 คณิตศาสตร์ Mathematics
618 การประมวลสารสนเทศ Information processing
619 การเมือง Politics
627 Ans User:ans
628 ทดลองเขียน Wikipedia:Sandbox
660 ดิมมูบอร์เกียร์ Dimmu Borgir
...
```
