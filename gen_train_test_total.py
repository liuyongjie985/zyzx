# coding:utf-8
import os
import re
import random

inpath = 'output/filtered_bank_sms_sample.txt'
# inpath = 'test'
place = [u'北京', u'天津', u'上海', u'重庆', u'新疆', u'乌鲁木齐', u'西藏', u'宁夏', u'内蒙古', u'广西', u'黑龙江', u'哈尔滨',
         u'大庆', u'齐齐哈尔',
         u'佳木斯', u'鸡西',
         u'鹤岗', u'双鸭山', u'牡丹江', u'伊春', u'七台河', u'黑河', u'绥化', u'五常', u'双城', u'尚志',
         u'纳河', u'虎林', u'密山', u'铁力',
         u'同江', u'富锦', u'绥芬河',
         u'海林', u'宁安', u'穆林', u'北安', u'五大连池', u'肇东', u'海伦', u'安达', u'吉林', u'长春',
         u'四平', u'辽源', u'通化', u'白山',
         u'松原', u'白城', u'九台市',
         u'榆树市', u'德惠市', u'舒兰市', u'桦甸市', u'蛟河市', u'磐石市', u'公主岭市', u'双辽市',
         u'梅河口市', u'集安市', u'临江市',
         u'大安市', u'洮南市', u'延吉市',
         u'图们市', u'敦化市', u'龙井市', u'珲春市', u'和龙市', u'辽宁', u'沈阳', u'大连', u'鞍山',
         u'抚顺', u'本溪', u'丹东', u'锦州',
         u'营口', u'阜新', u'辽阳', u'盘锦',
         u'铁岭', u'朝阳', u'葫芦岛', u'中寨', u'周家', u'周家屯', u'周口', u'庄河北', u'庄桥',
         u'诸城', u'珠海', u'珠海北', u'诸暨',
         u'朱家沟', u'褚家湾', u'朱家窑', u'驻马店', u'驻马店西', u'准格尔', u'涿州',
         u'涿州东', u'卓资东', u'朱日和',
         u'朱石寨', u'珠斯花', u'竹园坝', u'株洲', u'株洲南', u'株洲西',
         u'淄博', u'子长', u'自贡', u'紫荆关',
         u'资溪', u'资阳', u'紫阳', u'资阳北', u'资中', u'资中北',
         u'子洲', u'邹城', u'遵义', u'遵义南', u'遵义西', u'左家', u'左岭', u'昆明', u'泉州']


