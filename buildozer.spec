[app]

# অ্যাপের নাম (এটি আপনি পরে বদলাতে পারবেন)
title = MyPocoApp

# প্যাকেজ নাম (ছোট হাতের অক্ষরে)
package.name = mehrabapp

# প্যাকেজ ডোমেইন
package.domain = org.test

# সোর্স ফাইল কোথায় আছে (ডট মানে বর্তমান ফোল্ডার)
source.dir = .

# কোন কোন ফাইল অ্যাপে ঢুকবে
source.include_exts = py,png,jpg,kv,atlas

# ভার্সন
version = 0.1

# কি কি লাইব্রেরি লাগবে (এখন শুধু পাইথন আর কিভি)
requirements = python3,kivy

# স্ক্রিন কেমন থাকবে
orientation = portrait

# এন্ড্রয়েড আর্কিটেকচার (আপনার Poco ফোনের জন্য এটিই সেরা)
android.archs = arm64-v8a

# এন্ড্রয়েড এপিআই লেভেল (ডিফল্ট ৩১ রাখা ভালো)
android.api = 31

# ব্যাকআপ অপশন
android.allow_backup = True

# বিল্ডোজার কনফিগারেশন
[buildozer]
log_level = 2
warn_on_root = 1
