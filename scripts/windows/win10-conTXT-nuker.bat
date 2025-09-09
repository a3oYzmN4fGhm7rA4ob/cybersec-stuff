::Should make a large, undeletable file on older windows 10 systems. This is due to an issue existing from the MSDOS era.
:: Adjust the exact file size to your liking.
fsutil file createnew "\\.\C:/Users/Public/con.txt" 107374182400