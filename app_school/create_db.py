import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app_school import db

from app_school.xu_ly.Xu_ly_Model import Base

# Tạo cơ sở dữ liệu và các bảng
db.create_all()
print("Cơ sở dữ liệu đã được tạo thành công!")
