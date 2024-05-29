from arelle import ModelManager
from arelle import Cntlr

class jpsps100000:#特定有価証券の内容等の開示に関する内閣府令 第十号様式 半期報告書
	CabinetOfficeOrdinanceOnDisclosureOfInformationEtcOnSpecifiedSecuritiesFormNo10SemiannualSecuritiesReportHeading = '' #特定有価証券の内容等の開示に関する内閣府令 第十号様式 半期報告書 [目次項目]
	CoverPageHeading = '' #表紙 [目次項目]
	CoverPageHeading = '' #表紙 [目次項目]
	DocumentTitleCoverPage = '' #提出書類、表紙
	PlaceOfFilingCoverPage = '' #提出先、表紙
	FilingDateCoverPage = '' #提出日、表紙
	AccountingPeriodCoverPage = '' #計算期間、表紙
	FundNameCoverPage = '' #ファンド名、表紙
	IssuerNameCoverPage = '' #発行者名、表紙
	TitleAndNameOfRepresentativeCoverPage = '' #代表者の役職氏名、表紙
	AddressOfRegisteredHeadquarterCoverPage = '' #本店の所在の場所、表紙
	NameOfContactPersonCoverPage = '' #事務連絡者氏名、表紙
	PlaceOfContactCoverPage = '' #連絡場所、表紙
	TelephoneNumberCoverPage = '' #電話番号、表紙
	PlaceForPublicInspectionCoverPageTextBlock = '' #縦覧に供する場所、表紙 [テキストブロック]
	NotesCoverPageTextBlock = '' #脚注、表紙 [テキストブロック]
	StatusOfFundManagementHeading = '' #ファンドの運用状況 [目次項目]
	StatusOfFundManagementTextBlock = '' #ファンドの運用状況 [テキストブロック]
	StatusOfInvestmentHeading = '' #投資状況 [目次項目]
	StatusOfInvestmentTextBlock = '' #投資状況 [テキストブロック]
	ActualPerformanceHeading = '' #運用実績 [目次項目]
	ChangesInNetAssetsHeading = '' #純資産の推移 [目次項目]
	ChangesInNetAssetsTextBlock = '' #純資産の推移 [テキストブロック]
	HistoricalRecordsOfProfitDistributionHeading = '' #分配の推移 [目次項目]
	HistoricalRecordsOfProfitDistributionTextBlock = '' #分配の推移 [テキストブロック]
	HistoricalRecordsOfReturnRatioHeading = '' #収益率の推移 [目次項目]
	HistoricalRecordsOfReturnRatioTextBlock = '' #収益率の推移 [テキストブロック]
	HistoricalRecordsOfInceptionsAndCancellationsHeading = '' #設定及び解約の実績 [目次項目]
	HistoricalRecordsOfInceptionsAndCancellationsTextBlock = '' #設定及び解約の実績 [テキストブロック]
	SupplementaryReferenceInformationAboutMotherFundStatusOfInvestmentManagementHeading = '' #（参考）マザーファンド、運用状況 [目次項目]
	SupplementaryReferenceInformationAboutMotherFundStatusOfInvestmentManagementTextBlock = '' #（参考）マザーファンド、運用状況 [テキストブロック]
	FinancialInformationOfFundHeading = '' #ファンドの経理状況 [目次項目]
	FinancialInformationOfFundTextBlock = '' #ファンドの経理状況 [テキストブロック]
	SemiAnnualBalanceSheetHeading = '' #中間貸借対照表 [目次項目]
	SemiAnnualBalanceSheetTextBlock = '' #中間貸借対照表 [テキストブロック]
	SemiAnnualStatementOfIncomeAndRetainedEarningsHeading = '' #中間損益及び剰余金計算書 [目次項目]
	SemiAnnualStatementOfIncomeAndRetainedEarningsTextBlock = '' #中間損益及び剰余金計算書 [テキストブロック]
	NotesToSemiAnnualFinancialStatementsHeading = '' #中間注記表 [目次項目]
	NotesToSemiAnnualFinancialStatementsTextBlock = '' #中間注記表 [テキストブロック]
	OverviewOfInvestmentTrustManagementCompanyEtcHeading = '' #委託会社等の概況 [目次項目]
	OverviewOfInvestmentTrustManagementCompanyEtcTextBlock = '' #委託会社等の概況 [テキストブロック]
	AmountOfStatedCapitalOverviewOfInvestmentTrustManagementCompanyEtcHeading = '' #資本金の額、委託会社等の概況 [目次項目]
	AmountOfStatedCapitalOverviewOfInvestmentTrustManagementCompanyEtcTextBlock = '' #資本金の額、委託会社等の概況 [テキストブロック]
	DescriptionOfBusinessAndSummaryOfOperationOverviewOfInvestmentTrustManagementCompanyEtcHeading = '' #事業の内容及び営業の状況、委託会社等の概況 [目次項目]
	DescriptionOfBusinessAndSummaryOfOperationOverviewOfInvestmentTrustManagementCompanyEtcTextBlock = '' #事業の内容及び営業の状況、委託会社等の概況 [テキストブロック]
	OtherInformationOverviewOfInvestmentTrustManagementCompanyEtcHeading = '' #その他、委託会社等の概況 [目次項目]
	OtherInformationOverviewOfInvestmentTrustManagementCompanyEtcTextBlock = '' #その他、委託会社等の概況 [テキストブロック]
	FinancialInformationOfInvestmentTrustManagementCompanyEtcHeading = '' #委託会社等の経理状況 [目次項目]
	FinancialInformationOfInvestmentTrustManagementCompanyEtcTextBlock = '' #委託会社等の経理状況 [テキストブロック]
	BalanceSheetFinancialInformationOfInvestmentTrustManagementCompanyEtcHeading = '' #貸借対照表、委託会社等の経理状況 [目次項目]
	BalanceSheetFinancialInformationOfInvestmentTrustManagementCompanyEtcTextBlock = '' #貸借対照表、委託会社等の経理状況 [テキストブロック]
	StatementOfIncomeFinancialInformationOfInvestmentTrustManagementCompanyEtcHeading = '' #損益計算書、委託会社等の経理状況 [目次項目]
	StatementOfIncomeFinancialInformationOfInvestmentTrustManagementCompanyEtcTextBlock = '' #損益計算書、委託会社等の経理状況 [テキストブロック]
	StatementOfChangesInEquityFinancialInformationOfInvestmentTrustManagementCompanyEtcHeading = '' #株主資本等変動計算書、委託会社等の経理状況 [目次項目]
	StatementOfChangesInEquityFinancialInformationOfInvestmentTrustManagementCompanyEtcTextBlock = '' #株主資本等変動計算書、委託会社等の経理状況 [テキストブロック]
	NotesFinancialInformationOfInvestmentTrustManagementCompanyEtcHeading = '' #注記事項、委託会社等の経理状況 [目次項目]
	NotesFinancialInformationOfInvestmentTrustManagementCompanyEtcTextBlock = '' #注記事項、委託会社等の経理状況 [テキストブロック]
	IndependentAuditorsReportHeading = '' #独立監査人の報告書 [目次項目]
	IndependentAuditorsReportFundTextBlock = '' #独立監査人の報告書、ファンド [テキストブロック]
	IndependentAuditorsReportInvestmentTrustManagementCompanyTextBlock = '' #独立監査人の報告書、委託会社 [テキストブロック]
	IndependentAuditorsReportInvestmentTrustManagementCompanySemiAnnualPeriodOfNextFiscalYearTextBlock = '' #独立監査人の報告書、委託会社、次の中間期 [テキストブロック]

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
			elif fact.concept.qname.localName == 'CabinetOfficeOrdinanceOnDisclosureOfInformationEtcOnSpecifiedSecuritiesFormNo10SemiannualSecuritiesReportHeading': #特定有価証券の内容等の開示に関する内閣府令 第十号様式 半期報告書 [目次項目]
				self.CabinetOfficeOrdinanceOnDisclosureOfInformationEtcOnSpecifiedSecuritiesFormNo10SemiannualSecuritiesReportHeading = fact.value

			elif fact.concept.qname.localName == 'CoverPageHeading': #表紙 [目次項目]
				self.CoverPageHeading = fact.value

			elif fact.concept.qname.localName == 'CoverPageHeading': #表紙 [目次項目]
				self.CoverPageHeading = fact.value

			elif fact.concept.qname.localName == 'DocumentTitleCoverPage': #提出書類、表紙
				self.DocumentTitleCoverPage = fact.value

			elif fact.concept.qname.localName == 'PlaceOfFilingCoverPage': #提出先、表紙
				self.PlaceOfFilingCoverPage = fact.value

			elif fact.concept.qname.localName == 'FilingDateCoverPage': #提出日、表紙
				self.FilingDateCoverPage = fact.value

			elif fact.concept.qname.localName == 'AccountingPeriodCoverPage': #計算期間、表紙
				self.AccountingPeriodCoverPage = fact.value

			elif fact.concept.qname.localName == 'FundNameCoverPage': #ファンド名、表紙
				self.FundNameCoverPage = fact.value

			elif fact.concept.qname.localName == 'IssuerNameCoverPage': #発行者名、表紙
				self.IssuerNameCoverPage = fact.value

			elif fact.concept.qname.localName == 'TitleAndNameOfRepresentativeCoverPage': #代表者の役職氏名、表紙
				self.TitleAndNameOfRepresentativeCoverPage = fact.value

			elif fact.concept.qname.localName == 'AddressOfRegisteredHeadquarterCoverPage': #本店の所在の場所、表紙
				self.AddressOfRegisteredHeadquarterCoverPage = fact.value

			elif fact.concept.qname.localName == 'NameOfContactPersonCoverPage': #事務連絡者氏名、表紙
				self.NameOfContactPersonCoverPage = fact.value

			elif fact.concept.qname.localName == 'PlaceOfContactCoverPage': #連絡場所、表紙
				self.PlaceOfContactCoverPage = fact.value

			elif fact.concept.qname.localName == 'TelephoneNumberCoverPage': #電話番号、表紙
				self.TelephoneNumberCoverPage = fact.value

			elif fact.concept.qname.localName == 'PlaceForPublicInspectionCoverPageTextBlock': #縦覧に供する場所、表紙 [テキストブロック]
				self.PlaceForPublicInspectionCoverPageTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesCoverPageTextBlock': #脚注、表紙 [テキストブロック]
				self.NotesCoverPageTextBlock = fact.value

			elif fact.concept.qname.localName == 'StatusOfFundManagementHeading': #ファンドの運用状況 [目次項目]
				self.StatusOfFundManagementHeading = fact.value

			elif fact.concept.qname.localName == 'StatusOfFundManagementTextBlock': #ファンドの運用状況 [テキストブロック]
				self.StatusOfFundManagementTextBlock = fact.value

			elif fact.concept.qname.localName == 'StatusOfInvestmentHeading': #投資状況 [目次項目]
				self.StatusOfInvestmentHeading = fact.value

			elif fact.concept.qname.localName == 'StatusOfInvestmentTextBlock': #投資状況 [テキストブロック]
				self.StatusOfInvestmentTextBlock = fact.value

			elif fact.concept.qname.localName == 'ActualPerformanceHeading': #運用実績 [目次項目]
				self.ActualPerformanceHeading = fact.value

			elif fact.concept.qname.localName == 'ChangesInNetAssetsHeading': #純資産の推移 [目次項目]
				self.ChangesInNetAssetsHeading = fact.value

			elif fact.concept.qname.localName == 'ChangesInNetAssetsTextBlock': #純資産の推移 [テキストブロック]
				self.ChangesInNetAssetsTextBlock = fact.value

			elif fact.concept.qname.localName == 'HistoricalRecordsOfProfitDistributionHeading': #分配の推移 [目次項目]
				self.HistoricalRecordsOfProfitDistributionHeading = fact.value

			elif fact.concept.qname.localName == 'HistoricalRecordsOfProfitDistributionTextBlock': #分配の推移 [テキストブロック]
				self.HistoricalRecordsOfProfitDistributionTextBlock = fact.value

			elif fact.concept.qname.localName == 'HistoricalRecordsOfReturnRatioHeading': #収益率の推移 [目次項目]
				self.HistoricalRecordsOfReturnRatioHeading = fact.value

			elif fact.concept.qname.localName == 'HistoricalRecordsOfReturnRatioTextBlock': #収益率の推移 [テキストブロック]
				self.HistoricalRecordsOfReturnRatioTextBlock = fact.value

			elif fact.concept.qname.localName == 'HistoricalRecordsOfInceptionsAndCancellationsHeading': #設定及び解約の実績 [目次項目]
				self.HistoricalRecordsOfInceptionsAndCancellationsHeading = fact.value

			elif fact.concept.qname.localName == 'HistoricalRecordsOfInceptionsAndCancellationsTextBlock': #設定及び解約の実績 [テキストブロック]
				self.HistoricalRecordsOfInceptionsAndCancellationsTextBlock = fact.value

			elif fact.concept.qname.localName == 'SupplementaryReferenceInformationAboutMotherFundStatusOfInvestmentManagementHeading': #（参考）マザーファンド、運用状況 [目次項目]
				self.SupplementaryReferenceInformationAboutMotherFundStatusOfInvestmentManagementHeading = fact.value

			elif fact.concept.qname.localName == 'SupplementaryReferenceInformationAboutMotherFundStatusOfInvestmentManagementTextBlock': #（参考）マザーファンド、運用状況 [テキストブロック]
				self.SupplementaryReferenceInformationAboutMotherFundStatusOfInvestmentManagementTextBlock = fact.value

			elif fact.concept.qname.localName == 'FinancialInformationOfFundHeading': #ファンドの経理状況 [目次項目]
				self.FinancialInformationOfFundHeading = fact.value

			elif fact.concept.qname.localName == 'FinancialInformationOfFundTextBlock': #ファンドの経理状況 [テキストブロック]
				self.FinancialInformationOfFundTextBlock = fact.value

			elif fact.concept.qname.localName == 'SemiAnnualBalanceSheetHeading': #中間貸借対照表 [目次項目]
				self.SemiAnnualBalanceSheetHeading = fact.value

			elif fact.concept.qname.localName == 'SemiAnnualBalanceSheetTextBlock': #中間貸借対照表 [テキストブロック]
				self.SemiAnnualBalanceSheetTextBlock = fact.value

			elif fact.concept.qname.localName == 'SemiAnnualStatementOfIncomeAndRetainedEarningsHeading': #中間損益及び剰余金計算書 [目次項目]
				self.SemiAnnualStatementOfIncomeAndRetainedEarningsHeading = fact.value

			elif fact.concept.qname.localName == 'SemiAnnualStatementOfIncomeAndRetainedEarningsTextBlock': #中間損益及び剰余金計算書 [テキストブロック]
				self.SemiAnnualStatementOfIncomeAndRetainedEarningsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesToSemiAnnualFinancialStatementsHeading': #中間注記表 [目次項目]
				self.NotesToSemiAnnualFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesToSemiAnnualFinancialStatementsTextBlock': #中間注記表 [テキストブロック]
				self.NotesToSemiAnnualFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'OverviewOfInvestmentTrustManagementCompanyEtcHeading': #委託会社等の概況 [目次項目]
				self.OverviewOfInvestmentTrustManagementCompanyEtcHeading = fact.value

			elif fact.concept.qname.localName == 'OverviewOfInvestmentTrustManagementCompanyEtcTextBlock': #委託会社等の概況 [テキストブロック]
				self.OverviewOfInvestmentTrustManagementCompanyEtcTextBlock = fact.value

			elif fact.concept.qname.localName == 'AmountOfStatedCapitalOverviewOfInvestmentTrustManagementCompanyEtcHeading': #資本金の額、委託会社等の概況 [目次項目]
				self.AmountOfStatedCapitalOverviewOfInvestmentTrustManagementCompanyEtcHeading = fact.value

			elif fact.concept.qname.localName == 'AmountOfStatedCapitalOverviewOfInvestmentTrustManagementCompanyEtcTextBlock': #資本金の額、委託会社等の概況 [テキストブロック]
				self.AmountOfStatedCapitalOverviewOfInvestmentTrustManagementCompanyEtcTextBlock = fact.value

			elif fact.concept.qname.localName == 'DescriptionOfBusinessAndSummaryOfOperationOverviewOfInvestmentTrustManagementCompanyEtcHeading': #事業の内容及び営業の状況、委託会社等の概況 [目次項目]
				self.DescriptionOfBusinessAndSummaryOfOperationOverviewOfInvestmentTrustManagementCompanyEtcHeading = fact.value

			elif fact.concept.qname.localName == 'DescriptionOfBusinessAndSummaryOfOperationOverviewOfInvestmentTrustManagementCompanyEtcTextBlock': #事業の内容及び営業の状況、委託会社等の概況 [テキストブロック]
				self.DescriptionOfBusinessAndSummaryOfOperationOverviewOfInvestmentTrustManagementCompanyEtcTextBlock = fact.value

			elif fact.concept.qname.localName == 'OtherInformationOverviewOfInvestmentTrustManagementCompanyEtcHeading': #その他、委託会社等の概況 [目次項目]
				self.OtherInformationOverviewOfInvestmentTrustManagementCompanyEtcHeading = fact.value

			elif fact.concept.qname.localName == 'OtherInformationOverviewOfInvestmentTrustManagementCompanyEtcTextBlock': #その他、委託会社等の概況 [テキストブロック]
				self.OtherInformationOverviewOfInvestmentTrustManagementCompanyEtcTextBlock = fact.value

			elif fact.concept.qname.localName == 'FinancialInformationOfInvestmentTrustManagementCompanyEtcHeading': #委託会社等の経理状況 [目次項目]
				self.FinancialInformationOfInvestmentTrustManagementCompanyEtcHeading = fact.value

			elif fact.concept.qname.localName == 'FinancialInformationOfInvestmentTrustManagementCompanyEtcTextBlock': #委託会社等の経理状況 [テキストブロック]
				self.FinancialInformationOfInvestmentTrustManagementCompanyEtcTextBlock = fact.value

			elif fact.concept.qname.localName == 'BalanceSheetFinancialInformationOfInvestmentTrustManagementCompanyEtcHeading': #貸借対照表、委託会社等の経理状況 [目次項目]
				self.BalanceSheetFinancialInformationOfInvestmentTrustManagementCompanyEtcHeading = fact.value

			elif fact.concept.qname.localName == 'BalanceSheetFinancialInformationOfInvestmentTrustManagementCompanyEtcTextBlock': #貸借対照表、委託会社等の経理状況 [テキストブロック]
				self.BalanceSheetFinancialInformationOfInvestmentTrustManagementCompanyEtcTextBlock = fact.value

			elif fact.concept.qname.localName == 'StatementOfIncomeFinancialInformationOfInvestmentTrustManagementCompanyEtcHeading': #損益計算書、委託会社等の経理状況 [目次項目]
				self.StatementOfIncomeFinancialInformationOfInvestmentTrustManagementCompanyEtcHeading = fact.value

			elif fact.concept.qname.localName == 'StatementOfIncomeFinancialInformationOfInvestmentTrustManagementCompanyEtcTextBlock': #損益計算書、委託会社等の経理状況 [テキストブロック]
				self.StatementOfIncomeFinancialInformationOfInvestmentTrustManagementCompanyEtcTextBlock = fact.value

			elif fact.concept.qname.localName == 'StatementOfChangesInEquityFinancialInformationOfInvestmentTrustManagementCompanyEtcHeading': #株主資本等変動計算書、委託会社等の経理状況 [目次項目]
				self.StatementOfChangesInEquityFinancialInformationOfInvestmentTrustManagementCompanyEtcHeading = fact.value

			elif fact.concept.qname.localName == 'StatementOfChangesInEquityFinancialInformationOfInvestmentTrustManagementCompanyEtcTextBlock': #株主資本等変動計算書、委託会社等の経理状況 [テキストブロック]
				self.StatementOfChangesInEquityFinancialInformationOfInvestmentTrustManagementCompanyEtcTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesFinancialInformationOfInvestmentTrustManagementCompanyEtcHeading': #注記事項、委託会社等の経理状況 [目次項目]
				self.NotesFinancialInformationOfInvestmentTrustManagementCompanyEtcHeading = fact.value

			elif fact.concept.qname.localName == 'NotesFinancialInformationOfInvestmentTrustManagementCompanyEtcTextBlock': #注記事項、委託会社等の経理状況 [テキストブロック]
				self.NotesFinancialInformationOfInvestmentTrustManagementCompanyEtcTextBlock = fact.value

			elif fact.concept.qname.localName == 'IndependentAuditorsReportHeading': #独立監査人の報告書 [目次項目]
				self.IndependentAuditorsReportHeading = fact.value

			elif fact.concept.qname.localName == 'IndependentAuditorsReportFundTextBlock': #独立監査人の報告書、ファンド [テキストブロック]
				self.IndependentAuditorsReportFundTextBlock = fact.value

			elif fact.concept.qname.localName == 'IndependentAuditorsReportInvestmentTrustManagementCompanyTextBlock': #独立監査人の報告書、委託会社 [テキストブロック]
				self.IndependentAuditorsReportInvestmentTrustManagementCompanyTextBlock = fact.value

			elif fact.concept.qname.localName == 'IndependentAuditorsReportInvestmentTrustManagementCompanySemiAnnualPeriodOfNextFiscalYearTextBlock': #独立監査人の報告書、委託会社、次の中間期 [テキストブロック]
				self.IndependentAuditorsReportInvestmentTrustManagementCompanySemiAnnualPeriodOfNextFiscalYearTextBlock = fact.value


	def getCabinetOfficeOrdinanceOnDisclosureOfInformationEtcOnSpecifiedSecuritiesFormNo10SemiannualSecuritiesReportHeading(self): #特定有価証券の内容等の開示に関する内閣府令 第十号様式 半期報告書 [目次項目]
		return self.CabinetOfficeOrdinanceOnDisclosureOfInformationEtcOnSpecifiedSecuritiesFormNo10SemiannualSecuritiesReportHeading

	def getCoverPageHeading(self): #表紙 [目次項目]
		return self.CoverPageHeading

	def getCoverPageHeading(self): #表紙 [目次項目]
		return self.CoverPageHeading

	def getDocumentTitleCoverPage(self): #提出書類、表紙
		return self.DocumentTitleCoverPage

	def getPlaceOfFilingCoverPage(self): #提出先、表紙
		return self.PlaceOfFilingCoverPage

	def getFilingDateCoverPage(self): #提出日、表紙
		return self.FilingDateCoverPage

	def getAccountingPeriodCoverPage(self): #計算期間、表紙
		return self.AccountingPeriodCoverPage

	def getFundNameCoverPage(self): #ファンド名、表紙
		return self.FundNameCoverPage

	def getIssuerNameCoverPage(self): #発行者名、表紙
		return self.IssuerNameCoverPage

	def getTitleAndNameOfRepresentativeCoverPage(self): #代表者の役職氏名、表紙
		return self.TitleAndNameOfRepresentativeCoverPage

	def getAddressOfRegisteredHeadquarterCoverPage(self): #本店の所在の場所、表紙
		return self.AddressOfRegisteredHeadquarterCoverPage

	def getNameOfContactPersonCoverPage(self): #事務連絡者氏名、表紙
		return self.NameOfContactPersonCoverPage

	def getPlaceOfContactCoverPage(self): #連絡場所、表紙
		return self.PlaceOfContactCoverPage

	def getTelephoneNumberCoverPage(self): #電話番号、表紙
		return self.TelephoneNumberCoverPage

	def getPlaceForPublicInspectionCoverPageTextBlock(self): #縦覧に供する場所、表紙 [テキストブロック]
		return self.PlaceForPublicInspectionCoverPageTextBlock

	def getNotesCoverPageTextBlock(self): #脚注、表紙 [テキストブロック]
		return self.NotesCoverPageTextBlock

	def getStatusOfFundManagementHeading(self): #ファンドの運用状況 [目次項目]
		return self.StatusOfFundManagementHeading

	def getStatusOfFundManagementTextBlock(self): #ファンドの運用状況 [テキストブロック]
		return self.StatusOfFundManagementTextBlock

	def getStatusOfInvestmentHeading(self): #投資状況 [目次項目]
		return self.StatusOfInvestmentHeading

	def getStatusOfInvestmentTextBlock(self): #投資状況 [テキストブロック]
		return self.StatusOfInvestmentTextBlock

	def getActualPerformanceHeading(self): #運用実績 [目次項目]
		return self.ActualPerformanceHeading

	def getChangesInNetAssetsHeading(self): #純資産の推移 [目次項目]
		return self.ChangesInNetAssetsHeading

	def getChangesInNetAssetsTextBlock(self): #純資産の推移 [テキストブロック]
		return self.ChangesInNetAssetsTextBlock

	def getHistoricalRecordsOfProfitDistributionHeading(self): #分配の推移 [目次項目]
		return self.HistoricalRecordsOfProfitDistributionHeading

	def getHistoricalRecordsOfProfitDistributionTextBlock(self): #分配の推移 [テキストブロック]
		return self.HistoricalRecordsOfProfitDistributionTextBlock

	def getHistoricalRecordsOfReturnRatioHeading(self): #収益率の推移 [目次項目]
		return self.HistoricalRecordsOfReturnRatioHeading

	def getHistoricalRecordsOfReturnRatioTextBlock(self): #収益率の推移 [テキストブロック]
		return self.HistoricalRecordsOfReturnRatioTextBlock

	def getHistoricalRecordsOfInceptionsAndCancellationsHeading(self): #設定及び解約の実績 [目次項目]
		return self.HistoricalRecordsOfInceptionsAndCancellationsHeading

	def getHistoricalRecordsOfInceptionsAndCancellationsTextBlock(self): #設定及び解約の実績 [テキストブロック]
		return self.HistoricalRecordsOfInceptionsAndCancellationsTextBlock

	def getSupplementaryReferenceInformationAboutMotherFundStatusOfInvestmentManagementHeading(self): #（参考）マザーファンド、運用状況 [目次項目]
		return self.SupplementaryReferenceInformationAboutMotherFundStatusOfInvestmentManagementHeading

	def getSupplementaryReferenceInformationAboutMotherFundStatusOfInvestmentManagementTextBlock(self): #（参考）マザーファンド、運用状況 [テキストブロック]
		return self.SupplementaryReferenceInformationAboutMotherFundStatusOfInvestmentManagementTextBlock

	def getFinancialInformationOfFundHeading(self): #ファンドの経理状況 [目次項目]
		return self.FinancialInformationOfFundHeading

	def getFinancialInformationOfFundTextBlock(self): #ファンドの経理状況 [テキストブロック]
		return self.FinancialInformationOfFundTextBlock

	def getSemiAnnualBalanceSheetHeading(self): #中間貸借対照表 [目次項目]
		return self.SemiAnnualBalanceSheetHeading

	def getSemiAnnualBalanceSheetTextBlock(self): #中間貸借対照表 [テキストブロック]
		return self.SemiAnnualBalanceSheetTextBlock

	def getSemiAnnualStatementOfIncomeAndRetainedEarningsHeading(self): #中間損益及び剰余金計算書 [目次項目]
		return self.SemiAnnualStatementOfIncomeAndRetainedEarningsHeading

	def getSemiAnnualStatementOfIncomeAndRetainedEarningsTextBlock(self): #中間損益及び剰余金計算書 [テキストブロック]
		return self.SemiAnnualStatementOfIncomeAndRetainedEarningsTextBlock

	def getNotesToSemiAnnualFinancialStatementsHeading(self): #中間注記表 [目次項目]
		return self.NotesToSemiAnnualFinancialStatementsHeading

	def getNotesToSemiAnnualFinancialStatementsTextBlock(self): #中間注記表 [テキストブロック]
		return self.NotesToSemiAnnualFinancialStatementsTextBlock

	def getOverviewOfInvestmentTrustManagementCompanyEtcHeading(self): #委託会社等の概況 [目次項目]
		return self.OverviewOfInvestmentTrustManagementCompanyEtcHeading

	def getOverviewOfInvestmentTrustManagementCompanyEtcTextBlock(self): #委託会社等の概況 [テキストブロック]
		return self.OverviewOfInvestmentTrustManagementCompanyEtcTextBlock

	def getAmountOfStatedCapitalOverviewOfInvestmentTrustManagementCompanyEtcHeading(self): #資本金の額、委託会社等の概況 [目次項目]
		return self.AmountOfStatedCapitalOverviewOfInvestmentTrustManagementCompanyEtcHeading

	def getAmountOfStatedCapitalOverviewOfInvestmentTrustManagementCompanyEtcTextBlock(self): #資本金の額、委託会社等の概況 [テキストブロック]
		return self.AmountOfStatedCapitalOverviewOfInvestmentTrustManagementCompanyEtcTextBlock

	def getDescriptionOfBusinessAndSummaryOfOperationOverviewOfInvestmentTrustManagementCompanyEtcHeading(self): #事業の内容及び営業の状況、委託会社等の概況 [目次項目]
		return self.DescriptionOfBusinessAndSummaryOfOperationOverviewOfInvestmentTrustManagementCompanyEtcHeading

	def getDescriptionOfBusinessAndSummaryOfOperationOverviewOfInvestmentTrustManagementCompanyEtcTextBlock(self): #事業の内容及び営業の状況、委託会社等の概況 [テキストブロック]
		return self.DescriptionOfBusinessAndSummaryOfOperationOverviewOfInvestmentTrustManagementCompanyEtcTextBlock

	def getOtherInformationOverviewOfInvestmentTrustManagementCompanyEtcHeading(self): #その他、委託会社等の概況 [目次項目]
		return self.OtherInformationOverviewOfInvestmentTrustManagementCompanyEtcHeading

	def getOtherInformationOverviewOfInvestmentTrustManagementCompanyEtcTextBlock(self): #その他、委託会社等の概況 [テキストブロック]
		return self.OtherInformationOverviewOfInvestmentTrustManagementCompanyEtcTextBlock

	def getFinancialInformationOfInvestmentTrustManagementCompanyEtcHeading(self): #委託会社等の経理状況 [目次項目]
		return self.FinancialInformationOfInvestmentTrustManagementCompanyEtcHeading

	def getFinancialInformationOfInvestmentTrustManagementCompanyEtcTextBlock(self): #委託会社等の経理状況 [テキストブロック]
		return self.FinancialInformationOfInvestmentTrustManagementCompanyEtcTextBlock

	def getBalanceSheetFinancialInformationOfInvestmentTrustManagementCompanyEtcHeading(self): #貸借対照表、委託会社等の経理状況 [目次項目]
		return self.BalanceSheetFinancialInformationOfInvestmentTrustManagementCompanyEtcHeading

	def getBalanceSheetFinancialInformationOfInvestmentTrustManagementCompanyEtcTextBlock(self): #貸借対照表、委託会社等の経理状況 [テキストブロック]
		return self.BalanceSheetFinancialInformationOfInvestmentTrustManagementCompanyEtcTextBlock

	def getStatementOfIncomeFinancialInformationOfInvestmentTrustManagementCompanyEtcHeading(self): #損益計算書、委託会社等の経理状況 [目次項目]
		return self.StatementOfIncomeFinancialInformationOfInvestmentTrustManagementCompanyEtcHeading

	def getStatementOfIncomeFinancialInformationOfInvestmentTrustManagementCompanyEtcTextBlock(self): #損益計算書、委託会社等の経理状況 [テキストブロック]
		return self.StatementOfIncomeFinancialInformationOfInvestmentTrustManagementCompanyEtcTextBlock

	def getStatementOfChangesInEquityFinancialInformationOfInvestmentTrustManagementCompanyEtcHeading(self): #株主資本等変動計算書、委託会社等の経理状況 [目次項目]
		return self.StatementOfChangesInEquityFinancialInformationOfInvestmentTrustManagementCompanyEtcHeading

	def getStatementOfChangesInEquityFinancialInformationOfInvestmentTrustManagementCompanyEtcTextBlock(self): #株主資本等変動計算書、委託会社等の経理状況 [テキストブロック]
		return self.StatementOfChangesInEquityFinancialInformationOfInvestmentTrustManagementCompanyEtcTextBlock

	def getNotesFinancialInformationOfInvestmentTrustManagementCompanyEtcHeading(self): #注記事項、委託会社等の経理状況 [目次項目]
		return self.NotesFinancialInformationOfInvestmentTrustManagementCompanyEtcHeading

	def getNotesFinancialInformationOfInvestmentTrustManagementCompanyEtcTextBlock(self): #注記事項、委託会社等の経理状況 [テキストブロック]
		return self.NotesFinancialInformationOfInvestmentTrustManagementCompanyEtcTextBlock

	def getIndependentAuditorsReportHeading(self): #独立監査人の報告書 [目次項目]
		return self.IndependentAuditorsReportHeading

	def getIndependentAuditorsReportFundTextBlock(self): #独立監査人の報告書、ファンド [テキストブロック]
		return self.IndependentAuditorsReportFundTextBlock

	def getIndependentAuditorsReportInvestmentTrustManagementCompanyTextBlock(self): #独立監査人の報告書、委託会社 [テキストブロック]
		return self.IndependentAuditorsReportInvestmentTrustManagementCompanyTextBlock

	def getIndependentAuditorsReportInvestmentTrustManagementCompanySemiAnnualPeriodOfNextFiscalYearTextBlock(self): #独立監査人の報告書、委託会社、次の中間期 [テキストブロック]
		return self.IndependentAuditorsReportInvestmentTrustManagementCompanySemiAnnualPeriodOfNextFiscalYearTextBlock
