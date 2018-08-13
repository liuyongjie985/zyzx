# coding:utf-8
import os
import re
import random

# inpath = 'data/TotalData.txt'
# inpath = 'output/filtered_sms_sample.txt'
inpath = 'output/sampleData.txt'
# inpath = 'test2'

place = [u'北京', u'天津', u'上海', u'重庆', u'新疆', u'乌鲁木齐', u'西藏', u'宁夏', u'内蒙古', u'广西', u'黑龙江', u'哈尔滨',
         u'大庆', u'齐齐哈尔',
         u'佳木斯', u'鸡西',
         u'鹤岗', u'双鸭山', u'牡丹江', u'伊春', u'七台河', u'黑河', u'绥化', u'五常', u'双城', u'尚志',
         u'纳河', u'虎林', u'密山', u'铁力',
         u'同江', u'富锦', u'绥芬河',
         u'海林', u'宁安', u'穆林', u'北安', u'五大连池', u'肇东', u'海伦', u'安达', u'吉林', u'长春',
         u'四平', u'辽源', u'通化', u'白山',
         u'松原', u'白城', u'九台',
         u'榆树', u'德惠', u'舒兰', u'桦甸', u'蛟河', u'磐石', u'公主岭', u'双辽',
         u'梅河口', u'集安', u'临江',
         u'大安', u'洮南', u'延吉',
         u'图们', u'敦化', u'龙井', u'珲春', u'和龙', u'辽宁', u'沈阳', u'大连', u'鞍山',
         u'抚顺', u'本溪', u'丹东', u'锦州',
         u'营口', u'阜新', u'辽阳', u'盘锦',
         u'铁岭', u'朝阳', u'葫芦岛', u'中寨', u'周家', u'周家屯', u'周口', u'庄河北', u'庄桥',
         u'诸城', u'珠海', u'珠海北', u'诸暨',
         u'朱家沟', u'褚家湾', u'朱家窑', u'驻马店', u'驻马店西', u'准格尔', u'涿州',
         u'涿州东', u'卓资东', u'朱日和',
         u'朱石寨', u'珠斯花', u'竹园坝', u'株洲', u'株洲南', u'株洲西',
         u'淄博', u'子长', u'自贡', u'紫荆关',
         u'资溪', u'资阳', u'紫阳', u'资阳北', u'资中', u'资中北',
         u'子洲', u'邹城', u'遵义', u'遵义南', u'遵义西', u'左家', u'左岭', u'昆明', u'泉州',

         u'芷江', u'枝江北', u'织金', u'中川机场', u'中和',
         u'钟家村', u'仲恺', u'中宁', u'中宁南', u'中山',
         u'中山北', u'钟山西', u'中卫', u'钟祥', u'中兴', u'新民', u'瓦房店', u'普兰', u'庄河', u'海城', u'东港'
    , u'凤城', u'凌海', u'北镇', u'大石桥', u'盖州', u'灯塔', u'调兵山', u'开原', u'凌源', u'北票', u'兴城', u'河北', u'石家庄',
         u'唐山', u'邯郸', u'秦皇岛', u'保定', u'张家口', u'承德', u'廊坊', u'沧州', u'衡水', u'邢台', u'辛集', u'藁城市',
         u'晋州市', u'新乐市', u'鹿泉市', u'遵化市', u'迁安市', u'武安市', u'南宫市', u'沙河市', u'涿州市', u'定州市',
         u'安国市', u'高碑店市', u'泊头市', u'任丘市', u'黄骅市', u'河间市', u'霸州市', u'三河市', u'冀州市', u'深州市', u'山东',
         u'济南', u'青岛', u'淄博', u'枣庄', u'东营', u'烟台', u'潍坊', u'济宁', u'泰安', u'威海', u'日照', u'莱芜', u'临沂', u'德州',
         u'聊城', u'菏泽', u'滨州', u'章丘', u'胶南', u'胶州', u'平度', u'莱西', u'即墨', u'滕州', u'龙口', u'莱阳', u'莱州', u'招远', u'蓬莱'
    , u'栖霞', u'海阳', u'青州', u'诸城', u'安丘', u'高密', u'昌邑', u'兖州', u'曲阜',
         u'邹城', u'乳山', u'文登', u'荣成', u'乐陵', u'临清', u'禹城', u'江苏', u'南京', u'镇江', u'常州', u'无锡', u'苏州',
         u'徐州', u'连云港', u'淮安', u'盐城', u'扬州', u'泰州', u'南通', u'宿迁', u'江阴', u'宜兴', u'邳州', u'新沂', u'金坛', u'溧阳', u'常熟',
         u'张家港', u'太仓',
         u'昆山', u'吴江', u'如皋', u'通州', u'海门', u'启东', u'东台', u'大丰', u'高邮', u'江都', u'仪征', u'丹阳', u'扬中', u'句容',
         u'泰兴', u'姜堰', u'靖江', u'兴化', u'安徽', u'合肥', u'蚌埠', u'芜湖', u'淮南', u'亳州', u'阜阳', u'淮北', u'宿州', u'滁州', u'安庆',
         u'巢湖', u'马鞍山', u'宣城', u'黄山', u'池州', u'铜陵', u'界首', u'天长', u'明光', u'桐城', u'宁国', u'浙江', u'杭州', u'嘉兴',
         u'湖州', u'宁波', u'金华', u'温州', u'丽水', u'绍兴', u'衢州', u'舟山', u'台州', u'建德', u'富阳', u'临安', u'余姚', u'慈溪', u'奉化',
         u'瑞安', u'乐清', u'海宁', u'平湖', u'桐乡', u'诸暨', u'上虞', u'嵊州', u'兰溪', u'义乌', u'东阳', u'永康', u'江山', u'临海',
         u'温岭', u'龙泉', u'福建', u'福州', u'厦门', u'三明', u'南平', u'漳州', u'莆田', u'宁德', u'龙岩', u'福清', u'长乐', u'永安', u'石狮', u'晋江',
         u'南安', u'龙海', u'邵武', u'武夷山', u'建瓯', u'建阳', u'漳平', u'福安', u'福鼎', u'广东', u'广州', u'深圳', u'汕头', u'惠州', u'珠海',
         u'揭阳',
         u'佛山', u'河源', u'阳江', u'茂名', u'湛江', u'梅州', u'肇庆', u'韶关', u'潮州', u'东莞', u'中山', u'清远', u'江门', u'汕尾', u'云浮',
         u'增城', u'从化', u'乐昌', u'南雄', u'台山', u'开平', u'鹤山', u'恩平', u'廉江', u'雷州', u'吴川', u'高州', u'化州市', u'高要市',
         u'四会', u'兴宁', u'陆丰', u'阳春', u'英德', u'连州', u'普宁', u'罗定', u'海南', u'海口', u'三亚',
         u'琼海', u'文昌', u'万宁', u'五指山', u'儋州', u'东方', u'云南', u'曲靖', u'玉溪', u'保山', u'昭通', u'丽江', u'普洱', u'临沧,'
                                                                                                     u'安宁', u'宣威',
         u'个旧', u'开远', u'景洪', u'楚雄', u'大理', u'潞西', u'瑞丽', u'贵州', u'贵阳', u'六盘水', u'遵义', u'安顺',
         u'清镇', u'赤水', u'仁怀', u'铜仁', u'毕节', u'兴义', u'凯里', u'都匀', u'福泉', u'四川', u'成都', u'绵阳', u'德阳', u'广元',
         u'自贡', u'攀枝花', u'乐山', u'南充', u'内江', u'遂宁', u'广安', u'泸州', u'达州', u'眉山', u'宜宾', u'雅安', u'资阳',
         u'都江堰', u'彭州', u'邛崃', u'崇州', u'广汉', u'什邡', u'绵竹', u'江油', u'峨眉山', u'阆中', u'华蓥', u'万源', u'简阳', u'西昌',
         u'湖南', u'长沙', u'株洲', u'湘潭', u'衡阳', u'岳阳', u'郴州', u'永州', u'邵阳', u'怀化', u'常德', u'益阳', u'张家界', u'娄底',
         u'浏阳', u'醴陵', u'湘乡', u'韶山', u'耒阳', u'常宁', u'武冈', u'临湘', u'汨罗', u'津市', u'沅江', u'资兴', u'洪江市', u'冷水江市', u'涟源市',
         u'吉首市']