# 17县级市——新民、瓦房店、普兰、庄河、海城、东港、凤城、凌海、北镇、大石桥、盖州、灯塔、调兵山、开原、凌源、北票、兴城
# 4，【河北】：11地级市——石家庄、唐山、邯郸、秦皇岛、保定、张家口、承德、廊坊、沧州、衡水、邢台
# 22县级市——辛集市、藁城市、晋州市、新乐市、鹿泉市、遵化市、迁安市、武安市、南宫市、沙河市、涿州市、定州市、安国市、高碑店市、泊头市、任丘市、黄骅市、河间市、霸州市、三河市、冀州市、深州市
# 5，【山东】：17地级市——济南、青岛、淄博、枣庄、东营、烟台、潍坊、济宁、泰安、威海、日照、莱芜、临沂、德州、聊城、菏泽、滨州
# 28县级市——章丘、胶南、胶州、平度、莱西、即墨、滕州、龙口、莱阳、莱州、招远、蓬莱、栖霞、海阳、青州、诸城、安丘、高密、昌邑、兖州、曲阜、邹城、乳山、文登、荣成、乐陵、临清、禹城
# 6，【江苏】：13地级市——南京、镇江、常州、无锡、苏州、徐州、连云港、淮安、盐城、扬州、泰州、南通、宿迁
# 27县级市——江阴市、宜兴市、邳州市、新沂市、金坛市、溧阳市、常熟市、张家港市、太仓市、昆山市、吴江市、如皋市、通州市、海门市、启东市、东台市、大丰市、高邮市、江都市、仪征市、丹阳市、扬中市、句容市、泰兴市、姜堰市、靖江市、兴化市
# 7，【安徽】：17地级市——合肥、蚌埠、芜湖、淮南、亳州、阜阳、淮北、宿州、滁州、安庆、巢湖、马鞍山、宣城、黄山、池州、铜陵
# 5县级市——界首、天长、明光、桐城、宁国
# 8，【浙江】：11地级市——杭州、嘉兴、湖州、宁波、金华、温州、丽水、绍兴、衢州、舟山、台州
# 22县级市——建德市、富阳市、临安市、余姚市、慈溪市、奉化市、瑞安市、乐清市、海宁市、平湖市、桐乡市、诸暨市、上虞市、嵊州市、兰溪市、义乌市、东阳市、永康市、江山市、临海市、温岭市、龙泉市
# 9，【福建】：9地级市——福州、厦门、、三明、南平、漳州、莆田、宁德、龙岩
# 14县级市——福清市、长乐市、永安市、石狮市、晋江市、南安市、龙海市、邵武市、武夷山、建瓯市、建阳市、漳平市、福安市、福鼎市
# 10，【广东】：21地级市——广州、深圳、汕头、惠州、珠海、揭阳、佛山、河源、阳江、茂名、湛江、梅州、肇庆、韶关、潮州、东莞、中山、清远、江门、汕尾、云浮
# 22县级市——增城市、从化市、乐昌市、南雄市、台山市、开平市、鹤山市、恩平市、廉江市、雷州市 吴川市、高州市、化州市、高要市、四会市、兴宁市、陆丰市、阳春市、英德市、连州市、普宁市、罗定市
# 11，【海南】：2地级市——海口、三亚
# 6县级市——琼海、文昌、万宁、五指山、儋州、东方
# 12，【云南】：8地级市——、曲靖、玉溪、保山、昭通、丽江、普洱、临沧
# 9县级市——安宁市、宣威市、个旧市、开远市、景洪市、楚雄市、大理市、潞西市、瑞丽市
# 13，【贵州】：4地级市——贵阳、六盘水、遵义、安顺
# 9县级市——清镇市、赤水市、仁怀市、铜仁市、毕节市、兴义市、凯里市、都匀市、福泉市
# 14，【四川】：18地级市——成都、绵阳、德阳、广元、自贡、攀枝花、乐山、南充、内江、遂宁、广安、泸州、达州、眉山、宜宾、雅安、资阳
# 14县级市——都江堰市、彭州市、邛崃市、崇州市、广汉市、什邡市、绵竹市、江油市、峨眉山市、阆中市、华蓥市、万源市、简阳市、西昌市
# 15，【湖南】：13地级市——长沙、株洲、湘潭、衡阳、岳阳、郴州、永州、邵阳、怀化、常德、益阳、张家界、娄底
# 16县级市——浏阳市、醴陵市、湘乡市、韶山市、耒阳市、常宁市、武冈市、临湘市、汨罗市、津市市、沅江市、资兴市、洪江市、冷水江市、涟源市、吉首市
# 16，【湖北】：12地级市——武汉、襄樊、宜昌、黄石、鄂州、随州、荆州、荆门、十堰、孝感、黄冈、咸宁
# 24县级市——大冶市、丹江口市、洪湖市、石首市、松滋市、宜都市、当阳市、枝江市、老河口市、枣阳市、宜城市、钟祥市、应城市、安陆市、汉川市、麻城市、武穴市、赤壁市、广水市、仙桃市、天门市、潜江市、恩施市、利川市
# 17，【河南】：17地级市——郑州、洛阳、开封、漯河、安阳、新乡、周口、三门峡、焦作、平顶山、信阳、南阳、鹤壁、濮阳、许昌、商丘、驻马店
# 21县级市——巩义市、新郑市、新密市、登封市、荥阳市、偃师市、汝州市、舞钢市、林州市、卫辉市、辉县市、沁阳市、孟州市、禹州市、长葛市、义马市、灵宝市、邓州市、永城市、项城市、济源市
# 18，【山西】：11地级市——太原、大同、忻州、阳泉、长治、晋城、朔州、晋中、运城、临汾、吕梁
# 11县级市——古交、潞城、高平、介休、永济、河津、原平、侯马、霍州、孝义、汾阳
# 19，【陕西】：10地级市——西安、咸阳、铜川、延安、宝鸡、渭南、汉中、安康、商洛、榆林
# 3县级市——兴平市、韩城市、华阴市
# 20，【甘肃】：12地级市——兰州、天水、平凉、酒泉、嘉峪关、金昌、白银、武威、张掖、庆阳、定西、陇南
# 4县级市——玉门市、敦煌市、临夏市、合作市
# 21，【青海】：1地级市——西宁
# 2县级市——格尔木、德令哈
# 22，【江西】：11地级市——南昌、九江、赣州、吉安、鹰潭、上饶、萍乡、景德镇、新余、宜春、抚州
# 10县级市——乐平市、瑞昌市、贵溪市、瑞金市、南康市、井冈山市、丰城市、樟树市、高安市、德兴市
# 23，【台湾】：7市——台北、台中、基隆、高雄、台南、新竹、嘉义
# 16县级市——板桥市、宜兰市、竹北市、桃园市、苗栗市、丰原市、彰化市、南投市、太保市、斗六市、新营市、凤山市、屏东市、台东市、花莲市、马公市
# 四、【特别行政区】
# 1，【香港】
# 2，【澳门】
# #
# #
# #
# #
# 阿巴嘎旗	阿城	阿木尔	阿尔山	阿尔山北
# 艾河	艾家村	阿金	阿克苏	阿克陶
# 阿拉山口	阿勒泰	阿里河	阿南庄	安达
# 安德	安多	昂昂溪	安广	安化
# 安家	安靖	安康	安口窑	安陆
# 安平	安庆	安庆西	安仁	鞍山
# 鞍山西	安顺	安顺西	安塘	安亭北
# 安图	安图西	安阳	安阳东	敖汉
# 鳌江	敖力布告	敖头	阿图什	阿乌尼
# B
# 巴楚	巴东	八方山	八虎力	白壁关
# 白城	白沟	柏果	白河	白河东
# 白河县	白涧	白芨沟	白鸡坡	白奎堡
# 白狼	百里峡	白马井	白旗	白泉
# 百色	白山市	白沙坡	白沙铺	白水江
# 白水镇	白洋淀	百宜	白音察干	白音华南
# 白音胡硕	白银市	白银西	白云鄂博	白桦排
# 巴林	八面城	八面通	板城	半截河
# 班猫箐	板塘	宝坻	保定	保定东
# 宝华山	宝鸡	宝鸡南	保康	宝林
# 宝龙山	宝清	宝泉岭	包头	包头东
# 包头西	八仙筒	巴彦高勒	鲅鱼圈	巴中
# 霸州	霸州西	北安	北碚	北戴河
# 北海	北滘	北京	北京东	北京南
# 北京西	北井子	北流	北马圈子	北票南
# 北屯	北屯市	背荫河	北宅	栟茶
# 蚌埠	蚌埠南	本溪	本溪新城	贲红
# 碧江	笔架山	滨海	滨海北	彬县
# 宾阳	滨州	璧山	博鳌	博白
# 博克图	博乐	勃利	泊头	博兴
# 亳州	布海
# C
# 蔡家沟	蔡家坡	苍南	苍石	苍溪
# 沧州	沧州西	草海	草河口	曹家营子
# 草市	曹县	曹子里	岑溪	查布嘎
# 察尔汗	查干湖	柴沟堡	柴河	岔江
# 茶陵南	长城	长冲	长春	长春西
# 常德	长甸	长发屯	长葛	长虹
# 昌乐	昌黎	长临河	长农	常平
# 昌平北	常平东	常平南	长坡岭	长庆桥
# 长沙	常山	长沙南	长山屯	长沙西
# 长寿北	长寿湖	长汀南	长汀镇	昌图
# 昌图西	长武	长兴	长兴南	长垣
# 长征	长治	长治北	常州	常州北
# 常庄	巢湖	巢湖东	潮汕	朝天
# 朝天南	潮阳	朝阳川	朝阳村	朝阳地
# 朝阳南	朝阳镇	朝中	潮州	察素齐
# 册亨	承德	承德东	成都	成都东
# 成都南	成高子	城固	城固北	成吉思汗
# 陈官营	城子坦	晨明	辰清	辰溪
# 陈相屯	郴州	郴州西	车转湾	赤壁
# 赤壁北	赤峰	赤峰西	池州	重庆
# 重庆北	重庆南	重庆西	崇信	崇左
# 春阳	楚山	楚雄南	滁州	滁州北
# 嵯岗	慈利	磁山	磁县	磁窑
# 从江	翠岗	崔黄口
# D
# 大安	大安北	大坝	大板	大堡
# 打柴沟	大磴沟	大东	大方南	大丰
# 大关	大官屯	大孤山	大红旗	大灰厂
# 大虎山	带岭	代县	岱岳	达家沟
# 大涧	大口屯	大朗镇	达拉特西	大理
# 大荔	大连	大连北	大荔北	大林
# 大民屯	丹东	丹东西	丹凤	砀山
# 砀山南	当涂东	当雄	当阳	丹徒
# 丹霞山	丹阳	丹阳北	到保	道滘
# 道清	道州	大盘石	大平房	大埔
# 大庆	大庆东	大青沟	大庆西	大石桥
# 大石头	大石寨	大田边	大同	大通西
# 大屯	大旺	大湾子	大武口	大西
# 大兴	大兴沟	大辛庄	大雁	大杨树
# 大冶北	大营	大英东	大营镇	大余
# 大战场	大杖子	达州	大竹园	大苴
# 大足南	德安	德保	德伯斯	德昌
# 得耳布尔	德惠	德惠西	德令哈	登沙河
# 灯塔	邓州	德清	德清西	德兴
# 德兴东	德阳	德州	德州东	垫江
# 甸心	滴道	定边	鼎湖东	鼎湖山
# 定南	定陶	定西	定襄	定西北
# 定远	定州	定州东	低窝铺	低庄
# 东安东	东边井	东城南	东戴河	东二道河
# 东方	东方红	东丰	东富	东港北
# 东沟门	东莞	东莞东	东光	东海
# 东海县	洞井	东京城	东来	洞庙河
# 东明县	东升	东胜西	东台	东通化
# 东湾	东乡	东兴	东辛庄	东营
# 东营南	东淤地	东镇	东至	东庄
# 斗沟子	豆罗	豆庄	端州	都昌
# 都格	对青山	兑镇	都江堰	杜拉尔
# 敦化	敦煌	独山	渡市	都匀
# 都匀东
# E
# 峨边	鄂尔多斯	额济纳	峨眉	峨眉山
# 恩施	阿房宫	二道沟门	二道沙河	二井
# 二连	二龙	二龙山屯	二龙屯	二营
# 鄂州	鄂州东
# F
# 发耳	繁昌西	防城港北	范家屯	范镇
# 繁峙	费县	丰城	凤城东	丰城南
# 丰都	丰广	奉化	凤凰城	凤凰机场
# 丰乐镇	枫林	风陵渡	丰水村	丰顺
# 冯屯	凤县	丰镇	凤州	汾河
# 汾阳	分宜	佛岭	佛坪	佛山
# 佛山西	福安	富川	福鼎	富海
# 福海	富锦	福巨	富拉尔基	涪陵
# 涪陵北	福利屯	阜南	抚宁	阜宁
# 富宁	福清	福泉	芙蓉南	福山口
# 福山镇	复盛	抚顺北	扶绥	福田
# 浮图峪	富县东	阜新南	阜阳	扶余
# 富裕	富源	抚远	富源北	扶余北
# 福州	抚州	抚州东	福州南
# G
# 盖州	盖州西	甘草店	甘谷	甘河
# 甘洛	甘旗卡	甘泉北	赶水东	干塘
# 赣州	高安	高碑店	高碑店东	藁城
# 藁城南	高村	高峰	高各庄	皋兰
# 高林屯	高密	高平	高山子	高台
# 高台南	高台子	高滩	高头	高邑
# 高邑西	高州	葛店南	格尔木	葛根庙
# 革居	根河	恭城	共青城	巩义
# 巩义南	公营子	公主岭	公主岭南	沟帮子
# 广安	广安南	官高	广德	广汉北
# 光明	光明城	广南卫	广南县	广宁
# 广宁寺	光山	广水	广通北	广元
# 光泽	广州	广州北	广州东	广州南
# 关林	关岭	观沙岭	官厅	官厅西
# 冠豸山	瓜州	谷城	古城镇	古城子
# 古东	贵定	贵定北	贵定南	贵定县
# 贵港	桂林	桂林北	桂林西	归流河
# 桂平	贵溪	贵阳	贵阳北	贵阳东
# 古交	古浪	古莲	郭家店	果松
# 涡阳	虢镇	谷山	孤山口	固始
# 古田	古田北	古田会址	固原	菇园
# 古镇	固镇
# H
# 哈达铺	哈尔滨	哈尔滨北	哈尔滨东	哈尔滨西
# 海安县	海北	海城	海城西	海东西
# 海口	海口东	海拉尔	海林	海伦
# 海宁	海宁西	海石湾	海阳	海阳北
# 海晏	哈拉海	哈力图	哈密	韩城
# 汉川	寒葱沟	邯郸	邯郸东	韩府湾
# 杭州	杭州东	涵江	汉口	寒岭
# 韩麻营	汉寿	汉阴	汉源	汉中
# 浩良河	哈日努拉	鹤北	鹤壁	河边
# 鹤壁东	合川	河唇	合肥	合肥北城
# 合肥南	鹤岗	黑冲滩	黑河	黑井
# 黑水	黑台	黑旺	贺家店	河津
# 河口北	河口南	鹤立	和龙	河洛营
# 横道河子	横峰	横沟桥东	衡山	衡山西
# 衡水	衡水北	衡阳	衡阳东	和平
# 合浦	鹤庆	贺胜桥东	和什托洛盖	和硕
# 荷塘	和田	合阳北	河源	菏泽
# 贺州	红安西	洪洞	红光镇	红果
# 洪河	红江	宏庆	红旗营	红山
# 红砂岘	红寺堡	洪洞西	红岘台	红星
# 红兴隆	红彦	后湖	侯马	侯马西
# 鲘门	猴山	后寨	华城	化德
# 花湖	淮安	淮北	淮北北	淮滨
# 怀化	怀化南	怀集	淮南	淮南东
# 怀仁	怀柔	怀柔北	槐荫	华家
# 花家庄	桦林	桦南	黄柏	潢川
# 黄村	黄冈	黄冈东	黄冈西	黄瓜园
# 黄河景区	黄口	黄陵	黄陵南	黄流
# 黄梅	黄泥河	黄山	黄山北	黄石
# 黄石北	黄松甸	黄土店	黄羊滩	黄羊湾
# 黄羊镇	湟源	黄州	华蓥	怀仁东
# 换新天	花棚子	花桥	华容东	华容南
# 华山	华山北	花山南	花土坡	花园
# 花园口	化州	虎尔虎拉	呼和浩特	呼和浩特东
# 惠安	会昌北	珲春	惠东	惠环
# 汇流河	惠农	惠山	会同	徽县
# 惠州	惠州南	湖口	呼兰	虎林
# 葫芦岛	葫芦岛北	呼鲁斯太	虎门	霍城
# 霍尔果斯	获嘉	火炬沟	霍林郭勒	霍邱
# 霍州	霍州东	虎山	鄠邑	湖州
# 互助
# I
# J
# 加格达奇	佳木斯	吉安	集安	加南
# 尖峰	江都	江华	姜家	将乐
# 江门东	江密峰	江宁	江宁西	江桥
# 江山	江所田	姜堰	江永	江油
# 江油北	江源	剑门关	建宁县北	建瓯
# 建瓯西	建三江	尖山	建始	建水
# 建阳	简阳	简阳南	交城	蛟河
# 蛟河西	角美	胶州	焦作	嘉善
# 甲山	嘉善南	嘉祥	嘉兴	嘉兴南
# 嘉峪关	嘉峪关南	鸡东	界首市	介休
# 介休东	揭阳	纪家沟	吉林	芨岭
# 即墨北	济南	济南东	济南西	金宝屯
# 金昌	晋城	金城江	靖边	泾川
# 旌德	景德镇	景德镇北	井店	井冈山
# 静海	精河南	荆门	井南	金沟屯
# 经棚	京山	景泰	镜铁山	靖西
# 泾县	井陉	靖远	靖远西	晋中
# 靖州	荆州	景州	锦和	锦河
# 金华	金华南	济宁	集宁南	晋江
# 锦界	金山北	金山屯	劲松	进贤
# 进贤南	金银潭	金月湾	缙云	缙云西
# 金寨	锦州	金州	晋州	锦州南
# 稷山	吉首	吉舒	九江	九郎山
# 九龙	酒泉	酒泉南	九三	九台
# 九台南	九营	吉文	鸡西	绩溪北
# 吉新河	绩溪县	济源	蓟州	鄄城
# 莒南	峻德	军粮城北	句容西	莒县
# 巨野
# K
# 开安	凯北	开封	开封北	开福寺
# 开化	开江	凯里	凯里南	开鲁
# 开通	开阳	开原	开原西	喀喇其
# 卡伦	康金井	康庄	喀什	克东
# 克拉玛依	岢岚	克山	克一河	口前
# 库车	库都尔	库尔勒	奎山	葵潭
# 奎屯	库伦	昆独仑召	昆明	昆明南
# 昆山	昆山南	昆阳
# L
# 拉白	拉古	拉哈	来宾	来宾北
# 濑湍	莱芜东	莱西	莱西北	莱阳
# 涞源	拉林	喇嘛甸	蓝村	兰岗
# 廊坊	廊坊北	狼尾山	朗乡	阆中
# 兰家屯	兰考	兰考南	兰岭	兰陵北
# 兰溪	兰州	兰州东	兰州西	兰州新区
# 老边	老城镇	老莱	老营	拉萨
# 拉鲊	乐昌	乐昌东	乐东	乐都
# 乐都南	耒阳	耒阳西	雷州	乐平市
# 乐山	乐善村	两当	梁底下	良各庄
# 两家	超梁沟	梁平	梁平南	梁山
# 廉江	连江	莲江口	连山关	涟源
# 连云港东	连珠山	寮步	聊城	辽阳
# 辽源	辽中	黎城	利川	离堆公园
# 李家	丽江	李家坪	利津南	沥林北
# 醴陵	醴陵东	里木店	临城	林东
# 临汾	临汾西	临高南	灵宝	灵宝西
# 灵璧	陵城	凌海	零陵	灵丘
# 灵山	灵石	灵石东	陵水	冷水江东
# 灵武	凌源	凌源东	临海	临河
# 蔺家楼	临江	林口	临澧	临清
# 林盛堡	林西	临西	临湘	临沂
# 临邑	临沂北	临颍	林源	临泽
# 临泽南	林子头	礼泉	李石寨	丽水
# 溧水	梨树镇	黎塘	六安	六道河子
# 六个鸡	柳沟	柳河	六合镇	刘家店
# 刘家河	柳江	柳家庄	柳林南	柳毛
# 六盘山	六盘水	流水沟	柳园	柳园南
# 六枝	柳州	李旺	澧县	溧阳
# 立志	隆安东	隆昌	隆昌北	龙池
# 龙川	龙洞堡	龙丰	龙沟	龙骨甸
# 龙华	隆化	龙嘉	龙江	龙井
# 龙口市	龙里北	龙南	陇南	龙泉寺
# 龙山镇	龙市	龙塘坝	陇西	陇县
# 龙岩	龙游	龙镇	娄底	娄底南
# 娄山关南	滦河	滦河沿	滦平	滦县
# 潞城	陆川	鹿道	略阳	鲁番
# 陆丰	禄丰南	芦沟	麓谷	庐江
# 芦家庄	路口铺	陆良	卢龙	轮台
# 罗城	漯河	漯河西	珞璜南	罗江东
# 洛门	罗平	罗山	洛湾三江	洛阳
# 洛阳东	洛阳龙门	罗源	洛碛	庐山
# 鲁山	露水河	芦台	鹿寨	鹿寨北
# 绿博园	绿化	吕梁
# M
# 马鞍山	马鞍山东	麻城	麻城北	马兰
# 马莲河	马林	麻柳	马龙	玛纳斯
# 忙罕屯	满归	满洲里	毛坝	毛坝关
# 茅草坪	毛陈	帽儿山	茂林	茂名
# 茂名西	茂舍祖	马三家	麻尾	麻阳
# 梅河口	梅江	美兰	眉山	眉山东
# 美溪	梅州	门达	猛洞河	孟家岗
# 孟津	蒙自	蒙自北	门源	渑池
# 渑池南	免渡河	冕宁	勉县	绵阳
# 庙城	庙岭	庙庄	弥渡	弥勒
# 汨罗	汨罗东	明港东	明城	明光
# 明水河	明珠	民和南	闵集	民乐
# 闽清北	民权	民权北	岷县	密山
# 密山西	米沙子	米易	密云北	米脂
# 磨刀石	莫尔道嘎	漠河	无为	牡丹江
# 穆棱	沐滂	牟平	墨玉	暮云
# N
# 乃林	奈曼	内江	南陵	南博山
# 南部	南岔	南昌	南昌西	南城
# 南城司	南充	南充北	南仇	南大庙
# 南丹	南芬	南芬北	南丰	南观村
# 南河川	南湖东	南江	南江口	南京
# 南靖	南京南	南口	南口前	南朗
# 南宁	南宁东	南宁西	南平北	南平南
# 南通	南头	南洼	南湾子	南翔北
# 南雄	南阳	南阳寨	南峪	南杂木
# 南召	那曲	内乡	纳雍	讷河
# 内江北	内江南	能家	嫩江	娘子关
# 碾子山	聂河	捏掌	尼勒克	宁安
# 宁波	宁德	宁东	宁东南	宁国
# 宁海	宁陵县	宁明	宁强南	宁武
# 宁乡	牛家	牛庄	农安	暖泉
# O
# P
# 徘徊北	磐安镇	盘古	盘关	潘家店
# 盘锦	盘锦北	磐石	攀枝花	盘州
# 泡子	裴德	蓬安	蓬莱市	彭山北
# 彭水	彭阳	彭泽	彭州	偏岭
# 庙山	皮口	平安	平安驿	平坝南
# 屏边	平昌	平顶山	平顶山西	平度
# 平房	平关	平果	平河口	平湖
# 平凉	平凉南	平罗	平南南	平泉
# 平山	坪上	平社	坪石	平台
# 平田	平旺	萍乡	凭祥	萍乡北
# 平型关	平洋	平遥	平遥古城	平邑
# 平峪	平原	平原堡	平原东	平庄
# 平庄南	皮山	郫县	郫县西	邳州
# 坡底下	鄱阳	普安	普安县	蒲城
# 蒲城东	普定	普兰店	普宁	莆田
# 普湾	普雄	濮阳	普者黑
# Q
# 迁安	乾安	前锋	千河	黔江
# 潜江	前进镇	前磨头	前山	前苇塘
# 乾县	千阳	桥北	桥头	桥湾
# 桥西	七甸	祁东	奇峰塔	齐哈日格图
# 祁家堡	綦江东	七龙星	祁门	秦安
# 蕲春	庆安	青白江东	青城山	青川
# 青岛	青岛北	青堆	清河城	清河门
# 清涧县	青莲	青龙	青山	青神
# 庆盛	清水	清水北	清水县	青田
# 青铜峡	青县	清徐	清原	清远
# 青州市	秦皇岛	秦家	秦家庄	秦岭
# 沁县	沁阳	钦州东	琼海	棋盘
# 齐齐哈尔	齐齐哈尔南	岐山	戚墅堰	七苏木
# 七台河	祁县	祁县东	祁阳	七营
# 棋子湾	泉江	全椒	泉州	全州南
# 确山	曲阜	曲阜东	曲家店	曲江
# 曲靖	曲靖北	渠旧	曲水县	渠县
# 衢州
# R
# 饶平	饶阳	绕阳河	任丘	热水
# 日喀则	日照	融安	荣昌北	荣成
# 容桂	榕江	融水	容县	如东
# 如皋	瑞安	瑞昌	瑞昌西	瑞金
# 汝箕沟	乳山	汝州
# S
# 赛汗塔拉	赛乌苏	萨拉齐	三都县	桑根达来
# 三关口	三河县	三合庄	三花石	三汇镇
# 三家店	三间房	三江口	三江南	三江县
# 三家寨	三家子	三门峡	三门县	三门峡南
# 三门峡西	三明	三明北	三十家	三十里堡
# 三水	三水北	三水南	三穗	三堂集
# 三亚	三阳川	三营	三原	三源浦
# 莎车	沙城	沙海	沙河市	沙岭子西
# 山城镇	山丹	上板城	上板城南	上仓
# 商城	商都	上高镇	上谷	上海
# 上海虹桥	上海南	上海西	商河	尚家
# 商洛	商南	上普雄	商丘	商丘南
# 上饶	上万	上西铺	上腰墩	上虞
# 上园	尚志	山海关	山河屯	山坡东
# 鄯善	鄯善北	山市	汕头	汕尾
# 山阴	邵东	韶关	韶关东	邵家堂
# 韶山南	邵武	绍兴	绍兴北	绍兴东
# 邵阳	邵阳北	沙坪坝	沙坡头	沙桥
# 沙沱	沙湾	沙湾县	沙园	舍伯吐
# 神池	绅坊	升昌	胜芳	沈家
# 申家店	沈家河	深井子	神木	沈丘
# 神树	神头	沈阳	沈阳北	沈阳南
# 深圳	深圳北	深圳东	深圳坪山	深圳西
# 深州	神州	涉县	歙县	歙县北
# 石坝	施秉	石城	十渡	石河子
# 石湖	石家庄	石家庄北	石家庄东	十家子
# 施家嘴	什里店	石林	石磷	石岭
# 石林南	石林西	十里坪	石门县北	石门子
# 石脑	石桥子	石泉县	石人城	狮山
# 狮山北	石头	始兴	十堰	师庄
# 石柱县	师宗	石嘴山	寿阳	双城堡
# 双城北	双丰	双峰北	双河镇	双吉
# 双辽	双柳	双流机场	双流西	双龙山
# 双牌	双阳	双鸭山	双子河	舒城
# 水洞	水富	水家湖	水泉	水源
# 舒兰	疏勒河	树木岭	顺昌	顺德
# 顺德学院	顺义	朔州	沭阳	四道湾
# 四方台	四合永	四会	司家岭	四马架
# 四平	四平东	泗水	泗县	泗阳
# 宋	松坝	宋城路	松河	松江
# 松江河	松江南	松岭	嵩明	松山湖北
# 松树	松树林	松树台	松树镇	松桃
# 松原	松滋	苏北	绥德	绥芬河
# 绥化	绥棱	遂宁	遂平	遂溪
# 绥阳	绥中	绥中北	随州	苏家屯
# 肃宁	苏尼特左旗	孙家	孙吴	孙镇
# 索伦	宿松	苏州	宿州	苏州北
# 宿州东	苏州新区	苏州园区
# T
# 塔尔根	塔尔气	塔哈	塔河	台安
# 泰安	太谷	太谷西	泰和	太和北
# 太湖	泰康	泰来	太姥山	泰宁
# 太平川	太平镇	台前	泰山	太阳山
# 太阳升	太原	太原东	太原南	泰州
# 台州	郯城	塘豹	汤池	塘沽
# 唐河	唐家湾	唐山	唐山北	汤山城
# 汤旺河	汤逊湖	汤阴	汤原	桃村
# 桃村北	陶家屯	陶赖昭	洮南	桃山
# 桃园	塔崖驿	藤县	滕州	滕州东
# 田东北	天河机场	天河街	天津	天津北
# 天津南	天津西	田林	天门	天门南
# 天桥岭	天水	天水南	田心东	田阳
# 天义	天镇	天祝	天柱山	铁厂
# 铁佛寺	铁力	铁岭	铁岭西	亭亮
# 通安驿	桐柏	通北	桐城	通道
# 潼关	通海	通化	通化县	同江
# 统军庄	通辽	铜陵	铜陵北	潼南
# 铜仁	铜仁南	通渭	桐乡	同心
# 通远堡	通远堡西	通州	通州西	桐梓北
# 桐梓东	桐子林	团结	土地堂东	土贵乌拉
# 吐哈	图里河	吐鲁番	吐鲁番北	图们
# 图们北	土门子	土牧尔台	驼腰岭	图强
# 土桥子	土溪
# U
# V
# W
# 瓦房店	瓦房店西	歪头山	万发屯	王安镇
# 王府	王岗	望江	王家营西	万宁
# 完工	湾沟	汪清	王团庄	万乐
# 万年	万源	万州	万州北	瓦屋山
# 瓦窑田	潍坊	威海	威海北	苇河
# 卫辉	威岭	渭南	渭南北	渭南镇
# 威宁	威箐	威舍	卫星	渭源
# 魏杖子	韦庄	文昌	温春	文登
# 文登东	文地	温根托海	温岭	温泉寺
# 文水	闻喜	闻喜西	温州	温州南
# 倭肯	卧里屯	沃皮	武安	吴堡
# 五叉沟	武昌	五常	五大连池	武当山
# 五道沟	五道河	五府山	武功	吴官田
# 乌海	乌海北	乌海西	武汉	芜湖
# 午汲	五家	吴家川	吴家屯	五棵树
# 乌兰	乌兰察布	乌兰哈达	乌兰浩特	乌兰胡同
# 乌拉特前旗	五莲	五林	武隆	五龙背
# 五龙背东	乌龙泉南	乌鲁木齐	乌鲁木齐南	乌奴耳
# 吴桥	武清	武山	武胜	五台山
# 五通	武威	武威南	无锡	武乡
# 无锡东	无锡新区	武穴	武义	武义北
# 乌伊岭	五营	武夷山	武夷山北	武夷山东
# 五原	婺源	五寨	武陟	梧州
# 梧州南
# X
# 下板城	下仓	下城子	夏官营	下花园
# 峡江	下马塘	厦门	厦门北	西安
# 西安北	先锋	项城	香坊	襄汾
# 襄汾西	湘府路	襄河	香兰	湘潭
# 湘潭北	向塘	湘乡	向阳	襄阳
# 向阳川	襄阳东	襄垣	祥云	香樟路
# 仙林	西安南	咸宁	咸宁北	咸宁东
# 咸宁南	仙桃西	咸阳	咸阳秦都	仙游
# 小白	小池口	小村	小得江	小东
# 孝感	孝感北	孝感东	小河镇	小金口
# 小榄	小岭	孝南	小南海	小哨
# 小市	小寺沟	孝西	萧县北	小新街
# 小西庄	小扬气	小月旧	小雨谷	小榆树
# 霞浦	下社	下台子	夏邑县	西昌
# 西昌南	西大庙	喜德	谢家镇	息烽
# 西岗子	西固城	西湖东	西街口	西里
# 西林	西岭口	锡林浩特	西柳	西六方
# 西麻山	新安	新安县	新绰源	新都东
# 信丰	新干	兴安北	兴安岭	兴城
# 兴国	兴和西	兴凯	兴莲	兴隆店
# 兴隆县	兴隆镇	兴宁	兴平	兴泉堡
# 杏树	杏树屯	邢台	邢台东	新固镇
# 兴业	兴义	新寒岭	新和	新化
# 新华	新化南	新晃	新晃西	新华屯
# 新会	西宁	辛集	新江	新绛
# 新津	辛集南	新津南	新李	新林
# 新立屯	新立镇	新民	新坪田	新青
# 新邱	新松浦	新县	新贤城	新乡
# 新乡东	新香坊	信阳	信阳东	新阳镇
# 新沂	信宜	新友谊	新余	新余北
# 新杖子	新肇	新郑机场	忻州	熊岳城
# 西平	西平西	犀浦	浠水	锡铁山
# 秀山	修文县	修武西	西乌旗	西峡
# 息县	西乡	西阳岔	汐子	宣城
# 轩岗	宣汉	宣和	宣化	宣威
# 悬钟	许昌	许昌东	学庄	徐家
# 许家台	许家屯	旬阳	旬阳北	溆浦
# 溆浦南	许三湾	徐水	徐闻	徐州
# 徐州东
# Y
# 亚布力	亚布力南	亚沟	亚河	牙克石
# 亚龙湾	延安	晏城	盐城	盐池
# 砚川	雁荡山	燕岗	羊草	秧草地
# 阳岔	阳澄湖	阳春	杨村	杨岗
# 阳高	阳谷	洋河	羊臼河	杨林
# 杨陵	杨陵南	杨柳青	阳明堡	羊木
# 羊坪	阳平关	阳曲	阳泉	阳泉北
# 阳泉曲	羊圈子	杨树岭	阳朔	羊尾哨
# 洋县西	阳新	阳信	阳邑	羊者窝
# 扬州	岩会	延吉	燕郊	燕家庄
# 盐津	延吉西	阎良	炎陵	焉耆
# 燕山	偃师	烟台	烟台南	烟台西
# 烟筒山	烟筒屯	兖州	燕子砭	姚安
# 姚渡	姚家	姚千户屯	窑上	牙屯堡
# 鸭园	崖州	叶柏寿	叶城	野三坡
# 依安	宜宾	宜昌东	宜城	宜春
# 伊春	一间堡	弋江	伊拉哈	宜良北
# 义马	一面坡	一面山	伊敏	伊敏索木
# 宜耐	沂南	银川	尹地	迎宾路
# 应城	迎春	英德	英德西	营街
# 英吉沙	营口	营口东	营盘水	营山
# 颍上	鹰手营子	鹰潭	鹰潭北	应县
# 伊宁	伊宁东	银浪	饮马峡	银瓶
# 银滩	沂水	伊通	伊图里河	义乌
# 义县	宜兴	益阳	弋阳	宜州
# 迤资	永安	永安乡	永城北	永川东
# 永登	永甸	永定	永丰营	永福南
# 永和	永济	永嘉	永济北	永康
# 永康南	永郎	永乐店	永胜	永寿
# 永泰	永修	永州	友好	尤溪
# 攸县南	酉阳	元宝山	园墩	原林
# 元谋	原平	源迁	元氏	源潭
# 鸳鸯镇	禹城	禹城东	虞城县	榆次
# 于都	岳池	月亮田	乐清	月山
# 越西	岳阳	岳阳东	雨格	裕国
# 余杭	余江	于家堡	余粮堡	玉林
# 榆林	玉门	郁南	云彩岭	运城
# 郓城	运城北	云东海	云浮东	云居寺
# 云梦	云山	云霄	玉屏	玉泉
# 玉山	玉山南	榆社	玉舍	玉石
# 榆树	榆树川	榆树屯	玉田县	玉溪
# 余姚	余姚北	榆中
# Z
# 枣林	枣强	枣阳	枣庄	枣庄东
# 枣庄西	枣子林	扎赉诺尔西	扎兰屯	扎罗木得
# 扎鲁特	张百湾	章党	张家川	张家界
# 张家口南	张兰	樟木头	樟木头东	漳平
# 漳浦	张桥	章丘	樟树	樟树东
# 张台子	张维屯	彰武	漳县	张辛
# 张掖	张掖西	漳州	漳州东	湛江
# 湛江西	诏安	招柏	赵城	肇东
# 照福铺	赵光	肇庆	肇庆东	昭山
# 昭通	昭通北	昭通南	柞水	扎音河
# 扎赉诺尔	哲里木	镇安	镇城底	正定
# 正定机场	正镶白旗	郑州	郑州东	郑州西
# 镇江	镇江南	镇赉	镇平	镇西
# 镇远	泽普	治安	枝城	纸坊东
# 芷江	枝江北	织金	中川机场	中和
# 钟家村	仲恺	中宁	中宁南	中山
# 中山北	钟山西	中卫	钟祥	中兴


