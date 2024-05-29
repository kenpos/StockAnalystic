from arelle import ModelManager
from arelle import Cntlr

class jplvh030000:#株券等の大量保有の状況の開示に関する内閣府令 第三号様式 大量保有報告書
	CabinetOfficeOrdinanceOnDisclosureOfStatusOfLargeVolumeHoldingOfShareCertificatesEtcFormNo3ReportOfLargeVolumeHoldingHeading = '' #株券等の大量保有の状況の開示に関する内閣府令 第三号様式 大量保有報告書 [目次項目]
	CoverPageHeading = '' #表紙 [目次項目]
	CoverPageHeading = '' #表紙 [目次項目]
	DocumentTitleCoverPage = '' #提出書類、表紙
	ClauseOfStipulationCoverPage = '' #根拠条文、表紙
	PlaceOfFilingCoverPage = '' #提出先、表紙
	NameCoverPage = '' #氏名又は名称、表紙
	ResidentialAddressOrAddressOfRegisteredHeadquarterCoverPage = '' #住所又は本店所在地、表紙
	DateWhenFilingRequirementAroseCoverPage = '' #報告義務発生日、表紙
	FilingDateCoverPage = '' #提出日、表紙
	TotalNumberOfFilersAndJointHoldersCoverPage = '' #提出者及び共同保有者の総数（名）、表紙
	ArrangementOfFilingCoverPage = '' #提出形態、表紙
	ReasonForFilingChangeReportCoverPage = '' #変更報告書提出事由、表紙
	ReasonForFilingChangeReportCoverPageNA = '' #変更報告書提出事由、表紙（該当なし）
	InformationAboutIssuerHeading = '' #発行者に関する事項 [目次項目]
	InformationAboutIssuerHeading = '' #発行者に関する事項 [目次項目]
	NameOfIssuer = '' #発行者の名称
	SecurityCodeOfIssuer = '' #発行者の証券コード
	ListedOrOTC = '' #上場・店頭の別
	StockListing = '' #上場金融商品取引所
	InformationAboutFilersHeading = '' #提出者に関する事項 [目次項目]
	InformationAboutFilersHeading = '' #提出者に関する事項 [目次項目]
	InformationAboutFilersTable = '' #提出者に関する事項 [表]
	FilersLargeVolumeHoldersAndJointHoldersAxis = '' #提出者（大量保有者）・共同保有者 [軸]
	FilersLargeVolumeHoldersOrJointHoldersMember = '' #提出者（大量保有者）・共同保有者 [メンバー] ※ディメンションデフォルト
	FilersLargeVolumeHoldersMember = '' #提出者（大量保有者） [メンバー]
	InformationAboutFilersLineItems = '' #提出者に関する事項 [表示項目]
	FilerLargeVolumeHolderSerialNumberAbstract = '' #提出者（大量保有者）／連番 [タイトル項目]
	OverviewOfFilerAbstract = '' #提出者の概要 [タイトル項目]
	FilerLargeVolumeHolderAbstract = '' #提出者（大量保有者） [タイトル項目]
	IndividualOrCorporation = '' #個人・法人の別
	Name = '' #氏名又は名称
	ResidentialAddressOrAddressOfRegisteredHeadquarter = '' #住所又は本店所在地
	FormerName = '' #旧氏名又は名称
	FormerResidentialAddressOrAddressOfRegisteredHeadquarter = '' #旧住所又は本店所在地
	InformationAboutIndividualAbstract = '' #個人の場合 [タイトル項目]
	InformationAboutIndividualNATextBlock = '' #個人の場合（該当なし） [テキストブロック]
	DateOfBirth = '' #生年月日
	Occupation = '' #職業
	NameOfEmployer = '' #勤務先名称
	AddressOfEmployer = '' #勤務先住所
	InformationAboutCorporationAbstract = '' #法人の場合 [タイトル項目]
	InformationAboutCorporationNATextBlock = '' #法人の場合（該当なし） [テキストブロック]
	DateOfEstablishment = '' #設立年月日
	NameOfRepresentative = '' #代表者氏名
	JobTitleOfRepresentative = '' #代表者役職
	DescriptionOfBusiness = '' #事業内容
	ContactInformationAbstract = '' #事務上の連絡先 [タイトル項目]
	ContactInformationAndPerson = '' #事務上の連絡先及び担当者名
	TelephoneNumber = '' #電話番号
	PurposeOfHoldingAbstract = '' #保有目的 [タイトル項目]
	PurposeOfHolding = '' #保有目的
	PurposeOfHoldingNA = '' #保有目的（該当なし）
	BreakdownOfStocksEtcHeldBySaidFilerAbstract = '' #上記提出者の保有株券等の内訳 [タイトル項目]
	NumberOfStocksEtcHeldAbstract = '' #保有株券等の数 [タイトル項目]
	Article27233MainClauseAbstract = '' #法第27条の23第3項本文 [タイトル項目]
	StocksOrInvestmentSecuritiesEtcArticle27233MainClause = '' #株券又は投資証券等、法第27条の23第3項本文
	SubscriptionRightsToSharesArticle27233MainClause = '' #新株予約権証券又は新投資口予約権証券等、法第27条の23第3項本文
	ConvertibleBondsArticle27233MainClause = '' #新株予約権付社債券、法第27条の23第3項本文
	TargetSecurityCoveredWarrantsArticle27233MainClause = '' #対象有価証券カバードワラント、法第27条の23第3項本文
	StockDepositoryReceiptsArticle27233MainClause = '' #株券預託証券、法第27条の23第3項本文
	StockRelatedDepositoryReceiptsArticle27233MainClause = '' #株券関連預託証券、法第27条の23第3項本文
	StockTrustBeneficiaryRightsArticle27233MainClause = '' #株券信託受益証券、法第27条の23第3項本文
	StockRelatedTrustBeneficiaryRightsArticle27233MainClause = '' #株券関連信託受益証券、法第27条の23第3項本文
	TargetSecurityRedeemableBondsArticle27233MainClause = '' #対象有価証券償還社債、法第27条の23第3項本文
	ExchangeableBondsArticle27233MainClause = '' #他社株等転換株券、法第27条の23第3項本文
	TotalArticle27233MainClause = '' #合計、法第27条の23第3項本文
	Article27233Item1Abstract = '' #法第27条の23第3項第１号 [タイトル項目]
	StocksOrInvestmentSecuritiesEtcArticle27233Item1 = '' #株券又は投資証券等、法第27条の23第3項第１号
	TargetSecurityCoveredWarrantsArticle27233Item1 = '' #対象有価証券カバードワラント、法第27条の23第3項第１号
	StockDepositoryReceiptsArticle27233Item1 = '' #株券預託証券、法第27条の23第3項第１号
	StockRelatedDepositoryReceiptsArticle27233Item1 = '' #株券関連預託証券、法第27条の23第3項第１号
	StockTrustBeneficiaryRightsArticle27233Item1 = '' #株券信託受益証券、法第27条の23第3項第１号
	StockRelatedTrustBeneficiaryRightsArticle27233Item1 = '' #株券関連信託受益証券、法第27条の23第3項第１号
	TargetSecurityRedeemableBondsArticle27233Item1 = '' #対象有価証券償還社債、法第27条の23第3項第１号
	ExchangeableBondsArticle27233Item1 = '' #他社株等転換株券、法第27条の23第3項第１号
	TotalArticle27233Item1 = '' #合計、法第27条の23第3項第１号
	Article27233Item2Abstract = '' #法第27条の23第3項第2号 [タイトル項目]
	StocksOrInvestmentSecuritiesEtcArticle27233Item2 = '' #株券又は投資証券等、法第27条の23第3項第2号
	SubscriptionRightsToSharesArticle27233Item2 = '' #新株予約権証券又は新投資口予約権証券等、法第27条の23第3項第2号
	ConvertibleBondsArticle27233Item2 = '' #新株予約権付社債券、法第27条の23第3項第2号
	TargetSecurityCoveredWarrantsArticle27233Item2 = '' #対象有価証券カバードワラント、法第27条の23第3項第2号
	StockDepositoryReceiptsArticle27233Item2 = '' #株券預託証券、法第27条の23第3項第2号
	StockRelatedDepositoryReceiptsArticle27233Item2 = '' #株券関連預託証券、法第27条の23第3項第2号
	StockTrustBeneficiaryRightsArticle27233Item2 = '' #株券信託受益証券、法第27条の23第3項第2号
	StockRelatedTrustBeneficiaryRightsArticle27233Item2 = '' #株券関連信託受益証券、法第27条の23第3項第2号
	TargetSecurityRedeemableBondsArticle27233Item2 = '' #対象有価証券償還社債、法第27条の23第3項第2号
	ExchangeableBondsArticle27233Item2 = '' #他社株等転換株券、法第27条の23第3項第2号
	TotalArticle27233Item2 = '' #合計、法第27条の23第3項第2号
	NumberOfStocksEtcToDeductAsSoldOnMarginTrading = '' #信用取引により譲渡したことにより控除する株券等の数
	NumberOfStocksEtcToDeductAsRightsToDemandExistBetweenJointHolders = '' #共同保有者間で引渡請求権等の権利が存在するものとして控除する株券等の数
	TotalNumberOfStocksEtcHeld = '' #保有株券等の数（総数）
	NumberOfResidualStocksHeld = '' #保有潜在株券等の数
	NotesNumberOfStocksEtcHeldTextBlock = '' #欄外注記、保有株券等の数 [テキストブロック]
	HoldingRatioOfShareCertificatesEtcAbstract = '' #株券等保有割合 [タイトル項目]
	TotalNumberOfOutstandingStocksEtcAbstract = '' #発行済株式等総数 [タイトル項目]
	BaseDate = '' #基準日
	TotalNumberOfOutstandingStocksEtc = '' #発行済株式等総数
	HoldingRatioOfShareCertificatesEtc = '' #株券等保有割合
	HoldingRatioOfShareCertificatesEtcPerLastReport = '' #直前の報告書に記載された株券等保有割合
	NotesHoldingRatioOfShareCertificatesEtcTextBlock = '' #欄外注記、株券等保有割合 [テキストブロック]
	SignificantContractsRelatedToSaidStocksEtcSuchAsCollateralAgreementsAbstract = '' #当該株券等に関する担保契約等重要な契約 [タイトル項目]
	SignificantContractsRelatedToSaidStocksEtcSuchAsCollateralAgreementsTextBlock = '' #当該株券等に関する担保契約等重要な契約 [テキストブロック]
	SignificantContractsRelatedToSaidStocksEtcSuchAsCollateralAgreementsNA = '' #当該株券等に関する担保契約等重要な契約（該当なし）
	InformationAboutJointHoldersHeading = '' #共同保有者に関する事項 [目次項目]
	InformationAboutJointHoldersHeading = '' #共同保有者に関する事項 [目次項目]
	InformationAboutJointHoldersTable = '' #共同保有者に関する事項 [表]
	FilersLargeVolumeHoldersAndJointHoldersAxis = '' #提出者（大量保有者）・共同保有者 [軸]
	FilersLargeVolumeHoldersOrJointHoldersMember = '' #提出者（大量保有者）・共同保有者 [メンバー] ※ディメンションデフォルト
	JointHoldersMember = '' #共同保有者 [メンバー]
	InformationAboutJointHoldersLineItems = '' #共同保有者に関する事項 [表示項目]
	JointHolderSerialNumberAbstract = '' #共同保有者／連番 [タイトル項目]
	OverviewOfJointHolderAbstract = '' #共同保有者の概要 [タイトル項目]
	JointHolderAbstract = '' #共同保有者 [タイトル項目]
	IndividualOrCorporation = '' #個人・法人の別
	Name = '' #氏名又は名称
	ResidentialAddressOrAddressOfRegisteredHeadquarter = '' #住所又は本店所在地
	FormerName = '' #旧氏名又は名称
	FormerResidentialAddressOrAddressOfRegisteredHeadquarter = '' #旧住所又は本店所在地
	InformationAboutIndividualAbstract = '' #個人の場合 [タイトル項目]
	InformationAboutIndividualNATextBlock = '' #個人の場合（該当なし） [テキストブロック]
	DateOfBirth = '' #生年月日
	Occupation = '' #職業
	NameOfEmployer = '' #勤務先名称
	AddressOfEmployer = '' #勤務先住所
	InformationAboutCorporationAbstract = '' #法人の場合 [タイトル項目]
	InformationAboutCorporationNATextBlock = '' #法人の場合（該当なし） [テキストブロック]
	DateOfEstablishment = '' #設立年月日
	NameOfRepresentative = '' #代表者氏名
	JobTitleOfRepresentative = '' #代表者役職
	DescriptionOfBusiness = '' #事業内容
	ContactInformationAbstract = '' #事務上の連絡先 [タイトル項目]
	ContactInformationAndPerson = '' #事務上の連絡先及び担当者名
	TelephoneNumber = '' #電話番号
	BreakdownOfStocksEtcHeldBySaidJointHolderAbstract = '' #上記共同保有者の保有株券等の内訳 [タイトル項目]
	NumberOfStocksEtcHeldAbstract = '' #保有株券等の数 [タイトル項目]
	Article27233MainClauseAbstract = '' #法第27条の23第3項本文 [タイトル項目]
	StocksOrInvestmentSecuritiesEtcArticle27233MainClause = '' #株券又は投資証券等、法第27条の23第3項本文
	SubscriptionRightsToSharesArticle27233MainClause = '' #新株予約権証券又は新投資口予約権証券等、法第27条の23第3項本文
	ConvertibleBondsArticle27233MainClause = '' #新株予約権付社債券、法第27条の23第3項本文
	TargetSecurityCoveredWarrantsArticle27233MainClause = '' #対象有価証券カバードワラント、法第27条の23第3項本文
	StockDepositoryReceiptsArticle27233MainClause = '' #株券預託証券、法第27条の23第3項本文
	StockRelatedDepositoryReceiptsArticle27233MainClause = '' #株券関連預託証券、法第27条の23第3項本文
	StockTrustBeneficiaryRightsArticle27233MainClause = '' #株券信託受益証券、法第27条の23第3項本文
	StockRelatedTrustBeneficiaryRightsArticle27233MainClause = '' #株券関連信託受益証券、法第27条の23第3項本文
	TargetSecurityRedeemableBondsArticle27233MainClause = '' #対象有価証券償還社債、法第27条の23第3項本文
	ExchangeableBondsArticle27233MainClause = '' #他社株等転換株券、法第27条の23第3項本文
	TotalArticle27233MainClause = '' #合計、法第27条の23第3項本文
	Article27233Item1Abstract = '' #法第27条の23第3項第１号 [タイトル項目]
	StocksOrInvestmentSecuritiesEtcArticle27233Item1 = '' #株券又は投資証券等、法第27条の23第3項第１号
	TargetSecurityCoveredWarrantsArticle27233Item1 = '' #対象有価証券カバードワラント、法第27条の23第3項第１号
	StockDepositoryReceiptsArticle27233Item1 = '' #株券預託証券、法第27条の23第3項第１号
	StockRelatedDepositoryReceiptsArticle27233Item1 = '' #株券関連預託証券、法第27条の23第3項第１号
	StockTrustBeneficiaryRightsArticle27233Item1 = '' #株券信託受益証券、法第27条の23第3項第１号
	StockRelatedTrustBeneficiaryRightsArticle27233Item1 = '' #株券関連信託受益証券、法第27条の23第3項第１号
	TargetSecurityRedeemableBondsArticle27233Item1 = '' #対象有価証券償還社債、法第27条の23第3項第１号
	ExchangeableBondsArticle27233Item1 = '' #他社株等転換株券、法第27条の23第3項第１号
	TotalArticle27233Item1 = '' #合計、法第27条の23第3項第１号
	Article27233Item2Abstract = '' #法第27条の23第3項第2号 [タイトル項目]
	StocksOrInvestmentSecuritiesEtcArticle27233Item2 = '' #株券又は投資証券等、法第27条の23第3項第2号
	SubscriptionRightsToSharesArticle27233Item2 = '' #新株予約権証券又は新投資口予約権証券等、法第27条の23第3項第2号
	ConvertibleBondsArticle27233Item2 = '' #新株予約権付社債券、法第27条の23第3項第2号
	TargetSecurityCoveredWarrantsArticle27233Item2 = '' #対象有価証券カバードワラント、法第27条の23第3項第2号
	StockDepositoryReceiptsArticle27233Item2 = '' #株券預託証券、法第27条の23第3項第2号
	StockRelatedDepositoryReceiptsArticle27233Item2 = '' #株券関連預託証券、法第27条の23第3項第2号
	StockTrustBeneficiaryRightsArticle27233Item2 = '' #株券信託受益証券、法第27条の23第3項第2号
	StockRelatedTrustBeneficiaryRightsArticle27233Item2 = '' #株券関連信託受益証券、法第27条の23第3項第2号
	TargetSecurityRedeemableBondsArticle27233Item2 = '' #対象有価証券償還社債、法第27条の23第3項第2号
	ExchangeableBondsArticle27233Item2 = '' #他社株等転換株券、法第27条の23第3項第2号
	TotalArticle27233Item2 = '' #合計、法第27条の23第3項第2号
	NumberOfStocksEtcToDeductAsSoldOnMarginTrading = '' #信用取引により譲渡したことにより控除する株券等の数
	NumberOfStocksEtcToDeductAsRightsToDemandExistBetweenJointHolders = '' #共同保有者間で引渡請求権等の権利が存在するものとして控除する株券等の数
	TotalNumberOfStocksEtcHeld = '' #保有株券等の数（総数）
	NumberOfResidualStocksHeld = '' #保有潜在株券等の数
	NotesNumberOfStocksEtcHeldTextBlock = '' #欄外注記、保有株券等の数 [テキストブロック]
	HoldingRatioOfShareCertificatesEtcAbstract = '' #株券等保有割合 [タイトル項目]
	TotalNumberOfOutstandingStocksEtcAbstract = '' #発行済株式等総数 [タイトル項目]
	BaseDate = '' #基準日
	TotalNumberOfOutstandingStocksEtc = '' #発行済株式等総数
	HoldingRatioOfShareCertificatesEtc = '' #株券等保有割合
	HoldingRatioOfShareCertificatesEtcPerLastReport = '' #直前の報告書に記載された株券等保有割合
	NotesHoldingRatioOfShareCertificatesEtcTextBlock = '' #欄外注記、株券等保有割合 [テキストブロック]
	InformationAboutJointHoldersNA = '' #共同保有者に関する事項（該当なし）
	SummaryOfFilerAndJointHoldersHeading = '' #提出者及び共同保有者に関する総括表 [目次項目]
	FilersAndJointHoldersHeading = '' #提出者及び共同保有者 [目次項目]
	FilersAndJointHoldersHeading = '' #提出者及び共同保有者 [目次項目]
	FilersAndJointHoldersTable = '' #提出者及び共同保有者 [表]
	FilersLargeVolumeHoldersAndJointHoldersAxis = '' #提出者（大量保有者）・共同保有者 [軸]
	FilersLargeVolumeHoldersOrJointHoldersMember = '' #提出者（大量保有者）・共同保有者 [メンバー] ※ディメンションデフォルト
	FilersAndJointHoldersLineItems = '' #提出者及び共同保有者 [表示項目]
	Name = '' #氏名又は名称
	BreakdownOfStocksEtcHeldBySaidFilerAndJointHoldersHeading = '' #上記提出者及び共同保有者の保有株券等の内訳 [目次項目]
	NumberOfStocksEtcHeldSummaryHeading = '' #保有株券等の数、総括表 [目次項目]
	NumberOfStocksEtcHeldSummaryHeading = '' #保有株券等の数、総括表 [目次項目]
	Article27233MainClauseAbstract = '' #法第27条の23第3項本文 [タイトル項目]
	StocksOrInvestmentSecuritiesEtcArticle27233MainClause = '' #株券又は投資証券等、法第27条の23第3項本文
	SubscriptionRightsToSharesArticle27233MainClause = '' #新株予約権証券又は新投資口予約権証券等、法第27条の23第3項本文
	ConvertibleBondsArticle27233MainClause = '' #新株予約権付社債券、法第27条の23第3項本文
	TargetSecurityCoveredWarrantsArticle27233MainClause = '' #対象有価証券カバードワラント、法第27条の23第3項本文
	StockDepositoryReceiptsArticle27233MainClause = '' #株券預託証券、法第27条の23第3項本文
	StockRelatedDepositoryReceiptsArticle27233MainClause = '' #株券関連預託証券、法第27条の23第3項本文
	StockTrustBeneficiaryRightsArticle27233MainClause = '' #株券信託受益証券、法第27条の23第3項本文
	StockRelatedTrustBeneficiaryRightsArticle27233MainClause = '' #株券関連信託受益証券、法第27条の23第3項本文
	TargetSecurityRedeemableBondsArticle27233MainClause = '' #対象有価証券償還社債、法第27条の23第3項本文
	ExchangeableBondsArticle27233MainClause = '' #他社株等転換株券、法第27条の23第3項本文
	TotalArticle27233MainClause = '' #合計、法第27条の23第3項本文
	Article27233Item1Abstract = '' #法第27条の23第3項第１号 [タイトル項目]
	StocksOrInvestmentSecuritiesEtcArticle27233Item1 = '' #株券又は投資証券等、法第27条の23第3項第１号
	TargetSecurityCoveredWarrantsArticle27233Item1 = '' #対象有価証券カバードワラント、法第27条の23第3項第１号
	StockDepositoryReceiptsArticle27233Item1 = '' #株券預託証券、法第27条の23第3項第１号
	StockRelatedDepositoryReceiptsArticle27233Item1 = '' #株券関連預託証券、法第27条の23第3項第１号
	StockTrustBeneficiaryRightsArticle27233Item1 = '' #株券信託受益証券、法第27条の23第3項第１号
	StockRelatedTrustBeneficiaryRightsArticle27233Item1 = '' #株券関連信託受益証券、法第27条の23第3項第１号
	TargetSecurityRedeemableBondsArticle27233Item1 = '' #対象有価証券償還社債、法第27条の23第3項第１号
	ExchangeableBondsArticle27233Item1 = '' #他社株等転換株券、法第27条の23第3項第１号
	TotalArticle27233Item1 = '' #合計、法第27条の23第3項第１号
	Article27233Item2Abstract = '' #法第27条の23第3項第2号 [タイトル項目]
	StocksOrInvestmentSecuritiesEtcArticle27233Item2 = '' #株券又は投資証券等、法第27条の23第3項第2号
	SubscriptionRightsToSharesArticle27233Item2 = '' #新株予約権証券又は新投資口予約権証券等、法第27条の23第3項第2号
	ConvertibleBondsArticle27233Item2 = '' #新株予約権付社債券、法第27条の23第3項第2号
	TargetSecurityCoveredWarrantsArticle27233Item2 = '' #対象有価証券カバードワラント、法第27条の23第3項第2号
	StockDepositoryReceiptsArticle27233Item2 = '' #株券預託証券、法第27条の23第3項第2号
	StockRelatedDepositoryReceiptsArticle27233Item2 = '' #株券関連預託証券、法第27条の23第3項第2号
	StockTrustBeneficiaryRightsArticle27233Item2 = '' #株券信託受益証券、法第27条の23第3項第2号
	StockRelatedTrustBeneficiaryRightsArticle27233Item2 = '' #株券関連信託受益証券、法第27条の23第3項第2号
	TargetSecurityRedeemableBondsArticle27233Item2 = '' #対象有価証券償還社債、法第27条の23第3項第2号
	ExchangeableBondsArticle27233Item2 = '' #他社株等転換株券、法第27条の23第3項第2号
	TotalArticle27233Item2 = '' #合計、法第27条の23第3項第2号
	NumberOfStocksEtcToDeductAsSoldOnMarginTrading = '' #信用取引により譲渡したことにより控除する株券等の数
	NumberOfStocksEtcToDeductAsRightsToDemandExistBetweenJointHolders = '' #共同保有者間で引渡請求権等の権利が存在するものとして控除する株券等の数
	TotalNumberOfStocksEtcHeld = '' #保有株券等の数（総数）
	NumberOfResidualStocksHeld = '' #保有潜在株券等の数
	NotesNumberOfStocksEtcHeldTextBlock = '' #欄外注記、保有株券等の数 [テキストブロック]
	HoldingRatioOfShareCertificatesEtcSummaryHeading = '' #株券等保有割合、総括表 [目次項目]
	HoldingRatioOfShareCertificatesEtcSummaryHeading = '' #株券等保有割合、総括表 [目次項目]
	TotalNumberOfOutstandingStocksEtcAbstract = '' #発行済株式等総数 [タイトル項目]
	BaseDate = '' #基準日
	TotalNumberOfOutstandingStocksEtc = '' #発行済株式等総数
	HoldingRatioOfShareCertificatesEtc = '' #株券等保有割合
	HoldingRatioOfShareCertificatesEtcPerLastReport = '' #直前の報告書に記載された株券等保有割合
	NotesHoldingRatioOfShareCertificatesEtcTextBlock = '' #欄外注記、株券等保有割合 [テキストブロック]
	HoldingRatioOfShareCertificatesEtcHeldByJointHoldingHeading = '' #共同保有における株券等保有割合の内訳 [目次項目]
	HoldingRatioOfShareCertificatesEtcHeldByJointHoldingHeading = '' #共同保有における株券等保有割合の内訳 [目次項目]
	HoldingRatioOfShareCertificatesEtcHeldByJointHoldingTable = '' #共同保有における株券等保有割合の内訳 [表]
	FilersLargeVolumeHoldersAndJointHoldersAxis = '' #提出者（大量保有者）・共同保有者 [軸]
	FilersLargeVolumeHoldersOrJointHoldersMember = '' #提出者（大量保有者）・共同保有者 [メンバー] ※ディメンションデフォルト
	HoldingRatioOfShareCertificatesEtcHeldByJointHoldingLineItems = '' #共同保有における株券等保有割合の内訳 [表示項目]
	Name = '' #氏名又は名称
	TotalNumberOfStocksEtcHeld = '' #保有株券等の数（総数）
	HoldingRatioOfShareCertificatesEtc = '' #株券等保有割合

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
			elif fact.concept.qname.localName == 'CabinetOfficeOrdinanceOnDisclosureOfStatusOfLargeVolumeHoldingOfShareCertificatesEtcFormNo3ReportOfLargeVolumeHoldingHeading': #株券等の大量保有の状況の開示に関する内閣府令 第三号様式 大量保有報告書 [目次項目]
				self.CabinetOfficeOrdinanceOnDisclosureOfStatusOfLargeVolumeHoldingOfShareCertificatesEtcFormNo3ReportOfLargeVolumeHoldingHeading = fact.value

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

			elif fact.concept.qname.localName == 'NameCoverPage': #氏名又は名称、表紙
				self.NameCoverPage = fact.value

			elif fact.concept.qname.localName == 'ResidentialAddressOrAddressOfRegisteredHeadquarterCoverPage': #住所又は本店所在地、表紙
				self.ResidentialAddressOrAddressOfRegisteredHeadquarterCoverPage = fact.value

			elif fact.concept.qname.localName == 'DateWhenFilingRequirementAroseCoverPage': #報告義務発生日、表紙
				self.DateWhenFilingRequirementAroseCoverPage = fact.value

			elif fact.concept.qname.localName == 'FilingDateCoverPage': #提出日、表紙
				self.FilingDateCoverPage = fact.value

			elif fact.concept.qname.localName == 'TotalNumberOfFilersAndJointHoldersCoverPage': #提出者及び共同保有者の総数（名）、表紙
				self.TotalNumberOfFilersAndJointHoldersCoverPage = fact.value

			elif fact.concept.qname.localName == 'ArrangementOfFilingCoverPage': #提出形態、表紙
				self.ArrangementOfFilingCoverPage = fact.value

			elif fact.concept.qname.localName == 'ReasonForFilingChangeReportCoverPage': #変更報告書提出事由、表紙
				self.ReasonForFilingChangeReportCoverPage = fact.value

			elif fact.concept.qname.localName == 'ReasonForFilingChangeReportCoverPageNA': #変更報告書提出事由、表紙（該当なし）
				self.ReasonForFilingChangeReportCoverPageNA = fact.value

			elif fact.concept.qname.localName == 'InformationAboutIssuerHeading': #発行者に関する事項 [目次項目]
				self.InformationAboutIssuerHeading = fact.value

			elif fact.concept.qname.localName == 'InformationAboutIssuerHeading': #発行者に関する事項 [目次項目]
				self.InformationAboutIssuerHeading = fact.value

			elif fact.concept.qname.localName == 'NameOfIssuer': #発行者の名称
				self.NameOfIssuer = fact.value

			elif fact.concept.qname.localName == 'SecurityCodeOfIssuer': #発行者の証券コード
				self.SecurityCodeOfIssuer = fact.value

			elif fact.concept.qname.localName == 'ListedOrOTC': #上場・店頭の別
				self.ListedOrOTC = fact.value

			elif fact.concept.qname.localName == 'StockListing': #上場金融商品取引所
				self.StockListing = fact.value

			elif fact.concept.qname.localName == 'InformationAboutFilersHeading': #提出者に関する事項 [目次項目]
				self.InformationAboutFilersHeading = fact.value

			elif fact.concept.qname.localName == 'InformationAboutFilersHeading': #提出者に関する事項 [目次項目]
				self.InformationAboutFilersHeading = fact.value

			elif fact.concept.qname.localName == 'InformationAboutFilersTable': #提出者に関する事項 [表]
				self.InformationAboutFilersTable = fact.value

			elif fact.concept.qname.localName == 'FilersLargeVolumeHoldersAndJointHoldersAxis': #提出者（大量保有者）・共同保有者 [軸]
				self.FilersLargeVolumeHoldersAndJointHoldersAxis = fact.value

			elif fact.concept.qname.localName == 'FilersLargeVolumeHoldersOrJointHoldersMember': #提出者（大量保有者）・共同保有者 [メンバー] ※ディメンションデフォルト
				self.FilersLargeVolumeHoldersOrJointHoldersMember = fact.value

			elif fact.concept.qname.localName == 'FilersLargeVolumeHoldersMember': #提出者（大量保有者） [メンバー]
				self.FilersLargeVolumeHoldersMember = fact.value

			elif fact.concept.qname.localName == 'InformationAboutFilersLineItems': #提出者に関する事項 [表示項目]
				self.InformationAboutFilersLineItems = fact.value

			elif fact.concept.qname.localName == 'FilerLargeVolumeHolderSerialNumberAbstract': #提出者（大量保有者）／連番 [タイトル項目]
				self.FilerLargeVolumeHolderSerialNumberAbstract = fact.value

			elif fact.concept.qname.localName == 'OverviewOfFilerAbstract': #提出者の概要 [タイトル項目]
				self.OverviewOfFilerAbstract = fact.value

			elif fact.concept.qname.localName == 'FilerLargeVolumeHolderAbstract': #提出者（大量保有者） [タイトル項目]
				self.FilerLargeVolumeHolderAbstract = fact.value

			elif fact.concept.qname.localName == 'IndividualOrCorporation': #個人・法人の別
				self.IndividualOrCorporation = fact.value

			elif fact.concept.qname.localName == 'Name': #氏名又は名称
				self.Name = fact.value

			elif fact.concept.qname.localName == 'ResidentialAddressOrAddressOfRegisteredHeadquarter': #住所又は本店所在地
				self.ResidentialAddressOrAddressOfRegisteredHeadquarter = fact.value

			elif fact.concept.qname.localName == 'FormerName': #旧氏名又は名称
				self.FormerName = fact.value

			elif fact.concept.qname.localName == 'FormerResidentialAddressOrAddressOfRegisteredHeadquarter': #旧住所又は本店所在地
				self.FormerResidentialAddressOrAddressOfRegisteredHeadquarter = fact.value

			elif fact.concept.qname.localName == 'InformationAboutIndividualAbstract': #個人の場合 [タイトル項目]
				self.InformationAboutIndividualAbstract = fact.value

			elif fact.concept.qname.localName == 'InformationAboutIndividualNATextBlock': #個人の場合（該当なし） [テキストブロック]
				self.InformationAboutIndividualNATextBlock = fact.value

			elif fact.concept.qname.localName == 'DateOfBirth': #生年月日
				self.DateOfBirth = fact.value

			elif fact.concept.qname.localName == 'Occupation': #職業
				self.Occupation = fact.value

			elif fact.concept.qname.localName == 'NameOfEmployer': #勤務先名称
				self.NameOfEmployer = fact.value

			elif fact.concept.qname.localName == 'AddressOfEmployer': #勤務先住所
				self.AddressOfEmployer = fact.value

			elif fact.concept.qname.localName == 'InformationAboutCorporationAbstract': #法人の場合 [タイトル項目]
				self.InformationAboutCorporationAbstract = fact.value

			elif fact.concept.qname.localName == 'InformationAboutCorporationNATextBlock': #法人の場合（該当なし） [テキストブロック]
				self.InformationAboutCorporationNATextBlock = fact.value

			elif fact.concept.qname.localName == 'DateOfEstablishment': #設立年月日
				self.DateOfEstablishment = fact.value

			elif fact.concept.qname.localName == 'NameOfRepresentative': #代表者氏名
				self.NameOfRepresentative = fact.value

			elif fact.concept.qname.localName == 'JobTitleOfRepresentative': #代表者役職
				self.JobTitleOfRepresentative = fact.value

			elif fact.concept.qname.localName == 'DescriptionOfBusiness': #事業内容
				self.DescriptionOfBusiness = fact.value

			elif fact.concept.qname.localName == 'ContactInformationAbstract': #事務上の連絡先 [タイトル項目]
				self.ContactInformationAbstract = fact.value

			elif fact.concept.qname.localName == 'ContactInformationAndPerson': #事務上の連絡先及び担当者名
				self.ContactInformationAndPerson = fact.value

			elif fact.concept.qname.localName == 'TelephoneNumber': #電話番号
				self.TelephoneNumber = fact.value

			elif fact.concept.qname.localName == 'PurposeOfHoldingAbstract': #保有目的 [タイトル項目]
				self.PurposeOfHoldingAbstract = fact.value

			elif fact.concept.qname.localName == 'PurposeOfHolding': #保有目的
				self.PurposeOfHolding = fact.value

			elif fact.concept.qname.localName == 'PurposeOfHoldingNA': #保有目的（該当なし）
				self.PurposeOfHoldingNA = fact.value

			elif fact.concept.qname.localName == 'BreakdownOfStocksEtcHeldBySaidFilerAbstract': #上記提出者の保有株券等の内訳 [タイトル項目]
				self.BreakdownOfStocksEtcHeldBySaidFilerAbstract = fact.value

			elif fact.concept.qname.localName == 'NumberOfStocksEtcHeldAbstract': #保有株券等の数 [タイトル項目]
				self.NumberOfStocksEtcHeldAbstract = fact.value

			elif fact.concept.qname.localName == 'Article27233MainClauseAbstract': #法第27条の23第3項本文 [タイトル項目]
				self.Article27233MainClauseAbstract = fact.value

			elif fact.concept.qname.localName == 'StocksOrInvestmentSecuritiesEtcArticle27233MainClause': #株券又は投資証券等、法第27条の23第3項本文
				self.StocksOrInvestmentSecuritiesEtcArticle27233MainClause = fact.value

			elif fact.concept.qname.localName == 'SubscriptionRightsToSharesArticle27233MainClause': #新株予約権証券又は新投資口予約権証券等、法第27条の23第3項本文
				self.SubscriptionRightsToSharesArticle27233MainClause = fact.value

			elif fact.concept.qname.localName == 'ConvertibleBondsArticle27233MainClause': #新株予約権付社債券、法第27条の23第3項本文
				self.ConvertibleBondsArticle27233MainClause = fact.value

			elif fact.concept.qname.localName == 'TargetSecurityCoveredWarrantsArticle27233MainClause': #対象有価証券カバードワラント、法第27条の23第3項本文
				self.TargetSecurityCoveredWarrantsArticle27233MainClause = fact.value

			elif fact.concept.qname.localName == 'StockDepositoryReceiptsArticle27233MainClause': #株券預託証券、法第27条の23第3項本文
				self.StockDepositoryReceiptsArticle27233MainClause = fact.value

			elif fact.concept.qname.localName == 'StockRelatedDepositoryReceiptsArticle27233MainClause': #株券関連預託証券、法第27条の23第3項本文
				self.StockRelatedDepositoryReceiptsArticle27233MainClause = fact.value

			elif fact.concept.qname.localName == 'StockTrustBeneficiaryRightsArticle27233MainClause': #株券信託受益証券、法第27条の23第3項本文
				self.StockTrustBeneficiaryRightsArticle27233MainClause = fact.value

			elif fact.concept.qname.localName == 'StockRelatedTrustBeneficiaryRightsArticle27233MainClause': #株券関連信託受益証券、法第27条の23第3項本文
				self.StockRelatedTrustBeneficiaryRightsArticle27233MainClause = fact.value

			elif fact.concept.qname.localName == 'TargetSecurityRedeemableBondsArticle27233MainClause': #対象有価証券償還社債、法第27条の23第3項本文
				self.TargetSecurityRedeemableBondsArticle27233MainClause = fact.value

			elif fact.concept.qname.localName == 'ExchangeableBondsArticle27233MainClause': #他社株等転換株券、法第27条の23第3項本文
				self.ExchangeableBondsArticle27233MainClause = fact.value

			elif fact.concept.qname.localName == 'TotalArticle27233MainClause': #合計、法第27条の23第3項本文
				self.TotalArticle27233MainClause = fact.value

			elif fact.concept.qname.localName == 'Article27233Item1Abstract': #法第27条の23第3項第１号 [タイトル項目]
				self.Article27233Item1Abstract = fact.value

			elif fact.concept.qname.localName == 'StocksOrInvestmentSecuritiesEtcArticle27233Item1': #株券又は投資証券等、法第27条の23第3項第１号
				self.StocksOrInvestmentSecuritiesEtcArticle27233Item1 = fact.value

			elif fact.concept.qname.localName == 'TargetSecurityCoveredWarrantsArticle27233Item1': #対象有価証券カバードワラント、法第27条の23第3項第１号
				self.TargetSecurityCoveredWarrantsArticle27233Item1 = fact.value

			elif fact.concept.qname.localName == 'StockDepositoryReceiptsArticle27233Item1': #株券預託証券、法第27条の23第3項第１号
				self.StockDepositoryReceiptsArticle27233Item1 = fact.value

			elif fact.concept.qname.localName == 'StockRelatedDepositoryReceiptsArticle27233Item1': #株券関連預託証券、法第27条の23第3項第１号
				self.StockRelatedDepositoryReceiptsArticle27233Item1 = fact.value

			elif fact.concept.qname.localName == 'StockTrustBeneficiaryRightsArticle27233Item1': #株券信託受益証券、法第27条の23第3項第１号
				self.StockTrustBeneficiaryRightsArticle27233Item1 = fact.value

			elif fact.concept.qname.localName == 'StockRelatedTrustBeneficiaryRightsArticle27233Item1': #株券関連信託受益証券、法第27条の23第3項第１号
				self.StockRelatedTrustBeneficiaryRightsArticle27233Item1 = fact.value

			elif fact.concept.qname.localName == 'TargetSecurityRedeemableBondsArticle27233Item1': #対象有価証券償還社債、法第27条の23第3項第１号
				self.TargetSecurityRedeemableBondsArticle27233Item1 = fact.value

			elif fact.concept.qname.localName == 'ExchangeableBondsArticle27233Item1': #他社株等転換株券、法第27条の23第3項第１号
				self.ExchangeableBondsArticle27233Item1 = fact.value

			elif fact.concept.qname.localName == 'TotalArticle27233Item1': #合計、法第27条の23第3項第１号
				self.TotalArticle27233Item1 = fact.value

			elif fact.concept.qname.localName == 'Article27233Item2Abstract': #法第27条の23第3項第2号 [タイトル項目]
				self.Article27233Item2Abstract = fact.value

			elif fact.concept.qname.localName == 'StocksOrInvestmentSecuritiesEtcArticle27233Item2': #株券又は投資証券等、法第27条の23第3項第2号
				self.StocksOrInvestmentSecuritiesEtcArticle27233Item2 = fact.value

			elif fact.concept.qname.localName == 'SubscriptionRightsToSharesArticle27233Item2': #新株予約権証券又は新投資口予約権証券等、法第27条の23第3項第2号
				self.SubscriptionRightsToSharesArticle27233Item2 = fact.value

			elif fact.concept.qname.localName == 'ConvertibleBondsArticle27233Item2': #新株予約権付社債券、法第27条の23第3項第2号
				self.ConvertibleBondsArticle27233Item2 = fact.value

			elif fact.concept.qname.localName == 'TargetSecurityCoveredWarrantsArticle27233Item2': #対象有価証券カバードワラント、法第27条の23第3項第2号
				self.TargetSecurityCoveredWarrantsArticle27233Item2 = fact.value

			elif fact.concept.qname.localName == 'StockDepositoryReceiptsArticle27233Item2': #株券預託証券、法第27条の23第3項第2号
				self.StockDepositoryReceiptsArticle27233Item2 = fact.value

			elif fact.concept.qname.localName == 'StockRelatedDepositoryReceiptsArticle27233Item2': #株券関連預託証券、法第27条の23第3項第2号
				self.StockRelatedDepositoryReceiptsArticle27233Item2 = fact.value

			elif fact.concept.qname.localName == 'StockTrustBeneficiaryRightsArticle27233Item2': #株券信託受益証券、法第27条の23第3項第2号
				self.StockTrustBeneficiaryRightsArticle27233Item2 = fact.value

			elif fact.concept.qname.localName == 'StockRelatedTrustBeneficiaryRightsArticle27233Item2': #株券関連信託受益証券、法第27条の23第3項第2号
				self.StockRelatedTrustBeneficiaryRightsArticle27233Item2 = fact.value

			elif fact.concept.qname.localName == 'TargetSecurityRedeemableBondsArticle27233Item2': #対象有価証券償還社債、法第27条の23第3項第2号
				self.TargetSecurityRedeemableBondsArticle27233Item2 = fact.value

			elif fact.concept.qname.localName == 'ExchangeableBondsArticle27233Item2': #他社株等転換株券、法第27条の23第3項第2号
				self.ExchangeableBondsArticle27233Item2 = fact.value

			elif fact.concept.qname.localName == 'TotalArticle27233Item2': #合計、法第27条の23第3項第2号
				self.TotalArticle27233Item2 = fact.value

			elif fact.concept.qname.localName == 'NumberOfStocksEtcToDeductAsSoldOnMarginTrading': #信用取引により譲渡したことにより控除する株券等の数
				self.NumberOfStocksEtcToDeductAsSoldOnMarginTrading = fact.value

			elif fact.concept.qname.localName == 'NumberOfStocksEtcToDeductAsRightsToDemandExistBetweenJointHolders': #共同保有者間で引渡請求権等の権利が存在するものとして控除する株券等の数
				self.NumberOfStocksEtcToDeductAsRightsToDemandExistBetweenJointHolders = fact.value

			elif fact.concept.qname.localName == 'TotalNumberOfStocksEtcHeld': #保有株券等の数（総数）
				self.TotalNumberOfStocksEtcHeld = fact.value

			elif fact.concept.qname.localName == 'NumberOfResidualStocksHeld': #保有潜在株券等の数
				self.NumberOfResidualStocksHeld = fact.value

			elif fact.concept.qname.localName == 'NotesNumberOfStocksEtcHeldTextBlock': #欄外注記、保有株券等の数 [テキストブロック]
				self.NotesNumberOfStocksEtcHeldTextBlock = fact.value

			elif fact.concept.qname.localName == 'HoldingRatioOfShareCertificatesEtcAbstract': #株券等保有割合 [タイトル項目]
				self.HoldingRatioOfShareCertificatesEtcAbstract = fact.value

			elif fact.concept.qname.localName == 'TotalNumberOfOutstandingStocksEtcAbstract': #発行済株式等総数 [タイトル項目]
				self.TotalNumberOfOutstandingStocksEtcAbstract = fact.value

			elif fact.concept.qname.localName == 'BaseDate': #基準日
				self.BaseDate = fact.value

			elif fact.concept.qname.localName == 'TotalNumberOfOutstandingStocksEtc': #発行済株式等総数
				self.TotalNumberOfOutstandingStocksEtc = fact.value

			elif fact.concept.qname.localName == 'HoldingRatioOfShareCertificatesEtc': #株券等保有割合
				self.HoldingRatioOfShareCertificatesEtc = fact.value

			elif fact.concept.qname.localName == 'HoldingRatioOfShareCertificatesEtcPerLastReport': #直前の報告書に記載された株券等保有割合
				self.HoldingRatioOfShareCertificatesEtcPerLastReport = fact.value

			elif fact.concept.qname.localName == 'NotesHoldingRatioOfShareCertificatesEtcTextBlock': #欄外注記、株券等保有割合 [テキストブロック]
				self.NotesHoldingRatioOfShareCertificatesEtcTextBlock = fact.value

			elif fact.concept.qname.localName == 'SignificantContractsRelatedToSaidStocksEtcSuchAsCollateralAgreementsAbstract': #当該株券等に関する担保契約等重要な契約 [タイトル項目]
				self.SignificantContractsRelatedToSaidStocksEtcSuchAsCollateralAgreementsAbstract = fact.value

			elif fact.concept.qname.localName == 'SignificantContractsRelatedToSaidStocksEtcSuchAsCollateralAgreementsTextBlock': #当該株券等に関する担保契約等重要な契約 [テキストブロック]
				self.SignificantContractsRelatedToSaidStocksEtcSuchAsCollateralAgreementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'SignificantContractsRelatedToSaidStocksEtcSuchAsCollateralAgreementsNA': #当該株券等に関する担保契約等重要な契約（該当なし）
				self.SignificantContractsRelatedToSaidStocksEtcSuchAsCollateralAgreementsNA = fact.value

			elif fact.concept.qname.localName == 'InformationAboutJointHoldersHeading': #共同保有者に関する事項 [目次項目]
				self.InformationAboutJointHoldersHeading = fact.value

			elif fact.concept.qname.localName == 'InformationAboutJointHoldersHeading': #共同保有者に関する事項 [目次項目]
				self.InformationAboutJointHoldersHeading = fact.value

			elif fact.concept.qname.localName == 'InformationAboutJointHoldersTable': #共同保有者に関する事項 [表]
				self.InformationAboutJointHoldersTable = fact.value

			elif fact.concept.qname.localName == 'FilersLargeVolumeHoldersAndJointHoldersAxis': #提出者（大量保有者）・共同保有者 [軸]
				self.FilersLargeVolumeHoldersAndJointHoldersAxis = fact.value

			elif fact.concept.qname.localName == 'FilersLargeVolumeHoldersOrJointHoldersMember': #提出者（大量保有者）・共同保有者 [メンバー] ※ディメンションデフォルト
				self.FilersLargeVolumeHoldersOrJointHoldersMember = fact.value

			elif fact.concept.qname.localName == 'JointHoldersMember': #共同保有者 [メンバー]
				self.JointHoldersMember = fact.value

			elif fact.concept.qname.localName == 'InformationAboutJointHoldersLineItems': #共同保有者に関する事項 [表示項目]
				self.InformationAboutJointHoldersLineItems = fact.value

			elif fact.concept.qname.localName == 'JointHolderSerialNumberAbstract': #共同保有者／連番 [タイトル項目]
				self.JointHolderSerialNumberAbstract = fact.value

			elif fact.concept.qname.localName == 'OverviewOfJointHolderAbstract': #共同保有者の概要 [タイトル項目]
				self.OverviewOfJointHolderAbstract = fact.value

			elif fact.concept.qname.localName == 'JointHolderAbstract': #共同保有者 [タイトル項目]
				self.JointHolderAbstract = fact.value

			elif fact.concept.qname.localName == 'IndividualOrCorporation': #個人・法人の別
				self.IndividualOrCorporation = fact.value

			elif fact.concept.qname.localName == 'Name': #氏名又は名称
				self.Name = fact.value

			elif fact.concept.qname.localName == 'ResidentialAddressOrAddressOfRegisteredHeadquarter': #住所又は本店所在地
				self.ResidentialAddressOrAddressOfRegisteredHeadquarter = fact.value

			elif fact.concept.qname.localName == 'FormerName': #旧氏名又は名称
				self.FormerName = fact.value

			elif fact.concept.qname.localName == 'FormerResidentialAddressOrAddressOfRegisteredHeadquarter': #旧住所又は本店所在地
				self.FormerResidentialAddressOrAddressOfRegisteredHeadquarter = fact.value

			elif fact.concept.qname.localName == 'InformationAboutIndividualAbstract': #個人の場合 [タイトル項目]
				self.InformationAboutIndividualAbstract = fact.value

			elif fact.concept.qname.localName == 'InformationAboutIndividualNATextBlock': #個人の場合（該当なし） [テキストブロック]
				self.InformationAboutIndividualNATextBlock = fact.value

			elif fact.concept.qname.localName == 'DateOfBirth': #生年月日
				self.DateOfBirth = fact.value

			elif fact.concept.qname.localName == 'Occupation': #職業
				self.Occupation = fact.value

			elif fact.concept.qname.localName == 'NameOfEmployer': #勤務先名称
				self.NameOfEmployer = fact.value

			elif fact.concept.qname.localName == 'AddressOfEmployer': #勤務先住所
				self.AddressOfEmployer = fact.value

			elif fact.concept.qname.localName == 'InformationAboutCorporationAbstract': #法人の場合 [タイトル項目]
				self.InformationAboutCorporationAbstract = fact.value

			elif fact.concept.qname.localName == 'InformationAboutCorporationNATextBlock': #法人の場合（該当なし） [テキストブロック]
				self.InformationAboutCorporationNATextBlock = fact.value

			elif fact.concept.qname.localName == 'DateOfEstablishment': #設立年月日
				self.DateOfEstablishment = fact.value

			elif fact.concept.qname.localName == 'NameOfRepresentative': #代表者氏名
				self.NameOfRepresentative = fact.value

			elif fact.concept.qname.localName == 'JobTitleOfRepresentative': #代表者役職
				self.JobTitleOfRepresentative = fact.value

			elif fact.concept.qname.localName == 'DescriptionOfBusiness': #事業内容
				self.DescriptionOfBusiness = fact.value

			elif fact.concept.qname.localName == 'ContactInformationAbstract': #事務上の連絡先 [タイトル項目]
				self.ContactInformationAbstract = fact.value

			elif fact.concept.qname.localName == 'ContactInformationAndPerson': #事務上の連絡先及び担当者名
				self.ContactInformationAndPerson = fact.value

			elif fact.concept.qname.localName == 'TelephoneNumber': #電話番号
				self.TelephoneNumber = fact.value

			elif fact.concept.qname.localName == 'BreakdownOfStocksEtcHeldBySaidJointHolderAbstract': #上記共同保有者の保有株券等の内訳 [タイトル項目]
				self.BreakdownOfStocksEtcHeldBySaidJointHolderAbstract = fact.value

			elif fact.concept.qname.localName == 'NumberOfStocksEtcHeldAbstract': #保有株券等の数 [タイトル項目]
				self.NumberOfStocksEtcHeldAbstract = fact.value

			elif fact.concept.qname.localName == 'Article27233MainClauseAbstract': #法第27条の23第3項本文 [タイトル項目]
				self.Article27233MainClauseAbstract = fact.value

			elif fact.concept.qname.localName == 'StocksOrInvestmentSecuritiesEtcArticle27233MainClause': #株券又は投資証券等、法第27条の23第3項本文
				self.StocksOrInvestmentSecuritiesEtcArticle27233MainClause = fact.value

			elif fact.concept.qname.localName == 'SubscriptionRightsToSharesArticle27233MainClause': #新株予約権証券又は新投資口予約権証券等、法第27条の23第3項本文
				self.SubscriptionRightsToSharesArticle27233MainClause = fact.value

			elif fact.concept.qname.localName == 'ConvertibleBondsArticle27233MainClause': #新株予約権付社債券、法第27条の23第3項本文
				self.ConvertibleBondsArticle27233MainClause = fact.value

			elif fact.concept.qname.localName == 'TargetSecurityCoveredWarrantsArticle27233MainClause': #対象有価証券カバードワラント、法第27条の23第3項本文
				self.TargetSecurityCoveredWarrantsArticle27233MainClause = fact.value

			elif fact.concept.qname.localName == 'StockDepositoryReceiptsArticle27233MainClause': #株券預託証券、法第27条の23第3項本文
				self.StockDepositoryReceiptsArticle27233MainClause = fact.value

			elif fact.concept.qname.localName == 'StockRelatedDepositoryReceiptsArticle27233MainClause': #株券関連預託証券、法第27条の23第3項本文
				self.StockRelatedDepositoryReceiptsArticle27233MainClause = fact.value

			elif fact.concept.qname.localName == 'StockTrustBeneficiaryRightsArticle27233MainClause': #株券信託受益証券、法第27条の23第3項本文
				self.StockTrustBeneficiaryRightsArticle27233MainClause = fact.value

			elif fact.concept.qname.localName == 'StockRelatedTrustBeneficiaryRightsArticle27233MainClause': #株券関連信託受益証券、法第27条の23第3項本文
				self.StockRelatedTrustBeneficiaryRightsArticle27233MainClause = fact.value

			elif fact.concept.qname.localName == 'TargetSecurityRedeemableBondsArticle27233MainClause': #対象有価証券償還社債、法第27条の23第3項本文
				self.TargetSecurityRedeemableBondsArticle27233MainClause = fact.value

			elif fact.concept.qname.localName == 'ExchangeableBondsArticle27233MainClause': #他社株等転換株券、法第27条の23第3項本文
				self.ExchangeableBondsArticle27233MainClause = fact.value

			elif fact.concept.qname.localName == 'TotalArticle27233MainClause': #合計、法第27条の23第3項本文
				self.TotalArticle27233MainClause = fact.value

			elif fact.concept.qname.localName == 'Article27233Item1Abstract': #法第27条の23第3項第１号 [タイトル項目]
				self.Article27233Item1Abstract = fact.value

			elif fact.concept.qname.localName == 'StocksOrInvestmentSecuritiesEtcArticle27233Item1': #株券又は投資証券等、法第27条の23第3項第１号
				self.StocksOrInvestmentSecuritiesEtcArticle27233Item1 = fact.value

			elif fact.concept.qname.localName == 'TargetSecurityCoveredWarrantsArticle27233Item1': #対象有価証券カバードワラント、法第27条の23第3項第１号
				self.TargetSecurityCoveredWarrantsArticle27233Item1 = fact.value

			elif fact.concept.qname.localName == 'StockDepositoryReceiptsArticle27233Item1': #株券預託証券、法第27条の23第3項第１号
				self.StockDepositoryReceiptsArticle27233Item1 = fact.value

			elif fact.concept.qname.localName == 'StockRelatedDepositoryReceiptsArticle27233Item1': #株券関連預託証券、法第27条の23第3項第１号
				self.StockRelatedDepositoryReceiptsArticle27233Item1 = fact.value

			elif fact.concept.qname.localName == 'StockTrustBeneficiaryRightsArticle27233Item1': #株券信託受益証券、法第27条の23第3項第１号
				self.StockTrustBeneficiaryRightsArticle27233Item1 = fact.value

			elif fact.concept.qname.localName == 'StockRelatedTrustBeneficiaryRightsArticle27233Item1': #株券関連信託受益証券、法第27条の23第3項第１号
				self.StockRelatedTrustBeneficiaryRightsArticle27233Item1 = fact.value

			elif fact.concept.qname.localName == 'TargetSecurityRedeemableBondsArticle27233Item1': #対象有価証券償還社債、法第27条の23第3項第１号
				self.TargetSecurityRedeemableBondsArticle27233Item1 = fact.value

			elif fact.concept.qname.localName == 'ExchangeableBondsArticle27233Item1': #他社株等転換株券、法第27条の23第3項第１号
				self.ExchangeableBondsArticle27233Item1 = fact.value

			elif fact.concept.qname.localName == 'TotalArticle27233Item1': #合計、法第27条の23第3項第１号
				self.TotalArticle27233Item1 = fact.value

			elif fact.concept.qname.localName == 'Article27233Item2Abstract': #法第27条の23第3項第2号 [タイトル項目]
				self.Article27233Item2Abstract = fact.value

			elif fact.concept.qname.localName == 'StocksOrInvestmentSecuritiesEtcArticle27233Item2': #株券又は投資証券等、法第27条の23第3項第2号
				self.StocksOrInvestmentSecuritiesEtcArticle27233Item2 = fact.value

			elif fact.concept.qname.localName == 'SubscriptionRightsToSharesArticle27233Item2': #新株予約権証券又は新投資口予約権証券等、法第27条の23第3項第2号
				self.SubscriptionRightsToSharesArticle27233Item2 = fact.value

			elif fact.concept.qname.localName == 'ConvertibleBondsArticle27233Item2': #新株予約権付社債券、法第27条の23第3項第2号
				self.ConvertibleBondsArticle27233Item2 = fact.value

			elif fact.concept.qname.localName == 'TargetSecurityCoveredWarrantsArticle27233Item2': #対象有価証券カバードワラント、法第27条の23第3項第2号
				self.TargetSecurityCoveredWarrantsArticle27233Item2 = fact.value

			elif fact.concept.qname.localName == 'StockDepositoryReceiptsArticle27233Item2': #株券預託証券、法第27条の23第3項第2号
				self.StockDepositoryReceiptsArticle27233Item2 = fact.value

			elif fact.concept.qname.localName == 'StockRelatedDepositoryReceiptsArticle27233Item2': #株券関連預託証券、法第27条の23第3項第2号
				self.StockRelatedDepositoryReceiptsArticle27233Item2 = fact.value

			elif fact.concept.qname.localName == 'StockTrustBeneficiaryRightsArticle27233Item2': #株券信託受益証券、法第27条の23第3項第2号
				self.StockTrustBeneficiaryRightsArticle27233Item2 = fact.value

			elif fact.concept.qname.localName == 'StockRelatedTrustBeneficiaryRightsArticle27233Item2': #株券関連信託受益証券、法第27条の23第3項第2号
				self.StockRelatedTrustBeneficiaryRightsArticle27233Item2 = fact.value

			elif fact.concept.qname.localName == 'TargetSecurityRedeemableBondsArticle27233Item2': #対象有価証券償還社債、法第27条の23第3項第2号
				self.TargetSecurityRedeemableBondsArticle27233Item2 = fact.value

			elif fact.concept.qname.localName == 'ExchangeableBondsArticle27233Item2': #他社株等転換株券、法第27条の23第3項第2号
				self.ExchangeableBondsArticle27233Item2 = fact.value

			elif fact.concept.qname.localName == 'TotalArticle27233Item2': #合計、法第27条の23第3項第2号
				self.TotalArticle27233Item2 = fact.value

			elif fact.concept.qname.localName == 'NumberOfStocksEtcToDeductAsSoldOnMarginTrading': #信用取引により譲渡したことにより控除する株券等の数
				self.NumberOfStocksEtcToDeductAsSoldOnMarginTrading = fact.value

			elif fact.concept.qname.localName == 'NumberOfStocksEtcToDeductAsRightsToDemandExistBetweenJointHolders': #共同保有者間で引渡請求権等の権利が存在するものとして控除する株券等の数
				self.NumberOfStocksEtcToDeductAsRightsToDemandExistBetweenJointHolders = fact.value

			elif fact.concept.qname.localName == 'TotalNumberOfStocksEtcHeld': #保有株券等の数（総数）
				self.TotalNumberOfStocksEtcHeld = fact.value

			elif fact.concept.qname.localName == 'NumberOfResidualStocksHeld': #保有潜在株券等の数
				self.NumberOfResidualStocksHeld = fact.value

			elif fact.concept.qname.localName == 'NotesNumberOfStocksEtcHeldTextBlock': #欄外注記、保有株券等の数 [テキストブロック]
				self.NotesNumberOfStocksEtcHeldTextBlock = fact.value

			elif fact.concept.qname.localName == 'HoldingRatioOfShareCertificatesEtcAbstract': #株券等保有割合 [タイトル項目]
				self.HoldingRatioOfShareCertificatesEtcAbstract = fact.value

			elif fact.concept.qname.localName == 'TotalNumberOfOutstandingStocksEtcAbstract': #発行済株式等総数 [タイトル項目]
				self.TotalNumberOfOutstandingStocksEtcAbstract = fact.value

			elif fact.concept.qname.localName == 'BaseDate': #基準日
				self.BaseDate = fact.value

			elif fact.concept.qname.localName == 'TotalNumberOfOutstandingStocksEtc': #発行済株式等総数
				self.TotalNumberOfOutstandingStocksEtc = fact.value

			elif fact.concept.qname.localName == 'HoldingRatioOfShareCertificatesEtc': #株券等保有割合
				self.HoldingRatioOfShareCertificatesEtc = fact.value

			elif fact.concept.qname.localName == 'HoldingRatioOfShareCertificatesEtcPerLastReport': #直前の報告書に記載された株券等保有割合
				self.HoldingRatioOfShareCertificatesEtcPerLastReport = fact.value

			elif fact.concept.qname.localName == 'NotesHoldingRatioOfShareCertificatesEtcTextBlock': #欄外注記、株券等保有割合 [テキストブロック]
				self.NotesHoldingRatioOfShareCertificatesEtcTextBlock = fact.value

			elif fact.concept.qname.localName == 'InformationAboutJointHoldersNA': #共同保有者に関する事項（該当なし）
				self.InformationAboutJointHoldersNA = fact.value

			elif fact.concept.qname.localName == 'SummaryOfFilerAndJointHoldersHeading': #提出者及び共同保有者に関する総括表 [目次項目]
				self.SummaryOfFilerAndJointHoldersHeading = fact.value

			elif fact.concept.qname.localName == 'FilersAndJointHoldersHeading': #提出者及び共同保有者 [目次項目]
				self.FilersAndJointHoldersHeading = fact.value

			elif fact.concept.qname.localName == 'FilersAndJointHoldersHeading': #提出者及び共同保有者 [目次項目]
				self.FilersAndJointHoldersHeading = fact.value

			elif fact.concept.qname.localName == 'FilersAndJointHoldersTable': #提出者及び共同保有者 [表]
				self.FilersAndJointHoldersTable = fact.value

			elif fact.concept.qname.localName == 'FilersLargeVolumeHoldersAndJointHoldersAxis': #提出者（大量保有者）・共同保有者 [軸]
				self.FilersLargeVolumeHoldersAndJointHoldersAxis = fact.value

			elif fact.concept.qname.localName == 'FilersLargeVolumeHoldersOrJointHoldersMember': #提出者（大量保有者）・共同保有者 [メンバー] ※ディメンションデフォルト
				self.FilersLargeVolumeHoldersOrJointHoldersMember = fact.value

			elif fact.concept.qname.localName == 'FilersAndJointHoldersLineItems': #提出者及び共同保有者 [表示項目]
				self.FilersAndJointHoldersLineItems = fact.value

			elif fact.concept.qname.localName == 'Name': #氏名又は名称
				self.Name = fact.value

			elif fact.concept.qname.localName == 'BreakdownOfStocksEtcHeldBySaidFilerAndJointHoldersHeading': #上記提出者及び共同保有者の保有株券等の内訳 [目次項目]
				self.BreakdownOfStocksEtcHeldBySaidFilerAndJointHoldersHeading = fact.value

			elif fact.concept.qname.localName == 'NumberOfStocksEtcHeldSummaryHeading': #保有株券等の数、総括表 [目次項目]
				self.NumberOfStocksEtcHeldSummaryHeading = fact.value

			elif fact.concept.qname.localName == 'NumberOfStocksEtcHeldSummaryHeading': #保有株券等の数、総括表 [目次項目]
				self.NumberOfStocksEtcHeldSummaryHeading = fact.value

			elif fact.concept.qname.localName == 'Article27233MainClauseAbstract': #法第27条の23第3項本文 [タイトル項目]
				self.Article27233MainClauseAbstract = fact.value

			elif fact.concept.qname.localName == 'StocksOrInvestmentSecuritiesEtcArticle27233MainClause': #株券又は投資証券等、法第27条の23第3項本文
				self.StocksOrInvestmentSecuritiesEtcArticle27233MainClause = fact.value

			elif fact.concept.qname.localName == 'SubscriptionRightsToSharesArticle27233MainClause': #新株予約権証券又は新投資口予約権証券等、法第27条の23第3項本文
				self.SubscriptionRightsToSharesArticle27233MainClause = fact.value

			elif fact.concept.qname.localName == 'ConvertibleBondsArticle27233MainClause': #新株予約権付社債券、法第27条の23第3項本文
				self.ConvertibleBondsArticle27233MainClause = fact.value

			elif fact.concept.qname.localName == 'TargetSecurityCoveredWarrantsArticle27233MainClause': #対象有価証券カバードワラント、法第27条の23第3項本文
				self.TargetSecurityCoveredWarrantsArticle27233MainClause = fact.value

			elif fact.concept.qname.localName == 'StockDepositoryReceiptsArticle27233MainClause': #株券預託証券、法第27条の23第3項本文
				self.StockDepositoryReceiptsArticle27233MainClause = fact.value

			elif fact.concept.qname.localName == 'StockRelatedDepositoryReceiptsArticle27233MainClause': #株券関連預託証券、法第27条の23第3項本文
				self.StockRelatedDepositoryReceiptsArticle27233MainClause = fact.value

			elif fact.concept.qname.localName == 'StockTrustBeneficiaryRightsArticle27233MainClause': #株券信託受益証券、法第27条の23第3項本文
				self.StockTrustBeneficiaryRightsArticle27233MainClause = fact.value

			elif fact.concept.qname.localName == 'StockRelatedTrustBeneficiaryRightsArticle27233MainClause': #株券関連信託受益証券、法第27条の23第3項本文
				self.StockRelatedTrustBeneficiaryRightsArticle27233MainClause = fact.value

			elif fact.concept.qname.localName == 'TargetSecurityRedeemableBondsArticle27233MainClause': #対象有価証券償還社債、法第27条の23第3項本文
				self.TargetSecurityRedeemableBondsArticle27233MainClause = fact.value

			elif fact.concept.qname.localName == 'ExchangeableBondsArticle27233MainClause': #他社株等転換株券、法第27条の23第3項本文
				self.ExchangeableBondsArticle27233MainClause = fact.value

			elif fact.concept.qname.localName == 'TotalArticle27233MainClause': #合計、法第27条の23第3項本文
				self.TotalArticle27233MainClause = fact.value

			elif fact.concept.qname.localName == 'Article27233Item1Abstract': #法第27条の23第3項第１号 [タイトル項目]
				self.Article27233Item1Abstract = fact.value

			elif fact.concept.qname.localName == 'StocksOrInvestmentSecuritiesEtcArticle27233Item1': #株券又は投資証券等、法第27条の23第3項第１号
				self.StocksOrInvestmentSecuritiesEtcArticle27233Item1 = fact.value

			elif fact.concept.qname.localName == 'TargetSecurityCoveredWarrantsArticle27233Item1': #対象有価証券カバードワラント、法第27条の23第3項第１号
				self.TargetSecurityCoveredWarrantsArticle27233Item1 = fact.value

			elif fact.concept.qname.localName == 'StockDepositoryReceiptsArticle27233Item1': #株券預託証券、法第27条の23第3項第１号
				self.StockDepositoryReceiptsArticle27233Item1 = fact.value

			elif fact.concept.qname.localName == 'StockRelatedDepositoryReceiptsArticle27233Item1': #株券関連預託証券、法第27条の23第3項第１号
				self.StockRelatedDepositoryReceiptsArticle27233Item1 = fact.value

			elif fact.concept.qname.localName == 'StockTrustBeneficiaryRightsArticle27233Item1': #株券信託受益証券、法第27条の23第3項第１号
				self.StockTrustBeneficiaryRightsArticle27233Item1 = fact.value

			elif fact.concept.qname.localName == 'StockRelatedTrustBeneficiaryRightsArticle27233Item1': #株券関連信託受益証券、法第27条の23第3項第１号
				self.StockRelatedTrustBeneficiaryRightsArticle27233Item1 = fact.value

			elif fact.concept.qname.localName == 'TargetSecurityRedeemableBondsArticle27233Item1': #対象有価証券償還社債、法第27条の23第3項第１号
				self.TargetSecurityRedeemableBondsArticle27233Item1 = fact.value

			elif fact.concept.qname.localName == 'ExchangeableBondsArticle27233Item1': #他社株等転換株券、法第27条の23第3項第１号
				self.ExchangeableBondsArticle27233Item1 = fact.value

			elif fact.concept.qname.localName == 'TotalArticle27233Item1': #合計、法第27条の23第3項第１号
				self.TotalArticle27233Item1 = fact.value

			elif fact.concept.qname.localName == 'Article27233Item2Abstract': #法第27条の23第3項第2号 [タイトル項目]
				self.Article27233Item2Abstract = fact.value

			elif fact.concept.qname.localName == 'StocksOrInvestmentSecuritiesEtcArticle27233Item2': #株券又は投資証券等、法第27条の23第3項第2号
				self.StocksOrInvestmentSecuritiesEtcArticle27233Item2 = fact.value

			elif fact.concept.qname.localName == 'SubscriptionRightsToSharesArticle27233Item2': #新株予約権証券又は新投資口予約権証券等、法第27条の23第3項第2号
				self.SubscriptionRightsToSharesArticle27233Item2 = fact.value

			elif fact.concept.qname.localName == 'ConvertibleBondsArticle27233Item2': #新株予約権付社債券、法第27条の23第3項第2号
				self.ConvertibleBondsArticle27233Item2 = fact.value

			elif fact.concept.qname.localName == 'TargetSecurityCoveredWarrantsArticle27233Item2': #対象有価証券カバードワラント、法第27条の23第3項第2号
				self.TargetSecurityCoveredWarrantsArticle27233Item2 = fact.value

			elif fact.concept.qname.localName == 'StockDepositoryReceiptsArticle27233Item2': #株券預託証券、法第27条の23第3項第2号
				self.StockDepositoryReceiptsArticle27233Item2 = fact.value

			elif fact.concept.qname.localName == 'StockRelatedDepositoryReceiptsArticle27233Item2': #株券関連預託証券、法第27条の23第3項第2号
				self.StockRelatedDepositoryReceiptsArticle27233Item2 = fact.value

			elif fact.concept.qname.localName == 'StockTrustBeneficiaryRightsArticle27233Item2': #株券信託受益証券、法第27条の23第3項第2号
				self.StockTrustBeneficiaryRightsArticle27233Item2 = fact.value

			elif fact.concept.qname.localName == 'StockRelatedTrustBeneficiaryRightsArticle27233Item2': #株券関連信託受益証券、法第27条の23第3項第2号
				self.StockRelatedTrustBeneficiaryRightsArticle27233Item2 = fact.value

			elif fact.concept.qname.localName == 'TargetSecurityRedeemableBondsArticle27233Item2': #対象有価証券償還社債、法第27条の23第3項第2号
				self.TargetSecurityRedeemableBondsArticle27233Item2 = fact.value

			elif fact.concept.qname.localName == 'ExchangeableBondsArticle27233Item2': #他社株等転換株券、法第27条の23第3項第2号
				self.ExchangeableBondsArticle27233Item2 = fact.value

			elif fact.concept.qname.localName == 'TotalArticle27233Item2': #合計、法第27条の23第3項第2号
				self.TotalArticle27233Item2 = fact.value

			elif fact.concept.qname.localName == 'NumberOfStocksEtcToDeductAsSoldOnMarginTrading': #信用取引により譲渡したことにより控除する株券等の数
				self.NumberOfStocksEtcToDeductAsSoldOnMarginTrading = fact.value

			elif fact.concept.qname.localName == 'NumberOfStocksEtcToDeductAsRightsToDemandExistBetweenJointHolders': #共同保有者間で引渡請求権等の権利が存在するものとして控除する株券等の数
				self.NumberOfStocksEtcToDeductAsRightsToDemandExistBetweenJointHolders = fact.value

			elif fact.concept.qname.localName == 'TotalNumberOfStocksEtcHeld': #保有株券等の数（総数）
				self.TotalNumberOfStocksEtcHeld = fact.value

			elif fact.concept.qname.localName == 'NumberOfResidualStocksHeld': #保有潜在株券等の数
				self.NumberOfResidualStocksHeld = fact.value

			elif fact.concept.qname.localName == 'NotesNumberOfStocksEtcHeldTextBlock': #欄外注記、保有株券等の数 [テキストブロック]
				self.NotesNumberOfStocksEtcHeldTextBlock = fact.value

			elif fact.concept.qname.localName == 'HoldingRatioOfShareCertificatesEtcSummaryHeading': #株券等保有割合、総括表 [目次項目]
				self.HoldingRatioOfShareCertificatesEtcSummaryHeading = fact.value

			elif fact.concept.qname.localName == 'HoldingRatioOfShareCertificatesEtcSummaryHeading': #株券等保有割合、総括表 [目次項目]
				self.HoldingRatioOfShareCertificatesEtcSummaryHeading = fact.value

			elif fact.concept.qname.localName == 'TotalNumberOfOutstandingStocksEtcAbstract': #発行済株式等総数 [タイトル項目]
				self.TotalNumberOfOutstandingStocksEtcAbstract = fact.value

			elif fact.concept.qname.localName == 'BaseDate': #基準日
				self.BaseDate = fact.value

			elif fact.concept.qname.localName == 'TotalNumberOfOutstandingStocksEtc': #発行済株式等総数
				self.TotalNumberOfOutstandingStocksEtc = fact.value

			elif fact.concept.qname.localName == 'HoldingRatioOfShareCertificatesEtc': #株券等保有割合
				self.HoldingRatioOfShareCertificatesEtc = fact.value

			elif fact.concept.qname.localName == 'HoldingRatioOfShareCertificatesEtcPerLastReport': #直前の報告書に記載された株券等保有割合
				self.HoldingRatioOfShareCertificatesEtcPerLastReport = fact.value

			elif fact.concept.qname.localName == 'NotesHoldingRatioOfShareCertificatesEtcTextBlock': #欄外注記、株券等保有割合 [テキストブロック]
				self.NotesHoldingRatioOfShareCertificatesEtcTextBlock = fact.value

			elif fact.concept.qname.localName == 'HoldingRatioOfShareCertificatesEtcHeldByJointHoldingHeading': #共同保有における株券等保有割合の内訳 [目次項目]
				self.HoldingRatioOfShareCertificatesEtcHeldByJointHoldingHeading = fact.value

			elif fact.concept.qname.localName == 'HoldingRatioOfShareCertificatesEtcHeldByJointHoldingHeading': #共同保有における株券等保有割合の内訳 [目次項目]
				self.HoldingRatioOfShareCertificatesEtcHeldByJointHoldingHeading = fact.value

			elif fact.concept.qname.localName == 'HoldingRatioOfShareCertificatesEtcHeldByJointHoldingTable': #共同保有における株券等保有割合の内訳 [表]
				self.HoldingRatioOfShareCertificatesEtcHeldByJointHoldingTable = fact.value

			elif fact.concept.qname.localName == 'FilersLargeVolumeHoldersAndJointHoldersAxis': #提出者（大量保有者）・共同保有者 [軸]
				self.FilersLargeVolumeHoldersAndJointHoldersAxis = fact.value

			elif fact.concept.qname.localName == 'FilersLargeVolumeHoldersOrJointHoldersMember': #提出者（大量保有者）・共同保有者 [メンバー] ※ディメンションデフォルト
				self.FilersLargeVolumeHoldersOrJointHoldersMember = fact.value

			elif fact.concept.qname.localName == 'HoldingRatioOfShareCertificatesEtcHeldByJointHoldingLineItems': #共同保有における株券等保有割合の内訳 [表示項目]
				self.HoldingRatioOfShareCertificatesEtcHeldByJointHoldingLineItems = fact.value

			elif fact.concept.qname.localName == 'Name': #氏名又は名称
				self.Name = fact.value

			elif fact.concept.qname.localName == 'TotalNumberOfStocksEtcHeld': #保有株券等の数（総数）
				self.TotalNumberOfStocksEtcHeld = fact.value

			elif fact.concept.qname.localName == 'HoldingRatioOfShareCertificatesEtc': #株券等保有割合
				self.HoldingRatioOfShareCertificatesEtc = fact.value


	def getCabinetOfficeOrdinanceOnDisclosureOfStatusOfLargeVolumeHoldingOfShareCertificatesEtcFormNo3ReportOfLargeVolumeHoldingHeading(self): #株券等の大量保有の状況の開示に関する内閣府令 第三号様式 大量保有報告書 [目次項目]
		return self.CabinetOfficeOrdinanceOnDisclosureOfStatusOfLargeVolumeHoldingOfShareCertificatesEtcFormNo3ReportOfLargeVolumeHoldingHeading

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

	def getNameCoverPage(self): #氏名又は名称、表紙
		return self.NameCoverPage

	def getResidentialAddressOrAddressOfRegisteredHeadquarterCoverPage(self): #住所又は本店所在地、表紙
		return self.ResidentialAddressOrAddressOfRegisteredHeadquarterCoverPage

	def getDateWhenFilingRequirementAroseCoverPage(self): #報告義務発生日、表紙
		return self.DateWhenFilingRequirementAroseCoverPage

	def getFilingDateCoverPage(self): #提出日、表紙
		return self.FilingDateCoverPage

	def getTotalNumberOfFilersAndJointHoldersCoverPage(self): #提出者及び共同保有者の総数（名）、表紙
		return self.TotalNumberOfFilersAndJointHoldersCoverPage

	def getArrangementOfFilingCoverPage(self): #提出形態、表紙
		return self.ArrangementOfFilingCoverPage

	def getReasonForFilingChangeReportCoverPage(self): #変更報告書提出事由、表紙
		return self.ReasonForFilingChangeReportCoverPage

	def getReasonForFilingChangeReportCoverPageNA(self): #変更報告書提出事由、表紙（該当なし）
		return self.ReasonForFilingChangeReportCoverPageNA

	def getInformationAboutIssuerHeading(self): #発行者に関する事項 [目次項目]
		return self.InformationAboutIssuerHeading

	def getInformationAboutIssuerHeading(self): #発行者に関する事項 [目次項目]
		return self.InformationAboutIssuerHeading

	def getNameOfIssuer(self): #発行者の名称
		return self.NameOfIssuer

	def getSecurityCodeOfIssuer(self): #発行者の証券コード
		return self.SecurityCodeOfIssuer

	def getListedOrOTC(self): #上場・店頭の別
		return self.ListedOrOTC

	def getStockListing(self): #上場金融商品取引所
		return self.StockListing

	def getInformationAboutFilersHeading(self): #提出者に関する事項 [目次項目]
		return self.InformationAboutFilersHeading

	def getInformationAboutFilersHeading(self): #提出者に関する事項 [目次項目]
		return self.InformationAboutFilersHeading

	def getInformationAboutFilersTable(self): #提出者に関する事項 [表]
		return self.InformationAboutFilersTable

	def getFilersLargeVolumeHoldersAndJointHoldersAxis(self): #提出者（大量保有者）・共同保有者 [軸]
		return self.FilersLargeVolumeHoldersAndJointHoldersAxis

	def getFilersLargeVolumeHoldersOrJointHoldersMember(self): #提出者（大量保有者）・共同保有者 [メンバー] ※ディメンションデフォルト
		return self.FilersLargeVolumeHoldersOrJointHoldersMember

	def getFilersLargeVolumeHoldersMember(self): #提出者（大量保有者） [メンバー]
		return self.FilersLargeVolumeHoldersMember

	def getInformationAboutFilersLineItems(self): #提出者に関する事項 [表示項目]
		return self.InformationAboutFilersLineItems

	def getFilerLargeVolumeHolderSerialNumberAbstract(self): #提出者（大量保有者）／連番 [タイトル項目]
		return self.FilerLargeVolumeHolderSerialNumberAbstract

	def getOverviewOfFilerAbstract(self): #提出者の概要 [タイトル項目]
		return self.OverviewOfFilerAbstract

	def getFilerLargeVolumeHolderAbstract(self): #提出者（大量保有者） [タイトル項目]
		return self.FilerLargeVolumeHolderAbstract

	def getIndividualOrCorporation(self): #個人・法人の別
		return self.IndividualOrCorporation

	def getName(self): #氏名又は名称
		return self.Name

	def getResidentialAddressOrAddressOfRegisteredHeadquarter(self): #住所又は本店所在地
		return self.ResidentialAddressOrAddressOfRegisteredHeadquarter

	def getFormerName(self): #旧氏名又は名称
		return self.FormerName

	def getFormerResidentialAddressOrAddressOfRegisteredHeadquarter(self): #旧住所又は本店所在地
		return self.FormerResidentialAddressOrAddressOfRegisteredHeadquarter

	def getInformationAboutIndividualAbstract(self): #個人の場合 [タイトル項目]
		return self.InformationAboutIndividualAbstract

	def getInformationAboutIndividualNATextBlock(self): #個人の場合（該当なし） [テキストブロック]
		return self.InformationAboutIndividualNATextBlock

	def getDateOfBirth(self): #生年月日
		return self.DateOfBirth

	def getOccupation(self): #職業
		return self.Occupation

	def getNameOfEmployer(self): #勤務先名称
		return self.NameOfEmployer

	def getAddressOfEmployer(self): #勤務先住所
		return self.AddressOfEmployer

	def getInformationAboutCorporationAbstract(self): #法人の場合 [タイトル項目]
		return self.InformationAboutCorporationAbstract

	def getInformationAboutCorporationNATextBlock(self): #法人の場合（該当なし） [テキストブロック]
		return self.InformationAboutCorporationNATextBlock

	def getDateOfEstablishment(self): #設立年月日
		return self.DateOfEstablishment

	def getNameOfRepresentative(self): #代表者氏名
		return self.NameOfRepresentative

	def getJobTitleOfRepresentative(self): #代表者役職
		return self.JobTitleOfRepresentative

	def getDescriptionOfBusiness(self): #事業内容
		return self.DescriptionOfBusiness

	def getContactInformationAbstract(self): #事務上の連絡先 [タイトル項目]
		return self.ContactInformationAbstract

	def getContactInformationAndPerson(self): #事務上の連絡先及び担当者名
		return self.ContactInformationAndPerson

	def getTelephoneNumber(self): #電話番号
		return self.TelephoneNumber

	def getPurposeOfHoldingAbstract(self): #保有目的 [タイトル項目]
		return self.PurposeOfHoldingAbstract

	def getPurposeOfHolding(self): #保有目的
		return self.PurposeOfHolding

	def getPurposeOfHoldingNA(self): #保有目的（該当なし）
		return self.PurposeOfHoldingNA

	def getBreakdownOfStocksEtcHeldBySaidFilerAbstract(self): #上記提出者の保有株券等の内訳 [タイトル項目]
		return self.BreakdownOfStocksEtcHeldBySaidFilerAbstract

	def getNumberOfStocksEtcHeldAbstract(self): #保有株券等の数 [タイトル項目]
		return self.NumberOfStocksEtcHeldAbstract

	def getArticle27233MainClauseAbstract(self): #法第27条の23第3項本文 [タイトル項目]
		return self.Article27233MainClauseAbstract

	def getStocksOrInvestmentSecuritiesEtcArticle27233MainClause(self): #株券又は投資証券等、法第27条の23第3項本文
		return self.StocksOrInvestmentSecuritiesEtcArticle27233MainClause

	def getSubscriptionRightsToSharesArticle27233MainClause(self): #新株予約権証券又は新投資口予約権証券等、法第27条の23第3項本文
		return self.SubscriptionRightsToSharesArticle27233MainClause

	def getConvertibleBondsArticle27233MainClause(self): #新株予約権付社債券、法第27条の23第3項本文
		return self.ConvertibleBondsArticle27233MainClause

	def getTargetSecurityCoveredWarrantsArticle27233MainClause(self): #対象有価証券カバードワラント、法第27条の23第3項本文
		return self.TargetSecurityCoveredWarrantsArticle27233MainClause

	def getStockDepositoryReceiptsArticle27233MainClause(self): #株券預託証券、法第27条の23第3項本文
		return self.StockDepositoryReceiptsArticle27233MainClause

	def getStockRelatedDepositoryReceiptsArticle27233MainClause(self): #株券関連預託証券、法第27条の23第3項本文
		return self.StockRelatedDepositoryReceiptsArticle27233MainClause

	def getStockTrustBeneficiaryRightsArticle27233MainClause(self): #株券信託受益証券、法第27条の23第3項本文
		return self.StockTrustBeneficiaryRightsArticle27233MainClause

	def getStockRelatedTrustBeneficiaryRightsArticle27233MainClause(self): #株券関連信託受益証券、法第27条の23第3項本文
		return self.StockRelatedTrustBeneficiaryRightsArticle27233MainClause

	def getTargetSecurityRedeemableBondsArticle27233MainClause(self): #対象有価証券償還社債、法第27条の23第3項本文
		return self.TargetSecurityRedeemableBondsArticle27233MainClause

	def getExchangeableBondsArticle27233MainClause(self): #他社株等転換株券、法第27条の23第3項本文
		return self.ExchangeableBondsArticle27233MainClause

	def getTotalArticle27233MainClause(self): #合計、法第27条の23第3項本文
		return self.TotalArticle27233MainClause

	def getArticle27233Item1Abstract(self): #法第27条の23第3項第１号 [タイトル項目]
		return self.Article27233Item1Abstract

	def getStocksOrInvestmentSecuritiesEtcArticle27233Item1(self): #株券又は投資証券等、法第27条の23第3項第１号
		return self.StocksOrInvestmentSecuritiesEtcArticle27233Item1

	def getTargetSecurityCoveredWarrantsArticle27233Item1(self): #対象有価証券カバードワラント、法第27条の23第3項第１号
		return self.TargetSecurityCoveredWarrantsArticle27233Item1

	def getStockDepositoryReceiptsArticle27233Item1(self): #株券預託証券、法第27条の23第3項第１号
		return self.StockDepositoryReceiptsArticle27233Item1

	def getStockRelatedDepositoryReceiptsArticle27233Item1(self): #株券関連預託証券、法第27条の23第3項第１号
		return self.StockRelatedDepositoryReceiptsArticle27233Item1

	def getStockTrustBeneficiaryRightsArticle27233Item1(self): #株券信託受益証券、法第27条の23第3項第１号
		return self.StockTrustBeneficiaryRightsArticle27233Item1

	def getStockRelatedTrustBeneficiaryRightsArticle27233Item1(self): #株券関連信託受益証券、法第27条の23第3項第１号
		return self.StockRelatedTrustBeneficiaryRightsArticle27233Item1

	def getTargetSecurityRedeemableBondsArticle27233Item1(self): #対象有価証券償還社債、法第27条の23第3項第１号
		return self.TargetSecurityRedeemableBondsArticle27233Item1

	def getExchangeableBondsArticle27233Item1(self): #他社株等転換株券、法第27条の23第3項第１号
		return self.ExchangeableBondsArticle27233Item1

	def getTotalArticle27233Item1(self): #合計、法第27条の23第3項第１号
		return self.TotalArticle27233Item1

	def getArticle27233Item2Abstract(self): #法第27条の23第3項第2号 [タイトル項目]
		return self.Article27233Item2Abstract

	def getStocksOrInvestmentSecuritiesEtcArticle27233Item2(self): #株券又は投資証券等、法第27条の23第3項第2号
		return self.StocksOrInvestmentSecuritiesEtcArticle27233Item2

	def getSubscriptionRightsToSharesArticle27233Item2(self): #新株予約権証券又は新投資口予約権証券等、法第27条の23第3項第2号
		return self.SubscriptionRightsToSharesArticle27233Item2

	def getConvertibleBondsArticle27233Item2(self): #新株予約権付社債券、法第27条の23第3項第2号
		return self.ConvertibleBondsArticle27233Item2

	def getTargetSecurityCoveredWarrantsArticle27233Item2(self): #対象有価証券カバードワラント、法第27条の23第3項第2号
		return self.TargetSecurityCoveredWarrantsArticle27233Item2

	def getStockDepositoryReceiptsArticle27233Item2(self): #株券預託証券、法第27条の23第3項第2号
		return self.StockDepositoryReceiptsArticle27233Item2

	def getStockRelatedDepositoryReceiptsArticle27233Item2(self): #株券関連預託証券、法第27条の23第3項第2号
		return self.StockRelatedDepositoryReceiptsArticle27233Item2

	def getStockTrustBeneficiaryRightsArticle27233Item2(self): #株券信託受益証券、法第27条の23第3項第2号
		return self.StockTrustBeneficiaryRightsArticle27233Item2

	def getStockRelatedTrustBeneficiaryRightsArticle27233Item2(self): #株券関連信託受益証券、法第27条の23第3項第2号
		return self.StockRelatedTrustBeneficiaryRightsArticle27233Item2

	def getTargetSecurityRedeemableBondsArticle27233Item2(self): #対象有価証券償還社債、法第27条の23第3項第2号
		return self.TargetSecurityRedeemableBondsArticle27233Item2

	def getExchangeableBondsArticle27233Item2(self): #他社株等転換株券、法第27条の23第3項第2号
		return self.ExchangeableBondsArticle27233Item2

	def getTotalArticle27233Item2(self): #合計、法第27条の23第3項第2号
		return self.TotalArticle27233Item2

	def getNumberOfStocksEtcToDeductAsSoldOnMarginTrading(self): #信用取引により譲渡したことにより控除する株券等の数
		return self.NumberOfStocksEtcToDeductAsSoldOnMarginTrading

	def getNumberOfStocksEtcToDeductAsRightsToDemandExistBetweenJointHolders(self): #共同保有者間で引渡請求権等の権利が存在するものとして控除する株券等の数
		return self.NumberOfStocksEtcToDeductAsRightsToDemandExistBetweenJointHolders

	def getTotalNumberOfStocksEtcHeld(self): #保有株券等の数（総数）
		return self.TotalNumberOfStocksEtcHeld

	def getNumberOfResidualStocksHeld(self): #保有潜在株券等の数
		return self.NumberOfResidualStocksHeld

	def getNotesNumberOfStocksEtcHeldTextBlock(self): #欄外注記、保有株券等の数 [テキストブロック]
		return self.NotesNumberOfStocksEtcHeldTextBlock

	def getHoldingRatioOfShareCertificatesEtcAbstract(self): #株券等保有割合 [タイトル項目]
		return self.HoldingRatioOfShareCertificatesEtcAbstract

	def getTotalNumberOfOutstandingStocksEtcAbstract(self): #発行済株式等総数 [タイトル項目]
		return self.TotalNumberOfOutstandingStocksEtcAbstract

	def getBaseDate(self): #基準日
		return self.BaseDate

	def getTotalNumberOfOutstandingStocksEtc(self): #発行済株式等総数
		return self.TotalNumberOfOutstandingStocksEtc

	def getHoldingRatioOfShareCertificatesEtc(self): #株券等保有割合
		return self.HoldingRatioOfShareCertificatesEtc

	def getHoldingRatioOfShareCertificatesEtcPerLastReport(self): #直前の報告書に記載された株券等保有割合
		return self.HoldingRatioOfShareCertificatesEtcPerLastReport

	def getNotesHoldingRatioOfShareCertificatesEtcTextBlock(self): #欄外注記、株券等保有割合 [テキストブロック]
		return self.NotesHoldingRatioOfShareCertificatesEtcTextBlock

	def getSignificantContractsRelatedToSaidStocksEtcSuchAsCollateralAgreementsAbstract(self): #当該株券等に関する担保契約等重要な契約 [タイトル項目]
		return self.SignificantContractsRelatedToSaidStocksEtcSuchAsCollateralAgreementsAbstract

	def getSignificantContractsRelatedToSaidStocksEtcSuchAsCollateralAgreementsTextBlock(self): #当該株券等に関する担保契約等重要な契約 [テキストブロック]
		return self.SignificantContractsRelatedToSaidStocksEtcSuchAsCollateralAgreementsTextBlock

	def getSignificantContractsRelatedToSaidStocksEtcSuchAsCollateralAgreementsNA(self): #当該株券等に関する担保契約等重要な契約（該当なし）
		return self.SignificantContractsRelatedToSaidStocksEtcSuchAsCollateralAgreementsNA

	def getInformationAboutJointHoldersHeading(self): #共同保有者に関する事項 [目次項目]
		return self.InformationAboutJointHoldersHeading

	def getInformationAboutJointHoldersHeading(self): #共同保有者に関する事項 [目次項目]
		return self.InformationAboutJointHoldersHeading

	def getInformationAboutJointHoldersTable(self): #共同保有者に関する事項 [表]
		return self.InformationAboutJointHoldersTable

	def getFilersLargeVolumeHoldersAndJointHoldersAxis(self): #提出者（大量保有者）・共同保有者 [軸]
		return self.FilersLargeVolumeHoldersAndJointHoldersAxis

	def getFilersLargeVolumeHoldersOrJointHoldersMember(self): #提出者（大量保有者）・共同保有者 [メンバー] ※ディメンションデフォルト
		return self.FilersLargeVolumeHoldersOrJointHoldersMember

	def getJointHoldersMember(self): #共同保有者 [メンバー]
		return self.JointHoldersMember

	def getInformationAboutJointHoldersLineItems(self): #共同保有者に関する事項 [表示項目]
		return self.InformationAboutJointHoldersLineItems

	def getJointHolderSerialNumberAbstract(self): #共同保有者／連番 [タイトル項目]
		return self.JointHolderSerialNumberAbstract

	def getOverviewOfJointHolderAbstract(self): #共同保有者の概要 [タイトル項目]
		return self.OverviewOfJointHolderAbstract

	def getJointHolderAbstract(self): #共同保有者 [タイトル項目]
		return self.JointHolderAbstract

	def getIndividualOrCorporation(self): #個人・法人の別
		return self.IndividualOrCorporation

	def getName(self): #氏名又は名称
		return self.Name

	def getResidentialAddressOrAddressOfRegisteredHeadquarter(self): #住所又は本店所在地
		return self.ResidentialAddressOrAddressOfRegisteredHeadquarter

	def getFormerName(self): #旧氏名又は名称
		return self.FormerName

	def getFormerResidentialAddressOrAddressOfRegisteredHeadquarter(self): #旧住所又は本店所在地
		return self.FormerResidentialAddressOrAddressOfRegisteredHeadquarter

	def getInformationAboutIndividualAbstract(self): #個人の場合 [タイトル項目]
		return self.InformationAboutIndividualAbstract

	def getInformationAboutIndividualNATextBlock(self): #個人の場合（該当なし） [テキストブロック]
		return self.InformationAboutIndividualNATextBlock

	def getDateOfBirth(self): #生年月日
		return self.DateOfBirth

	def getOccupation(self): #職業
		return self.Occupation

	def getNameOfEmployer(self): #勤務先名称
		return self.NameOfEmployer

	def getAddressOfEmployer(self): #勤務先住所
		return self.AddressOfEmployer

	def getInformationAboutCorporationAbstract(self): #法人の場合 [タイトル項目]
		return self.InformationAboutCorporationAbstract

	def getInformationAboutCorporationNATextBlock(self): #法人の場合（該当なし） [テキストブロック]
		return self.InformationAboutCorporationNATextBlock

	def getDateOfEstablishment(self): #設立年月日
		return self.DateOfEstablishment

	def getNameOfRepresentative(self): #代表者氏名
		return self.NameOfRepresentative

	def getJobTitleOfRepresentative(self): #代表者役職
		return self.JobTitleOfRepresentative

	def getDescriptionOfBusiness(self): #事業内容
		return self.DescriptionOfBusiness

	def getContactInformationAbstract(self): #事務上の連絡先 [タイトル項目]
		return self.ContactInformationAbstract

	def getContactInformationAndPerson(self): #事務上の連絡先及び担当者名
		return self.ContactInformationAndPerson

	def getTelephoneNumber(self): #電話番号
		return self.TelephoneNumber

	def getBreakdownOfStocksEtcHeldBySaidJointHolderAbstract(self): #上記共同保有者の保有株券等の内訳 [タイトル項目]
		return self.BreakdownOfStocksEtcHeldBySaidJointHolderAbstract

	def getNumberOfStocksEtcHeldAbstract(self): #保有株券等の数 [タイトル項目]
		return self.NumberOfStocksEtcHeldAbstract

	def getArticle27233MainClauseAbstract(self): #法第27条の23第3項本文 [タイトル項目]
		return self.Article27233MainClauseAbstract

	def getStocksOrInvestmentSecuritiesEtcArticle27233MainClause(self): #株券又は投資証券等、法第27条の23第3項本文
		return self.StocksOrInvestmentSecuritiesEtcArticle27233MainClause

	def getSubscriptionRightsToSharesArticle27233MainClause(self): #新株予約権証券又は新投資口予約権証券等、法第27条の23第3項本文
		return self.SubscriptionRightsToSharesArticle27233MainClause

	def getConvertibleBondsArticle27233MainClause(self): #新株予約権付社債券、法第27条の23第3項本文
		return self.ConvertibleBondsArticle27233MainClause

	def getTargetSecurityCoveredWarrantsArticle27233MainClause(self): #対象有価証券カバードワラント、法第27条の23第3項本文
		return self.TargetSecurityCoveredWarrantsArticle27233MainClause

	def getStockDepositoryReceiptsArticle27233MainClause(self): #株券預託証券、法第27条の23第3項本文
		return self.StockDepositoryReceiptsArticle27233MainClause

	def getStockRelatedDepositoryReceiptsArticle27233MainClause(self): #株券関連預託証券、法第27条の23第3項本文
		return self.StockRelatedDepositoryReceiptsArticle27233MainClause

	def getStockTrustBeneficiaryRightsArticle27233MainClause(self): #株券信託受益証券、法第27条の23第3項本文
		return self.StockTrustBeneficiaryRightsArticle27233MainClause

	def getStockRelatedTrustBeneficiaryRightsArticle27233MainClause(self): #株券関連信託受益証券、法第27条の23第3項本文
		return self.StockRelatedTrustBeneficiaryRightsArticle27233MainClause

	def getTargetSecurityRedeemableBondsArticle27233MainClause(self): #対象有価証券償還社債、法第27条の23第3項本文
		return self.TargetSecurityRedeemableBondsArticle27233MainClause

	def getExchangeableBondsArticle27233MainClause(self): #他社株等転換株券、法第27条の23第3項本文
		return self.ExchangeableBondsArticle27233MainClause

	def getTotalArticle27233MainClause(self): #合計、法第27条の23第3項本文
		return self.TotalArticle27233MainClause

	def getArticle27233Item1Abstract(self): #法第27条の23第3項第１号 [タイトル項目]
		return self.Article27233Item1Abstract

	def getStocksOrInvestmentSecuritiesEtcArticle27233Item1(self): #株券又は投資証券等、法第27条の23第3項第１号
		return self.StocksOrInvestmentSecuritiesEtcArticle27233Item1

	def getTargetSecurityCoveredWarrantsArticle27233Item1(self): #対象有価証券カバードワラント、法第27条の23第3項第１号
		return self.TargetSecurityCoveredWarrantsArticle27233Item1

	def getStockDepositoryReceiptsArticle27233Item1(self): #株券預託証券、法第27条の23第3項第１号
		return self.StockDepositoryReceiptsArticle27233Item1

	def getStockRelatedDepositoryReceiptsArticle27233Item1(self): #株券関連預託証券、法第27条の23第3項第１号
		return self.StockRelatedDepositoryReceiptsArticle27233Item1

	def getStockTrustBeneficiaryRightsArticle27233Item1(self): #株券信託受益証券、法第27条の23第3項第１号
		return self.StockTrustBeneficiaryRightsArticle27233Item1

	def getStockRelatedTrustBeneficiaryRightsArticle27233Item1(self): #株券関連信託受益証券、法第27条の23第3項第１号
		return self.StockRelatedTrustBeneficiaryRightsArticle27233Item1

	def getTargetSecurityRedeemableBondsArticle27233Item1(self): #対象有価証券償還社債、法第27条の23第3項第１号
		return self.TargetSecurityRedeemableBondsArticle27233Item1

	def getExchangeableBondsArticle27233Item1(self): #他社株等転換株券、法第27条の23第3項第１号
		return self.ExchangeableBondsArticle27233Item1

	def getTotalArticle27233Item1(self): #合計、法第27条の23第3項第１号
		return self.TotalArticle27233Item1

	def getArticle27233Item2Abstract(self): #法第27条の23第3項第2号 [タイトル項目]
		return self.Article27233Item2Abstract

	def getStocksOrInvestmentSecuritiesEtcArticle27233Item2(self): #株券又は投資証券等、法第27条の23第3項第2号
		return self.StocksOrInvestmentSecuritiesEtcArticle27233Item2

	def getSubscriptionRightsToSharesArticle27233Item2(self): #新株予約権証券又は新投資口予約権証券等、法第27条の23第3項第2号
		return self.SubscriptionRightsToSharesArticle27233Item2

	def getConvertibleBondsArticle27233Item2(self): #新株予約権付社債券、法第27条の23第3項第2号
		return self.ConvertibleBondsArticle27233Item2

	def getTargetSecurityCoveredWarrantsArticle27233Item2(self): #対象有価証券カバードワラント、法第27条の23第3項第2号
		return self.TargetSecurityCoveredWarrantsArticle27233Item2

	def getStockDepositoryReceiptsArticle27233Item2(self): #株券預託証券、法第27条の23第3項第2号
		return self.StockDepositoryReceiptsArticle27233Item2

	def getStockRelatedDepositoryReceiptsArticle27233Item2(self): #株券関連預託証券、法第27条の23第3項第2号
		return self.StockRelatedDepositoryReceiptsArticle27233Item2

	def getStockTrustBeneficiaryRightsArticle27233Item2(self): #株券信託受益証券、法第27条の23第3項第2号
		return self.StockTrustBeneficiaryRightsArticle27233Item2

	def getStockRelatedTrustBeneficiaryRightsArticle27233Item2(self): #株券関連信託受益証券、法第27条の23第3項第2号
		return self.StockRelatedTrustBeneficiaryRightsArticle27233Item2

	def getTargetSecurityRedeemableBondsArticle27233Item2(self): #対象有価証券償還社債、法第27条の23第3項第2号
		return self.TargetSecurityRedeemableBondsArticle27233Item2

	def getExchangeableBondsArticle27233Item2(self): #他社株等転換株券、法第27条の23第3項第2号
		return self.ExchangeableBondsArticle27233Item2

	def getTotalArticle27233Item2(self): #合計、法第27条の23第3項第2号
		return self.TotalArticle27233Item2

	def getNumberOfStocksEtcToDeductAsSoldOnMarginTrading(self): #信用取引により譲渡したことにより控除する株券等の数
		return self.NumberOfStocksEtcToDeductAsSoldOnMarginTrading

	def getNumberOfStocksEtcToDeductAsRightsToDemandExistBetweenJointHolders(self): #共同保有者間で引渡請求権等の権利が存在するものとして控除する株券等の数
		return self.NumberOfStocksEtcToDeductAsRightsToDemandExistBetweenJointHolders

	def getTotalNumberOfStocksEtcHeld(self): #保有株券等の数（総数）
		return self.TotalNumberOfStocksEtcHeld

	def getNumberOfResidualStocksHeld(self): #保有潜在株券等の数
		return self.NumberOfResidualStocksHeld

	def getNotesNumberOfStocksEtcHeldTextBlock(self): #欄外注記、保有株券等の数 [テキストブロック]
		return self.NotesNumberOfStocksEtcHeldTextBlock

	def getHoldingRatioOfShareCertificatesEtcAbstract(self): #株券等保有割合 [タイトル項目]
		return self.HoldingRatioOfShareCertificatesEtcAbstract

	def getTotalNumberOfOutstandingStocksEtcAbstract(self): #発行済株式等総数 [タイトル項目]
		return self.TotalNumberOfOutstandingStocksEtcAbstract

	def getBaseDate(self): #基準日
		return self.BaseDate

	def getTotalNumberOfOutstandingStocksEtc(self): #発行済株式等総数
		return self.TotalNumberOfOutstandingStocksEtc

	def getHoldingRatioOfShareCertificatesEtc(self): #株券等保有割合
		return self.HoldingRatioOfShareCertificatesEtc

	def getHoldingRatioOfShareCertificatesEtcPerLastReport(self): #直前の報告書に記載された株券等保有割合
		return self.HoldingRatioOfShareCertificatesEtcPerLastReport

	def getNotesHoldingRatioOfShareCertificatesEtcTextBlock(self): #欄外注記、株券等保有割合 [テキストブロック]
		return self.NotesHoldingRatioOfShareCertificatesEtcTextBlock

	def getInformationAboutJointHoldersNA(self): #共同保有者に関する事項（該当なし）
		return self.InformationAboutJointHoldersNA

	def getSummaryOfFilerAndJointHoldersHeading(self): #提出者及び共同保有者に関する総括表 [目次項目]
		return self.SummaryOfFilerAndJointHoldersHeading

	def getFilersAndJointHoldersHeading(self): #提出者及び共同保有者 [目次項目]
		return self.FilersAndJointHoldersHeading

	def getFilersAndJointHoldersHeading(self): #提出者及び共同保有者 [目次項目]
		return self.FilersAndJointHoldersHeading

	def getFilersAndJointHoldersTable(self): #提出者及び共同保有者 [表]
		return self.FilersAndJointHoldersTable

	def getFilersLargeVolumeHoldersAndJointHoldersAxis(self): #提出者（大量保有者）・共同保有者 [軸]
		return self.FilersLargeVolumeHoldersAndJointHoldersAxis

	def getFilersLargeVolumeHoldersOrJointHoldersMember(self): #提出者（大量保有者）・共同保有者 [メンバー] ※ディメンションデフォルト
		return self.FilersLargeVolumeHoldersOrJointHoldersMember

	def getFilersAndJointHoldersLineItems(self): #提出者及び共同保有者 [表示項目]
		return self.FilersAndJointHoldersLineItems

	def getName(self): #氏名又は名称
		return self.Name

	def getBreakdownOfStocksEtcHeldBySaidFilerAndJointHoldersHeading(self): #上記提出者及び共同保有者の保有株券等の内訳 [目次項目]
		return self.BreakdownOfStocksEtcHeldBySaidFilerAndJointHoldersHeading

	def getNumberOfStocksEtcHeldSummaryHeading(self): #保有株券等の数、総括表 [目次項目]
		return self.NumberOfStocksEtcHeldSummaryHeading

	def getNumberOfStocksEtcHeldSummaryHeading(self): #保有株券等の数、総括表 [目次項目]
		return self.NumberOfStocksEtcHeldSummaryHeading

	def getArticle27233MainClauseAbstract(self): #法第27条の23第3項本文 [タイトル項目]
		return self.Article27233MainClauseAbstract

	def getStocksOrInvestmentSecuritiesEtcArticle27233MainClause(self): #株券又は投資証券等、法第27条の23第3項本文
		return self.StocksOrInvestmentSecuritiesEtcArticle27233MainClause

	def getSubscriptionRightsToSharesArticle27233MainClause(self): #新株予約権証券又は新投資口予約権証券等、法第27条の23第3項本文
		return self.SubscriptionRightsToSharesArticle27233MainClause

	def getConvertibleBondsArticle27233MainClause(self): #新株予約権付社債券、法第27条の23第3項本文
		return self.ConvertibleBondsArticle27233MainClause

	def getTargetSecurityCoveredWarrantsArticle27233MainClause(self): #対象有価証券カバードワラント、法第27条の23第3項本文
		return self.TargetSecurityCoveredWarrantsArticle27233MainClause

	def getStockDepositoryReceiptsArticle27233MainClause(self): #株券預託証券、法第27条の23第3項本文
		return self.StockDepositoryReceiptsArticle27233MainClause

	def getStockRelatedDepositoryReceiptsArticle27233MainClause(self): #株券関連預託証券、法第27条の23第3項本文
		return self.StockRelatedDepositoryReceiptsArticle27233MainClause

	def getStockTrustBeneficiaryRightsArticle27233MainClause(self): #株券信託受益証券、法第27条の23第3項本文
		return self.StockTrustBeneficiaryRightsArticle27233MainClause

	def getStockRelatedTrustBeneficiaryRightsArticle27233MainClause(self): #株券関連信託受益証券、法第27条の23第3項本文
		return self.StockRelatedTrustBeneficiaryRightsArticle27233MainClause

	def getTargetSecurityRedeemableBondsArticle27233MainClause(self): #対象有価証券償還社債、法第27条の23第3項本文
		return self.TargetSecurityRedeemableBondsArticle27233MainClause

	def getExchangeableBondsArticle27233MainClause(self): #他社株等転換株券、法第27条の23第3項本文
		return self.ExchangeableBondsArticle27233MainClause

	def getTotalArticle27233MainClause(self): #合計、法第27条の23第3項本文
		return self.TotalArticle27233MainClause

	def getArticle27233Item1Abstract(self): #法第27条の23第3項第１号 [タイトル項目]
		return self.Article27233Item1Abstract

	def getStocksOrInvestmentSecuritiesEtcArticle27233Item1(self): #株券又は投資証券等、法第27条の23第3項第１号
		return self.StocksOrInvestmentSecuritiesEtcArticle27233Item1

	def getTargetSecurityCoveredWarrantsArticle27233Item1(self): #対象有価証券カバードワラント、法第27条の23第3項第１号
		return self.TargetSecurityCoveredWarrantsArticle27233Item1

	def getStockDepositoryReceiptsArticle27233Item1(self): #株券預託証券、法第27条の23第3項第１号
		return self.StockDepositoryReceiptsArticle27233Item1

	def getStockRelatedDepositoryReceiptsArticle27233Item1(self): #株券関連預託証券、法第27条の23第3項第１号
		return self.StockRelatedDepositoryReceiptsArticle27233Item1

	def getStockTrustBeneficiaryRightsArticle27233Item1(self): #株券信託受益証券、法第27条の23第3項第１号
		return self.StockTrustBeneficiaryRightsArticle27233Item1

	def getStockRelatedTrustBeneficiaryRightsArticle27233Item1(self): #株券関連信託受益証券、法第27条の23第3項第１号
		return self.StockRelatedTrustBeneficiaryRightsArticle27233Item1

	def getTargetSecurityRedeemableBondsArticle27233Item1(self): #対象有価証券償還社債、法第27条の23第3項第１号
		return self.TargetSecurityRedeemableBondsArticle27233Item1

	def getExchangeableBondsArticle27233Item1(self): #他社株等転換株券、法第27条の23第3項第１号
		return self.ExchangeableBondsArticle27233Item1

	def getTotalArticle27233Item1(self): #合計、法第27条の23第3項第１号
		return self.TotalArticle27233Item1

	def getArticle27233Item2Abstract(self): #法第27条の23第3項第2号 [タイトル項目]
		return self.Article27233Item2Abstract

	def getStocksOrInvestmentSecuritiesEtcArticle27233Item2(self): #株券又は投資証券等、法第27条の23第3項第2号
		return self.StocksOrInvestmentSecuritiesEtcArticle27233Item2

	def getSubscriptionRightsToSharesArticle27233Item2(self): #新株予約権証券又は新投資口予約権証券等、法第27条の23第3項第2号
		return self.SubscriptionRightsToSharesArticle27233Item2

	def getConvertibleBondsArticle27233Item2(self): #新株予約権付社債券、法第27条の23第3項第2号
		return self.ConvertibleBondsArticle27233Item2

	def getTargetSecurityCoveredWarrantsArticle27233Item2(self): #対象有価証券カバードワラント、法第27条の23第3項第2号
		return self.TargetSecurityCoveredWarrantsArticle27233Item2

	def getStockDepositoryReceiptsArticle27233Item2(self): #株券預託証券、法第27条の23第3項第2号
		return self.StockDepositoryReceiptsArticle27233Item2

	def getStockRelatedDepositoryReceiptsArticle27233Item2(self): #株券関連預託証券、法第27条の23第3項第2号
		return self.StockRelatedDepositoryReceiptsArticle27233Item2

	def getStockTrustBeneficiaryRightsArticle27233Item2(self): #株券信託受益証券、法第27条の23第3項第2号
		return self.StockTrustBeneficiaryRightsArticle27233Item2

	def getStockRelatedTrustBeneficiaryRightsArticle27233Item2(self): #株券関連信託受益証券、法第27条の23第3項第2号
		return self.StockRelatedTrustBeneficiaryRightsArticle27233Item2

	def getTargetSecurityRedeemableBondsArticle27233Item2(self): #対象有価証券償還社債、法第27条の23第3項第2号
		return self.TargetSecurityRedeemableBondsArticle27233Item2

	def getExchangeableBondsArticle27233Item2(self): #他社株等転換株券、法第27条の23第3項第2号
		return self.ExchangeableBondsArticle27233Item2

	def getTotalArticle27233Item2(self): #合計、法第27条の23第3項第2号
		return self.TotalArticle27233Item2

	def getNumberOfStocksEtcToDeductAsSoldOnMarginTrading(self): #信用取引により譲渡したことにより控除する株券等の数
		return self.NumberOfStocksEtcToDeductAsSoldOnMarginTrading

	def getNumberOfStocksEtcToDeductAsRightsToDemandExistBetweenJointHolders(self): #共同保有者間で引渡請求権等の権利が存在するものとして控除する株券等の数
		return self.NumberOfStocksEtcToDeductAsRightsToDemandExistBetweenJointHolders

	def getTotalNumberOfStocksEtcHeld(self): #保有株券等の数（総数）
		return self.TotalNumberOfStocksEtcHeld

	def getNumberOfResidualStocksHeld(self): #保有潜在株券等の数
		return self.NumberOfResidualStocksHeld

	def getNotesNumberOfStocksEtcHeldTextBlock(self): #欄外注記、保有株券等の数 [テキストブロック]
		return self.NotesNumberOfStocksEtcHeldTextBlock

	def getHoldingRatioOfShareCertificatesEtcSummaryHeading(self): #株券等保有割合、総括表 [目次項目]
		return self.HoldingRatioOfShareCertificatesEtcSummaryHeading

	def getHoldingRatioOfShareCertificatesEtcSummaryHeading(self): #株券等保有割合、総括表 [目次項目]
		return self.HoldingRatioOfShareCertificatesEtcSummaryHeading

	def getTotalNumberOfOutstandingStocksEtcAbstract(self): #発行済株式等総数 [タイトル項目]
		return self.TotalNumberOfOutstandingStocksEtcAbstract

	def getBaseDate(self): #基準日
		return self.BaseDate

	def getTotalNumberOfOutstandingStocksEtc(self): #発行済株式等総数
		return self.TotalNumberOfOutstandingStocksEtc

	def getHoldingRatioOfShareCertificatesEtc(self): #株券等保有割合
		return self.HoldingRatioOfShareCertificatesEtc

	def getHoldingRatioOfShareCertificatesEtcPerLastReport(self): #直前の報告書に記載された株券等保有割合
		return self.HoldingRatioOfShareCertificatesEtcPerLastReport

	def getNotesHoldingRatioOfShareCertificatesEtcTextBlock(self): #欄外注記、株券等保有割合 [テキストブロック]
		return self.NotesHoldingRatioOfShareCertificatesEtcTextBlock

	def getHoldingRatioOfShareCertificatesEtcHeldByJointHoldingHeading(self): #共同保有における株券等保有割合の内訳 [目次項目]
		return self.HoldingRatioOfShareCertificatesEtcHeldByJointHoldingHeading

	def getHoldingRatioOfShareCertificatesEtcHeldByJointHoldingHeading(self): #共同保有における株券等保有割合の内訳 [目次項目]
		return self.HoldingRatioOfShareCertificatesEtcHeldByJointHoldingHeading

	def getHoldingRatioOfShareCertificatesEtcHeldByJointHoldingTable(self): #共同保有における株券等保有割合の内訳 [表]
		return self.HoldingRatioOfShareCertificatesEtcHeldByJointHoldingTable

	def getFilersLargeVolumeHoldersAndJointHoldersAxis(self): #提出者（大量保有者）・共同保有者 [軸]
		return self.FilersLargeVolumeHoldersAndJointHoldersAxis

	def getFilersLargeVolumeHoldersOrJointHoldersMember(self): #提出者（大量保有者）・共同保有者 [メンバー] ※ディメンションデフォルト
		return self.FilersLargeVolumeHoldersOrJointHoldersMember

	def getHoldingRatioOfShareCertificatesEtcHeldByJointHoldingLineItems(self): #共同保有における株券等保有割合の内訳 [表示項目]
		return self.HoldingRatioOfShareCertificatesEtcHeldByJointHoldingLineItems

	def getName(self): #氏名又は名称
		return self.Name

	def getTotalNumberOfStocksEtcHeld(self): #保有株券等の数（総数）
		return self.TotalNumberOfStocksEtcHeld

	def getHoldingRatioOfShareCertificatesEtc(self): #株券等保有割合
		return self.HoldingRatioOfShareCertificatesEtc
