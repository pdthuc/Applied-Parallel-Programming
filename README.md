# Applied-Parallel-Programming

## Đồ án môn Lập trình song song ứng dụng
### GVHD: Trần Trung Kiên
### Nhóm: 04
### DANH SÁCH THÀNH VIÊN:
  1. 18120167 - Nguyễn Viết Dũng - kaiser1038
  2. 18120579 - Đặng Minh Thọ - MinhTho-162
  3. 18120584 - Phạm Đình Thục - pdthuc

### THÙNG CHỨA GITHUB:
- Link github: https://github.com/pdthuc/Applied-Parallel-Programming

### KẾ HOẠCH THỰC HÀNH:
- Link google sheets: 

### LINK GOOGLE COLAB 
- [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1B78maMjn4Kj92OiXho6Zem89KnpvBc9k)
- Link: https://colab.research.google.com/drive/1B78maMjn4Kj92OiXho6Zem89KnpvBc9k

### **1.1 MÔ TẢ TỔNG QUAN**
**Tên đề tài:** 
Image-Search-using-Parallel-Computing
*(Công cụ Tìm kiếm Hình ảnh bằng kỹ thuật truy vấn truy xuất hình ảnh dựa trên nội dung liên quan )*

Với sự phát triển mạnh mẽ của internet, mọi người có thể tiếp cận với một lượng lớn thông tin. Do đó, việc truy xuất thông tin quan tâm trở nên rất khó khăn.
Chẳng hạn như ảnh, video ở nhiều định dạng khác nhau như JPG, PNG, BMP và thậm chí cả GIF. 

-> Do đó cần có một công cụ tìm kiếm hình ảnh để tìm kiếm các hình ảnh liên quan và chính xác.

Truy xuất hình ảnh dựa trên nội dung tìm kiếm các phương pháp để index, browse và truy vấn cơ sở dữ liệu hình ảnh lớn bằng cách sử dụng các phương pháp feature extraction và so sánh các feature.

- **Input:** Hình ảnh trong dataset.
- **Output:** Những hình ảnh liên quan với ảnh input từ dataset.


### **1.2 VẤN ĐỀ SONG SONG HÓA**

Ứng dụng nảy có cần song song hóa hay không?

**-> Có**

 Vì:
- Bài toán sẽ làm việc với một số lượng lớn hình ảnh
- Thuật toán xử lý và lưu trữ dữ liệu hình ảnh
- Sử dụng các phương pháp feature extraction và xử lý quá trình extraction

Với sự trợ giúp của song song, quá trình nặng nhọc này có thể được chia thành nhiều tác vụ nhỏ hơn và thực hiện chúng cùng một lúc. Điều này giúp chương trình chạy nhanh hơn, mượt mà hơn và sử dụng tài nguyên hiệu quả hơn rất nhiều. Do đó, việc thực hiện song song trong tìm kiếm hình ảnh có thể giảm đáng kể thời gian truy xuất và cải thiện hiệu suất của hệ thống truy xuất vốn rất quan trọng trong 

### TÀI LIỆU THAM KHẢO
Để hoàn thành đồ án này, nhóm mình đã tham khảo những tài liệu sau:

Và nhóm xin gửi lời cảm ơn đặc biệt đến https://stackoverflow.com/ vì đã hỗ trợ nhóm trong quá trình làm đồ án này. :">