# inpath = 'test'

def split_train_test(path):
    i = 0
    fout1 = open('_train.txt', 'w')
    fout2 = open('_test.txt', 'w')
    fout3 = open('_test2.txt', 'w')

    r = random.randint(0, 10)
    with open(path) as f:
        for line in f.readlines():
            if i % 10 == r:
                fout2.write(line)
                fout3.write(line)
            else:
                fout1.write(line)
                r = random.randint(0, 10)
            i += 1
    fout1.close()
    fout2.close()
    fout3.close()


def dealwithline(line):
    # 转账    金额
    def _line1(matched):
        re_str = ''
        time = matched.group("stream9")
        word_list = [c for c in time]
        re_str = ''.join(word_list[0:2])
        for i, c in enumerate(word_list[2:]):
            if i == 0:
                re_str += u'\n' + c + u' B-9\n'
            else:
                re_str += c + u' I-９\n'
        # re_str += ''.join(word_list[-1])
        return re_str

    # 您尾号
    def _line2(matched):
        re_str = ''
        time = matched.group("stream10")
        word_list = [c for c in time]

        firstrNum = re.compile("\d")

        idx = firstrNum.search(time).start()

        re_str = ''.join(word_list[:idx])
        for i, c in enumerate(word_list[idx:]):
            if i == 0:
                re_str += u'\n' + c + u' B-' + u'10' + u'\n'
            else:
                re_str += c + u' I-' + u'10' + u'\n'
        # re_str += ''.join(word_list[-1])
        return re_str

    # 支出
    def _line3(matched):
        re_str = ''
        time = matched.group("stream11")
        word_list = [c for c in time]
        re_str = ''.join(word_list[0:2])
        for i, c in enumerate(word_list[2:]):
            if i == 0:
                re_str += '\n' + c + ' B-' + '11' + '\n'
            else:
                re_str += c + ' I-' + '11' + '\n'
        # re_str += ''.join(word_list[-1])
        return re_str

    def _line4(matched):
        re_str = ''
        time = matched.group("stream11")
        if u'验证码' in time or u"校验码" in time:
            return time

        word_list = [c for c in time]

        firstrNum = re.compile("\d")

        idx = firstrNum.search(time).start()

        re_str = ''.join(word_list[0:idx])
        for i, c in enumerate(word_list[idx:]):
            if i == 0:
                re_str += '\n' + c + ' B-' + '11' + '\n'
            else:
                re_str += c + ' I-' + '11' + '\n'
        # re_str += ''.join(word_list[-1])
        return re_str

    # 余额
    def _line5(matched):
        re_str = ''
        time = matched.group("stream12")
        word_list = [c for c in time]
        firstrNum = re.compile("\d")

        idx = firstrNum.search(time).start()
        re_str = ''.join(word_list[0:idx])
        for i, c in enumerate(word_list[idx:]):
            if i == 0:
                re_str += '\n' + c + ' B-' + '12' + '\n'
            else:
                re_str += c + ' I-' + '12' + '\n'
        # re_str += ''.join(word_list[-1])
        return re_str

    def _line6(matched):
        re_str = ''
        time = matched.group("stream13")
        word_list = [c for c in time]
        re_str = ''.join(word_list[0:2])
        for i, c in enumerate(word_list[2:]):
            if i == 0:
                re_str += '\n' + c + ' B-' + '13' + '\n'
            else:
                re_str += c + ' I-' + '13' + '\n'
        # re_str += ''.join(word_list[-1])
        return re_str

    def _line7(matched):
        re_str = ''
        time = matched.group("time")
        word_list = [c for c in time]
        re_str = ''.join(word_list[0:2])
        for i, c in enumerate(word_list[2:]):
            if i == 0:
                re_str += '\n' + c + ' B-' + '1' + '\n'
            else:
                re_str += c + ' I-' + '1' + '\n'
        # re_str += ''.join(word_list[-1])
        return re_str

    def _line8(matched):
        re_str = ''
        time = matched.group("stream1")
        word_list = [c for c in time]
        re_str = ''.join(word_list[:7])
        for i, c in enumerate(word_list[7:]):
            if i == 0:
                re_str += '\n' + c + ' B-' + '2' + '\n'
            else:
                re_str += c + ' I-' + '2' + '\n'
        # re_str += ''.join(word_list[-1])
        return re_str

    def _line9(matched):
        re_str = ''
        time = matched.group("stream2")
        word_list = [c for c in time]
        re_str = ''.join(word_list[0:6])
        for i, c in enumerate(word_list[6:]):
            if i == 0:
                re_str += '\n' + c + ' B-' + '3' + '\n'
            else:
                re_str += c + ' I-' + '3' + '\n'
        # re_str += ''.join(word_list[-1])
        return re_str

    def _line10(matched):
        re_str = ''
        time = matched.group("stream3")
        word_list = [c for c in time]
        re_str = ''.join(word_list[0:6])
        for i, c in enumerate(word_list[6:]):
            if i == 0:
                re_str += '\n' + c + ' B-' + '4' + '\n'
            else:
                re_str += c + ' I-' + '4' + '\n'
        # re_str += ''.join(word_list[-1])
        return re_str

    def _line11(matched):
        re_str = ''
        time = matched.group("stream4")
        word_list = [c for c in time]
        re_str = ''.join(word_list[0:6])
        for i, c in enumerate(word_list[6:]):
            if i == 0:
                re_str += '\n' + c + ' B-' + '5' + '\n'
            else:
                re_str += c + ' I-' + '5' + '\n'
        # re_str += ''.join(word_list[-1])
        return re_str

    def _line12(matched):
        re_str = ''
        time = matched.group("stream5")
        word_list = [c for c in time]
        re_str = ''.join(word_list[0:9])
        for i, c in enumerate(word_list[9:]):
            if i == 0:
                re_str += '\n' + c + ' B-' + '5' + '\n'
            else:
                re_str += c + ' I-' + '5' + '\n'
        # re_str += ''.join(word_list[-1])
        return re_str

    def _line13(matched):
        re_str = ''
        time = matched.group("stream6")
        word_list = [c for c in time]
        re_str = ''.join(word_list[0:7])
        for i, c in enumerate(word_list[7:]):
            if i == 0:
                re_str += '\n' + c + ' B-' + '7' + '\n'
            else:
                re_str += c + ' I-' + '7' + '\n'
        # re_str += ''.join(word_list[-1])
        return re_str

    def _line20(matched):
        re_str = ''
        time = matched.group("stream14")
        word_list = [c for c in time]

        firstrNum = re.compile("\d")

        idx = firstrNum.search(time).start()

        re_str = ''.join(word_list[0:idx])
        for i, c in enumerate(word_list[idx:]):
            if i == 0:
                re_str += '\n' + c + ' B-' + '14' + '\n'
            else:
                re_str += c + ' I-' + '14' + '\n'
        # re_str += ''.join(word_list[-1])
        return re_str

    def _line21(matched):
        re_str = ''
        time = matched.group("stream15")
        word_list = [c for c in time]

        firstrNum = re.compile("\d")

        idx = firstrNum.search(time).start()

        re_str = ''.join(word_list[0:idx])
        for i, c in enumerate(word_list[idx:]):
            if i == 0:
                re_str += '\n' + c + ' B-' + '15' + '\n'
            else:
                re_str += c + ' I-' + '15' + '\n'
        # re_str += ''.join(word_list[-1])
        return re_str

    def _line23(matched):
        re_str = ''
        time = matched.group("stream17")
        word_list = [c for c in time]

        re_str = ''
        for i, c in enumerate(word_list):
            if i == 0:
                re_str += '\n' + c + ' B-' + '17' + '\n'
            else:
                re_str += c + ' I-' + '17' + '\n'
        # re_str += ''.join(word_list[-1])
        return re_str

    def _line24(matched):
        re_str = ''
        time = matched.group("stream18")
        word_list = [c for c in time]

        firstrNum = re.compile("\d")
        idx = firstrNum.search(time).start()

        re_str = ''.join(word_list[:idx])
        for i, c in enumerate(word_list[idx:]):
            if i == 0:
                re_str += '\n' + c + ' B-' + '18' + '\n'
            else:
                re_str += c + ' I-' + '18' + '\n'
        # re_str += ''.join(word_list[-1])
        return re_str

    def _line25(matched):
        re_str = ''
        time = matched.group("stream19")
        word_list = [c for c in time]

        # firstrNum = re.compile("\d")
        # idx = firstrNum.search(time).start()

        re_str = ''.join(word_list[:2])
        for i, c in enumerate(word_list[2:]):
            if i == 0:
                re_str += '\n' + c + ' B-' + '19' + '\n'
            else:
                re_str += c + ' I-' + '19' + '\n'
        # re_str += ''.join(word_list[-1])
        return re_str

    def _line26(matched):
        re_str = ''
        time = matched.group("stream20")
        word_list = [c for c in time]

        # firstrNum = re.compile("\d")
        # idx = firstrNum.search(time).start()

        re_str = ''.join(word_list[:3])
        for i, c in enumerate(word_list[3:]):
            if i == 0:
                re_str += '\n' + c + ' B-' + '20' + '\n'
            else:
                re_str += c + ' I-' + '20' + '\n'
        # re_str += ''.join(word_list[-1])
        return re_str

    def _line27(matched):
        re_str = ''
        time = matched.group("stream21")
        word_list = [c for c in time]

        # firstrNum = re.compile("\d")
        # idx = firstrNum.search(time).start()

        re_str = ''.join(word_list[:2])
        for i, c in enumerate(word_list[2:]):
            if i == 0:
                re_str += '\n' + c + ' B-' + '21' + '\n'
            else:
                re_str += c + ' I-' + '21' + '\n'
        # re_str += ''.join(word_list[-1])
        return re_str

    def _line28(matched):
        re_str = ''
        time = matched.group("stream22")
        word_list = [c for c in time]

        # firstrNum = re.compile("\d")
        # idx = firstrNum.search(time).start()

        re_str = ''.join(word_list[:3])
        for i, c in enumerate(word_list[3:]):
            if i == 0:
                re_str += '\n' + c + ' B-' + '22' + '\n'
            else:
                re_str += c + ' I-' + '22' + '\n'
        # re_str += ''.join(word_list[-1])
        return re_str

    def _line29(matched):
        re_str = ''
        time = matched.group("stream23")
        if len(time) < 8:
            return time
        word_list = [c for c in time]

        # firstrNum = re.compile("\d")
        # idx = firstrNum.search(time).start()

        re_str = ''.join(word_list)
        for i, c in enumerate(word_list):
            if i == 0:
                re_str += '\n' + c + ' B-' + '23' + '\n'
            else:
                re_str += c + ' I-' + '23' + '\n'
        # re_str += ''.join(word_list[-1])
        return re_str

    # 提取验证码和动态密码
    start = -1
    end = -1

    line = line.decode("utf-8")
    idx_list = [i.start() for i in re.finditer(u'验证码', line)]
    idx_list += [i.start() for i in re.finditer(u'动态密码', line)]
    idx_list += [i.start() for i in re.finditer(u'校验码', line)]
    for idx in idx_list:
        # 先看后方5个单位内有没有验证码
        end = idx + 3 + 5 + 1
        if end > len(line):
            end = len(line)
        temp = line[idx:end]
        firstrNum = re.compile("\d")
        n_idx = -1

        try:
            n_idx = firstrNum.search(temp).start()
        except:
            pass
        # 有
        if n_idx >= 0:
            start = n_idx + idx
            while n_idx + idx < len(line):
                try:
                    n = int(line[n_idx + idx])
                except:
                    end = n_idx + idx
                    break;
                n_idx += 1
            if start != -1 and end != -1:
                deal = line[start:end]
                if len(deal) < 4:
                    break
                re_str = ""
                for l, x in enumerate(deal):
                    if l == 0:
                        re_str += '\n' + x + ' B-' + '8' + '\n'
                    else:
                        re_str += x + ' I-' + '8' + '\n'
                line = line[:start] + re_str + line[end:]
                # 验证码不可能有两个
                break;
        # 前方与后方只需要一个有即可 现在是前方
        else:
            # 看前方8个单位有没有（，如果有看前面2个单位是不是数字
            start = idx
            end = idx
            while start >= 0 and start >= idx - 8:
                if line[start] == u'(' or line[start] == u'（':
                    end = start
                    break;
                start -= 1
            start -= 3
            if end == idx:
                continue
            if start < 0:
                start = 0
            temp = line[start:end]
            firstrNum = re.compile("\d")
            n_idx = -1
            try:
                n_idx = firstrNum.search(temp).start()
            except:
                pass
            # 有
            if n_idx >= 0:
                # 确定end
                end = - 1
                start = n_idx + start
                while n_idx + start < len(line):
                    try:
                        n = int(line[n_idx + start])
                    except:
                        end = n_idx + start
                        break;
                    n_idx += 1
                start = -1
                # 确定start
                start = end - 1
                while start >= 0:
                    try:
                        n = int(line[start])
                    except:
                        start = start + 1
                        break;
                    start -= 1
                if start != end - 1 and end != -1:
                    deal = line[start:end]
                    if len(deal) < 4:
                        break
                    re_str = ""
                    for l, x in enumerate(deal):
                        if l == 0:
                            re_str += '\n' + x + ' B-' + '8' + '\n'
                        else:
                            re_str += x + ' I-' + '8' + '\n'
                    line = line[:start] + re_str + line[end:]
                    # 验证码不可能有两个
                    break;

    # if u"转账" in line and u"金额" in line:
    line = re.sub(ur"(?P<stream9>转账[\d\.]+)", _line1, line.strip())
    line = re.sub(ur"(?P<stream9>金额[\d\.]+)", _line1, line.strip())
    line = re.sub(ur"(?P<stream9>转出[\d\.]+)", _line1, line.strip())

    # idx_list = [i.start() for i in re.finditer(u'尾号', line)]
    # 尾号
    # if len(idx_list) == 2:
    # 银行类
    line = re.sub(ur"(?P<stream10>尾号.{0,1}\d{4,4})", _line2, line.strip())

    line = re.sub(ur"(?P<stream11>取款[\d\.]+)", _line3, line.strip())

    line = re.sub(ur"(?P<stream11>付款.{0,3}\d+)", _line4, line.strip())

    line = re.sub(ur"(?P<stream12>余额-?为?(人民币)?[\d\.]{2,})", _line5, line.strip())

    line = re.sub(ur"(?P<stream13>存入(人民币)?[\d\.]+)", _line6, line.strip())
    line = re.sub(ur"(?P<stream13>存款[\d\.]+)", _line6, line.strip())
    line = re.sub(ur"(?P<stream13>工资[\d\.]+)", _line6, line.strip())
    line = re.sub(ur"(?P<stream13>转入[\d\.]+)", _line6, line.strip())
    # 流量类
    line = re.sub(ur"(?P<time>截至.*?分)", _line7, line.strip())
    line = re.sub(ur"(?P<stream1>国内通用流量共([\d\.]+[MG]{0,1}B{0,1}){1,3})", _line8, line.strip())
    line = re.sub(ur"(?P<stream2>省内流量剩余([\d\.]+[MG]{0,1}B{0,1}){1,3})", _line9, line.strip())
    line = re.sub(ur"(?P<stream3>套餐外流量为([\d\.]+[MG]{0,1}B{0,1}){1,3})", _line10, line.strip())
    line = re.sub(ur"(?P<stream4>国内流量剩余([\d\.]+[MG]{0,1}B{0,1}){1,3})", _line11, line.strip())
    line = re.sub(ur"(?P<stream5>已使用.+?数据流量([\d\.]+[MG]{0,1}B{0,1}){1,3)", _line12, line.strip())
    line = re.sub(ur"(?P<stream6>套餐内流量剩余([\d\.]+[MG]{0,1}B{0,1}){1,3})", _line13, line.strip())
    line = re.sub(ur"(?P<stream6>剩余流量([\d\.]+[MG]{0,1}B{0,1}){1,3})", _line13, line.strip())

    # 差旅类
    line = re.sub(ur"(?P<stream14>[(订单)(取票)]号?\d+)", _line20, line.strip())

    # 始发地与目的地
    start = -1
    end = -1

    idx_list = [i.start() for i in re.finditer(u'飞', line)]
    idx_list += [i.start() for i in re.finditer(u'-', line)]
    idx_list += [i.start() for i in re.finditer(u'到', line)]
    for idx in idx_list:
        # 先看后方5个单位内有没有验证码
        end = idx + 3 + 10 + 1
        if end > len(line):
            end = len(line)
        start = idx - 10
        temp = line[start:end]
        temp_result = []
        for x in place:
            if x in temp:
                temp_result.append(x)

        # 有
        if len(temp_result) >= 2 and temp_result[0] != temp_result[1]:
            temp_result = temp_result[:2]
            tag = 15

            firstWordStart1 = line.find(temp_result[0])
            firstWordStart2 = line.find(temp_result[1])

            if firstWordStart1 < firstWordStart2:
                tag = 15
            else:
                tag = 16

            for x in temp_result:
                firstWordStart = line.find(x)
                firstWordEnd = firstWordStart + len(x)

                deal = line[firstWordStart:firstWordEnd]
                re_str = ""
                for l, x in enumerate(deal):
                    if l == 0:
                        re_str += '\n' + x + ' B-' + str(tag) + '\n'
                    else:
                        re_str += x + ' I-' + str(tag) + '\n'
                line = line[:firstWordStart] + re_str + line[firstWordEnd:]
                if tag == 15:
                    tag += 1
                else:
                    tag -= 1
            # 始发地终点不可能有两个
            break;

    # line = re.sub(ur"(?P<stream15>.+?-.+?)", _line21, line.strip())
    # line = re.sub(ur"(?P<stream16>目的地)", _line22, line.strip())
    if u"火车" in line or u"飞机" in line or u"航班" in line:
        line = re.sub(ur"(?P<stream17>\d{2,2}\:\d{2,2})", _line23, line.strip())

    # 水电煤
    line = re.sub(ur"(?P<stream18>欠费-?[\d\.]+)", _line24, line.strip())
    line = re.sub(ur"(?P<stream19>电费[\d\.]+)", _line25, line.strip())
    line = re.sub(ur"(?P<stream20>用电量[\d\.]+)", _line26, line.strip())
    line = re.sub(ur"(?P<stream21>水费[\d\.]+)", _line27, line.strip())
    line = re.sub(ur"(?P<stream22>用水量[\d\.]+)", _line28, line.strip())
    if u'电话' not in line and u'户' in line:
        line = re.sub(ur"(?P<stream23>[\d\.]+)", _line29, line.strip())

    # 生活快递

    # line = re.sub(ur"(?P<stream10>您\d{4,4}账户)", _line3, line.strip())
    # line = re.sub(ur"(?P<stream10>您尾号.{0,1}\d{4,4})", _line2, line.strip())
    # line = re.sub(ur"(?P<stream11>尾号为\d+)", _line1, line.strip())

    # replacedStr = re.sub(r"(?P<stream6>套餐内流量剩余([\d\.]+[MG]{0,1}B{0,1}){1,3})", _line7, line.strip())

    replacedStr = line.encode("utf-8")
    return replacedStr


