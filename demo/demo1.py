# -*- coding: utf-8 -*-
# @Date : 2019/10/16
# @Author : water
# @Version  : v1.0
# @Desc  :

def search_dict_key(temp,target_key,target_value):
    for k in temp:
        if k == target_key:
            temp[k] = target_value
            print(f"if 中 {k}")
            break
        elif isinstance(temp[k], dict):
            search_dict_key(temp[k],target_key,target_value)
        elif isinstance(temp[k],list):
            for l in temp[k]:
                search_dict_key(l, target_key, target_value)
    return temp

if __name__ == "__main__":
    temp = {
	"head": {
		"lsh": "1234567890",
		"pjdm": "150901000089",
		"pjhm": "02703762",
		"jym": "65137256530416380661",
		"jydm": "65137",
		"cydm":"123456",
		"mw": "",
		"sj": "20180515091021",
		"zsdwmc": "航天中心医院",
		"zsdwbm": "000000000100010",
		"zsdwdz": "北京市海淀区玉泉路1号",
		"zsdwdh": "010-88891234",
		"zsdwkhyh": "建设银行北大南大街支行",
		"zsdwzh": "923749732473294",
		"zsxmbm": "000000000100010",
		"zsyj": "执收依据",
		"xzswjdshm": "43234234",
		"jkfs": "医保",
		"jkdwmc": "航天信息",
		"jkdwdz": "北京市海淀区杏石口路甲18号",
		"jkdwkhyh": "工商银行",
		"jkdwzh": "24234315345435",
		"jkdwsjh": "13245678903",
		"jkdwyx": "81924573@163.com",
		"ewm": "+cQhhPMgKB/vzhnCmOMRyL1E3Q4AmR4It3xyEgPmVa76VkndsPgAxy5AtM7cco/D1iaOetfepYjISbo4hxzvOwg7ZOpSERZZ3lFW217/4q7J7r6iv4ZmyMZhHwESl",
		"xzqhbm": "3300",
		"djbm": "0004",
		"mbdm": "0004",
		"hjje": "142.21",
		"kpr": "开票人",
		"fhr": "复核人",
		"skdw": "收款单位",
		"skr": "收款人",
		"jbr": "经办人",
		"qdbz": "0",
		"qdxmmc": "清单项目名称",
		"bz": "备注",
		"pjxzfs": "0",
		"sfqz": "1",
		"qzbh": "",
		"bxzfzt": "0",
		"bxzfrq": "报销作废日期",
		"bxzfbh": "报销作废编号",
		"kzzd": {"xjzpjsje":"2271.21","yljglx":"","cwfje":"123","zdysfxm2je":"4496.50","zyrq":"测试住院日期","zlfzlzf":"123","zyh":"615520171011051725","zdyjsxm3je":"2361.93","zdysfxm4je":"4846.43","sxfje":"7067.36","zdyjsxm2mc":"自定义结算项目1","zdyjsxm4mc":"自定义结算项目3","shbzhm":"381819","lnzf":"3579.95","dnh":"-139140044","cwfzlzf":"123","zdysfxm2mc":"自定义收费项目0","zdysfxm4mc":"自定义收费项目1","xjzf":"123","zptkje":"6691.72","qtje":"5662.47","bjje":"123","sfxj":"123","jcfzlzf":"2649.77","xjtkje":"9362.26","bnzhje":"6873.10","zlzfhj":"5947.50","je":"123","lnye":"123","xjbjje":"266.42","clfje":"6053.07","zcfje":"7968.58","zpbjje":"123","rq":"2017年10月11日","tkje":"123","zcyzlzf":"9546.89","zdysfxm1je":"4835.41","zcfzlzf":"7968.58","zdysfxm3je":"7464.91","zlfje":"123","jsr":"测试支付方法","zdyjsxm2je":"929.19","zdysfxm5je":"7901.39","zdysfxm2zlzf":"4496.50","zdyjsxm4je":"6602.53","ssfje":"123","jcfje":"2649.77","jehj":"68492.78","zcyje":"9546.89","ybzh":"","zdyxm3zlzf":"7464.91","clfzlzf":"6053.07","zdyjsxm1mc":"自定义结算项目0","xyfje":"123","zdyjsxm3mc":"自定义结算项目2","bnzf":"123","kb":"测试科室","sbkh":"381819","zdysfxm1zlzf":"4835.41","blh":"730120171011051725","xyfzlzf":"123","jshjje":"9262.98","zdysfxm1mc":"自定义收费项目2","zdysfxm3mc":"自定义收费项目4","ssfzlzf":"123","zdysfxm5mc":"自定义收费项目3","zchyje":"123","zdysfxm5zlzf":"7901.39","hlfzlzf":"123","xb":"123","ybzhje":"9729.04","zchyzlzf":"123","yblx":"测试医保类型","qtzlzf":"5662.47","yjkje":"9568.43","jyfzlzf":"123","mxbz":"","hlfje":"123","cbr":"","xm":"航信测试","bnye":"123","gzdw":"测试工作单位","sxfzlzf":"7067.36","zdyjsxm1je":"7261.49","zdysfxm4zlzf":"4846.43","lnzhje":"1957.03","jyfje":"123"}
	},
	"item": [{
			"gg": "111",
			"dw": "",
			"xmmc": "string1",
			"dj": "",
			"xmbm": "ing1",
			"xmje": "10.21",
			"sl": "111",
			"kzzd": {"lb":"1231","zlzf":"1231"}
		},
		{
			"xmmc": "项目名称",
			"xmbm": "234234234",
			"gg": "规格",
			"dw": "单位",
			"dj": "11",
			"sl": "12",
			"xmje": "132",
			"kzzd": {"lb":"1231","zlzf":"1231"}
		}],
	"jfxx": [{
		"jflx": "1",
		"delivery": "81924573@163.com"
	}],
	"zdyxmxx": {
		"xmbt": {
			"xm1": "项目标题1",
			"xm2": "项目标题2",
			"xm3": "项目标题3",
			"xm4": "项目标题4",
			"xm5": "项目标题5",
			"xm6": "项目标题6",
			"xm7": "项目标题7",
			"xm8": "项目标题8",
			"xm9": "项目标题9",
			"xm10": "项目标题10"
		},
		"zdyitems": [{
			"xm1": "项目信息1",
			"xm2": "项目信息2",
			"xm3": "项目信息3",
			"xm4": "项目信息4",
			"xm5": "项目信息5",
			"xm6": "项目信息6",
			"xm7": "项目信息7",
			"xm8": "项目信息8",
			"xm9": "项目信息9",
			"xm10": "项目信息10"
		},
		{
			"xm1": "项目信息1",
			"xm2": "项目信息2",
			"xm3": "项目信息3",
			"xm4": "项目信息4",
			"xm5": "项目信息5",
			"xm6": "项目信息6",
			"xm7": "项目信息7",
			"xm8": "项目信息8",
			"xm9": "项目信息9",
			"xm10": "项目信息10"
		}]
	}
    }
    print(search_dict_key(temp,"xm7","AAAA修改成功AAAA"))
