mysql --user="root" --password="root" --database="tokensystem" --execute="select v.vendorName, date(t.tokenDateTime), count(*) from webapp_token t join webapp_vendor v where v.id=t.vendor_id and MONTH(t.tokenDateTime) = MONTH(NOW()) group by date(t.tokenDateTime), t.vendor_id;">C:\Users\mmanojkumar\Desktop\TokenSystem\%date:~4,2%-%date:~10,4%.xls

