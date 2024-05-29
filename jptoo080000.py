from arelle import ModelManager
from arelle import Cntlr

class jptoo080000:#発行者以外の者による株券等の公開買付けの開示に関する内閣府令 第八号様式 対質問回答報告書
	CabinetOfficeOrdinanceOnDisclosureOfTenderOfferForShareCertificatesEtcByThoseOtherThanIssuerFormNo8TenderOfferorSAnswerHeading = '' #発行者以外の者による株券等の公開買付けの開示に関する内閣府令 第八号様式 対質問回答報告書 [目次項目]
	CoverPageHeading = '' #表紙 [目次項目]
	CoverPageHeading = '' #表紙 [目次項目]
	DocumentTitleCoverPage = '' #提出書類、表紙
	PlaceOfFilingCoverPage = '' #提出先、表紙
	DateWhenPositionStatementWasReceivedCoverPage = '' #意見表明報告書受理日、表紙
	FilingDateCoverPage = '' #提出日、表紙
	FullNameOrNameOfFilerCoverPage = '' #報告者の氏名又は名称、表紙
	ResidentialAddressOrLocationOfFilerCoverPage = '' #報告者の住所又は所在地、表紙
	NearestPlaceOfContactCoverPage = '' #最寄りの連絡場所、表紙
	NearestPlaceOfContactCoverPageNA = '' #最寄りの連絡場所、表紙（該当なし）
	TelephoneNumberCoverPage = '' #電話番号、表紙
	TelephoneNumberCoverPageNA = '' #電話番号、表紙（該当なし）
	NameOfContactPersonCoverPage = '' #事務連絡者氏名、表紙
	PlaceForPublicInspectionCoverPageTextBlock = '' #縦覧に供する場所、表紙 [テキストブロック]
	PlaceForPublicInspectionCoverPageNA = '' #縦覧に供する場所、表紙（該当なし）
	NotesCoverPageTextBlock = '' #脚注、表紙 [テキストブロック]
	NameOfSubjectCompanyHeading = '' #対象者名 [目次項目]
	NameOfSubjectCompanyTextBlock = '' #対象者名 [テキストブロック]
	ResponsesToInquiriesHeading = '' #質問に対する回答 [目次項目]
	ResponsesToInquiriesTextBlock = '' #質問に対する回答 [テキストブロック]

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
			elif fact.concept.qname.localName == 'CabinetOfficeOrdinanceOnDisclosureOfTenderOfferForShareCertificatesEtcByThoseOtherThanIssuerFormNo8TenderOfferorSAnswerHeading': #発行者以外の者による株券等の公開買付けの開示に関する内閣府令 第八号様式 対質問回答報告書 [目次項目]
				self.CabinetOfficeOrdinanceOnDisclosureOfTenderOfferForShareCertificatesEtcByThoseOtherThanIssuerFormNo8TenderOfferorSAnswerHeading = fact.value

			elif fact.concept.qname.localName == 'CoverPageHeading': #表紙 [目次項目]
				self.CoverPageHeading = fact.value

			elif fact.concept.qname.localName == 'CoverPageHeading': #表紙 [目次項目]
				self.CoverPageHeading = fact.value

			elif fact.concept.qname.localName == 'DocumentTitleCoverPage': #提出書類、表紙
				self.DocumentTitleCoverPage = fact.value

			elif fact.concept.qname.localName == 'PlaceOfFilingCoverPage': #提出先、表紙
				self.PlaceOfFilingCoverPage = fact.value

			elif fact.concept.qname.localName == 'DateWhenPositionStatementWasReceivedCoverPage': #意見表明報告書受理日、表紙
				self.DateWhenPositionStatementWasReceivedCoverPage = fact.value

			elif fact.concept.qname.localName == 'FilingDateCoverPage': #提出日、表紙
				self.FilingDateCoverPage = fact.value

			elif fact.concept.qname.localName == 'FullNameOrNameOfFilerCoverPage': #報告者の氏名又は名称、表紙
				self.FullNameOrNameOfFilerCoverPage = fact.value

			elif fact.concept.qname.localName == 'ResidentialAddressOrLocationOfFilerCoverPage': #報告者の住所又は所在地、表紙
				self.ResidentialAddressOrLocationOfFilerCoverPage = fact.value

			elif fact.concept.qname.localName == 'NearestPlaceOfContactCoverPage': #最寄りの連絡場所、表紙
				self.NearestPlaceOfContactCoverPage = fact.value

			elif fact.concept.qname.localName == 'NearestPlaceOfContactCoverPageNA': #最寄りの連絡場所、表紙（該当なし）
				self.NearestPlaceOfContactCoverPageNA = fact.value

			elif fact.concept.qname.localName == 'TelephoneNumberCoverPage': #電話番号、表紙
				self.TelephoneNumberCoverPage = fact.value

			elif fact.concept.qname.localName == 'TelephoneNumberCoverPageNA': #電話番号、表紙（該当なし）
				self.TelephoneNumberCoverPageNA = fact.value

			elif fact.concept.qname.localName == 'NameOfContactPersonCoverPage': #事務連絡者氏名、表紙
				self.NameOfContactPersonCoverPage = fact.value

			elif fact.concept.qname.localName == 'PlaceForPublicInspectionCoverPageTextBlock': #縦覧に供する場所、表紙 [テキストブロック]
				self.PlaceForPublicInspectionCoverPageTextBlock = fact.value

			elif fact.concept.qname.localName == 'PlaceForPublicInspectionCoverPageNA': #縦覧に供する場所、表紙（該当なし）
				self.PlaceForPublicInspectionCoverPageNA = fact.value

			elif fact.concept.qname.localName == 'NotesCoverPageTextBlock': #脚注、表紙 [テキストブロック]
				self.NotesCoverPageTextBlock = fact.value

			elif fact.concept.qname.localName == 'NameOfSubjectCompanyHeading': #対象者名 [目次項目]
				self.NameOfSubjectCompanyHeading = fact.value

			elif fact.concept.qname.localName == 'NameOfSubjectCompanyTextBlock': #対象者名 [テキストブロック]
				self.NameOfSubjectCompanyTextBlock = fact.value

			elif fact.concept.qname.localName == 'ResponsesToInquiriesHeading': #質問に対する回答 [目次項目]
				self.ResponsesToInquiriesHeading = fact.value

			elif fact.concept.qname.localName == 'ResponsesToInquiriesTextBlock': #質問に対する回答 [テキストブロック]
				self.ResponsesToInquiriesTextBlock = fact.value


	def getCabinetOfficeOrdinanceOnDisclosureOfTenderOfferForShareCertificatesEtcByThoseOtherThanIssuerFormNo8TenderOfferorSAnswerHeading(self): #発行者以外の者による株券等の公開買付けの開示に関する内閣府令 第八号様式 対質問回答報告書 [目次項目]
		return self.CabinetOfficeOrdinanceOnDisclosureOfTenderOfferForShareCertificatesEtcByThoseOtherThanIssuerFormNo8TenderOfferorSAnswerHeading

	def getCoverPageHeading(self): #表紙 [目次項目]
		return self.CoverPageHeading

	def getCoverPageHeading(self): #表紙 [目次項目]
		return self.CoverPageHeading

	def getDocumentTitleCoverPage(self): #提出書類、表紙
		return self.DocumentTitleCoverPage

	def getPlaceOfFilingCoverPage(self): #提出先、表紙
		return self.PlaceOfFilingCoverPage

	def getDateWhenPositionStatementWasReceivedCoverPage(self): #意見表明報告書受理日、表紙
		return self.DateWhenPositionStatementWasReceivedCoverPage

	def getFilingDateCoverPage(self): #提出日、表紙
		return self.FilingDateCoverPage

	def getFullNameOrNameOfFilerCoverPage(self): #報告者の氏名又は名称、表紙
		return self.FullNameOrNameOfFilerCoverPage

	def getResidentialAddressOrLocationOfFilerCoverPage(self): #報告者の住所又は所在地、表紙
		return self.ResidentialAddressOrLocationOfFilerCoverPage

	def getNearestPlaceOfContactCoverPage(self): #最寄りの連絡場所、表紙
		return self.NearestPlaceOfContactCoverPage

	def getNearestPlaceOfContactCoverPageNA(self): #最寄りの連絡場所、表紙（該当なし）
		return self.NearestPlaceOfContactCoverPageNA

	def getTelephoneNumberCoverPage(self): #電話番号、表紙
		return self.TelephoneNumberCoverPage

	def getTelephoneNumberCoverPageNA(self): #電話番号、表紙（該当なし）
		return self.TelephoneNumberCoverPageNA

	def getNameOfContactPersonCoverPage(self): #事務連絡者氏名、表紙
		return self.NameOfContactPersonCoverPage

	def getPlaceForPublicInspectionCoverPageTextBlock(self): #縦覧に供する場所、表紙 [テキストブロック]
		return self.PlaceForPublicInspectionCoverPageTextBlock

	def getPlaceForPublicInspectionCoverPageNA(self): #縦覧に供する場所、表紙（該当なし）
		return self.PlaceForPublicInspectionCoverPageNA

	def getNotesCoverPageTextBlock(self): #脚注、表紙 [テキストブロック]
		return self.NotesCoverPageTextBlock

	def getNameOfSubjectCompanyHeading(self): #対象者名 [目次項目]
		return self.NameOfSubjectCompanyHeading

	def getNameOfSubjectCompanyTextBlock(self): #対象者名 [テキストブロック]
		return self.NameOfSubjectCompanyTextBlock

	def getResponsesToInquiriesHeading(self): #質問に対する回答 [目次項目]
		return self.ResponsesToInquiriesHeading

	def getResponsesToInquiriesTextBlock(self): #質問に対する回答 [テキストブロック]
		return self.ResponsesToInquiriesTextBlock