# ',u'16，【湖北】：12地级市——武汉',u'襄樊',u'宜昌',u'黄石',u'鄂州',u'随州',u'荆州',u'荆门',u'十堰',u'孝感',u'黄冈',u'咸宁
# ',u'24县级市——大冶市',u'丹江口市',u'洪湖市',u'石首市',u'松滋市',u'宜都市',u'当阳市',u'枝江市',u'老河口市',u'枣阳市',u'宜城市',u'钟祥市',u'应城市',u'安陆市',u'汉川市',u'麻城市',u'武穴市',u'赤壁市',u'广水市',u'仙桃市',u'天门市',u'潜江市',u'恩施市',u'利川市
# ',u'17，【河南】：17地级市——郑州',u'洛阳',u'开封',u'漯河',u'安阳',u'新乡',u'周口',u'三门峡',u'焦作',u'平顶山',u'信阳',u'南阳',u'鹤壁',u'濮阳',u'许昌',u'商丘',u'驻马店
# ',u'21县级市——巩义市',u'新郑市',u'新密市',u'登封市',u'荥阳市',u'偃师市',u'汝州市',u'舞钢市',u'林州市',u'卫辉市',u'辉县市',u'沁阳市',u'孟州市',u'禹州市',u'长葛市',u'义马市',u'灵宝市',u'邓州市',u'永城市',u'项城市',u'济源市
# ',u'18，【山西】：11地级市——太原',u'大同',u'忻州',u'阳泉',u'长治',u'晋城',u'朔州',u'晋中',u'运城',u'临汾',u'吕梁
# ',u'11县级市——古交',u'潞城',u'高平',u'介休',u'永济',u'河津',u'原平',u'侯马',u'霍州',u'孝义',u'汾阳
# ',u'19，【陕西】：10地级市——西安',u'咸阳',u'铜川',u'延安',u'宝鸡',u'渭南',u'汉中',u'安康',u'商洛',u'榆林
# ',u'3县级市——兴平市',u'韩城市',u'华阴市
# ',u'20，【甘肃】：12地级市——兰州',u'天水',u'平凉',u'酒泉',u'嘉峪关',u'金昌',u'白银',u'武威',u'张掖',u'庆阳',u'定西',u'陇南
# ',u'4县级市——玉门市',u'敦煌市',u'临夏市',u'合作市
# ',u'21，【青海】：1地级市——西宁
# ',u'2县级市——格尔木',u'德令哈
# ',u'22，【江西】：11地级市——南昌',u'九江',u'赣州',u'吉安',u'鹰潭',u'上饶',u'萍乡',u'景德镇',u'新余',u'宜春',u'抚州
# ',u'10县级市——乐平市',u'瑞昌市',u'贵溪市',u'瑞金市',u'南康市',u'井冈山市',u'丰城市',u'樟树市',u'高安市',u'德兴市
# ',u'23，【台湾】：7市——台北',u'台中',u'基隆',u'高雄',u'台南',u'新竹',u'嘉义
# ',u'16县级市——板桥市',u'宜兰市',u'竹北市',u'桃园市',u'苗栗市',u'丰原市',u'彰化市',u'南投市',u'太保市',u'斗六市',u'新营市',u'凤山市',u'屏东市',u'台东市',u'花莲市',u'马公市
# ',u'四',u'【特别行政区】
# ',u'1，【香港】
# ',u'2，【澳门】
# ',u'#
# ',u'#
# ',u'#
# ',u'#
# ',u'阿巴嘎旗',u'阿城',u'阿木尔',u'阿尔山',u'阿尔山北
# ',u'艾河',u'艾家村',u'阿金',u'阿克苏',u'阿克陶
# ',u'阿拉山口',u'阿勒泰',u'阿里河',u'阿南庄',u'安达
# ',u'安德',u'安多',u'昂昂溪',u'安广',u'安化
# ',u'安家',u'安靖',u'安康',u'安口窑',u'安陆
# ',u'安平',u'安庆',u'安庆西',u'安仁',u'鞍山
# ',u'鞍山西',u'安顺',u'安顺西',u'安塘',u'安亭北
# ',u'安图',u'安图西',u'安阳',u'安阳东',u'敖汉
# ',u'鳌江',u'敖力布告',u'敖头',u'阿图什',u'阿乌尼
# ',u'B
# ',u'巴楚',u'巴东',u'八方山',u'八虎力',u'白壁关
# ',u'白城',u'白沟',u'柏果',u'白河',u'白河东
# ',u'白河县',u'白涧',u'白芨沟',u'白鸡坡',u'白奎堡
# ',u'白狼',u'百里峡',u'白马井',u'白旗',u'白泉
# ',u'百色',u'白山市',u'白沙坡',u'白沙铺',u'白水江
# ',u'白水镇',u'白洋淀',u'百宜',u'白音察干',u'白音华南
# ',u'白音胡硕',u'白银市',u'白银西',u'白云鄂博',u'白桦排
# ',u'巴林',u'八面城',u'八面通',u'板城',u'半截河
# ',u'班猫箐',u'板塘',u'宝坻',u'保定',u'保定东
# ',u'宝华山',u'宝鸡',u'宝鸡南',u'保康',u'宝林
# ',u'宝龙山',u'宝清',u'宝泉岭',u'包头',u'包头东
# ',u'包头西',u'八仙筒',u'巴彦高勒',u'鲅鱼圈',u'巴中
# ',u'霸州',u'霸州西',u'北安',u'北碚',u'北戴河
# ',u'北海',u'北滘',u'北京',u'北京东',u'北京南
# ',u'北京西',u'北井子',u'北流',u'北马圈子',u'北票南
# ',u'北屯',u'北屯市',u'背荫河',u'北宅',u'栟茶
# ',u'蚌埠',u'蚌埠南',u'本溪',u'本溪新城',u'贲红
# ',u'碧江',u'笔架山',u'滨海',u'滨海北',u'彬县
# ',u'宾阳',u'滨州',u'璧山',u'博鳌',u'博白
# ',u'博克图',u'博乐',u'勃利',u'泊头',u'博兴
# ',u'亳州',u'布海
# ',u'C
# ',u'蔡家沟',u'蔡家坡',u'苍南',u'苍石',u'苍溪
# ',u'沧州',u'沧州西',u'草海',u'草河口',u'曹家营子
# ',u'草市',u'曹县',u'曹子里',u'岑溪',u'查布嘎
# ',u'察尔汗',u'查干湖',u'柴沟堡',u'柴河',u'岔江
# ',u'茶陵南',u'长城',u'长冲',u'长春',u'长春西
# ',u'常德',u'长甸',u'长发屯',u'长葛',u'长虹
# ',u'昌乐',u'昌黎',u'长临河',u'长农',u'常平
# ',u'昌平北',u'常平东',u'常平南',u'长坡岭',u'长庆桥
# ',u'长沙',u'常山',u'长沙南',u'长山屯',u'长沙西
# ',u'长寿北',u'长寿湖',u'长汀南',u'长汀镇',u'昌图
# ',u'昌图西',u'长武',u'长兴',u'长兴南',u'长垣
# ',u'长征',u'长治',u'长治北',u'常州',u'常州北
# ',u'常庄',u'巢湖',u'巢湖东',u'潮汕',u'朝天
# ',u'朝天南',u'潮阳',u'朝阳川',u'朝阳村',u'朝阳地
# ',u'朝阳南',u'朝阳镇',u'朝中',u'潮州',u'察素齐
# ',u'册亨',u'承德',u'承德东',u'成都',u'成都东
# ',u'成都南',u'成高子',u'城固',u'城固北',u'成吉思汗
# ',u'陈官营',u'城子坦',u'晨明',u'辰清',u'辰溪
# ',u'陈相屯',u'郴州',u'郴州西',u'车转湾',u'赤壁
# ',u'赤壁北',u'赤峰',u'赤峰西',u'池州',u'重庆
# ',u'重庆北',u'重庆南',u'重庆西',u'崇信',u'崇左
# ',u'春阳',u'楚山',u'楚雄南',u'滁州',u'滁州北
# ',u'嵯岗',u'慈利',u'磁山',u'磁县',u'磁窑
# ',u'从江',u'翠岗',u'崔黄口
# ',u'D
# ',u'大安',u'大安北',u'大坝',u'大板',u'大堡
# ',u'打柴沟',u'大磴沟',u'大东',u'大方南',u'大丰
# ',u'大关',u'大官屯',u'大孤山',u'大红旗',u'大灰厂
# ',u'大虎山',u'带岭',u'代县',u'岱岳',u'达家沟
# ',u'大涧',u'大口屯',u'大朗镇',u'达拉特西',u'大理
# ',u'大荔',u'大连',u'大连北',u'大荔北',u'大林
# ',u'大民屯',u'丹东',u'丹东西',u'丹凤',u'砀山
# ',u'砀山南',u'当涂东',u'当雄',u'当阳',u'丹徒
# ',u'丹霞山',u'丹阳',u'丹阳北',u'到保',u'道滘
# ',u'道清',u'道州',u'大盘石',u'大平房',u'大埔
# ',u'大庆',u'大庆东',u'大青沟',u'大庆西',u'大石桥
# ',u'大石头',u'大石寨',u'大田边',u'大同',u'大通西
# ',u'大屯',u'大旺',u'大湾子',u'大武口',u'大西
# ',u'大兴',u'大兴沟',u'大辛庄',u'大雁',u'大杨树
# ',u'大冶北',u'大营',u'大英东',u'大营镇',u'大余
# ',u'大战场',u'大杖子',u'达州',u'大竹园',u'大苴
# ',u'大足南',u'德安',u'德保',u'德伯斯',u'德昌
# ',u'得耳布尔',u'德惠',u'德惠西',u'德令哈',u'登沙河
# ',u'灯塔',u'邓州',u'德清',u'德清西',u'德兴
# ',u'德兴东',u'德阳',u'德州',u'德州东',u'垫江
# ',u'甸心',u'滴道',u'定边',u'鼎湖东',u'鼎湖山
# ',u'定南',u'定陶',u'定西',u'定襄',u'定西北
# ',u'定远',u'定州',u'定州东',u'低窝铺',u'低庄
# ',u'东安东',u'东边井',u'东城南',u'东戴河',u'东二道河
# ',u'东方',u'东方红',u'东丰',u'东富',u'东港北
# ',u'东沟门',u'东莞',u'东莞东',u'东光',u'东海
# ',u'东海县',u'洞井',u'东京城',u'东来',u'洞庙河
# ',u'东明县',u'东升',u'东胜西',u'东台',u'东通化
# ',u'东湾',u'东乡',u'东兴',u'东辛庄',u'东营
# ',u'东营南',u'东淤地',u'东镇',u'东至',u'东庄
# ',u'斗沟子',u'豆罗',u'豆庄',u'端州',u'都昌
# ',u'都格',u'对青山',u'兑镇',u'都江堰',u'杜拉尔
# ',u'敦化',u'敦煌',u'独山',u'渡市',u'都匀
# ',u'都匀东
# ',u'E
# ',u'峨边',u'鄂尔多斯',u'额济纳',u'峨眉',u'峨眉山
# ',u'恩施',u'阿房宫',u'二道沟门',u'二道沙河',u'二井
# ',u'二连',u'二龙',u'二龙山屯',u'二龙屯',u'二营
# ',u'鄂州',u'鄂州东
# ',u'F
# ',u'发耳',u'繁昌西',u'防城港北',u'范家屯',u'范镇
# ',u'繁峙',u'费县',u'丰城',u'凤城东',u'丰城南
# ',u'丰都',u'丰广',u'奉化',u'凤凰城',u'凤凰机场
# ',u'丰乐镇',u'枫林',u'风陵渡',u'丰水村',u'丰顺
# ',u'冯屯',u'凤县',u'丰镇',u'凤州',u'汾河
# ',u'汾阳',u'分宜',u'佛岭',u'佛坪',u'佛山
# ',u'佛山西',u'福安',u'富川',u'福鼎',u'富海
# ',u'福海',u'富锦',u'福巨',u'富拉尔基',u'涪陵
# ',u'涪陵北',u'福利屯',u'阜南',u'抚宁',u'阜宁
# ',u'富宁',u'福清',u'福泉',u'芙蓉南',u'福山口
# ',u'福山镇',u'复盛',u'抚顺北',u'扶绥',u'福田
# ',u'浮图峪',u'富县东',u'阜新南',u'阜阳',u'扶余
# ',u'富裕',u'富源',u'抚远',u'富源北',u'扶余北
# ',u'福州',u'抚州',u'抚州东',u'福州南
# ',u'G
# ',u'盖州',u'盖州西',u'甘草店',u'甘谷',u'甘河
# ',u'甘洛',u'甘旗卡',u'甘泉北',u'赶水东',u'干塘
# ',u'赣州',u'高安',u'高碑店',u'高碑店东',u'藁城
# ',u'藁城南',u'高村',u'高峰',u'高各庄',u'皋兰
# ',u'高林屯',u'高密',u'高平',u'高山子',u'高台
# ',u'高台南',u'高台子',u'高滩',u'高头',u'高邑
# ',u'高邑西',u'高州',u'葛店南',u'格尔木',u'葛根庙
# ',u'革居',u'根河',u'恭城',u'共青城',u'巩义
# ',u'巩义南',u'公营子',u'公主岭',u'公主岭南',u'沟帮子
# ',u'广安',u'广安南',u'官高',u'广德',u'广汉北
# ',u'光明',u'光明城',u'广南卫',u'广南县',u'广宁
# ',u'广宁寺',u'光山',u'广水',u'广通北',u'广元
# ',u'光泽',u'广州',u'广州北',u'广州东',u'广州南
# ',u'关林',u'关岭',u'观沙岭',u'官厅',u'官厅西
# ',u'冠豸山',u'瓜州',u'谷城',u'古城镇',u'古城子
# ',u'古东',u'贵定',u'贵定北',u'贵定南',u'贵定县
# ',u'贵港',u'桂林',u'桂林北',u'桂林西',u'归流河
# ',u'桂平',u'贵溪',u'贵阳',u'贵阳北',u'贵阳东
# ',u'古交',u'古浪',u'古莲',u'郭家店',u'果松
# ',u'涡阳',u'虢镇',u'谷山',u'孤山口',u'固始
# ',u'古田',u'古田北',u'古田会址',u'固原',u'菇园
# ',u'古镇',u'固镇
# ',u'H
# ',u'哈达铺',u'哈尔滨',u'哈尔滨北',u'哈尔滨东',u'哈尔滨西
# ',u'海安县',u'海北',u'海城',u'海城西',u'海东西
# ',u'海口',u'海口东',u'海拉尔',u'海林',u'海伦
# ',u'海宁',u'海宁西',u'海石湾',u'海阳',u'海阳北
# ',u'海晏',u'哈拉海',u'哈力图',u'哈密',u'韩城
# ',u'汉川',u'寒葱沟',u'邯郸',u'邯郸东',u'韩府湾
# ',u'杭州',u'杭州东',u'涵江',u'汉口',u'寒岭
# ',u'韩麻营',u'汉寿',u'汉阴',u'汉源',u'汉中
# ',u'浩良河',u'哈日努拉',u'鹤北',u'鹤壁',u'河边
# ',u'鹤壁东',u'合川',u'河唇',u'合肥',u'合肥北城
# ',u'合肥南',u'鹤岗',u'黑冲滩',u'黑河',u'黑井
# ',u'黑水',u'黑台',u'黑旺',u'贺家店',u'河津
# ',u'河口北',u'河口南',u'鹤立',u'和龙',u'河洛营
# ',u'横道河子',u'横峰',u'横沟桥东',u'衡山',u'衡山西
# ',u'衡水',u'衡水北',u'衡阳',u'衡阳东',u'和平
# ',u'合浦',u'鹤庆',u'贺胜桥东',u'和什托洛盖',u'和硕
# ',u'荷塘',u'和田',u'合阳北',u'河源',u'菏泽
# ',u'贺州',u'红安西',u'洪洞',u'红光镇',u'红果
# ',u'洪河',u'红江',u'宏庆',u'红旗营',u'红山
# ',u'红砂岘',u'红寺堡',u'洪洞西',u'红岘台',u'红星
# ',u'红兴隆',u'红彦',u'后湖',u'侯马',u'侯马西
# ',u'鲘门',u'猴山',u'后寨',u'华城',u'化德
# ',u'花湖',u'淮安',u'淮北',u'淮北北',u'淮滨
# ',u'怀化',u'怀化南',u'怀集',u'淮南',u'淮南东
# ',u'怀仁',u'怀柔',u'怀柔北',u'槐荫',u'华家
# ',u'花家庄',u'桦林',u'桦南',u'黄柏',u'潢川
# ',u'黄村',u'黄冈',u'黄冈东',u'黄冈西',u'黄瓜园
# ',u'黄河景区',u'黄口',u'黄陵',u'黄陵南',u'黄流
# ',u'黄梅',u'黄泥河',u'黄山',u'黄山北',u'黄石
# ',u'黄石北',u'黄松甸',u'黄土店',u'黄羊滩',u'黄羊湾
# ',u'黄羊镇',u'湟源',u'黄州',u'华蓥',u'怀仁东
# ',u'换新天',u'花棚子',u'花桥',u'华容东',u'华容南
# ',u'华山',u'华山北',u'花山南',u'花土坡',u'花园
# ',u'花园口',u'化州',u'虎尔虎拉',u'呼和浩特',u'呼和浩特东
# ',u'惠安',u'会昌北',u'珲春',u'惠东',u'惠环
# ',u'汇流河',u'惠农',u'惠山',u'会同',u'徽县
# ',u'惠州',u'惠州南',u'湖口',u'呼兰',u'虎林
# ',u'葫芦岛',u'葫芦岛北',u'呼鲁斯太',u'虎门',u'霍城
# ',u'霍尔果斯',u'获嘉',u'火炬沟',u'霍林郭勒',u'霍邱
# ',u'霍州',u'霍州东',u'虎山',u'鄠邑',u'湖州
# ',u'互助
# ',u'I
# ',u'J
# ',u'加格达奇',u'佳木斯',u'吉安',u'集安',u'加南
# ',u'尖峰',u'江都',u'江华',u'姜家',u'将乐
# ',u'江门东',u'江密峰',u'江宁',u'江宁西',u'江桥
# ',u'江山',u'江所田',u'姜堰',u'江永',u'江油
# ',u'江油北',u'江源',u'剑门关',u'建宁县北',u'建瓯
# ',u'建瓯西',u'建三江',u'尖山',u'建始',u'建水
# ',u'建阳',u'简阳',u'简阳南',u'交城',u'蛟河
# ',u'蛟河西',u'角美',u'胶州',u'焦作',u'嘉善
# ',u'甲山',u'嘉善南',u'嘉祥',u'嘉兴',u'嘉兴南
# ',u'嘉峪关',u'嘉峪关南',u'鸡东',u'界首市',u'介休
# ',u'介休东',u'揭阳',u'纪家沟',u'吉林',u'芨岭
# ',u'即墨北',u'济南',u'济南东',u'济南西',u'金宝屯
# ',u'金昌',u'晋城',u'金城江',u'靖边',u'泾川
# ',u'旌德',u'景德镇',u'景德镇北',u'井店',u'井冈山
# ',u'静海',u'精河南',u'荆门',u'井南',u'金沟屯
# ',u'经棚',u'京山',u'景泰',u'镜铁山',u'靖西
# ',u'泾县',u'井陉',u'靖远',u'靖远西',u'晋中
# ',u'靖州',u'荆州',u'景州',u'锦和',u'锦河
# ',u'金华',u'金华南',u'济宁',u'集宁南',u'晋江
# ',u'锦界',u'金山北',u'金山屯',u'劲松',u'进贤
# ',u'进贤南',u'金银潭',u'金月湾',u'缙云',u'缙云西
# ',u'金寨',u'锦州',u'金州',u'晋州',u'锦州南
# ',u'稷山',u'吉首',u'吉舒',u'九江',u'九郎山
# ',u'九龙',u'酒泉',u'酒泉南',u'九三',u'九台
# ',u'九台南',u'九营',u'吉文',u'鸡西',u'绩溪北
# ',u'吉新河',u'绩溪县',u'济源',u'蓟州',u'鄄城
# ',u'莒南',u'峻德',u'军粮城北',u'句容西',u'莒县
# ',u'巨野
# ',u'K
# ',u'开安',u'凯北',u'开封',u'开封北',u'开福寺
# ',u'开化',u'开江',u'凯里',u'凯里南',u'开鲁
# ',u'开通',u'开阳',u'开原',u'开原西',u'喀喇其
# ',u'卡伦',u'康金井',u'康庄',u'喀什',u'克东
# ',u'克拉玛依',u'岢岚',u'克山',u'克一河',u'口前
# ',u'库车',u'库都尔',u'库尔勒',u'奎山',u'葵潭
# ',u'奎屯',u'库伦',u'昆独仑召',u'昆明',u'昆明南
# ',u'昆山',u'昆山南',u'昆阳
# ',u'L
# ',u'拉白',u'拉古',u'拉哈',u'来宾',u'来宾北
# ',u'濑湍',u'莱芜东',u'莱西',u'莱西北',u'莱阳
# ',u'涞源',u'拉林',u'喇嘛甸',u'蓝村',u'兰岗
# ',u'廊坊',u'廊坊北',u'狼尾山',u'朗乡',u'阆中
# ',u'兰家屯',u'兰考',u'兰考南',u'兰岭',u'兰陵北
# ',u'兰溪',u'兰州',u'兰州东',u'兰州西',u'兰州新区
# ',u'老边',u'老城镇',u'老莱',u'老营',u'拉萨
# ',u'拉鲊',u'乐昌',u'乐昌东',u'乐东',u'乐都
# ',u'乐都南',u'耒阳',u'耒阳西',u'雷州',u'乐平市
# ',u'乐山',u'乐善村',u'两当',u'梁底下',u'良各庄
# ',u'两家',u'超梁沟',u'梁平',u'梁平南',u'梁山
# ',u'廉江',u'连江',u'莲江口',u'连山关',u'涟源
# ',u'连云港东',u'连珠山',u'寮步',u'聊城',u'辽阳
# ',u'辽源',u'辽中',u'黎城',u'利川',u'离堆公园
# ',u'李家',u'丽江',u'李家坪',u'利津南',u'沥林北
# ',u'醴陵',u'醴陵东',u'里木店',u'临城',u'林东
# ',u'临汾',u'临汾西',u'临高南',u'灵宝',u'灵宝西
# ',u'灵璧',u'陵城',u'凌海',u'零陵',u'灵丘
# ',u'灵山',u'灵石',u'灵石东',u'陵水',u'冷水江东
# ',u'灵武',u'凌源',u'凌源东',u'临海',u'临河
# ',u'蔺家楼',u'临江',u'林口',u'临澧',u'临清
# ',u'林盛堡',u'林西',u'临西',u'临湘',u'临沂
# ',u'临邑',u'临沂北',u'临颍',u'林源',u'临泽
# ',u'临泽南',u'林子头',u'礼泉',u'李石寨',u'丽水
# ',u'溧水',u'梨树镇',u'黎塘',u'六安',u'六道河子
# ',u'六个鸡',u'柳沟',u'柳河',u'六合镇',u'刘家店
# ',u'刘家河',u'柳江',u'柳家庄',u'柳林南',u'柳毛
# ',u'六盘山',u'六盘水',u'流水沟',u'柳园',u'柳园南
# ',u'六枝',u'柳州',u'李旺',u'澧县',u'溧阳
# ',u'立志',u'隆安东',u'隆昌',u'隆昌北',u'龙池
# ',u'龙川',u'龙洞堡',u'龙丰',u'龙沟',u'龙骨甸
# ',u'龙华',u'隆化',u'龙嘉',u'龙江',u'龙井
# ',u'龙口市',u'龙里北',u'龙南',u'陇南',u'龙泉寺
# ',u'龙山镇',u'龙市',u'龙塘坝',u'陇西',u'陇县
# ',u'龙岩',u'龙游',u'龙镇',u'娄底',u'娄底南
# ',u'娄山关南',u'滦河',u'滦河沿',u'滦平',u'滦县
# ',u'潞城',u'陆川',u'鹿道',u'略阳',u'鲁番
# ',u'陆丰',u'禄丰南',u'芦沟',u'麓谷',u'庐江
# ',u'芦家庄',u'路口铺',u'陆良',u'卢龙',u'轮台
# ',u'罗城',u'漯河',u'漯河西',u'珞璜南',u'罗江东
# ',u'洛门',u'罗平',u'罗山',u'洛湾三江',u'洛阳
# ',u'洛阳东',u'洛阳龙门',u'罗源',u'洛碛',u'庐山
# ',u'鲁山',u'露水河',u'芦台',u'鹿寨',u'鹿寨北
# ',u'绿博园',u'绿化',u'吕梁
# ',u'M
# ',u'马鞍山',u'马鞍山东',u'麻城',u'麻城北',u'马兰
# ',u'马莲河',u'马林',u'麻柳',u'马龙',u'玛纳斯
# ',u'忙罕屯',u'满归',u'满洲里',u'毛坝',u'毛坝关
# ',u'茅草坪',u'毛陈',u'帽儿山',u'茂林',u'茂名
# ',u'茂名西',u'茂舍祖',u'马三家',u'麻尾',u'麻阳
# ',u'梅河口',u'梅江',u'美兰',u'眉山',u'眉山东
# ',u'美溪',u'梅州',u'门达',u'猛洞河',u'孟家岗
# ',u'孟津',u'蒙自',u'蒙自北',u'门源',u'渑池
# ',u'渑池南',u'免渡河',u'冕宁',u'勉县',u'绵阳
# ',u'庙城',u'庙岭',u'庙庄',u'弥渡',u'弥勒
# ',u'汨罗',u'汨罗东',u'明港东',u'明城',u'明光
# ',u'明水河',u'明珠',u'民和南',u'闵集',u'民乐
# ',u'闽清北',u'民权',u'民权北',u'岷县',u'密山
# ',u'密山西',u'米沙子',u'米易',u'密云北',u'米脂
# ',u'磨刀石',u'莫尔道嘎',u'漠河',u'无为',u'牡丹江
# ',u'穆棱',u'沐滂',u'牟平',u'墨玉',u'暮云
# ',u'N
# ',u'乃林',u'奈曼',u'内江',u'南陵',u'南博山
# ',u'南部',u'南岔',u'南昌',u'南昌西',u'南城
# ',u'南城司',u'南充',u'南充北',u'南仇',u'南大庙
# ',u'南丹',u'南芬',u'南芬北',u'南丰',u'南观村
# ',u'南河川',u'南湖东',u'南江',u'南江口',u'南京
# ',u'南靖',u'南京南',u'南口',u'南口前',u'南朗
# ',u'南宁',u'南宁东',u'南宁西',u'南平北',u'南平南
# ',u'南通',u'南头',u'南洼',u'南湾子',u'南翔北
# ',u'南雄',u'南阳',u'南阳寨',u'南峪',u'南杂木
# ',u'南召',u'那曲',u'内乡',u'纳雍',u'讷河
# ',u'内江北',u'内江南',u'能家',u'嫩江',u'娘子关
# ',u'碾子山',u'聂河',u'捏掌',u'尼勒克',u'宁安
# ',u'宁波',u'宁德',u'宁东',u'宁东南',u'宁国
# ',u'宁海',u'宁陵县',u'宁明',u'宁强南',u'宁武
# ',u'宁乡',u'牛家',u'牛庄',u'农安',u'暖泉
# ',u'O
# ',u'P
# ',u'徘徊北',u'磐安镇',u'盘古',u'盘关',u'潘家店
# ',u'盘锦',u'盘锦北',u'磐石',u'攀枝花',u'盘州
# ',u'泡子',u'裴德',u'蓬安',u'蓬莱市',u'彭山北
# ',u'彭水',u'彭阳',u'彭泽',u'彭州',u'偏岭
# ',u'庙山',u'皮口',u'平安',u'平安驿',u'平坝南
# ',u'屏边',u'平昌',u'平顶山',u'平顶山西',u'平度
# ',u'平房',u'平关',u'平果',u'平河口',u'平湖
# ',u'平凉',u'平凉南',u'平罗',u'平南南',u'平泉
# ',u'平山',u'坪上',u'平社',u'坪石',u'平台
# ',u'平田',u'平旺',u'萍乡',u'凭祥',u'萍乡北
# ',u'平型关',u'平洋',u'平遥',u'平遥古城',u'平邑
# ',u'平峪',u'平原',u'平原堡',u'平原东',u'平庄
# ',u'平庄南',u'皮山',u'郫县',u'郫县西',u'邳州
# ',u'坡底下',u'鄱阳',u'普安',u'普安县',u'蒲城
# ',u'蒲城东',u'普定',u'普兰店',u'普宁',u'莆田
# ',u'普湾',u'普雄',u'濮阳',u'普者黑
# ',u'Q
# ',u'迁安',u'乾安',u'前锋',u'千河',u'黔江
# ',u'潜江',u'前进镇',u'前磨头',u'前山',u'前苇塘
# ',u'乾县',u'千阳',u'桥北',u'桥头',u'桥湾
# ',u'桥西',u'七甸',u'祁东',u'奇峰塔',u'齐哈日格图
# ',u'祁家堡',u'綦江东',u'七龙星',u'祁门',u'秦安
# ',u'蕲春',u'庆安',u'青白江东',u'青城山',u'青川
# ',u'青岛',u'青岛北',u'青堆',u'清河城',u'清河门
# ',u'清涧县',u'青莲',u'青龙',u'青山',u'青神
# ',u'庆盛',u'清水',u'清水北',u'清水县',u'青田
# ',u'青铜峡',u'青县',u'清徐',u'清原',u'清远
# ',u'青州市',u'秦皇岛',u'秦家',u'秦家庄',u'秦岭
# ',u'沁县',u'沁阳',u'钦州东',u'琼海',u'棋盘
# ',u'齐齐哈尔',u'齐齐哈尔南',u'岐山',u'戚墅堰',u'七苏木
# ',u'七台河',u'祁县',u'祁县东',u'祁阳',u'七营
# ',u'棋子湾',u'泉江',u'全椒',u'泉州',u'全州南
# ',u'确山',u'曲阜',u'曲阜东',u'曲家店',u'曲江
# ',u'曲靖',u'曲靖北',u'渠旧',u'曲水县',u'渠县
# ',u'衢州
# ',u'R
# ',u'饶平',u'饶阳',u'绕阳河',u'任丘',u'热水
# ',u'日喀则',u'日照',u'融安',u'荣昌北',u'荣成
# ',u'容桂',u'榕江',u'融水',u'容县',u'如东
# ',u'如皋',u'瑞安',u'瑞昌',u'瑞昌西',u'瑞金
# ',u'汝箕沟',u'乳山',u'汝州
# ',u'S
# ',u'赛汗塔拉',u'赛乌苏',u'萨拉齐',u'三都县',u'桑根达来
# ',u'三关口',u'三河县',u'三合庄',u'三花石',u'三汇镇
# ',u'三家店',u'三间房',u'三江口',u'三江南',u'三江县
# ',u'三家寨',u'三家子',u'三门峡',u'三门县',u'三门峡南
# ',u'三门峡西',u'三明',u'三明北',u'三十家',u'三十里堡
# ',u'三水',u'三水北',u'三水南',u'三穗',u'三堂集
# ',u'三亚',u'三阳川',u'三营',u'三原',u'三源浦
# ',u'莎车',u'沙城',u'沙海',u'沙河市',u'沙岭子西
# ',u'山城镇',u'山丹',u'上板城',u'上板城南',u'上仓
# ',u'商城',u'商都',u'上高镇',u'上谷',u'上海
# ',u'上海虹桥',u'上海南',u'上海西',u'商河',u'尚家
# ',u'商洛',u'商南',u'上普雄',u'商丘',u'商丘南
# ',u'上饶',u'上万',u'上西铺',u'上腰墩',u'上虞
# ',u'上园',u'尚志',u'山海关',u'山河屯',u'山坡东
# ',u'鄯善',u'鄯善北',u'山市',u'汕头',u'汕尾
# ',u'山阴',u'邵东',u'韶关',u'韶关东',u'邵家堂
# ',u'韶山南',u'邵武',u'绍兴',u'绍兴北',u'绍兴东
# ',u'邵阳',u'邵阳北',u'沙坪坝',u'沙坡头',u'沙桥
# ',u'沙沱',u'沙湾',u'沙湾县',u'沙园',u'舍伯吐
# ',u'神池',u'绅坊',u'升昌',u'胜芳',u'沈家
# ',u'申家店',u'沈家河',u'深井子',u'神木',u'沈丘
# ',u'神树',u'神头',u'沈阳',u'沈阳北',u'沈阳南
# ',u'深圳',u'深圳北',u'深圳东',u'深圳坪山',u'深圳西
# ',u'深州',u'神州',u'涉县',u'歙县',u'歙县北
# ',u'石坝',u'施秉',u'石城',u'十渡',u'石河子
# ',u'石湖',u'石家庄',u'石家庄北',u'石家庄东',u'十家子
# ',u'施家嘴',u'什里店',u'石林',u'石磷',u'石岭
# ',u'石林南',u'石林西',u'十里坪',u'石门县北',u'石门子
# ',u'石脑',u'石桥子',u'石泉县',u'石人城',u'狮山
# ',u'狮山北',u'石头',u'始兴',u'十堰',u'师庄
# ',u'石柱县',u'师宗',u'石嘴山',u'寿阳',u'双城堡
# ',u'双城北',u'双丰',u'双峰北',u'双河镇',u'双吉
# ',u'双辽',u'双柳',u'双流机场',u'双流西',u'双龙山
# ',u'双牌',u'双阳',u'双鸭山',u'双子河',u'舒城
# ',u'水洞',u'水富',u'水家湖',u'水泉',u'水源
# ',u'舒兰',u'疏勒河',u'树木岭',u'顺昌',u'顺德
# ',u'顺德学院',u'顺义',u'朔州',u'沭阳',u'四道湾
# ',u'四方台',u'四合永',u'四会',u'司家岭',u'四马架
# ',u'四平',u'四平东',u'泗水',u'泗县',u'泗阳
# ',u'宋',u'松坝',u'宋城路',u'松河',u'松江
# ',u'松江河',u'松江南',u'松岭',u'嵩明',u'松山湖北
# ',u'松树',u'松树林',u'松树台',u'松树镇',u'松桃
# ',u'松原',u'松滋',u'苏北',u'绥德',u'绥芬河
# ',u'绥化',u'绥棱',u'遂宁',u'遂平',u'遂溪
# ',u'绥阳',u'绥中',u'绥中北',u'随州',u'苏家屯
# ',u'肃宁',u'苏尼特左旗',u'孙家',u'孙吴',u'孙镇
# ',u'索伦',u'宿松',u'苏州',u'宿州',u'苏州北
# ',u'宿州东',u'苏州新区',u'苏州园区
# ',u'T
# ',u'塔尔根',u'塔尔气',u'塔哈',u'塔河',u'台安
# ',u'泰安',u'太谷',u'太谷西',u'泰和',u'太和北
# ',u'太湖',u'泰康',u'泰来',u'太姥山',u'泰宁
# ',u'太平川',u'太平镇',u'台前',u'泰山',u'太阳山
# ',u'太阳升',u'太原',u'太原东',u'太原南',u'泰州
# ',u'台州',u'郯城',u'塘豹',u'汤池',u'塘沽
# ',u'唐河',u'唐家湾',u'唐山',u'唐山北',u'汤山城
# ',u'汤旺河',u'汤逊湖',u'汤阴',u'汤原',u'桃村
# ',u'桃村北',u'陶家屯',u'陶赖昭',u'洮南',u'桃山
# ',u'桃园',u'塔崖驿',u'藤县',u'滕州',u'滕州东
# ',u'田东北',u'天河机场',u'天河街',u'天津',u'天津北
# ',u'天津南',u'天津西',u'田林',u'天门',u'天门南
# ',u'天桥岭',u'天水',u'天水南',u'田心东',u'田阳
# ',u'天义',u'天镇',u'天祝',u'天柱山',u'铁厂
# ',u'铁佛寺',u'铁力',u'铁岭',u'铁岭西',u'亭亮
# ',u'通安驿',u'桐柏',u'通北',u'桐城',u'通道
# ',u'潼关',u'通海',u'通化',u'通化县',u'同江
# ',u'统军庄',u'通辽',u'铜陵',u'铜陵北',u'潼南
# ',u'铜仁',u'铜仁南',u'通渭',u'桐乡',u'同心
# ',u'通远堡',u'通远堡西',u'通州',u'通州西',u'桐梓北
# ',u'桐梓东',u'桐子林',u'团结',u'土地堂东',u'土贵乌拉
# ',u'吐哈',u'图里河',u'吐鲁番',u'吐鲁番北',u'图们
# ',u'图们北',u'土门子',u'土牧尔台',u'驼腰岭',u'图强
# ',u'土桥子',u'土溪
# ',u'U
# ',u'V
# ',u'W
# ',u'瓦房店',u'瓦房店西',u'歪头山',u'万发屯',u'王安镇
# ',u'王府',u'王岗',u'望江',u'王家营西',u'万宁
# ',u'完工',u'湾沟',u'汪清',u'王团庄',u'万乐
# ',u'万年',u'万源',u'万州',u'万州北',u'瓦屋山
# ',u'瓦窑田',u'潍坊',u'威海',u'威海北',u'苇河
# ',u'卫辉',u'威岭',u'渭南',u'渭南北',u'渭南镇
# ',u'威宁',u'威箐',u'威舍',u'卫星',u'渭源
# ',u'魏杖子',u'韦庄',u'文昌',u'温春',u'文登
# ',u'文登东',u'文地',u'温根托海',u'温岭',u'温泉寺
# ',u'文水',u'闻喜',u'闻喜西',u'温州',u'温州南
# ',u'倭肯',u'卧里屯',u'沃皮',u'武安',u'吴堡
# ',u'五叉沟',u'武昌',u'五常',u'五大连池',u'武当山
# ',u'五道沟',u'五道河',u'五府山',u'武功',u'吴官田
# ',u'乌海',u'乌海北',u'乌海西',u'武汉',u'芜湖
# ',u'午汲',u'五家',u'吴家川',u'吴家屯',u'五棵树
# ',u'乌兰',u'乌兰察布',u'乌兰哈达',u'乌兰浩特',u'乌兰胡同
# ',u'乌拉特前旗',u'五莲',u'五林',u'武隆',u'五龙背
# ',u'五龙背东',u'乌龙泉南',u'乌鲁木齐',u'乌鲁木齐南',u'乌奴耳
# ',u'吴桥',u'武清',u'武山',u'武胜',u'五台山
# ',u'五通',u'武威',u'武威南',u'无锡',u'武乡
# ',u'无锡东',u'无锡新区',u'武穴',u'武义',u'武义北
# ',u'乌伊岭',u'五营',u'武夷山',u'武夷山北',u'武夷山东
# ',u'五原',u'婺源',u'五寨',u'武陟',u'梧州
# ',u'梧州南
# ',u'X
# ',u'下板城',u'下仓',u'下城子',u'夏官营',u'下花园
# ',u'峡江',u'下马塘',u'厦门',u'厦门北',u'西安
# ',u'西安北',u'先锋',u'项城',u'香坊',u'襄汾
# ',u'襄汾西',u'湘府路',u'襄河',u'香兰',u'湘潭
# ',u'湘潭北',u'向塘',u'湘乡',u'向阳',u'襄阳
# ',u'向阳川',u'襄阳东',u'襄垣',u'祥云',u'香樟路
# ',u'仙林',u'西安南',u'咸宁',u'咸宁北',u'咸宁东
# ',u'咸宁南',u'仙桃西',u'咸阳',u'咸阳秦都',u'仙游
# ',u'小白',u'小池口',u'小村',u'小得江',u'小东
# ',u'孝感',u'孝感北',u'孝感东',u'小河镇',u'小金口
# ',u'小榄',u'小岭',u'孝南',u'小南海',u'小哨
# ',u'小市',u'小寺沟',u'孝西',u'萧县北',u'小新街
# ',u'小西庄',u'小扬气',u'小月旧',u'小雨谷',u'小榆树
# ',u'霞浦',u'下社',u'下台子',u'夏邑县',u'西昌
# ',u'西昌南',u'西大庙',u'喜德',u'谢家镇',u'息烽
# ',u'西岗子',u'西固城',u'西湖东',u'西街口',u'西里
# ',u'西林',u'西岭口',u'锡林浩特',u'西柳',u'西六方
# ',u'西麻山',u'新安',u'新安县',u'新绰源',u'新都东
# ',u'信丰',u'新干',u'兴安北',u'兴安岭',u'兴城
# ',u'兴国',u'兴和西',u'兴凯',u'兴莲',u'兴隆店
# ',u'兴隆县',u'兴隆镇',u'兴宁',u'兴平',u'兴泉堡
# ',u'杏树',u'杏树屯',u'邢台',u'邢台东',u'新固镇
# ',u'兴业',u'兴义',u'新寒岭',u'新和',u'新化
# ',u'新华',u'新化南',u'新晃',u'新晃西',u'新华屯
# ',u'新会',u'西宁',u'辛集',u'新江',u'新绛
# ',u'新津',u'辛集南',u'新津南',u'新李',u'新林
# ',u'新立屯',u'新立镇',u'新民',u'新坪田',u'新青
# ',u'新邱',u'新松浦',u'新县',u'新贤城',u'新乡
# ',u'新乡东',u'新香坊',u'信阳',u'信阳东',u'新阳镇
# ',u'新沂',u'信宜',u'新友谊',u'新余',u'新余北
# ',u'新杖子',u'新肇',u'新郑机场',u'忻州',u'熊岳城
# ',u'西平',u'西平西',u'犀浦',u'浠水',u'锡铁山
# ',u'秀山',u'修文县',u'修武西',u'西乌旗',u'西峡
# ',u'息县',u'西乡',u'西阳岔',u'汐子',u'宣城
# ',u'轩岗',u'宣汉',u'宣和',u'宣化',u'宣威
# ',u'悬钟',u'许昌',u'许昌东',u'学庄',u'徐家
# ',u'许家台',u'许家屯',u'旬阳',u'旬阳北',u'溆浦
# ',u'溆浦南',u'许三湾',u'徐水',u'徐闻',u'徐州
# ',u'徐州东
# ',u'Y
# ',u'亚布力',u'亚布力南',u'亚沟',u'亚河',u'牙克石
# ',u'亚龙湾',u'延安',u'晏城',u'盐城',u'盐池
# ',u'砚川',u'雁荡山',u'燕岗',u'羊草',u'秧草地
# ',u'阳岔',u'阳澄湖',u'阳春',u'杨村',u'杨岗
# ',u'阳高',u'阳谷',u'洋河',u'羊臼河',u'杨林
# ',u'杨陵',u'杨陵南',u'杨柳青',u'阳明堡',u'羊木
# ',u'羊坪',u'阳平关',u'阳曲',u'阳泉',u'阳泉北
# ',u'阳泉曲',u'羊圈子',u'杨树岭',u'阳朔',u'羊尾哨
# ',u'洋县西',u'阳新',u'阳信',u'阳邑',u'羊者窝
# ',u'扬州',u'岩会',u'延吉',u'燕郊',u'燕家庄
# ',u'盐津',u'延吉西',u'阎良',u'炎陵',u'焉耆
# ',u'燕山',u'偃师',u'烟台',u'烟台南',u'烟台西
# ',u'烟筒山',u'烟筒屯',u'兖州',u'燕子砭',u'姚安
# ',u'姚渡',u'姚家',u'姚千户屯',u'窑上',u'牙屯堡
# ',u'鸭园',u'崖州',u'叶柏寿',u'叶城',u'野三坡
# ',u'依安',u'宜宾',u'宜昌东',u'宜城',u'宜春
# ',u'伊春',u'一间堡',u'弋江',u'伊拉哈',u'宜良北
# ',u'义马',u'一面坡',u'一面山',u'伊敏',u'伊敏索木
# ',u'宜耐',u'沂南',u'银川',u'尹地',u'迎宾路
# ',u'应城',u'迎春',u'英德',u'英德西',u'营街
# ',u'英吉沙',u'营口',u'营口东',u'营盘水',u'营山
# ',u'颍上',u'鹰手营子',u'鹰潭',u'鹰潭北',u'应县
# ',u'伊宁',u'伊宁东',u'银浪',u'饮马峡',u'银瓶
# ',u'银滩',u'沂水',u'伊通',u'伊图里河',u'义乌
# ',u'义县',u'宜兴',u'益阳',u'弋阳',u'宜州
# ',u'迤资',u'永安',u'永安乡',u'永城北',u'永川东
# ',u'永登',u'永甸',u'永定',u'永丰营',u'永福南
# ',u'永和',u'永济',u'永嘉',u'永济北',u'永康
# ',u'永康南',u'永郎',u'永乐店',u'永胜',u'永寿
# ',u'永泰',u'永修',u'永州',u'友好',u'尤溪
# ',u'攸县南',u'酉阳',u'元宝山',u'园墩',u'原林
# ',u'元谋',u'原平',u'源迁',u'元氏',u'源潭
# ',u'鸳鸯镇',u'禹城',u'禹城东',u'虞城县',u'榆次
# ',u'于都',u'岳池',u'月亮田',u'乐清',u'月山
# ',u'越西',u'岳阳',u'岳阳东',u'雨格',u'裕国
# ',u'余杭',u'余江',u'于家堡',u'余粮堡',u'玉林
# ',u'榆林',u'玉门',u'郁南',u'云彩岭',u'运城
# ',u'郓城',u'运城北',u'云东海',u'云浮东',u'云居寺
# ',u'云梦',u'云山',u'云霄',u'玉屏',u'玉泉
# ',u'玉山',u'玉山南',u'榆社',u'玉舍',u'玉石
# ',u'榆树',u'榆树川',u'榆树屯',u'玉田县',u'玉溪
# ',u'余姚',u'余姚北',u'榆中
# ',u'Z
# ',u'枣林',u'枣强',u'枣阳',u'枣庄',u'枣庄东
# ',u'枣庄西',u'枣子林',u'扎赉诺尔西',u'扎兰屯',u'扎罗木得
# ',u'扎鲁特',u'张百湾',u'章党',u'张家川',u'张家界
# ',u'张家口南',u'张兰',u'樟木头',u'樟木头东',u'漳平
# ',u'漳浦',u'张桥',u'章丘',u'樟树',u'樟树东
# ',u'张台子',u'张维屯',u'彰武',u'漳县',u'张辛
# ',u'张掖',u'张掖西',u'漳州',u'漳州东',u'湛江
# ',u'湛江西',u'诏安',u'招柏',u'赵城',u'肇东
# ',u'照福铺',u'赵光',u'肇庆',u'肇庆东',u'昭山
# ',u'昭通',u'昭通北',u'昭通南',u'柞水',u'扎音河
# ',u'扎赉诺尔',u'哲里木',u'镇安',u'镇城底',u'正定
# ',u'正定机场',u'正镶白旗',u'郑州',u'郑州东',u'郑州西
# ',u'镇江',u'镇江南',u'镇赉',u'镇平',u'镇西
# ',u'镇远',u'泽普',u'治安',u'枝城',u'纸坊东',


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


