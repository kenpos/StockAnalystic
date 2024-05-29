from arelle import ModelManager
from arelle import Cntlr

class jpsps250300:#特定有価証券の内容等の開示に関する内閣府令 第二十五号の三様式 自己株券買付状況報告書
	CabinetOfficeOrdinanceOnDisclosureOfInformationEtcOnSpecifiedSecuritiesFormNo253ShareBuybackReportHeading = '' #特定有価証券の内容等の開示に関する内閣府令 第二十五号の三様式 自己株券買付状況報告書 [目次項目]
	CoverPageHeading = '' #表紙 [目次項目]
	CoverPageHeading = '' #表紙 [目次項目]
	DocumentTitleCoverPage = '' #提出書類、表紙
	ClauseOfStipulationCoverPage = '' #根拠条文、表紙
	PlaceOfFilingCoverPage = '' #提出先、表紙
	FilingDateCoverPage = '' #提出日、表紙
	ReportingPeriodCoverPage = '' #報告期間、表紙
	IssuerNameCoverPage = '' #発行者名、表紙
	TitleAndNameOfRepresentativeCoverPage = '' #代表者の役職氏名、表紙
	AddressOfRegisteredHeadquarterCoverPage = '' #本店の所在の場所、表紙
	NameOfContactPersonCoverPage = '' #事務連絡者氏名、表紙
	TelephoneNumberCoverPage = '' #電話番号、表紙
	PlaceForPublicInspectionCoverPageTextBlock = '' #縦覧に供する場所、表紙 [テキストブロック]
	AcquisitionsOfTreasurySharesHeading = '' #取得状況 [目次項目]
	AcquisitionsOfTreasurySharesTextBlock = '' #取得状況 [テキストブロック]
	DisposalsOfTreasurySharesHeading = '' #処理状況 [目次項目]
	DisposalsOfTreasurySharesTextBlock = '' #処理状況 [テキストブロック]
	HoldingOfTreasurySharesHeading = '' #保有状況 [目次項目]
	HoldingOfTreasurySharesTextBlock = '' #保有状況 [テキストブロック]

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
			elif fact.concept.qname.localName == 'CabinetOfficeOrdinanceOnDisclosureOfInformationEtcOnSpecifiedSecuritiesFormNo253ShareBuybackReportHeading': #特定有価証券の内容等の開示に関する内閣府令 第二十五号の三様式 自己株券買付状況報告書 [目次項目]
				self.CabinetOfficeOrdinanceOnDisclosureOfInformationEtcOnSpecifiedSecuritiesFormNo253ShareBuybackReportHeading = fact.value

			elif fact.concept.qname.localName == 'CoverPageHeading': #表紙 [目次項目]
				self.CoverPageHeading = fact.value

			elif fact.concept.qname.localName == 'CoverPageHeading': #表紙 [目次項目]
				self.CoverPageHeading = fact.value

			elif fact.concept.qname.localName == 'DocumentTitleCoverPage': #提出書類、表紙
				self.DocumentTitleCoverPage = fact.value

			elif fact.concept.qname.localName == 'ClauseOfStipulationCoverPage': #根拠条文、表紙
				self.ClauseOfStipulationCoverPage = fact.value

			elif fact.concept.qname.localName == 'PlaceOfFilingCoverPage': #提出先、表紙
				self.PlaceOfFilingCoverPage = fact.value

			elif fact.concept.qname.localName == 'FilingDateCoverPage': #提出日、表紙
				self.FilingDateCoverPage = fact.value

			elif fact.concept.qname.localName == 'ReportingPeriodCoverPage': #報告期間、表紙
				self.ReportingPeriodCoverPage = fact.value

			elif fact.concept.qname.localName == 'IssuerNameCoverPage': #発行者名、表紙
				self.IssuerNameCoverPage = fact.value

			elif fact.concept.qname.localName == 'TitleAndNameOfRepresentativeCoverPage': #代表者の役職氏名、表紙
				self.TitleAndNameOfRepresentativeCoverPage = fact.value

			elif fact.concept.qname.localName == 'AddressOfRegisteredHeadquarterCoverPage': #本店の所在の場所、表紙
				self.AddressOfRegisteredHeadquarterCoverPage = fact.value

			elif fact.concept.qname.localName == 'NameOfContactPersonCoverPage': #事務連絡者氏名、表紙
				self.NameOfContactPersonCoverPage = fact.value

			elif fact.concept.qname.localName == 'TelephoneNumberCoverPage': #電話番号、表紙
				self.TelephoneNumberCoverPage = fact.value

			elif fact.concept.qname.localName == 'PlaceForPublicInspectionCoverPageTextBlock': #縦覧に供する場所、表紙 [テキストブロック]
				self.PlaceForPublicInspectionCoverPageTextBlock = fact.value

			elif fact.concept.qname.localName == 'AcquisitionsOfTreasurySharesHeading': #取得状況 [目次項目]
				self.AcquisitionsOfTreasurySharesHeading = fact.value

			elif fact.concept.qname.localName == 'AcquisitionsOfTreasurySharesTextBlock': #取得状況 [テキストブロック]
				self.AcquisitionsOfTreasurySharesTextBlock = fact.value

			elif fact.concept.qname.localName == 'DisposalsOfTreasurySharesHeading': #処理状況 [目次項目]
				self.DisposalsOfTreasurySharesHeading = fact.value

			elif fact.concept.qname.localName == 'DisposalsOfTreasurySharesTextBlock': #処理状況 [テキストブロック]
				self.DisposalsOfTreasurySharesTextBlock = fact.value

			elif fact.concept.qname.localName == 'HoldingOfTreasurySharesHeading': #保有状況 [目次項目]
				self.HoldingOfTreasurySharesHeading = fact.value

			elif fact.concept.qname.localName == 'HoldingOfTreasurySharesTextBlock': #保有状況 [テキストブロック]
				self.HoldingOfTreasurySharesTextBlock = fact.value


	def getCabinetOfficeOrdinanceOnDisclosureOfInformationEtcOnSpecifiedSecuritiesFormNo253ShareBuybackReportHeading(self): #特定有価証券の内容等の開示に関する内閣府令 第二十五号の三様式 自己株券買付状況報告書 [目次項目]
		return self.CabinetOfficeOrdinanceOnDisclosureOfInformationEtcOnSpecifiedSecuritiesFormNo253ShareBuybackReportHeading

	def getCoverPageHeading(self): #表紙 [目次項目]
		return self.CoverPageHeading

	def getCoverPageHeading(self): #表紙 [目次項目]
		return self.CoverPageHeading

	def getDocumentTitleCoverPage(self): #提出書類、表紙
		return self.DocumentTitleCoverPage

	def getClauseOfStipulationCoverPage(self): #根拠条文、表紙
		return self.ClauseOfStipulationCoverPage

	def getPlaceOfFilingCoverPage(self): #提出先、表紙
		return self.PlaceOfFilingCoverPage

	def getFilingDateCoverPage(self): #提出日、表紙
		return self.FilingDateCoverPage

	def getReportingPeriodCoverPage(self): #報告期間、表紙
		return self.ReportingPeriodCoverPage

	def getIssuerNameCoverPage(self): #発行者名、表紙
		return self.IssuerNameCoverPage

	def getTitleAndNameOfRepresentativeCoverPage(self): #代表者の役職氏名、表紙
		return self.TitleAndNameOfRepresentativeCoverPage

	def getAddressOfRegisteredHeadquarterCoverPage(self): #本店の所在の場所、表紙
		return self.AddressOfRegisteredHeadquarterCoverPage

	def getNameOfContactPersonCoverPage(self): #事務連絡者氏名、表紙
		return self.NameOfContactPersonCoverPage

	def getTelephoneNumberCoverPage(self): #電話番号、表紙
		return self.TelephoneNumberCoverPage

	def getPlaceForPublicInspectionCoverPageTextBlock(self): #縦覧に供する場所、表紙 [テキストブロック]
		return self.PlaceForPublicInspectionCoverPageTextBlock

	def getAcquisitionsOfTreasurySharesHeading(self): #取得状況 [目次項目]
		return self.AcquisitionsOfTreasurySharesHeading

	def getAcquisitionsOfTreasurySharesTextBlock(self): #取得状況 [テキストブロック]
		return self.AcquisitionsOfTreasurySharesTextBlock

	def getDisposalsOfTreasurySharesHeading(self): #処理状況 [目次項目]
		return self.DisposalsOfTreasurySharesHeading

	def getDisposalsOfTreasurySharesTextBlock(self): #処理状況 [テキストブロック]
		return self.DisposalsOfTreasurySharesTextBlock

	def getHoldingOfTreasurySharesHeading(self): #保有状況 [目次項目]
		return self.HoldingOfTreasurySharesHeading

	def getHoldingOfTreasurySharesTextBlock(self): #保有状況 [テキストブロック]
		return self.HoldingOfTreasurySharesTextBlock
