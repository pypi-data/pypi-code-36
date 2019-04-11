# -*- coding:utf-8 -*-
import random
from SCLibrary.base import keyword

class RandomKeywords(object):
    @keyword("Random Item Of Array")
    def random_item_of_array(self, arr, num=None):
        """ 随机返回数组中的某一项 """
        if type(arr) is not list:
            raise ValueError('类型错误：传入的参数不是一个数组')
        length = len(arr)

        if num == None:
            return arr[random.randint(0, length - 1)]

        num = int(num)
        if num == -1:
            num = random.randint(1, length)

        if num < length:
            times = length - num
            for i in range(times):
                length = len(arr)
                index = random.randint(0, length - 1)
                del arr[index]

        return arr

    @keyword("Random Boolean")
    def boolean(self):
        """ 随机返回一个布尔值，True 或者 False """
        return True if random.randint(0, 1) == 0 else False

    @keyword("Random Float")
    def float(self, start, end):
        """ 随机返回一个float，参数为最小值和最大值(包含) """
        start = float(start)
        end = float(end)
        return random.uniform(start, end)

    @keyword("Random Int")
    def int(self, start, end):
        """ 随机返回一个int，参数为最小值和最大值(包含) """
        start = int(start)
        end = int(end)
        return random.randint(start, end)

    @keyword("Random Name")
    def name(self):
        """ 随机返回一个中文名 """
        last_name = ['王', '李', '张', '刘', '陈', '杨', '赵', '黄', '周', '吴',
                     '徐', '孙', '胡', '朱', '高', '林', '何', '郭', '马', '罗',
                     '梁', '宋', '郑', '谢', '韩', '唐', '冯', '于', '董', '萧',
                     '程', '曹', '袁', '邓', '许', '傅', '沈', '曾', '彭', '吕',
                     '苏', '卢', '蒋', '蔡', '贾', '丁', '魏', '薛', '叶', '阎',
                     '余', '潘', '杜', '戴', '夏', '锺', '汪', '田', '任', '姜',
                     '范', '方', '石', '姚', '谭', '廖', '邹', '熊', '金', '陆',
                     '郝', '孔', '白', '崔', '康', '毛', '邱', '秦', '江', '史',
                     '顾', '侯', '邵', '孟', '龙', '万', '段', '雷', '钱', '汤',
                     '尹', '黎', '易', '常', '武', '乔', '贺', '赖', '龚', '文']
    
        first_name = ['伟', '芳', '娜', '秀英', '敏', '静', '丽', '强', '磊', '军',
                      '洋', '勇', '艳', '杰', '娟', '涛', '明', '超', '秀兰', '霞',
                      '平', '刚', '桂英']
    
        return random.choice(last_name) + random.choice(first_name)
    
    @keyword("Random String")
    def string(self, length = -1, mode=None):
        """ 如果不传参数默认返回1-50长度之间的随机字符串, mode = [CHARS | SYMBOL | NUM | CN] 分别为字符、符号、数字、中文"""
        length = int(length)
        result = ''
        if length < 0:
            length = random.randint(1, 50)
        data = [['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
                ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '[', ']'],
                ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
                ['你', '我', '他', '哈', '黑', '棒', '天', '的', '干', '地', '人', '男', '女', '东', '南', '西', '北', '中', '发', '白', '书', '数', '一', '二', '打', '吹']]
        for _ in range(length):
            if mode == 'CHARS':
                result += random.choice(data[0])
            elif mode == 'SYMBOL':
                result += random.choice(data[1])
            elif mode == 'NUM':
                result += random.choice(data[2])
            elif mode == 'CN':
                result += random.choice(data[3])
            else:
                result += random.choice(random.choice(data))
        return result
    
    @keyword("Random Car Number")
    def license_number(self):
        """ 随机返回一个车牌号 """
        prefix = ['京', '津', '沪', '渝', '冀', '豫',
                  '云', '辽', '黑', '湘', '皖', '鲁',
                  '新', '苏', '浙', '赣', '鄂', '桂',
                  '甘', '晋', '蒙', '陕', '吉', '闽',
                  '贵', '粤', '青', '藏', '川', '宁',
                  '琼']
        result = random.choice(prefix) + random.choice(['A', 'B', 'C'])
        for _ in range(5):
            seed = random.randint(0, 100)
            if seed < 10:
                result += random.choice([chr(i) for i in range(ord('A'),ord('Z')+1)])
            else:
                result += random.choice([str(i) for i in range(0, 10)])
        return result
    
    @keyword("Random Phone")
    def phone(self):
        """ 随机返回一个电话号码 """
        arr = [130,131,132,134,135,136,137,138,139,150,151,152,155,156,157,158,159,182,183,184,185,186,187,188,145,147,170,176,178]
        phone = str(arr[random.randint(0, 28)])
        for _ in range(8):
            phone += str(random.randint(0, 9))
        return phone 
    
    @keyword("Random Email")
    def email(self):
        """ 随机返回一个邮箱地址 """
        names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones',
                 'Miller', 'Davis', 'Garcia', 'Rodriguez', 'Wilson', 'Martinez',
                 'Anderson', 'Taylor', 'Thomas', 'Hernandez', 'Moore', 'Martin',
                 'Jackson', 'Thompson', 'White', 'Lopez', 'Lee', 'Gonzalez',
                 'Harris', 'Clark', 'Lewis', 'Robinson', 'Walker',
                 'Perez', 'Hall', 'Young', 'Allen']
        hosts = ['gmail', 'sina', 'qq', '163', 'foxmail',
                 'outlook', 'souche', 'hotmail', 'msn', 'yahoo']
        shuffix = ['.com', '.net', '.org', '.top']
        return random.choice(names) + '@' + random.choice(hosts) + random.choice(shuffix)
    
    @keyword("Random City")
    def city(self):
        """ 随机返回一个城市 """
        cities = ['香港', '澳门','北京市', '天津市', '上海市', '重庆市', '乌鲁木齐','克拉玛依','石河子','阿拉尔市','图木舒克','五家渠','哈密','吐鲁番','阿克苏','喀什','和田','伊宁','塔城','阿勒泰','奎屯','博乐','昌吉','阜康','库尔勒','阿图什','乌苏','拉萨','日喀则','银川','石嘴山','吴忠','固原','中卫','青铜峡市','灵武市','呼和浩特','包头','乌海','赤峰','通辽','鄂尔多斯','呼伦贝尔','巴彦淖尔','乌兰察布','霍林郭勒市','满洲里市','牙克石市','扎兰屯市','根河市','额尔古纳市','丰镇市','锡林浩特市','二连浩特市','乌兰浩特市','阿尔山市','南宁','柳州','桂林','梧州','北海','崇左','来宾','贺州','玉林','百色','河池','钦州','防城港','贵港','岑溪','凭祥','合山','北流','宜州','东兴','桂平','哈尔滨','大庆','齐齐哈尔','佳木斯','鸡西','鹤岗','双鸭山','牡丹江','伊春','七台河','黑河','绥化','五常','双城','尚志','纳河','虎林','密山','铁力','同江','富锦','绥芬河','海林','宁安','穆林','北安','五大连池','肇东','海伦','安达','长春','吉林','四平','辽源','通化','白山','松原','白城','九台市','榆树市','德惠市','舒兰市','桦甸市','蛟河市','磐石市','公主岭市','双辽市','梅河口市','集安市','临江市','大安市','洮南市','延吉市','图们市','敦化市','龙井市','珲春市','和龙市','沈阳','大连','鞍山','抚顺','本溪','丹东','锦州','营口','阜新','辽阳','盘锦','铁岭','朝阳','葫芦岛','新民','瓦房店','普兰','庄河','海城','东港','凤城','凌海','北镇','大石桥','盖州','灯塔','调兵山','开原','凌源','北票','兴城','石家庄','唐山','邯郸','秦皇岛','保定','张家口','承德','廊坊','沧州','衡水','邢台','辛集市','藁城市','晋州市','新乐市','鹿泉市','遵化市','迁安市','武安市','南宫市','沙河市','涿州市','定州市','安国市','高碑店市','泊头市','任丘市','黄骅市','河间市','霸州市','三河市','冀州市','深州市','济南','青岛','淄博','枣庄','东营','烟台','潍坊','济宁','泰安','威海','日照','莱芜','临沂','德州','聊城','菏泽','滨州','章丘','胶南','胶州','平度','莱西','即墨','滕州','龙口','莱阳','莱州','招远','蓬莱','栖霞','海阳','青州','诸城','安丘','高密','昌邑','兖州','曲阜','邹城','乳山','文登','荣成','乐陵','临清','禹城','南京','镇江','常州','无锡','苏州','徐州','连云港','淮安','盐城','扬州','泰州','南通','宿迁','江阴市','宜兴市','邳州市','新沂市','金坛市','溧阳市','常熟市','张家港市','太仓市','昆山市','吴江市','如皋市','通州市','海门市','启东市','东台市','大丰市','高邮市','江都市','仪征市','丹阳市','扬中市','句容市','泰兴市','姜堰市','靖江市','兴化市','合肥','蚌埠','芜湖','淮南','亳州','阜阳','淮北','宿州','滁州','安庆','巢湖','马鞍山','宣城','黄山','池州','铜陵','界首','天长','明光','桐城','宁国','杭州','嘉兴','湖州','宁波','金华','温州','丽水','绍兴','衢州','舟山','台州','建德市','富阳市','临安市','余姚市','慈溪市','奉化市','瑞安市','乐清市','海宁市','平湖市','桐乡市','诸暨市','上虞市','嵊州市','兰溪市','义乌市','东阳市','永康市','江山市','临海市','温岭市','龙泉市','福州','厦门','泉州','三明','南平','漳州','莆田','宁德','龙岩','福清市','长乐市','永安市','石狮市','晋江市','南安市','龙海市','邵武市','武夷山','建瓯市','建阳市','漳平市','福安市','福鼎市','广州','深圳','汕头','惠州','珠海','揭阳','佛山','河源','阳江','茂名','湛江','梅州','肇庆','韶关','潮州','东莞','中山','清远','江门','汕尾','云浮','增城市','从化市','乐昌市','南雄市','台山市','开平市','鹤山市','恩平市','廉江市','雷州市 吴川市','高州市','化州市','高要市','四会市','兴宁市','陆丰市','阳春市','英德市','连州市','普宁市','罗定市','海口','三亚','琼海','文昌','万宁','五指山','儋州','东方','昆明','曲靖','玉溪','保山','昭通','丽江','普洱','临沧','安宁市','宣威市','个旧市','开远市','景洪市','楚雄市','大理市','潞西市','瑞丽市','贵阳','六盘水','遵义','安顺','清镇市','赤水市','仁怀市','铜仁市','毕节市','兴义市','凯里市','都匀市','福泉市','成都','绵阳','德阳','广元','自贡','攀枝花','乐山','南充','内江','遂宁','广安','泸州','达州','眉山','宜宾','雅安','资阳', '都江堰市','彭州市','邛崃市','崇州市','广汉市','什邡市','绵竹市','江油市','峨眉山市','阆中市','华蓥市','万源市','简阳市','西昌市','长沙','株洲','湘潭','衡阳','岳阳','郴州','永州','邵阳','怀化','常德','益阳','张家界','娄底','浏阳市','醴陵市','湘乡市','韶山市','耒阳市','常宁市','武冈市','临湘市','汨罗市','津市市','沅江市','资兴市','洪江市','冷水江市','涟源市','吉首市','武汉','襄樊','宜昌','黄石','鄂州','随州','荆州','荆门','十堰','孝感','黄冈','咸宁','大冶市','丹江口市','洪湖市','石首市','松滋市','宜都市','当阳市','枝江市','老河口市','枣阳市','宜城市','钟祥市','应城市','安陆市','汉川市','麻城市','武穴市','赤壁市','广水市','仙桃市','天门市','潜江市','恩施市','利川市','郑州','洛阳','开封','漯河','安阳','新乡','周口','三门峡','焦作','平顶山','信阳','南阳','鹤壁','濮阳','许昌','商丘','驻马店','巩义市','新郑市','新密市','登封市','荥阳市','偃师市','汝州市','舞钢市','林州市','卫辉市','辉县市','沁阳市','孟州市','禹州市','长葛市','义马市','灵宝市','邓州市','永城市','项城市','济源市','太原','大同','忻州','阳泉','长治','晋城','朔州','晋中','运城','临汾','吕梁','古交','潞城','高平','介休','永济','河津','原平','侯马','霍州','孝义','汾阳','西安','咸阳','铜川','延安','宝鸡','渭南','汉中','安康','商洛','榆林','兴平市','韩城市','华阴市','兰州','天水','平凉','酒泉','嘉峪关','金昌','白银','武威','张掖','庆阳','定西','陇南','玉门市','敦煌市','临夏市','合作市','西宁','格尔木','德令哈','南昌','九江','赣州','吉安','鹰潭','上饶','萍乡','景德镇','新余','宜春','抚州','乐平市','瑞昌市','贵溪市','瑞金市','南康市','井冈山市','丰城市','樟树市','高安市','德兴市','台北','台中','基隆','高雄','台南','新竹','嘉义','板桥市','宜兰市','竹北市','桃园市','苗栗市','丰原市','彰化市','南投市','太保市','斗六市','新营市','凤山市','屏东市','台东市','花莲市','马公市']
        return random.choice(cities)
    
    @keyword("Random Province")
    def province(self):
        """ 随机返回一个省份 """
        provices= ['北京市', '天津市', '上海市', '重庆市', '河北省', '山西省',
                    '辽宁省', '吉林省', '黑龙江省', '江苏省', '浙江省', '安徽省',
                    '福建省', '江西省', '山东省', '河南省', '湖北省', '湖南省',
                    '广东省', '海南省', '四川省', '贵州省', '云南省', '陕西省',
                    '甘肃省', '青海省', '台湾省', '内蒙古自治区', '广西壮族自治区', '西藏自治区',
                    '宁夏回族自治区', '新疆维吾尔自治区', '香港特别行政区', '澳门特别行政区']
        return random.choice(provices)