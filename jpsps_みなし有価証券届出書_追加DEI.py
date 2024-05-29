from arelle import ModelManager
from arelle import Cntlr

class jpsps_みなし有価証券届出書_追加DEI:#みなし有価証券届出書の追加DEI
	AdditionalDEIForDeemedRegistrationStatementAbstract = '' #みなし有価証券届出書の追加DEI [タイトル項目]
	ScopeOfAmendmentDeemedRegistrationStatementDEIAbstract = '' #訂正対象区分、みなし有価証券届出書DEI [タイトル項目]
	SecuritiesRegistrationStatementAmendmentFlagDeemedRegistrationStatementDEI = '' #有価証券届出書訂正のフラグ、みなし有価証券届出書DEI
	AnnualSecuritiesReportAmendmentFlagDeemedRegistrationStatementDEI = '' #有価証券報告書訂正のフラグ、みなし有価証券届出書DEI
	IdentificationOfRegistrationStatementSubjectToAmendmentDeemedRegistrationStatementDEI = '' #訂正対象となるみなし有価証券届出書の書類管理番号、みなし有価証券届出書DEI

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
			elif fact.concept.qname.localName == 'AdditionalDEIForDeemedRegistrationStatementAbstract': #みなし有価証券届出書の追加DEI [タイトル項目]
				self.AdditionalDEIForDeemedRegistrationStatementAbstract = fact.value

			elif fact.concept.qname.localName == 'ScopeOfAmendmentDeemedRegistrationStatementDEIAbstract': #訂正対象区分、みなし有価証券届出書DEI [タイトル項目]
				self.ScopeOfAmendmentDeemedRegistrationStatementDEIAbstract = fact.value

			elif fact.concept.qname.localName == 'SecuritiesRegistrationStatementAmendmentFlagDeemedRegistrationStatementDEI': #有価証券届出書訂正のフラグ、みなし有価証券届出書DEI
				self.SecuritiesRegistrationStatementAmendmentFlagDeemedRegistrationStatementDEI = fact.value

			elif fact.concept.qname.localName == 'AnnualSecuritiesReportAmendmentFlagDeemedRegistrationStatementDEI': #有価証券報告書訂正のフラグ、みなし有価証券届出書DEI
				self.AnnualSecuritiesReportAmendmentFlagDeemedRegistrationStatementDEI = fact.value

			elif fact.concept.qname.localName == 'IdentificationOfRegistrationStatementSubjectToAmendmentDeemedRegistrationStatementDEI': #訂正対象となるみなし有価証券届出書の書類管理番号、みなし有価証券届出書DEI
				self.IdentificationOfRegistrationStatementSubjectToAmendmentDeemedRegistrationStatementDEI = fact.value


	def getAdditionalDEIForDeemedRegistrationStatementAbstract(self): #みなし有価証券届出書の追加DEI [タイトル項目]
		return self.AdditionalDEIForDeemedRegistrationStatementAbstract

	def getScopeOfAmendmentDeemedRegistrationStatementDEIAbstract(self): #訂正対象区分、みなし有価証券届出書DEI [タイトル項目]
		return self.ScopeOfAmendmentDeemedRegistrationStatementDEIAbstract

	def getSecuritiesRegistrationStatementAmendmentFlagDeemedRegistrationStatementDEI(self): #有価証券届出書訂正のフラグ、みなし有価証券届出書DEI
		return self.SecuritiesRegistrationStatementAmendmentFlagDeemedRegistrationStatementDEI

	def getAnnualSecuritiesReportAmendmentFlagDeemedRegistrationStatementDEI(self): #有価証券報告書訂正のフラグ、みなし有価証券届出書DEI
		return self.AnnualSecuritiesReportAmendmentFlagDeemedRegistrationStatementDEI

	def getIdentificationOfRegistrationStatementSubjectToAmendmentDeemedRegistrationStatementDEI(self): #訂正対象となるみなし有価証券届出書の書類管理番号、みなし有価証券届出書DEI
		return self.IdentificationOfRegistrationStatementSubjectToAmendmentDeemedRegistrationStatementDEI