"""
    author: konglili
            start
"""


class labeling():
    def __init__(self, label):
        self.label = label

    def match_digitnumber(self, matched):
        re_str = ''
        key_value = matched.group("stream" + str(self.label))
        word_list = [c for c in key_value]

        firstrNum = re.compile("[\d\.]{1,}")
        if firstrNum:
            firstidx = firstrNum.search(key_value).start()
            endidx = firstrNum.search(key_value).end()
            re_str = ''.join(word_list[0:firstidx])
        for i, c in enumerate(word_list[firstidx:endidx]):
            if i == 0:
                re_str += '\n' + c + ' B-' + str(self.label) + '\n'
            else:
                re_str += c + ' I-' + str(self.label) + '\n'
        re_str += ''.join(word_list[endidx:])
        return re_str

    def match_ordernumber(self, matched):
        re_str = ''
        key_value = matched.group("stream" + str(self.label))
        word_list = [c for c in key_value]

        firstrNum = re.compile("[a-zA-Z0-9\-]{1,}")

        if firstrNum:
            firstidx = firstrNum.search(key_value).start()
            endidx = firstrNum.search(key_value).end()
            re_str = ''.join(word_list[0:firstidx])
        for i, c in enumerate(word_list[firstidx:endidx]):
            if i == 0:
                re_str += '\n' + c + ' B-' + str(self.label) + '\n'
            else:
                re_str += c + ' I-' + str(self.label) + '\n'
        re_str += ''.join(word_list[endidx:])
        return re_str

    """
    author: chenyuxiang
            start
    """

    def match_workword(self, matched):
        re_str = ''
        key_value = matched.group("stream" + str(self.label))
        word_list = [c for c in key_value]

        firstrNum = re.compile(":")

        if firstrNum:
            firstidx = firstrNum.search(key_value).start()
            endidx = firstrNum.search(key_value).end()
            re_str = ''.join(word_list[0:firstidx])
        for i, c in enumerate(word_list[firstidx:endidx]):
            if i == 0:
                re_str += '\n' + c + ' B-' + str(self.label) + '\n'
            else:
                re_str += c + ' I-' + str(self.label) + '\n'
        re_str += ''.join(word_list[endidx:])
        return re_str

    """
    author: 
            end
    """


