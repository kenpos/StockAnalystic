from arelle import ModelManager
from arelle import Cntlr

class jplvh_大量保有報告書_追加DEI:#大量保有報告書の追加DEI
	AdditionalDEIForReportOfLargeVolumeHoldingAbstract = '' #大量保有報告書の追加DEI [タイトル項目]
	InformationAboutFilersLargeVolumeHoldersAndJointHoldersDEITable = '' #提出者（大量保有者）・共同保有者情報、大量保有DEI [表]
	FilersLargeVolumeHoldersAndJointHoldersAxis = '' #提出者（大量保有者）・共同保有者 [軸]
	FilersLargeVolumeHoldersOrJointHoldersMember = '' #提出者（大量保有者）・共同保有者 [メンバー] ※ディメンションデフォルト
	FilersLargeVolumeHoldersMember = '' #提出者（大量保有者） [メンバー]
	JointHoldersMember = '' #共同保有者 [メンバー]
	InformationAboutFilersAndJointHoldersDEILineItems = '' #提出者・共同保有者情報、大量保有DEI [表示項目]
	EDINETCodeDEI = '' #EDINETコード、大量保有DEI
	SecurityCodeDEI = '' #証券コード、大量保有DEI
	FilerNameInJapaneseDEI = '' #氏名又は名称（日本語表記）、大量保有DEI
	FilerNameInEnglishDEI = '' #氏名又は名称（英語表記）、大量保有DEI

	def __init__(self,xbrl_file):
		ctrl = Cntlr.Cntlr()
		model_manager = ModelManager.initialize(ctrl)
		self.model_xbrl = model_manager.load(xbrl_file)
	def setInfo(self, edinet_info_list):
		for fact in self.model_xbrl.facts:
			if fact.concept.qname.localName == 'EDINETCodeDEI':
				self.edinet_code = fact.value
				for code_name in edinet_info_list:
					if code_name[0] == self.edinet_code:
						self.industry_code = code_name[1]
						break
			elif fact.concept.qname.localName == 'AdditionalDEIForReportOfLargeVolumeHoldingAbstract': #大量保有報告書の追加DEI [タイトル項目]
				self.AdditionalDEIForReportOfLargeVolumeHoldingAbstract = fact.value

			elif fact.concept.qname.localName == 'InformationAboutFilersLargeVolumeHoldersAndJointHoldersDEITable': #提出者（大量保有者）・共同保有者情報、大量保有DEI [表]
				self.InformationAboutFilersLargeVolumeHoldersAndJointHoldersDEITable = fact.value

			elif fact.concept.qname.localName == 'FilersLargeVolumeHoldersAndJointHoldersAxis': #提出者（大量保有者）・共同保有者 [軸]
				self.FilersLargeVolumeHoldersAndJointHoldersAxis = fact.value

			elif fact.concept.qname.localName == 'FilersLargeVolumeHoldersOrJointHoldersMember': #提出者（大量保有者）・共同保有者 [メンバー] ※ディメンションデフォルト
				self.FilersLargeVolumeHoldersOrJointHoldersMember = fact.value

			elif fact.concept.qname.localName == 'FilersLargeVolumeHoldersMember': #提出者（大量保有者） [メンバー]
				self.FilersLargeVolumeHoldersMember = fact.value

			elif fact.concept.qname.localName == 'JointHoldersMember': #共同保有者 [メンバー]
				self.JointHoldersMember = fact.value

			elif fact.concept.qname.localName == 'InformationAboutFilersAndJointHoldersDEILineItems': #提出者・共同保有者情報、大量保有DEI [表示項目]
				self.InformationAboutFilersAndJointHoldersDEILineItems = fact.value

			elif fact.concept.qname.localName == 'EDINETCodeDEI': #EDINETコード、大量保有DEI
				self.EDINETCodeDEI = fact.value

			elif fact.concept.qname.localName == 'SecurityCodeDEI': #証券コード、大量保有DEI
				self.SecurityCodeDEI = fact.value

			elif fact.concept.qname.localName == 'FilerNameInJapaneseDEI': #氏名又は名称（日本語表記）、大量保有DEI
				self.FilerNameInJapaneseDEI = fact.value

			elif fact.concept.qname.localName == 'FilerNameInEnglishDEI': #氏名又は名称（英語表記）、大量保有DEI
				self.FilerNameInEnglishDEI = fact.value


	def getAdditionalDEIForReportOfLargeVolumeHoldingAbstract(self): #大量保有報告書の追加DEI [タイトル項目]
		return self.AdditionalDEIForReportOfLargeVolumeHoldingAbstract

	def getInformationAboutFilersLargeVolumeHoldersAndJointHoldersDEITable(self): #提出者（大量保有者）・共同保有者情報、大量保有DEI [表]
		return self.InformationAboutFilersLargeVolumeHoldersAndJointHoldersDEITable

	def getFilersLargeVolumeHoldersAndJointHoldersAxis(self): #提出者（大量保有者）・共同保有者 [軸]
		return self.FilersLargeVolumeHoldersAndJointHoldersAxis

	def getFilersLargeVolumeHoldersOrJointHoldersMember(self): #提出者（大量保有者）・共同保有者 [メンバー] ※ディメンションデフォルト
		return self.FilersLargeVolumeHoldersOrJointHoldersMember

	def getFilersLargeVolumeHoldersMember(self): #提出者（大量保有者） [メンバー]
		return self.FilersLargeVolumeHoldersMember

	def getJointHoldersMember(self): #共同保有者 [メンバー]
		return self.JointHoldersMember

	def getInformationAboutFilersAndJointHoldersDEILineItems(self): #提出者・共同保有者情報、大量保有DEI [表示項目]
		return self.InformationAboutFilersAndJointHoldersDEILineItems

	def getEDINETCodeDEI(self): #EDINETコード、大量保有DEI
		return self.EDINETCodeDEI

	def getSecurityCodeDEI(self): #証券コード、大量保有DEI
		return self.SecurityCodeDEI

	def getFilerNameInJapaneseDEI(self): #氏名又は名称（日本語表記）、大量保有DEI
		return self.FilerNameInJapaneseDEI

	def getFilerNameInEnglishDEI(self): #氏名又は名称（英語表記）、大量保有DEI
		return self.FilerNameInEnglishDEI
