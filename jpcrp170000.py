from arelle import ModelManager
from arelle import Cntlr

class jpcrp170000:#企業内容等の開示に関する内閣府令 第十七号様式 自己株券買付状況報告書
	CabinetOfficeOrdinanceOnDisclosureOfCorporateInformationEtcFormNo17ShareBuybackReportHeading = '' #企業内容等の開示に関する内閣府令 第十七号様式 自己株券買付状況報告書 [目次項目]
	CoverPageHeading = '' #表紙 [目次項目]
	CoverPageHeading = '' #表紙 [目次項目]
	DocumentTitleCoverPage = '' #提出書類、表紙
	ClauseOfStipulationCoverPage = '' #根拠条文、表紙
	PlaceOfFilingCoverPage = '' #提出先、表紙
	FilingDateCoverPage = '' #提出日、表紙
	ReportingPeriodCoverPage = '' #報告期間、表紙
	CompanyNameCoverPage = '' #会社名、表紙
	CompanyNameInEnglishCoverPage = '' #英訳名、表紙
	TitleAndNameOfRepresentativeCoverPage = '' #代表者の役職氏名、表紙
	AddressOfRegisteredHeadquarterCoverPage = '' #本店の所在の場所、表紙
	TelephoneNumberAddressOfRegisteredHeadquarterCoverPage = '' #電話番号、本店の所在の場所、表紙
	NameOfContactPersonCoverPage = '' #事務連絡者氏名、表紙
	NearestPlaceOfContactCoverPage = '' #最寄りの連絡場所、表紙
	TelephoneNumberNearestPlaceOfContactCoverPage = '' #電話番号、最寄りの連絡場所、表紙
	NameOfContactPersonNearestPlaceOfContactCoverPage = '' #事務連絡者氏名、最寄りの連絡場所、表紙
	PlaceForPublicInspectionCoverPageTextBlock = '' #縦覧に供する場所、表紙 [テキストブロック]
	ClassesOfSharesHeading = '' #株式の種類 [目次項目]
	ClassesOfSharesTextBlock = '' #株式の種類 [テキストブロック]
	AcquisitionsOfTreasurySharesHeading = '' #取得状況 [目次項目]
	AcquisitionsByResolutionOfShareholdersMeetingHeading = '' #株主総会決議による取得の状況 [目次項目]
	AcquisitionsByResolutionOfShareholdersMeetingTextBlock = '' #株主総会決議による取得の状況 [テキストブロック]
	AcquisitionsByResolutionOfBoardOfDirectorsMeetingHeading = '' #取締役会決議による取得の状況 [目次項目]
	AcquisitionsByResolutionOfBoardOfDirectorsMeetingTextBlock = '' #取締役会決議による取得の状況 [テキストブロック]
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
			elif fact.concept.qname.localName == 'CabinetOfficeOrdinanceOnDisclosureOfCorporateInformationEtcFormNo17ShareBuybackReportHeading': #企業内容等の開示に関する内閣府令 第十七号様式 自己株券買付状況報告書 [目次項目]
				self.CabinetOfficeOrdinanceOnDisclosureOfCorporateInformationEtcFormNo17ShareBuybackReportHeading = fact.value

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

			elif fact.concept.qname.localName == 'CompanyNameCoverPage': #会社名、表紙
				self.CompanyNameCoverPage = fact.value

			elif fact.concept.qname.localName == 'CompanyNameInEnglishCoverPage': #英訳名、表紙
				self.CompanyNameInEnglishCoverPage = fact.value

			elif fact.concept.qname.localName == 'TitleAndNameOfRepresentativeCoverPage': #代表者の役職氏名、表紙
				self.TitleAndNameOfRepresentativeCoverPage = fact.value

			elif fact.concept.qname.localName == 'AddressOfRegisteredHeadquarterCoverPage': #本店の所在の場所、表紙
				self.AddressOfRegisteredHeadquarterCoverPage = fact.value

			elif fact.concept.qname.localName == 'TelephoneNumberAddressOfRegisteredHeadquarterCoverPage': #電話番号、本店の所在の場所、表紙
				self.TelephoneNumberAddressOfRegisteredHeadquarterCoverPage = fact.value

			elif fact.concept.qname.localName == 'NameOfContactPersonCoverPage': #事務連絡者氏名、表紙
				self.NameOfContactPersonCoverPage = fact.value

			elif fact.concept.qname.localName == 'NearestPlaceOfContactCoverPage': #最寄りの連絡場所、表紙
				self.NearestPlaceOfContactCoverPage = fact.value

			elif fact.concept.qname.localName == 'TelephoneNumberNearestPlaceOfContactCoverPage': #電話番号、最寄りの連絡場所、表紙
				self.TelephoneNumberNearestPlaceOfContactCoverPage = fact.value

			elif fact.concept.qname.localName == 'NameOfContactPersonNearestPlaceOfContactCoverPage': #事務連絡者氏名、最寄りの連絡場所、表紙
				self.NameOfContactPersonNearestPlaceOfContactCoverPage = fact.value

			elif fact.concept.qname.localName == 'PlaceForPublicInspectionCoverPageTextBlock': #縦覧に供する場所、表紙 [テキストブロック]
				self.PlaceForPublicInspectionCoverPageTextBlock = fact.value

			elif fact.concept.qname.localName == 'ClassesOfSharesHeading': #株式の種類 [目次項目]
				self.ClassesOfSharesHeading = fact.value

			elif fact.concept.qname.localName == 'ClassesOfSharesTextBlock': #株式の種類 [テキストブロック]
				self.ClassesOfSharesTextBlock = fact.value

			elif fact.concept.qname.localName == 'AcquisitionsOfTreasurySharesHeading': #取得状況 [目次項目]
				self.AcquisitionsOfTreasurySharesHeading = fact.value

			elif fact.concept.qname.localName == 'AcquisitionsByResolutionOfShareholdersMeetingHeading': #株主総会決議による取得の状況 [目次項目]
				self.AcquisitionsByResolutionOfShareholdersMeetingHeading = fact.value

			elif fact.concept.qname.localName == 'AcquisitionsByResolutionOfShareholdersMeetingTextBlock': #株主総会決議による取得の状況 [テキストブロック]
				self.AcquisitionsByResolutionOfShareholdersMeetingTextBlock = fact.value

			elif fact.concept.qname.localName == 'AcquisitionsByResolutionOfBoardOfDirectorsMeetingHeading': #取締役会決議による取得の状況 [目次項目]
				self.AcquisitionsByResolutionOfBoardOfDirectorsMeetingHeading = fact.value

			elif fact.concept.qname.localName == 'AcquisitionsByResolutionOfBoardOfDirectorsMeetingTextBlock': #取締役会決議による取得の状況 [テキストブロック]
				self.AcquisitionsByResolutionOfBoardOfDirectorsMeetingTextBlock = fact.value

			elif fact.concept.qname.localName == 'DisposalsOfTreasurySharesHeading': #処理状況 [目次項目]
				self.DisposalsOfTreasurySharesHeading = fact.value

			elif fact.concept.qname.localName == 'DisposalsOfTreasurySharesTextBlock': #処理状況 [テキストブロック]
				self.DisposalsOfTreasurySharesTextBlock = fact.value

			elif fact.concept.qname.localName == 'HoldingOfTreasurySharesHeading': #保有状況 [目次項目]
				self.HoldingOfTreasurySharesHeading = fact.value

			elif fact.concept.qname.localName == 'HoldingOfTreasurySharesTextBlock': #保有状況 [テキストブロック]
				self.HoldingOfTreasurySharesTextBlock = fact.value


	def getCabinetOfficeOrdinanceOnDisclosureOfCorporateInformationEtcFormNo17ShareBuybackReportHeading(self): #企業内容等の開示に関する内閣府令 第十七号様式 自己株券買付状況報告書 [目次項目]
		return self.CabinetOfficeOrdinanceOnDisclosureOfCorporateInformationEtcFormNo17ShareBuybackReportHeading

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

	def getCompanyNameCoverPage(self): #会社名、表紙
		return self.CompanyNameCoverPage

	def getCompanyNameInEnglishCoverPage(self): #英訳名、表紙
		return self.CompanyNameInEnglishCoverPage

	def getTitleAndNameOfRepresentativeCoverPage(self): #代表者の役職氏名、表紙
		return self.TitleAndNameOfRepresentativeCoverPage

	def getAddressOfRegisteredHeadquarterCoverPage(self): #本店の所在の場所、表紙
		return self.AddressOfRegisteredHeadquarterCoverPage

	def getTelephoneNumberAddressOfRegisteredHeadquarterCoverPage(self): #電話番号、本店の所在の場所、表紙
		return self.TelephoneNumberAddressOfRegisteredHeadquarterCoverPage

	def getNameOfContactPersonCoverPage(self): #事務連絡者氏名、表紙
		return self.NameOfContactPersonCoverPage

	def getNearestPlaceOfContactCoverPage(self): #最寄りの連絡場所、表紙
		return self.NearestPlaceOfContactCoverPage

	def getTelephoneNumberNearestPlaceOfContactCoverPage(self): #電話番号、最寄りの連絡場所、表紙
		return self.TelephoneNumberNearestPlaceOfContactCoverPage

	def getNameOfContactPersonNearestPlaceOfContactCoverPage(self): #事務連絡者氏名、最寄りの連絡場所、表紙
		return self.NameOfContactPersonNearestPlaceOfContactCoverPage

	def getPlaceForPublicInspectionCoverPageTextBlock(self): #縦覧に供する場所、表紙 [テキストブロック]
		return self.PlaceForPublicInspectionCoverPageTextBlock

	def getClassesOfSharesHeading(self): #株式の種類 [目次項目]
		return self.ClassesOfSharesHeading

	def getClassesOfSharesTextBlock(self): #株式の種類 [テキストブロック]
		return self.ClassesOfSharesTextBlock

	def getAcquisitionsOfTreasurySharesHeading(self): #取得状況 [目次項目]
		return self.AcquisitionsOfTreasurySharesHeading

	def getAcquisitionsByResolutionOfShareholdersMeetingHeading(self): #株主総会決議による取得の状況 [目次項目]
		return self.AcquisitionsByResolutionOfShareholdersMeetingHeading

	def getAcquisitionsByResolutionOfShareholdersMeetingTextBlock(self): #株主総会決議による取得の状況 [テキストブロック]
		return self.AcquisitionsByResolutionOfShareholdersMeetingTextBlock

	def getAcquisitionsByResolutionOfBoardOfDirectorsMeetingHeading(self): #取締役会決議による取得の状況 [目次項目]
		return self.AcquisitionsByResolutionOfBoardOfDirectorsMeetingHeading

	def getAcquisitionsByResolutionOfBoardOfDirectorsMeetingTextBlock(self): #取締役会決議による取得の状況 [テキストブロック]
		return self.AcquisitionsByResolutionOfBoardOfDirectorsMeetingTextBlock

	def getDisposalsOfTreasurySharesHeading(self): #処理状況 [目次項目]
		return self.DisposalsOfTreasurySharesHeading

	def getDisposalsOfTreasurySharesTextBlock(self): #処理状況 [テキストブロック]
		return self.DisposalsOfTreasurySharesTextBlock

	def getHoldingOfTreasurySharesHeading(self): #保有状況 [目次項目]
		return self.HoldingOfTreasurySharesHeading

	def getHoldingOfTreasurySharesTextBlock(self): #保有状況 [テキストブロック]
		return self.HoldingOfTreasurySharesTextBlock
