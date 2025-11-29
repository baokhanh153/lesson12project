import streamlit as st

st.set_page_config(page_title='🏪Vương Quốc Mô Hình', page_icon=':sparkles:')

with st.sidebar:
	st.title('🏪Vương Quốc Mô Hình')
	st.header('Lady and gentlemen, welcome to the Kingdom of Models!')
	st.image('mo_hinh.jpg')
	st.write('Chúng tôi chuyên bán các mô hình nhân vật hoạt hoạt hình chất lượng.\
 Luôn cập nhật và đa dạng sản phẩm. Cam kết sự hài lòng của khách hàng với dịch\
 vụ chuyên nghiệp. Hãy đến và khám phá thế giới mô hình tại Vương Quốc Mô Hình!')
	st.write(':house: Địa chỉ cửa hàng:')
	st.write(':phone: Điện thoại liên hệ')

st.title('🏪Vương Quốc Mô Hình')
col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
	b1 = st.button('Conan')
with col2:
	b2 = st.button('Naruto')
with col3:
	b3 = st.button('One Piece')
with col4:
	b4 = st.button('Demon Slayer')
with col5:
	b5 = st.button('Jujutsu Kaisen')
with col6:
	b6 = st.button('Bluelock')

if b1:
	st.header('Danh sách mô hình Conan')
	col7, col8, col9, col10, col11, col12 = st.columns(6)
	with col7:
		st.image('conan.jpg',
			caption='Conan Thám Tử - Mã số: 001')
	with col8:
		st.image('kudo_shinichi.jpg',
			caption='kudo_shinichi vs conan - Mã số: 002')
	with col9:
		st.image('Kaito_kid.webp', caption='Mini Kaito Kid - Mã số: 003')
	with col10:
		st.image('hattori.jpg', caption='Hattori núp trong bóng tối - Mã số: 004')
	with col11:
		st.image('Ran.jpg', caption='Ran cute - Mã số: 005')
	with col12:
		st.image('Gin.webp',caption='Gin nằm trong nôi - Mã số: 006')
if b2:
	st.header('Danh sách mô hình Naruto')
	col13, col14, col15, col16,col17, col18 = st.columns(6)
	with col13:
		st.image('boruto.jpg',
			caption='boruto hồi trẻ - Mã số: 001')
	with col14:
		st.image('minato.jpg',
			caption='Minato tổng hợp chiêu - Mã số: 002')
	with col15:
		st.image('Naruto.webp', caption='Naruto thiền nhân - Mã số: 003')
	with col16:
		st.image('madara.webp', caption='Madara thập vĩ - Mã số: 004')
	with col17:
		st.image('Kakashi.webp', caption='Kakashi chidrori - Mã số: 005')
	with col18:
		st.image('sasuke.jpg', caption='sasuke bật susanoo - Mã số: 006')
if b3:
	st.header('Danh sách mô hình One Piece')
	col19, col20, col21, col22,col23, col24 = st.columns(6)
	with col19:
		st.image('luffy.jpg',
			caption='luffy gear 5 - Mã số: 001')
	with col20:
		st.image('zoro.jpg',
			caption='zoro kiếm sĩ - Mã số: 002')
	with col21:
		st.image('sanji.jpg', caption='sanji germa 66 - Mã số: 003')
	with col22:
		st.image('gol_d_roger.jpg', caption='gold roger - Mã số: 004')
	with col23:
		st.image('kaido.webp', caption='Kaido dạng bán thú - Mã số: 005')
	with col24:
		st.image('ace.webp', caption='ace hỏa quyền - Mã số: 006')
if b4:
	st.header('Danh sách mô hình Demon Slayer')
	col25, col26, col27, col28,col29, col30 = st.columns(6)
	with col25:
		st.image('tanjiro.jpeg',
			caption='tanjiro hơi thở mặt trời - Mã số: 001')
	with col26:
		st.image('daki.webp',
			caption='Daki quỷ thượng huyền - Mã số: 002')
	with col27:
		st.image('rengoku.jpg', caption='Rengoku viêm trụ - Mã số: 003')
	with col28:
		st.image('kukusubo.webp', caption='Kukusubo hơi thở mặt trăng  - Mã số: 004')
	with col29:
		st.image('ha_tru.jpg', caption='hà trụ lạnh lùng - Mã số: 005')
	with col30:
		st.image('akaza.png', caption='akaza thượng tam - Mã số: 006')
if b5:
	st.header('Danh sách mô hình Jujutsu Kaisen')
	col31, col32, col33, col34, col35, col36 = st.columns(6)
	with col31:
		st.image('sukuna.jpg',
			caption='sukuna - Mã số: 001')
	with col32:
		st.image('toji.webp',
			caption='toji thợ săn -  Mã số: 002')
	with col33:
		st.image('Mai.webp', caption='zenin Mai - Mã số: 003')
	with col34:
		st.image('gojo.jpg', caption='gojo  - Mã số: 004')
	with col35:
		st.image('Itadori.jpg', caption='yuri itadori - Mã số: 005')
	with col36:
		st.image('megumi.webp', caption='megumi  - Mã số:006')
if b6:
	st.header('Danh sách mô hình Bluelock')
	col37, col38, col39, col40, col41, col42 = st.columns(6)
	with col37:
		st.image('isagi.jpg',
			caption='isagi - Mã số: 001')
	with col38:
		st.image('rin_itoshi.jpg',
			caption='rin itoshi phá hoại - Mã số: 002')
	with col39:
		st.image('bachira.jpg', caption='bachira nghệ nhân - Mã số: 003')
	with col40:
		st.image('kunigami.jpg', caption='kunigami lạnh lùng boy - Mã số: 004')
	with col41:
		st.image('chigiri.jpg', caption='chigiri tốc độ - Mã số: 005')
	with col42:
		st.image('nagi.jpg', caption='Nagi thiên tài - Mã số:006')

st.header('Đặt hàng')
with st.form('Đơn đặt hàng'):

	topics = ('Conan', 'Naruto', 'One Piece', 'Demon Slayer', 'Jujutsu Kaisen', 'Bluelock')
	option_topic = st.selectbox('Chủ đề mô hình', topics)

	codes =('001', '002', '003', '004', '005', '006')
	option_code = st.selectbox('Mã số mô hình', codes)

	nums = st.slider('Số lượng bạn muốn đặt:', 1, 1000000, 1)

	name = st.text_input('Họ và tên')

	phone = st.text_input('Số điện thoại nhà riêng')

	address = st.text_input('Địa chỉ giao hàng')
	bill = {'Loại mô hình:': option_topic, 'Mã số:': option_code, 'Số lượng:': nums,
			'Họ tên khách hàng:': name, 'Số điện thoại liên hệ:': phone, 'Địa chỉ giao hàng:': address}

	submmitted = st.form_submit_button("Xác nhận")
	if submmitted:
		st.header('Bạn đã chọn:')
		for x, y in bill.items():
					st.write(x, y)
print_bill = st.checkbox('In hóa đơn')
if print_bill:
	ans = ''
	for x in bill:
		ans += str(x) + '' + str(bill[x]) + '\n'
	st.download_button('In hóa đơn', ans)