"""
    author: konglili
            end
"""


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

        firstrNum = re.compile("\d")

        result = firstrNum.search(time)
        if result == None:
            return time
        idx = result.start()

        re_str = ''.join(word_list[0:idx])
        for i, c in enumerate(word_list[idx:]):
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

        firstrNum = re.compile("\d")
        idx = firstrNum.search(time).start()

        re_str = ''.join(word_list[0:idx])
        for i, c in enumerate(word_list[idx:]):
            if i == 0:
                re_str += '\n' + c + ' B-' + '6' + '\n'
            else:
                re_str += c + ' I-' + '6' + '\n'
        # re_str += ''.join(word_list[-1])
        return re_str

    def _line13(matched):
        re_str = ''
        time = matched.group("stream6")
        word_list = [c for c in time]

        firstrNum = re.compile("\d")
        idx = firstrNum.search(time).start()

        re_str = ''.join(word_list[0:idx])
        for i, c in enumerate(word_list[idx:]):
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
        deal = word_list[idx:]
        if len(deal) < 8:
            return time
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

        re_str = ''
        for i, c in enumerate(word_list):
            if i == 0:
                re_str += '\n' + c + ' B-' + '23' + '\n'
            else:
                re_str += c + ' I-' + '23' + '\n'
        # re_str += ''.join(word_list[-1])
        return re_str

    # 本月总流量
    def _line401(matched):
        re_str = ''
        time = matched.group("stream401")

        word_list = [c for c in time]

        firstrNum = re.compile("\d")
        idx = firstrNum.search(time).start()

        re_str = ''.join(word_list[:idx])
        for i, c in enumerate(word_list[idx:]):

            if i == 0:
                re_str += '\n' + c + ' B-' + '401' + '\n'
            else:
                re_str += c + ' I-' + '401' + '\n'
        # re_str += ''.join(word_list[-1])
        return re_str

    def _line402(matched):
        re_str = ''
        time = matched.group("stream402")

        word_list = [c for c in time]

        firstrNum = re.compile("\d")
        idx = firstrNum.search(time).start()

        re_str = ''.join(word_list[:idx])
        for i, c in enumerate(word_list[idx:]):

            if i == 0:
                re_str += '\n' + c + ' B-' + '402' + '\n'
            else:
                re_str += c + ' I-' + '402' + '\n'
        # re_str += ''.join(word_list[-1])
        return re_str

    def _line403(matched):
        re_str = ''
        time = matched.group("stream403")

        word_list = [c for c in time]

        firstrNum = re.compile("\d")
        try:
            idx = firstrNum.search(time).start()
        except:
            return time

        re_str = ''.join(word_list[:idx])
        for i, c in enumerate(word_list[idx:]):

            if i == 0:
                re_str += '\n' + c + ' B-' + '403' + '\n'
            else:
                re_str += c + ' I-' + '403' + '\n'
        # re_str += ''.join(word_list[-1])
        return re_str

    def _line404(matched):
        re_str = ''
        time = matched.group("stream404")

        word_list = [c for c in time]

        firstrNum = re.compile("\d")
        idx = firstrNum.search(time).start()

        re_str = ''.join(word_list[:idx])
        for i, c in enumerate(word_list[idx:]):

            if i == 0:
                re_str += '\n' + c + ' B-' + '404' + '\n'
            else:
                re_str += c + ' I-' + '404' + '\n'
        # re_str += ''.join(word_list[-1])
        return re_str

    def _line405(matched):
        re_str = ''
        time = matched.group("stream405")

        word_list = [c for c in time]

        re_str = ''
        for i, c in enumerate(word_list):

            if i == 0:
                re_str += '\n' + c + ' B-' + '405' + '\n'
            else:
                re_str += c + ' I-' + '405' + '\n'
        # re_str += ''.join(word_list[-1])
        return re_str

    def _line111(matched):
        re_str = ''
        time = matched.group("stream111")
        word_list = [c for c in time]

        firstrNum = re.compile("\d")
        try:
            idx = firstrNum.search(time).start()
        except:
            return time

        re_str = ''.join(word_list[0:idx])
        for i, c in enumerate(word_list[idx:]):
            if i == 0:
                re_str += '\n' + c + ' B-' + '111' + '\n'
            else:
                re_str += c + ' I-' + '111' + '\n'
        # re_str += ''.join(word_list[-1])
        return re_str

    '''
    author: jsheng
    start 
    '''

    def _line301(matched):
        re_str = ''
        time = matched.group("stream301")
        word_list = [c for c in time]
        re_str = ''.join(word_list[0:2])
        for i, c in enumerate(word_list[2:]):
            if i == 0:
                re_str += u'\n' + c + u' B-301\n'
            else:
                re_str += c + u' I-301\n'
        # re_str += ''.join(word_list[-1])
        return re_str

    def _line302(matched):
        re_str = ''
        time = matched.group("stream302")

        word_list = [c for c in time]

        re_str = ''
        for i, c in enumerate(word_list):

            if i == 0:
                re_str += '\n' + c + ' B-' + '302' + '\n'
            else:
                re_str += c + ' I-' + '302' + '\n'
        # re_str += ''.join(word_list[-1])
        return re_str

    # 您尾号
    def _line303(matched):
        re_str = ''
        time = matched.group("stream303")
        word_list = [c for c in time]

        firstrNum = re.compile("\d")

        idx = firstrNum.search(time).start()

        re_str = ''.join(word_list[:idx])
        for i, c in enumerate(word_list[idx:]):
            if i == 0:
                re_str += u'\n' + c + u' B-' + u'303' + u'\n'
            else:
                re_str += c + u' I-' + u'303' + u'\n'
        # re_str += ''.join(word_list[-1])
        return re_str

    # 取款金额
    def _line304(matched):
        re_str = ''
        time = matched.group("stream11")
        word_list = [c for c in time]
        firstrNum = re.compile("\d")

        idx = firstrNum.search(time).start()

        re_str = ''.join(word_list[0:idx])
        for i, c in enumerate(word_list[idx:]):
            if i == 0:
                re_str += '\n' + c + ' B-' + '304' + '\n'
            else:
                re_str += c + ' I-' + '304' + '\n'
        # re_str += ''.join(word_list[-1])
        return re_str

    # 支付金额
    def _line305(matched):
        re_str = ''
        time = matched.group("stream11")
        word_list = [c for c in time]
        firstrNum = re.compile("\d")

        idx = firstrNum.search(time).start()

        re_str = ''.join(word_list[0:idx])
        for i, c in enumerate(word_list[idx:]):
            if i == 0:
                re_str += '\n' + c + ' B-' + '305' + '\n'
            else:
                re_str += c + ' I-' + '305' + '\n'
        # re_str += ''.join(word_list[-1])
        return re_str

    # 余额
    def _line306(matched):
        re_str = ''
        time = matched.group("stream306")
        word_list = [c for c in time]
        firstrNum = re.compile("\d")

        idx = firstrNum.search(time).start()
        re_str = ''.join(word_list[0:idx])
        for i, c in enumerate(word_list[idx:]):
            if i == 0:
                re_str += '\n' + c + ' B-' + '306' + '\n'
            else:
                re_str += c + ' I-' + '306' + '\n'
        # re_str += ''.join(word_list[-1])
        return re_str

    # 存入/转入
    def _line307(matched):
        re_str = ''
        time = matched.group("stream307")
        word_list = [c for c in time]

        firstrNum = re.compile("\d")

        result = firstrNum.search(time)
        if result == None:
            return time
        idx = result.start()

        re_str = ''.join(word_list[0:idx])
        for i, c in enumerate(word_list[idx:]):
            if i == 0:
                re_str += '\n' + c + ' B-' + '307' + '\n'
            else:
                re_str += c + ' I-' + '307' + '\n'
        # re_str += ''.join(word_list[-1])
        return re_str

    def _line308(matched):
        re_str = ''
        time = matched.group("stream308")
        word_list = [c for c in time]

        firstrNum = re.compile("\d")

        idx = firstrNum.search(time).start()

        re_str = ''.join(word_list[0:idx])
        deal = word_list[idx:]
        if len(deal) < 8:
            return time
        for i, c in enumerate(word_list[idx:]):
            if i == 0:
                re_str += '\n' + c + ' B-' + '308' + '\n'
            else:
                re_str += c + ' I-' + '308' + '\n'
        # re_str += ''.join(word_list[-1])
        return re_str

    def _line311(matched):
        re_str = ''
        time = matched.group("stream311")
        word_list = [c for c in time]

        re_str = ''
        for i, c in enumerate(word_list):
            if i == 0:
                re_str += '\n' + c + ' B-' + '311' + '\n'
            else:
                re_str += c + ' I-' + '311' + '\n'
        # re_str += ''.join(word_list[-1])
        return re_str

    def _line312(matched):
        re_str = ''
        time = matched.group("stream312")
        word_list = [c for c in time]

        re_str = ''
        for i, c in enumerate(word_list):
            if i == 0:
                re_str += '\n' + c + ' B-' + '312' + '\n'
            else:
                re_str += c + ' I-' + '312' + '\n'
        # re_str += ''.join(word_list[-1])
        return re_str

    def _line313(matched):
        re_str = ''
        time = matched.group("stream313")
        word_list = [c for c in time]

        re_str = ''
        for i, c in enumerate(word_list):
            if i == 0:
                re_str += '\n' + c + ' B-' + '313' + '\n'
            else:
                re_str += c + ' I-' + '313' + '\n'
        # re_str += ''.join(word_list[-1])
        return re_str

    '''
    author: jsheng
    end 
    '''

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
    '''
    author: jsheng
    start 
    '''

    # 银行类
    # 301: 交易金额
    # 302: 日期
    # 303: 银行账号（尾号）
    # 304: 取款金额
    # 305: 支付金额
    # 306: 余额
    # 307: 存入/转入
    # 312: 还款日
    # 313: 已还金额

    # 银行类
    if "10085" not in line:
        line = re.sub(ur"(?P<stream9>转账[\d\.]+)", _line1, line.strip())
        line = re.sub(ur"(?P<stream9>金额[\d\.]+)", _line1, line.strip())
        line = re.sub(ur"(?P<stream9>转出[\d\.]+)", _line1, line.strip())

    line = re.sub(ur"(?P<stream405>(\d{4,4}年)(\d{1,2}月)(\d{1,2}日)?(\d{2,2}时)?(\d{2,2}分)?(\d{2,2}\:\d{2,2})?)", _line405,
                  line.strip())

    line = re.sub(ur"(?P<stream312>还款最迟(\d{4,4}年)(\d{1,2}月)(\d{1,2}日)?(\d{2,2}时)?(\d{2,2}分)?(\d{2,2}\:\d{2,2})?)",
                  _line312, line.strip())

    line = re.sub(ur"(?P<stream10>尾号.{0,1}\d{4,4})", _line2, line.strip())

    line = re.sub(ur"(?P<stream11>取款[\d\.]{2,})", _line3, line.strip())
    line = re.sub(ur"(?P<stream11>支[出取](人民币)?为?(\(.+\))?[\d\.]+)", _line3, line.strip())

    line = re.sub(ur"(?P<stream11>付款.{0,3}\d+)", _line4, line.strip())

    line = re.sub(ur"(?P<stream12>余额-?为?(人民币)?[\d\.,]{2,})", _line5, line.strip())
    line = re.sub(ur"(?P<stream12>托收[\d\.,]{2,})", _line5, line.strip())

    line = re.sub(ur"(?P<stream13>存入(人民币)?[\d\.]{2,})", _line6, line.strip())
    line = re.sub(ur"(?P<stream13>存款[\d\.]{2,})", _line6, line.strip())
    line = re.sub(ur"(?P<stream13>工资[\d\.])", _line6, line.strip())
    line = re.sub(ur"(?P<stream13>转入[\d\.]+)", _line6, line.strip())

    line = re.sub(ur"(?P<stream313>成功还款[\d\.]{2,})", _line313, line.strip())

    # 差旅类

    line = re.sub(ur"(?P<stream14>[(订单)(取票)]号?\d+)", _line20, line.strip())

    # 始发地与目的地
    start = -1
    end = -1

    idx_list = [i.start() for i in re.finditer(u'飞', line)]
    idx_list += [i.start() for i in re.finditer(u'-', line)]
    idx_list += [i.start() for i in re.finditer(u'到', line)]
    idx_list += [i.start() for i in re.finditer(u'至', line)]
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

    if u"火车" in line or u"飞机" in line or u"航班" in line:
        line = re.sub(ur"(?P<stream17>\d{2,2}\:\d{2,2})", _line23, line.strip())

    '''
    author: jsheng
    end 
    '''

    # 流量类
    line = re.sub(ur"(?P<time>截[至止](\d{4,4}年)?(\d{1,2}月)(\d{1,2}日)?(\d{2,2}时)?(\d{2,2}分)?)", _line7, line.strip())
    line = re.sub(ur"(?P<stream1>国内通用流量共([\d\.]+[MG]{0,1}B{0,1}){1,3})", _line8, line.strip())
    line = re.sub(ur"(?P<stream2>省内流量剩余([\d\.]+[MG]{0,1}B{0,1}){1,3})", _line9, line.strip())
    line = re.sub(ur"(?P<stream3>套餐外流量为([\d\.]+[MG]{0,1}B{0,1}){1,3})", _line10, line.strip())
    line = re.sub(ur"(?P<stream4>国内流量剩余([\d\.]+[MG]{0,1}B{0,1}){1,3})", _line11, line.strip())
    line = re.sub(ur"(?P<stream5>已?使用.{,4}流量数?([\d\.]+[MGB(MB)(GB)]){1,3})", _line12, line.strip())

    line = re.sub(ur"(?P<stream6>套餐内流量剩余([\d\.]+[MG]{0,1}B{0,1}){1,3})", _line13, line.strip())
    line = re.sub(ur"(?P<stream6>剩余(流量)?([\d\.]+[MGB(MB)(GB)]){1,3})", _line13, line.strip())

    line = re.sub(ur"(?P<stream402>已使?用(流量)?数?[\d\.]+([MGB(MB)(GB)]){1,3})", _line402, line.strip())

    line = re.sub(ur"(?P<stream401>本月.{,6}流量共([\d\.]+[MG]{0,1}B{0,1}){1,3})", _line401, line.strip())
    line = re.sub(ur"(?P<stream401>流量共有[\d\.]+([MGB(MB)(GB)]){1,3})", _line401, line.strip())

    line = re.sub(ur"(?P<stream403>套餐内(流量)?使用.+?([\d\.]+[MG]{0,1}B{0,1}){1,3})", _line403, line.strip())
    line = re.sub(ur"(?P<stream404>套餐外(流量)?使用.+?([\d\.]+[MG]{0,1}B{0,1}){1,3})", _line404, line.strip())

    # 水电煤
    line = re.sub(ur"(?P<stream18>欠费-?[\d\.]{2,})", _line24, line.strip())
    line = re.sub(ur"(?P<stream19>电费[\d\.]+)", _line25, line.strip())
    line = re.sub(ur"(?P<stream20>用电量[\d\.]+)", _line26, line.strip())
    line = re.sub(ur"(?P<stream21>水费[\d\.]+)", _line27, line.strip())
    line = re.sub(ur"(?P<stream22>用水量[\d\.]+)", _line28, line.strip())
    if u'电话' not in line and u'户' in line and (u"电费" in line or u"用电量" in line or u"水费" in line or u"用水量" in line):
        line = re.sub(ur"(?P<stream23>[\d\.]+)", _line29, line.strip())

    """
    author: konglili
            start
    """

    # 使用话费
    line = re.sub(ur"(?P<stream111>(话费)-?为?(人民币)?(：)?-?[\d\.]{1,})", _line111,
                  line.strip())

    # 查询话费: 账户余额 必配  label-100
    line = re.sub(ur"(?P<stream100>(账户余额|话费余额|当前余额)-?为?(人民币)?(：)?-?[\d\.]{1,})", labeling(100).match_digitnumber,
                  line.strip())

    # 话费余额提醒，余额状态 必配  "余额不足-101"，"欠费-102"
    if u'余额不足' in line:
        line = re.sub(ur"(?P<stream101>(余额不足|余额)-?为?[\d\.]{1,})", labeling(101).match_digitnumber, line.strip())
    if u'已欠费' in line:
        line = re.sub(ur"(?P<stream102>欠费(金额)?-?为?[\d\.]{1,})", labeling(102).match_digitnumber, line.strip())

    # 账单提醒 消费金额-103 必配
    line = re.sub(ur"(?P<stream103>(本月|已)?消费(金额)?-?为?(：)?[\d\.]{1,})", labeling(103).match_digitnumber, line.strip())

    # 充值成功 缴费金额-104 必配
    line = re.sub(ur"(?P<stream104>(充值成功|充值金额|成功充值|缴费金额)-?为?[\d\.]{1,})", labeling(104).match_digitnumber, line.strip())

    # 交易提醒 支付金额-105 发起交易-106 退款金额-107 必配
    line = re.sub(ur"(?P<stream105>支出.*(人民币)?(:)?[\d\.]{1,})", labeling(105).match_digitnumber, line.strip())
    line = re.sub(ur"(?P<stream106>发起交易[\d\.]{1,})", labeling(106).match_digitnumber, line.strip())
    line = re.sub(ur"(?P<stream107>[\d\.]{1,}元退款)", labeling(107).match_digitnumber, line.strip())
    line = re.sub(ur"(?P<stream107>退款([a-z]{1,})?([A-Z]{1,})?(金额)-?为?[\d\.]{1,})", labeling(107).match_digitnumber,
                  line.strip())

    # 团购 详单 券号-108 必配
    line = re.sub(ur"(?P<stream108>(取票|券)号-?为?(“)?(：)?[a-zA-Z0-9\-]{1,})", labeling(108).match_ordernumber,
                  line.strip())

    # 生后快递 签收提醒 订单号 快件 单号 快递 - 109   派送提醒 订单号 快件 单号 快递 - 110
    if u'签收' in line or u'代收' in line:
        line = re.sub(ur"(?P<stream109>(快递|快件|单号)[a-zA-Z0-9\-]{1,})", labeling(109).match_ordernumber, line.strip())
    if u'派送' in line or u'派件' in line:
        line = re.sub(ur"(?P<stream110>(快递|快递号|快件|单号)(：)?[a-zA-Z0-9\-]{1,})", labeling(110).match_ordernumber,
                      line.strip())

    """
    author: konglili
            end
    """

    """
    author：chenyuxiang
            start
    """

    # 包月详情
    line = re.sub(ur"(?P<stream200>剩余流量总计([\d\.]+[MG]{0,1}B{0,1}){1,3})", labeling(200).match_digitnumber, line.strip())
    line = re.sub(ur"(?P<stream201>WLAN剩余([\d\.]+[MG]{0,1}B{0,1}){1,3})", labeling(201).match_digitnumber, line.strip())
    line = re.sub(ur"(?P<stream202>流量剩余([\d\.]+[MG]{0,1}B{0,1}){1,3})", labeling(202).match_digitnumber, line.strip())
    line = re.sub(ur"(?P<stream203>语音剩余([\d]){1,})", labeling(203).match_digitnumber, line.strip())
    line = re.sub(ur"(?P<stream211>短信剩余([\d\.]){1,})", labeling(211).match_digitnumber, line.strip())

    # 已开通业务
    line = re.sub(ur"(?P<stream204>您已开通的优惠如下：([\d\.]+[.*]+[；;。]){1,3})", labeling(204).match_workword, line.strip())
    line = re.sub(ur"(?P<stream205>您已开通的套餐业务有：([\d\.]+[.*]+[，;。]){1,3})", labeling(205).match_workword, line.strip())
    line = re.sub(ur"(?P<stream206>您已开通如下功能：([.*]+[;。]){1,2})", labeling(206).match_workword, line.strip())
    line = re.sub(ur"(?P<stream207>您已开通的套餐有：([\d\、]+[.*]+[，;。]){1,3})", labeling(207).match_workword, line.strip())

    # 票务

    line = re.sub(ur"(?P<stream208>影票信息：.*，.*，)", labeling(208).match_workword, line.strip())
    line = re.sub(ur"(?P<stream209>影片：.*，)", labeling(209).match_workword, line.strip())
    line = re.sub(ur"(?P<stream210>放映时间：.*，)", labeling(210).match_workword, line.strip())

    """
    author: xiaoxingxing
            end
    """

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
