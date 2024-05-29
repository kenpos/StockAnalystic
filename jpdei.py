from arelle import ModelManager
from arelle import Cntlr

class jpdei:#DEI
	DocumentAndEntityInformationDEIAbstract = '' #DEI [タイトル項目]
	EntityInformationDEIAbstract = '' #提出者情報、DEI [タイトル項目]
	EDINETCodeDEI = '' #EDINETコード、DEI
	FundCodeDEI = '' #ファンドコード、DEI
	SecurityCodeDEI = '' #証券コード、DEI
	FilerNameInJapaneseDEI = '' #提出者名（日本語表記）、DEI
	FilerNameInEnglishDEI = '' #提出者名（英語表記）、DEI
	FundNameInJapaneseDEI = '' #ファンド名称（日本語表記）、DEI
	FundNameInEnglishDEI = '' #ファンド名称（英語表記）、DEI
	DocumentInformationDEIAbstract = '' #提出書類情報、DEI [タイトル項目]
	CabinetOfficeOrdinanceDEI = '' #府令、DEI
	DocumentTypeDEI = '' #様式、DEI
	AccountingStandardsDEI = '' #会計基準、DEI
	WhetherConsolidatedFinancialStatementsArePreparedDEI = '' #連結決算の有無、DEI
	IndustryCodeWhenConsolidatedFinancialStatementsArePreparedInAccordanceWithIndustrySpecificRegulationsDEI = '' #別記事業（連結）、DEI
	IndustryCodeWhenFinancialStatementsArePreparedInAccordanceWithIndustrySpecificRegulationsDEI = '' #別記事業（個別）、DEI
	CurrentPeriodDEIAbstract = '' #当会計期間、DEI [タイトル項目]
	CurrentFiscalYearStartDateDEI = '' #当事業年度開始日、DEI
	CurrentPeriodEndDateDEI = '' #当会計期間終了日、DEI
	TypeOfCurrentPeriodDEI = '' #当会計期間の種類、DEI
	CurrentFiscalYearEndDateDEI = '' #当事業年度終了日、DEI
	ComparativePeriodDEIAbstract = '' #比較対象会計期間、DEI [タイトル項目]
	PreviousFiscalYearStartDateDEI = '' #前事業年度開始日、DEI
	ComparativePeriodEndDateDEI = '' #比較対象会計期間終了日、DEI
	PreviousFiscalYearEndDateDEI = '' #前事業年度終了日、DEI
	QuarterlyOrSemiAnnualPeriodOfNextFiscalYearDEIAbstract = '' #次の四半期又は中間期の会計期間、DEI [タイトル項目]
	NextFiscalYearStartDateDEI = '' #次の事業年度開始日、DEI
	EndDateOfQuarterlyOrSemiAnnualPeriodOfNextFiscalYearDEI = '' #次の四半期又は中間期の会計期間終了日、DEI
	NumberOfSubmissionDEI = '' #提出回数、DEI
	AmendmentFlagDEI = '' #訂正の有無、DEI
	IdentificationOfDocumentSubjectToAmendmentDEI = '' #訂正対象書類の書類管理番号、DEI
	TypeOfAmendmentDEIAbstract = '' #訂正の種類、DEI [タイトル項目]
	ReportAmendmentFlagDEI = '' #記載事項訂正のフラグ、DEI
	XBRLAmendmentFlagDEI = '' #XBRL訂正のフラグ、DEI

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
			elif fact.concept.qname.localName == 'DocumentAndEntityInformationDEIAbstract': #DEI [タイトル項目]
				self.DocumentAndEntityInformationDEIAbstract = fact.value

			elif fact.concept.qname.localName == 'EntityInformationDEIAbstract': #提出者情報、DEI [タイトル項目]
				self.EntityInformationDEIAbstract = fact.value

			elif fact.concept.qname.localName == 'EDINETCodeDEI': #EDINETコード、DEI
				self.EDINETCodeDEI = fact.value

			elif fact.concept.qname.localName == 'FundCodeDEI': #ファンドコード、DEI
				self.FundCodeDEI = fact.value

			elif fact.concept.qname.localName == 'SecurityCodeDEI': #証券コード、DEI
				self.SecurityCodeDEI = fact.value

			elif fact.concept.qname.localName == 'FilerNameInJapaneseDEI': #提出者名（日本語表記）、DEI
				self.FilerNameInJapaneseDEI = fact.value

			elif fact.concept.qname.localName == 'FilerNameInEnglishDEI': #提出者名（英語表記）、DEI
				self.FilerNameInEnglishDEI = fact.value

			elif fact.concept.qname.localName == 'FundNameInJapaneseDEI': #ファンド名称（日本語表記）、DEI
				self.FundNameInJapaneseDEI = fact.value

			elif fact.concept.qname.localName == 'FundNameInEnglishDEI': #ファンド名称（英語表記）、DEI
				self.FundNameInEnglishDEI = fact.value

			elif fact.concept.qname.localName == 'DocumentInformationDEIAbstract': #提出書類情報、DEI [タイトル項目]
				self.DocumentInformationDEIAbstract = fact.value

			elif fact.concept.qname.localName == 'CabinetOfficeOrdinanceDEI': #府令、DEI
				self.CabinetOfficeOrdinanceDEI = fact.value

			elif fact.concept.qname.localName == 'DocumentTypeDEI': #様式、DEI
				self.DocumentTypeDEI = fact.value

			elif fact.concept.qname.localName == 'AccountingStandardsDEI': #会計基準、DEI
				self.AccountingStandardsDEI = fact.value

			elif fact.concept.qname.localName == 'WhetherConsolidatedFinancialStatementsArePreparedDEI': #連結決算の有無、DEI
				self.WhetherConsolidatedFinancialStatementsArePreparedDEI = fact.value

			elif fact.concept.qname.localName == 'IndustryCodeWhenConsolidatedFinancialStatementsArePreparedInAccordanceWithIndustrySpecificRegulationsDEI': #別記事業（連結）、DEI
				self.IndustryCodeWhenConsolidatedFinancialStatementsArePreparedInAccordanceWithIndustrySpecificRegulationsDEI = fact.value

			elif fact.concept.qname.localName == 'IndustryCodeWhenFinancialStatementsArePreparedInAccordanceWithIndustrySpecificRegulationsDEI': #別記事業（個別）、DEI
				self.IndustryCodeWhenFinancialStatementsArePreparedInAccordanceWithIndustrySpecificRegulationsDEI = fact.value

			elif fact.concept.qname.localName == 'CurrentPeriodDEIAbstract': #当会計期間、DEI [タイトル項目]
				self.CurrentPeriodDEIAbstract = fact.value

			elif fact.concept.qname.localName == 'CurrentFiscalYearStartDateDEI': #当事業年度開始日、DEI
				self.CurrentFiscalYearStartDateDEI = fact.value

			elif fact.concept.qname.localName == 'CurrentPeriodEndDateDEI': #当会計期間終了日、DEI
				self.CurrentPeriodEndDateDEI = fact.value

			elif fact.concept.qname.localName == 'TypeOfCurrentPeriodDEI': #当会計期間の種類、DEI
				self.TypeOfCurrentPeriodDEI = fact.value

			elif fact.concept.qname.localName == 'CurrentFiscalYearEndDateDEI': #当事業年度終了日、DEI
				self.CurrentFiscalYearEndDateDEI = fact.value

			elif fact.concept.qname.localName == 'ComparativePeriodDEIAbstract': #比較対象会計期間、DEI [タイトル項目]
				self.ComparativePeriodDEIAbstract = fact.value

			elif fact.concept.qname.localName == 'PreviousFiscalYearStartDateDEI': #前事業年度開始日、DEI
				self.PreviousFiscalYearStartDateDEI = fact.value

			elif fact.concept.qname.localName == 'ComparativePeriodEndDateDEI': #比較対象会計期間終了日、DEI
				self.ComparativePeriodEndDateDEI = fact.value

			elif fact.concept.qname.localName == 'PreviousFiscalYearEndDateDEI': #前事業年度終了日、DEI
				self.PreviousFiscalYearEndDateDEI = fact.value

			elif fact.concept.qname.localName == 'QuarterlyOrSemiAnnualPeriodOfNextFiscalYearDEIAbstract': #次の四半期又は中間期の会計期間、DEI [タイトル項目]
				self.QuarterlyOrSemiAnnualPeriodOfNextFiscalYearDEIAbstract = fact.value

			elif fact.concept.qname.localName == 'NextFiscalYearStartDateDEI': #次の事業年度開始日、DEI
				self.NextFiscalYearStartDateDEI = fact.value

			elif fact.concept.qname.localName == 'EndDateOfQuarterlyOrSemiAnnualPeriodOfNextFiscalYearDEI': #次の四半期又は中間期の会計期間終了日、DEI
				self.EndDateOfQuarterlyOrSemiAnnualPeriodOfNextFiscalYearDEI = fact.value

			elif fact.concept.qname.localName == 'NumberOfSubmissionDEI': #提出回数、DEI
				self.NumberOfSubmissionDEI = fact.value

			elif fact.concept.qname.localName == 'AmendmentFlagDEI': #訂正の有無、DEI
				self.AmendmentFlagDEI = fact.value

			elif fact.concept.qname.localName == 'IdentificationOfDocumentSubjectToAmendmentDEI': #訂正対象書類の書類管理番号、DEI
				self.IdentificationOfDocumentSubjectToAmendmentDEI = fact.value

			elif fact.concept.qname.localName == 'TypeOfAmendmentDEIAbstract': #訂正の種類、DEI [タイトル項目]
				self.TypeOfAmendmentDEIAbstract = fact.value

			elif fact.concept.qname.localName == 'ReportAmendmentFlagDEI': #記載事項訂正のフラグ、DEI
				self.ReportAmendmentFlagDEI = fact.value

			elif fact.concept.qname.localName == 'XBRLAmendmentFlagDEI': #XBRL訂正のフラグ、DEI
				self.XBRLAmendmentFlagDEI = fact.value


	def getDocumentAndEntityInformationDEIAbstract(self): #DEI [タイトル項目]
		return self.DocumentAndEntityInformationDEIAbstract

	def getEntityInformationDEIAbstract(self): #提出者情報、DEI [タイトル項目]
		return self.EntityInformationDEIAbstract

	def getEDINETCodeDEI(self): #EDINETコード、DEI
		return self.EDINETCodeDEI

	def getFundCodeDEI(self): #ファンドコード、DEI
		return self.FundCodeDEI

	def getSecurityCodeDEI(self): #証券コード、DEI
		return self.SecurityCodeDEI

	def getFilerNameInJapaneseDEI(self): #提出者名（日本語表記）、DEI
		return self.FilerNameInJapaneseDEI

	def getFilerNameInEnglishDEI(self): #提出者名（英語表記）、DEI
		return self.FilerNameInEnglishDEI

	def getFundNameInJapaneseDEI(self): #ファンド名称（日本語表記）、DEI
		return self.FundNameInJapaneseDEI

	def getFundNameInEnglishDEI(self): #ファンド名称（英語表記）、DEI
		return self.FundNameInEnglishDEI

	def getDocumentInformationDEIAbstract(self): #提出書類情報、DEI [タイトル項目]
		return self.DocumentInformationDEIAbstract

	def getCabinetOfficeOrdinanceDEI(self): #府令、DEI
		return self.CabinetOfficeOrdinanceDEI

	def getDocumentTypeDEI(self): #様式、DEI
		return self.DocumentTypeDEI

	def getAccountingStandardsDEI(self): #会計基準、DEI
		return self.AccountingStandardsDEI

	def getWhetherConsolidatedFinancialStatementsArePreparedDEI(self): #連結決算の有無、DEI
		return self.WhetherConsolidatedFinancialStatementsArePreparedDEI

	def getIndustryCodeWhenConsolidatedFinancialStatementsArePreparedInAccordanceWithIndustrySpecificRegulationsDEI(self): #別記事業（連結）、DEI
		return self.IndustryCodeWhenConsolidatedFinancialStatementsArePreparedInAccordanceWithIndustrySpecificRegulationsDEI

	def getIndustryCodeWhenFinancialStatementsArePreparedInAccordanceWithIndustrySpecificRegulationsDEI(self): #別記事業（個別）、DEI
		return self.IndustryCodeWhenFinancialStatementsArePreparedInAccordanceWithIndustrySpecificRegulationsDEI

	def getCurrentPeriodDEIAbstract(self): #当会計期間、DEI [タイトル項目]
		return self.CurrentPeriodDEIAbstract

	def getCurrentFiscalYearStartDateDEI(self): #当事業年度開始日、DEI
		return self.CurrentFiscalYearStartDateDEI

	def getCurrentPeriodEndDateDEI(self): #当会計期間終了日、DEI
		return self.CurrentPeriodEndDateDEI

	def getTypeOfCurrentPeriodDEI(self): #当会計期間の種類、DEI
		return self.TypeOfCurrentPeriodDEI

	def getCurrentFiscalYearEndDateDEI(self): #当事業年度終了日、DEI
		return self.CurrentFiscalYearEndDateDEI

	def getComparativePeriodDEIAbstract(self): #比較対象会計期間、DEI [タイトル項目]
		return self.ComparativePeriodDEIAbstract

	def getPreviousFiscalYearStartDateDEI(self): #前事業年度開始日、DEI
		return self.PreviousFiscalYearStartDateDEI

	def getComparativePeriodEndDateDEI(self): #比較対象会計期間終了日、DEI
		return self.ComparativePeriodEndDateDEI

	def getPreviousFiscalYearEndDateDEI(self): #前事業年度終了日、DEI
		return self.PreviousFiscalYearEndDateDEI

	def getQuarterlyOrSemiAnnualPeriodOfNextFiscalYearDEIAbstract(self): #次の四半期又は中間期の会計期間、DEI [タイトル項目]
		return self.QuarterlyOrSemiAnnualPeriodOfNextFiscalYearDEIAbstract

	def getNextFiscalYearStartDateDEI(self): #次の事業年度開始日、DEI
		return self.NextFiscalYearStartDateDEI

	def getEndDateOfQuarterlyOrSemiAnnualPeriodOfNextFiscalYearDEI(self): #次の四半期又は中間期の会計期間終了日、DEI
		return self.EndDateOfQuarterlyOrSemiAnnualPeriodOfNextFiscalYearDEI

	def getNumberOfSubmissionDEI(self): #提出回数、DEI
		return self.NumberOfSubmissionDEI

	def getAmendmentFlagDEI(self): #訂正の有無、DEI
		return self.AmendmentFlagDEI

	def getIdentificationOfDocumentSubjectToAmendmentDEI(self): #訂正対象書類の書類管理番号、DEI
		return self.IdentificationOfDocumentSubjectToAmendmentDEI

	def getTypeOfAmendmentDEIAbstract(self): #訂正の種類、DEI [タイトル項目]
		return self.TypeOfAmendmentDEIAbstract

	def getReportAmendmentFlagDEI(self): #記載事項訂正のフラグ、DEI
		return self.ReportAmendmentFlagDEI

	def getXBRLAmendmentFlagDEI(self): #XBRL訂正のフラグ、DEI
		return self.XBRLAmendmentFlagDEI
