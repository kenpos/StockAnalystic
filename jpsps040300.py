from arelle import ModelManager
from arelle import Cntlr

class jpsps040300:#特定有価証券の内容等の開示に関する内閣府令 第四号の三様式 有価証券届出書
	CabinetOfficeOrdinanceOnDisclosureOfInformationEtcOnSpecifiedSecuritiesFormNo43SecuritiesRegistrationStatementHeading = '' #特定有価証券の内容等の開示に関する内閣府令 第四号の三様式 有価証券届出書 [目次項目]
	CoverPageHeading = '' #表紙 [目次項目]
	CoverPageHeading = '' #表紙 [目次項目]
	DocumentTitleCoverPage = '' #提出書類、表紙
	PlaceOfFilingCoverPage = '' #提出先、表紙
	FilingDateCoverPage = '' #提出日、表紙
	IssuerNameCoverPage = '' #発行者名、表紙
	TitleAndNameOfRepresentativeCoverPage = '' #代表者の役職氏名、表紙
	AddressOfRegisteredHeadquarterCoverPage = '' #本店の所在の場所、表紙
	NameOfContactPersonCoverPage = '' #事務連絡者氏名、表紙
	TelephoneNumberCoverPage = '' #電話番号、表紙
	NameOfInvestmentCorporationRelatedToDomesticInvestmentSecuritiesToRegisterForOfferingOrDistributionCoverPage = '' #届出の対象とした募集（売出）内国投資証券に係る投資法人の名称、表紙
	LegalFormAndAmountOfDomesticInvestmentSecuritiesToRegisterForOfferingOrDistributionCoverPageTextBlock = '' #届出の対象とした募集（売出）内国投資証券の形態及び金額、表紙 [テキストブロック]
	PlaceForPublicInspectionCoverPageTextBlock = '' #縦覧に供する場所、表紙 [テキストブロック]
	SecurityInformationHeading = '' #証券情報 [目次項目]
	DomesticInvestmentSecuritiesOtherThanInvestmentCorporationBondsHeading = '' #内国投資証券（新投資口予約権証券及び投資法人債券を除く。） [目次項目]
	DomesticInvestmentSecuritiesOtherThanInvestmentUnitAcquisitionRightsAndInvestmentCorporationBondsTextBlock = '' #内国投資証券（新投資口予約権証券及び投資法人債券を除く。） [テキストブロック]
	PublicOfferingOfDomesticInvestmentSecuritiesHeading = '' #募集内国投資証券 [目次項目]
	NameOfInvestmentCorporationPublicOfferingOfDomesticInvestmentSecuritiesHeading = '' #投資法人の名称、募集内国投資証券 [目次項目]
	NameOfInvestmentCorporationPublicOfferingOfDomesticInvestmentSecuritiesTextBlock = '' #投資法人の名称、募集内国投資証券 [テキストブロック]
	LegalFormEtcOfDomesticInvestmentSecuritiesPublicOfferingOfDomesticInvestmentSecuritiesHeading = '' #内国投資証券の形態等、募集内国投資証券 [目次項目]
	LegalFormEtcOfDomesticInvestmentSecuritiesPublicOfferingOfDomesticInvestmentSecuritiesTextBlock = '' #内国投資証券の形態等、募集内国投資証券 [テキストブロック]
	NumberOfSecuritiesToBeIssuedPublicOfferingOfDomesticInvestmentSecuritiesHeading = '' #発行数、募集内国投資証券 [目次項目]
	NumberOfSecuritiesToBeIssuedPublicOfferingOfDomesticInvestmentSecuritiesTextBlock = '' #発行数、募集内国投資証券 [テキストブロック]
	TotalAmountOfIssuePublicOfferingOfDomesticInvestmentSecuritiesHeading = '' #発行価額の総額、募集内国投資証券 [目次項目]
	TotalAmountOfIssuePublicOfferingOfDomesticInvestmentSecuritiesTextBlock = '' #発行価額の総額、募集内国投資証券 [テキストブロック]
	PriceOfIssuePublicOfferingOfDomesticInvestmentSecuritiesHeading = '' #発行価格、募集内国投資証券 [目次項目]
	PriceOfIssuePublicOfferingOfDomesticInvestmentSecuritiesTextBlock = '' #発行価格、募集内国投資証券 [テキストブロック]
	ApplicationFeePublicOfferingOfDomesticInvestmentSecuritiesHeading = '' #申込手数料、募集内国投資証券 [目次項目]
	ApplicationFeePublicOfferingOfDomesticInvestmentSecuritiesTextBlock = '' #申込手数料、募集内国投資証券 [テキストブロック]
	ApplicationUnitPublicOfferingOfDomesticInvestmentSecuritiesHeading = '' #申込単位、募集内国投資証券 [目次項目]
	ApplicationUnitPublicOfferingOfDomesticInvestmentSecuritiesTextBlock = '' #申込単位、募集内国投資証券 [テキストブロック]
	ApplicationPeriodPublicOfferingOfDomesticInvestmentSecuritiesHeading = '' #申込期間、募集内国投資証券 [目次項目]
	ApplicationPeriodPublicOfferingOfDomesticInvestmentSecuritiesTextBlock = '' #申込期間、募集内国投資証券 [テキストブロック]
	ApplicationMoneyPublicOfferingOfDomesticInvestmentSecuritiesHeading = '' #申込証拠金、募集内国投資証券 [目次項目]
	ApplicationMoneyPublicOfferingOfDomesticInvestmentSecuritiesTextBlock = '' #申込証拠金、募集内国投資証券 [テキストブロック]
	PlaceForApplicationPublicOfferingOfDomesticInvestmentSecuritiesHeading = '' #申込取扱場所、募集内国投資証券 [目次項目]
	PlaceForApplicationPublicOfferingOfDomesticInvestmentSecuritiesTextBlock = '' #申込取扱場所、募集内国投資証券 [テキストブロック]
	DueDateOfPaymentPublicOfferingOfDomesticInvestmentSecuritiesHeading = '' #払込期日、募集内国投資証券 [目次項目]
	DueDateOfPaymentPublicOfferingOfDomesticInvestmentSecuritiesTextBlock = '' #払込期日、募集内国投資証券 [テキストブロック]
	PlaceForPaymentPublicOfferingOfDomesticInvestmentSecuritiesHeading = '' #払込取扱場所、募集内国投資証券 [目次項目]
	PlaceForPaymentPublicOfferingOfDomesticInvestmentSecuritiesTextBlock = '' #払込取扱場所、募集内国投資証券 [テキストブロック]
	OverviewOfUnderwritingEtcPublicOfferingOfDomesticInvestmentSecuritiesHeading = '' #引受け等の概要、募集内国投資証券 [目次項目]
	OverviewOfUnderwritingEtcPublicOfferingOfDomesticInvestmentSecuritiesTextBlock = '' #引受け等の概要、募集内国投資証券 [テキストブロック]
	BookEntryTransferInstitutionPublicOfferingOfDomesticInvestmentSecuritiesHeading = '' #振替機関に関する事項、募集内国投資証券 [目次項目]
	BookEntryTransferInstitutionPublicOfferingOfDomesticInvestmentSecuritiesTextBlock = '' #振替機関に関する事項、募集内国投資証券 [テキストブロック]
	UseOfNetProceedsPublicOfferingOfDomesticInvestmentSecuritiesHeading = '' #手取金の使途、募集内国投資証券 [目次項目]
	UseOfNetProceedsPublicOfferingOfDomesticInvestmentSecuritiesTextBlock = '' #手取金の使途、募集内国投資証券 [テキストブロック]
	OtherInformationPublicOfferingOfDomesticInvestmentSecuritiesHeading = '' #その他、募集内国投資証券 [目次項目]
	OtherInformationPublicOfferingOfDomesticInvestmentSecuritiesTextBlock = '' #その他、募集内国投資証券 [テキストブロック]
	SecondaryDistributionOfDomesticInvestmentSecuritiesHeading = '' #売出内国投資証券 [目次項目]
	NameOfInvestmentCorporationSecondaryDistributionOfDomesticInvestmentSecuritiesHeading = '' #投資法人の名称、売出内国投資証券 [目次項目]
	NameOfInvestmentCorporationSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock = '' #投資法人の名称、売出内国投資証券 [テキストブロック]
	LegalFormEtcOfDomesticInvestmentSecuritiesSecondaryDistributionOfDomesticInvestmentSecuritiesHeading = '' #内国投資証券の形態等、売出内国投資証券 [目次項目]
	LegalFormEtcOfDomesticInvestmentSecuritiesSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock = '' #内国投資証券の形態等、売出内国投資証券 [テキストブロック]
	NumberOfSecuritiesToBeDistributedSecondaryDistributionOfDomesticInvestmentSecuritiesHeading = '' #売出数、売出内国投資証券 [目次項目]
	NumberOfSecuritiesToBeDistributedSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock = '' #売出数、売出内国投資証券 [テキストブロック]
	TotalAmountOfSecondaryDistributionSecondaryDistributionOfDomesticInvestmentSecuritiesHeading = '' #売出価額の総額、売出内国投資証券 [目次項目]
	TotalAmountOfSecondaryDistributionSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock = '' #売出価額の総額、売出内国投資証券 [テキストブロック]
	PriceOfSecondaryDistributionSecondaryDistributionOfDomesticInvestmentSecuritiesHeading = '' #売出価格、売出内国投資証券 [目次項目]
	PriceOfSecondaryDistributionSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock = '' #売出価格、売出内国投資証券 [テキストブロック]
	ApplicationFeeSecondaryDistributionOfDomesticInvestmentSecuritiesHeading = '' #申込手数料、売出内国投資証券 [目次項目]
	ApplicationFeeSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock = '' #申込手数料、売出内国投資証券 [テキストブロック]
	ApplicationUnitSecondaryDistributionOfDomesticInvestmentSecuritiesHeading = '' #申込単位、売出内国投資証券 [目次項目]
	ApplicationUnitSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock = '' #申込単位、売出内国投資証券 [テキストブロック]
	ApplicationPeriodSecondaryDistributionOfDomesticInvestmentSecuritiesHeading = '' #申込期間、売出内国投資証券 [目次項目]
	ApplicationPeriodSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock = '' #申込期間、売出内国投資証券 [テキストブロック]
	ApplicationMoneySecondaryDistributionOfDomesticInvestmentSecuritiesHeading = '' #申込証拠金、売出内国投資証券 [目次項目]
	ApplicationMoneySecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock = '' #申込証拠金、売出内国投資証券 [テキストブロック]
	PlaceForApplicationSecondaryDistributionOfDomesticInvestmentSecuritiesHeading = '' #申込取扱場所、売出内国投資証券 [目次項目]
	PlaceForApplicationSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock = '' #申込取扱場所、売出内国投資証券 [テキストブロック]
	SettlementDateSecondaryDistributionOfDomesticInvestmentSecuritiesHeading = '' #受渡期日、売出内国投資証券 [目次項目]
	SettlementDateSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock = '' #受渡期日、売出内国投資証券 [テキストブロック]
	PlaceForPaymentSecondaryDistributionOfDomesticInvestmentSecuritiesHeading = '' #払込取扱場所、売出内国投資証券 [目次項目]
	PlaceForPaymentSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock = '' #払込取扱場所、売出内国投資証券 [テキストブロック]
	OverviewOfUnderwritingEtcSecondaryDistributionOfDomesticInvestmentSecuritiesHeading = '' #引受け等の概要、売出内国投資証券 [目次項目]
	OverviewOfUnderwritingEtcSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock = '' #引受け等の概要、売出内国投資証券 [テキストブロック]
	BookEntryTransferInstitutionSecondaryDistributionOfDomesticInvestmentSecuritiesHeading = '' #振替機関に関する事項、売出内国投資証券 [目次項目]
	BookEntryTransferInstitutionSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock = '' #振替機関に関する事項、売出内国投資証券 [テキストブロック]
	UseOfNetProceedsSecondaryDistributionOfDomesticInvestmentSecuritiesHeading = '' #手取金の使途、売出内国投資証券 [目次項目]
	UseOfNetProceedsSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock = '' #手取金の使途、売出内国投資証券 [テキストブロック]
	OtherInformationSecondaryDistributionOfDomesticInvestmentSecuritiesHeading = '' #その他、売出内国投資証券 [目次項目]
	OtherInformationSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock = '' #その他、売出内国投資証券 [テキストブロック]
	SubscriptionRightsToSharesOfInvestmentCorporationHeading = '' #新投資口予約権証券 [目次項目]
	InvestmentUnitAcquisitionRightsTextBlock = '' #新投資口予約権証券 [テキストブロック]
	NameOfInvestmentCorporationSubscriptionRightsToSharesOfInvestmentCorporationHeading = '' #投資法人の名称、新投資口予約権証券 [目次項目]
	NameOfInvestmentCorporationSubscriptionRightsToSharesOfInvestmentCorporationTextBlock = '' #投資法人の名称、新投資口予約権証券 [テキストブロック]
	LegalFormEtcOfSubscriptionRightsToSharesOfInvestmentCorporationHeading = '' #新投資口予約権証券の形態等 [目次項目]
	LegalFormEtcOfSubscriptionRightsToSharesOfInvestmentCorporationTextBlock = '' #新投資口予約権証券の形態等 [テキストブロック]
	NumberOfSecuritiesToBeIssuedSubscriptionRightsToSharesOfInvestmentCorporationHeading = '' #発行数、新投資口予約権証券 [目次項目]
	NumberOfSecuritiesToBeIssuedSubscriptionRightsToSharesOfInvestmentCorporationTextBlock = '' #発行数、新投資口予約権証券 [テキストブロック]
	DateOfAllotmentSubscriptionRightsToSharesOfInvestmentCorporationHeading = '' #割当日、新投資口予約権証券 [目次項目]
	DateOfAllotmentSubscriptionRightsToSharesOfInvestmentCorporationTextBlock = '' #割当日、新投資口予約権証券 [テキストブロック]
	ParticularsOfSubscriptionRightsToSharesOfInvestmentCorporationHeading = '' #新投資口予約権の内容 [目次項目]
	ParticularsOfSubscriptionRightsToSharesOfInvestmentCorporationTextBlock = '' #新投資口予約権の内容 [テキストブロック]
	LegalFormEtcOfDomesticInvestmentSecuritiesUnderlyingSubscriptionRightsToSharesOfInvestmentCorporationHeading = '' #新投資口予約権の目的となる内国投資証券の形態等 [目次項目]
	LegalFormEtcOfDomesticInvestmentSecuritiesUnderlyingSubscriptionRightsToSharesOfInvestmentCorporationTextBlock = '' #新投資口予約権の目的となる内国投資証券の形態等 [テキストブロック]
	NumberOfDomesticInvestmentSecuritiesUnderlyingSubscriptionRightsToSharesOfInvestmentCorporationHeading = '' #新投資口予約権の目的となる内国投資証券の数 [目次項目]
	NumberOfDomesticInvestmentSecuritiesUnderlyingSubscriptionRightsToSharesOfInvestmentCorporationTextBlock = '' #新投資口予約権の目的となる内国投資証券の数 [テキストブロック]
	AmountOfPaymentWhenSubscriptionRightToShareOfInvestmentCorporationIsExercisedHeading = '' #新投資口予約権の行使時の払込金額 [目次項目]
	AmountOfPaymentWhenSubscriptionRightToShareOfInvestmentCorporationIsExercisedTextBlock = '' #新投資口予約権の行使時の払込金額 [テキストブロック]
	TotalAmountOfDomesticInvestmentSecuritiesToBeIssuedWhenSubscriptionRightsToSharesOfInvestmentCorporationAreExercisedHeading = '' #新投資口予約権の行使により発行する内国投資証券の発行価額の総額 [目次項目]
	TotalAmountOfDomesticInvestmentSecuritiesToBeIssuedWhenSubscriptionRightsToSharesOfInvestmentCorporationAreExercisedTextBlock = '' #新投資口予約権の行使により発行する内国投資証券の発行価額の総額 [テキストブロック]
	ExercisePeriodOfSubscriptionRightsToSharesOfInvestmentCorporationHeading = '' #新投資口予約権の行使期間 [目次項目]
	ExercisePeriodOfSubscriptionRightsToSharesOfInvestmentCorporationTextBlock = '' #新投資口予約権の行使期間 [テキストブロック]
	CustodianAgentAndPlaceOfPaymentForExerciseOfSubscriptionRightsToSharesOfInvestmentCorporationHeading = '' #新投資口予約権の行使請求の受付場所、取次場所及び払込取扱場所 [目次項目]
	CustodianAgentAndPlaceOfPaymentForExerciseOfSubscriptionRightsToSharesOfInvestmentCorporationTextBlock = '' #新投資口予約権の行使請求の受付場所、取次場所及び払込取扱場所 [テキストブロック]
	TermsOfExerciseOfSubscriptionRightsToSharesOfInvestmentCorporationHeading = '' #新投資口予約権の行使の条件 [目次項目]
	TermsOfExerciseOfSubscriptionRightsToSharesOfInvestmentCorporationTextBlock = '' #新投資口予約権の行使の条件 [テキストブロック]
	ReasonAndTermsOfAcquisitionOfTreasurySubscriptionRightsToSharesOfInvestmentCorporationHeading = '' #自己新投資口予約権の取得の事由及び取得の条件 [目次項目]
	ReasonAndTermsOfAcquisitionOfTreasurySubscriptionRightsToSharesOfInvestmentCorporationTextBlock = '' #自己新投資口予約権の取得の事由及び取得の条件 [テキストブロック]
	InformationAboutTransferOfSubscriptionRightsToSharesOfInvestmentCorporationHeading = '' #新投資口予約権の譲渡に関する事項 [目次項目]
	InformationAboutTransferOfSubscriptionRightsToSharesOfInvestmentCorporationTextBlock = '' #新投資口予約権の譲渡に関する事項 [テキストブロック]
	OverviewOfUnderwritingEtcSubscriptionRightsToSharesOfInvestmentCorporationHeading = '' #引受け等の概要、新投資口予約権証券 [目次項目]
	OverviewOfUnderwritingEtcSubscriptionRightsToSharesOfInvestmentCorporationTextBlock = '' #引受け等の概要、新投資口予約権証券 [テキストブロック]
	BookEntryTransferInstitutionSubscriptionRightsToSharesOfInvestmentCorporationHeading = '' #振替機関に関する事項、新投資口予約権証券 [目次項目]
	BookEntryTransferInstitutionSubscriptionRightsToSharesOfInvestmentCorporationTextBlock = '' #振替機関に関する事項、新投資口予約権証券 [テキストブロック]
	UseOfNetProceedsSubscriptionRightsToSharesOfInvestmentCorporationHeading = '' #手取金の使途、新投資口予約権証券 [目次項目]
	UseOfNetProceedsSubscriptionRightsToSharesOfInvestmentCorporationTextBlock = '' #手取金の使途、新投資口予約権証券 [テキストブロック]
	OtherInformationSubscriptionRightsToSharesOfInvestmentCorporationHeading = '' #その他、新投資口予約権証券 [目次項目]
	OtherInformationSubscriptionRightsToSharesOfInvestmentCorporationTextBlock = '' #その他、新投資口予約権証券 [テキストブロック]
	InvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading = '' #投資法人債券（短期投資法人債を除く。） [目次項目]
	InvestmentCorporationBondsOtherThanShortTermOnesTextBlock = '' #投資法人債券（短期投資法人債を除く。） [テキストブロック]
	SecurityTitlesHeading = '' #銘柄 [目次項目]
	SecurityTitlesTextBlock = '' #銘柄 [テキストブロック]
	LegalFormEtcOfInvestmentCorporationBondsHeading = '' #投資法人債券の形態等 [目次項目]
	LegalFormEtcOfInvestmentCorporationBondsTextBlock = '' #投資法人債券の形態等 [テキストブロック]
	TotalFaceValueHeading = '' #券面総額 [目次項目]
	TotalFaceValueTextBlock = '' #券面総額 [テキストブロック]
	AmountOfEachOfInvestmentCorporationBondsHeading = '' #各投資法人債の金額 [目次項目]
	AmountOfEachOfInvestmentCorporationBondsTextBlock = '' #各投資法人債の金額 [テキストブロック]
	TotalAmountOfIssueOrSecondaryDistributionInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading = '' #発行（売出）価額の総額、投資法人債券（短期投資法人債を除く。） [目次項目]
	TotalAmountOfIssueOrSecondaryDistributionInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock = '' #発行（売出）価額の総額、投資法人債券（短期投資法人債を除く。） [テキストブロック]
	PriceOfIssueOrSecondaryDistributionInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading = '' #発行（売出）価格、投資法人債券（短期投資法人債を除く。） [目次項目]
	PriceOfIssueOrSecondaryDistributionInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock = '' #発行（売出）価格、投資法人債券（短期投資法人債を除く。） [テキストブロック]
	InterestRateHeading = '' #利率 [目次項目]
	InterestRateTextBlock = '' #利率 [テキストブロック]
	DateAndMethodOfInterestPaymentHeading = '' #利払日及び利息支払の方法 [目次項目]
	DateAndMethodOfInterestPaymentTextBlock = '' #利払日及び利息支払の方法 [テキストブロック]
	DateAndMethodOfRedemptionHeading = '' #償還期限及び償還の方法 [目次項目]
	DateAndMethodOfRedemptionTextBlock = '' #償還期限及び償還の方法 [テキストブロック]
	MethodOfPublicOfferingInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading = '' #募集の方法、投資法人債券（短期投資法人債を除く。） [目次項目]
	MethodOfPublicOfferingInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock = '' #募集の方法、投資法人債券（短期投資法人債を除く。） [テキストブロック]
	ApplicationMoneyInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading = '' #申込証拠金、投資法人債券（短期投資法人債を除く。） [目次項目]
	ApplicationMoneyInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock = '' #申込証拠金、投資法人債券（短期投資法人債を除く。） [テキストブロック]
	ApplicationPeriodInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading = '' #申込期間、投資法人債券（短期投資法人債を除く。） [目次項目]
	ApplicationPeriodInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock = '' #申込期間、投資法人債券（短期投資法人債を除く。） [テキストブロック]
	PlaceForApplicationInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading = '' #申込取扱場所、投資法人債券（短期投資法人債を除く。） [目次項目]
	PlaceForApplicationInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock = '' #申込取扱場所、投資法人債券（短期投資法人債を除く。） [テキストブロック]
	DueDateOfPaymentInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading = '' #払込期日、投資法人債券（短期投資法人債を除く。） [目次項目]
	DueDateOfPaymentInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock = '' #払込期日、投資法人債券（短期投資法人債を除く。） [テキストブロック]
	PlaceForPaymentInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading = '' #払込取扱場所、投資法人債券（短期投資法人債を除く。） [目次項目]
	PlaceForPaymentInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock = '' #払込取扱場所、投資法人債券（短期投資法人債を除く。） [テキストブロック]
	OverviewOfUnderwritingEtcInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading = '' #引受け等の概要、投資法人債券（短期投資法人債を除く。） [目次項目]
	OverviewOfUnderwritingEtcInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock = '' #引受け等の概要、投資法人債券（短期投資法人債を除く。） [テキストブロック]
	AdministratorOfInvestmentCorporationBondsHeading = '' #投資法人債管理者又は投資法人債の管理会社 [目次項目]
	AdministratorOfInvestmentCorporationBondsTextBlock = '' #投資法人債管理者又は投資法人債の管理会社 [テキストブロック]
	BookEntryTransferInstitutionInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading = '' #振替機関に関する事項、投資法人債券（短期投資法人債を除く。） [目次項目]
	BookEntryTransferInstitutionInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock = '' #振替機関に関する事項、投資法人債券（短期投資法人債を除く。） [テキストブロック]
	RegistrationDateAndRegistrationNumberOfInvestmentCorporationHeading = '' #投資法人の登録年月日及び登録番号 [目次項目]
	RegistrationDateAndRegistrationNumberOfInvestmentCorporationTextBlock = '' #投資法人の登録年月日及び登録番号 [テキストブロック]
	UseOfNetProceedsInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading = '' #手取金の使途、投資法人債券（短期投資法人債を除く。） [目次項目]
	UseOfNetProceedsInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock = '' #手取金の使途、投資法人債券（短期投資法人債を除く。） [テキストブロック]
	OtherInformationInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading = '' #その他、投資法人債券（短期投資法人債を除く。） [目次項目]
	OtherInformationInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock = '' #その他、投資法人債券（短期投資法人債を除く。） [テキストブロック]
	ShortTermInvestmentCorporationBondsHeading = '' #短期投資法人債 [目次項目]
	ShortTermInvestmentCorporationBondsTextBlock = '' #短期投資法人債 [テキストブロック]
	TotalAmountOfIssueOrSecondaryDistributionOfShortTermInvestmentCorporationBondsHeading = '' #発行（売出）短期投資法人債の総額 [目次項目]
	TotalAmountOfIssueOrSecondaryDistributionOfShortTermInvestmentCorporationBondsTextBlock = '' #発行（売出）短期投資法人債の総額 [テキストブロック]
	TotalAmountOfIssueOrSecondaryDistributionShortTermInvestmentCorporationBondsHeading = '' #発行（売出）価額の総額、短期投資法人債 [目次項目]
	TotalAmountOfIssueOrSecondaryDistributionShortTermInvestmentCorporationBondsTextBlock = '' #発行（売出）価額の総額、短期投資法人債 [テキストブロック]
	PriceOfIssueOrSecondaryDistributionShortTermInvestmentCorporationBondsHeading = '' #発行（売出）価格、短期投資法人債 [目次項目]
	PriceOfIssueOrSecondaryDistributionShortTermInvestmentCorporationBondsTextBlock = '' #発行（売出）価格、短期投資法人債 [テキストブロック]
	LimitOnAmountOfIssueHeading = '' #発行限度額 [目次項目]
	LimitOnAmountOfIssueTextBlock = '' #発行限度額 [テキストブロック]
	RemainingBalanceOfLimitOnAmountOfIssueHeading = '' #発行限度額残高 [目次項目]
	RemainingBalanceOfLimitOnAmountOfIssueTextBlock = '' #発行限度額残高 [テキストブロック]
	DueDateOfPaymentHeading = '' #支払期日 [目次項目]
	DueDateOfPaymentTextBlock = '' #支払期日 [テキストブロック]
	PlaceForPaymentHeading = '' #支払場所 [目次項目]
	PlaceForPaymentTextBlock = '' #支払場所 [テキストブロック]
	BookEntryTransferInstitutionShortTermInvestmentCorporationBondsHeading = '' #振替機関に関する事項、短期投資法人債 [目次項目]
	BookEntryTransferInstitutionShortTermInvestmentCorporationBondsTextBlock = '' #振替機関に関する事項、短期投資法人債 [テキストブロック]
	FinancialInstitutionProvidingBackupLineHeading = '' #バックアップラインの設定金融機関 [目次項目]
	FinancialInstitutionProvidingBackupLineTextBlock = '' #バックアップラインの設定金融機関 [テキストブロック]
	DescriptionOfBackupLineHeading = '' #バックアップラインの設定内容 [目次項目]
	DescriptionOfBackupLineTextBlock = '' #バックアップラインの設定内容 [テキストブロック]
	RatingHeading = '' #取得格付 [目次項目]
	RatingTextBlock = '' #取得格付 [テキストブロック]
	SpecialDisclosureAboutPublicOfferingOrSecondaryDistributionHeading = '' #募集又は売出しに関する特別記載事項 [目次項目]
	SpecialDisclosureAboutPublicOfferingOrSecondaryDistributionTextBlock = '' #募集又は売出しに関する特別記載事項 [テキストブロック]
	FundInformationHeading = '' #ファンド情報 [目次項目]
	OverviewOfFundHeading = '' #ファンドの状況 [目次項目]
	OverviewOfInvestmentCorporationHeading = '' #投資法人の概況 [目次項目]
	SummaryOfBusinessResultsHeading = '' #主要な経営指標等の推移 [目次項目]
	SummaryOfBusinessResultsTextBlock = '' #主要な経営指標等の推移 [テキストブロック]
	PurposesAndBasicFeaturesOfInvestmentCorporationHeading = '' #投資法人の目的及び基本的性格 [目次項目]
	PurposesAndBasicFeaturesOfInvestmentCorporationTextBlock = '' #投資法人の目的及び基本的性格 [テキストブロック]
	SchemeOfInvestmentCorporationHeading = '' #投資法人の仕組み [目次項目]
	SchemeOfInvestmentCorporationTextBlock = '' #投資法人の仕組み [テキストブロック]
	OrganizationOfInvestmentCorporationHeading = '' #投資法人の機構 [目次項目]
	OrganizationOfInvestmentCorporationTextBlock = '' #投資法人の機構 [テキストブロック]
	PaidInCapitalOfInvestmentCorporationHeading = '' #投資法人の出資総額 [目次項目]
	PaidInCapitalOfInvestmentCorporationTextBlock = '' #投資法人の出資総額 [テキストブロック]
	MajorUnitholdersHeading = '' #主要な投資主の状況 [目次項目]
	MajorUnitholdersTextBlock = '' #主要な投資主の状況 [テキストブロック]
	ShareOwnershipProgramForEmployeesOfAssetManagementCompanyHeading = '' #資産運用会社従業員等投資口所有制度の内容 [目次項目]
	ShareOwnershipProgramForEmployeesOfAssetManagementCompanyTextBlock = '' #資産運用会社従業員等投資口所有制度の内容 [テキストブロック]
	InvestmentPolicyOverviewOfFundHeading = '' #投資方針、ファンドの状況 [目次項目]
	InvestmentPolicyHeading = '' #投資方針 [目次項目]
	InvestmentPolicyTextBlock = '' #投資方針 [テキストブロック]
	ThingsToInvestInHeading = '' #投資対象 [目次項目]
	ThingsToInvestInTextBlock = '' #投資対象 [テキストブロック]
	ProfitDistributionPolicyHeading = '' #分配方針 [目次項目]
	ProfitDistributionPolicyTextBlock = '' #分配方針 [テキストブロック]
	RestrictionsOnInvestmentHeading = '' #投資制限 [目次項目]
	RestrictionsOnInvestmentTextBlock = '' #投資制限 [テキストブロック]
	InvestmentRisksHeading = '' #投資リスク [目次項目]
	InvestmentRisksTextBlock = '' #投資リスク [テキストブロック]
	FeesChargesAndTaxesHeading = '' #手数料等及び税金 [目次項目]
	ApplicationFeeOverviewOfFundHeading = '' #申込手数料、ファンドの状況 [目次項目]
	ApplicationFeeOverviewOfFundTextBlock = '' #申込手数料、ファンドの状況 [テキストブロック]
	RedemptionFeeInvestmentCorporationHeading = '' #買戻し手数料、投資法人 [目次項目]
	RedemptionFeeInvestmentCorporationTextBlock = '' #買戻し手数料、投資法人 [テキストブロック]
	AdministrationFeesAndChargesHeading = '' #管理報酬等 [目次項目]
	AdministrationFeesAndChargesTextBlock = '' #管理報酬等 [テキストブロック]
	OtherFeesAndChargesHeading = '' #その他の手数料等 [目次項目]
	OtherFeesAndChargesTextBlock = '' #その他の手数料等 [テキストブロック]
	TaxationHeading = '' #課税上の取扱い [目次項目]
	TaxationTextBlock = '' #課税上の取扱い [テキストブロック]
	StatusOfInvestmentManagementHeading = '' #運用状況 [目次項目]
	StatusOfInvestmentManagementTextBlock = '' #運用状況 [テキストブロック]
	StatusOfInvestmentHeading = '' #投資状況 [目次項目]
	StatusOfInvestmentTextBlock = '' #投資状況 [テキストブロック]
	InvestmentAssetsHeading = '' #投資資産 [目次項目]
	MajorComponentsOfInvestmentSecuritiesHeading = '' #投資有価証券の主要銘柄 [目次項目]
	MajorComponentsOfInvestmentSecuritiesTextBlock = '' #投資有価証券の主要銘柄 [テキストブロック]
	ComponentsOfRealEstateInvestmentsHeading = '' #投資不動産物件 [目次項目]
	ComponentsOfRealEstateInvestmentsTextBlock = '' #投資不動産物件 [テキストブロック]
	MajorComponentsOfOtherInvestmentsHeading = '' #その他投資資産の主要なもの [目次項目]
	MajorComponentsOfOtherInvestmentsTextBlock = '' #その他投資資産の主要なもの [テキストブロック]
	ActualPerformanceHeading = '' #運用実績 [目次項目]
	ChangesInNetAssetsEtcHeading = '' #純資産等の推移 [目次項目]
	ChangesInNetAssetsEtcTextBlock = '' #純資産等の推移 [テキストブロック]
	HistoricalRecordsOfProfitDistributionHeading = '' #分配の推移 [目次項目]
	HistoricalRecordsOfProfitDistributionTextBlock = '' #分配の推移 [テキストブロック]
	HistoricalRecordsOfROEHeading = '' #自己資本利益率（収益率）の推移 [目次項目]
	HistoricalRecordsOfROETextBlock = '' #自己資本利益率（収益率）の推移 [テキストブロック]
	OverviewOfProceduresEtcHeading = '' #手続等の概要 [目次項目]
	OverviewOfProceduresEtcTextBlock = '' #手続等の概要 [テキストブロック]
	OverviewOfAdministrationAndOperationHeading = '' #管理及び運営の概要 [目次項目]
	OverviewOfAdministrationAndOperationTextBlock = '' #管理及び運営の概要 [テキストブロック]
	FinancialHighlightsHeading = '' #財務ハイライト情報 [目次項目]
	BalanceSheetFinancialHighlightsHeading = '' #貸借対照表、財務ハイライト情報 [目次項目]
	BalanceSheetFinancialHighlightsTextBlock = '' #貸借対照表、財務ハイライト情報 [テキストブロック]
	StatementOfIncomeFinancialHighlightsHeading = '' #損益計算書、財務ハイライト情報 [目次項目]
	StatementOfIncomeFinancialHighlightsTextBlock = '' #損益計算書、財務ハイライト情報 [テキストブロック]
	StatementOfCashDistributionFinancialHighlightsHeading = '' #金銭の分配に係る計算書、財務ハイライト情報 [目次項目]
	StatementOfCashDistributionFinancialHighlightsTextBlock = '' #金銭の分配に係る計算書、財務ハイライト情報 [テキストブロック]
	StatementOfCashFlowsFinancialHighlightsHeading = '' #キャッシュ・フロー計算書、財務ハイライト情報 [目次項目]
	StatementOfCashFlowsFinancialHighlightsTextBlock = '' #キャッシュ・フロー計算書、財務ハイライト情報 [テキストブロック]
	OverviewOfOperationalProceduresRelatedToDomesticInvestmentSecuritiesHeading = '' #内国投資証券事務の概要 [目次項目]
	OverviewOfOperationalProceduresRelatedToDomesticInvestmentSecuritiesTextBlock = '' #内国投資証券事務の概要 [テキストブロック]
	ListOfContentsIncludedInDetailsOfInvestmentCorporationHeading = '' #投資法人の詳細情報の項目 [目次項目]
	ListOfContentsIncludedInDetailsOfInvestmentCorporationTextBlock = '' #投資法人の詳細情報の項目 [テキストブロック]
	DetailsOfInvestmentCorporationHeading = '' #投資法人の詳細情報 [目次項目]
	AdditionalInformationAboutInvestmentCorporationHeading = '' #投資法人の追加情報 [目次項目]
	HistoryOfInvestmentCorporationHeading = '' #投資法人の沿革 [目次項目]
	HistoryOfInvestmentCorporationTextBlock = '' #投資法人の沿革 [テキストブロック]
	InformationAboutOfficersAdditionalInformationAboutInvestmentCorporationHeading = '' #役員の状況、投資法人の追加情報 [目次項目]
	InformationAboutOfficersAdditionalInformationAboutInvestmentCorporationTextBlock = '' #役員の状況、投資法人の追加情報 [テキストブロック]
	OtherInformationAdditionalInformationAboutInvestmentCorporationHeading = '' #その他、投資法人の追加情報 [目次項目]
	OtherInformationAdditionalInformationAboutInvestmentCorporationTextBlock = '' #その他、投資法人の追加情報 [テキストブロック]
	ProceduresEtcHeading = '' #手続等 [目次項目]
	ProceduresEtcForApplicationAndDistributionInvestmentCorporationHeading = '' #申込（販売）手続等、投資法人 [目次項目]
	ProceduresEtcForApplicationAndDistributionInvestmentCorporationTextBlock = '' #申込（販売）手続等、投資法人 [テキストブロック]
	RedemptionProceduresEtcInvestmentCorporationHeading = '' #買戻し手続等、投資法人 [目次項目]
	RedemptionProceduresEtcInvestmentCorporationTextBlock = '' #買戻し手続等、投資法人 [テキストブロック]
	AdministrationAndOperationHeading = '' #管理及び運営 [目次項目]
	OverviewOfAssetManagementEtcHeading = '' #資産管理等の概要 [目次項目]
	ValuationOfAssetsHeading = '' #資産の評価 [目次項目]
	ValuationOfAssetsTextBlock = '' #資産の評価 [テキストブロック]
	CustodyHeading = '' #保管 [目次項目]
	CustodyTextBlock = '' #保管 [テキストブロック]
	DurationOfInvestmentCorporationHeading = '' #存続期間 [目次項目]
	DurationOfInvestmentCorporationTextBlock = '' #存続期間 [テキストブロック]
	AccountingPeriodHeading = '' #計算期間 [目次項目]
	AccountingPeriodTextBlock = '' #計算期間 [テキストブロック]
	OtherInformationOverviewOfAssetManagementEtcHeading = '' #その他、資産管理等の概要 [目次項目]
	OtherInformationOverviewOfAssetManagementEtcTextBlock = '' #その他、資産管理等の概要 [テキストブロック]
	RestrictionsOnTradesWithInterestedPartiesHeading = '' #利害関係人との取引制限 [目次項目]
	RestrictionsOnTradesWithInterestedPartiesTextBlock = '' #利害関係人との取引制限 [テキストブロック]
	RightsOfUnitholdersAndBondholdersOfInvestmentCorporationHeading = '' #投資主・投資法人債権者の権利 [目次項目]
	RightsOfUnitholdersAndBondholdersOfInvestmentCorporationTextBlock = '' #投資主・投資法人債権者の権利 [テキストブロック]
	OverviewOfPartiesInvolvedHeading = '' #関係法人の状況 [目次項目]
	OverviewOfAssetManagementCompanyHeading = '' #資産運用会社の概況 [目次項目]
	NameStatedCapitalAndDescriptionOfBusinessOverviewOfAssetManagementCompanyHeading = '' #名称、資本金の額及び事業の内容、資産運用会社の概況 [目次項目]
	NameStatedCapitalAndDescriptionOfBusinessOverviewOfAssetManagementCompanyTextBlock = '' #名称、資本金の額及び事業の内容、資産運用会社の概況 [テキストブロック]
	OrganizationAndFrameworkOfInvestmentManagementOverviewOfAssetManagementCompanyHeading = '' #運用体制、資産運用会社の概況 [目次項目]
	OrganizationAndFrameworkOfInvestmentManagementOverviewOfAssetManagementCompanyTextBlock = '' #運用体制、資産運用会社の概況 [テキストブロック]
	MajorShareholdersOverviewOfAssetManagementCompanyHeading = '' #大株主の状況、資産運用会社の概況 [目次項目]
	MajorShareholdersOverviewOfAssetManagementCompanyTextBlock = '' #大株主の状況、資産運用会社の概況 [テキストブロック]
	InformationAboutOfficersOverviewOfAssetManagementCompanyHeading = '' #役員の状況、資産運用会社の概況 [目次項目]
	InformationAboutOfficersOverviewOfAssetManagementCompanyTextBlock = '' #役員の状況、資産運用会社の概況 [テキストブロック]
	DescriptionOfBusinessAndOverviewOfOperationOverviewOfAssetManagementCompanyHeading = '' #事業の内容及び営業の概況、資産運用会社の概況 [目次項目]
	DescriptionOfBusinessAndOverviewOfOperationOverviewOfAssetManagementCompanyTextBlock = '' #事業の内容及び営業の概況、資産運用会社の概況 [テキストブロック]
	OverviewOfOtherPartiesInvolvedHeading = '' #その他の関係法人の概況 [目次項目]
	OverviewOfOtherPartiesInvolvedTextBlock = '' #その他の関係法人の概況 [テキストブロック]
	FinancialInformationOfInvestmentCorporationHeading = '' #投資法人の経理状況 [目次項目]
	FinancialInformationOfInvestmentCorporationTextBlock = '' #投資法人の経理状況 [テキストブロック]
	FinancialStatementsHeading = '' #財務諸表 [目次項目]
	BalanceSheetHeading = '' #貸借対照表 [目次項目]
	BalanceSheetTextBlock = '' #貸借対照表 [テキストブロック]
	StatementOfIncomeHeading = '' #損益計算書 [目次項目]
	StatementOfIncomeTextBlock = '' #損益計算書 [テキストブロック]
	StatementOfUnitholdersEquityHeading = '' #投資主資本等変動計算書 [目次項目]
	StatementOfUnitholdersEquityTextBlock = '' #投資主資本等変動計算書 [テキストブロック]
	StatementOfCashDistributionHeading = '' #金銭の分配に係る計算書 [目次項目]
	StatementOfCashDistributionTextBlock = '' #金銭の分配に係る計算書 [テキストブロック]
	StatementOfCashFlowsHeading = '' #キャッシュ・フロー計算書 [目次項目]
	StatementOfCashFlowsTextBlock = '' #キャッシュ・フロー計算書 [テキストブロック]
	NotesToFinancialStatementsHeading = '' #注記表 [目次項目]
	NotesToFinancialStatementsTextBlock = '' #注記表 [テキストブロック]
	AnnexedDetailedSchedulesHeading = '' #附属明細表 [目次項目]
	AnnexedDetailedSchedulesTextBlock = '' #附属明細表 [テキストブロック]
	CurrentStatusOfInvestmentCorporationHeading = '' #投資法人の現況 [目次項目]
	CalculationOfNetAssetsHeading = '' #純資産額計算書 [目次項目]
	CalculationOfNetAssetsTextBlock = '' #純資産額計算書 [テキストブロック]
	HistoricalRecordsOfSalesAndBuybacksHeading = '' #販売及び買戻しの実績 [目次項目]
	HistoricalRecordsOfSalesAndBuybacksTextBlock = '' #販売及び買戻しの実績 [テキストブロック]
	PhotographsDiagramsAndOtherItemsHeading = '' #写真、図面その他 [目次項目]
	PhotographsDiagramsAndOtherItemsTextBlock = '' #写真、図面その他 [テキストブロック]
	IndependentAuditorsReportHeading = '' #独立監査人の報告書 [目次項目]
	IndependentAuditorsReportInvestmentCorporationTextBlock = '' #独立監査人の報告書、投資法人 [テキストブロック]

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
			elif fact.concept.qname.localName == 'CabinetOfficeOrdinanceOnDisclosureOfInformationEtcOnSpecifiedSecuritiesFormNo43SecuritiesRegistrationStatementHeading': #特定有価証券の内容等の開示に関する内閣府令 第四号の三様式 有価証券届出書 [目次項目]
				self.CabinetOfficeOrdinanceOnDisclosureOfInformationEtcOnSpecifiedSecuritiesFormNo43SecuritiesRegistrationStatementHeading = fact.value

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

			elif fact.concept.qname.localName == 'NameOfInvestmentCorporationRelatedToDomesticInvestmentSecuritiesToRegisterForOfferingOrDistributionCoverPage': #届出の対象とした募集（売出）内国投資証券に係る投資法人の名称、表紙
				self.NameOfInvestmentCorporationRelatedToDomesticInvestmentSecuritiesToRegisterForOfferingOrDistributionCoverPage = fact.value

			elif fact.concept.qname.localName == 'LegalFormAndAmountOfDomesticInvestmentSecuritiesToRegisterForOfferingOrDistributionCoverPageTextBlock': #届出の対象とした募集（売出）内国投資証券の形態及び金額、表紙 [テキストブロック]
				self.LegalFormAndAmountOfDomesticInvestmentSecuritiesToRegisterForOfferingOrDistributionCoverPageTextBlock = fact.value

			elif fact.concept.qname.localName == 'PlaceForPublicInspectionCoverPageTextBlock': #縦覧に供する場所、表紙 [テキストブロック]
				self.PlaceForPublicInspectionCoverPageTextBlock = fact.value

			elif fact.concept.qname.localName == 'SecurityInformationHeading': #証券情報 [目次項目]
				self.SecurityInformationHeading = fact.value

			elif fact.concept.qname.localName == 'DomesticInvestmentSecuritiesOtherThanInvestmentCorporationBondsHeading': #内国投資証券（新投資口予約権証券及び投資法人債券を除く。） [目次項目]
				self.DomesticInvestmentSecuritiesOtherThanInvestmentCorporationBondsHeading = fact.value

			elif fact.concept.qname.localName == 'DomesticInvestmentSecuritiesOtherThanInvestmentUnitAcquisitionRightsAndInvestmentCorporationBondsTextBlock': #内国投資証券（新投資口予約権証券及び投資法人債券を除く。） [テキストブロック]
				self.DomesticInvestmentSecuritiesOtherThanInvestmentUnitAcquisitionRightsAndInvestmentCorporationBondsTextBlock = fact.value

			elif fact.concept.qname.localName == 'PublicOfferingOfDomesticInvestmentSecuritiesHeading': #募集内国投資証券 [目次項目]
				self.PublicOfferingOfDomesticInvestmentSecuritiesHeading = fact.value

			elif fact.concept.qname.localName == 'NameOfInvestmentCorporationPublicOfferingOfDomesticInvestmentSecuritiesHeading': #投資法人の名称、募集内国投資証券 [目次項目]
				self.NameOfInvestmentCorporationPublicOfferingOfDomesticInvestmentSecuritiesHeading = fact.value

			elif fact.concept.qname.localName == 'NameOfInvestmentCorporationPublicOfferingOfDomesticInvestmentSecuritiesTextBlock': #投資法人の名称、募集内国投資証券 [テキストブロック]
				self.NameOfInvestmentCorporationPublicOfferingOfDomesticInvestmentSecuritiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'LegalFormEtcOfDomesticInvestmentSecuritiesPublicOfferingOfDomesticInvestmentSecuritiesHeading': #内国投資証券の形態等、募集内国投資証券 [目次項目]
				self.LegalFormEtcOfDomesticInvestmentSecuritiesPublicOfferingOfDomesticInvestmentSecuritiesHeading = fact.value

			elif fact.concept.qname.localName == 'LegalFormEtcOfDomesticInvestmentSecuritiesPublicOfferingOfDomesticInvestmentSecuritiesTextBlock': #内国投資証券の形態等、募集内国投資証券 [テキストブロック]
				self.LegalFormEtcOfDomesticInvestmentSecuritiesPublicOfferingOfDomesticInvestmentSecuritiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'NumberOfSecuritiesToBeIssuedPublicOfferingOfDomesticInvestmentSecuritiesHeading': #発行数、募集内国投資証券 [目次項目]
				self.NumberOfSecuritiesToBeIssuedPublicOfferingOfDomesticInvestmentSecuritiesHeading = fact.value

			elif fact.concept.qname.localName == 'NumberOfSecuritiesToBeIssuedPublicOfferingOfDomesticInvestmentSecuritiesTextBlock': #発行数、募集内国投資証券 [テキストブロック]
				self.NumberOfSecuritiesToBeIssuedPublicOfferingOfDomesticInvestmentSecuritiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'TotalAmountOfIssuePublicOfferingOfDomesticInvestmentSecuritiesHeading': #発行価額の総額、募集内国投資証券 [目次項目]
				self.TotalAmountOfIssuePublicOfferingOfDomesticInvestmentSecuritiesHeading = fact.value

			elif fact.concept.qname.localName == 'TotalAmountOfIssuePublicOfferingOfDomesticInvestmentSecuritiesTextBlock': #発行価額の総額、募集内国投資証券 [テキストブロック]
				self.TotalAmountOfIssuePublicOfferingOfDomesticInvestmentSecuritiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'PriceOfIssuePublicOfferingOfDomesticInvestmentSecuritiesHeading': #発行価格、募集内国投資証券 [目次項目]
				self.PriceOfIssuePublicOfferingOfDomesticInvestmentSecuritiesHeading = fact.value

			elif fact.concept.qname.localName == 'PriceOfIssuePublicOfferingOfDomesticInvestmentSecuritiesTextBlock': #発行価格、募集内国投資証券 [テキストブロック]
				self.PriceOfIssuePublicOfferingOfDomesticInvestmentSecuritiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'ApplicationFeePublicOfferingOfDomesticInvestmentSecuritiesHeading': #申込手数料、募集内国投資証券 [目次項目]
				self.ApplicationFeePublicOfferingOfDomesticInvestmentSecuritiesHeading = fact.value

			elif fact.concept.qname.localName == 'ApplicationFeePublicOfferingOfDomesticInvestmentSecuritiesTextBlock': #申込手数料、募集内国投資証券 [テキストブロック]
				self.ApplicationFeePublicOfferingOfDomesticInvestmentSecuritiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'ApplicationUnitPublicOfferingOfDomesticInvestmentSecuritiesHeading': #申込単位、募集内国投資証券 [目次項目]
				self.ApplicationUnitPublicOfferingOfDomesticInvestmentSecuritiesHeading = fact.value

			elif fact.concept.qname.localName == 'ApplicationUnitPublicOfferingOfDomesticInvestmentSecuritiesTextBlock': #申込単位、募集内国投資証券 [テキストブロック]
				self.ApplicationUnitPublicOfferingOfDomesticInvestmentSecuritiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'ApplicationPeriodPublicOfferingOfDomesticInvestmentSecuritiesHeading': #申込期間、募集内国投資証券 [目次項目]
				self.ApplicationPeriodPublicOfferingOfDomesticInvestmentSecuritiesHeading = fact.value

			elif fact.concept.qname.localName == 'ApplicationPeriodPublicOfferingOfDomesticInvestmentSecuritiesTextBlock': #申込期間、募集内国投資証券 [テキストブロック]
				self.ApplicationPeriodPublicOfferingOfDomesticInvestmentSecuritiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'ApplicationMoneyPublicOfferingOfDomesticInvestmentSecuritiesHeading': #申込証拠金、募集内国投資証券 [目次項目]
				self.ApplicationMoneyPublicOfferingOfDomesticInvestmentSecuritiesHeading = fact.value

			elif fact.concept.qname.localName == 'ApplicationMoneyPublicOfferingOfDomesticInvestmentSecuritiesTextBlock': #申込証拠金、募集内国投資証券 [テキストブロック]
				self.ApplicationMoneyPublicOfferingOfDomesticInvestmentSecuritiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'PlaceForApplicationPublicOfferingOfDomesticInvestmentSecuritiesHeading': #申込取扱場所、募集内国投資証券 [目次項目]
				self.PlaceForApplicationPublicOfferingOfDomesticInvestmentSecuritiesHeading = fact.value

			elif fact.concept.qname.localName == 'PlaceForApplicationPublicOfferingOfDomesticInvestmentSecuritiesTextBlock': #申込取扱場所、募集内国投資証券 [テキストブロック]
				self.PlaceForApplicationPublicOfferingOfDomesticInvestmentSecuritiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'DueDateOfPaymentPublicOfferingOfDomesticInvestmentSecuritiesHeading': #払込期日、募集内国投資証券 [目次項目]
				self.DueDateOfPaymentPublicOfferingOfDomesticInvestmentSecuritiesHeading = fact.value

			elif fact.concept.qname.localName == 'DueDateOfPaymentPublicOfferingOfDomesticInvestmentSecuritiesTextBlock': #払込期日、募集内国投資証券 [テキストブロック]
				self.DueDateOfPaymentPublicOfferingOfDomesticInvestmentSecuritiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'PlaceForPaymentPublicOfferingOfDomesticInvestmentSecuritiesHeading': #払込取扱場所、募集内国投資証券 [目次項目]
				self.PlaceForPaymentPublicOfferingOfDomesticInvestmentSecuritiesHeading = fact.value

			elif fact.concept.qname.localName == 'PlaceForPaymentPublicOfferingOfDomesticInvestmentSecuritiesTextBlock': #払込取扱場所、募集内国投資証券 [テキストブロック]
				self.PlaceForPaymentPublicOfferingOfDomesticInvestmentSecuritiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'OverviewOfUnderwritingEtcPublicOfferingOfDomesticInvestmentSecuritiesHeading': #引受け等の概要、募集内国投資証券 [目次項目]
				self.OverviewOfUnderwritingEtcPublicOfferingOfDomesticInvestmentSecuritiesHeading = fact.value

			elif fact.concept.qname.localName == 'OverviewOfUnderwritingEtcPublicOfferingOfDomesticInvestmentSecuritiesTextBlock': #引受け等の概要、募集内国投資証券 [テキストブロック]
				self.OverviewOfUnderwritingEtcPublicOfferingOfDomesticInvestmentSecuritiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'BookEntryTransferInstitutionPublicOfferingOfDomesticInvestmentSecuritiesHeading': #振替機関に関する事項、募集内国投資証券 [目次項目]
				self.BookEntryTransferInstitutionPublicOfferingOfDomesticInvestmentSecuritiesHeading = fact.value

			elif fact.concept.qname.localName == 'BookEntryTransferInstitutionPublicOfferingOfDomesticInvestmentSecuritiesTextBlock': #振替機関に関する事項、募集内国投資証券 [テキストブロック]
				self.BookEntryTransferInstitutionPublicOfferingOfDomesticInvestmentSecuritiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'UseOfNetProceedsPublicOfferingOfDomesticInvestmentSecuritiesHeading': #手取金の使途、募集内国投資証券 [目次項目]
				self.UseOfNetProceedsPublicOfferingOfDomesticInvestmentSecuritiesHeading = fact.value

			elif fact.concept.qname.localName == 'UseOfNetProceedsPublicOfferingOfDomesticInvestmentSecuritiesTextBlock': #手取金の使途、募集内国投資証券 [テキストブロック]
				self.UseOfNetProceedsPublicOfferingOfDomesticInvestmentSecuritiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'OtherInformationPublicOfferingOfDomesticInvestmentSecuritiesHeading': #その他、募集内国投資証券 [目次項目]
				self.OtherInformationPublicOfferingOfDomesticInvestmentSecuritiesHeading = fact.value

			elif fact.concept.qname.localName == 'OtherInformationPublicOfferingOfDomesticInvestmentSecuritiesTextBlock': #その他、募集内国投資証券 [テキストブロック]
				self.OtherInformationPublicOfferingOfDomesticInvestmentSecuritiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'SecondaryDistributionOfDomesticInvestmentSecuritiesHeading': #売出内国投資証券 [目次項目]
				self.SecondaryDistributionOfDomesticInvestmentSecuritiesHeading = fact.value

			elif fact.concept.qname.localName == 'NameOfInvestmentCorporationSecondaryDistributionOfDomesticInvestmentSecuritiesHeading': #投資法人の名称、売出内国投資証券 [目次項目]
				self.NameOfInvestmentCorporationSecondaryDistributionOfDomesticInvestmentSecuritiesHeading = fact.value

			elif fact.concept.qname.localName == 'NameOfInvestmentCorporationSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock': #投資法人の名称、売出内国投資証券 [テキストブロック]
				self.NameOfInvestmentCorporationSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'LegalFormEtcOfDomesticInvestmentSecuritiesSecondaryDistributionOfDomesticInvestmentSecuritiesHeading': #内国投資証券の形態等、売出内国投資証券 [目次項目]
				self.LegalFormEtcOfDomesticInvestmentSecuritiesSecondaryDistributionOfDomesticInvestmentSecuritiesHeading = fact.value

			elif fact.concept.qname.localName == 'LegalFormEtcOfDomesticInvestmentSecuritiesSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock': #内国投資証券の形態等、売出内国投資証券 [テキストブロック]
				self.LegalFormEtcOfDomesticInvestmentSecuritiesSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'NumberOfSecuritiesToBeDistributedSecondaryDistributionOfDomesticInvestmentSecuritiesHeading': #売出数、売出内国投資証券 [目次項目]
				self.NumberOfSecuritiesToBeDistributedSecondaryDistributionOfDomesticInvestmentSecuritiesHeading = fact.value

			elif fact.concept.qname.localName == 'NumberOfSecuritiesToBeDistributedSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock': #売出数、売出内国投資証券 [テキストブロック]
				self.NumberOfSecuritiesToBeDistributedSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'TotalAmountOfSecondaryDistributionSecondaryDistributionOfDomesticInvestmentSecuritiesHeading': #売出価額の総額、売出内国投資証券 [目次項目]
				self.TotalAmountOfSecondaryDistributionSecondaryDistributionOfDomesticInvestmentSecuritiesHeading = fact.value

			elif fact.concept.qname.localName == 'TotalAmountOfSecondaryDistributionSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock': #売出価額の総額、売出内国投資証券 [テキストブロック]
				self.TotalAmountOfSecondaryDistributionSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'PriceOfSecondaryDistributionSecondaryDistributionOfDomesticInvestmentSecuritiesHeading': #売出価格、売出内国投資証券 [目次項目]
				self.PriceOfSecondaryDistributionSecondaryDistributionOfDomesticInvestmentSecuritiesHeading = fact.value

			elif fact.concept.qname.localName == 'PriceOfSecondaryDistributionSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock': #売出価格、売出内国投資証券 [テキストブロック]
				self.PriceOfSecondaryDistributionSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'ApplicationFeeSecondaryDistributionOfDomesticInvestmentSecuritiesHeading': #申込手数料、売出内国投資証券 [目次項目]
				self.ApplicationFeeSecondaryDistributionOfDomesticInvestmentSecuritiesHeading = fact.value

			elif fact.concept.qname.localName == 'ApplicationFeeSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock': #申込手数料、売出内国投資証券 [テキストブロック]
				self.ApplicationFeeSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'ApplicationUnitSecondaryDistributionOfDomesticInvestmentSecuritiesHeading': #申込単位、売出内国投資証券 [目次項目]
				self.ApplicationUnitSecondaryDistributionOfDomesticInvestmentSecuritiesHeading = fact.value

			elif fact.concept.qname.localName == 'ApplicationUnitSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock': #申込単位、売出内国投資証券 [テキストブロック]
				self.ApplicationUnitSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'ApplicationPeriodSecondaryDistributionOfDomesticInvestmentSecuritiesHeading': #申込期間、売出内国投資証券 [目次項目]
				self.ApplicationPeriodSecondaryDistributionOfDomesticInvestmentSecuritiesHeading = fact.value

			elif fact.concept.qname.localName == 'ApplicationPeriodSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock': #申込期間、売出内国投資証券 [テキストブロック]
				self.ApplicationPeriodSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'ApplicationMoneySecondaryDistributionOfDomesticInvestmentSecuritiesHeading': #申込証拠金、売出内国投資証券 [目次項目]
				self.ApplicationMoneySecondaryDistributionOfDomesticInvestmentSecuritiesHeading = fact.value

			elif fact.concept.qname.localName == 'ApplicationMoneySecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock': #申込証拠金、売出内国投資証券 [テキストブロック]
				self.ApplicationMoneySecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'PlaceForApplicationSecondaryDistributionOfDomesticInvestmentSecuritiesHeading': #申込取扱場所、売出内国投資証券 [目次項目]
				self.PlaceForApplicationSecondaryDistributionOfDomesticInvestmentSecuritiesHeading = fact.value

			elif fact.concept.qname.localName == 'PlaceForApplicationSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock': #申込取扱場所、売出内国投資証券 [テキストブロック]
				self.PlaceForApplicationSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'SettlementDateSecondaryDistributionOfDomesticInvestmentSecuritiesHeading': #受渡期日、売出内国投資証券 [目次項目]
				self.SettlementDateSecondaryDistributionOfDomesticInvestmentSecuritiesHeading = fact.value

			elif fact.concept.qname.localName == 'SettlementDateSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock': #受渡期日、売出内国投資証券 [テキストブロック]
				self.SettlementDateSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'PlaceForPaymentSecondaryDistributionOfDomesticInvestmentSecuritiesHeading': #払込取扱場所、売出内国投資証券 [目次項目]
				self.PlaceForPaymentSecondaryDistributionOfDomesticInvestmentSecuritiesHeading = fact.value

			elif fact.concept.qname.localName == 'PlaceForPaymentSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock': #払込取扱場所、売出内国投資証券 [テキストブロック]
				self.PlaceForPaymentSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'OverviewOfUnderwritingEtcSecondaryDistributionOfDomesticInvestmentSecuritiesHeading': #引受け等の概要、売出内国投資証券 [目次項目]
				self.OverviewOfUnderwritingEtcSecondaryDistributionOfDomesticInvestmentSecuritiesHeading = fact.value

			elif fact.concept.qname.localName == 'OverviewOfUnderwritingEtcSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock': #引受け等の概要、売出内国投資証券 [テキストブロック]
				self.OverviewOfUnderwritingEtcSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'BookEntryTransferInstitutionSecondaryDistributionOfDomesticInvestmentSecuritiesHeading': #振替機関に関する事項、売出内国投資証券 [目次項目]
				self.BookEntryTransferInstitutionSecondaryDistributionOfDomesticInvestmentSecuritiesHeading = fact.value

			elif fact.concept.qname.localName == 'BookEntryTransferInstitutionSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock': #振替機関に関する事項、売出内国投資証券 [テキストブロック]
				self.BookEntryTransferInstitutionSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'UseOfNetProceedsSecondaryDistributionOfDomesticInvestmentSecuritiesHeading': #手取金の使途、売出内国投資証券 [目次項目]
				self.UseOfNetProceedsSecondaryDistributionOfDomesticInvestmentSecuritiesHeading = fact.value

			elif fact.concept.qname.localName == 'UseOfNetProceedsSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock': #手取金の使途、売出内国投資証券 [テキストブロック]
				self.UseOfNetProceedsSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'OtherInformationSecondaryDistributionOfDomesticInvestmentSecuritiesHeading': #その他、売出内国投資証券 [目次項目]
				self.OtherInformationSecondaryDistributionOfDomesticInvestmentSecuritiesHeading = fact.value

			elif fact.concept.qname.localName == 'OtherInformationSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock': #その他、売出内国投資証券 [テキストブロック]
				self.OtherInformationSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'SubscriptionRightsToSharesOfInvestmentCorporationHeading': #新投資口予約権証券 [目次項目]
				self.SubscriptionRightsToSharesOfInvestmentCorporationHeading = fact.value

			elif fact.concept.qname.localName == 'InvestmentUnitAcquisitionRightsTextBlock': #新投資口予約権証券 [テキストブロック]
				self.InvestmentUnitAcquisitionRightsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NameOfInvestmentCorporationSubscriptionRightsToSharesOfInvestmentCorporationHeading': #投資法人の名称、新投資口予約権証券 [目次項目]
				self.NameOfInvestmentCorporationSubscriptionRightsToSharesOfInvestmentCorporationHeading = fact.value

			elif fact.concept.qname.localName == 'NameOfInvestmentCorporationSubscriptionRightsToSharesOfInvestmentCorporationTextBlock': #投資法人の名称、新投資口予約権証券 [テキストブロック]
				self.NameOfInvestmentCorporationSubscriptionRightsToSharesOfInvestmentCorporationTextBlock = fact.value

			elif fact.concept.qname.localName == 'LegalFormEtcOfSubscriptionRightsToSharesOfInvestmentCorporationHeading': #新投資口予約権証券の形態等 [目次項目]
				self.LegalFormEtcOfSubscriptionRightsToSharesOfInvestmentCorporationHeading = fact.value

			elif fact.concept.qname.localName == 'LegalFormEtcOfSubscriptionRightsToSharesOfInvestmentCorporationTextBlock': #新投資口予約権証券の形態等 [テキストブロック]
				self.LegalFormEtcOfSubscriptionRightsToSharesOfInvestmentCorporationTextBlock = fact.value

			elif fact.concept.qname.localName == 'NumberOfSecuritiesToBeIssuedSubscriptionRightsToSharesOfInvestmentCorporationHeading': #発行数、新投資口予約権証券 [目次項目]
				self.NumberOfSecuritiesToBeIssuedSubscriptionRightsToSharesOfInvestmentCorporationHeading = fact.value

			elif fact.concept.qname.localName == 'NumberOfSecuritiesToBeIssuedSubscriptionRightsToSharesOfInvestmentCorporationTextBlock': #発行数、新投資口予約権証券 [テキストブロック]
				self.NumberOfSecuritiesToBeIssuedSubscriptionRightsToSharesOfInvestmentCorporationTextBlock = fact.value

			elif fact.concept.qname.localName == 'DateOfAllotmentSubscriptionRightsToSharesOfInvestmentCorporationHeading': #割当日、新投資口予約権証券 [目次項目]
				self.DateOfAllotmentSubscriptionRightsToSharesOfInvestmentCorporationHeading = fact.value

			elif fact.concept.qname.localName == 'DateOfAllotmentSubscriptionRightsToSharesOfInvestmentCorporationTextBlock': #割当日、新投資口予約権証券 [テキストブロック]
				self.DateOfAllotmentSubscriptionRightsToSharesOfInvestmentCorporationTextBlock = fact.value

			elif fact.concept.qname.localName == 'ParticularsOfSubscriptionRightsToSharesOfInvestmentCorporationHeading': #新投資口予約権の内容 [目次項目]
				self.ParticularsOfSubscriptionRightsToSharesOfInvestmentCorporationHeading = fact.value

			elif fact.concept.qname.localName == 'ParticularsOfSubscriptionRightsToSharesOfInvestmentCorporationTextBlock': #新投資口予約権の内容 [テキストブロック]
				self.ParticularsOfSubscriptionRightsToSharesOfInvestmentCorporationTextBlock = fact.value

			elif fact.concept.qname.localName == 'LegalFormEtcOfDomesticInvestmentSecuritiesUnderlyingSubscriptionRightsToSharesOfInvestmentCorporationHeading': #新投資口予約権の目的となる内国投資証券の形態等 [目次項目]
				self.LegalFormEtcOfDomesticInvestmentSecuritiesUnderlyingSubscriptionRightsToSharesOfInvestmentCorporationHeading = fact.value

			elif fact.concept.qname.localName == 'LegalFormEtcOfDomesticInvestmentSecuritiesUnderlyingSubscriptionRightsToSharesOfInvestmentCorporationTextBlock': #新投資口予約権の目的となる内国投資証券の形態等 [テキストブロック]
				self.LegalFormEtcOfDomesticInvestmentSecuritiesUnderlyingSubscriptionRightsToSharesOfInvestmentCorporationTextBlock = fact.value

			elif fact.concept.qname.localName == 'NumberOfDomesticInvestmentSecuritiesUnderlyingSubscriptionRightsToSharesOfInvestmentCorporationHeading': #新投資口予約権の目的となる内国投資証券の数 [目次項目]
				self.NumberOfDomesticInvestmentSecuritiesUnderlyingSubscriptionRightsToSharesOfInvestmentCorporationHeading = fact.value

			elif fact.concept.qname.localName == 'NumberOfDomesticInvestmentSecuritiesUnderlyingSubscriptionRightsToSharesOfInvestmentCorporationTextBlock': #新投資口予約権の目的となる内国投資証券の数 [テキストブロック]
				self.NumberOfDomesticInvestmentSecuritiesUnderlyingSubscriptionRightsToSharesOfInvestmentCorporationTextBlock = fact.value

			elif fact.concept.qname.localName == 'AmountOfPaymentWhenSubscriptionRightToShareOfInvestmentCorporationIsExercisedHeading': #新投資口予約権の行使時の払込金額 [目次項目]
				self.AmountOfPaymentWhenSubscriptionRightToShareOfInvestmentCorporationIsExercisedHeading = fact.value

			elif fact.concept.qname.localName == 'AmountOfPaymentWhenSubscriptionRightToShareOfInvestmentCorporationIsExercisedTextBlock': #新投資口予約権の行使時の払込金額 [テキストブロック]
				self.AmountOfPaymentWhenSubscriptionRightToShareOfInvestmentCorporationIsExercisedTextBlock = fact.value

			elif fact.concept.qname.localName == 'TotalAmountOfDomesticInvestmentSecuritiesToBeIssuedWhenSubscriptionRightsToSharesOfInvestmentCorporationAreExercisedHeading': #新投資口予約権の行使により発行する内国投資証券の発行価額の総額 [目次項目]
				self.TotalAmountOfDomesticInvestmentSecuritiesToBeIssuedWhenSubscriptionRightsToSharesOfInvestmentCorporationAreExercisedHeading = fact.value

			elif fact.concept.qname.localName == 'TotalAmountOfDomesticInvestmentSecuritiesToBeIssuedWhenSubscriptionRightsToSharesOfInvestmentCorporationAreExercisedTextBlock': #新投資口予約権の行使により発行する内国投資証券の発行価額の総額 [テキストブロック]
				self.TotalAmountOfDomesticInvestmentSecuritiesToBeIssuedWhenSubscriptionRightsToSharesOfInvestmentCorporationAreExercisedTextBlock = fact.value

			elif fact.concept.qname.localName == 'ExercisePeriodOfSubscriptionRightsToSharesOfInvestmentCorporationHeading': #新投資口予約権の行使期間 [目次項目]
				self.ExercisePeriodOfSubscriptionRightsToSharesOfInvestmentCorporationHeading = fact.value

			elif fact.concept.qname.localName == 'ExercisePeriodOfSubscriptionRightsToSharesOfInvestmentCorporationTextBlock': #新投資口予約権の行使期間 [テキストブロック]
				self.ExercisePeriodOfSubscriptionRightsToSharesOfInvestmentCorporationTextBlock = fact.value

			elif fact.concept.qname.localName == 'CustodianAgentAndPlaceOfPaymentForExerciseOfSubscriptionRightsToSharesOfInvestmentCorporationHeading': #新投資口予約権の行使請求の受付場所、取次場所及び払込取扱場所 [目次項目]
				self.CustodianAgentAndPlaceOfPaymentForExerciseOfSubscriptionRightsToSharesOfInvestmentCorporationHeading = fact.value

			elif fact.concept.qname.localName == 'CustodianAgentAndPlaceOfPaymentForExerciseOfSubscriptionRightsToSharesOfInvestmentCorporationTextBlock': #新投資口予約権の行使請求の受付場所、取次場所及び払込取扱場所 [テキストブロック]
				self.CustodianAgentAndPlaceOfPaymentForExerciseOfSubscriptionRightsToSharesOfInvestmentCorporationTextBlock = fact.value

			elif fact.concept.qname.localName == 'TermsOfExerciseOfSubscriptionRightsToSharesOfInvestmentCorporationHeading': #新投資口予約権の行使の条件 [目次項目]
				self.TermsOfExerciseOfSubscriptionRightsToSharesOfInvestmentCorporationHeading = fact.value

			elif fact.concept.qname.localName == 'TermsOfExerciseOfSubscriptionRightsToSharesOfInvestmentCorporationTextBlock': #新投資口予約権の行使の条件 [テキストブロック]
				self.TermsOfExerciseOfSubscriptionRightsToSharesOfInvestmentCorporationTextBlock = fact.value

			elif fact.concept.qname.localName == 'ReasonAndTermsOfAcquisitionOfTreasurySubscriptionRightsToSharesOfInvestmentCorporationHeading': #自己新投資口予約権の取得の事由及び取得の条件 [目次項目]
				self.ReasonAndTermsOfAcquisitionOfTreasurySubscriptionRightsToSharesOfInvestmentCorporationHeading = fact.value

			elif fact.concept.qname.localName == 'ReasonAndTermsOfAcquisitionOfTreasurySubscriptionRightsToSharesOfInvestmentCorporationTextBlock': #自己新投資口予約権の取得の事由及び取得の条件 [テキストブロック]
				self.ReasonAndTermsOfAcquisitionOfTreasurySubscriptionRightsToSharesOfInvestmentCorporationTextBlock = fact.value

			elif fact.concept.qname.localName == 'InformationAboutTransferOfSubscriptionRightsToSharesOfInvestmentCorporationHeading': #新投資口予約権の譲渡に関する事項 [目次項目]
				self.InformationAboutTransferOfSubscriptionRightsToSharesOfInvestmentCorporationHeading = fact.value

			elif fact.concept.qname.localName == 'InformationAboutTransferOfSubscriptionRightsToSharesOfInvestmentCorporationTextBlock': #新投資口予約権の譲渡に関する事項 [テキストブロック]
				self.InformationAboutTransferOfSubscriptionRightsToSharesOfInvestmentCorporationTextBlock = fact.value

			elif fact.concept.qname.localName == 'OverviewOfUnderwritingEtcSubscriptionRightsToSharesOfInvestmentCorporationHeading': #引受け等の概要、新投資口予約権証券 [目次項目]
				self.OverviewOfUnderwritingEtcSubscriptionRightsToSharesOfInvestmentCorporationHeading = fact.value

			elif fact.concept.qname.localName == 'OverviewOfUnderwritingEtcSubscriptionRightsToSharesOfInvestmentCorporationTextBlock': #引受け等の概要、新投資口予約権証券 [テキストブロック]
				self.OverviewOfUnderwritingEtcSubscriptionRightsToSharesOfInvestmentCorporationTextBlock = fact.value

			elif fact.concept.qname.localName == 'BookEntryTransferInstitutionSubscriptionRightsToSharesOfInvestmentCorporationHeading': #振替機関に関する事項、新投資口予約権証券 [目次項目]
				self.BookEntryTransferInstitutionSubscriptionRightsToSharesOfInvestmentCorporationHeading = fact.value

			elif fact.concept.qname.localName == 'BookEntryTransferInstitutionSubscriptionRightsToSharesOfInvestmentCorporationTextBlock': #振替機関に関する事項、新投資口予約権証券 [テキストブロック]
				self.BookEntryTransferInstitutionSubscriptionRightsToSharesOfInvestmentCorporationTextBlock = fact.value

			elif fact.concept.qname.localName == 'UseOfNetProceedsSubscriptionRightsToSharesOfInvestmentCorporationHeading': #手取金の使途、新投資口予約権証券 [目次項目]
				self.UseOfNetProceedsSubscriptionRightsToSharesOfInvestmentCorporationHeading = fact.value

			elif fact.concept.qname.localName == 'UseOfNetProceedsSubscriptionRightsToSharesOfInvestmentCorporationTextBlock': #手取金の使途、新投資口予約権証券 [テキストブロック]
				self.UseOfNetProceedsSubscriptionRightsToSharesOfInvestmentCorporationTextBlock = fact.value

			elif fact.concept.qname.localName == 'OtherInformationSubscriptionRightsToSharesOfInvestmentCorporationHeading': #その他、新投資口予約権証券 [目次項目]
				self.OtherInformationSubscriptionRightsToSharesOfInvestmentCorporationHeading = fact.value

			elif fact.concept.qname.localName == 'OtherInformationSubscriptionRightsToSharesOfInvestmentCorporationTextBlock': #その他、新投資口予約権証券 [テキストブロック]
				self.OtherInformationSubscriptionRightsToSharesOfInvestmentCorporationTextBlock = fact.value

			elif fact.concept.qname.localName == 'InvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading': #投資法人債券（短期投資法人債を除く。） [目次項目]
				self.InvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading = fact.value

			elif fact.concept.qname.localName == 'InvestmentCorporationBondsOtherThanShortTermOnesTextBlock': #投資法人債券（短期投資法人債を除く。） [テキストブロック]
				self.InvestmentCorporationBondsOtherThanShortTermOnesTextBlock = fact.value

			elif fact.concept.qname.localName == 'SecurityTitlesHeading': #銘柄 [目次項目]
				self.SecurityTitlesHeading = fact.value

			elif fact.concept.qname.localName == 'SecurityTitlesTextBlock': #銘柄 [テキストブロック]
				self.SecurityTitlesTextBlock = fact.value

			elif fact.concept.qname.localName == 'LegalFormEtcOfInvestmentCorporationBondsHeading': #投資法人債券の形態等 [目次項目]
				self.LegalFormEtcOfInvestmentCorporationBondsHeading = fact.value

			elif fact.concept.qname.localName == 'LegalFormEtcOfInvestmentCorporationBondsTextBlock': #投資法人債券の形態等 [テキストブロック]
				self.LegalFormEtcOfInvestmentCorporationBondsTextBlock = fact.value

			elif fact.concept.qname.localName == 'TotalFaceValueHeading': #券面総額 [目次項目]
				self.TotalFaceValueHeading = fact.value

			elif fact.concept.qname.localName == 'TotalFaceValueTextBlock': #券面総額 [テキストブロック]
				self.TotalFaceValueTextBlock = fact.value

			elif fact.concept.qname.localName == 'AmountOfEachOfInvestmentCorporationBondsHeading': #各投資法人債の金額 [目次項目]
				self.AmountOfEachOfInvestmentCorporationBondsHeading = fact.value

			elif fact.concept.qname.localName == 'AmountOfEachOfInvestmentCorporationBondsTextBlock': #各投資法人債の金額 [テキストブロック]
				self.AmountOfEachOfInvestmentCorporationBondsTextBlock = fact.value

			elif fact.concept.qname.localName == 'TotalAmountOfIssueOrSecondaryDistributionInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading': #発行（売出）価額の総額、投資法人債券（短期投資法人債を除く。） [目次項目]
				self.TotalAmountOfIssueOrSecondaryDistributionInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading = fact.value

			elif fact.concept.qname.localName == 'TotalAmountOfIssueOrSecondaryDistributionInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock': #発行（売出）価額の総額、投資法人債券（短期投資法人債を除く。） [テキストブロック]
				self.TotalAmountOfIssueOrSecondaryDistributionInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock = fact.value

			elif fact.concept.qname.localName == 'PriceOfIssueOrSecondaryDistributionInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading': #発行（売出）価格、投資法人債券（短期投資法人債を除く。） [目次項目]
				self.PriceOfIssueOrSecondaryDistributionInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading = fact.value

			elif fact.concept.qname.localName == 'PriceOfIssueOrSecondaryDistributionInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock': #発行（売出）価格、投資法人債券（短期投資法人債を除く。） [テキストブロック]
				self.PriceOfIssueOrSecondaryDistributionInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock = fact.value

			elif fact.concept.qname.localName == 'InterestRateHeading': #利率 [目次項目]
				self.InterestRateHeading = fact.value

			elif fact.concept.qname.localName == 'InterestRateTextBlock': #利率 [テキストブロック]
				self.InterestRateTextBlock = fact.value

			elif fact.concept.qname.localName == 'DateAndMethodOfInterestPaymentHeading': #利払日及び利息支払の方法 [目次項目]
				self.DateAndMethodOfInterestPaymentHeading = fact.value

			elif fact.concept.qname.localName == 'DateAndMethodOfInterestPaymentTextBlock': #利払日及び利息支払の方法 [テキストブロック]
				self.DateAndMethodOfInterestPaymentTextBlock = fact.value

			elif fact.concept.qname.localName == 'DateAndMethodOfRedemptionHeading': #償還期限及び償還の方法 [目次項目]
				self.DateAndMethodOfRedemptionHeading = fact.value

			elif fact.concept.qname.localName == 'DateAndMethodOfRedemptionTextBlock': #償還期限及び償還の方法 [テキストブロック]
				self.DateAndMethodOfRedemptionTextBlock = fact.value

			elif fact.concept.qname.localName == 'MethodOfPublicOfferingInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading': #募集の方法、投資法人債券（短期投資法人債を除く。） [目次項目]
				self.MethodOfPublicOfferingInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading = fact.value

			elif fact.concept.qname.localName == 'MethodOfPublicOfferingInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock': #募集の方法、投資法人債券（短期投資法人債を除く。） [テキストブロック]
				self.MethodOfPublicOfferingInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock = fact.value

			elif fact.concept.qname.localName == 'ApplicationMoneyInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading': #申込証拠金、投資法人債券（短期投資法人債を除く。） [目次項目]
				self.ApplicationMoneyInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading = fact.value

			elif fact.concept.qname.localName == 'ApplicationMoneyInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock': #申込証拠金、投資法人債券（短期投資法人債を除く。） [テキストブロック]
				self.ApplicationMoneyInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock = fact.value

			elif fact.concept.qname.localName == 'ApplicationPeriodInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading': #申込期間、投資法人債券（短期投資法人債を除く。） [目次項目]
				self.ApplicationPeriodInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading = fact.value

			elif fact.concept.qname.localName == 'ApplicationPeriodInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock': #申込期間、投資法人債券（短期投資法人債を除く。） [テキストブロック]
				self.ApplicationPeriodInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock = fact.value

			elif fact.concept.qname.localName == 'PlaceForApplicationInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading': #申込取扱場所、投資法人債券（短期投資法人債を除く。） [目次項目]
				self.PlaceForApplicationInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading = fact.value

			elif fact.concept.qname.localName == 'PlaceForApplicationInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock': #申込取扱場所、投資法人債券（短期投資法人債を除く。） [テキストブロック]
				self.PlaceForApplicationInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock = fact.value

			elif fact.concept.qname.localName == 'DueDateOfPaymentInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading': #払込期日、投資法人債券（短期投資法人債を除く。） [目次項目]
				self.DueDateOfPaymentInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading = fact.value

			elif fact.concept.qname.localName == 'DueDateOfPaymentInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock': #払込期日、投資法人債券（短期投資法人債を除く。） [テキストブロック]
				self.DueDateOfPaymentInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock = fact.value

			elif fact.concept.qname.localName == 'PlaceForPaymentInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading': #払込取扱場所、投資法人債券（短期投資法人債を除く。） [目次項目]
				self.PlaceForPaymentInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading = fact.value

			elif fact.concept.qname.localName == 'PlaceForPaymentInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock': #払込取扱場所、投資法人債券（短期投資法人債を除く。） [テキストブロック]
				self.PlaceForPaymentInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock = fact.value

			elif fact.concept.qname.localName == 'OverviewOfUnderwritingEtcInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading': #引受け等の概要、投資法人債券（短期投資法人債を除く。） [目次項目]
				self.OverviewOfUnderwritingEtcInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading = fact.value

			elif fact.concept.qname.localName == 'OverviewOfUnderwritingEtcInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock': #引受け等の概要、投資法人債券（短期投資法人債を除く。） [テキストブロック]
				self.OverviewOfUnderwritingEtcInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock = fact.value

			elif fact.concept.qname.localName == 'AdministratorOfInvestmentCorporationBondsHeading': #投資法人債管理者又は投資法人債の管理会社 [目次項目]
				self.AdministratorOfInvestmentCorporationBondsHeading = fact.value

			elif fact.concept.qname.localName == 'AdministratorOfInvestmentCorporationBondsTextBlock': #投資法人債管理者又は投資法人債の管理会社 [テキストブロック]
				self.AdministratorOfInvestmentCorporationBondsTextBlock = fact.value

			elif fact.concept.qname.localName == 'BookEntryTransferInstitutionInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading': #振替機関に関する事項、投資法人債券（短期投資法人債を除く。） [目次項目]
				self.BookEntryTransferInstitutionInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading = fact.value

			elif fact.concept.qname.localName == 'BookEntryTransferInstitutionInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock': #振替機関に関する事項、投資法人債券（短期投資法人債を除く。） [テキストブロック]
				self.BookEntryTransferInstitutionInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock = fact.value

			elif fact.concept.qname.localName == 'RegistrationDateAndRegistrationNumberOfInvestmentCorporationHeading': #投資法人の登録年月日及び登録番号 [目次項目]
				self.RegistrationDateAndRegistrationNumberOfInvestmentCorporationHeading = fact.value

			elif fact.concept.qname.localName == 'RegistrationDateAndRegistrationNumberOfInvestmentCorporationTextBlock': #投資法人の登録年月日及び登録番号 [テキストブロック]
				self.RegistrationDateAndRegistrationNumberOfInvestmentCorporationTextBlock = fact.value

			elif fact.concept.qname.localName == 'UseOfNetProceedsInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading': #手取金の使途、投資法人債券（短期投資法人債を除く。） [目次項目]
				self.UseOfNetProceedsInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading = fact.value

			elif fact.concept.qname.localName == 'UseOfNetProceedsInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock': #手取金の使途、投資法人債券（短期投資法人債を除く。） [テキストブロック]
				self.UseOfNetProceedsInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock = fact.value

			elif fact.concept.qname.localName == 'OtherInformationInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading': #その他、投資法人債券（短期投資法人債を除く。） [目次項目]
				self.OtherInformationInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading = fact.value

			elif fact.concept.qname.localName == 'OtherInformationInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock': #その他、投資法人債券（短期投資法人債を除く。） [テキストブロック]
				self.OtherInformationInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock = fact.value

			elif fact.concept.qname.localName == 'ShortTermInvestmentCorporationBondsHeading': #短期投資法人債 [目次項目]
				self.ShortTermInvestmentCorporationBondsHeading = fact.value

			elif fact.concept.qname.localName == 'ShortTermInvestmentCorporationBondsTextBlock': #短期投資法人債 [テキストブロック]
				self.ShortTermInvestmentCorporationBondsTextBlock = fact.value

			elif fact.concept.qname.localName == 'TotalAmountOfIssueOrSecondaryDistributionOfShortTermInvestmentCorporationBondsHeading': #発行（売出）短期投資法人債の総額 [目次項目]
				self.TotalAmountOfIssueOrSecondaryDistributionOfShortTermInvestmentCorporationBondsHeading = fact.value

			elif fact.concept.qname.localName == 'TotalAmountOfIssueOrSecondaryDistributionOfShortTermInvestmentCorporationBondsTextBlock': #発行（売出）短期投資法人債の総額 [テキストブロック]
				self.TotalAmountOfIssueOrSecondaryDistributionOfShortTermInvestmentCorporationBondsTextBlock = fact.value

			elif fact.concept.qname.localName == 'TotalAmountOfIssueOrSecondaryDistributionShortTermInvestmentCorporationBondsHeading': #発行（売出）価額の総額、短期投資法人債 [目次項目]
				self.TotalAmountOfIssueOrSecondaryDistributionShortTermInvestmentCorporationBondsHeading = fact.value

			elif fact.concept.qname.localName == 'TotalAmountOfIssueOrSecondaryDistributionShortTermInvestmentCorporationBondsTextBlock': #発行（売出）価額の総額、短期投資法人債 [テキストブロック]
				self.TotalAmountOfIssueOrSecondaryDistributionShortTermInvestmentCorporationBondsTextBlock = fact.value

			elif fact.concept.qname.localName == 'PriceOfIssueOrSecondaryDistributionShortTermInvestmentCorporationBondsHeading': #発行（売出）価格、短期投資法人債 [目次項目]
				self.PriceOfIssueOrSecondaryDistributionShortTermInvestmentCorporationBondsHeading = fact.value

			elif fact.concept.qname.localName == 'PriceOfIssueOrSecondaryDistributionShortTermInvestmentCorporationBondsTextBlock': #発行（売出）価格、短期投資法人債 [テキストブロック]
				self.PriceOfIssueOrSecondaryDistributionShortTermInvestmentCorporationBondsTextBlock = fact.value

			elif fact.concept.qname.localName == 'LimitOnAmountOfIssueHeading': #発行限度額 [目次項目]
				self.LimitOnAmountOfIssueHeading = fact.value

			elif fact.concept.qname.localName == 'LimitOnAmountOfIssueTextBlock': #発行限度額 [テキストブロック]
				self.LimitOnAmountOfIssueTextBlock = fact.value

			elif fact.concept.qname.localName == 'RemainingBalanceOfLimitOnAmountOfIssueHeading': #発行限度額残高 [目次項目]
				self.RemainingBalanceOfLimitOnAmountOfIssueHeading = fact.value

			elif fact.concept.qname.localName == 'RemainingBalanceOfLimitOnAmountOfIssueTextBlock': #発行限度額残高 [テキストブロック]
				self.RemainingBalanceOfLimitOnAmountOfIssueTextBlock = fact.value

			elif fact.concept.qname.localName == 'DueDateOfPaymentHeading': #支払期日 [目次項目]
				self.DueDateOfPaymentHeading = fact.value

			elif fact.concept.qname.localName == 'DueDateOfPaymentTextBlock': #支払期日 [テキストブロック]
				self.DueDateOfPaymentTextBlock = fact.value

			elif fact.concept.qname.localName == 'PlaceForPaymentHeading': #支払場所 [目次項目]
				self.PlaceForPaymentHeading = fact.value

			elif fact.concept.qname.localName == 'PlaceForPaymentTextBlock': #支払場所 [テキストブロック]
				self.PlaceForPaymentTextBlock = fact.value

			elif fact.concept.qname.localName == 'BookEntryTransferInstitutionShortTermInvestmentCorporationBondsHeading': #振替機関に関する事項、短期投資法人債 [目次項目]
				self.BookEntryTransferInstitutionShortTermInvestmentCorporationBondsHeading = fact.value

			elif fact.concept.qname.localName == 'BookEntryTransferInstitutionShortTermInvestmentCorporationBondsTextBlock': #振替機関に関する事項、短期投資法人債 [テキストブロック]
				self.BookEntryTransferInstitutionShortTermInvestmentCorporationBondsTextBlock = fact.value

			elif fact.concept.qname.localName == 'FinancialInstitutionProvidingBackupLineHeading': #バックアップラインの設定金融機関 [目次項目]
				self.FinancialInstitutionProvidingBackupLineHeading = fact.value

			elif fact.concept.qname.localName == 'FinancialInstitutionProvidingBackupLineTextBlock': #バックアップラインの設定金融機関 [テキストブロック]
				self.FinancialInstitutionProvidingBackupLineTextBlock = fact.value

			elif fact.concept.qname.localName == 'DescriptionOfBackupLineHeading': #バックアップラインの設定内容 [目次項目]
				self.DescriptionOfBackupLineHeading = fact.value

			elif fact.concept.qname.localName == 'DescriptionOfBackupLineTextBlock': #バックアップラインの設定内容 [テキストブロック]
				self.DescriptionOfBackupLineTextBlock = fact.value

			elif fact.concept.qname.localName == 'RatingHeading': #取得格付 [目次項目]
				self.RatingHeading = fact.value

			elif fact.concept.qname.localName == 'RatingTextBlock': #取得格付 [テキストブロック]
				self.RatingTextBlock = fact.value

			elif fact.concept.qname.localName == 'SpecialDisclosureAboutPublicOfferingOrSecondaryDistributionHeading': #募集又は売出しに関する特別記載事項 [目次項目]
				self.SpecialDisclosureAboutPublicOfferingOrSecondaryDistributionHeading = fact.value

			elif fact.concept.qname.localName == 'SpecialDisclosureAboutPublicOfferingOrSecondaryDistributionTextBlock': #募集又は売出しに関する特別記載事項 [テキストブロック]
				self.SpecialDisclosureAboutPublicOfferingOrSecondaryDistributionTextBlock = fact.value

			elif fact.concept.qname.localName == 'FundInformationHeading': #ファンド情報 [目次項目]
				self.FundInformationHeading = fact.value

			elif fact.concept.qname.localName == 'OverviewOfFundHeading': #ファンドの状況 [目次項目]
				self.OverviewOfFundHeading = fact.value

			elif fact.concept.qname.localName == 'OverviewOfInvestmentCorporationHeading': #投資法人の概況 [目次項目]
				self.OverviewOfInvestmentCorporationHeading = fact.value

			elif fact.concept.qname.localName == 'SummaryOfBusinessResultsHeading': #主要な経営指標等の推移 [目次項目]
				self.SummaryOfBusinessResultsHeading = fact.value

			elif fact.concept.qname.localName == 'SummaryOfBusinessResultsTextBlock': #主要な経営指標等の推移 [テキストブロック]
				self.SummaryOfBusinessResultsTextBlock = fact.value

			elif fact.concept.qname.localName == 'PurposesAndBasicFeaturesOfInvestmentCorporationHeading': #投資法人の目的及び基本的性格 [目次項目]
				self.PurposesAndBasicFeaturesOfInvestmentCorporationHeading = fact.value

			elif fact.concept.qname.localName == 'PurposesAndBasicFeaturesOfInvestmentCorporationTextBlock': #投資法人の目的及び基本的性格 [テキストブロック]
				self.PurposesAndBasicFeaturesOfInvestmentCorporationTextBlock = fact.value

			elif fact.concept.qname.localName == 'SchemeOfInvestmentCorporationHeading': #投資法人の仕組み [目次項目]
				self.SchemeOfInvestmentCorporationHeading = fact.value

			elif fact.concept.qname.localName == 'SchemeOfInvestmentCorporationTextBlock': #投資法人の仕組み [テキストブロック]
				self.SchemeOfInvestmentCorporationTextBlock = fact.value

			elif fact.concept.qname.localName == 'OrganizationOfInvestmentCorporationHeading': #投資法人の機構 [目次項目]
				self.OrganizationOfInvestmentCorporationHeading = fact.value

			elif fact.concept.qname.localName == 'OrganizationOfInvestmentCorporationTextBlock': #投資法人の機構 [テキストブロック]
				self.OrganizationOfInvestmentCorporationTextBlock = fact.value

			elif fact.concept.qname.localName == 'PaidInCapitalOfInvestmentCorporationHeading': #投資法人の出資総額 [目次項目]
				self.PaidInCapitalOfInvestmentCorporationHeading = fact.value

			elif fact.concept.qname.localName == 'PaidInCapitalOfInvestmentCorporationTextBlock': #投資法人の出資総額 [テキストブロック]
				self.PaidInCapitalOfInvestmentCorporationTextBlock = fact.value

			elif fact.concept.qname.localName == 'MajorUnitholdersHeading': #主要な投資主の状況 [目次項目]
				self.MajorUnitholdersHeading = fact.value

			elif fact.concept.qname.localName == 'MajorUnitholdersTextBlock': #主要な投資主の状況 [テキストブロック]
				self.MajorUnitholdersTextBlock = fact.value

			elif fact.concept.qname.localName == 'ShareOwnershipProgramForEmployeesOfAssetManagementCompanyHeading': #資産運用会社従業員等投資口所有制度の内容 [目次項目]
				self.ShareOwnershipProgramForEmployeesOfAssetManagementCompanyHeading = fact.value

			elif fact.concept.qname.localName == 'ShareOwnershipProgramForEmployeesOfAssetManagementCompanyTextBlock': #資産運用会社従業員等投資口所有制度の内容 [テキストブロック]
				self.ShareOwnershipProgramForEmployeesOfAssetManagementCompanyTextBlock = fact.value

			elif fact.concept.qname.localName == 'InvestmentPolicyOverviewOfFundHeading': #投資方針、ファンドの状況 [目次項目]
				self.InvestmentPolicyOverviewOfFundHeading = fact.value

			elif fact.concept.qname.localName == 'InvestmentPolicyHeading': #投資方針 [目次項目]
				self.InvestmentPolicyHeading = fact.value

			elif fact.concept.qname.localName == 'InvestmentPolicyTextBlock': #投資方針 [テキストブロック]
				self.InvestmentPolicyTextBlock = fact.value

			elif fact.concept.qname.localName == 'ThingsToInvestInHeading': #投資対象 [目次項目]
				self.ThingsToInvestInHeading = fact.value

			elif fact.concept.qname.localName == 'ThingsToInvestInTextBlock': #投資対象 [テキストブロック]
				self.ThingsToInvestInTextBlock = fact.value

			elif fact.concept.qname.localName == 'ProfitDistributionPolicyHeading': #分配方針 [目次項目]
				self.ProfitDistributionPolicyHeading = fact.value

			elif fact.concept.qname.localName == 'ProfitDistributionPolicyTextBlock': #分配方針 [テキストブロック]
				self.ProfitDistributionPolicyTextBlock = fact.value

			elif fact.concept.qname.localName == 'RestrictionsOnInvestmentHeading': #投資制限 [目次項目]
				self.RestrictionsOnInvestmentHeading = fact.value

			elif fact.concept.qname.localName == 'RestrictionsOnInvestmentTextBlock': #投資制限 [テキストブロック]
				self.RestrictionsOnInvestmentTextBlock = fact.value

			elif fact.concept.qname.localName == 'InvestmentRisksHeading': #投資リスク [目次項目]
				self.InvestmentRisksHeading = fact.value

			elif fact.concept.qname.localName == 'InvestmentRisksTextBlock': #投資リスク [テキストブロック]
				self.InvestmentRisksTextBlock = fact.value

			elif fact.concept.qname.localName == 'FeesChargesAndTaxesHeading': #手数料等及び税金 [目次項目]
				self.FeesChargesAndTaxesHeading = fact.value

			elif fact.concept.qname.localName == 'ApplicationFeeOverviewOfFundHeading': #申込手数料、ファンドの状況 [目次項目]
				self.ApplicationFeeOverviewOfFundHeading = fact.value

			elif fact.concept.qname.localName == 'ApplicationFeeOverviewOfFundTextBlock': #申込手数料、ファンドの状況 [テキストブロック]
				self.ApplicationFeeOverviewOfFundTextBlock = fact.value

			elif fact.concept.qname.localName == 'RedemptionFeeInvestmentCorporationHeading': #買戻し手数料、投資法人 [目次項目]
				self.RedemptionFeeInvestmentCorporationHeading = fact.value

			elif fact.concept.qname.localName == 'RedemptionFeeInvestmentCorporationTextBlock': #買戻し手数料、投資法人 [テキストブロック]
				self.RedemptionFeeInvestmentCorporationTextBlock = fact.value

			elif fact.concept.qname.localName == 'AdministrationFeesAndChargesHeading': #管理報酬等 [目次項目]
				self.AdministrationFeesAndChargesHeading = fact.value

			elif fact.concept.qname.localName == 'AdministrationFeesAndChargesTextBlock': #管理報酬等 [テキストブロック]
				self.AdministrationFeesAndChargesTextBlock = fact.value

			elif fact.concept.qname.localName == 'OtherFeesAndChargesHeading': #その他の手数料等 [目次項目]
				self.OtherFeesAndChargesHeading = fact.value

			elif fact.concept.qname.localName == 'OtherFeesAndChargesTextBlock': #その他の手数料等 [テキストブロック]
				self.OtherFeesAndChargesTextBlock = fact.value

			elif fact.concept.qname.localName == 'TaxationHeading': #課税上の取扱い [目次項目]
				self.TaxationHeading = fact.value

			elif fact.concept.qname.localName == 'TaxationTextBlock': #課税上の取扱い [テキストブロック]
				self.TaxationTextBlock = fact.value

			elif fact.concept.qname.localName == 'StatusOfInvestmentManagementHeading': #運用状況 [目次項目]
				self.StatusOfInvestmentManagementHeading = fact.value

			elif fact.concept.qname.localName == 'StatusOfInvestmentManagementTextBlock': #運用状況 [テキストブロック]
				self.StatusOfInvestmentManagementTextBlock = fact.value

			elif fact.concept.qname.localName == 'StatusOfInvestmentHeading': #投資状況 [目次項目]
				self.StatusOfInvestmentHeading = fact.value

			elif fact.concept.qname.localName == 'StatusOfInvestmentTextBlock': #投資状況 [テキストブロック]
				self.StatusOfInvestmentTextBlock = fact.value

			elif fact.concept.qname.localName == 'InvestmentAssetsHeading': #投資資産 [目次項目]
				self.InvestmentAssetsHeading = fact.value

			elif fact.concept.qname.localName == 'MajorComponentsOfInvestmentSecuritiesHeading': #投資有価証券の主要銘柄 [目次項目]
				self.MajorComponentsOfInvestmentSecuritiesHeading = fact.value

			elif fact.concept.qname.localName == 'MajorComponentsOfInvestmentSecuritiesTextBlock': #投資有価証券の主要銘柄 [テキストブロック]
				self.MajorComponentsOfInvestmentSecuritiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'ComponentsOfRealEstateInvestmentsHeading': #投資不動産物件 [目次項目]
				self.ComponentsOfRealEstateInvestmentsHeading = fact.value

			elif fact.concept.qname.localName == 'ComponentsOfRealEstateInvestmentsTextBlock': #投資不動産物件 [テキストブロック]
				self.ComponentsOfRealEstateInvestmentsTextBlock = fact.value

			elif fact.concept.qname.localName == 'MajorComponentsOfOtherInvestmentsHeading': #その他投資資産の主要なもの [目次項目]
				self.MajorComponentsOfOtherInvestmentsHeading = fact.value

			elif fact.concept.qname.localName == 'MajorComponentsOfOtherInvestmentsTextBlock': #その他投資資産の主要なもの [テキストブロック]
				self.MajorComponentsOfOtherInvestmentsTextBlock = fact.value

			elif fact.concept.qname.localName == 'ActualPerformanceHeading': #運用実績 [目次項目]
				self.ActualPerformanceHeading = fact.value

			elif fact.concept.qname.localName == 'ChangesInNetAssetsEtcHeading': #純資産等の推移 [目次項目]
				self.ChangesInNetAssetsEtcHeading = fact.value

			elif fact.concept.qname.localName == 'ChangesInNetAssetsEtcTextBlock': #純資産等の推移 [テキストブロック]
				self.ChangesInNetAssetsEtcTextBlock = fact.value

			elif fact.concept.qname.localName == 'HistoricalRecordsOfProfitDistributionHeading': #分配の推移 [目次項目]
				self.HistoricalRecordsOfProfitDistributionHeading = fact.value

			elif fact.concept.qname.localName == 'HistoricalRecordsOfProfitDistributionTextBlock': #分配の推移 [テキストブロック]
				self.HistoricalRecordsOfProfitDistributionTextBlock = fact.value

			elif fact.concept.qname.localName == 'HistoricalRecordsOfROEHeading': #自己資本利益率（収益率）の推移 [目次項目]
				self.HistoricalRecordsOfROEHeading = fact.value

			elif fact.concept.qname.localName == 'HistoricalRecordsOfROETextBlock': #自己資本利益率（収益率）の推移 [テキストブロック]
				self.HistoricalRecordsOfROETextBlock = fact.value

			elif fact.concept.qname.localName == 'OverviewOfProceduresEtcHeading': #手続等の概要 [目次項目]
				self.OverviewOfProceduresEtcHeading = fact.value

			elif fact.concept.qname.localName == 'OverviewOfProceduresEtcTextBlock': #手続等の概要 [テキストブロック]
				self.OverviewOfProceduresEtcTextBlock = fact.value

			elif fact.concept.qname.localName == 'OverviewOfAdministrationAndOperationHeading': #管理及び運営の概要 [目次項目]
				self.OverviewOfAdministrationAndOperationHeading = fact.value

			elif fact.concept.qname.localName == 'OverviewOfAdministrationAndOperationTextBlock': #管理及び運営の概要 [テキストブロック]
				self.OverviewOfAdministrationAndOperationTextBlock = fact.value

			elif fact.concept.qname.localName == 'FinancialHighlightsHeading': #財務ハイライト情報 [目次項目]
				self.FinancialHighlightsHeading = fact.value

			elif fact.concept.qname.localName == 'BalanceSheetFinancialHighlightsHeading': #貸借対照表、財務ハイライト情報 [目次項目]
				self.BalanceSheetFinancialHighlightsHeading = fact.value

			elif fact.concept.qname.localName == 'BalanceSheetFinancialHighlightsTextBlock': #貸借対照表、財務ハイライト情報 [テキストブロック]
				self.BalanceSheetFinancialHighlightsTextBlock = fact.value

			elif fact.concept.qname.localName == 'StatementOfIncomeFinancialHighlightsHeading': #損益計算書、財務ハイライト情報 [目次項目]
				self.StatementOfIncomeFinancialHighlightsHeading = fact.value

			elif fact.concept.qname.localName == 'StatementOfIncomeFinancialHighlightsTextBlock': #損益計算書、財務ハイライト情報 [テキストブロック]
				self.StatementOfIncomeFinancialHighlightsTextBlock = fact.value

			elif fact.concept.qname.localName == 'StatementOfCashDistributionFinancialHighlightsHeading': #金銭の分配に係る計算書、財務ハイライト情報 [目次項目]
				self.StatementOfCashDistributionFinancialHighlightsHeading = fact.value

			elif fact.concept.qname.localName == 'StatementOfCashDistributionFinancialHighlightsTextBlock': #金銭の分配に係る計算書、財務ハイライト情報 [テキストブロック]
				self.StatementOfCashDistributionFinancialHighlightsTextBlock = fact.value

			elif fact.concept.qname.localName == 'StatementOfCashFlowsFinancialHighlightsHeading': #キャッシュ・フロー計算書、財務ハイライト情報 [目次項目]
				self.StatementOfCashFlowsFinancialHighlightsHeading = fact.value

			elif fact.concept.qname.localName == 'StatementOfCashFlowsFinancialHighlightsTextBlock': #キャッシュ・フロー計算書、財務ハイライト情報 [テキストブロック]
				self.StatementOfCashFlowsFinancialHighlightsTextBlock = fact.value

			elif fact.concept.qname.localName == 'OverviewOfOperationalProceduresRelatedToDomesticInvestmentSecuritiesHeading': #内国投資証券事務の概要 [目次項目]
				self.OverviewOfOperationalProceduresRelatedToDomesticInvestmentSecuritiesHeading = fact.value

			elif fact.concept.qname.localName == 'OverviewOfOperationalProceduresRelatedToDomesticInvestmentSecuritiesTextBlock': #内国投資証券事務の概要 [テキストブロック]
				self.OverviewOfOperationalProceduresRelatedToDomesticInvestmentSecuritiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'ListOfContentsIncludedInDetailsOfInvestmentCorporationHeading': #投資法人の詳細情報の項目 [目次項目]
				self.ListOfContentsIncludedInDetailsOfInvestmentCorporationHeading = fact.value

			elif fact.concept.qname.localName == 'ListOfContentsIncludedInDetailsOfInvestmentCorporationTextBlock': #投資法人の詳細情報の項目 [テキストブロック]
				self.ListOfContentsIncludedInDetailsOfInvestmentCorporationTextBlock = fact.value

			elif fact.concept.qname.localName == 'DetailsOfInvestmentCorporationHeading': #投資法人の詳細情報 [目次項目]
				self.DetailsOfInvestmentCorporationHeading = fact.value

			elif fact.concept.qname.localName == 'AdditionalInformationAboutInvestmentCorporationHeading': #投資法人の追加情報 [目次項目]
				self.AdditionalInformationAboutInvestmentCorporationHeading = fact.value

			elif fact.concept.qname.localName == 'HistoryOfInvestmentCorporationHeading': #投資法人の沿革 [目次項目]
				self.HistoryOfInvestmentCorporationHeading = fact.value

			elif fact.concept.qname.localName == 'HistoryOfInvestmentCorporationTextBlock': #投資法人の沿革 [テキストブロック]
				self.HistoryOfInvestmentCorporationTextBlock = fact.value

			elif fact.concept.qname.localName == 'InformationAboutOfficersAdditionalInformationAboutInvestmentCorporationHeading': #役員の状況、投資法人の追加情報 [目次項目]
				self.InformationAboutOfficersAdditionalInformationAboutInvestmentCorporationHeading = fact.value

			elif fact.concept.qname.localName == 'InformationAboutOfficersAdditionalInformationAboutInvestmentCorporationTextBlock': #役員の状況、投資法人の追加情報 [テキストブロック]
				self.InformationAboutOfficersAdditionalInformationAboutInvestmentCorporationTextBlock = fact.value

			elif fact.concept.qname.localName == 'OtherInformationAdditionalInformationAboutInvestmentCorporationHeading': #その他、投資法人の追加情報 [目次項目]
				self.OtherInformationAdditionalInformationAboutInvestmentCorporationHeading = fact.value

			elif fact.concept.qname.localName == 'OtherInformationAdditionalInformationAboutInvestmentCorporationTextBlock': #その他、投資法人の追加情報 [テキストブロック]
				self.OtherInformationAdditionalInformationAboutInvestmentCorporationTextBlock = fact.value

			elif fact.concept.qname.localName == 'ProceduresEtcHeading': #手続等 [目次項目]
				self.ProceduresEtcHeading = fact.value

			elif fact.concept.qname.localName == 'ProceduresEtcForApplicationAndDistributionInvestmentCorporationHeading': #申込（販売）手続等、投資法人 [目次項目]
				self.ProceduresEtcForApplicationAndDistributionInvestmentCorporationHeading = fact.value

			elif fact.concept.qname.localName == 'ProceduresEtcForApplicationAndDistributionInvestmentCorporationTextBlock': #申込（販売）手続等、投資法人 [テキストブロック]
				self.ProceduresEtcForApplicationAndDistributionInvestmentCorporationTextBlock = fact.value

			elif fact.concept.qname.localName == 'RedemptionProceduresEtcInvestmentCorporationHeading': #買戻し手続等、投資法人 [目次項目]
				self.RedemptionProceduresEtcInvestmentCorporationHeading = fact.value

			elif fact.concept.qname.localName == 'RedemptionProceduresEtcInvestmentCorporationTextBlock': #買戻し手続等、投資法人 [テキストブロック]
				self.RedemptionProceduresEtcInvestmentCorporationTextBlock = fact.value

			elif fact.concept.qname.localName == 'AdministrationAndOperationHeading': #管理及び運営 [目次項目]
				self.AdministrationAndOperationHeading = fact.value

			elif fact.concept.qname.localName == 'OverviewOfAssetManagementEtcHeading': #資産管理等の概要 [目次項目]
				self.OverviewOfAssetManagementEtcHeading = fact.value

			elif fact.concept.qname.localName == 'ValuationOfAssetsHeading': #資産の評価 [目次項目]
				self.ValuationOfAssetsHeading = fact.value

			elif fact.concept.qname.localName == 'ValuationOfAssetsTextBlock': #資産の評価 [テキストブロック]
				self.ValuationOfAssetsTextBlock = fact.value

			elif fact.concept.qname.localName == 'CustodyHeading': #保管 [目次項目]
				self.CustodyHeading = fact.value

			elif fact.concept.qname.localName == 'CustodyTextBlock': #保管 [テキストブロック]
				self.CustodyTextBlock = fact.value

			elif fact.concept.qname.localName == 'DurationOfInvestmentCorporationHeading': #存続期間 [目次項目]
				self.DurationOfInvestmentCorporationHeading = fact.value

			elif fact.concept.qname.localName == 'DurationOfInvestmentCorporationTextBlock': #存続期間 [テキストブロック]
				self.DurationOfInvestmentCorporationTextBlock = fact.value

			elif fact.concept.qname.localName == 'AccountingPeriodHeading': #計算期間 [目次項目]
				self.AccountingPeriodHeading = fact.value

			elif fact.concept.qname.localName == 'AccountingPeriodTextBlock': #計算期間 [テキストブロック]
				self.AccountingPeriodTextBlock = fact.value

			elif fact.concept.qname.localName == 'OtherInformationOverviewOfAssetManagementEtcHeading': #その他、資産管理等の概要 [目次項目]
				self.OtherInformationOverviewOfAssetManagementEtcHeading = fact.value

			elif fact.concept.qname.localName == 'OtherInformationOverviewOfAssetManagementEtcTextBlock': #その他、資産管理等の概要 [テキストブロック]
				self.OtherInformationOverviewOfAssetManagementEtcTextBlock = fact.value

			elif fact.concept.qname.localName == 'RestrictionsOnTradesWithInterestedPartiesHeading': #利害関係人との取引制限 [目次項目]
				self.RestrictionsOnTradesWithInterestedPartiesHeading = fact.value

			elif fact.concept.qname.localName == 'RestrictionsOnTradesWithInterestedPartiesTextBlock': #利害関係人との取引制限 [テキストブロック]
				self.RestrictionsOnTradesWithInterestedPartiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'RightsOfUnitholdersAndBondholdersOfInvestmentCorporationHeading': #投資主・投資法人債権者の権利 [目次項目]
				self.RightsOfUnitholdersAndBondholdersOfInvestmentCorporationHeading = fact.value

			elif fact.concept.qname.localName == 'RightsOfUnitholdersAndBondholdersOfInvestmentCorporationTextBlock': #投資主・投資法人債権者の権利 [テキストブロック]
				self.RightsOfUnitholdersAndBondholdersOfInvestmentCorporationTextBlock = fact.value

			elif fact.concept.qname.localName == 'OverviewOfPartiesInvolvedHeading': #関係法人の状況 [目次項目]
				self.OverviewOfPartiesInvolvedHeading = fact.value

			elif fact.concept.qname.localName == 'OverviewOfAssetManagementCompanyHeading': #資産運用会社の概況 [目次項目]
				self.OverviewOfAssetManagementCompanyHeading = fact.value

			elif fact.concept.qname.localName == 'NameStatedCapitalAndDescriptionOfBusinessOverviewOfAssetManagementCompanyHeading': #名称、資本金の額及び事業の内容、資産運用会社の概況 [目次項目]
				self.NameStatedCapitalAndDescriptionOfBusinessOverviewOfAssetManagementCompanyHeading = fact.value

			elif fact.concept.qname.localName == 'NameStatedCapitalAndDescriptionOfBusinessOverviewOfAssetManagementCompanyTextBlock': #名称、資本金の額及び事業の内容、資産運用会社の概況 [テキストブロック]
				self.NameStatedCapitalAndDescriptionOfBusinessOverviewOfAssetManagementCompanyTextBlock = fact.value

			elif fact.concept.qname.localName == 'OrganizationAndFrameworkOfInvestmentManagementOverviewOfAssetManagementCompanyHeading': #運用体制、資産運用会社の概況 [目次項目]
				self.OrganizationAndFrameworkOfInvestmentManagementOverviewOfAssetManagementCompanyHeading = fact.value

			elif fact.concept.qname.localName == 'OrganizationAndFrameworkOfInvestmentManagementOverviewOfAssetManagementCompanyTextBlock': #運用体制、資産運用会社の概況 [テキストブロック]
				self.OrganizationAndFrameworkOfInvestmentManagementOverviewOfAssetManagementCompanyTextBlock = fact.value

			elif fact.concept.qname.localName == 'MajorShareholdersOverviewOfAssetManagementCompanyHeading': #大株主の状況、資産運用会社の概況 [目次項目]
				self.MajorShareholdersOverviewOfAssetManagementCompanyHeading = fact.value

			elif fact.concept.qname.localName == 'MajorShareholdersOverviewOfAssetManagementCompanyTextBlock': #大株主の状況、資産運用会社の概況 [テキストブロック]
				self.MajorShareholdersOverviewOfAssetManagementCompanyTextBlock = fact.value

			elif fact.concept.qname.localName == 'InformationAboutOfficersOverviewOfAssetManagementCompanyHeading': #役員の状況、資産運用会社の概況 [目次項目]
				self.InformationAboutOfficersOverviewOfAssetManagementCompanyHeading = fact.value

			elif fact.concept.qname.localName == 'InformationAboutOfficersOverviewOfAssetManagementCompanyTextBlock': #役員の状況、資産運用会社の概況 [テキストブロック]
				self.InformationAboutOfficersOverviewOfAssetManagementCompanyTextBlock = fact.value

			elif fact.concept.qname.localName == 'DescriptionOfBusinessAndOverviewOfOperationOverviewOfAssetManagementCompanyHeading': #事業の内容及び営業の概況、資産運用会社の概況 [目次項目]
				self.DescriptionOfBusinessAndOverviewOfOperationOverviewOfAssetManagementCompanyHeading = fact.value

			elif fact.concept.qname.localName == 'DescriptionOfBusinessAndOverviewOfOperationOverviewOfAssetManagementCompanyTextBlock': #事業の内容及び営業の概況、資産運用会社の概況 [テキストブロック]
				self.DescriptionOfBusinessAndOverviewOfOperationOverviewOfAssetManagementCompanyTextBlock = fact.value

			elif fact.concept.qname.localName == 'OverviewOfOtherPartiesInvolvedHeading': #その他の関係法人の概況 [目次項目]
				self.OverviewOfOtherPartiesInvolvedHeading = fact.value

			elif fact.concept.qname.localName == 'OverviewOfOtherPartiesInvolvedTextBlock': #その他の関係法人の概況 [テキストブロック]
				self.OverviewOfOtherPartiesInvolvedTextBlock = fact.value

			elif fact.concept.qname.localName == 'FinancialInformationOfInvestmentCorporationHeading': #投資法人の経理状況 [目次項目]
				self.FinancialInformationOfInvestmentCorporationHeading = fact.value

			elif fact.concept.qname.localName == 'FinancialInformationOfInvestmentCorporationTextBlock': #投資法人の経理状況 [テキストブロック]
				self.FinancialInformationOfInvestmentCorporationTextBlock = fact.value

			elif fact.concept.qname.localName == 'FinancialStatementsHeading': #財務諸表 [目次項目]
				self.FinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'BalanceSheetHeading': #貸借対照表 [目次項目]
				self.BalanceSheetHeading = fact.value

			elif fact.concept.qname.localName == 'BalanceSheetTextBlock': #貸借対照表 [テキストブロック]
				self.BalanceSheetTextBlock = fact.value

			elif fact.concept.qname.localName == 'StatementOfIncomeHeading': #損益計算書 [目次項目]
				self.StatementOfIncomeHeading = fact.value

			elif fact.concept.qname.localName == 'StatementOfIncomeTextBlock': #損益計算書 [テキストブロック]
				self.StatementOfIncomeTextBlock = fact.value

			elif fact.concept.qname.localName == 'StatementOfUnitholdersEquityHeading': #投資主資本等変動計算書 [目次項目]
				self.StatementOfUnitholdersEquityHeading = fact.value

			elif fact.concept.qname.localName == 'StatementOfUnitholdersEquityTextBlock': #投資主資本等変動計算書 [テキストブロック]
				self.StatementOfUnitholdersEquityTextBlock = fact.value

			elif fact.concept.qname.localName == 'StatementOfCashDistributionHeading': #金銭の分配に係る計算書 [目次項目]
				self.StatementOfCashDistributionHeading = fact.value

			elif fact.concept.qname.localName == 'StatementOfCashDistributionTextBlock': #金銭の分配に係る計算書 [テキストブロック]
				self.StatementOfCashDistributionTextBlock = fact.value

			elif fact.concept.qname.localName == 'StatementOfCashFlowsHeading': #キャッシュ・フロー計算書 [目次項目]
				self.StatementOfCashFlowsHeading = fact.value

			elif fact.concept.qname.localName == 'StatementOfCashFlowsTextBlock': #キャッシュ・フロー計算書 [テキストブロック]
				self.StatementOfCashFlowsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesToFinancialStatementsHeading': #注記表 [目次項目]
				self.NotesToFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesToFinancialStatementsTextBlock': #注記表 [テキストブロック]
				self.NotesToFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'AnnexedDetailedSchedulesHeading': #附属明細表 [目次項目]
				self.AnnexedDetailedSchedulesHeading = fact.value

			elif fact.concept.qname.localName == 'AnnexedDetailedSchedulesTextBlock': #附属明細表 [テキストブロック]
				self.AnnexedDetailedSchedulesTextBlock = fact.value

			elif fact.concept.qname.localName == 'CurrentStatusOfInvestmentCorporationHeading': #投資法人の現況 [目次項目]
				self.CurrentStatusOfInvestmentCorporationHeading = fact.value

			elif fact.concept.qname.localName == 'CalculationOfNetAssetsHeading': #純資産額計算書 [目次項目]
				self.CalculationOfNetAssetsHeading = fact.value

			elif fact.concept.qname.localName == 'CalculationOfNetAssetsTextBlock': #純資産額計算書 [テキストブロック]
				self.CalculationOfNetAssetsTextBlock = fact.value

			elif fact.concept.qname.localName == 'HistoricalRecordsOfSalesAndBuybacksHeading': #販売及び買戻しの実績 [目次項目]
				self.HistoricalRecordsOfSalesAndBuybacksHeading = fact.value

			elif fact.concept.qname.localName == 'HistoricalRecordsOfSalesAndBuybacksTextBlock': #販売及び買戻しの実績 [テキストブロック]
				self.HistoricalRecordsOfSalesAndBuybacksTextBlock = fact.value

			elif fact.concept.qname.localName == 'PhotographsDiagramsAndOtherItemsHeading': #写真、図面その他 [目次項目]
				self.PhotographsDiagramsAndOtherItemsHeading = fact.value

			elif fact.concept.qname.localName == 'PhotographsDiagramsAndOtherItemsTextBlock': #写真、図面その他 [テキストブロック]
				self.PhotographsDiagramsAndOtherItemsTextBlock = fact.value

			elif fact.concept.qname.localName == 'IndependentAuditorsReportHeading': #独立監査人の報告書 [目次項目]
				self.IndependentAuditorsReportHeading = fact.value

			elif fact.concept.qname.localName == 'IndependentAuditorsReportInvestmentCorporationTextBlock': #独立監査人の報告書、投資法人 [テキストブロック]
				self.IndependentAuditorsReportInvestmentCorporationTextBlock = fact.value


	def getCabinetOfficeOrdinanceOnDisclosureOfInformationEtcOnSpecifiedSecuritiesFormNo43SecuritiesRegistrationStatementHeading(self): #特定有価証券の内容等の開示に関する内閣府令 第四号の三様式 有価証券届出書 [目次項目]
		return self.CabinetOfficeOrdinanceOnDisclosureOfInformationEtcOnSpecifiedSecuritiesFormNo43SecuritiesRegistrationStatementHeading

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

	def getNameOfInvestmentCorporationRelatedToDomesticInvestmentSecuritiesToRegisterForOfferingOrDistributionCoverPage(self): #届出の対象とした募集（売出）内国投資証券に係る投資法人の名称、表紙
		return self.NameOfInvestmentCorporationRelatedToDomesticInvestmentSecuritiesToRegisterForOfferingOrDistributionCoverPage

	def getLegalFormAndAmountOfDomesticInvestmentSecuritiesToRegisterForOfferingOrDistributionCoverPageTextBlock(self): #届出の対象とした募集（売出）内国投資証券の形態及び金額、表紙 [テキストブロック]
		return self.LegalFormAndAmountOfDomesticInvestmentSecuritiesToRegisterForOfferingOrDistributionCoverPageTextBlock

	def getPlaceForPublicInspectionCoverPageTextBlock(self): #縦覧に供する場所、表紙 [テキストブロック]
		return self.PlaceForPublicInspectionCoverPageTextBlock

	def getSecurityInformationHeading(self): #証券情報 [目次項目]
		return self.SecurityInformationHeading

	def getDomesticInvestmentSecuritiesOtherThanInvestmentCorporationBondsHeading(self): #内国投資証券（新投資口予約権証券及び投資法人債券を除く。） [目次項目]
		return self.DomesticInvestmentSecuritiesOtherThanInvestmentCorporationBondsHeading

	def getDomesticInvestmentSecuritiesOtherThanInvestmentUnitAcquisitionRightsAndInvestmentCorporationBondsTextBlock(self): #内国投資証券（新投資口予約権証券及び投資法人債券を除く。） [テキストブロック]
		return self.DomesticInvestmentSecuritiesOtherThanInvestmentUnitAcquisitionRightsAndInvestmentCorporationBondsTextBlock

	def getPublicOfferingOfDomesticInvestmentSecuritiesHeading(self): #募集内国投資証券 [目次項目]
		return self.PublicOfferingOfDomesticInvestmentSecuritiesHeading

	def getNameOfInvestmentCorporationPublicOfferingOfDomesticInvestmentSecuritiesHeading(self): #投資法人の名称、募集内国投資証券 [目次項目]
		return self.NameOfInvestmentCorporationPublicOfferingOfDomesticInvestmentSecuritiesHeading

	def getNameOfInvestmentCorporationPublicOfferingOfDomesticInvestmentSecuritiesTextBlock(self): #投資法人の名称、募集内国投資証券 [テキストブロック]
		return self.NameOfInvestmentCorporationPublicOfferingOfDomesticInvestmentSecuritiesTextBlock

	def getLegalFormEtcOfDomesticInvestmentSecuritiesPublicOfferingOfDomesticInvestmentSecuritiesHeading(self): #内国投資証券の形態等、募集内国投資証券 [目次項目]
		return self.LegalFormEtcOfDomesticInvestmentSecuritiesPublicOfferingOfDomesticInvestmentSecuritiesHeading

	def getLegalFormEtcOfDomesticInvestmentSecuritiesPublicOfferingOfDomesticInvestmentSecuritiesTextBlock(self): #内国投資証券の形態等、募集内国投資証券 [テキストブロック]
		return self.LegalFormEtcOfDomesticInvestmentSecuritiesPublicOfferingOfDomesticInvestmentSecuritiesTextBlock

	def getNumberOfSecuritiesToBeIssuedPublicOfferingOfDomesticInvestmentSecuritiesHeading(self): #発行数、募集内国投資証券 [目次項目]
		return self.NumberOfSecuritiesToBeIssuedPublicOfferingOfDomesticInvestmentSecuritiesHeading

	def getNumberOfSecuritiesToBeIssuedPublicOfferingOfDomesticInvestmentSecuritiesTextBlock(self): #発行数、募集内国投資証券 [テキストブロック]
		return self.NumberOfSecuritiesToBeIssuedPublicOfferingOfDomesticInvestmentSecuritiesTextBlock

	def getTotalAmountOfIssuePublicOfferingOfDomesticInvestmentSecuritiesHeading(self): #発行価額の総額、募集内国投資証券 [目次項目]
		return self.TotalAmountOfIssuePublicOfferingOfDomesticInvestmentSecuritiesHeading

	def getTotalAmountOfIssuePublicOfferingOfDomesticInvestmentSecuritiesTextBlock(self): #発行価額の総額、募集内国投資証券 [テキストブロック]
		return self.TotalAmountOfIssuePublicOfferingOfDomesticInvestmentSecuritiesTextBlock

	def getPriceOfIssuePublicOfferingOfDomesticInvestmentSecuritiesHeading(self): #発行価格、募集内国投資証券 [目次項目]
		return self.PriceOfIssuePublicOfferingOfDomesticInvestmentSecuritiesHeading

	def getPriceOfIssuePublicOfferingOfDomesticInvestmentSecuritiesTextBlock(self): #発行価格、募集内国投資証券 [テキストブロック]
		return self.PriceOfIssuePublicOfferingOfDomesticInvestmentSecuritiesTextBlock

	def getApplicationFeePublicOfferingOfDomesticInvestmentSecuritiesHeading(self): #申込手数料、募集内国投資証券 [目次項目]
		return self.ApplicationFeePublicOfferingOfDomesticInvestmentSecuritiesHeading

	def getApplicationFeePublicOfferingOfDomesticInvestmentSecuritiesTextBlock(self): #申込手数料、募集内国投資証券 [テキストブロック]
		return self.ApplicationFeePublicOfferingOfDomesticInvestmentSecuritiesTextBlock

	def getApplicationUnitPublicOfferingOfDomesticInvestmentSecuritiesHeading(self): #申込単位、募集内国投資証券 [目次項目]
		return self.ApplicationUnitPublicOfferingOfDomesticInvestmentSecuritiesHeading

	def getApplicationUnitPublicOfferingOfDomesticInvestmentSecuritiesTextBlock(self): #申込単位、募集内国投資証券 [テキストブロック]
		return self.ApplicationUnitPublicOfferingOfDomesticInvestmentSecuritiesTextBlock

	def getApplicationPeriodPublicOfferingOfDomesticInvestmentSecuritiesHeading(self): #申込期間、募集内国投資証券 [目次項目]
		return self.ApplicationPeriodPublicOfferingOfDomesticInvestmentSecuritiesHeading

	def getApplicationPeriodPublicOfferingOfDomesticInvestmentSecuritiesTextBlock(self): #申込期間、募集内国投資証券 [テキストブロック]
		return self.ApplicationPeriodPublicOfferingOfDomesticInvestmentSecuritiesTextBlock

	def getApplicationMoneyPublicOfferingOfDomesticInvestmentSecuritiesHeading(self): #申込証拠金、募集内国投資証券 [目次項目]
		return self.ApplicationMoneyPublicOfferingOfDomesticInvestmentSecuritiesHeading

	def getApplicationMoneyPublicOfferingOfDomesticInvestmentSecuritiesTextBlock(self): #申込証拠金、募集内国投資証券 [テキストブロック]
		return self.ApplicationMoneyPublicOfferingOfDomesticInvestmentSecuritiesTextBlock

	def getPlaceForApplicationPublicOfferingOfDomesticInvestmentSecuritiesHeading(self): #申込取扱場所、募集内国投資証券 [目次項目]
		return self.PlaceForApplicationPublicOfferingOfDomesticInvestmentSecuritiesHeading

	def getPlaceForApplicationPublicOfferingOfDomesticInvestmentSecuritiesTextBlock(self): #申込取扱場所、募集内国投資証券 [テキストブロック]
		return self.PlaceForApplicationPublicOfferingOfDomesticInvestmentSecuritiesTextBlock

	def getDueDateOfPaymentPublicOfferingOfDomesticInvestmentSecuritiesHeading(self): #払込期日、募集内国投資証券 [目次項目]
		return self.DueDateOfPaymentPublicOfferingOfDomesticInvestmentSecuritiesHeading

	def getDueDateOfPaymentPublicOfferingOfDomesticInvestmentSecuritiesTextBlock(self): #払込期日、募集内国投資証券 [テキストブロック]
		return self.DueDateOfPaymentPublicOfferingOfDomesticInvestmentSecuritiesTextBlock

	def getPlaceForPaymentPublicOfferingOfDomesticInvestmentSecuritiesHeading(self): #払込取扱場所、募集内国投資証券 [目次項目]
		return self.PlaceForPaymentPublicOfferingOfDomesticInvestmentSecuritiesHeading

	def getPlaceForPaymentPublicOfferingOfDomesticInvestmentSecuritiesTextBlock(self): #払込取扱場所、募集内国投資証券 [テキストブロック]
		return self.PlaceForPaymentPublicOfferingOfDomesticInvestmentSecuritiesTextBlock

	def getOverviewOfUnderwritingEtcPublicOfferingOfDomesticInvestmentSecuritiesHeading(self): #引受け等の概要、募集内国投資証券 [目次項目]
		return self.OverviewOfUnderwritingEtcPublicOfferingOfDomesticInvestmentSecuritiesHeading

	def getOverviewOfUnderwritingEtcPublicOfferingOfDomesticInvestmentSecuritiesTextBlock(self): #引受け等の概要、募集内国投資証券 [テキストブロック]
		return self.OverviewOfUnderwritingEtcPublicOfferingOfDomesticInvestmentSecuritiesTextBlock

	def getBookEntryTransferInstitutionPublicOfferingOfDomesticInvestmentSecuritiesHeading(self): #振替機関に関する事項、募集内国投資証券 [目次項目]
		return self.BookEntryTransferInstitutionPublicOfferingOfDomesticInvestmentSecuritiesHeading

	def getBookEntryTransferInstitutionPublicOfferingOfDomesticInvestmentSecuritiesTextBlock(self): #振替機関に関する事項、募集内国投資証券 [テキストブロック]
		return self.BookEntryTransferInstitutionPublicOfferingOfDomesticInvestmentSecuritiesTextBlock

	def getUseOfNetProceedsPublicOfferingOfDomesticInvestmentSecuritiesHeading(self): #手取金の使途、募集内国投資証券 [目次項目]
		return self.UseOfNetProceedsPublicOfferingOfDomesticInvestmentSecuritiesHeading

	def getUseOfNetProceedsPublicOfferingOfDomesticInvestmentSecuritiesTextBlock(self): #手取金の使途、募集内国投資証券 [テキストブロック]
		return self.UseOfNetProceedsPublicOfferingOfDomesticInvestmentSecuritiesTextBlock

	def getOtherInformationPublicOfferingOfDomesticInvestmentSecuritiesHeading(self): #その他、募集内国投資証券 [目次項目]
		return self.OtherInformationPublicOfferingOfDomesticInvestmentSecuritiesHeading

	def getOtherInformationPublicOfferingOfDomesticInvestmentSecuritiesTextBlock(self): #その他、募集内国投資証券 [テキストブロック]
		return self.OtherInformationPublicOfferingOfDomesticInvestmentSecuritiesTextBlock

	def getSecondaryDistributionOfDomesticInvestmentSecuritiesHeading(self): #売出内国投資証券 [目次項目]
		return self.SecondaryDistributionOfDomesticInvestmentSecuritiesHeading

	def getNameOfInvestmentCorporationSecondaryDistributionOfDomesticInvestmentSecuritiesHeading(self): #投資法人の名称、売出内国投資証券 [目次項目]
		return self.NameOfInvestmentCorporationSecondaryDistributionOfDomesticInvestmentSecuritiesHeading

	def getNameOfInvestmentCorporationSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock(self): #投資法人の名称、売出内国投資証券 [テキストブロック]
		return self.NameOfInvestmentCorporationSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock

	def getLegalFormEtcOfDomesticInvestmentSecuritiesSecondaryDistributionOfDomesticInvestmentSecuritiesHeading(self): #内国投資証券の形態等、売出内国投資証券 [目次項目]
		return self.LegalFormEtcOfDomesticInvestmentSecuritiesSecondaryDistributionOfDomesticInvestmentSecuritiesHeading

	def getLegalFormEtcOfDomesticInvestmentSecuritiesSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock(self): #内国投資証券の形態等、売出内国投資証券 [テキストブロック]
		return self.LegalFormEtcOfDomesticInvestmentSecuritiesSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock

	def getNumberOfSecuritiesToBeDistributedSecondaryDistributionOfDomesticInvestmentSecuritiesHeading(self): #売出数、売出内国投資証券 [目次項目]
		return self.NumberOfSecuritiesToBeDistributedSecondaryDistributionOfDomesticInvestmentSecuritiesHeading

	def getNumberOfSecuritiesToBeDistributedSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock(self): #売出数、売出内国投資証券 [テキストブロック]
		return self.NumberOfSecuritiesToBeDistributedSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock

	def getTotalAmountOfSecondaryDistributionSecondaryDistributionOfDomesticInvestmentSecuritiesHeading(self): #売出価額の総額、売出内国投資証券 [目次項目]
		return self.TotalAmountOfSecondaryDistributionSecondaryDistributionOfDomesticInvestmentSecuritiesHeading

	def getTotalAmountOfSecondaryDistributionSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock(self): #売出価額の総額、売出内国投資証券 [テキストブロック]
		return self.TotalAmountOfSecondaryDistributionSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock

	def getPriceOfSecondaryDistributionSecondaryDistributionOfDomesticInvestmentSecuritiesHeading(self): #売出価格、売出内国投資証券 [目次項目]
		return self.PriceOfSecondaryDistributionSecondaryDistributionOfDomesticInvestmentSecuritiesHeading

	def getPriceOfSecondaryDistributionSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock(self): #売出価格、売出内国投資証券 [テキストブロック]
		return self.PriceOfSecondaryDistributionSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock

	def getApplicationFeeSecondaryDistributionOfDomesticInvestmentSecuritiesHeading(self): #申込手数料、売出内国投資証券 [目次項目]
		return self.ApplicationFeeSecondaryDistributionOfDomesticInvestmentSecuritiesHeading

	def getApplicationFeeSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock(self): #申込手数料、売出内国投資証券 [テキストブロック]
		return self.ApplicationFeeSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock

	def getApplicationUnitSecondaryDistributionOfDomesticInvestmentSecuritiesHeading(self): #申込単位、売出内国投資証券 [目次項目]
		return self.ApplicationUnitSecondaryDistributionOfDomesticInvestmentSecuritiesHeading

	def getApplicationUnitSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock(self): #申込単位、売出内国投資証券 [テキストブロック]
		return self.ApplicationUnitSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock

	def getApplicationPeriodSecondaryDistributionOfDomesticInvestmentSecuritiesHeading(self): #申込期間、売出内国投資証券 [目次項目]
		return self.ApplicationPeriodSecondaryDistributionOfDomesticInvestmentSecuritiesHeading

	def getApplicationPeriodSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock(self): #申込期間、売出内国投資証券 [テキストブロック]
		return self.ApplicationPeriodSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock

	def getApplicationMoneySecondaryDistributionOfDomesticInvestmentSecuritiesHeading(self): #申込証拠金、売出内国投資証券 [目次項目]
		return self.ApplicationMoneySecondaryDistributionOfDomesticInvestmentSecuritiesHeading

	def getApplicationMoneySecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock(self): #申込証拠金、売出内国投資証券 [テキストブロック]
		return self.ApplicationMoneySecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock

	def getPlaceForApplicationSecondaryDistributionOfDomesticInvestmentSecuritiesHeading(self): #申込取扱場所、売出内国投資証券 [目次項目]
		return self.PlaceForApplicationSecondaryDistributionOfDomesticInvestmentSecuritiesHeading

	def getPlaceForApplicationSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock(self): #申込取扱場所、売出内国投資証券 [テキストブロック]
		return self.PlaceForApplicationSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock

	def getSettlementDateSecondaryDistributionOfDomesticInvestmentSecuritiesHeading(self): #受渡期日、売出内国投資証券 [目次項目]
		return self.SettlementDateSecondaryDistributionOfDomesticInvestmentSecuritiesHeading

	def getSettlementDateSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock(self): #受渡期日、売出内国投資証券 [テキストブロック]
		return self.SettlementDateSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock

	def getPlaceForPaymentSecondaryDistributionOfDomesticInvestmentSecuritiesHeading(self): #払込取扱場所、売出内国投資証券 [目次項目]
		return self.PlaceForPaymentSecondaryDistributionOfDomesticInvestmentSecuritiesHeading

	def getPlaceForPaymentSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock(self): #払込取扱場所、売出内国投資証券 [テキストブロック]
		return self.PlaceForPaymentSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock

	def getOverviewOfUnderwritingEtcSecondaryDistributionOfDomesticInvestmentSecuritiesHeading(self): #引受け等の概要、売出内国投資証券 [目次項目]
		return self.OverviewOfUnderwritingEtcSecondaryDistributionOfDomesticInvestmentSecuritiesHeading

	def getOverviewOfUnderwritingEtcSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock(self): #引受け等の概要、売出内国投資証券 [テキストブロック]
		return self.OverviewOfUnderwritingEtcSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock

	def getBookEntryTransferInstitutionSecondaryDistributionOfDomesticInvestmentSecuritiesHeading(self): #振替機関に関する事項、売出内国投資証券 [目次項目]
		return self.BookEntryTransferInstitutionSecondaryDistributionOfDomesticInvestmentSecuritiesHeading

	def getBookEntryTransferInstitutionSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock(self): #振替機関に関する事項、売出内国投資証券 [テキストブロック]
		return self.BookEntryTransferInstitutionSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock

	def getUseOfNetProceedsSecondaryDistributionOfDomesticInvestmentSecuritiesHeading(self): #手取金の使途、売出内国投資証券 [目次項目]
		return self.UseOfNetProceedsSecondaryDistributionOfDomesticInvestmentSecuritiesHeading

	def getUseOfNetProceedsSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock(self): #手取金の使途、売出内国投資証券 [テキストブロック]
		return self.UseOfNetProceedsSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock

	def getOtherInformationSecondaryDistributionOfDomesticInvestmentSecuritiesHeading(self): #その他、売出内国投資証券 [目次項目]
		return self.OtherInformationSecondaryDistributionOfDomesticInvestmentSecuritiesHeading

	def getOtherInformationSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock(self): #その他、売出内国投資証券 [テキストブロック]
		return self.OtherInformationSecondaryDistributionOfDomesticInvestmentSecuritiesTextBlock

	def getSubscriptionRightsToSharesOfInvestmentCorporationHeading(self): #新投資口予約権証券 [目次項目]
		return self.SubscriptionRightsToSharesOfInvestmentCorporationHeading

	def getInvestmentUnitAcquisitionRightsTextBlock(self): #新投資口予約権証券 [テキストブロック]
		return self.InvestmentUnitAcquisitionRightsTextBlock

	def getNameOfInvestmentCorporationSubscriptionRightsToSharesOfInvestmentCorporationHeading(self): #投資法人の名称、新投資口予約権証券 [目次項目]
		return self.NameOfInvestmentCorporationSubscriptionRightsToSharesOfInvestmentCorporationHeading

	def getNameOfInvestmentCorporationSubscriptionRightsToSharesOfInvestmentCorporationTextBlock(self): #投資法人の名称、新投資口予約権証券 [テキストブロック]
		return self.NameOfInvestmentCorporationSubscriptionRightsToSharesOfInvestmentCorporationTextBlock

	def getLegalFormEtcOfSubscriptionRightsToSharesOfInvestmentCorporationHeading(self): #新投資口予約権証券の形態等 [目次項目]
		return self.LegalFormEtcOfSubscriptionRightsToSharesOfInvestmentCorporationHeading

	def getLegalFormEtcOfSubscriptionRightsToSharesOfInvestmentCorporationTextBlock(self): #新投資口予約権証券の形態等 [テキストブロック]
		return self.LegalFormEtcOfSubscriptionRightsToSharesOfInvestmentCorporationTextBlock

	def getNumberOfSecuritiesToBeIssuedSubscriptionRightsToSharesOfInvestmentCorporationHeading(self): #発行数、新投資口予約権証券 [目次項目]
		return self.NumberOfSecuritiesToBeIssuedSubscriptionRightsToSharesOfInvestmentCorporationHeading

	def getNumberOfSecuritiesToBeIssuedSubscriptionRightsToSharesOfInvestmentCorporationTextBlock(self): #発行数、新投資口予約権証券 [テキストブロック]
		return self.NumberOfSecuritiesToBeIssuedSubscriptionRightsToSharesOfInvestmentCorporationTextBlock

	def getDateOfAllotmentSubscriptionRightsToSharesOfInvestmentCorporationHeading(self): #割当日、新投資口予約権証券 [目次項目]
		return self.DateOfAllotmentSubscriptionRightsToSharesOfInvestmentCorporationHeading

	def getDateOfAllotmentSubscriptionRightsToSharesOfInvestmentCorporationTextBlock(self): #割当日、新投資口予約権証券 [テキストブロック]
		return self.DateOfAllotmentSubscriptionRightsToSharesOfInvestmentCorporationTextBlock

	def getParticularsOfSubscriptionRightsToSharesOfInvestmentCorporationHeading(self): #新投資口予約権の内容 [目次項目]
		return self.ParticularsOfSubscriptionRightsToSharesOfInvestmentCorporationHeading

	def getParticularsOfSubscriptionRightsToSharesOfInvestmentCorporationTextBlock(self): #新投資口予約権の内容 [テキストブロック]
		return self.ParticularsOfSubscriptionRightsToSharesOfInvestmentCorporationTextBlock

	def getLegalFormEtcOfDomesticInvestmentSecuritiesUnderlyingSubscriptionRightsToSharesOfInvestmentCorporationHeading(self): #新投資口予約権の目的となる内国投資証券の形態等 [目次項目]
		return self.LegalFormEtcOfDomesticInvestmentSecuritiesUnderlyingSubscriptionRightsToSharesOfInvestmentCorporationHeading

	def getLegalFormEtcOfDomesticInvestmentSecuritiesUnderlyingSubscriptionRightsToSharesOfInvestmentCorporationTextBlock(self): #新投資口予約権の目的となる内国投資証券の形態等 [テキストブロック]
		return self.LegalFormEtcOfDomesticInvestmentSecuritiesUnderlyingSubscriptionRightsToSharesOfInvestmentCorporationTextBlock

	def getNumberOfDomesticInvestmentSecuritiesUnderlyingSubscriptionRightsToSharesOfInvestmentCorporationHeading(self): #新投資口予約権の目的となる内国投資証券の数 [目次項目]
		return self.NumberOfDomesticInvestmentSecuritiesUnderlyingSubscriptionRightsToSharesOfInvestmentCorporationHeading

	def getNumberOfDomesticInvestmentSecuritiesUnderlyingSubscriptionRightsToSharesOfInvestmentCorporationTextBlock(self): #新投資口予約権の目的となる内国投資証券の数 [テキストブロック]
		return self.NumberOfDomesticInvestmentSecuritiesUnderlyingSubscriptionRightsToSharesOfInvestmentCorporationTextBlock

	def getAmountOfPaymentWhenSubscriptionRightToShareOfInvestmentCorporationIsExercisedHeading(self): #新投資口予約権の行使時の払込金額 [目次項目]
		return self.AmountOfPaymentWhenSubscriptionRightToShareOfInvestmentCorporationIsExercisedHeading

	def getAmountOfPaymentWhenSubscriptionRightToShareOfInvestmentCorporationIsExercisedTextBlock(self): #新投資口予約権の行使時の払込金額 [テキストブロック]
		return self.AmountOfPaymentWhenSubscriptionRightToShareOfInvestmentCorporationIsExercisedTextBlock

	def getTotalAmountOfDomesticInvestmentSecuritiesToBeIssuedWhenSubscriptionRightsToSharesOfInvestmentCorporationAreExercisedHeading(self): #新投資口予約権の行使により発行する内国投資証券の発行価額の総額 [目次項目]
		return self.TotalAmountOfDomesticInvestmentSecuritiesToBeIssuedWhenSubscriptionRightsToSharesOfInvestmentCorporationAreExercisedHeading

	def getTotalAmountOfDomesticInvestmentSecuritiesToBeIssuedWhenSubscriptionRightsToSharesOfInvestmentCorporationAreExercisedTextBlock(self): #新投資口予約権の行使により発行する内国投資証券の発行価額の総額 [テキストブロック]
		return self.TotalAmountOfDomesticInvestmentSecuritiesToBeIssuedWhenSubscriptionRightsToSharesOfInvestmentCorporationAreExercisedTextBlock

	def getExercisePeriodOfSubscriptionRightsToSharesOfInvestmentCorporationHeading(self): #新投資口予約権の行使期間 [目次項目]
		return self.ExercisePeriodOfSubscriptionRightsToSharesOfInvestmentCorporationHeading

	def getExercisePeriodOfSubscriptionRightsToSharesOfInvestmentCorporationTextBlock(self): #新投資口予約権の行使期間 [テキストブロック]
		return self.ExercisePeriodOfSubscriptionRightsToSharesOfInvestmentCorporationTextBlock

	def getCustodianAgentAndPlaceOfPaymentForExerciseOfSubscriptionRightsToSharesOfInvestmentCorporationHeading(self): #新投資口予約権の行使請求の受付場所、取次場所及び払込取扱場所 [目次項目]
		return self.CustodianAgentAndPlaceOfPaymentForExerciseOfSubscriptionRightsToSharesOfInvestmentCorporationHeading

	def getCustodianAgentAndPlaceOfPaymentForExerciseOfSubscriptionRightsToSharesOfInvestmentCorporationTextBlock(self): #新投資口予約権の行使請求の受付場所、取次場所及び払込取扱場所 [テキストブロック]
		return self.CustodianAgentAndPlaceOfPaymentForExerciseOfSubscriptionRightsToSharesOfInvestmentCorporationTextBlock

	def getTermsOfExerciseOfSubscriptionRightsToSharesOfInvestmentCorporationHeading(self): #新投資口予約権の行使の条件 [目次項目]
		return self.TermsOfExerciseOfSubscriptionRightsToSharesOfInvestmentCorporationHeading

	def getTermsOfExerciseOfSubscriptionRightsToSharesOfInvestmentCorporationTextBlock(self): #新投資口予約権の行使の条件 [テキストブロック]
		return self.TermsOfExerciseOfSubscriptionRightsToSharesOfInvestmentCorporationTextBlock

	def getReasonAndTermsOfAcquisitionOfTreasurySubscriptionRightsToSharesOfInvestmentCorporationHeading(self): #自己新投資口予約権の取得の事由及び取得の条件 [目次項目]
		return self.ReasonAndTermsOfAcquisitionOfTreasurySubscriptionRightsToSharesOfInvestmentCorporationHeading

	def getReasonAndTermsOfAcquisitionOfTreasurySubscriptionRightsToSharesOfInvestmentCorporationTextBlock(self): #自己新投資口予約権の取得の事由及び取得の条件 [テキストブロック]
		return self.ReasonAndTermsOfAcquisitionOfTreasurySubscriptionRightsToSharesOfInvestmentCorporationTextBlock

	def getInformationAboutTransferOfSubscriptionRightsToSharesOfInvestmentCorporationHeading(self): #新投資口予約権の譲渡に関する事項 [目次項目]
		return self.InformationAboutTransferOfSubscriptionRightsToSharesOfInvestmentCorporationHeading

	def getInformationAboutTransferOfSubscriptionRightsToSharesOfInvestmentCorporationTextBlock(self): #新投資口予約権の譲渡に関する事項 [テキストブロック]
		return self.InformationAboutTransferOfSubscriptionRightsToSharesOfInvestmentCorporationTextBlock

	def getOverviewOfUnderwritingEtcSubscriptionRightsToSharesOfInvestmentCorporationHeading(self): #引受け等の概要、新投資口予約権証券 [目次項目]
		return self.OverviewOfUnderwritingEtcSubscriptionRightsToSharesOfInvestmentCorporationHeading

	def getOverviewOfUnderwritingEtcSubscriptionRightsToSharesOfInvestmentCorporationTextBlock(self): #引受け等の概要、新投資口予約権証券 [テキストブロック]
		return self.OverviewOfUnderwritingEtcSubscriptionRightsToSharesOfInvestmentCorporationTextBlock

	def getBookEntryTransferInstitutionSubscriptionRightsToSharesOfInvestmentCorporationHeading(self): #振替機関に関する事項、新投資口予約権証券 [目次項目]
		return self.BookEntryTransferInstitutionSubscriptionRightsToSharesOfInvestmentCorporationHeading

	def getBookEntryTransferInstitutionSubscriptionRightsToSharesOfInvestmentCorporationTextBlock(self): #振替機関に関する事項、新投資口予約権証券 [テキストブロック]
		return self.BookEntryTransferInstitutionSubscriptionRightsToSharesOfInvestmentCorporationTextBlock

	def getUseOfNetProceedsSubscriptionRightsToSharesOfInvestmentCorporationHeading(self): #手取金の使途、新投資口予約権証券 [目次項目]
		return self.UseOfNetProceedsSubscriptionRightsToSharesOfInvestmentCorporationHeading

	def getUseOfNetProceedsSubscriptionRightsToSharesOfInvestmentCorporationTextBlock(self): #手取金の使途、新投資口予約権証券 [テキストブロック]
		return self.UseOfNetProceedsSubscriptionRightsToSharesOfInvestmentCorporationTextBlock

	def getOtherInformationSubscriptionRightsToSharesOfInvestmentCorporationHeading(self): #その他、新投資口予約権証券 [目次項目]
		return self.OtherInformationSubscriptionRightsToSharesOfInvestmentCorporationHeading

	def getOtherInformationSubscriptionRightsToSharesOfInvestmentCorporationTextBlock(self): #その他、新投資口予約権証券 [テキストブロック]
		return self.OtherInformationSubscriptionRightsToSharesOfInvestmentCorporationTextBlock

	def getInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading(self): #投資法人債券（短期投資法人債を除く。） [目次項目]
		return self.InvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading

	def getInvestmentCorporationBondsOtherThanShortTermOnesTextBlock(self): #投資法人債券（短期投資法人債を除く。） [テキストブロック]
		return self.InvestmentCorporationBondsOtherThanShortTermOnesTextBlock

	def getSecurityTitlesHeading(self): #銘柄 [目次項目]
		return self.SecurityTitlesHeading

	def getSecurityTitlesTextBlock(self): #銘柄 [テキストブロック]
		return self.SecurityTitlesTextBlock

	def getLegalFormEtcOfInvestmentCorporationBondsHeading(self): #投資法人債券の形態等 [目次項目]
		return self.LegalFormEtcOfInvestmentCorporationBondsHeading

	def getLegalFormEtcOfInvestmentCorporationBondsTextBlock(self): #投資法人債券の形態等 [テキストブロック]
		return self.LegalFormEtcOfInvestmentCorporationBondsTextBlock

	def getTotalFaceValueHeading(self): #券面総額 [目次項目]
		return self.TotalFaceValueHeading

	def getTotalFaceValueTextBlock(self): #券面総額 [テキストブロック]
		return self.TotalFaceValueTextBlock

	def getAmountOfEachOfInvestmentCorporationBondsHeading(self): #各投資法人債の金額 [目次項目]
		return self.AmountOfEachOfInvestmentCorporationBondsHeading

	def getAmountOfEachOfInvestmentCorporationBondsTextBlock(self): #各投資法人債の金額 [テキストブロック]
		return self.AmountOfEachOfInvestmentCorporationBondsTextBlock

	def getTotalAmountOfIssueOrSecondaryDistributionInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading(self): #発行（売出）価額の総額、投資法人債券（短期投資法人債を除く。） [目次項目]
		return self.TotalAmountOfIssueOrSecondaryDistributionInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading

	def getTotalAmountOfIssueOrSecondaryDistributionInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock(self): #発行（売出）価額の総額、投資法人債券（短期投資法人債を除く。） [テキストブロック]
		return self.TotalAmountOfIssueOrSecondaryDistributionInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock

	def getPriceOfIssueOrSecondaryDistributionInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading(self): #発行（売出）価格、投資法人債券（短期投資法人債を除く。） [目次項目]
		return self.PriceOfIssueOrSecondaryDistributionInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading

	def getPriceOfIssueOrSecondaryDistributionInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock(self): #発行（売出）価格、投資法人債券（短期投資法人債を除く。） [テキストブロック]
		return self.PriceOfIssueOrSecondaryDistributionInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock

	def getInterestRateHeading(self): #利率 [目次項目]
		return self.InterestRateHeading

	def getInterestRateTextBlock(self): #利率 [テキストブロック]
		return self.InterestRateTextBlock

	def getDateAndMethodOfInterestPaymentHeading(self): #利払日及び利息支払の方法 [目次項目]
		return self.DateAndMethodOfInterestPaymentHeading

	def getDateAndMethodOfInterestPaymentTextBlock(self): #利払日及び利息支払の方法 [テキストブロック]
		return self.DateAndMethodOfInterestPaymentTextBlock

	def getDateAndMethodOfRedemptionHeading(self): #償還期限及び償還の方法 [目次項目]
		return self.DateAndMethodOfRedemptionHeading

	def getDateAndMethodOfRedemptionTextBlock(self): #償還期限及び償還の方法 [テキストブロック]
		return self.DateAndMethodOfRedemptionTextBlock

	def getMethodOfPublicOfferingInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading(self): #募集の方法、投資法人債券（短期投資法人債を除く。） [目次項目]
		return self.MethodOfPublicOfferingInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading

	def getMethodOfPublicOfferingInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock(self): #募集の方法、投資法人債券（短期投資法人債を除く。） [テキストブロック]
		return self.MethodOfPublicOfferingInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock

	def getApplicationMoneyInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading(self): #申込証拠金、投資法人債券（短期投資法人債を除く。） [目次項目]
		return self.ApplicationMoneyInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading

	def getApplicationMoneyInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock(self): #申込証拠金、投資法人債券（短期投資法人債を除く。） [テキストブロック]
		return self.ApplicationMoneyInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock

	def getApplicationPeriodInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading(self): #申込期間、投資法人債券（短期投資法人債を除く。） [目次項目]
		return self.ApplicationPeriodInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading

	def getApplicationPeriodInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock(self): #申込期間、投資法人債券（短期投資法人債を除く。） [テキストブロック]
		return self.ApplicationPeriodInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock

	def getPlaceForApplicationInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading(self): #申込取扱場所、投資法人債券（短期投資法人債を除く。） [目次項目]
		return self.PlaceForApplicationInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading

	def getPlaceForApplicationInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock(self): #申込取扱場所、投資法人債券（短期投資法人債を除く。） [テキストブロック]
		return self.PlaceForApplicationInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock

	def getDueDateOfPaymentInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading(self): #払込期日、投資法人債券（短期投資法人債を除く。） [目次項目]
		return self.DueDateOfPaymentInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading

	def getDueDateOfPaymentInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock(self): #払込期日、投資法人債券（短期投資法人債を除く。） [テキストブロック]
		return self.DueDateOfPaymentInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock

	def getPlaceForPaymentInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading(self): #払込取扱場所、投資法人債券（短期投資法人債を除く。） [目次項目]
		return self.PlaceForPaymentInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading

	def getPlaceForPaymentInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock(self): #払込取扱場所、投資法人債券（短期投資法人債を除く。） [テキストブロック]
		return self.PlaceForPaymentInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock

	def getOverviewOfUnderwritingEtcInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading(self): #引受け等の概要、投資法人債券（短期投資法人債を除く。） [目次項目]
		return self.OverviewOfUnderwritingEtcInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading

	def getOverviewOfUnderwritingEtcInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock(self): #引受け等の概要、投資法人債券（短期投資法人債を除く。） [テキストブロック]
		return self.OverviewOfUnderwritingEtcInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock

	def getAdministratorOfInvestmentCorporationBondsHeading(self): #投資法人債管理者又は投資法人債の管理会社 [目次項目]
		return self.AdministratorOfInvestmentCorporationBondsHeading

	def getAdministratorOfInvestmentCorporationBondsTextBlock(self): #投資法人債管理者又は投資法人債の管理会社 [テキストブロック]
		return self.AdministratorOfInvestmentCorporationBondsTextBlock

	def getBookEntryTransferInstitutionInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading(self): #振替機関に関する事項、投資法人債券（短期投資法人債を除く。） [目次項目]
		return self.BookEntryTransferInstitutionInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading

	def getBookEntryTransferInstitutionInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock(self): #振替機関に関する事項、投資法人債券（短期投資法人債を除く。） [テキストブロック]
		return self.BookEntryTransferInstitutionInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock

	def getRegistrationDateAndRegistrationNumberOfInvestmentCorporationHeading(self): #投資法人の登録年月日及び登録番号 [目次項目]
		return self.RegistrationDateAndRegistrationNumberOfInvestmentCorporationHeading

	def getRegistrationDateAndRegistrationNumberOfInvestmentCorporationTextBlock(self): #投資法人の登録年月日及び登録番号 [テキストブロック]
		return self.RegistrationDateAndRegistrationNumberOfInvestmentCorporationTextBlock

	def getUseOfNetProceedsInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading(self): #手取金の使途、投資法人債券（短期投資法人債を除く。） [目次項目]
		return self.UseOfNetProceedsInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading

	def getUseOfNetProceedsInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock(self): #手取金の使途、投資法人債券（短期投資法人債を除く。） [テキストブロック]
		return self.UseOfNetProceedsInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock

	def getOtherInformationInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading(self): #その他、投資法人債券（短期投資法人債を除く。） [目次項目]
		return self.OtherInformationInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsHeading

	def getOtherInformationInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock(self): #その他、投資法人債券（短期投資法人債を除く。） [テキストブロック]
		return self.OtherInformationInvestmentCorporationBondsOtherThanShortTermInvestmentCorporationBondsTextBlock

	def getShortTermInvestmentCorporationBondsHeading(self): #短期投資法人債 [目次項目]
		return self.ShortTermInvestmentCorporationBondsHeading

	def getShortTermInvestmentCorporationBondsTextBlock(self): #短期投資法人債 [テキストブロック]
		return self.ShortTermInvestmentCorporationBondsTextBlock

	def getTotalAmountOfIssueOrSecondaryDistributionOfShortTermInvestmentCorporationBondsHeading(self): #発行（売出）短期投資法人債の総額 [目次項目]
		return self.TotalAmountOfIssueOrSecondaryDistributionOfShortTermInvestmentCorporationBondsHeading

	def getTotalAmountOfIssueOrSecondaryDistributionOfShortTermInvestmentCorporationBondsTextBlock(self): #発行（売出）短期投資法人債の総額 [テキストブロック]
		return self.TotalAmountOfIssueOrSecondaryDistributionOfShortTermInvestmentCorporationBondsTextBlock

	def getTotalAmountOfIssueOrSecondaryDistributionShortTermInvestmentCorporationBondsHeading(self): #発行（売出）価額の総額、短期投資法人債 [目次項目]
		return self.TotalAmountOfIssueOrSecondaryDistributionShortTermInvestmentCorporationBondsHeading

	def getTotalAmountOfIssueOrSecondaryDistributionShortTermInvestmentCorporationBondsTextBlock(self): #発行（売出）価額の総額、短期投資法人債 [テキストブロック]
		return self.TotalAmountOfIssueOrSecondaryDistributionShortTermInvestmentCorporationBondsTextBlock

	def getPriceOfIssueOrSecondaryDistributionShortTermInvestmentCorporationBondsHeading(self): #発行（売出）価格、短期投資法人債 [目次項目]
		return self.PriceOfIssueOrSecondaryDistributionShortTermInvestmentCorporationBondsHeading

	def getPriceOfIssueOrSecondaryDistributionShortTermInvestmentCorporationBondsTextBlock(self): #発行（売出）価格、短期投資法人債 [テキストブロック]
		return self.PriceOfIssueOrSecondaryDistributionShortTermInvestmentCorporationBondsTextBlock

	def getLimitOnAmountOfIssueHeading(self): #発行限度額 [目次項目]
		return self.LimitOnAmountOfIssueHeading

	def getLimitOnAmountOfIssueTextBlock(self): #発行限度額 [テキストブロック]
		return self.LimitOnAmountOfIssueTextBlock

	def getRemainingBalanceOfLimitOnAmountOfIssueHeading(self): #発行限度額残高 [目次項目]
		return self.RemainingBalanceOfLimitOnAmountOfIssueHeading

	def getRemainingBalanceOfLimitOnAmountOfIssueTextBlock(self): #発行限度額残高 [テキストブロック]
		return self.RemainingBalanceOfLimitOnAmountOfIssueTextBlock

	def getDueDateOfPaymentHeading(self): #支払期日 [目次項目]
		return self.DueDateOfPaymentHeading

	def getDueDateOfPaymentTextBlock(self): #支払期日 [テキストブロック]
		return self.DueDateOfPaymentTextBlock

	def getPlaceForPaymentHeading(self): #支払場所 [目次項目]
		return self.PlaceForPaymentHeading

	def getPlaceForPaymentTextBlock(self): #支払場所 [テキストブロック]
		return self.PlaceForPaymentTextBlock

	def getBookEntryTransferInstitutionShortTermInvestmentCorporationBondsHeading(self): #振替機関に関する事項、短期投資法人債 [目次項目]
		return self.BookEntryTransferInstitutionShortTermInvestmentCorporationBondsHeading

	def getBookEntryTransferInstitutionShortTermInvestmentCorporationBondsTextBlock(self): #振替機関に関する事項、短期投資法人債 [テキストブロック]
		return self.BookEntryTransferInstitutionShortTermInvestmentCorporationBondsTextBlock

	def getFinancialInstitutionProvidingBackupLineHeading(self): #バックアップラインの設定金融機関 [目次項目]
		return self.FinancialInstitutionProvidingBackupLineHeading

	def getFinancialInstitutionProvidingBackupLineTextBlock(self): #バックアップラインの設定金融機関 [テキストブロック]
		return self.FinancialInstitutionProvidingBackupLineTextBlock

	def getDescriptionOfBackupLineHeading(self): #バックアップラインの設定内容 [目次項目]
		return self.DescriptionOfBackupLineHeading

	def getDescriptionOfBackupLineTextBlock(self): #バックアップラインの設定内容 [テキストブロック]
		return self.DescriptionOfBackupLineTextBlock

	def getRatingHeading(self): #取得格付 [目次項目]
		return self.RatingHeading

	def getRatingTextBlock(self): #取得格付 [テキストブロック]
		return self.RatingTextBlock

	def getSpecialDisclosureAboutPublicOfferingOrSecondaryDistributionHeading(self): #募集又は売出しに関する特別記載事項 [目次項目]
		return self.SpecialDisclosureAboutPublicOfferingOrSecondaryDistributionHeading

	def getSpecialDisclosureAboutPublicOfferingOrSecondaryDistributionTextBlock(self): #募集又は売出しに関する特別記載事項 [テキストブロック]
		return self.SpecialDisclosureAboutPublicOfferingOrSecondaryDistributionTextBlock

	def getFundInformationHeading(self): #ファンド情報 [目次項目]
		return self.FundInformationHeading

	def getOverviewOfFundHeading(self): #ファンドの状況 [目次項目]
		return self.OverviewOfFundHeading

	def getOverviewOfInvestmentCorporationHeading(self): #投資法人の概況 [目次項目]
		return self.OverviewOfInvestmentCorporationHeading

	def getSummaryOfBusinessResultsHeading(self): #主要な経営指標等の推移 [目次項目]
		return self.SummaryOfBusinessResultsHeading

	def getSummaryOfBusinessResultsTextBlock(self): #主要な経営指標等の推移 [テキストブロック]
		return self.SummaryOfBusinessResultsTextBlock

	def getPurposesAndBasicFeaturesOfInvestmentCorporationHeading(self): #投資法人の目的及び基本的性格 [目次項目]
		return self.PurposesAndBasicFeaturesOfInvestmentCorporationHeading

	def getPurposesAndBasicFeaturesOfInvestmentCorporationTextBlock(self): #投資法人の目的及び基本的性格 [テキストブロック]
		return self.PurposesAndBasicFeaturesOfInvestmentCorporationTextBlock

	def getSchemeOfInvestmentCorporationHeading(self): #投資法人の仕組み [目次項目]
		return self.SchemeOfInvestmentCorporationHeading

	def getSchemeOfInvestmentCorporationTextBlock(self): #投資法人の仕組み [テキストブロック]
		return self.SchemeOfInvestmentCorporationTextBlock

	def getOrganizationOfInvestmentCorporationHeading(self): #投資法人の機構 [目次項目]
		return self.OrganizationOfInvestmentCorporationHeading

	def getOrganizationOfInvestmentCorporationTextBlock(self): #投資法人の機構 [テキストブロック]
		return self.OrganizationOfInvestmentCorporationTextBlock

	def getPaidInCapitalOfInvestmentCorporationHeading(self): #投資法人の出資総額 [目次項目]
		return self.PaidInCapitalOfInvestmentCorporationHeading

	def getPaidInCapitalOfInvestmentCorporationTextBlock(self): #投資法人の出資総額 [テキストブロック]
		return self.PaidInCapitalOfInvestmentCorporationTextBlock

	def getMajorUnitholdersHeading(self): #主要な投資主の状況 [目次項目]
		return self.MajorUnitholdersHeading

	def getMajorUnitholdersTextBlock(self): #主要な投資主の状況 [テキストブロック]
		return self.MajorUnitholdersTextBlock

	def getShareOwnershipProgramForEmployeesOfAssetManagementCompanyHeading(self): #資産運用会社従業員等投資口所有制度の内容 [目次項目]
		return self.ShareOwnershipProgramForEmployeesOfAssetManagementCompanyHeading

	def getShareOwnershipProgramForEmployeesOfAssetManagementCompanyTextBlock(self): #資産運用会社従業員等投資口所有制度の内容 [テキストブロック]
		return self.ShareOwnershipProgramForEmployeesOfAssetManagementCompanyTextBlock

	def getInvestmentPolicyOverviewOfFundHeading(self): #投資方針、ファンドの状況 [目次項目]
		return self.InvestmentPolicyOverviewOfFundHeading

	def getInvestmentPolicyHeading(self): #投資方針 [目次項目]
		return self.InvestmentPolicyHeading

	def getInvestmentPolicyTextBlock(self): #投資方針 [テキストブロック]
		return self.InvestmentPolicyTextBlock

	def getThingsToInvestInHeading(self): #投資対象 [目次項目]
		return self.ThingsToInvestInHeading

	def getThingsToInvestInTextBlock(self): #投資対象 [テキストブロック]
		return self.ThingsToInvestInTextBlock

	def getProfitDistributionPolicyHeading(self): #分配方針 [目次項目]
		return self.ProfitDistributionPolicyHeading

	def getProfitDistributionPolicyTextBlock(self): #分配方針 [テキストブロック]
		return self.ProfitDistributionPolicyTextBlock

	def getRestrictionsOnInvestmentHeading(self): #投資制限 [目次項目]
		return self.RestrictionsOnInvestmentHeading

	def getRestrictionsOnInvestmentTextBlock(self): #投資制限 [テキストブロック]
		return self.RestrictionsOnInvestmentTextBlock

	def getInvestmentRisksHeading(self): #投資リスク [目次項目]
		return self.InvestmentRisksHeading

	def getInvestmentRisksTextBlock(self): #投資リスク [テキストブロック]
		return self.InvestmentRisksTextBlock

	def getFeesChargesAndTaxesHeading(self): #手数料等及び税金 [目次項目]
		return self.FeesChargesAndTaxesHeading

	def getApplicationFeeOverviewOfFundHeading(self): #申込手数料、ファンドの状況 [目次項目]
		return self.ApplicationFeeOverviewOfFundHeading

	def getApplicationFeeOverviewOfFundTextBlock(self): #申込手数料、ファンドの状況 [テキストブロック]
		return self.ApplicationFeeOverviewOfFundTextBlock

	def getRedemptionFeeInvestmentCorporationHeading(self): #買戻し手数料、投資法人 [目次項目]
		return self.RedemptionFeeInvestmentCorporationHeading

	def getRedemptionFeeInvestmentCorporationTextBlock(self): #買戻し手数料、投資法人 [テキストブロック]
		return self.RedemptionFeeInvestmentCorporationTextBlock

	def getAdministrationFeesAndChargesHeading(self): #管理報酬等 [目次項目]
		return self.AdministrationFeesAndChargesHeading

	def getAdministrationFeesAndChargesTextBlock(self): #管理報酬等 [テキストブロック]
		return self.AdministrationFeesAndChargesTextBlock

	def getOtherFeesAndChargesHeading(self): #その他の手数料等 [目次項目]
		return self.OtherFeesAndChargesHeading

	def getOtherFeesAndChargesTextBlock(self): #その他の手数料等 [テキストブロック]
		return self.OtherFeesAndChargesTextBlock

	def getTaxationHeading(self): #課税上の取扱い [目次項目]
		return self.TaxationHeading

	def getTaxationTextBlock(self): #課税上の取扱い [テキストブロック]
		return self.TaxationTextBlock

	def getStatusOfInvestmentManagementHeading(self): #運用状況 [目次項目]
		return self.StatusOfInvestmentManagementHeading

	def getStatusOfInvestmentManagementTextBlock(self): #運用状況 [テキストブロック]
		return self.StatusOfInvestmentManagementTextBlock

	def getStatusOfInvestmentHeading(self): #投資状況 [目次項目]
		return self.StatusOfInvestmentHeading

	def getStatusOfInvestmentTextBlock(self): #投資状況 [テキストブロック]
		return self.StatusOfInvestmentTextBlock

	def getInvestmentAssetsHeading(self): #投資資産 [目次項目]
		return self.InvestmentAssetsHeading

	def getMajorComponentsOfInvestmentSecuritiesHeading(self): #投資有価証券の主要銘柄 [目次項目]
		return self.MajorComponentsOfInvestmentSecuritiesHeading

	def getMajorComponentsOfInvestmentSecuritiesTextBlock(self): #投資有価証券の主要銘柄 [テキストブロック]
		return self.MajorComponentsOfInvestmentSecuritiesTextBlock

	def getComponentsOfRealEstateInvestmentsHeading(self): #投資不動産物件 [目次項目]
		return self.ComponentsOfRealEstateInvestmentsHeading

	def getComponentsOfRealEstateInvestmentsTextBlock(self): #投資不動産物件 [テキストブロック]
		return self.ComponentsOfRealEstateInvestmentsTextBlock

	def getMajorComponentsOfOtherInvestmentsHeading(self): #その他投資資産の主要なもの [目次項目]
		return self.MajorComponentsOfOtherInvestmentsHeading

	def getMajorComponentsOfOtherInvestmentsTextBlock(self): #その他投資資産の主要なもの [テキストブロック]
		return self.MajorComponentsOfOtherInvestmentsTextBlock

	def getActualPerformanceHeading(self): #運用実績 [目次項目]
		return self.ActualPerformanceHeading

	def getChangesInNetAssetsEtcHeading(self): #純資産等の推移 [目次項目]
		return self.ChangesInNetAssetsEtcHeading

	def getChangesInNetAssetsEtcTextBlock(self): #純資産等の推移 [テキストブロック]
		return self.ChangesInNetAssetsEtcTextBlock

	def getHistoricalRecordsOfProfitDistributionHeading(self): #分配の推移 [目次項目]
		return self.HistoricalRecordsOfProfitDistributionHeading

	def getHistoricalRecordsOfProfitDistributionTextBlock(self): #分配の推移 [テキストブロック]
		return self.HistoricalRecordsOfProfitDistributionTextBlock

	def getHistoricalRecordsOfROEHeading(self): #自己資本利益率（収益率）の推移 [目次項目]
		return self.HistoricalRecordsOfROEHeading

	def getHistoricalRecordsOfROETextBlock(self): #自己資本利益率（収益率）の推移 [テキストブロック]
		return self.HistoricalRecordsOfROETextBlock

	def getOverviewOfProceduresEtcHeading(self): #手続等の概要 [目次項目]
		return self.OverviewOfProceduresEtcHeading

	def getOverviewOfProceduresEtcTextBlock(self): #手続等の概要 [テキストブロック]
		return self.OverviewOfProceduresEtcTextBlock

	def getOverviewOfAdministrationAndOperationHeading(self): #管理及び運営の概要 [目次項目]
		return self.OverviewOfAdministrationAndOperationHeading

	def getOverviewOfAdministrationAndOperationTextBlock(self): #管理及び運営の概要 [テキストブロック]
		return self.OverviewOfAdministrationAndOperationTextBlock

	def getFinancialHighlightsHeading(self): #財務ハイライト情報 [目次項目]
		return self.FinancialHighlightsHeading

	def getBalanceSheetFinancialHighlightsHeading(self): #貸借対照表、財務ハイライト情報 [目次項目]
		return self.BalanceSheetFinancialHighlightsHeading

	def getBalanceSheetFinancialHighlightsTextBlock(self): #貸借対照表、財務ハイライト情報 [テキストブロック]
		return self.BalanceSheetFinancialHighlightsTextBlock

	def getStatementOfIncomeFinancialHighlightsHeading(self): #損益計算書、財務ハイライト情報 [目次項目]
		return self.StatementOfIncomeFinancialHighlightsHeading

	def getStatementOfIncomeFinancialHighlightsTextBlock(self): #損益計算書、財務ハイライト情報 [テキストブロック]
		return self.StatementOfIncomeFinancialHighlightsTextBlock

	def getStatementOfCashDistributionFinancialHighlightsHeading(self): #金銭の分配に係る計算書、財務ハイライト情報 [目次項目]
		return self.StatementOfCashDistributionFinancialHighlightsHeading

	def getStatementOfCashDistributionFinancialHighlightsTextBlock(self): #金銭の分配に係る計算書、財務ハイライト情報 [テキストブロック]
		return self.StatementOfCashDistributionFinancialHighlightsTextBlock

	def getStatementOfCashFlowsFinancialHighlightsHeading(self): #キャッシュ・フロー計算書、財務ハイライト情報 [目次項目]
		return self.StatementOfCashFlowsFinancialHighlightsHeading

	def getStatementOfCashFlowsFinancialHighlightsTextBlock(self): #キャッシュ・フロー計算書、財務ハイライト情報 [テキストブロック]
		return self.StatementOfCashFlowsFinancialHighlightsTextBlock

	def getOverviewOfOperationalProceduresRelatedToDomesticInvestmentSecuritiesHeading(self): #内国投資証券事務の概要 [目次項目]
		return self.OverviewOfOperationalProceduresRelatedToDomesticInvestmentSecuritiesHeading

	def getOverviewOfOperationalProceduresRelatedToDomesticInvestmentSecuritiesTextBlock(self): #内国投資証券事務の概要 [テキストブロック]
		return self.OverviewOfOperationalProceduresRelatedToDomesticInvestmentSecuritiesTextBlock

	def getListOfContentsIncludedInDetailsOfInvestmentCorporationHeading(self): #投資法人の詳細情報の項目 [目次項目]
		return self.ListOfContentsIncludedInDetailsOfInvestmentCorporationHeading

	def getListOfContentsIncludedInDetailsOfInvestmentCorporationTextBlock(self): #投資法人の詳細情報の項目 [テキストブロック]
		return self.ListOfContentsIncludedInDetailsOfInvestmentCorporationTextBlock

	def getDetailsOfInvestmentCorporationHeading(self): #投資法人の詳細情報 [目次項目]
		return self.DetailsOfInvestmentCorporationHeading

	def getAdditionalInformationAboutInvestmentCorporationHeading(self): #投資法人の追加情報 [目次項目]
		return self.AdditionalInformationAboutInvestmentCorporationHeading

	def getHistoryOfInvestmentCorporationHeading(self): #投資法人の沿革 [目次項目]
		return self.HistoryOfInvestmentCorporationHeading

	def getHistoryOfInvestmentCorporationTextBlock(self): #投資法人の沿革 [テキストブロック]
		return self.HistoryOfInvestmentCorporationTextBlock

	def getInformationAboutOfficersAdditionalInformationAboutInvestmentCorporationHeading(self): #役員の状況、投資法人の追加情報 [目次項目]
		return self.InformationAboutOfficersAdditionalInformationAboutInvestmentCorporationHeading

	def getInformationAboutOfficersAdditionalInformationAboutInvestmentCorporationTextBlock(self): #役員の状況、投資法人の追加情報 [テキストブロック]
		return self.InformationAboutOfficersAdditionalInformationAboutInvestmentCorporationTextBlock

	def getOtherInformationAdditionalInformationAboutInvestmentCorporationHeading(self): #その他、投資法人の追加情報 [目次項目]
		return self.OtherInformationAdditionalInformationAboutInvestmentCorporationHeading

	def getOtherInformationAdditionalInformationAboutInvestmentCorporationTextBlock(self): #その他、投資法人の追加情報 [テキストブロック]
		return self.OtherInformationAdditionalInformationAboutInvestmentCorporationTextBlock

	def getProceduresEtcHeading(self): #手続等 [目次項目]
		return self.ProceduresEtcHeading

	def getProceduresEtcForApplicationAndDistributionInvestmentCorporationHeading(self): #申込（販売）手続等、投資法人 [目次項目]
		return self.ProceduresEtcForApplicationAndDistributionInvestmentCorporationHeading

	def getProceduresEtcForApplicationAndDistributionInvestmentCorporationTextBlock(self): #申込（販売）手続等、投資法人 [テキストブロック]
		return self.ProceduresEtcForApplicationAndDistributionInvestmentCorporationTextBlock

	def getRedemptionProceduresEtcInvestmentCorporationHeading(self): #買戻し手続等、投資法人 [目次項目]
		return self.RedemptionProceduresEtcInvestmentCorporationHeading

	def getRedemptionProceduresEtcInvestmentCorporationTextBlock(self): #買戻し手続等、投資法人 [テキストブロック]
		return self.RedemptionProceduresEtcInvestmentCorporationTextBlock

	def getAdministrationAndOperationHeading(self): #管理及び運営 [目次項目]
		return self.AdministrationAndOperationHeading

	def getOverviewOfAssetManagementEtcHeading(self): #資産管理等の概要 [目次項目]
		return self.OverviewOfAssetManagementEtcHeading

	def getValuationOfAssetsHeading(self): #資産の評価 [目次項目]
		return self.ValuationOfAssetsHeading

	def getValuationOfAssetsTextBlock(self): #資産の評価 [テキストブロック]
		return self.ValuationOfAssetsTextBlock

	def getCustodyHeading(self): #保管 [目次項目]
		return self.CustodyHeading

	def getCustodyTextBlock(self): #保管 [テキストブロック]
		return self.CustodyTextBlock

	def getDurationOfInvestmentCorporationHeading(self): #存続期間 [目次項目]
		return self.DurationOfInvestmentCorporationHeading

	def getDurationOfInvestmentCorporationTextBlock(self): #存続期間 [テキストブロック]
		return self.DurationOfInvestmentCorporationTextBlock

	def getAccountingPeriodHeading(self): #計算期間 [目次項目]
		return self.AccountingPeriodHeading

	def getAccountingPeriodTextBlock(self): #計算期間 [テキストブロック]
		return self.AccountingPeriodTextBlock

	def getOtherInformationOverviewOfAssetManagementEtcHeading(self): #その他、資産管理等の概要 [目次項目]
		return self.OtherInformationOverviewOfAssetManagementEtcHeading

	def getOtherInformationOverviewOfAssetManagementEtcTextBlock(self): #その他、資産管理等の概要 [テキストブロック]
		return self.OtherInformationOverviewOfAssetManagementEtcTextBlock

	def getRestrictionsOnTradesWithInterestedPartiesHeading(self): #利害関係人との取引制限 [目次項目]
		return self.RestrictionsOnTradesWithInterestedPartiesHeading

	def getRestrictionsOnTradesWithInterestedPartiesTextBlock(self): #利害関係人との取引制限 [テキストブロック]
		return self.RestrictionsOnTradesWithInterestedPartiesTextBlock

	def getRightsOfUnitholdersAndBondholdersOfInvestmentCorporationHeading(self): #投資主・投資法人債権者の権利 [目次項目]
		return self.RightsOfUnitholdersAndBondholdersOfInvestmentCorporationHeading

	def getRightsOfUnitholdersAndBondholdersOfInvestmentCorporationTextBlock(self): #投資主・投資法人債権者の権利 [テキストブロック]
		return self.RightsOfUnitholdersAndBondholdersOfInvestmentCorporationTextBlock

	def getOverviewOfPartiesInvolvedHeading(self): #関係法人の状況 [目次項目]
		return self.OverviewOfPartiesInvolvedHeading

	def getOverviewOfAssetManagementCompanyHeading(self): #資産運用会社の概況 [目次項目]
		return self.OverviewOfAssetManagementCompanyHeading

	def getNameStatedCapitalAndDescriptionOfBusinessOverviewOfAssetManagementCompanyHeading(self): #名称、資本金の額及び事業の内容、資産運用会社の概況 [目次項目]
		return self.NameStatedCapitalAndDescriptionOfBusinessOverviewOfAssetManagementCompanyHeading

	def getNameStatedCapitalAndDescriptionOfBusinessOverviewOfAssetManagementCompanyTextBlock(self): #名称、資本金の額及び事業の内容、資産運用会社の概況 [テキストブロック]
		return self.NameStatedCapitalAndDescriptionOfBusinessOverviewOfAssetManagementCompanyTextBlock

	def getOrganizationAndFrameworkOfInvestmentManagementOverviewOfAssetManagementCompanyHeading(self): #運用体制、資産運用会社の概況 [目次項目]
		return self.OrganizationAndFrameworkOfInvestmentManagementOverviewOfAssetManagementCompanyHeading

	def getOrganizationAndFrameworkOfInvestmentManagementOverviewOfAssetManagementCompanyTextBlock(self): #運用体制、資産運用会社の概況 [テキストブロック]
		return self.OrganizationAndFrameworkOfInvestmentManagementOverviewOfAssetManagementCompanyTextBlock

	def getMajorShareholdersOverviewOfAssetManagementCompanyHeading(self): #大株主の状況、資産運用会社の概況 [目次項目]
		return self.MajorShareholdersOverviewOfAssetManagementCompanyHeading

	def getMajorShareholdersOverviewOfAssetManagementCompanyTextBlock(self): #大株主の状況、資産運用会社の概況 [テキストブロック]
		return self.MajorShareholdersOverviewOfAssetManagementCompanyTextBlock

	def getInformationAboutOfficersOverviewOfAssetManagementCompanyHeading(self): #役員の状況、資産運用会社の概況 [目次項目]
		return self.InformationAboutOfficersOverviewOfAssetManagementCompanyHeading

	def getInformationAboutOfficersOverviewOfAssetManagementCompanyTextBlock(self): #役員の状況、資産運用会社の概況 [テキストブロック]
		return self.InformationAboutOfficersOverviewOfAssetManagementCompanyTextBlock

	def getDescriptionOfBusinessAndOverviewOfOperationOverviewOfAssetManagementCompanyHeading(self): #事業の内容及び営業の概況、資産運用会社の概況 [目次項目]
		return self.DescriptionOfBusinessAndOverviewOfOperationOverviewOfAssetManagementCompanyHeading

	def getDescriptionOfBusinessAndOverviewOfOperationOverviewOfAssetManagementCompanyTextBlock(self): #事業の内容及び営業の概況、資産運用会社の概況 [テキストブロック]
		return self.DescriptionOfBusinessAndOverviewOfOperationOverviewOfAssetManagementCompanyTextBlock

	def getOverviewOfOtherPartiesInvolvedHeading(self): #その他の関係法人の概況 [目次項目]
		return self.OverviewOfOtherPartiesInvolvedHeading

	def getOverviewOfOtherPartiesInvolvedTextBlock(self): #その他の関係法人の概況 [テキストブロック]
		return self.OverviewOfOtherPartiesInvolvedTextBlock

	def getFinancialInformationOfInvestmentCorporationHeading(self): #投資法人の経理状況 [目次項目]
		return self.FinancialInformationOfInvestmentCorporationHeading

	def getFinancialInformationOfInvestmentCorporationTextBlock(self): #投資法人の経理状況 [テキストブロック]
		return self.FinancialInformationOfInvestmentCorporationTextBlock

	def getFinancialStatementsHeading(self): #財務諸表 [目次項目]
		return self.FinancialStatementsHeading

	def getBalanceSheetHeading(self): #貸借対照表 [目次項目]
		return self.BalanceSheetHeading

	def getBalanceSheetTextBlock(self): #貸借対照表 [テキストブロック]
		return self.BalanceSheetTextBlock

	def getStatementOfIncomeHeading(self): #損益計算書 [目次項目]
		return self.StatementOfIncomeHeading

	def getStatementOfIncomeTextBlock(self): #損益計算書 [テキストブロック]
		return self.StatementOfIncomeTextBlock

	def getStatementOfUnitholdersEquityHeading(self): #投資主資本等変動計算書 [目次項目]
		return self.StatementOfUnitholdersEquityHeading

	def getStatementOfUnitholdersEquityTextBlock(self): #投資主資本等変動計算書 [テキストブロック]
		return self.StatementOfUnitholdersEquityTextBlock

	def getStatementOfCashDistributionHeading(self): #金銭の分配に係る計算書 [目次項目]
		return self.StatementOfCashDistributionHeading

	def getStatementOfCashDistributionTextBlock(self): #金銭の分配に係る計算書 [テキストブロック]
		return self.StatementOfCashDistributionTextBlock

	def getStatementOfCashFlowsHeading(self): #キャッシュ・フロー計算書 [目次項目]
		return self.StatementOfCashFlowsHeading

	def getStatementOfCashFlowsTextBlock(self): #キャッシュ・フロー計算書 [テキストブロック]
		return self.StatementOfCashFlowsTextBlock

	def getNotesToFinancialStatementsHeading(self): #注記表 [目次項目]
		return self.NotesToFinancialStatementsHeading

	def getNotesToFinancialStatementsTextBlock(self): #注記表 [テキストブロック]
		return self.NotesToFinancialStatementsTextBlock

	def getAnnexedDetailedSchedulesHeading(self): #附属明細表 [目次項目]
		return self.AnnexedDetailedSchedulesHeading

	def getAnnexedDetailedSchedulesTextBlock(self): #附属明細表 [テキストブロック]
		return self.AnnexedDetailedSchedulesTextBlock

	def getCurrentStatusOfInvestmentCorporationHeading(self): #投資法人の現況 [目次項目]
		return self.CurrentStatusOfInvestmentCorporationHeading

	def getCalculationOfNetAssetsHeading(self): #純資産額計算書 [目次項目]
		return self.CalculationOfNetAssetsHeading

	def getCalculationOfNetAssetsTextBlock(self): #純資産額計算書 [テキストブロック]
		return self.CalculationOfNetAssetsTextBlock

	def getHistoricalRecordsOfSalesAndBuybacksHeading(self): #販売及び買戻しの実績 [目次項目]
		return self.HistoricalRecordsOfSalesAndBuybacksHeading

	def getHistoricalRecordsOfSalesAndBuybacksTextBlock(self): #販売及び買戻しの実績 [テキストブロック]
		return self.HistoricalRecordsOfSalesAndBuybacksTextBlock

	def getPhotographsDiagramsAndOtherItemsHeading(self): #写真、図面その他 [目次項目]
		return self.PhotographsDiagramsAndOtherItemsHeading

	def getPhotographsDiagramsAndOtherItemsTextBlock(self): #写真、図面その他 [テキストブロック]
		return self.PhotographsDiagramsAndOtherItemsTextBlock

	def getIndependentAuditorsReportHeading(self): #独立監査人の報告書 [目次項目]
		return self.IndependentAuditorsReportHeading

	def getIndependentAuditorsReportInvestmentCorporationTextBlock(self): #独立監査人の報告書、投資法人 [テキストブロック]
		return self.IndependentAuditorsReportInvestmentCorporationTextBlock
