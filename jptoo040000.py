from arelle import ModelManager
from arelle import Cntlr

class jptoo040000:#発行者以外の者による株券等の公開買付けの開示に関する内閣府令 第四号様式 意見表明報告書
	CabinetOfficeOrdinanceOnDisclosureOfTenderOfferForShareCertificatesEtcByThoseOtherThanIssuerFormNo4SubjectCompanySPositionStatementHeading = '' #発行者以外の者による株券等の公開買付けの開示に関する内閣府令 第四号様式 意見表明報告書 [目次項目]
	CoverPageHeading = '' #表紙 [目次項目]
	CoverPageHeading = '' #表紙 [目次項目]
	DocumentTitleCoverPage = '' #提出書類、表紙
	PlaceOfFilingCoverPage = '' #提出先、表紙
	FilingDateCoverPage = '' #提出日、表紙
	NameOfFilerCoverPage = '' #報告者の名称、表紙
	LocationOfFilerCoverPage = '' #報告者の所在地、表紙
	NearestPlaceOfContactCoverPage = '' #最寄りの連絡場所、表紙
	TelephoneNumberCoverPage = '' #電話番号、表紙
	NameOfContactPersonCoverPage = '' #事務連絡者氏名、表紙
	PlaceForPublicInspectionCoverPageTextBlock = '' #縦覧に供する場所、表紙 [テキストブロック]
	PlaceForPublicInspectionCoverPageNA = '' #縦覧に供する場所、表紙（該当なし）
	NotesCoverPageTextBlock = '' #脚注、表紙 [テキストブロック]
	NameAndResidentialAddressOrLocationOfTenderOfferorHeading = '' #公開買付者の氏名又は名称及び住所又は所在地 [目次項目]
	NameAndResidentialAddressOrLocationOfTenderOfferorTextBlock = '' #公開買付者の氏名又は名称及び住所又は所在地 [テキストブロック]
	ClassesOfShareCertificatesEtcForTenderOfferorToAcquireByPurchaseEtcHeading = '' #公開買付者が買付け等を行う株券等の種類 [目次項目]
	ClassesOfShareCertificatesEtcForTenderOfferorToAcquireByPurchaseEtcTextBlock = '' #公開買付者が買付け等を行う株券等の種類 [テキストブロック]
	OpinionAndBasisAndReasonOfOpinionRegardingSaidTenderOfferHeading = '' #当該公開買付けに関する意見の内容、根拠及び理由 [目次項目]
	OpinionAndBasisAndReasonOfOpinionRegardingSaidTenderOfferTextBlock = '' #当該公開買付けに関する意見の内容、根拠及び理由 [テキストブロック]
	NumberOfShareCertificatesEtcAndNumberOfVotingRightsOwnedByOfficersHeading = '' #役員が所有する株券等の数及び当該株券等に係る議決権の数 [目次項目]
	NumberOfShareCertificatesEtcAndNumberOfVotingRightsOwnedByOfficersTextBlock = '' #役員が所有する株券等の数及び当該株券等に係る議決権の数 [テキストブロック]
	DescriptionOfProvisionOfProfitByTenderOfferorOrItsSpecialInterestPartiesHeading = '' #公開買付者又はその特別関係者による利益供与の内容 [目次項目]
	DescriptionOfProvisionOfProfitByTenderOfferorOrItsSpecialInterestPartiesTextBlock = '' #公開買付者又はその特別関係者による利益供与の内容 [テキストブロック]
	DescriptionOfProvisionOfProfitByTenderOfferorOrItsSpecialInterestPartiesNA = '' #公開買付者又はその特別関係者による利益供与の内容（該当なし）
	PolicyToAddressBasicPolicyAboutHowToControlCompanyHeading = '' #会社の支配に関する基本方針に係る対応方針 [目次項目]
	PolicyToAddressBasicPolicyAboutHowToControlCompanyTextBlock = '' #会社の支配に関する基本方針に係る対応方針 [テキストブロック]
	PolicyToAddressBasicPolicyAboutHowToControlCompanyNA = '' #会社の支配に関する基本方針に係る対応方針（該当なし）
	InquiriesToTenderOfferorHeading = '' #公開買付者に対する質問 [目次項目]
	InquiriesToTenderOfferorTextBlock = '' #公開買付者に対する質問 [テキストブロック]
	InquiriesToTenderOfferorNA = '' #公開買付者に対する質問（該当なし）
	RequestForExtendingTenderOfferPeriodHeading = '' #公開買付期間の延長請求 [目次項目]
	RequestForExtendingTenderOfferPeriodTextBlock = '' #公開買付期間の延長請求 [テキストブロック]
	RequestForExtendingTenderOfferPeriodNA = '' #公開買付期間の延長請求（該当なし）

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
			elif fact.concept.qname.localName == 'CabinetOfficeOrdinanceOnDisclosureOfTenderOfferForShareCertificatesEtcByThoseOtherThanIssuerFormNo4SubjectCompanySPositionStatementHeading': #発行者以外の者による株券等の公開買付けの開示に関する内閣府令 第四号様式 意見表明報告書 [目次項目]
				self.CabinetOfficeOrdinanceOnDisclosureOfTenderOfferForShareCertificatesEtcByThoseOtherThanIssuerFormNo4SubjectCompanySPositionStatementHeading = fact.value

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

			elif fact.concept.qname.localName == 'NameOfFilerCoverPage': #報告者の名称、表紙
				self.NameOfFilerCoverPage = fact.value

			elif fact.concept.qname.localName == 'LocationOfFilerCoverPage': #報告者の所在地、表紙
				self.LocationOfFilerCoverPage = fact.value

			elif fact.concept.qname.localName == 'NearestPlaceOfContactCoverPage': #最寄りの連絡場所、表紙
				self.NearestPlaceOfContactCoverPage = fact.value

			elif fact.concept.qname.localName == 'TelephoneNumberCoverPage': #電話番号、表紙
				self.TelephoneNumberCoverPage = fact.value

			elif fact.concept.qname.localName == 'NameOfContactPersonCoverPage': #事務連絡者氏名、表紙
				self.NameOfContactPersonCoverPage = fact.value

			elif fact.concept.qname.localName == 'PlaceForPublicInspectionCoverPageTextBlock': #縦覧に供する場所、表紙 [テキストブロック]
				self.PlaceForPublicInspectionCoverPageTextBlock = fact.value

			elif fact.concept.qname.localName == 'PlaceForPublicInspectionCoverPageNA': #縦覧に供する場所、表紙（該当なし）
				self.PlaceForPublicInspectionCoverPageNA = fact.value

			elif fact.concept.qname.localName == 'NotesCoverPageTextBlock': #脚注、表紙 [テキストブロック]
				self.NotesCoverPageTextBlock = fact.value

			elif fact.concept.qname.localName == 'NameAndResidentialAddressOrLocationOfTenderOfferorHeading': #公開買付者の氏名又は名称及び住所又は所在地 [目次項目]
				self.NameAndResidentialAddressOrLocationOfTenderOfferorHeading = fact.value

			elif fact.concept.qname.localName == 'NameAndResidentialAddressOrLocationOfTenderOfferorTextBlock': #公開買付者の氏名又は名称及び住所又は所在地 [テキストブロック]
				self.NameAndResidentialAddressOrLocationOfTenderOfferorTextBlock = fact.value

			elif fact.concept.qname.localName == 'ClassesOfShareCertificatesEtcForTenderOfferorToAcquireByPurchaseEtcHeading': #公開買付者が買付け等を行う株券等の種類 [目次項目]
				self.ClassesOfShareCertificatesEtcForTenderOfferorToAcquireByPurchaseEtcHeading = fact.value

			elif fact.concept.qname.localName == 'ClassesOfShareCertificatesEtcForTenderOfferorToAcquireByPurchaseEtcTextBlock': #公開買付者が買付け等を行う株券等の種類 [テキストブロック]
				self.ClassesOfShareCertificatesEtcForTenderOfferorToAcquireByPurchaseEtcTextBlock = fact.value

			elif fact.concept.qname.localName == 'OpinionAndBasisAndReasonOfOpinionRegardingSaidTenderOfferHeading': #当該公開買付けに関する意見の内容、根拠及び理由 [目次項目]
				self.OpinionAndBasisAndReasonOfOpinionRegardingSaidTenderOfferHeading = fact.value

			elif fact.concept.qname.localName == 'OpinionAndBasisAndReasonOfOpinionRegardingSaidTenderOfferTextBlock': #当該公開買付けに関する意見の内容、根拠及び理由 [テキストブロック]
				self.OpinionAndBasisAndReasonOfOpinionRegardingSaidTenderOfferTextBlock = fact.value

			elif fact.concept.qname.localName == 'NumberOfShareCertificatesEtcAndNumberOfVotingRightsOwnedByOfficersHeading': #役員が所有する株券等の数及び当該株券等に係る議決権の数 [目次項目]
				self.NumberOfShareCertificatesEtcAndNumberOfVotingRightsOwnedByOfficersHeading = fact.value

			elif fact.concept.qname.localName == 'NumberOfShareCertificatesEtcAndNumberOfVotingRightsOwnedByOfficersTextBlock': #役員が所有する株券等の数及び当該株券等に係る議決権の数 [テキストブロック]
				self.NumberOfShareCertificatesEtcAndNumberOfVotingRightsOwnedByOfficersTextBlock = fact.value

			elif fact.concept.qname.localName == 'DescriptionOfProvisionOfProfitByTenderOfferorOrItsSpecialInterestPartiesHeading': #公開買付者又はその特別関係者による利益供与の内容 [目次項目]
				self.DescriptionOfProvisionOfProfitByTenderOfferorOrItsSpecialInterestPartiesHeading = fact.value

			elif fact.concept.qname.localName == 'DescriptionOfProvisionOfProfitByTenderOfferorOrItsSpecialInterestPartiesTextBlock': #公開買付者又はその特別関係者による利益供与の内容 [テキストブロック]
				self.DescriptionOfProvisionOfProfitByTenderOfferorOrItsSpecialInterestPartiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'DescriptionOfProvisionOfProfitByTenderOfferorOrItsSpecialInterestPartiesNA': #公開買付者又はその特別関係者による利益供与の内容（該当なし）
				self.DescriptionOfProvisionOfProfitByTenderOfferorOrItsSpecialInterestPartiesNA = fact.value

			elif fact.concept.qname.localName == 'PolicyToAddressBasicPolicyAboutHowToControlCompanyHeading': #会社の支配に関する基本方針に係る対応方針 [目次項目]
				self.PolicyToAddressBasicPolicyAboutHowToControlCompanyHeading = fact.value

			elif fact.concept.qname.localName == 'PolicyToAddressBasicPolicyAboutHowToControlCompanyTextBlock': #会社の支配に関する基本方針に係る対応方針 [テキストブロック]
				self.PolicyToAddressBasicPolicyAboutHowToControlCompanyTextBlock = fact.value

			elif fact.concept.qname.localName == 'PolicyToAddressBasicPolicyAboutHowToControlCompanyNA': #会社の支配に関する基本方針に係る対応方針（該当なし）
				self.PolicyToAddressBasicPolicyAboutHowToControlCompanyNA = fact.value

			elif fact.concept.qname.localName == 'InquiriesToTenderOfferorHeading': #公開買付者に対する質問 [目次項目]
				self.InquiriesToTenderOfferorHeading = fact.value

			elif fact.concept.qname.localName == 'InquiriesToTenderOfferorTextBlock': #公開買付者に対する質問 [テキストブロック]
				self.InquiriesToTenderOfferorTextBlock = fact.value

			elif fact.concept.qname.localName == 'InquiriesToTenderOfferorNA': #公開買付者に対する質問（該当なし）
				self.InquiriesToTenderOfferorNA = fact.value

			elif fact.concept.qname.localName == 'RequestForExtendingTenderOfferPeriodHeading': #公開買付期間の延長請求 [目次項目]
				self.RequestForExtendingTenderOfferPeriodHeading = fact.value

			elif fact.concept.qname.localName == 'RequestForExtendingTenderOfferPeriodTextBlock': #公開買付期間の延長請求 [テキストブロック]
				self.RequestForExtendingTenderOfferPeriodTextBlock = fact.value

			elif fact.concept.qname.localName == 'RequestForExtendingTenderOfferPeriodNA': #公開買付期間の延長請求（該当なし）
				self.RequestForExtendingTenderOfferPeriodNA = fact.value


	def getCabinetOfficeOrdinanceOnDisclosureOfTenderOfferForShareCertificatesEtcByThoseOtherThanIssuerFormNo4SubjectCompanySPositionStatementHeading(self): #発行者以外の者による株券等の公開買付けの開示に関する内閣府令 第四号様式 意見表明報告書 [目次項目]
		return self.CabinetOfficeOrdinanceOnDisclosureOfTenderOfferForShareCertificatesEtcByThoseOtherThanIssuerFormNo4SubjectCompanySPositionStatementHeading

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

	def getNameOfFilerCoverPage(self): #報告者の名称、表紙
		return self.NameOfFilerCoverPage

	def getLocationOfFilerCoverPage(self): #報告者の所在地、表紙
		return self.LocationOfFilerCoverPage

	def getNearestPlaceOfContactCoverPage(self): #最寄りの連絡場所、表紙
		return self.NearestPlaceOfContactCoverPage

	def getTelephoneNumberCoverPage(self): #電話番号、表紙
		return self.TelephoneNumberCoverPage

	def getNameOfContactPersonCoverPage(self): #事務連絡者氏名、表紙
		return self.NameOfContactPersonCoverPage

	def getPlaceForPublicInspectionCoverPageTextBlock(self): #縦覧に供する場所、表紙 [テキストブロック]
		return self.PlaceForPublicInspectionCoverPageTextBlock

	def getPlaceForPublicInspectionCoverPageNA(self): #縦覧に供する場所、表紙（該当なし）
		return self.PlaceForPublicInspectionCoverPageNA

	def getNotesCoverPageTextBlock(self): #脚注、表紙 [テキストブロック]
		return self.NotesCoverPageTextBlock

	def getNameAndResidentialAddressOrLocationOfTenderOfferorHeading(self): #公開買付者の氏名又は名称及び住所又は所在地 [目次項目]
		return self.NameAndResidentialAddressOrLocationOfTenderOfferorHeading

	def getNameAndResidentialAddressOrLocationOfTenderOfferorTextBlock(self): #公開買付者の氏名又は名称及び住所又は所在地 [テキストブロック]
		return self.NameAndResidentialAddressOrLocationOfTenderOfferorTextBlock

	def getClassesOfShareCertificatesEtcForTenderOfferorToAcquireByPurchaseEtcHeading(self): #公開買付者が買付け等を行う株券等の種類 [目次項目]
		return self.ClassesOfShareCertificatesEtcForTenderOfferorToAcquireByPurchaseEtcHeading

	def getClassesOfShareCertificatesEtcForTenderOfferorToAcquireByPurchaseEtcTextBlock(self): #公開買付者が買付け等を行う株券等の種類 [テキストブロック]
		return self.ClassesOfShareCertificatesEtcForTenderOfferorToAcquireByPurchaseEtcTextBlock

	def getOpinionAndBasisAndReasonOfOpinionRegardingSaidTenderOfferHeading(self): #当該公開買付けに関する意見の内容、根拠及び理由 [目次項目]
		return self.OpinionAndBasisAndReasonOfOpinionRegardingSaidTenderOfferHeading

	def getOpinionAndBasisAndReasonOfOpinionRegardingSaidTenderOfferTextBlock(self): #当該公開買付けに関する意見の内容、根拠及び理由 [テキストブロック]
		return self.OpinionAndBasisAndReasonOfOpinionRegardingSaidTenderOfferTextBlock

	def getNumberOfShareCertificatesEtcAndNumberOfVotingRightsOwnedByOfficersHeading(self): #役員が所有する株券等の数及び当該株券等に係る議決権の数 [目次項目]
		return self.NumberOfShareCertificatesEtcAndNumberOfVotingRightsOwnedByOfficersHeading

	def getNumberOfShareCertificatesEtcAndNumberOfVotingRightsOwnedByOfficersTextBlock(self): #役員が所有する株券等の数及び当該株券等に係る議決権の数 [テキストブロック]
		return self.NumberOfShareCertificatesEtcAndNumberOfVotingRightsOwnedByOfficersTextBlock

	def getDescriptionOfProvisionOfProfitByTenderOfferorOrItsSpecialInterestPartiesHeading(self): #公開買付者又はその特別関係者による利益供与の内容 [目次項目]
		return self.DescriptionOfProvisionOfProfitByTenderOfferorOrItsSpecialInterestPartiesHeading

	def getDescriptionOfProvisionOfProfitByTenderOfferorOrItsSpecialInterestPartiesTextBlock(self): #公開買付者又はその特別関係者による利益供与の内容 [テキストブロック]
		return self.DescriptionOfProvisionOfProfitByTenderOfferorOrItsSpecialInterestPartiesTextBlock

	def getDescriptionOfProvisionOfProfitByTenderOfferorOrItsSpecialInterestPartiesNA(self): #公開買付者又はその特別関係者による利益供与の内容（該当なし）
		return self.DescriptionOfProvisionOfProfitByTenderOfferorOrItsSpecialInterestPartiesNA

	def getPolicyToAddressBasicPolicyAboutHowToControlCompanyHeading(self): #会社の支配に関する基本方針に係る対応方針 [目次項目]
		return self.PolicyToAddressBasicPolicyAboutHowToControlCompanyHeading

	def getPolicyToAddressBasicPolicyAboutHowToControlCompanyTextBlock(self): #会社の支配に関する基本方針に係る対応方針 [テキストブロック]
		return self.PolicyToAddressBasicPolicyAboutHowToControlCompanyTextBlock

	def getPolicyToAddressBasicPolicyAboutHowToControlCompanyNA(self): #会社の支配に関する基本方針に係る対応方針（該当なし）
		return self.PolicyToAddressBasicPolicyAboutHowToControlCompanyNA

	def getInquiriesToTenderOfferorHeading(self): #公開買付者に対する質問 [目次項目]
		return self.InquiriesToTenderOfferorHeading

	def getInquiriesToTenderOfferorTextBlock(self): #公開買付者に対する質問 [テキストブロック]
		return self.InquiriesToTenderOfferorTextBlock

	def getInquiriesToTenderOfferorNA(self): #公開買付者に対する質問（該当なし）
		return self.InquiriesToTenderOfferorNA

	def getRequestForExtendingTenderOfferPeriodHeading(self): #公開買付期間の延長請求 [目次項目]
		return self.RequestForExtendingTenderOfferPeriodHeading

	def getRequestForExtendingTenderOfferPeriodTextBlock(self): #公開買付期間の延長請求 [テキストブロック]
		return self.RequestForExtendingTenderOfferPeriodTextBlock

	def getRequestForExtendingTenderOfferPeriodNA(self): #公開買付期間の延長請求（該当なし）
		return self.RequestForExtendingTenderOfferPeriodNA
