from arelle import ModelManager
from arelle import Cntlr

class jpcrp050300:#企業内容等の開示に関する内閣府令 第五号の三様式 臨時報告書
	CabinetOfficeOrdinanceOnDisclosureOfCorporateInformationEtcFormNo53ExtraordinarySecuritiesReportHeading = '' #企業内容等の開示に関する内閣府令 第五号の三様式 臨時報告書 [目次項目]
	CoverPageHeading = '' #表紙 [目次項目]
	CoverPageHeading = '' #表紙 [目次項目]
	DocumentTitleCoverPage = '' #提出書類、表紙
	PlaceOfFilingCoverPage = '' #提出先、表紙
	FilingDateCoverPage = '' #提出日、表紙
	CompanyNameCoverPage = '' #会社名、表紙
	CompanyNameInEnglishCoverPage = '' #英訳名、表紙
	TitleAndNameOfRepresentativeCoverPage = '' #代表者の役職氏名、表紙
	AddressOfRegisteredHeadquarterCoverPage = '' #本店の所在の場所、表紙
	TelephoneNumberCoverPage = '' #電話番号、表紙
	NameOfContactPersonCoverPage = '' #事務連絡者氏名、表紙
	NearestPlaceOfContactCoverPage = '' #最寄りの連絡場所、表紙
	TelephoneNumberNearestPlaceOfContactCoverPage = '' #電話番号、最寄りの連絡場所、表紙
	NameOfContactPersonNearestPlaceOfContactCoverPage = '' #事務連絡者氏名、最寄りの連絡場所、表紙
	PlaceForPublicInspectionCoverPageTextBlock = '' #縦覧に供する場所、表紙 [テキストブロック]
	ReasonForFilingHeading = '' #提出理由 [目次項目]
	ReasonForFilingTextBlock = '' #提出理由 [テキストブロック]
	BodyOfReportHeading = '' #報告内容 [目次項目]
	PublicOfferingOrSecondaryDistributionOfSecuritiesOutsideJapanTextBlock = '' #本邦以外の地域における有価証券の募集又は売出 [テキストブロック]
	PrivatePlacementOfSecuritiesTextBlock = '' #有価証券の私募等による発行 [テキストブロック]
	IssueOfStockOptionsNotSubjectToSecuritiesRegistrationTextBlock = '' #届出を要しない株券等又は新株予約権証券等の発行 [テキストブロック]
	ChangesInParentCompaniesOrSpecifiedSubsidiariesTextBlock = '' #親会社又は特定子会社の異動 [テキストブロック]
	ChangesInMajorShareholderTextBlock = '' #主要株主の異動 [テキストブロック]
	NotificationOfRequestForSaleOfSharesFromSpecialControllingShareholdersOrDecisionOnWhetherToApproveRequestForSaleOfSharesOrNotTextBlock = '' #特別支配株主から株式等売渡請求の通知がされた場合又は当該株式等売渡請求を承認するか否かが決定された場合 [テキストブロック]
	DecisionOnHoldingShareholdersMeetingToAcquireAllClassSharesSubjectToWhollyCallTextBlock = '' #全部取得条項付種類株式の全部の取得を目的とする株主総会の招集の決定 [テキストブロック]
	DecisionOnHoldingShareholdersMeetingForPurposeOfReverseStockSplitTextBlock = '' #株式の併合を目的とする株主総会の招集の決定 [テキストブロック]
	SignificantDisasterTextBlock = '' #重要な災害の発生 [テキストブロック]
	CommencementOrResolutionOfLitigationTextBlock = '' #訴訟の提起又は解決 [テキストブロック]
	DecisionOnShareExchangeTextBlock = '' #株式交換の決定 [テキストブロック]
	DecisionOnShareTransferTextBlock = '' #株式移転の決定 [テキストブロック]
	DecisionOnAbsorptionTypeSplitTextBlock = '' #吸収分割の決定 [テキストブロック]
	DecisionOnIncorporationTypeSplitTextBlock = '' #新設分割の決定 [テキストブロック]
	DecisionOnAbsorptionTypeMergerTextBlock = '' #吸収合併の決定 [テキストブロック]
	DecisionOnConsolidationTypeMergerTextBlock = '' #新設合併の決定 [テキストブロック]
	DecisionOnTransferOrAcquisitionOfBusinessTextBlock = '' #事業の譲渡又は譲受けの決定 [テキストブロック]
	DecisionOnAcquisitionOfSubsidiaryTextBlock = '' #子会社取得の決定 [テキストブロック]
	ChangesInRepresentativeDirectorsTextBlock = '' #代表取締役の異動 [テキストブロック]
	ResolutionOfShareholdersMeetingTextBlock = '' #株主総会における決議 [テキストブロック]
	AmendmentOrRejectionByShareholdersMeetingTextBlock = '' #株主総会における修正又は否決 [テキストブロック]
	ChangeInIndependentAuditorsTextBlock = '' #監査公認会計士等の異動 [テキストブロック]
	PetitionEtcForCommencementOfBankruptcyProceedingsTextBlock = '' #破産手続開始の申立て等 [テキストブロック]
	LikelihoodOfUncollectibleOrDelinquentAccountsTextBlock = '' #取立不能又は取立遅延債権のおそれ [テキストブロック]
	EventWithSignificantEffectsOnFinancialPositionBusinessPerformanceAndCashFlowsTextBlock = '' #財政状態、経営成績及びキャッシュ・フローの状況に著しい影響を与える事象 [テキストブロック]
	SignificantDisasterAffectingConsolidatedSubsidiaryTextBlock = '' #連結子会社に係る重要な災害の発生 [テキストブロック]
	CommencementOrResolutionOfLitigationAgainstConsolidatedSubsidiaryTextBlock = '' #連結子会社に対する訴訟の提起又は解決 [テキストブロック]
	DecisionOnShareExchangeOfConsolidatedSubsidiaryTextBlock = '' #連結子会社の株式交換の決定 [テキストブロック]
	DecisionOnShareTransferOfConsolidatedSubsidiaryTextBlock = '' #連結子会社の株式移転の決定 [テキストブロック]
	DecisionOnAbsorptionTypeSplitOfConsolidatedSubsidiaryTextBlock = '' #連結子会社の吸収分割の決定 [テキストブロック]
	DecisionOnIncorporationTypeSplitOfConsolidatedSubsidiaryTextBlock = '' #連結子会社の新設分割の決定 [テキストブロック]
	DecisionOnAbsorptionTypeMergerOfConsolidatedSubsidiaryTextBlock = '' #連結子会社の吸収合併の決定 [テキストブロック]
	DecisionOnConsolidationTypeMergerOfConsolidatedSubsidiaryTextBlock = '' #連結子会社の新設合併の決定 [テキストブロック]
	DecisionOnTransferOrAcquisitionOfBusinessOfConsolidatedSubsidiaryTextBlock = '' #連結子会社の事業の譲渡又は譲受けの決定 [テキストブロック]
	DecisionOnAcquisitionOfSubsidiaryByConsolidatedSubsidiaryTextBlock = '' #連結子会社による子会社取得の決定 [テキストブロック]
	PetitionForCommencementOfBankruptcyProceedingsAgainstConsolidatedSubsidiaryTextBlock = '' #連結子会社に係る破産手続開始の申立て等 [テキストブロック]
	LikelihoodOfUncollectibleOrDelinquentAccountsOfConsolidatedSubsidiaryTextBlock = '' #連結子会社に係る取立不能又は取立遅延債権のおそれ [テキストブロック]
	EventWithSignificantEffectsOnFinancialPositionBusinessPerformanceAndCashFlowsOfGroupTextBlock = '' #連結会社の財政状態、経営成績及びキャッシュ・フローの状況に著しい影響を与える事象 [テキストブロック]
	NewMattersOrChangesInPublicOfferingInformationThroughToLastDayBeforeIPOTextBlock = '' #新規上場等の前日までにおける株式公開情報の発生又は変更 [テキストブロック]

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
			elif fact.concept.qname.localName == 'CabinetOfficeOrdinanceOnDisclosureOfCorporateInformationEtcFormNo53ExtraordinarySecuritiesReportHeading': #企業内容等の開示に関する内閣府令 第五号の三様式 臨時報告書 [目次項目]
				self.CabinetOfficeOrdinanceOnDisclosureOfCorporateInformationEtcFormNo53ExtraordinarySecuritiesReportHeading = fact.value

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

			elif fact.concept.qname.localName == 'CompanyNameCoverPage': #会社名、表紙
				self.CompanyNameCoverPage = fact.value

			elif fact.concept.qname.localName == 'CompanyNameInEnglishCoverPage': #英訳名、表紙
				self.CompanyNameInEnglishCoverPage = fact.value

			elif fact.concept.qname.localName == 'TitleAndNameOfRepresentativeCoverPage': #代表者の役職氏名、表紙
				self.TitleAndNameOfRepresentativeCoverPage = fact.value

			elif fact.concept.qname.localName == 'AddressOfRegisteredHeadquarterCoverPage': #本店の所在の場所、表紙
				self.AddressOfRegisteredHeadquarterCoverPage = fact.value

			elif fact.concept.qname.localName == 'TelephoneNumberCoverPage': #電話番号、表紙
				self.TelephoneNumberCoverPage = fact.value

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

			elif fact.concept.qname.localName == 'ReasonForFilingHeading': #提出理由 [目次項目]
				self.ReasonForFilingHeading = fact.value

			elif fact.concept.qname.localName == 'ReasonForFilingTextBlock': #提出理由 [テキストブロック]
				self.ReasonForFilingTextBlock = fact.value

			elif fact.concept.qname.localName == 'BodyOfReportHeading': #報告内容 [目次項目]
				self.BodyOfReportHeading = fact.value

			elif fact.concept.qname.localName == 'PublicOfferingOrSecondaryDistributionOfSecuritiesOutsideJapanTextBlock': #本邦以外の地域における有価証券の募集又は売出 [テキストブロック]
				self.PublicOfferingOrSecondaryDistributionOfSecuritiesOutsideJapanTextBlock = fact.value

			elif fact.concept.qname.localName == 'PrivatePlacementOfSecuritiesTextBlock': #有価証券の私募等による発行 [テキストブロック]
				self.PrivatePlacementOfSecuritiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'IssueOfStockOptionsNotSubjectToSecuritiesRegistrationTextBlock': #届出を要しない株券等又は新株予約権証券等の発行 [テキストブロック]
				self.IssueOfStockOptionsNotSubjectToSecuritiesRegistrationTextBlock = fact.value

			elif fact.concept.qname.localName == 'ChangesInParentCompaniesOrSpecifiedSubsidiariesTextBlock': #親会社又は特定子会社の異動 [テキストブロック]
				self.ChangesInParentCompaniesOrSpecifiedSubsidiariesTextBlock = fact.value

			elif fact.concept.qname.localName == 'ChangesInMajorShareholderTextBlock': #主要株主の異動 [テキストブロック]
				self.ChangesInMajorShareholderTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotificationOfRequestForSaleOfSharesFromSpecialControllingShareholdersOrDecisionOnWhetherToApproveRequestForSaleOfSharesOrNotTextBlock': #特別支配株主から株式等売渡請求の通知がされた場合又は当該株式等売渡請求を承認するか否かが決定された場合 [テキストブロック]
				self.NotificationOfRequestForSaleOfSharesFromSpecialControllingShareholdersOrDecisionOnWhetherToApproveRequestForSaleOfSharesOrNotTextBlock = fact.value

			elif fact.concept.qname.localName == 'DecisionOnHoldingShareholdersMeetingToAcquireAllClassSharesSubjectToWhollyCallTextBlock': #全部取得条項付種類株式の全部の取得を目的とする株主総会の招集の決定 [テキストブロック]
				self.DecisionOnHoldingShareholdersMeetingToAcquireAllClassSharesSubjectToWhollyCallTextBlock = fact.value

			elif fact.concept.qname.localName == 'DecisionOnHoldingShareholdersMeetingForPurposeOfReverseStockSplitTextBlock': #株式の併合を目的とする株主総会の招集の決定 [テキストブロック]
				self.DecisionOnHoldingShareholdersMeetingForPurposeOfReverseStockSplitTextBlock = fact.value

			elif fact.concept.qname.localName == 'SignificantDisasterTextBlock': #重要な災害の発生 [テキストブロック]
				self.SignificantDisasterTextBlock = fact.value

			elif fact.concept.qname.localName == 'CommencementOrResolutionOfLitigationTextBlock': #訴訟の提起又は解決 [テキストブロック]
				self.CommencementOrResolutionOfLitigationTextBlock = fact.value

			elif fact.concept.qname.localName == 'DecisionOnShareExchangeTextBlock': #株式交換の決定 [テキストブロック]
				self.DecisionOnShareExchangeTextBlock = fact.value

			elif fact.concept.qname.localName == 'DecisionOnShareTransferTextBlock': #株式移転の決定 [テキストブロック]
				self.DecisionOnShareTransferTextBlock = fact.value

			elif fact.concept.qname.localName == 'DecisionOnAbsorptionTypeSplitTextBlock': #吸収分割の決定 [テキストブロック]
				self.DecisionOnAbsorptionTypeSplitTextBlock = fact.value

			elif fact.concept.qname.localName == 'DecisionOnIncorporationTypeSplitTextBlock': #新設分割の決定 [テキストブロック]
				self.DecisionOnIncorporationTypeSplitTextBlock = fact.value

			elif fact.concept.qname.localName == 'DecisionOnAbsorptionTypeMergerTextBlock': #吸収合併の決定 [テキストブロック]
				self.DecisionOnAbsorptionTypeMergerTextBlock = fact.value

			elif fact.concept.qname.localName == 'DecisionOnConsolidationTypeMergerTextBlock': #新設合併の決定 [テキストブロック]
				self.DecisionOnConsolidationTypeMergerTextBlock = fact.value

			elif fact.concept.qname.localName == 'DecisionOnTransferOrAcquisitionOfBusinessTextBlock': #事業の譲渡又は譲受けの決定 [テキストブロック]
				self.DecisionOnTransferOrAcquisitionOfBusinessTextBlock = fact.value

			elif fact.concept.qname.localName == 'DecisionOnAcquisitionOfSubsidiaryTextBlock': #子会社取得の決定 [テキストブロック]
				self.DecisionOnAcquisitionOfSubsidiaryTextBlock = fact.value

			elif fact.concept.qname.localName == 'ChangesInRepresentativeDirectorsTextBlock': #代表取締役の異動 [テキストブロック]
				self.ChangesInRepresentativeDirectorsTextBlock = fact.value

			elif fact.concept.qname.localName == 'ResolutionOfShareholdersMeetingTextBlock': #株主総会における決議 [テキストブロック]
				self.ResolutionOfShareholdersMeetingTextBlock = fact.value

			elif fact.concept.qname.localName == 'AmendmentOrRejectionByShareholdersMeetingTextBlock': #株主総会における修正又は否決 [テキストブロック]
				self.AmendmentOrRejectionByShareholdersMeetingTextBlock = fact.value

			elif fact.concept.qname.localName == 'ChangeInIndependentAuditorsTextBlock': #監査公認会計士等の異動 [テキストブロック]
				self.ChangeInIndependentAuditorsTextBlock = fact.value

			elif fact.concept.qname.localName == 'PetitionEtcForCommencementOfBankruptcyProceedingsTextBlock': #破産手続開始の申立て等 [テキストブロック]
				self.PetitionEtcForCommencementOfBankruptcyProceedingsTextBlock = fact.value

			elif fact.concept.qname.localName == 'LikelihoodOfUncollectibleOrDelinquentAccountsTextBlock': #取立不能又は取立遅延債権のおそれ [テキストブロック]
				self.LikelihoodOfUncollectibleOrDelinquentAccountsTextBlock = fact.value

			elif fact.concept.qname.localName == 'EventWithSignificantEffectsOnFinancialPositionBusinessPerformanceAndCashFlowsTextBlock': #財政状態、経営成績及びキャッシュ・フローの状況に著しい影響を与える事象 [テキストブロック]
				self.EventWithSignificantEffectsOnFinancialPositionBusinessPerformanceAndCashFlowsTextBlock = fact.value

			elif fact.concept.qname.localName == 'SignificantDisasterAffectingConsolidatedSubsidiaryTextBlock': #連結子会社に係る重要な災害の発生 [テキストブロック]
				self.SignificantDisasterAffectingConsolidatedSubsidiaryTextBlock = fact.value

			elif fact.concept.qname.localName == 'CommencementOrResolutionOfLitigationAgainstConsolidatedSubsidiaryTextBlock': #連結子会社に対する訴訟の提起又は解決 [テキストブロック]
				self.CommencementOrResolutionOfLitigationAgainstConsolidatedSubsidiaryTextBlock = fact.value

			elif fact.concept.qname.localName == 'DecisionOnShareExchangeOfConsolidatedSubsidiaryTextBlock': #連結子会社の株式交換の決定 [テキストブロック]
				self.DecisionOnShareExchangeOfConsolidatedSubsidiaryTextBlock = fact.value

			elif fact.concept.qname.localName == 'DecisionOnShareTransferOfConsolidatedSubsidiaryTextBlock': #連結子会社の株式移転の決定 [テキストブロック]
				self.DecisionOnShareTransferOfConsolidatedSubsidiaryTextBlock = fact.value

			elif fact.concept.qname.localName == 'DecisionOnAbsorptionTypeSplitOfConsolidatedSubsidiaryTextBlock': #連結子会社の吸収分割の決定 [テキストブロック]
				self.DecisionOnAbsorptionTypeSplitOfConsolidatedSubsidiaryTextBlock = fact.value

			elif fact.concept.qname.localName == 'DecisionOnIncorporationTypeSplitOfConsolidatedSubsidiaryTextBlock': #連結子会社の新設分割の決定 [テキストブロック]
				self.DecisionOnIncorporationTypeSplitOfConsolidatedSubsidiaryTextBlock = fact.value

			elif fact.concept.qname.localName == 'DecisionOnAbsorptionTypeMergerOfConsolidatedSubsidiaryTextBlock': #連結子会社の吸収合併の決定 [テキストブロック]
				self.DecisionOnAbsorptionTypeMergerOfConsolidatedSubsidiaryTextBlock = fact.value

			elif fact.concept.qname.localName == 'DecisionOnConsolidationTypeMergerOfConsolidatedSubsidiaryTextBlock': #連結子会社の新設合併の決定 [テキストブロック]
				self.DecisionOnConsolidationTypeMergerOfConsolidatedSubsidiaryTextBlock = fact.value

			elif fact.concept.qname.localName == 'DecisionOnTransferOrAcquisitionOfBusinessOfConsolidatedSubsidiaryTextBlock': #連結子会社の事業の譲渡又は譲受けの決定 [テキストブロック]
				self.DecisionOnTransferOrAcquisitionOfBusinessOfConsolidatedSubsidiaryTextBlock = fact.value

			elif fact.concept.qname.localName == 'DecisionOnAcquisitionOfSubsidiaryByConsolidatedSubsidiaryTextBlock': #連結子会社による子会社取得の決定 [テキストブロック]
				self.DecisionOnAcquisitionOfSubsidiaryByConsolidatedSubsidiaryTextBlock = fact.value

			elif fact.concept.qname.localName == 'PetitionForCommencementOfBankruptcyProceedingsAgainstConsolidatedSubsidiaryTextBlock': #連結子会社に係る破産手続開始の申立て等 [テキストブロック]
				self.PetitionForCommencementOfBankruptcyProceedingsAgainstConsolidatedSubsidiaryTextBlock = fact.value

			elif fact.concept.qname.localName == 'LikelihoodOfUncollectibleOrDelinquentAccountsOfConsolidatedSubsidiaryTextBlock': #連結子会社に係る取立不能又は取立遅延債権のおそれ [テキストブロック]
				self.LikelihoodOfUncollectibleOrDelinquentAccountsOfConsolidatedSubsidiaryTextBlock = fact.value

			elif fact.concept.qname.localName == 'EventWithSignificantEffectsOnFinancialPositionBusinessPerformanceAndCashFlowsOfGroupTextBlock': #連結会社の財政状態、経営成績及びキャッシュ・フローの状況に著しい影響を与える事象 [テキストブロック]
				self.EventWithSignificantEffectsOnFinancialPositionBusinessPerformanceAndCashFlowsOfGroupTextBlock = fact.value

			elif fact.concept.qname.localName == 'NewMattersOrChangesInPublicOfferingInformationThroughToLastDayBeforeIPOTextBlock': #新規上場等の前日までにおける株式公開情報の発生又は変更 [テキストブロック]
				self.NewMattersOrChangesInPublicOfferingInformationThroughToLastDayBeforeIPOTextBlock = fact.value


	def getCabinetOfficeOrdinanceOnDisclosureOfCorporateInformationEtcFormNo53ExtraordinarySecuritiesReportHeading(self): #企業内容等の開示に関する内閣府令 第五号の三様式 臨時報告書 [目次項目]
		return self.CabinetOfficeOrdinanceOnDisclosureOfCorporateInformationEtcFormNo53ExtraordinarySecuritiesReportHeading

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

	def getCompanyNameCoverPage(self): #会社名、表紙
		return self.CompanyNameCoverPage

	def getCompanyNameInEnglishCoverPage(self): #英訳名、表紙
		return self.CompanyNameInEnglishCoverPage

	def getTitleAndNameOfRepresentativeCoverPage(self): #代表者の役職氏名、表紙
		return self.TitleAndNameOfRepresentativeCoverPage

	def getAddressOfRegisteredHeadquarterCoverPage(self): #本店の所在の場所、表紙
		return self.AddressOfRegisteredHeadquarterCoverPage

	def getTelephoneNumberCoverPage(self): #電話番号、表紙
		return self.TelephoneNumberCoverPage

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

	def getReasonForFilingHeading(self): #提出理由 [目次項目]
		return self.ReasonForFilingHeading

	def getReasonForFilingTextBlock(self): #提出理由 [テキストブロック]
		return self.ReasonForFilingTextBlock

	def getBodyOfReportHeading(self): #報告内容 [目次項目]
		return self.BodyOfReportHeading

	def getPublicOfferingOrSecondaryDistributionOfSecuritiesOutsideJapanTextBlock(self): #本邦以外の地域における有価証券の募集又は売出 [テキストブロック]
		return self.PublicOfferingOrSecondaryDistributionOfSecuritiesOutsideJapanTextBlock

	def getPrivatePlacementOfSecuritiesTextBlock(self): #有価証券の私募等による発行 [テキストブロック]
		return self.PrivatePlacementOfSecuritiesTextBlock

	def getIssueOfStockOptionsNotSubjectToSecuritiesRegistrationTextBlock(self): #届出を要しない株券等又は新株予約権証券等の発行 [テキストブロック]
		return self.IssueOfStockOptionsNotSubjectToSecuritiesRegistrationTextBlock

	def getChangesInParentCompaniesOrSpecifiedSubsidiariesTextBlock(self): #親会社又は特定子会社の異動 [テキストブロック]
		return self.ChangesInParentCompaniesOrSpecifiedSubsidiariesTextBlock

	def getChangesInMajorShareholderTextBlock(self): #主要株主の異動 [テキストブロック]
		return self.ChangesInMajorShareholderTextBlock

	def getNotificationOfRequestForSaleOfSharesFromSpecialControllingShareholdersOrDecisionOnWhetherToApproveRequestForSaleOfSharesOrNotTextBlock(self): #特別支配株主から株式等売渡請求の通知がされた場合又は当該株式等売渡請求を承認するか否かが決定された場合 [テキストブロック]
		return self.NotificationOfRequestForSaleOfSharesFromSpecialControllingShareholdersOrDecisionOnWhetherToApproveRequestForSaleOfSharesOrNotTextBlock

	def getDecisionOnHoldingShareholdersMeetingToAcquireAllClassSharesSubjectToWhollyCallTextBlock(self): #全部取得条項付種類株式の全部の取得を目的とする株主総会の招集の決定 [テキストブロック]
		return self.DecisionOnHoldingShareholdersMeetingToAcquireAllClassSharesSubjectToWhollyCallTextBlock

	def getDecisionOnHoldingShareholdersMeetingForPurposeOfReverseStockSplitTextBlock(self): #株式の併合を目的とする株主総会の招集の決定 [テキストブロック]
		return self.DecisionOnHoldingShareholdersMeetingForPurposeOfReverseStockSplitTextBlock

	def getSignificantDisasterTextBlock(self): #重要な災害の発生 [テキストブロック]
		return self.SignificantDisasterTextBlock

	def getCommencementOrResolutionOfLitigationTextBlock(self): #訴訟の提起又は解決 [テキストブロック]
		return self.CommencementOrResolutionOfLitigationTextBlock

	def getDecisionOnShareExchangeTextBlock(self): #株式交換の決定 [テキストブロック]
		return self.DecisionOnShareExchangeTextBlock

	def getDecisionOnShareTransferTextBlock(self): #株式移転の決定 [テキストブロック]
		return self.DecisionOnShareTransferTextBlock

	def getDecisionOnAbsorptionTypeSplitTextBlock(self): #吸収分割の決定 [テキストブロック]
		return self.DecisionOnAbsorptionTypeSplitTextBlock

	def getDecisionOnIncorporationTypeSplitTextBlock(self): #新設分割の決定 [テキストブロック]
		return self.DecisionOnIncorporationTypeSplitTextBlock

	def getDecisionOnAbsorptionTypeMergerTextBlock(self): #吸収合併の決定 [テキストブロック]
		return self.DecisionOnAbsorptionTypeMergerTextBlock

	def getDecisionOnConsolidationTypeMergerTextBlock(self): #新設合併の決定 [テキストブロック]
		return self.DecisionOnConsolidationTypeMergerTextBlock

	def getDecisionOnTransferOrAcquisitionOfBusinessTextBlock(self): #事業の譲渡又は譲受けの決定 [テキストブロック]
		return self.DecisionOnTransferOrAcquisitionOfBusinessTextBlock

	def getDecisionOnAcquisitionOfSubsidiaryTextBlock(self): #子会社取得の決定 [テキストブロック]
		return self.DecisionOnAcquisitionOfSubsidiaryTextBlock

	def getChangesInRepresentativeDirectorsTextBlock(self): #代表取締役の異動 [テキストブロック]
		return self.ChangesInRepresentativeDirectorsTextBlock

	def getResolutionOfShareholdersMeetingTextBlock(self): #株主総会における決議 [テキストブロック]
		return self.ResolutionOfShareholdersMeetingTextBlock

	def getAmendmentOrRejectionByShareholdersMeetingTextBlock(self): #株主総会における修正又は否決 [テキストブロック]
		return self.AmendmentOrRejectionByShareholdersMeetingTextBlock

	def getChangeInIndependentAuditorsTextBlock(self): #監査公認会計士等の異動 [テキストブロック]
		return self.ChangeInIndependentAuditorsTextBlock

	def getPetitionEtcForCommencementOfBankruptcyProceedingsTextBlock(self): #破産手続開始の申立て等 [テキストブロック]
		return self.PetitionEtcForCommencementOfBankruptcyProceedingsTextBlock

	def getLikelihoodOfUncollectibleOrDelinquentAccountsTextBlock(self): #取立不能又は取立遅延債権のおそれ [テキストブロック]
		return self.LikelihoodOfUncollectibleOrDelinquentAccountsTextBlock

	def getEventWithSignificantEffectsOnFinancialPositionBusinessPerformanceAndCashFlowsTextBlock(self): #財政状態、経営成績及びキャッシュ・フローの状況に著しい影響を与える事象 [テキストブロック]
		return self.EventWithSignificantEffectsOnFinancialPositionBusinessPerformanceAndCashFlowsTextBlock

	def getSignificantDisasterAffectingConsolidatedSubsidiaryTextBlock(self): #連結子会社に係る重要な災害の発生 [テキストブロック]
		return self.SignificantDisasterAffectingConsolidatedSubsidiaryTextBlock

	def getCommencementOrResolutionOfLitigationAgainstConsolidatedSubsidiaryTextBlock(self): #連結子会社に対する訴訟の提起又は解決 [テキストブロック]
		return self.CommencementOrResolutionOfLitigationAgainstConsolidatedSubsidiaryTextBlock

	def getDecisionOnShareExchangeOfConsolidatedSubsidiaryTextBlock(self): #連結子会社の株式交換の決定 [テキストブロック]
		return self.DecisionOnShareExchangeOfConsolidatedSubsidiaryTextBlock

	def getDecisionOnShareTransferOfConsolidatedSubsidiaryTextBlock(self): #連結子会社の株式移転の決定 [テキストブロック]
		return self.DecisionOnShareTransferOfConsolidatedSubsidiaryTextBlock

	def getDecisionOnAbsorptionTypeSplitOfConsolidatedSubsidiaryTextBlock(self): #連結子会社の吸収分割の決定 [テキストブロック]
		return self.DecisionOnAbsorptionTypeSplitOfConsolidatedSubsidiaryTextBlock

	def getDecisionOnIncorporationTypeSplitOfConsolidatedSubsidiaryTextBlock(self): #連結子会社の新設分割の決定 [テキストブロック]
		return self.DecisionOnIncorporationTypeSplitOfConsolidatedSubsidiaryTextBlock

	def getDecisionOnAbsorptionTypeMergerOfConsolidatedSubsidiaryTextBlock(self): #連結子会社の吸収合併の決定 [テキストブロック]
		return self.DecisionOnAbsorptionTypeMergerOfConsolidatedSubsidiaryTextBlock

	def getDecisionOnConsolidationTypeMergerOfConsolidatedSubsidiaryTextBlock(self): #連結子会社の新設合併の決定 [テキストブロック]
		return self.DecisionOnConsolidationTypeMergerOfConsolidatedSubsidiaryTextBlock

	def getDecisionOnTransferOrAcquisitionOfBusinessOfConsolidatedSubsidiaryTextBlock(self): #連結子会社の事業の譲渡又は譲受けの決定 [テキストブロック]
		return self.DecisionOnTransferOrAcquisitionOfBusinessOfConsolidatedSubsidiaryTextBlock

	def getDecisionOnAcquisitionOfSubsidiaryByConsolidatedSubsidiaryTextBlock(self): #連結子会社による子会社取得の決定 [テキストブロック]
		return self.DecisionOnAcquisitionOfSubsidiaryByConsolidatedSubsidiaryTextBlock

	def getPetitionForCommencementOfBankruptcyProceedingsAgainstConsolidatedSubsidiaryTextBlock(self): #連結子会社に係る破産手続開始の申立て等 [テキストブロック]
		return self.PetitionForCommencementOfBankruptcyProceedingsAgainstConsolidatedSubsidiaryTextBlock

	def getLikelihoodOfUncollectibleOrDelinquentAccountsOfConsolidatedSubsidiaryTextBlock(self): #連結子会社に係る取立不能又は取立遅延債権のおそれ [テキストブロック]
		return self.LikelihoodOfUncollectibleOrDelinquentAccountsOfConsolidatedSubsidiaryTextBlock

	def getEventWithSignificantEffectsOnFinancialPositionBusinessPerformanceAndCashFlowsOfGroupTextBlock(self): #連結会社の財政状態、経営成績及びキャッシュ・フローの状況に著しい影響を与える事象 [テキストブロック]
		return self.EventWithSignificantEffectsOnFinancialPositionBusinessPerformanceAndCashFlowsOfGroupTextBlock

	def getNewMattersOrChangesInPublicOfferingInformationThroughToLastDayBeforeIPOTextBlock(self): #新規上場等の前日までにおける株式公開情報の発生又は変更 [テキストブロック]
		return self.NewMattersOrChangesInPublicOfferingInformationThroughToLastDayBeforeIPOTextBlock