def gen(inpath, name, flag):
    # flag true的话保留大标签
    fout = open('output1.txt', 'w')
    with open(inpath) as f:
        for line in f.readlines():
            re_line = dealwithline(line)
            fout.write(re_line)
            fout.write('\n')
    fout.close()

    fout = open(name, 'w')
    with open('output1.txt') as f:
        for line in f.readlines():
            my_list = line.strip().split()

            if len(my_list) == 2 and (my_list[1].startswith('B') or my_list[1].startswith('I')):
                if not flag:
                    fout.write(line[:-2] + '\n')
                else:
                    fout.write(line.strip() + '\n')

            else:
                for w in line.strip().decode('utf-8'):
                    if w == "#":
                        fout.write('\n')
                    else:
                        fout.write(w.encode('utf-8') + ' O\n')

    os.remove('output1.txt')
    fout.close()


if __name__ == '__main__':
    split_train_test(inpath)
    gen('_train.txt', 'output/total_train.txt', True)
    gen('_test.txt', 'output/total_test.txt', True)
    # gen('_test2.txt', 'test2.txt', True)

    os.remove('_train.txt')
    os.remove('_test.txt')
    os.remove('_test2.txt')

    # origin_list = []

    # for i, x in enumerate(origin_list):
    #     f = open("bank_train.txt")
    #     new_train = open('output/new_bank_train.txt','w')
    #     statistic = {}
    #
    #     while 1:
    #         lines = f.readlines(100000)
    #         if not lines:
    #             break
    #         for line in lines:
    #             line = line.decode('utf-8')
    #
    #             if statistic.has_key(len(line)):
    #                 statistic[len(line)] += 1
    #             else:
    #                 statistic[len(line)] = 1
    #
    #             temp = line.strip().split()
    #             if len(temp) == 2 and temp[0] == '#':
    #                 new_train.write('\n')
    #             else:
    #                 new_train.write(line.encode('utf-8'))
    #     f.close()
    #     new_train.close()
    #     for x in statistic.items():
    #         print str(x[0]) + ':' + str(x[1])
