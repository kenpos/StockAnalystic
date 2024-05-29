from arelle import ModelManager
from arelle import Cntlr

class jpcrp030000:#企業内容等の開示に関する内閣府令 第三号様式 有価証券報告書
	CabinetOfficeOrdinanceOnDisclosureOfCorporateInformationEtcFormNo3AnnualSecuritiesReportHeading = '' #企業内容等の開示に関する内閣府令 第三号様式 有価証券報告書 [目次項目]
	CoverPageHeading = '' #表紙 [目次項目]
	CoverPageHeading = '' #表紙 [目次項目]
	DocumentTitleCoverPage = '' #提出書類、表紙
	ClauseOfStipulationCoverPage = '' #根拠条文、表紙
	PlaceOfFilingCoverPage = '' #提出先、表紙
	FilingDateCoverPage = '' #提出日、表紙
	FiscalYearCoverPage = '' #事業年度、表紙
	CompanyNameCoverPage = '' #会社名、表紙
	CompanyNameInEnglishCoverPage = '' #英訳名、表紙
	TitleAndNameOfRepresentativeCoverPage = '' #代表者の役職氏名、表紙
	AddressOfRegisteredHeadquarterCoverPage = '' #本店の所在の場所、表紙
	TelephoneNumberAddressOfRegisteredHeadquarterCoverPage = '' #電話番号、本店の所在の場所、表紙
	NameOfContactPersonAddressOfRegisteredHeadquarterCoverPage = '' #事務連絡者氏名、本店の所在の場所、表紙
	NearestPlaceOfContactCoverPage = '' #最寄りの連絡場所、表紙
	TelephoneNumberNearestPlaceOfContactCoverPage = '' #電話番号、最寄りの連絡場所、表紙
	NameOfContactPersonNearestPlaceOfContactCoverPage = '' #事務連絡者氏名、最寄りの連絡場所、表紙
	PlaceForPublicInspectionCoverPageTextBlock = '' #縦覧に供する場所、表紙 [テキストブロック]
	FootnotesCoverPageTextBlock = '' #脚注、表紙 [テキストブロック]
	CompanyInformationHeading = '' #企業情報 [目次項目]
	OverviewOfCompanyHeading = '' #企業の概況 [目次項目]
	SummaryOfBusinessResultsHeading = '' #主要な経営指標等の推移 [目次項目]
	BusinessResultsOfGroupHeading = '' #連結経営指標等 [目次項目]
	BusinessResultsOfGroupTextBlock = '' #連結経営指標等 [テキストブロック]
	BusinessResultsOfGroupHeading = '' #連結経営指標等 [目次項目]
	BusinessResultsOfGroupTable = '' #連結経営指標等 [表]
	ConsolidatedOrNonConsolidatedAxis = '' #連結個別 [軸]
	ConsolidatedMember = '' #連結 [メンバー] ※ディメンションデフォルト
	BusinessResultsOfGroupLineItems = '' #連結経営指標等 [表示項目]
	NetSalesSummaryOfBusinessResults = '' #売上高、経営指標等
	RevenueKeyFinancialData = '' #売上収益、経営指標等
	OperatingRevenue1SummaryOfBusinessResults = '' #営業収益、経営指標等
	OperatingRevenue2SummaryOfBusinessResults = '' #営業収入、経営指標等
	GrossOperatingRevenueSummaryOfBusinessResults = '' #営業総収入、経営指標等
	OrdinaryIncomeSummaryOfBusinessResults = '' #経常収益、経営指標等
	NetPremiumsWrittenSummaryOfBusinessResultsINS = '' #正味収入保険料、経営指標等、保険業
	OrdinaryIncomeLossSummaryOfBusinessResults = '' #経常利益又は経常損失（△）、経営指標等
	ProfitLossAttributableToOwnersOfParentSummaryOfBusinessResults = '' #親会社株主に帰属する当期純利益又は親会社株主に帰属する当期純損失（△）、経営指標等
	ComprehensiveIncomeSummaryOfBusinessResults = '' #包括利益、経営指標等
	NetAssetsSummaryOfBusinessResults = '' #純資産額、経営指標等
	TotalAssetsSummaryOfBusinessResults = '' #総資産額、経営指標等
	NetAssetsPerShareSummaryOfBusinessResults = '' #１株当たり純資産額、経営指標等
	BasicEarningsLossPerShareSummaryOfBusinessResults = '' #１株当たり当期純利益又は当期純損失（△）、経営指標等
	DilutedEarningsPerShareSummaryOfBusinessResults = '' #潜在株式調整後１株当たり当期純利益、経営指標等
	EquityToAssetRatioSummaryOfBusinessResults = '' #自己資本比率、経営指標等
	CapitalAdequacyRatioInternationalStandardSummaryOfBusinessResults = '' #自己資本比率（国際統一基準）、経営指標等
	CapitalAdequacyRatioDomesticStandardSummaryOfBusinessResults = '' #自己資本比率（国内基準）、経営指標等
	CapitalAdequacyRatioBISStandardSummaryOfBusinessResults = '' #自己資本比率（第一基準）、経営指標等
	CapitalAdequacyRatioDomesticStandard2SummaryOfBusinessResults = '' #自己資本比率（第二基準）、経営指標等
	RateOfReturnOnEquitySummaryOfBusinessResults = '' #自己資本利益率、経営指標等
	PriceEarningsRatioSummaryOfBusinessResults = '' #株価収益率、経営指標等
	NetCashProvidedByUsedInOperatingActivitiesSummaryOfBusinessResults = '' #営業活動によるキャッシュ・フロー、経営指標等
	NetCashProvidedByUsedInInvestingActivitiesSummaryOfBusinessResults = '' #投資活動によるキャッシュ・フロー、経営指標等
	NetCashProvidedByUsedInFinancingActivitiesSummaryOfBusinessResults = '' #財務活動によるキャッシュ・フロー、経営指標等
	CashAndCashEquivalentsSummaryOfBusinessResults = '' #現金及び現金同等物の残高、経営指標等
	NumberOfEmployees = '' #従業員数
	AverageNumberOfTemporaryWorkers = '' #平均臨時雇用人員
	RevenueIFRSSummaryOfBusinessResults = '' #売上収益（IFRS）、経営指標等
	ProfitLossBeforeTaxIFRSSummaryOfBusinessResults = '' #税引前利益又は税引前損失（△）（IFRS）、経営指標等
	ProfitLossFromContinuingOperationsIFRSSummaryOfBusinessResults = '' #継続事業からの当期利益又は当期損失（△）（IFRS）、経営指標等
	ProfitLossIFRSSummaryOfBusinessResults = '' #当期利益又は当期損失（△）（IFRS）、経営指標等
	ProfitLossAttributableToOwnersOfParentIFRSSummaryOfBusinessResults = '' #当期利益又は当期損失（△）：親会社の所有者に帰属（IFRS）、経営指標等
	ComprehensiveIncomeIFRSSummaryOfBusinessResults = '' #当期包括利益（IFRS）、経営指標等
	ComprehensiveIncomeAttributableToOwnersOfParentIFRSSummaryOfBusinessResults = '' #当期包括利益：親会社の所有者に帰属（IFRS）、経営指標等
	EquityAttributableToOwnersOfParentIFRSSummaryOfBusinessResults = '' #親会社の所有者に帰属する持分（IFRS）、経営指標等
	TotalAssetsIFRSSummaryOfBusinessResults = '' #総資産額（IFRS）、経営指標等
	EquityToAssetRatioIFRSSummaryOfBusinessResults = '' #１株当たり親会社所有者帰属持分（IFRS）、経営指標等
	BasicEarningsLossPerShareIFRSSummaryOfBusinessResults = '' #基本的１株当たり利益又は損失（△）（IFRS）、経営指標等
	DilutedEarningsLossPerShareIFRSSummaryOfBusinessResults = '' #希薄化後１株当たり利益又は損失（△）（IFRS）、経営指標等
	RatioOfOwnersEquityToGrossAssetsIFRSSummaryOfBusinessResults = '' #親会社所有者帰属持分比率（IFRS）、経営指標等
	RateOfReturnOnEquityIFRSSummaryOfBusinessResults = '' #親会社所有者帰属持分利益率（IFRS）、経営指標等
	PriceEarningsRatioIFRSSummaryOfBusinessResults = '' #株価収益率（IFRS）、経営指標等
	CashFlowsFromUsedInOperatingActivitiesIFRSSummaryOfBusinessResults = '' #営業活動によるキャッシュ・フロー（IFRS）、経営指標等
	CashFlowsFromUsedInInvestingActivitiesIFRSSummaryOfBusinessResults = '' #投資活動によるキャッシュ・フロー（IFRS）、経営指標等
	CashFlowsFromUsedInFinancingActivitiesIFRSSummaryOfBusinessResults = '' #財務活動によるキャッシュ・フロー（IFRS）、経営指標等
	CashAndCashEquivalentsIFRSSummaryOfBusinessResults = '' #現金及び現金同等物（IFRS）、経営指標等
	RevenueJMISSummaryOfBusinessResults = '' #売上収益（JMIS）、経営指標等
	ProfitLossBeforeTaxJMISSummaryOfBusinessResults = '' #税引前利益又は税引前損失（△）（JMIS）、経営指標等
	ProfitLossFromContinuingOperationsJMISSummaryOfBusinessResults = '' #継続事業からの当期利益又は当期損失（△）（JMIS）、経営指標等
	ProfitLossJMISSummaryOfBusinessResults = '' #当期利益又は当期損失（△）（JMIS）、経営指標等
	ProfitLossAttributableToOwnersOfParentJMISSummaryOfBusinessResults = '' #当期利益又は当期損失（△）：親会社の所有者に帰属（JMIS）、経営指標等
	ComprehensiveIncomeJMISSummaryOfBusinessResults = '' #当期包括利益（JMIS）、経営指標等
	ComprehensiveIncomeAttributableToOwnersOfParentJMISSummaryOfBusinessResults = '' #当期包括利益：親会社の所有者に帰属（JMIS）、経営指標等
	EquityAttributableToOwnersOfParentJMISSummaryOfBusinessResults = '' #親会社の所有者に帰属する持分（JMIS）、経営指標等
	TotalAssetsJMISSummaryOfBusinessResults = '' #総資産額（JMIS）、経営指標等
	EquityToAssetRatioJMISSummaryOfBusinessResults = '' #１株当たり親会社所有者帰属持分（JMIS）、経営指標等
	BasicEarningsLossPerShareJMISSummaryOfBusinessResults = '' #基本的１株当たり利益又は損失（△）（JMIS）、経営指標等
	DilutedEarningsLossPerShareJMISSummaryOfBusinessResults = '' #希薄化後１株当たり利益又は損失（△）（JMIS）、経営指標等
	RatioOfOwnersEquityToGrossAssetsJMISSummaryOfBusinessResults = '' #親会社所有者帰属持分比率（JMIS）、経営指標等
	RateOfReturnOnEquityJMISSummaryOfBusinessResults = '' #親会社所有者帰属持分利益率（JMIS）、経営指標等
	PriceEarningsRatioJMISSummaryOfBusinessResults = '' #株価収益率（JMIS）、経営指標等
	CashFlowsFromUsedInOperatingActivitiesJMISSummaryOfBusinessResults = '' #営業活動によるキャッシュ・フロー（JMIS）、経営指標等
	CashFlowsFromUsedInInvestingActivitiesJMISSummaryOfBusinessResults = '' #投資活動によるキャッシュ・フロー（JMIS）、経営指標等
	CashFlowsFromUsedInFinancingActivitiesJMISSummaryOfBusinessResults = '' #財務活動によるキャッシュ・フロー（JMIS）、経営指標等
	CashAndCashEquivalentsJMISSummaryOfBusinessResults = '' #現金及び現金同等物（JMIS）、経営指標等
	RevenuesUSGAAPSummaryOfBusinessResults = '' #売上高（US GAAP）、経営指標等
	OperatingIncomeLossUSGAAPSummaryOfBusinessResults = '' #営業利益又は営業損失（△）（US GAAP）、経営指標等
	ProfitLossBeforeTaxUSGAAPSummaryOfBusinessResults = '' #税引前利益又は税引前損失（△）（US GAAP）、経営指標等
	NetIncomeLossAttributableToOwnersOfParentUSGAAPSummaryOfBusinessResults = '' #当社株主に帰属する純利益又は純損失（△）（US GAAP）、経営指標等
	ComprehensiveIncomeUSGAAPSummaryOfBusinessResults = '' #包括利益（US GAAP）、経営指標等
	ComprehensiveIncomeAttributableToOwnersOfParentUSGAAPSummaryOfBusinessResults = '' #当社株主に帰属する包括利益（US GAAP）、経営指標等
	EquityAttributableToOwnersOfParentUSGAAPSummaryOfBusinessResults = '' #株主資本（US GAAP）、経営指標等
	EquityIncludingPortionAttributableToNonControllingInterestUSGAAPSummaryOfBusinessResults = '' #純資産額（US GAAP）、経営指標等
	TotalAssetsUSGAAPSummaryOfBusinessResults = '' #総資産額（US GAAP）、経営指標等
	EquityAttributableToOwnersOfParentPerShareUSGAAPSummaryOfBusinessResults = '' #１株当たり株主資本（US GAAP）、経営指標等
	BasicEarningsLossPerShareUSGAAPSummaryOfBusinessResults = '' #基本的１株当たり当社株主に帰属する利益又は損失（△）（US GAAP）、経営指標等
	DilutedEarningsLossPerShareUSGAAPSummaryOfBusinessResults = '' #希薄化後１株当たり当社株主に帰属する利益又は損失（△）（US GAAP）、経営指標等
	EquityToAssetRatioUSGAAPSummaryOfBusinessResults = '' #自己資本比率（US GAAP）、経営指標等
	PriceEarningsRatioUSGAAPSummaryOfBusinessResults = '' #株価収益率（US GAAP）、経営指標等
	RateOfReturnOnEquityUSGAAPSummaryOfBusinessResults = '' #株主資本利益率（US GAAP）、経営指標等
	CashFlowsFromUsedInOperatingActivitiesUSGAAPSummaryOfBusinessResults = '' #営業活動によるキャッシュ・フロー（US GAAP）、経営指標等
	CashFlowsFromUsedInInvestingActivitiesUSGAAPSummaryOfBusinessResults = '' #投資活動によるキャッシュ・フロー（US GAAP）、経営指標等
	CashFlowsFromUsedInFinancingActivitiesUSGAAPSummaryOfBusinessResults = '' #財務活動によるキャッシュ・フロー（US GAAP）、経営指標等
	CashAndCashEquivalentsUSGAAPSummaryOfBusinessResults = '' #現金及び現金同等物（US GAAP）、経営指標等
	BusinessResultsOfReportingCompanyHeading = '' #提出会社の経営指標等 [目次項目]
	BusinessResultsOfReportingCompanyTextBlock = '' #提出会社の経営指標等 [テキストブロック]
	BusinessResultsOfReportingCompanyHeading = '' #提出会社の経営指標等 [目次項目]
	BusinessResultsOfReportingCompanyTable = '' #提出会社の経営指標等 [表]
	ConsolidatedOrNonConsolidatedAxis = '' #連結個別 [軸]
	NonConsolidatedMember = '' #非連結又は個別 [メンバー]
	BusinessResultsOfReportingCompanyLineItems = '' #提出会社の経営指標等 [表示項目]
	NetSalesSummaryOfBusinessResults = '' #売上高、経営指標等
	RevenueKeyFinancialData = '' #売上収益、経営指標等
	OperatingRevenue1SummaryOfBusinessResults = '' #営業収益、経営指標等
	OperatingRevenue2SummaryOfBusinessResults = '' #営業収入、経営指標等
	GrossOperatingRevenueSummaryOfBusinessResults = '' #営業総収入、経営指標等
	OrdinaryIncomeSummaryOfBusinessResults = '' #経常収益、経営指標等
	NetPremiumsWrittenSummaryOfBusinessResultsINS = '' #正味収入保険料、経営指標等、保険業
	OrdinaryIncomeLossSummaryOfBusinessResults = '' #経常利益又は経常損失（△）、経営指標等
	NetIncomeLossSummaryOfBusinessResults = '' #当期純利益又は当期純損失（△）、経営指標等
	NetLossRatioSummaryOfBusinessResultsINS = '' #正味損害率、経営指標等、保険業
	NetOperatingExpenseRatioSummaryOfBusinessResultsINS = '' #正味事業費率、経営指標等、保険業
	InterestAndDividendIncomeSummaryOfBusinessResultsINS = '' #利息及び配当金収入、経営指標等、保険業
	InvestmentAssetsYieldIncomeYieldSummaryOfBusinessResultsINS = '' #運用資産利回り（インカム利回り）、経営指標等、保険業
	InvestmentYieldRealizedYieldSummaryOfBusinessResultsINS = '' #資産運用利回り（実現利回り）、経営指標等、保険業
	EquityInEarningsLossesOfAffiliatesIfEquityMethodIsAppliedSummaryOfBusinessResults = '' #持分法を適用した場合の投資利益又は投資損失（△）、経営指標等
	CapitalStockSummaryOfBusinessResults = '' #資本金、経営指標等
	TotalNumberOfIssuedSharesSummaryOfBusinessResults = '' #発行済株式総数（普通株式）、経営指標等
	NetAssetsSummaryOfBusinessResults = '' #純資産額、経営指標等
	TotalAssetsSummaryOfBusinessResults = '' #総資産額、経営指標等
	DepositsSummaryOfBusinessResults = '' #預金残高、経営指標等
	LoansAndBillsDiscountedSummaryOfBusinessResults = '' #貸出金残高、経営指標等
	SecuritiesSummaryOfBusinessResults = '' #有価証券残高、経営指標等
	NetAssetsPerShareSummaryOfBusinessResults = '' #１株当たり純資産額、経営指標等
	DividendPaidPerShareSummaryOfBusinessResults = '' #１株当たり配当額、経営指標等
	InterimDividendPaidPerShareSummaryOfBusinessResults = '' #１株当たり中間配当額、経営指標等
	FirstQuarterDividendPaidPerShareSummaryOfBusinessResults = '' #１株当たり第１四半期配当額、経営指標等
	SecondQuarterDividendPaidPerShareSummaryOfBusinessResults = '' #１株当たり第２四半期配当額、経営指標等
	ThirdQuarterDividendPaidPerShareSummaryOfBusinessResults = '' #１株当たり第３四半期配当額、経営指標等
	FourthQuarterDividendPaidPerShareSummaryOfBusinessResults = '' #１株当たり第４四半期配当額、経営指標等
	FifthQuarterDividendPaidPerShareSummaryOfBusinessResults = '' #１株当たり第５四半期配当額、経営指標等
	BasicEarningsLossPerShareSummaryOfBusinessResults = '' #１株当たり当期純利益又は当期純損失（△）、経営指標等
	DilutedEarningsPerShareSummaryOfBusinessResults = '' #潜在株式調整後１株当たり当期純利益、経営指標等
	EquityToAssetRatioSummaryOfBusinessResults = '' #自己資本比率、経営指標等
	CapitalAdequacyRatioInternationalStandardSummaryOfBusinessResults = '' #自己資本比率（国際統一基準）、経営指標等
	CapitalAdequacyRatioDomesticStandardSummaryOfBusinessResults = '' #自己資本比率（国内基準）、経営指標等
	CapitalAdequacyRatioBISStandardSummaryOfBusinessResults = '' #自己資本比率（第一基準）、経営指標等
	CapitalAdequacyRatioDomesticStandard2SummaryOfBusinessResults = '' #自己資本比率（第二基準）、経営指標等
	RateOfReturnOnEquitySummaryOfBusinessResults = '' #自己資本利益率、経営指標等
	PriceEarningsRatioSummaryOfBusinessResults = '' #株価収益率、経営指標等
	PayoutRatioSummaryOfBusinessResults = '' #配当性向、経営指標等
	NetCashProvidedByUsedInOperatingActivitiesSummaryOfBusinessResults = '' #営業活動によるキャッシュ・フロー、経営指標等
	NetCashProvidedByUsedInInvestingActivitiesSummaryOfBusinessResults = '' #投資活動によるキャッシュ・フロー、経営指標等
	NetCashProvidedByUsedInFinancingActivitiesSummaryOfBusinessResults = '' #財務活動によるキャッシュ・フロー、経営指標等
	CashAndCashEquivalentsSummaryOfBusinessResults = '' #現金及び現金同等物の残高、経営指標等
	NumberOfEmployees = '' #従業員数
	AverageNumberOfTemporaryWorkers = '' #平均臨時雇用人員
	TotalShareholderReturn = '' #株主総利回り
	TotalReturnOnSharePriceIndex = '' #株価指数における総利回り
	CompanyHistoryHeading = '' #沿革 [目次項目]
	CompanyHistoryTextBlock = '' #沿革 [テキストブロック]
	DescriptionOfBusinessHeading = '' #事業の内容 [目次項目]
	DescriptionOfBusinessTextBlock = '' #事業の内容 [テキストブロック]
	OverviewOfAffiliatedEntitiesHeading = '' #関係会社の状況 [目次項目]
	OverviewOfAffiliatedEntitiesTextBlock = '' #関係会社の状況 [テキストブロック]
	InformationAboutEmployeesHeading = '' #従業員の状況 [目次項目]
	InformationAboutEmployeesTextBlock = '' #従業員の状況 [テキストブロック]
	InformationAboutEmployeesHeading = '' #従業員の状況 [目次項目]
	InformationAboutGroupInformationAboutEmployeesAbstract = '' #連結会社の状況、従業員の状況 [タイトル項目]
	NumberOfEmployeesOfGroupTable = '' #連結会社の従業員数 [表]
	ConsolidatedOrNonConsolidatedAxis = '' #連結個別 [軸]
	ConsolidatedMember = '' #連結 [メンバー] ※ディメンションデフォルト
	OperatingSegmentsAxis = '' #事業セグメント [軸]
	EntityTotalMember = '' #連結合計又は会社合計 [メンバー] ※ディメンションデフォルト
	ReportableSegmentsMember = '' #報告セグメント [メンバー]
	OtherReportableSegmentsMember = '' #その他の報告セグメント [メンバー]
	OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember = '' #報告セグメント以外の全てのセグメント [メンバー]
	CorporateSharedMember = '' #全社（共通） [メンバー]
	OtherOperatingSegmentsAxisMember = '' #その他、事業セグメント軸 [メンバー]
	NumberOfEmployeesOfGroupLineItems = '' #連結会社の従業員数 [表示項目]
	NumberOfEmployees = '' #従業員数
	AverageNumberOfTemporaryWorkers = '' #平均臨時雇用人員
	InformationAboutEmployeesHeading = '' #従業員の状況 [目次項目]
	InformationAboutReportingCompanyInformationAboutEmployeesAbstract = '' #提出会社の状況、従業員の状況 [タイトル項目]
	InformationAboutEmployeesOfReportingCompanyTable = '' #提出会社の従業員の状況 [表]
	ConsolidatedOrNonConsolidatedAxis = '' #連結個別 [軸]
	NonConsolidatedMember = '' #非連結又は個別 [メンバー]
	InformationAboutEmployeesOfReportingCompanyLineItems = '' #提出会社の従業員の状況 [表示項目]
	NumberOfEmployees = '' #従業員数
	AverageNumberOfTemporaryWorkers = '' #平均臨時雇用人員
	AverageAgeYearsInformationAboutReportingCompanyInformationAboutEmployees = '' #平均年齢（年）、提出会社の状況、従業員の状況
	AverageAgeMonthsInformationAboutReportingCompanyInformationAboutEmployees = '' #平均年齢（月）、提出会社の状況、従業員の状況
	AverageLengthOfServiceYearsInformationAboutReportingCompanyInformationAboutEmployees = '' #平均勤続年数（年）、提出会社の状況、従業員の状況
	AverageLengthOfServiceMonthsInformationAboutReportingCompanyInformationAboutEmployees = '' #平均勤続年数（月）、提出会社の状況、従業員の状況
	AverageAnnualSalaryInformationAboutReportingCompanyInformationAboutEmployees = '' #平均年間給与、提出会社の状況、従業員の状況
	InformationAboutEmployeesHeading = '' #従業員の状況 [目次項目]
	InformationAboutReportingCompanyInformationAboutEmployeesAbstract = '' #提出会社の状況、従業員の状況 [タイトル項目]
	NumberOfEmployeesOfReportingCompanyTable = '' #提出会社の従業員数 [表]
	ConsolidatedOrNonConsolidatedAxis = '' #連結個別 [軸]
	NonConsolidatedMember = '' #非連結又は個別 [メンバー]
	OperatingSegmentsAxis = '' #事業セグメント [軸]
	EntityTotalMember = '' #連結合計又は会社合計 [メンバー] ※ディメンションデフォルト
	ReportableSegmentsMember = '' #報告セグメント [メンバー]
	OtherReportableSegmentsMember = '' #その他の報告セグメント [メンバー]
	OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember = '' #報告セグメント以外の全てのセグメント [メンバー]
	CorporateSharedMember = '' #全社（共通） [メンバー]
	OtherOperatingSegmentsAxisMember = '' #その他、事業セグメント軸 [メンバー]
	NumberOfEmployeesOfReportingCompanyLineItems = '' #提出会社の従業員数 [表示項目]
	NumberOfEmployees = '' #従業員数
	AverageNumberOfTemporaryWorkers = '' #平均臨時雇用人員
	OverviewOfBusinessHeading = '' #事業の状況 [目次項目]
	BusinessPolicyBusinessEnvironmentIssuesToAddressEtcHeading = '' #経営方針、経営環境及び対処すべき課題等 [目次項目]
	BusinessPolicyBusinessEnvironmentIssuesToAddressEtcTextBlock = '' #経営方針、経営環境及び対処すべき課題等 [テキストブロック]
	BusinessRisksHeading = '' #事業等のリスク [目次項目]
	BusinessRisksTextBlock = '' #事業等のリスク [テキストブロック]
	MaterialMattersRelatingToGoingConcernEtcBusinessRisksTextBlock = '' #重要事象等の内容、分析及び対応策、事業等のリスク [テキストブロック]
	ManagementAnalysisOfFinancialPositionOperatingResultsAndCashFlowsHeading = '' #経営者による財政状態、経営成績及びキャッシュ・フローの状況の分析 [目次項目]
	ManagementAnalysisOfFinancialPositionOperatingResultsAndCashFlowsTextBlock = '' #経営者による財政状態、経営成績及びキャッシュ・フローの状況の分析 [テキストブロック]
	CriticalContractsForOperationHeading = '' #経営上の重要な契約等 [目次項目]
	CriticalContractsForOperationTextBlock = '' #経営上の重要な契約等 [テキストブロック]
	ResearchAndDevelopmentActivitiesHeading = '' #研究開発活動 [目次項目]
	ResearchAndDevelopmentActivitiesTextBlock = '' #研究開発活動 [テキストブロック]
	ResearchAndDevelopmentActivitiesHeading = '' #研究開発活動 [目次項目]
	ResearchAndDevelopmentExpensesResearchAndDevelopmentActivitiesTable = '' #研究開発費、研究開発活動 [表]
	OperatingSegmentsAxis = '' #事業セグメント [軸]
	EntityTotalMember = '' #連結合計又は会社合計 [メンバー] ※ディメンションデフォルト
	ReportableSegmentsMember = '' #報告セグメント [メンバー]
	OtherReportableSegmentsMember = '' #その他の報告セグメント [メンバー]
	ResearchAndDevelopmentExpensesResearchAndDevelopmentActivitiesLineItems = '' #研究開発費、研究開発活動 [表示項目]
	ResearchAndDevelopmentExpensesResearchAndDevelopmentActivities = '' #研究開発費、研究開発活動
	InformationAboutFacilitiesHeading = '' #設備の状況 [目次項目]
	OverviewOfCapitalExpendituresEtcHeading = '' #設備投資等の概要 [目次項目]
	OverviewOfCapitalExpendituresEtcTextBlock = '' #設備投資等の概要 [テキストブロック]
	OverviewOfCapitalExpendituresEtcHeading = '' #設備投資等の概要 [目次項目]
	CapitalExpendituresOverviewOfCapitalExpendituresEtcTable = '' #設備投資額、設備投資等の概要 [表]
	OperatingSegmentsAxis = '' #事業セグメント [軸]
	EntityTotalMember = '' #連結合計又は会社合計 [メンバー] ※ディメンションデフォルト
	ReportableSegmentsMember = '' #報告セグメント [メンバー]
	OtherReportableSegmentsMember = '' #その他の報告セグメント [メンバー]
	CapitalExpendituresOverviewOfCapitalExpendituresEtcLineItems = '' #設備投資額、設備投資等の概要 [表示項目]
	CapitalExpendituresOverviewOfCapitalExpendituresEtc = '' #設備投資額、設備投資等の概要
	MajorFacilitiesHeading = '' #主要な設備の状況 [目次項目]
	MajorFacilitiesTextBlock = '' #主要な設備の状況 [テキストブロック]
	PlannedAdditionsRetirementsEtcOfFacilitiesHeading = '' #設備の新設、除却等の計画 [目次項目]
	PlannedAdditionsRetirementsEtcOfFacilitiesTextBlock = '' #設備の新設、除却等の計画 [テキストブロック]
	AssetsForLeaseLEAHeading = '' #賃貸資産、リース事業 [目次項目]
	OverviewOfCapitalExpendituresEtcAssetsForLeaseLEAHeading = '' #設備投資等の概要、賃貸資産、リース事業 [目次項目]
	OverviewOfCapitalExpendituresEtcAssetsForLeaseLEATextBlock = '' #設備投資等の概要、賃貸資産、リース事業 [テキストブロック]
	MajorFacilitiesAssetsForLeaseLEAHeading = '' #主要な設備の状況、賃貸資産、リース事業 [目次項目]
	MajorFacilitiesAssetsForLeaseLEATextBlock = '' #主要な設備の状況、賃貸資産、リース事業 [テキストブロック]
	PlannedAdditionsRetirementsEtcOfFacilitiesAssetsForLeaseLEAHeading = '' #設備の新設、除却等の計画、賃貸資産、リース事業 [目次項目]
	PlannedAdditionsRetirementsEtcOfFacilitiesAssetsForLeaseLEATextBlock = '' #設備の新設、除却等の計画、賃貸資産、リース事業 [テキストブロック]
	OwnUsedAssetsLEAHeading = '' #自社用資産、リース事業 [目次項目]
	OverviewOfCapitalExpendituresEtcOwnUsedAssetsLEAHeading = '' #設備投資等の概要、自社用資産、リース事業 [目次項目]
	OverviewOfCapitalExpendituresEtcOwnUsedAssetsLEATextBlock = '' #設備投資等の概要、自社用資産、リース事業 [テキストブロック]
	MajorFacilitiesOwnUsedAssetsLEAHeading = '' #主要な設備の状況、自社用資産、リース事業 [目次項目]
	MajorFacilitiesOwnUsedAssetsLEATextBlock = '' #主要な設備の状況、自社用資産、リース事業 [テキストブロック]
	PlannedAdditionsRetirementsEtcOfFacilitiesOwnUsedAssetsLEAHeading = '' #設備の新設、除却等の計画、自社用資産、リース事業 [目次項目]
	PlannedAdditionsRetirementsEtcOfFacilitiesOwnUsedAssetsLEATextBlock = '' #設備の新設、除却等の計画、自社用資産、リース事業 [テキストブロック]
	InformationAboutReportingCompanyHeading = '' #提出会社の状況 [目次項目]
	InformationAboutSharesEtcHeading = '' #株式等の状況 [目次項目]
	TotalNumberOfSharesEtcHeading = '' #株式の総数等 [目次項目]
	TotalNumberOfSharesHeading = '' #株式の総数 [目次項目]
	TotalNumberOfSharesTextBlock = '' #株式の総数 [テキストブロック]
	IssuedSharesTotalNumberOfSharesEtcHeading = '' #発行済株式、株式の総数等 [目次項目]
	IssuedSharesTotalNumberOfSharesEtcTextBlock = '' #発行済株式、株式の総数等 [テキストブロック]
	IssuedSharesTotalNumberOfSharesEtcHeading = '' #発行済株式、株式の総数等 [目次項目]
	IssuedSharesTotalNumberOfSharesEtcTable = '' #発行済株式、株式の総数等 [表]
	ClassesOfSharesAxis = '' #株式種類 [軸]
	TotalClassesOfSharesMember = '' #合計、株式種類 [メンバー] ※ディメンションデフォルト
	OrdinaryShareMember = '' #普通株式 [メンバー]
	ClassAPreferredSharesMember = '' #Ａ種優先株式 [メンバー]
	ClassBPreferredSharesMember = '' #Ｂ種優先株式 [メンバー]
	ClassOnePreferredSharesMember = '' #第一種優先株式 [メンバー]
	ClassTwoPreferredSharesMember = '' #第二種優先株式 [メンバー]
	ClassASharesMember = '' #Ａ種種類株式 [メンバー]
	IssuedSharesTotalNumberOfSharesEtcLineItems = '' #発行済株式、株式の総数等 [表示項目]
	ClassIssuedSharesTotalNumberOfSharesEtc = '' #種類、発行済株式、株式の総数等
	NumberOfIssuedSharesIssuedSharesTotalNumberOfSharesEtc = '' #発行数（株）、発行済株式、株式の総数等
	NumberOfIssuedSharesAsOfFiscalYearEndIssuedSharesTotalNumberOfSharesEtc = '' #事業年度末現在発行数（株）、発行済株式、株式の総数等
	NumberOfIssuedSharesAsOfFilingDateIssuedSharesTotalNumberOfSharesEtc = '' #提出日現在発行数（株）、発行済株式、株式の総数等
	NameOfFinancialInstrumentsExchangeOnWhichSecuritiesAreListedOrAuthorizedFinancialInstrumentsBusinessAssociationToWhichSecuritiesAreRegistered = '' #上場金融商品取引所名又は登録認可金融商品取引業協会名
	DescriptionIssuedSharesTotalNumberOfSharesEtc = '' #内容、発行済株式、株式の総数等
	SubscriptionRightsToSharesEtcHeading = '' #新株予約権等の状況 [目次項目]
	DetailsOfEmployeeShareOptionProgramHeading = '' #ストックオプション制度の内容 [目次項目]
	DetailsOfEmployeeShareOptionProgramTextBlock = '' #ストックオプション制度の内容 [テキストブロック]
	DescriptionOfRightsPlanHeading = '' #ライツプランの内容 [目次項目]
	DescriptionOfRightsPlanTextBlock = '' #ライツプランの内容 [テキストブロック]
	OtherInformationOnShareAcquisitionRightsHeading = '' #その他の新株予約権等の状況 [目次項目]
	OtherInformationOnShareAcquisitionRightsTextBlock = '' #その他の新株予約権等の状況 [テキストブロック]
	ExercisesEtcOfMovingStrikeConvertibleBondsEtcHeading = '' #行使価額修正条項付新株予約権付社債券等の行使状況等 [目次項目]
	ExercisesEtcOfMovingStrikeConvertibleBondsEtcTextBlock = '' #行使価額修正条項付新株予約権付社債券等の行使状況等 [テキストブロック]
	ChangesInNumberOfIssuedSharesStatedCapitalEtcHeading = '' #発行済株式総数、資本金等の推移 [目次項目]
	ChangesInNumberOfIssuedSharesStatedCapitalEtcTextBlock = '' #発行済株式総数、資本金等の推移 [テキストブロック]
	ShareholdingByShareholderCategoryHeading = '' #所有者別状況 [目次項目]
	ShareholdingByShareholderCategoryTextBlock = '' #所有者別状況 [テキストブロック]
	ShareholdingByShareholderCategoryHeading = '' #所有者別状況 [目次項目]
	ShareholdingByShareholderCategoryTable = '' #所有者別状況 [表]
	ClassesOfSharesAxis = '' #株式種類 [軸]
	TotalClassesOfSharesMember = '' #合計、株式種類 [メンバー] ※ディメンションデフォルト
	OrdinaryShareMember = '' #普通株式 [メンバー]
	ClassAPreferredSharesMember = '' #Ａ種優先株式 [メンバー]
	ClassBPreferredSharesMember = '' #Ｂ種優先株式 [メンバー]
	ClassOnePreferredSharesMember = '' #第一種優先株式 [メンバー]
	ClassTwoPreferredSharesMember = '' #第二種優先株式 [メンバー]
	ClassASharesMember = '' #Ａ種種類株式 [メンバー]
	ShareholdingByShareholderCategoryLineItems = '' #所有者別状況 [表示項目]
	NumberOfSharesConstitutingOneUnit = '' #１単元の株式数
	NumberOfShareholdersNationalAndLocalGovernments = '' #株主数－政府及び地方公共団体
	NumberOfShareholdersFinancialInstitutions = '' #株主数－金融機関
	NumberOfShareholdersFinancialServiceProviders = '' #株主数－金融商品取引業者
	NumberOfShareholdersOtherCorporations = '' #株主数－その他の法人
	NumberOfShareholdersForeignInvestorsOtherThanIndividuals = '' #株主数－外国法人等－個人以外
	NumberOfShareholdersForeignIndividualInvestors = '' #株主数－外国法人等－個人
	NumberOfShareholdersIndividualsAndOthers = '' #株主数－個人その他
	NumberOfShareholdersTotal = '' #株主数－計
	NumberOfSharesHeldNumberOfUnitsNationalAndLocalGovernments = '' #所有株式数（単元）－政府及び地方公共団体
	NumberOfSharesHeldNumberOfUnitsFinancialInstitutions = '' #所有株式数（単元）－金融機関
	NumberOfSharesHeldNumberOfUnitsFinancialServiceProviders = '' #所有株式数（単元）－金融商品取引業者
	NumberOfSharesHeldNumberOfUnitsOtherCorporations = '' #所有株式数（単元）－その他の法人
	NumberOfSharesHeldNumberOfUnitsForeignInvestorsOtherThanIndividuals = '' #所有株式数（単元）－外国法人等－個人以外
	NumberOfSharesHeldNumberOfUnitsForeignIndividualInvestors = '' #所有株式数（単元）－外国法人等－個人
	NumberOfSharesHeldNumberOfUnitsIndividualsAndOthers = '' #所有株式数（単元）－個人その他
	NumberOfSharesHeldNumberOfUnitsTotal = '' #所有株式数（単元）－計
	NumberOfSharesHeldSharesLessThanOneUnit = '' #所有株式数－単元未満株式の状況（株）
	PercentageOfShareholdingsNationalAndLocalGovernments = '' #所有株式数の割合（％）－政府及び地方公共団体
	PercentageOfShareholdingsFinancialInstitutions = '' #所有株式数の割合（％）－金融機関
	PercentageOfShareholdingsFinancialServiceProviders = '' #所有株式数の割合（％）－金融商品取引業者
	PercentageOfShareholdingsOtherCorporations = '' #所有株式数の割合（％）－その他の法人
	PercentageOfShareholdingsForeignersOtherThanIndividuals = '' #所有株式数の割合（％）－外国法人等－個人以外
	PercentageOfShareholdingsForeignIndividuals = '' #所有株式数の割合（％）－外国法人等－個人
	PercentageOfShareholdingsIndividualsAndOthers = '' #所有株式数の割合（％）－個人その他
	MajorShareholdersHeading = '' #大株主の状況 [目次項目]
	MajorShareholdersTextBlock = '' #大株主の状況 [テキストブロック]
	MajorShareholdersHeading = '' #大株主の状況 [目次項目]
	MajorShareholdersTable = '' #大株主の状況 [表]
	MajorShareholdersAxis = '' #大株主 [軸]
	MajorShareholdersMember = '' #大株主 [メンバー] ※ディメンションデフォルト
	No1MajorShareholdersMember = '' #第1位、大株主 [メンバー]
	No2MajorShareholdersMember = '' #第2位、大株主 [メンバー]
	No3MajorShareholdersMember = '' #第3位、大株主 [メンバー]
	No4MajorShareholdersMember = '' #第4位、大株主 [メンバー]
	No5MajorShareholdersMember = '' #第5位、大株主 [メンバー]
	No6MajorShareholdersMember = '' #第6位、大株主 [メンバー]
	No7MajorShareholdersMember = '' #第7位、大株主 [メンバー]
	No8MajorShareholdersMember = '' #第8位、大株主 [メンバー]
	No9MajorShareholdersMember = '' #第9位、大株主 [メンバー]
	No10MajorShareholdersMember = '' #第10位、大株主 [メンバー]
	No11MajorShareholdersMember = '' #第11位、大株主 [メンバー]
	No12MajorShareholdersMember = '' #第12位、大株主 [メンバー]
	No13MajorShareholdersMember = '' #第13位、大株主 [メンバー]
	No14MajorShareholdersMember = '' #第14位、大株主 [メンバー]
	No15MajorShareholdersMember = '' #第15位、大株主 [メンバー]
	MajorShareholdersLineItems = '' #大株主の状況 [表示項目]
	NameMajorShareholders = '' #氏名又は名称、大株主の状況
	AddressMajorShareholders = '' #住所、大株主の状況
	NumberOfSharesHeld = '' #所有株式数
	ShareholdingRatio = '' #発行済株式（自己株式を除く。）の総数に対する所有株式数の割合
	MajorShareholdersHeading = '' #大株主の状況 [目次項目]
	MajorShareholdersVotingRightsTable = '' #所有株式に係る議決権上位者の状況 [表]
	MajorShareholdersVotingRightsAxis = '' #議決権上位 [軸]
	MajorShareholdersVotingRightsMember = '' #議決権上位 [メンバー] ※ディメンションデフォルト
	No1MajorShareholdersVotingRightsMember = '' #第1位、議決権上位 [メンバー]
	No2MajorShareholdersVotingRightsMember = '' #第2位、議決権上位 [メンバー]
	No3MajorShareholdersVotingRightsMember = '' #第3位、議決権上位 [メンバー]
	No4MajorShareholdersVotingRightsMember = '' #第4位、議決権上位 [メンバー]
	No5MajorShareholdersVotingRightsMember = '' #第5位、議決権上位 [メンバー]
	No6MajorShareholdersVotingRightsMember = '' #第6位、議決権上位 [メンバー]
	No7MajorShareholdersVotingRightsMember = '' #第7位、議決権上位 [メンバー]
	No8MajorShareholdersVotingRightsMember = '' #第8位、議決権上位 [メンバー]
	No9MajorShareholdersVotingRightsMember = '' #第9位、議決権上位 [メンバー]
	No10MajorShareholdersVotingRightsMember = '' #第10位、議決権上位 [メンバー]
	No11MajorShareholdersVotingRightsMember = '' #第11位、議決権上位 [メンバー]
	No12MajorShareholdersVotingRightsMember = '' #第12位、議決権上位 [メンバー]
	No13MajorShareholdersVotingRightsMember = '' #第13位、議決権上位 [メンバー]
	No14MajorShareholdersVotingRightsMember = '' #第14位、議決権上位 [メンバー]
	No15MajorShareholdersVotingRightsMember = '' #第15位、議決権上位 [メンバー]
	MajorShareholdersVotingRightsLineItems = '' #所有株式に係る議決権上位者の状況 [表示項目]
	NameMajorShareholdersVotingRights = '' #氏名又は名称、所有株式に係る議決権上位者の状況
	AddressMajorShareholdersVotingRights = '' #住所、所有株式に係る議決権上位者の状況
	NumberOfVotingRightsHeld = '' #所有議決権数（個）
	RatioOfVotingRightsHeld = '' #総株主の議決権に対する所有議決権数の割合
	VotingRightsHeading = '' #議決権の状況 [目次項目]
	VotingRightsTextBlock = '' #議決権の状況 [テキストブロック]
	IssuedSharesVotingRightsHeading = '' #発行済株式、議決権の状況 [目次項目]
	IssuedSharesVotingRightsTextBlock = '' #発行済株式、議決権の状況 [テキストブロック]
	IssuedSharesVotingRightsHeading = '' #発行済株式、議決権の状況 [目次項目]
	IssuedSharesVotingRightsTable = '' #発行済株式、議決権の状況 [表]
	CategoriesIssuedSharesAxis = '' #区分、発行済株式 [軸]
	TotalNumberOfIssuedSharesNumberOfVotingRightsHeldByAllShareholdersMember = '' #発行済株式総数／総株主の議決権 [メンバー] ※ディメンションデフォルト
	SharesWithNoVotingRightsMember = '' #無議決権株式 [メンバー]
	SharesWithRestrictedVotingRightsTreasurySharesEtcMember = '' #議決権制限株式（自己株式等） [メンバー]
	SharesWithRestrictedVotingRightsOtherMember = '' #議決権制限株式（その他） [メンバー]
	SharesWithFullVotingRightsTreasurySharesEtcMember = '' #完全議決権株式（自己株式等） [メンバー]
	OrdinarySharesSharesWithFullVotingRightsTreasurySharesEtcMember = '' #普通株式、完全議決権株式（自己株式等） [メンバー]
	OrdinarySharesTreasurySharesSharesWithFullVotingRightsTreasurySharesEtcMember = '' #（自己保有株式）普通株式、完全議決権株式（自己株式等） [メンバー]
	OrdinarySharesReciprocalHoldingSharesWithFullVotingRightsTreasurySharesEtcMember = '' #（相互保有株式）普通株式、完全議決権株式（自己株式等） [メンバー]
	SharesWithFullVotingRightsOtherMember = '' #完全議決権株式（その他） [メンバー]
	OrdinarySharesSharesWithFullVotingRightsOtherMember = '' #普通株式、完全議決権株式（その他） [メンバー]
	SharesLessThanOneUnitMember = '' #単元未満株式 [メンバー]
	OrdinarySharesSharesLessThanOneUnitMember = '' #普通株式、単元未満株式 [メンバー]
	IssuedSharesVotingRightsLineItems = '' #発行済株式、議決権の状況 [表示項目]
	NumberOfSharesIssuedSharesVotingRights = '' #株式数（株）、発行済株式、議決権の状況
	NumberOfVotingRightsIssuedSharesVotingRights = '' #議決権の数（個）、発行済株式、議決権の状況
	DescriptionIssuedSharesVotingRights = '' #内容、発行済株式、議決権の状況
	TreasurySharesEtcHeading = '' #自己株式等 [目次項目]
	TreasurySharesEtcTextBlock = '' #自己株式等 [テキストブロック]
	TreasurySharesEtcHeading = '' #自己株式等 [目次項目]
	TreasurySharesEtcTable = '' #自己株式等 [表]
	SequentialNumbersAxis = '' #連番 [軸]
	TotalSequentialNumbersMember = '' #合計、連番 [メンバー] ※ディメンションデフォルト
	Row1Member = '' #1件目 [メンバー]
	Row2Member = '' #2件目 [メンバー]
	Row3Member = '' #3件目 [メンバー]
	Row4Member = '' #4件目 [メンバー]
	TreasurySharesEtcLineItems = '' #自己株式等 [表示項目]
	NameOfShareholderTreasurySharesEtc = '' #所有者の氏名又は名称、自己株式等
	AddressOfShareholderTreasurySharesEtc = '' #所有者の住所、自己株式等
	NumberOfSharesHeldInOwnNameTreasurySharesEtc = '' #自己名義所有株式数（株）、自己株式等
	NumberOfSharesHeldInOthersNamesTreasurySharesEtc = '' #他人名義所有株式数（株）、自己株式等
	TotalNumberOfSharesHeldTreasurySharesEtc = '' #所有株式数の合計（株）、自己株式等
	ShareholdingRatioTreasurySharesEtc = '' #発行済株式総数に対する所有株式数の割合（％）、自己株式等
	DetailsOfTransfersOfSharesEtcByAcquirerHeading = '' #取得者の株式等の移動状況 [目次項目]
	DetailsOfTransfersOfSharesEtcByAcquirerTextBlock = '' #取得者の株式等の移動状況 [テキストブロック]
	ShareOwnershipPlansForDirectorsAndOtherOfficersAndEmployeesHeading = '' #役員・従業員株式所有制度の内容 [目次項目]
	ShareOwnershipPlansForDirectorsAndOtherOfficersAndEmployeesTextBlock = '' #役員・従業員株式所有制度の内容 [テキストブロック]
	AcquisitionsEtcOfTreasurySharesHeading = '' #自己株式の取得等の状況 [目次項目]
	AcquisitionsEtcOfTreasurySharesTextBlock = '' #自己株式の取得等の状況 [テキストブロック]
	ClassesOfSharesEtcHeading = '' #株式の種類等 [目次項目]
	ClassesOfSharesEtcTextBlock = '' #株式の種類等 [テキストブロック]
	AcquisitionsByResolutionOfShareholdersMeetingHeading = '' #株主総会決議による取得の状況 [目次項目]
	AcquisitionsByResolutionOfShareholdersMeetingTextBlock = '' #株主総会決議による取得の状況 [テキストブロック]
	AcquisitionsByResolutionOfBoardOfDirectorsMeetingHeading = '' #取締役会決議による取得の状況 [目次項目]
	AcquisitionsByResolutionOfBoardOfDirectorsMeetingTextBlock = '' #取締役会決議による取得の状況 [テキストブロック]
	AcquisitionsNotBasedOnResolutionOfShareholdersMeetingOrBoardOfDirectorsMeetingHeading = '' #株主総会決議又は取締役会決議に基づかないものの内容 [目次項目]
	AcquisitionsNotBasedOnResolutionOfShareholdersMeetingOrBoardOfDirectorsMeetingTextBlock = '' #株主総会決議又は取締役会決議に基づかないものの内容 [テキストブロック]
	DisposalsOrHoldingOfAcquiredTreasurySharesHeading = '' #取得自己株式の処理状況及び保有状況 [目次項目]
	DisposalsOrHoldingOfAcquiredTreasurySharesTextBlock = '' #取得自己株式の処理状況及び保有状況 [テキストブロック]
	DividendPolicyHeading = '' #配当政策 [目次項目]
	DividendPolicyTextBlock = '' #配当政策 [テキストブロック]
	DividendPolicyHeading = '' #配当政策 [目次項目]
	DividendsOfSurplusTable = '' #剰余金の配当 [表]
	SequentialNumbersAxis = '' #連番 [軸]
	Row1Member = '' #1件目 [メンバー]
	Row2Member = '' #2件目 [メンバー]
	Row3Member = '' #3件目 [メンバー]
	Row4Member = '' #4件目 [メンバー]
	DividendsOfSurplusLineItems = '' #剰余金の配当 [表示項目]
	DateOfResolutionDividendsOfSurplus = '' #決議日付、剰余金の配当
	ResolutionDividendsOfSurplus = '' #決議、剰余金の配当
	RecordDateDividendsOfSurplus = '' #基準日、剰余金の配当
	TotalAmountOfDividendsDividendsOfSurplus = '' #配当金の総額、剰余金の配当
	DividendPerShareDividendsOfSurplus = '' #１株当たり配当額、剰余金の配当
	ExplanationAboutCorporateGovernanceEtcHeading = '' #コーポレート・ガバナンスの状況等 [目次項目]
	OverviewOfCorporateGovernanceHeading = '' #コーポレート・ガバナンスの概要 [目次項目]
	OverviewOfCorporateGovernanceTextBlock = '' #コーポレート・ガバナンスの概要 [テキストブロック]
	DescriptionOfFactThatCorporateGovernanceSystemChoiceFromThreeCategoriesWasChangedTextBlock = '' #企業統治の組織形態（３分類）の変更 [テキストブロック]
	CorporateGovernanceCompanyWithCorporateAuditorsTextBlock = '' #企業統治の体制の概要（監査役設置会社） [テキストブロック]
	CorporateGovernanceCompanyWithAuditAndSupervisoryCommitteeTextBlock = '' #企業統治の体制の概要（監査等委員会設置会社） [テキストブロック]
	CorporateGovernanceCompanyWithNominatingAndOtherCommitteesTextBlock = '' #企業統治の体制の概要（指名委員会等設置会社） [テキストブロック]
	BasicPolicyRegardingControlOfCompanyTextBlock = '' #会社の支配に関する基本方針 [テキストブロック]
	InformationAboutOfficersHeading = '' #役員の状況 [目次項目]
	InformationAboutOfficersTextBlock = '' #役員の状況 [テキストブロック]
	InformationAboutOfficersHeading = '' #役員の状況 [目次項目]
	NumberOfMaleDirectorsAndOtherOfficers = '' #役員のうち男性の人数
	NumberOfFemaleDirectorsAndOtherOfficers = '' #役員のうち女性の人数
	RatioOfFemaleDirectorsAndOtherOfficers = '' #役員のうち女性の比率
	InformationAboutOfficersHeading = '' #役員の状況 [目次項目]
	InformationAboutDirectorsAndCorporateAuditorsTable = '' #役員の状況（取締役（及び監査役）） [表]
	DirectorsAndOtherOfficersAxis = '' #役員 [軸]
	DirectorsAndOtherOfficersMember = '' #役員 [メンバー] ※ディメンションデフォルト
	InformationAboutDirectorsAndCorporateAuditorsLineItems = '' #役員の状況（取締役（及び監査役）） [表示項目]
	OfficialTitleOrPositionInformationAboutDirectorsAndCorporateAuditors = '' #役職名、役員の状況（取締役（及び監査役））
	NameInformationAboutDirectorsAndCorporateAuditors = '' #氏名、役員の状況（取締役（及び監査役））
	DateOfBirthInformationAboutDirectorsAndCorporateAuditors = '' #生年月日、役員の状況（取締役（及び監査役））
	CareerSummaryInformationAboutDirectorsAndCorporateAuditorsTextBlock = '' #略歴、役員の状況（取締役（及び監査役）） [テキストブロック]
	TermOfOfficeInformationAboutDirectorsAndCorporateAuditors = '' #任期、役員の状況（取締役（及び監査役））
	NumberOfSharesHeldOrdinarySharesInformationAboutDirectorsAndCorporateAuditors = '' #所有株式数（普通株式）、役員の状況（取締役（及び監査役））
	NumberOfSharesHeldOtherThanOrdinarySharesInformationAboutDirectorsAndCorporateAuditors = '' #所有株式数（普通株式以外）、役員の状況（取締役（及び監査役））
	InformationAboutOfficersHeading = '' #役員の状況 [目次項目]
	FootnotesDirectorsAndCorporateAuditorsTable = '' #脚注（取締役（及び監査役）） [表]
	SequentialNumbersAxis = '' #連番 [軸]
	Row1Member = '' #1件目 [メンバー]
	Row2Member = '' #2件目 [メンバー]
	Row3Member = '' #3件目 [メンバー]
	Row4Member = '' #4件目 [メンバー]
	Row5Member = '' #5件目 [メンバー]
	FootnotesDirectorsAndCorporateAuditorsLineItems = '' #脚注（取締役（及び監査役）） [表示項目]
	FootnotesDirectorsAndCorporateAuditorsTextBlock = '' #脚注（取締役（及び監査役） [テキストブロック]
	InformationAboutOfficersHeading = '' #役員の状況 [目次項目]
	InformationAboutExecutiveDirectorsTable = '' #役員の状況（執行役） [表]
	DirectorsAndOtherOfficersAxis = '' #役員 [軸]
	DirectorsAndOtherOfficersMember = '' #役員 [メンバー] ※ディメンションデフォルト
	InformationAboutExecutiveDirectorsLineItems = '' #役員の状況（執行役） [表示項目]
	OfficialTitleOrPositionInformationAboutExecutiveDirectors = '' #役職名、役員の状況（執行役）
	NameInformationAboutExecutiveDirectors = '' #氏名、役員の状況（執行役）
	DateOfBirthInformationAboutExecutiveDirectors = '' #生年月日、役員の状況（執行役）
	CareerSummaryInformationAboutExecutiveDirectorsTextBlock = '' #略歴、役員の状況（執行役） [テキストブロック]
	TermOfOfficeInformationAboutExecutiveDirectors = '' #任期、役員の状況（執行役）
	NumberOfSharesHeldOrdinarySharesInformationAboutExecutiveDirectors = '' #所有株式数（普通株式）、役員の状況（執行役）
	NumberOfSharesHeldOtherThanOrdinarySharesInformationAboutExecutiveDirectors = '' #所有株式数（普通株式以外）、役員の状況（執行役）
	InformationAboutOfficersHeading = '' #役員の状況 [目次項目]
	FootnotesExecutiveOfficersTable = '' #脚注（執行役） [表]
	SequentialNumbersAxis = '' #連番 [軸]
	Row1Member = '' #1件目 [メンバー]
	Row2Member = '' #2件目 [メンバー]
	Row3Member = '' #3件目 [メンバー]
	Row4Member = '' #4件目 [メンバー]
	Row5Member = '' #5件目 [メンバー]
	FootnotesExecutiveOfficersLineItems = '' #脚注（執行役） [表示項目]
	FootnotesExecutiveOfficersTextBlock = '' #脚注（執行役） [テキストブロック]
	InformationAboutOfficersHeading = '' #役員の状況 [目次項目]
	NumberOfMaleDirectorsAndOtherOfficersProposal = '' #役員のうち男性の人数（議案）
	NumberOfFemaleDirectorsAndOtherOfficersProposal = '' #役員のうち女性の人数（議案）
	RatioOfFemaleDirectorsAndOtherOfficersProposal = '' #役員のうち女性の比率（議案）
	InformationAboutOfficersHeading = '' #役員の状況 [目次項目]
	InformationAboutDirectorsAndCorporateAuditorsProposalTable = '' #役員の状況（取締役（及び監査役））（議案） [表]
	DirectorsAndOtherOfficersAxis = '' #役員 [軸]
	DirectorsAndOtherOfficersMember = '' #役員 [メンバー] ※ディメンションデフォルト
	InformationAboutDirectorsAndCorporateAuditorsProposalLineItems = '' #役員の状況（取締役（及び監査役））（議案） [表示項目]
	OfficialTitleOrPositionInformationAboutDirectorsAndCorporateAuditorsProposal = '' #役職名、役員の状況（取締役（及び監査役））（議案）
	NameInformationAboutDirectorsAndCorporateAuditorsProposal = '' #氏名、役員の状況（取締役（及び監査役））（議案）
	DateOfBirthInformationAboutDirectorsAndCorporateAuditorsProposal = '' #生年月日、役員の状況（取締役（及び監査役））（議案）
	CareerSummaryInformationAboutDirectorsAndCorporateAuditorsProposalTextBlock = '' #略歴、役員の状況（取締役（及び監査役））（議案） [テキストブロック]
	TermOfOfficeInformationAboutDirectorsAndCorporateAuditorsProposal = '' #任期、役員の状況（取締役（及び監査役））（議案）
	NumberOfSharesHeldOrdinarySharesInformationAboutDirectorsAndCorporateAuditorsProposal = '' #所有株式数（普通株式）、役員の状況（取締役（及び監査役））（議案）
	NumberOfSharesHeldOtherThanOrdinarySharesInformationAboutDirectorsAndCorporateAuditorsProposal = '' #所有株式数（普通株式以外）、役員の状況（取締役（及び監査役））（議案）
	InformationAboutOfficersHeading = '' #役員の状況 [目次項目]
	FootnotesDirectorsAndCorporateAuditorsProposalTable = '' #脚注（取締役（及び監査役））（議案） [表]
	SequentialNumbersAxis = '' #連番 [軸]
	Row1Member = '' #1件目 [メンバー]
	Row2Member = '' #2件目 [メンバー]
	Row3Member = '' #3件目 [メンバー]
	Row4Member = '' #4件目 [メンバー]
	Row5Member = '' #5件目 [メンバー]
	FootnotesDirectorsAndCorporateAuditorsProposalLineItems = '' #脚注（取締役（及び監査役））（議案） [表示項目]
	FootnotesDirectorsAndCorporateAuditorsProposalTextBlock = '' #脚注（取締役（及び監査役））（議案） [テキストブロック]
	InformationAboutOfficersHeading = '' #役員の状況 [目次項目]
	InformationAboutExecutiveDirectorsProposalTable = '' #役員の状況（執行役）（議案） [表]
	DirectorsAndOtherOfficersAxis = '' #役員 [軸]
	DirectorsAndOtherOfficersMember = '' #役員 [メンバー] ※ディメンションデフォルト
	InformationAboutExecutiveDirectorsProposalLineItems = '' #役員の状況（執行役）（議案） [表示項目]
	OfficialTitleOrPositionInformationAboutExecutiveDirectorsProposal = '' #役職名、役員の状況（執行役）（議案）
	NameInformationAboutExecutiveDirectorsProposal = '' #氏名、役員の状況（執行役）（議案）
	DateOfBirthInformationAboutExecutiveDirectorsProposal = '' #生年月日、役員の状況（執行役）（議案）
	CareerSummaryInformationAboutExecutiveDirectorsProposalTextBlock = '' #略歴、役員の状況（執行役）（議案） [テキストブロック]
	TermOfOfficeInformationAboutExecutiveDirectorsProposal = '' #任期、役員の状況（執行役）（議案）
	NumberOfSharesHeldOrdinarySharesInformationAboutExecutiveDirectorsProposal = '' #所有株式数（普通株式）、役員の状況（執行役）（議案）
	NumberOfSharesHeldOtherThanOrdinarySharesInformationAboutExecutiveDirectorsProposal = '' #所有株式数（普通株式以外）、役員の状況（執行役）（議案）
	InformationAboutOfficersHeading = '' #役員の状況 [目次項目]
	FootnotesExecutiveOfficersProposalTable = '' #脚注（執行役）（議案） [表]
	SequentialNumbersAxis = '' #連番 [軸]
	Row1Member = '' #1件目 [メンバー]
	Row2Member = '' #2件目 [メンバー]
	Row3Member = '' #3件目 [メンバー]
	Row4Member = '' #4件目 [メンバー]
	Row5Member = '' #5件目 [メンバー]
	FootnotesExecutiveOfficersProposalLineItems = '' #脚注（執行役）（議案） [表示項目]
	FootnotesExecutiveOfficersProposalTextBlock = '' #脚注（執行役）（議案） [テキストブロック]
	OutsideDirectorsAndOutsideCorporateAuditorsTextBlock = '' #社外取締役（及び社外監査役） [テキストブロック]
	AuditsHeading = '' #監査の状況 [目次項目]
	AuditsTextBlock = '' #監査の状況 [テキストブロック]
	AuditsHeading = '' #監査の状況 [目次項目]
	NoteOnChangeOfIndependentAuditorsAuditsTextBlock = '' #監査公認会計士等の異動について、監査の状況 [テキストブロック]
	FeesToPrimaryAuditorAbstract = '' #監査公認会計士等に対する報酬の内容 [タイトル項目]
	AuditFeesReportingCompany = '' #監査証明業務に基づく報酬－提出会社、監査公認会計士等
	NonAuditFeesReportingCompany = '' #非監査業務に基づく報酬－提出会社、監査公認会計士等
	AuditFeesConsolidatedSubsidiaries = '' #監査証明業務に基づく報酬－連結子会社、監査公認会計士等
	NonAuditFeesConsolidatedSubsidiaries = '' #非監査業務に基づく報酬－連結子会社、監査公認会計士等
	AuditFeesTotal = '' #監査証明業務に基づく報酬－計、監査公認会計士等
	NonAuditFeesTotal = '' #非監査業務に基づく報酬－計、監査公認会計士等
	FeesToNetworkFirmsAbstract = '' #ネットワークファームに対する報酬の内容 [タイトル項目]
	AuditFeesReportingCompanyNetworkFirms = '' #監査証明業務に基づく報酬－提出会社、ネットワークファーム
	NonAuditFeesReportingCompanyNetworkFirms = '' #非監査業務に基づく報酬－提出会社、ネットワークファーム
	AuditFeesConsolidatedSubsidiariesNetworkFirms = '' #監査証明業務に基づく報酬－連結子会社、ネットワークファーム
	NonAuditFeesConsolidatedSubsidiariesNetworkFirms = '' #非監査業務に基づく報酬－連結子会社、ネットワークファーム
	AuditFeesTotalNetworkFirms = '' #監査証明業務に基づく報酬－計、ネットワークファーム
	NonAuditFeesTotalNetworkFirms = '' #非監査業務に基づく報酬－計、ネットワークファーム
	RemunerationForDirectorsAndOtherOfficersHeading = '' #役員の報酬等 [目次項目]
	RemunerationForDirectorsAndOtherOfficersTextBlock = '' #役員の報酬等 [テキストブロック]
	RemunerationForDirectorsAndOtherOfficersHeading = '' #役員の報酬等 [目次項目]
	RemunerationEtcByCategoryOfDirectorsAndOtherOfficersAbstract = '' #役員区分ごとの報酬等 [タイトル項目]
	RemunerationEtcByCategoryOfDirectorsAndOtherOfficersTable = '' #役員区分ごとの報酬等 [表]
	CategoriesOfDirectorsAndOtherOfficersAxis = '' #役員区分 [軸]
	DirectorsExcludingOutsideDirectorsMember = '' #取締役（社外取締役を除く） [メンバー]
	DirectorsExcludingAuditAndSupervisoryCommitteeMembersAndOutsideDirectorsMember = '' #取締役（監査等委員及び社外取締役を除く） [メンバー]
	DirectorsAppointedAsAuditAndSupervisoryCommitteeMembersExcludingOutsideDirectorsMember = '' #監査等委員（社外取締役を除く） [メンバー]
	CorporateAuditorsExcludingOutsideCorporateAuditorsMember = '' #監査役（社外監査役を除く） [メンバー]
	ExecutiveOfficersMember = '' #執行役 [メンバー]
	OutsideDirectorsAndOtherOfficersMember = '' #社外役員 [メンバー]
	OutsideDirectorsMember = '' #社外取締役 [メンバー]
	OutsideCorporateAuditorsMember = '' #社外監査役 [メンバー]
	RemunerationEtcByCategoryOfDirectorsAndOtherOfficersLineItems = '' #役員区分ごとの報酬等 [表示項目]
	TotalAmountOfRemunerationEtcRemunerationEtcByCategoryOfDirectorsAndOtherOfficers = '' #報酬等の総額、役員区分ごとの報酬等
	TotalAmountByTypeOfRemunerationRemunerationEtcByCategoryOfDirectorsAndOtherOfficersAbstract = '' #報酬等の種類別の総額、役員区分ごとの報酬等 [タイトル項目]
	FixedRemunerationRemunerationByCategoryOfDirectorsAndOtherOfficers = '' #固定報酬、役員区分ごとの報酬等
	PerformanceBasedRemunerationRemunerationByCategoryOfDirectorsAndOtherOfficers = '' #業績連動報酬、役員区分ごとの報酬等
	BaseRemunerationRemunerationEtcByCategoryOfDirectorsAndOtherOfficers = '' #基本報酬、役員区分ごとの報酬等
	ShareAwardsRemunerationEtcByCategoryOfDirectorsAndOtherOfficers = '' #株式報酬、役員区分ごとの報酬等
	RestrictedShareAwardsRemunerationEtcByCategoryOfDirectorsAndOtherOfficers = '' #譲渡制限付株式報酬、役員区分ごとの報酬等
	PerformanceLinkedShareAwardsRemunerationEtcByCategoryOfDirectorsAndOtherOfficers = '' #業績連動型株式報酬、役員区分ごとの報酬等
	ShareOptionRemunerationEtcByCategoryOfDirectorsAndOtherOfficers = '' #ストックオプション、役員区分ごとの報酬等
	BonusRemunerationEtcByCategoryOfDirectorsAndOtherOfficers = '' #賞与、役員区分ごとの報酬等
	RetirementBenefitsRemunerationEtcByCategoryOfDirectorsAndOtherOfficers = '' #退職慰労金、役員区分ごとの報酬等
	NonMonetaryRemunerationRemunerationByCategoryOfDirectorsAndOtherOfficers = '' #非金銭報酬等、役員区分ごとの報酬等
	OtherRemunerationEtcByCategoryOfDirectorsAndOtherOfficers = '' #その他、役員区分ごとの報酬等
	NumberOfDirectorsAndOtherOfficersRemunerationEtcByCategoryOfDirectorsAndOtherOfficers = '' #対象となる役員の員数、役員区分ごとの報酬等
	RemunerationEtcPaidByGroupToEachDirectorOrOtherOfficerTextBlock = '' #役員ごとの連結報酬等 [テキストブロック]
	RemunerationForDirectorsAndOtherOfficersHeading = '' #役員の報酬等 [目次項目]
	RemunerationEtcPaidByGroupToEachDirectorOrOtherOfficerAbstract = '' #役員ごとの連結報酬等 [タイトル項目]
	RemunerationEtcPaidByGroupToEachDirectorOrOtherOfficerTable = '' #役員ごとの連結報酬等 [表]
	DirectorsAndOtherOfficersAxis = '' #役員 [軸]
	DirectorsAndOtherOfficersMember = '' #役員 [メンバー] ※ディメンションデフォルト
	RemunerationEtcPaidByGroupToEachDirectorOrOtherOfficerLineItems = '' #役員ごとの連結報酬等 [表示項目]
	TotalAmountOfRemunerationEtcPaidByGroupRemunerationEtcPaidByGroupToEachDirectorOrOtherOfficer = '' #連結報酬等の総額、役員ごとの連結報酬等
	ShareholdingsHeading = '' #株式の保有状況 [目次項目]
	ShareholdingsTextBlock = '' #株式の保有状況 [テキストブロック]
	ShareholdingsHeading = '' #株式の保有状況 [目次項目]
	ReportingCompanyEquitySecuritiesHeldAbstract = '' #提出会社、株式の保有状況 [タイトル項目]
	InvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentReportingCompanyAbstract = '' #保有目的が純投資目的以外の目的である投資株式、提出会社 [タイトル項目]
	SharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompanyAbstract = '' #非上場株式、保有目的が純投資目的以外の目的である投資株式、提出会社 [タイトル項目]
	NumberOfIssuesSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany = '' #銘柄数、非上場株式、保有目的が純投資目的以外の目的である投資株式、提出会社
	CarryingAmountSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany = '' #貸借対照表計上額、非上場株式、保有目的が純投資目的以外の目的である投資株式、提出会社
	NumberOfIssuesWhoseNumberOfSharesIncreasedSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany = '' #株式数が増加した銘柄数、非上場株式、保有目的が純投資目的以外の目的である投資株式、提出会社
	TotalAcquisitionCostForIncreasedSharesSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany = '' #株式数の増加に係る取得価額の合計額、非上場株式、保有目的が純投資目的以外の目的である投資株式、提出会社
	ReasonForIncreaseInNumberOfSharesSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany = '' #株式数が増加した理由、非上場株式、保有目的が純投資目的以外の目的である投資株式、提出会社
	NumberOfIssuesWhoseNumberOfSharesDecreasedSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany = '' #株式数が減少した銘柄数、非上場株式、保有目的が純投資目的以外の目的である投資株式、提出会社
	TotalSaleAmountForDecreasedSharesSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany = '' #株式数の減少に係る売却価額の合計額、非上場株式、保有目的が純投資目的以外の目的である投資株式、提出会社
	SharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompanyAbstract = '' #非上場株式以外の株式、保有目的が純投資目的以外の目的である投資株式、提出会社 [タイトル項目]
	NumberOfIssuesSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany = '' #銘柄数、非上場株式以外の株式、保有目的が純投資目的以外の目的である投資株式、提出会社
	CarryingAmountSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany = '' #貸借対照表計上額、非上場株式以外の株式、保有目的が純投資目的以外の目的である投資株式、提出会社
	NumberOfIssuesWhoseNumberOfSharesIncreasedSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany = '' #株式数が増加した銘柄数、非上場株式以外の株式、保有目的が純投資目的以外の目的である投資株式、提出会社
	TotalAcquisitionCostForIncreasedSharesSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany = '' #株式数の増加に係る取得価額の合計額、非上場株式以外の株式、保有目的が純投資目的以外の目的である投資株式、提出会社
	ReasonForIncreaseInNumberOfSharesSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany = '' #株式数が増加した理由、非上場株式以外の株式、保有目的が純投資目的以外の目的である投資株式、提出会社
	NumberOfIssuesWhoseNumberOfSharesDecreasedSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany = '' #株式数が減少した銘柄数、非上場株式以外の株式、保有目的が純投資目的以外の目的である投資株式、提出会社
	TotalSaleAmountForDecreasedSharesSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany = '' #株式数の減少に係る売却価額の合計額、非上場株式以外の株式、保有目的が純投資目的以外の目的である投資株式、提出会社
	ShareholdingsHeading = '' #株式の保有状況 [目次項目]
	ReportingCompanyEquitySecuritiesHeldAbstract = '' #提出会社、株式の保有状況 [タイトル項目]
	DetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentReportingCompanyTable = '' #保有目的が純投資目的以外の目的である特定投資株式の明細、提出会社 [表]
	SequentialNumbersAxis = '' #連番 [軸]
	Row1Member = '' #1件目 [メンバー]
	Row2Member = '' #2件目 [メンバー]
	Row3Member = '' #3件目 [メンバー]
	Row4Member = '' #4件目 [メンバー]
	Row5Member = '' #5件目 [メンバー]
	Row6Member = '' #6件目 [メンバー]
	Row7Member = '' #7件目 [メンバー]
	Row8Member = '' #8件目 [メンバー]
	Row9Member = '' #9件目 [メンバー]
	Row10Member = '' #10件目 [メンバー]
	Row11Member = '' #11件目 [メンバー]
	Row12Member = '' #12件目 [メンバー]
	Row13Member = '' #13件目 [メンバー]
	Row14Member = '' #14件目 [メンバー]
	Row15Member = '' #15件目 [メンバー]
	Row16Member = '' #16件目 [メンバー]
	Row17Member = '' #17件目 [メンバー]
	Row18Member = '' #18件目 [メンバー]
	Row19Member = '' #19件目 [メンバー]
	Row20Member = '' #20件目 [メンバー]
	Row21Member = '' #21件目 [メンバー]
	Row22Member = '' #22件目 [メンバー]
	Row23Member = '' #23件目 [メンバー]
	Row24Member = '' #24件目 [メンバー]
	Row25Member = '' #25件目 [メンバー]
	Row26Member = '' #26件目 [メンバー]
	Row27Member = '' #27件目 [メンバー]
	Row28Member = '' #28件目 [メンバー]
	Row29Member = '' #29件目 [メンバー]
	Row30Member = '' #30件目 [メンバー]
	Row31Member = '' #31件目 [メンバー]
	Row32Member = '' #32件目 [メンバー]
	Row33Member = '' #33件目 [メンバー]
	Row34Member = '' #34件目 [メンバー]
	Row35Member = '' #35件目 [メンバー]
	Row36Member = '' #36件目 [メンバー]
	Row37Member = '' #37件目 [メンバー]
	Row38Member = '' #38件目 [メンバー]
	Row39Member = '' #39件目 [メンバー]
	Row40Member = '' #40件目 [メンバー]
	Row41Member = '' #41件目 [メンバー]
	Row42Member = '' #42件目 [メンバー]
	Row43Member = '' #43件目 [メンバー]
	Row44Member = '' #44件目 [メンバー]
	Row45Member = '' #45件目 [メンバー]
	Row46Member = '' #46件目 [メンバー]
	Row47Member = '' #47件目 [メンバー]
	Row48Member = '' #48件目 [メンバー]
	Row49Member = '' #49件目 [メンバー]
	Row50Member = '' #50件目 [メンバー]
	Row51Member = '' #51件目 [メンバー]
	Row52Member = '' #52件目 [メンバー]
	Row53Member = '' #53件目 [メンバー]
	Row54Member = '' #54件目 [メンバー]
	Row55Member = '' #55件目 [メンバー]
	Row56Member = '' #56件目 [メンバー]
	Row57Member = '' #57件目 [メンバー]
	Row58Member = '' #58件目 [メンバー]
	Row59Member = '' #59件目 [メンバー]
	Row60Member = '' #60件目 [メンバー]
	DetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentReportingCompanyLineItems = '' #保有目的が純投資目的以外の目的である特定投資株式の明細、提出会社 [表示項目]
	NameOfSecuritiesDetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentReportingCompany = '' #銘柄、保有目的が純投資目的以外の目的である特定投資株式の明細、提出会社
	NumberOfSharesHeldDetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentReportingCompany = '' #株式数、保有目的が純投資目的以外の目的である特定投資株式の明細、提出会社
	NumberOfSharesNotDisclosedAsBelowThresholdDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany = '' #株式数（記載省略）、保有目的が純投資目的以外の目的である特定投資株式の明細、提出会社
	BookValueDetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentReportingCompany = '' #貸借対照表計上額、保有目的が純投資目的以外の目的である特定投資株式の明細、提出会社
	CarryingAmountNotDisclosedAsBelowThresholdDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany = '' #貸借対照表計上額（記載省略）、保有目的が純投資目的以外の目的である特定投資株式の明細、提出会社
	PurposesOfHoldingDetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentReportingCompany = '' #保有目的、保有目的が純投資目的以外の目的である特定投資株式の明細、提出会社
	QuantitativeEffectsOfShareholdingDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany = '' #定量的な保有効果、保有目的が純投資目的以外の目的である特定投資株式の明細、提出会社
	ReasonForIncreaseInNumberOfSharesDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany = '' #株式数が増加した理由、保有目的が純投資目的以外の目的である特定投資株式の明細、提出会社
	PurposeOfShareholdingQuantitativeEffectsOfShareholdingAndReasonForIncreaseInNumberOfSharesDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany = '' #保有目的、定量的な保有効果及び株式数が増加した理由、保有目的が純投資目的以外の目的である特定投資株式の明細、提出会社
	WhetherIssuerOfAforementionedSharesHoldsReportingCompanysSharesDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany = '' #当該株式の発行者による提出会社の株式の保有の有無、保有目的が純投資目的以外の目的である特定投資株式の明細、提出会社
	ShareholdingsHeading = '' #株式の保有状況 [目次項目]
	ReportingCompanyEquitySecuritiesHeldAbstract = '' #提出会社、株式の保有状況 [タイトル項目]
	DetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentReportingCompanyTable = '' #保有目的が純投資目的以外の目的であるみなし保有株式の明細、提出会社 [表]
	SequentialNumbersAxis = '' #連番 [軸]
	Row1Member = '' #1件目 [メンバー]
	Row2Member = '' #2件目 [メンバー]
	Row3Member = '' #3件目 [メンバー]
	Row4Member = '' #4件目 [メンバー]
	Row5Member = '' #5件目 [メンバー]
	Row6Member = '' #6件目 [メンバー]
	Row7Member = '' #7件目 [メンバー]
	Row8Member = '' #8件目 [メンバー]
	Row9Member = '' #9件目 [メンバー]
	Row10Member = '' #10件目 [メンバー]
	DetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentReportingCompanyLineItems = '' #保有目的が純投資目的以外の目的であるみなし保有株式の明細、提出会社 [表示項目]
	NameOfSecuritiesDetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentReportingCompany = '' #銘柄、保有目的が純投資目的以外の目的であるみなし保有株式の明細、提出会社
	NumberOfSharesHeldDetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentReportingCompany = '' #株式数、保有目的が純投資目的以外の目的であるみなし保有株式の明細、提出会社
	NumberOfSharesNotDisclosedAsBelowThresholdDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentReportingCompany = '' #株式数（記載省略）、保有目的が純投資目的以外の目的であるみなし保有株式の明細、提出会社
	BookValueDetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentReportingCompany = '' #貸借対照表計上額、保有目的が純投資目的以外の目的であるみなし保有株式の明細、提出会社
	CarryingAmountNotDisclosedAsBelowThresholdDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentReportingCompany = '' #貸借対照表計上額（記載省略）、保有目的が純投資目的以外の目的であるみなし保有株式の明細、提出会社
	PurposesOfHoldingDetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentReportingCompany = '' #保有目的、保有目的が純投資目的以外の目的であるみなし保有株式の明細、提出会社
	QuantitativeEffectsOfShareholdingDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentReportingCompany = '' #定量的な保有効果、保有目的が純投資目的以外の目的であるみなし保有株式の明細、提出会社
	ReasonForIncreaseInNumberOfSharesDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentReportingCompany = '' #株式数が増加した理由、保有目的が純投資目的以外の目的であるみなし保有株式の明細、提出会社
	PurposeOfShareholdingQuantitativeEffectsOfShareholdingAndReasonForIncreaseInNumberOfSharesDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentReportingCompany = '' #保有目的、定量的な保有効果及び株式数が増加した理由、保有目的が純投資目的以外の目的であるみなし保有株式の明細、提出会社
	WhetherIssuerOfAforementionedSharesHoldsReportingCompanysSharesDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentReportingCompany = '' #当該株式の発行者による提出会社の株式の保有の有無、保有目的が純投資目的以外の目的であるみなし保有株式の明細、提出会社
	ShareholdingsHeading = '' #株式の保有状況 [目次項目]
	ReportingCompanyEquitySecuritiesHeldAbstract = '' #提出会社、株式の保有状況 [タイトル項目]
	InvestmentEquitySecuritiesHeldForPureInvestmentReportingCompanyAbstract = '' #保有目的が純投資目的である投資株式、提出会社 [タイトル項目]
	EquitySecuritiesNotListedInvestmentEquitySecuritiesHeldForPureInvestmentReportingCompanyAbstract = '' #非上場株式、保有目的が純投資目的である投資株式、提出会社 [タイトル項目]
	NumberOfIssuesSharesNotListedInvestmentSharesHeldForPureInvestmentReportingCompany = '' #銘柄数、非上場株式、保有目的が純投資目的である投資株式、提出会社
	BookValueEquitySecuritiesNotListedInvestmentEquitySecuritiesHeldForPureInvestmentReportingCompany = '' #貸借対照表計上額の合計額、非上場株式、保有目的が純投資目的である投資株式、提出会社
	TotalOfDividendsReceivedEquitySecuritiesNotListedInvestmentEquitySecuritiesHeldForPureInvestmentReportingCompany = '' #受取配当金の合計額、非上場株式、保有目的が純投資目的である投資株式、提出会社
	TotalOfGainLossOnSaleEquitySecuritiesNotListedInvestmentEquitySecuritiesHeldForPureInvestmentReportingCompany = '' #売却損益の合計額、非上場株式、保有目的が純投資目的である投資株式、提出会社
	TotalOfValuationGainLossEquitySecuritiesNotListedInvestmentEquitySecuritiesHeldForPureInvestmentReportingCompany = '' #評価損益の合計額、非上場株式、保有目的が純投資目的である投資株式、提出会社
	EquitySecuritiesOtherThanThoseNotListedInvestmentEquitySecuritiesHeldForPureInvestmentReportingCompanyAbstract = '' #非上場株式以外の株式、保有目的が純投資目的である投資株式、提出会社 [タイトル項目]
	NumberOfIssuesSharesOtherThanThoseNotListedInvestmentSharesHeldForPureInvestmentReportingCompany = '' #銘柄数、非上場株式以外の株式、保有目的が純投資目的である投資株式、提出会社
	BookValueEquitySecuritiesOtherThanThoseNotListedInvestmentEquitySecuritiesHeldForPureInvestmentReportingCompany = '' #貸借対照表計上額の合計額、非上場株式以外の株式、保有目的が純投資目的である投資株式、提出会社
	TotalOfDividendsReceivedEquitySecuritiesOtherThanThoseNotListedInvestmentEquitySecuritiesHeldForPureInvestmentReportingCompany = '' #受取配当金の合計額、非上場株式以外の株式、保有目的が純投資目的である投資株式、提出会社
	TotalOfGainLossOnSaleEquitySecuritiesOtherThanThoseNotListedInvestmentEquitySecuritiesHeldForPureInvestmentReportingCompany = '' #売却損益の合計額、非上場株式以外の株式、保有目的が純投資目的である投資株式、提出会社
	TotalOfValuationGainLossEquitySecuritiesOtherThanThoseNotListedInvestmentEquitySecuritiesHeldForPureInvestmentReportingCompany = '' #評価損益の合計額、非上場株式以外の株式、保有目的が純投資目的である投資株式、提出会社
	ShareholdingsHeading = '' #株式の保有状況 [目次項目]
	ReportingCompanyEquitySecuritiesHeldAbstract = '' #提出会社、株式の保有状況 [タイトル項目]
	InvestmentEquitySecuritiesReclassifiedFromHeldForPureInvestmentToHeldForPurposesOtherThanPureInvestmentReportingCompanyTable = '' #投資株式の保有目的を純投資目的から純投資目的以外の目的に変更したもの、提出会社 [表]
	SequentialNumbersAxis = '' #連番 [軸]
	Row1Member = '' #1件目 [メンバー]
	Row2Member = '' #2件目 [メンバー]
	Row3Member = '' #3件目 [メンバー]
	InvestmentEquitySecuritiesReclassifiedFromHeldForPureInvestmentToHeldForPurposesOtherThanPureInvestmentReportingCompanyLineItems = '' #投資株式の保有目的を純投資目的から純投資目的以外の目的に変更したもの、提出会社 [表示項目]
	SecurityNameInvestmentEquitySecuritiesReclassifiedFromHeldForPureInvestmentToHeldForPurposesOtherThanPureInvestmentReportingCompany = '' #銘柄、投資株式の保有目的を純投資目的から純投資目的以外の目的に変更したもの、提出会社
	NumberOfSharesHeldInvestmentEquitySecuritiesReclassifiedFromHeldForPureInvestmentToHeldForPurposesOtherThanPureInvestmentReportingCompany = '' #株式数、投資株式の保有目的を純投資目的から純投資目的以外の目的に変更したもの、提出会社
	BookValueInvestmentEquitySecuritiesReclassifiedFromHeldForPureInvestmentToHeldForPurposesOtherThanPureInvestmentReportingCompany = '' #貸借対照表計上額、投資株式の保有目的を純投資目的から純投資目的以外の目的に変更したもの、提出会社
	ShareholdingsHeading = '' #株式の保有状況 [目次項目]
	ReportingCompanyEquitySecuritiesHeldAbstract = '' #提出会社、株式の保有状況 [タイトル項目]
	InvestmentEquitySecuritiesReclassifiedFromHeldForPurposesOtherThanPureInvestmentToHeldForPureInvestmentReportingCompanyTable = '' #投資株式の保有目的を純投資以外の目的から純投資目的に変更したもの、提出会社 [表]
	SequentialNumbersAxis = '' #連番 [軸]
	Row1Member = '' #1件目 [メンバー]
	Row2Member = '' #2件目 [メンバー]
	Row3Member = '' #3件目 [メンバー]
	InvestmentEquitySecuritiesReclassifiedFromHeldForPurposesOtherThanPureInvestmentToHeldForPureInvestmentReportingCompanyLineItems = '' #投資株式の保有目的を純投資以外の目的から純投資目的に変更したもの、提出会社 [表示項目]
	NameOfSecuritiesInvestmentEquitySecuritiesReclassifiedFromHeldForPurposesOtherThanPureInvestmentToHeldForPureInvestmentReportingCompany = '' #銘柄、投資株式の保有目的を純投資以外の目的から純投資目的に変更したもの、提出会社
	NumberOfSharesHeldInvestmentEquitySecuritiesReclassifiedFromHeldForPurposesOtherThanPureInvestmentToHeldForPureInvestmentReportingCompany = '' #株式数、投資株式の保有目的を純投資以外の目的から純投資目的に変更したもの、提出会社
	BookValueInvestmentEquitySecuritiesReclassifiedFromHeldForPurposesOtherThanPureInvestmentToHeldForPureInvestmentReportingCompany = '' #貸借対照表計上額、投資株式の保有目的を純投資以外の目的から純投資目的に変更したもの、提出会社
	ShareholdingsHeading = '' #株式の保有状況 [目次項目]
	GroupCompanyHoldingLargestAmountOfInvestmentEquitySecuritiesInGroupEquitySecuritiesHeldAbstract = '' #最大保有会社（提出会社でない場合）、株式の保有状況 [タイトル項目]
	InvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompanyAbstract = '' #保有目的が純投資目的以外の目的である投資株式、最大保有会社 [タイトル項目]
	SharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompanyAbstract = '' #非上場株式、保有目的が純投資目的以外の目的である投資株式、最大保有会社 [タイトル項目]
	NumberOfIssuesSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany = '' #銘柄数、非上場株式、保有目的が純投資目的以外の目的である投資株式、最大保有会社
	CarryingAmountSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany = '' #貸借対照表計上額、非上場株式、保有目的が純投資目的以外の目的である投資株式、最大保有会社
	NumberOfIssuesWhoseNumberOfSharesIncreasedSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany = '' #株式数が増加した銘柄数、非上場株式、保有目的が純投資目的以外の目的である投資株式、最大保有会社
	TotalAcquisitionCostForIncreasedSharesSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany = '' #株式数の増加に係る取得価額の合計額、非上場株式、保有目的が純投資目的以外の目的である投資株式、最大保有会社
	ReasonForIncreaseInNumberOfSharesSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany = '' #株式数が増加した理由、非上場株式、保有目的が純投資目的以外の目的である投資株式、最大保有会社
	NumberOfIssuesWhoseNumberOfSharesDecreasedSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany = '' #株式数が減少した銘柄数、非上場株式、保有目的が純投資目的以外の目的である投資株式、最大保有会社
	TotalSaleAmountForDecreasedSharesSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany = '' #株式数の減少に係る売却価額の合計額、非上場株式、保有目的が純投資目的以外の目的である投資株式、最大保有会社
	SharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompanyAbstract = '' #非上場株式以外の株式、保有目的が純投資目的以外の目的である投資株式、最大保有会社 [タイトル項目]
	NumberOfIssuesSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany = '' #銘柄数、非上場株式以外の株式、保有目的が純投資目的以外の目的である投資株式、最大保有会社
	CarryingAmountSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany = '' #貸借対照表計上額、非上場株式以外の株式、保有目的が純投資目的以外の目的である投資株式、最大保有会社
	NumberOfIssuesWhoseNumberOfSharesIncreasedSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany = '' #株式数が増加した銘柄数、非上場株式以外の株式、保有目的が純投資目的以外の目的である投資株式、最大保有会社
	TotalAcquisitionCostForIncreasedSharesSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany = '' #株式数の増加に係る取得価額の合計額、非上場株式以外の株式、保有目的が純投資目的以外の目的である投資株式、最大保有会社
	ReasonForIncreaseInNumberOfSharesSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany = '' #株式数が増加した理由、非上場株式以外の株式、保有目的が純投資目的以外の目的である投資株式、最大保有会社
	NumberOfIssuesWhoseNumberOfSharesDecreasedSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany = '' #株式数が減少した銘柄数、非上場株式以外の株式、保有目的が純投資目的以外の目的である投資株式、最大保有会社
	TotalSaleAmountForDecreasedSharesSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany = '' #株式数の減少に係る売却価額の合計額、非上場株式以外の株式、保有目的が純投資目的以外の目的である投資株式、最大保有会社
	ShareholdingsHeading = '' #株式の保有状況 [目次項目]
	GroupCompanyHoldingLargestAmountOfInvestmentEquitySecuritiesInGroupEquitySecuritiesHeldAbstract = '' #最大保有会社（提出会社でない場合）、株式の保有状況 [タイトル項目]
	DetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompanyTable = '' #保有目的が純投資目的以外の目的である特定投資株式の明細、最大保有会社 [表]
	SequentialNumbersAxis = '' #連番 [軸]
	Row1Member = '' #1件目 [メンバー]
	Row2Member = '' #2件目 [メンバー]
	Row3Member = '' #3件目 [メンバー]
	Row4Member = '' #4件目 [メンバー]
	Row5Member = '' #5件目 [メンバー]
	Row6Member = '' #6件目 [メンバー]
	Row7Member = '' #7件目 [メンバー]
	Row8Member = '' #8件目 [メンバー]
	Row9Member = '' #9件目 [メンバー]
	Row10Member = '' #10件目 [メンバー]
	Row11Member = '' #11件目 [メンバー]
	Row12Member = '' #12件目 [メンバー]
	Row13Member = '' #13件目 [メンバー]
	Row14Member = '' #14件目 [メンバー]
	Row15Member = '' #15件目 [メンバー]
	Row16Member = '' #16件目 [メンバー]
	Row17Member = '' #17件目 [メンバー]
	Row18Member = '' #18件目 [メンバー]
	Row19Member = '' #19件目 [メンバー]
	Row20Member = '' #20件目 [メンバー]
	Row21Member = '' #21件目 [メンバー]
	Row22Member = '' #22件目 [メンバー]
	Row23Member = '' #23件目 [メンバー]
	Row24Member = '' #24件目 [メンバー]
	Row25Member = '' #25件目 [メンバー]
	Row26Member = '' #26件目 [メンバー]
	Row27Member = '' #27件目 [メンバー]
	Row28Member = '' #28件目 [メンバー]
	Row29Member = '' #29件目 [メンバー]
	Row30Member = '' #30件目 [メンバー]
	Row31Member = '' #31件目 [メンバー]
	Row32Member = '' #32件目 [メンバー]
	Row33Member = '' #33件目 [メンバー]
	Row34Member = '' #34件目 [メンバー]
	Row35Member = '' #35件目 [メンバー]
	Row36Member = '' #36件目 [メンバー]
	Row37Member = '' #37件目 [メンバー]
	Row38Member = '' #38件目 [メンバー]
	Row39Member = '' #39件目 [メンバー]
	Row40Member = '' #40件目 [メンバー]
	Row41Member = '' #41件目 [メンバー]
	Row42Member = '' #42件目 [メンバー]
	Row43Member = '' #43件目 [メンバー]
	Row44Member = '' #44件目 [メンバー]
	Row45Member = '' #45件目 [メンバー]
	Row46Member = '' #46件目 [メンバー]
	Row47Member = '' #47件目 [メンバー]
	Row48Member = '' #48件目 [メンバー]
	Row49Member = '' #49件目 [メンバー]
	Row50Member = '' #50件目 [メンバー]
	Row51Member = '' #51件目 [メンバー]
	Row52Member = '' #52件目 [メンバー]
	Row53Member = '' #53件目 [メンバー]
	Row54Member = '' #54件目 [メンバー]
	Row55Member = '' #55件目 [メンバー]
	Row56Member = '' #56件目 [メンバー]
	Row57Member = '' #57件目 [メンバー]
	Row58Member = '' #58件目 [メンバー]
	Row59Member = '' #59件目 [メンバー]
	Row60Member = '' #60件目 [メンバー]
	DetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompanyLineItems = '' #保有目的が純投資目的以外の目的である特定投資株式の明細、最大保有会社 [表示項目]
	NameOfSecuritiesDetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany = '' #銘柄、保有目的が純投資目的以外の目的である特定投資株式の明細、最大保有会社
	NumberOfSharesHeldDetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany = '' #株式数、保有目的が純投資目的以外の目的である特定投資株式の明細、最大保有会社
	NumberOfSharesNotDisclosedAsBelowThresholdDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany = '' #株式数（記載省略）、保有目的が純投資目的以外の目的である特定投資株式の明細、最大保有会社
	BookValueDetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany = '' #貸借対照表計上額、保有目的が純投資目的以外の目的である特定投資株式の明細、最大保有会社
	CarryingAmountNotDisclosedAsBelowThresholdDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany = '' #貸借対照表計上額（記載省略）、保有目的が純投資目的以外の目的である特定投資株式の明細、最大保有会社
	PurposesOfHoldingDetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany = '' #保有目的、保有目的が純投資目的以外の目的である特定投資株式の明細、最大保有会社
	QuantitativeEffectsOfShareholdingDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany = '' #定量的な保有効果、保有目的が純投資目的以外の目的である特定投資株式の明細、最大保有会社
	ReasonForIncreaseInNumberOfSharesDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany = '' #株式数が増加した理由、保有目的が純投資目的以外の目的である特定投資株式の明細、最大保有会社
	PurposeOfShareholdingQuantitativeEffectsOfShareholdingAndReasonForIncreaseInNumberOfSharesDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany = '' #保有目的、定量的な保有効果及び株式数が増加した理由、保有目的が純投資目的以外の目的である特定投資株式の明細、最大保有会社
	WhetherIssuerOfAforementionedSharesHoldsReportingCompanysSharesDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany = '' #当該株式の発行者による提出会社の株式の保有の有無、保有目的が純投資目的以外の目的である特定投資株式の明細、最大保有会社
	ShareholdingsHeading = '' #株式の保有状況 [目次項目]
	GroupCompanyHoldingLargestAmountOfInvestmentEquitySecuritiesInGroupEquitySecuritiesHeldAbstract = '' #最大保有会社（提出会社でない場合）、株式の保有状況 [タイトル項目]
	DetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompanyTable = '' #保有目的が純投資目的以外の目的であるみなし保有株式の明細、最大保有会社 [表]
	SequentialNumbersAxis = '' #連番 [軸]
	Row1Member = '' #1件目 [メンバー]
	Row2Member = '' #2件目 [メンバー]
	Row3Member = '' #3件目 [メンバー]
	Row4Member = '' #4件目 [メンバー]
	Row5Member = '' #5件目 [メンバー]
	Row6Member = '' #6件目 [メンバー]
	Row7Member = '' #7件目 [メンバー]
	Row8Member = '' #8件目 [メンバー]
	Row9Member = '' #9件目 [メンバー]
	Row10Member = '' #10件目 [メンバー]
	DetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompanyLineItems = '' #保有目的が純投資目的以外の目的であるみなし保有株式の明細、最大保有会社 [表示項目]
	NameOfSecuritiesDetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany = '' #銘柄、保有目的が純投資目的以外の目的であるみなし保有株式の明細、最大保有会社
	NumberOfSharesHeldDetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany = '' #株式数、保有目的が純投資目的以外の目的であるみなし保有株式の明細、最大保有会社
	NumberOfSharesNotDisclosedAsBelowThresholdDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany = '' #株式数（記載省略）、保有目的が純投資目的以外の目的であるみなし保有株式の明細、最大保有会社
	BookValueDetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany = '' #貸借対照表計上額、保有目的が純投資目的以外の目的であるみなし保有株式の明細、最大保有会社
	CarryingAmountNotDisclosedAsBelowThresholdDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany = '' #貸借対照表計上額（記載省略）、保有目的が純投資目的以外の目的であるみなし保有株式の明細、最大保有会社
	PurposesOfHoldingDetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany = '' #保有目的、保有目的が純投資目的以外の目的であるみなし保有株式の明細、最大保有会社
	QuantitativeEffectsOfShareholdingDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany = '' #定量的な保有効果、保有目的が純投資目的以外の目的であるみなし保有株式の明細、最大保有会社
	ReasonForIncreaseInNumberOfSharesDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany = '' #株式数が増加した理由、保有目的が純投資目的以外の目的であるみなし保有株式の明細、最大保有会社
	PurposeOfShareholdingQuantitativeEffectsOfShareholdingAndReasonForIncreaseInNumberOfSharesDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany = '' #保有目的、定量的な保有効果及び株式数が増加した理由、保有目的が純投資目的以外の目的であるみなし保有株式の明細、最大保有会社
	WhetherIssuerOfAforementionedSharesHoldsReportingCompanysSharesDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany = '' #当該株式の発行者による提出会社の株式の保有の有無、保有目的が純投資目的以外の目的であるみなし保有株式の明細、最大保有会社
	ShareholdingsHeading = '' #株式の保有状況 [目次項目]
	GroupCompanyHoldingLargestAmountOfInvestmentEquitySecuritiesInGroupEquitySecuritiesHeldAbstract = '' #最大保有会社（提出会社でない場合）、株式の保有状況 [タイトル項目]
	InvestmentEquitySecuritiesHeldForPureInvestmentLargestHoldingCompanyAbstract = '' #保有目的が純投資目的である投資株式、最大保有会社 [タイトル項目]
	EquitySecuritiesNotListedInvestmentEquitySecuritiesHeldForPureInvestmentLargestHoldingCompanyAbstract = '' #非上場株式、保有目的が純投資目的である投資株式、最大保有会社 [タイトル項目]
	NumberOfIssuesSharesNotListedInvestmentSharesHeldForPureInvestmentLargestHoldingCompany = '' #銘柄数、非上場株式、保有目的が純投資目的である投資株式、最大保有会社
	BookValueEquitySecuritiesNotListedInvestmentEquitySecuritiesHeldForPureInvestmentLargestHoldingCompany = '' #貸借対照表計上額の合計額、非上場株式、保有目的が純投資目的である投資株式、最大保有会社
	TotalOfDividendsReceivedEquitySecuritiesNotListedInvestmentEquitySecuritiesHeldForPureInvestmentLargestHoldingCompany = '' #受取配当金の合計額、非上場株式、保有目的が純投資目的である投資株式、最大保有会社
	TotalOfGainLossOnSaleEquitySecuritiesNotListedInvestmentEquitySecuritiesHeldForPureInvestmentLargestHoldingCompany = '' #売却損益の合計額、非上場株式、保有目的が純投資目的である投資株式、最大保有会社
	TotalOfValuationGainLossEquitySecuritiesNotListedInvestmentEquitySecuritiesHeldForPureInvestmentLargestHoldingCompany = '' #評価損益の合計額、非上場株式、保有目的が純投資目的である投資株式、最大保有会社
	EquitySecuritiesOtherThanThoseNotListedInvestmentEquitySecuritiesHeldForPureInvestmentLargestHoldingCompanyAbstract = '' #非上場株式以外の株式、保有目的が純投資目的である投資株式、最大保有会社 [タイトル項目]
	NumberOfIssuesSharesOtherThanThoseNotListedInvestmentSharesHeldForPureInvestmentLargestHoldingCompany = '' #銘柄数、非上場株式以外の株式、保有目的が純投資目的である投資株式、最大保有会社
	BookValueEquitySecuritiesOtherThanThoseNotListedInvestmentEquitySecuritiesHeldForPureInvestmentLargestHoldingCompany = '' #貸借対照表計上額の合計額、非上場株式以外の株式、保有目的が純投資目的である投資株式、最大保有会社
	TotalOfDividendsReceivedEquitySecuritiesOtherThanThoseNotListedInvestmentEquitySecuritiesHeldForPureInvestmentLargestHoldingCompany = '' #受取配当金の合計額、非上場株式以外の株式、保有目的が純投資目的である投資株式、最大保有会社
	TotalOfGainLossOnSaleEquitySecuritiesOtherThanThoseNotListedInvestmentEquitySecuritiesHeldForPureInvestmentLargestHoldingCompany = '' #売却損益の合計額、非上場株式以外の株式、保有目的が純投資目的である投資株式、最大保有会社
	TotalOfValuationGainLossEquitySecuritiesOtherThanThoseNotListedInvestmentEquitySecuritiesHeldForPureInvestmentLargestHoldingCompany = '' #評価損益の合計額、非上場株式以外の株式、保有目的が純投資目的である投資株式、最大保有会社
	ShareholdingsHeading = '' #株式の保有状況 [目次項目]
	GroupCompanyHoldingLargestAmountOfInvestmentEquitySecuritiesInGroupEquitySecuritiesHeldAbstract = '' #最大保有会社（提出会社でない場合）、株式の保有状況 [タイトル項目]
	InvestmentEquitySecuritiesReclassifiedFromHeldForPureInvestmentToHeldForPurposesOtherThanPureInvestmentLargestHoldingCompanyTable = '' #投資株式の保有目的を純投資目的から純投資目的以外の目的に変更したもの、最大保有会社 [表]
	SequentialNumbersAxis = '' #連番 [軸]
	Row1Member = '' #1件目 [メンバー]
	Row2Member = '' #2件目 [メンバー]
	Row3Member = '' #3件目 [メンバー]
	InvestmentEquitySecuritiesReclassifiedFromHeldForPureInvestmentToHeldForPurposesOtherThanPureInvestmentLargestHoldingCompanyLineItems = '' #投資株式の保有目的を純投資目的から純投資目的以外の目的に変更したもの、最大保有会社 [表示項目]
	NameOfSecuritiesInvestmentEquitySecuritiesReclassifiedFromHeldForPureInvestmentToHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany = '' #銘柄、投資株式の保有目的を純投資目的から純投資目的以外の目的に変更したもの、最大保有会社
	NumberOfSharesHeldInvestmentEquitySecuritiesReclassifiedFromHeldForPureInvestmentToHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany = '' #株式数、投資株式の保有目的を純投資目的から純投資目的以外の目的に変更したもの、最大保有会社
	BookValueInvestmentEquitySecuritiesReclassifiedFromHeldForPureInvestmentToHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany = '' #貸借対照表計上額、投資株式の保有目的を純投資目的から純投資目的以外の目的に変更したもの、最大保有会社
	ShareholdingsHeading = '' #株式の保有状況 [目次項目]
	GroupCompanyHoldingLargestAmountOfInvestmentEquitySecuritiesInGroupEquitySecuritiesHeldAbstract = '' #最大保有会社（提出会社でない場合）、株式の保有状況 [タイトル項目]
	InvestmentEquitySecuritiesReclassifiedFromHeldForPurposesOtherThanPureInvestmentToHeldForPureInvestmentLargestHoldingCompanyTable = '' #投資株式の保有目的を純投資以外の目的から純投資目的に変更したもの、最大保有会社 [表]
	SequentialNumbersAxis = '' #連番 [軸]
	Row1Member = '' #1件目 [メンバー]
	Row2Member = '' #2件目 [メンバー]
	Row3Member = '' #3件目 [メンバー]
	InvestmentEquitySecuritiesReclassifiedFromHeldForPurposesOtherThanPureInvestmentToHeldForPureInvestmentLargestHoldingCompanyLineItems = '' #投資株式の保有目的を純投資以外の目的から純投資目的に変更したもの、最大保有会社 [表示項目]
	NameOfSecuritiesInvestmentEquitySecuritiesReclassifiedFromHeldForPurposesOtherThanPureInvestmentToHeldForPureInvestmentLargestHoldingCompany = '' #銘柄、投資株式の保有目的を純投資以外の目的から純投資目的に変更したもの、最大保有会社
	NumberOfSharesHeldInvestmentEquitySecuritiesReclassifiedFromHeldForPurposesOtherThanPureInvestmentToHeldForPureInvestmentLargestHoldingCompany = '' #株式数、投資株式の保有目的を純投資以外の目的から純投資目的に変更したもの、最大保有会社
	BookValueInvestmentEquitySecuritiesReclassifiedFromHeldForPurposesOtherThanPureInvestmentToHeldForPureInvestmentLargestHoldingCompany = '' #貸借対照表計上額、投資株式の保有目的を純投資以外の目的から純投資目的に変更したもの、最大保有会社
	ShareholdingsHeading = '' #株式の保有状況 [目次項目]
	GroupCompanyHoldingSecondLargestAmountOfInvestmentEquitySecuritiesInGroupEquitySecuritiesHeldAbstract = '' #投資株式計上額が次に大きい会社（提出会社でない場合）、株式の保有状況 [タイトル項目]
	InvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompanyAbstract = '' #保有目的が純投資目的以外の目的である投資株式、投資株式計上額が次に大きい会社 [タイトル項目]
	SharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompanyAbstract = '' #非上場株式、保有目的が純投資目的以外の目的である投資株式、投資株式計上額が次に大きい会社 [タイトル項目]
	NumberOfIssuesSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany = '' #銘柄数、非上場株式、保有目的が純投資目的以外の目的である投資株式、投資株式計上額が次に大きい会社
	CarryingAmountSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany = '' #貸借対照表計上額、非上場株式、保有目的が純投資目的以外の目的である投資株式、投資株式計上額が次に大きい会社
	NumberOfIssuesWhoseNumberOfSharesIncreasedSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany = '' #株式数が増加した銘柄数、非上場株式、保有目的が純投資目的以外の目的である投資株式、投資株式計上額が次に大きい会社
	TotalAcquisitionCostForIncreasedSharesSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany = '' #株式数の増加に係る取得価額の合計額、非上場株式、保有目的が純投資目的以外の目的である投資株式、投資株式計上額が次に大きい会社
	ReasonForIncreaseInNumberOfSharesSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany = '' #株式数が増加した理由、非上場株式、保有目的が純投資目的以外の目的である投資株式、投資株式計上額が次に大きい会社
	NumberOfIssuesWhoseNumberOfSharesDecreasedSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany = '' #株式数が減少した銘柄数、非上場株式、保有目的が純投資目的以外の目的である投資株式、投資株式計上額が次に大きい会社
	TotalSaleAmountForDecreasedSharesSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany = '' #株式数の減少に係る売却価額の合計額、非上場株式、保有目的が純投資目的以外の目的である投資株式、投資株式計上額が次に大きい会社
	SharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompanyAbstract = '' #非上場株式以外の株式、保有目的が純投資目的以外の目的である投資株式、投資株式計上額が次に大きい会社 [タイトル項目]
	NumberOfIssuesSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany = '' #銘柄数、非上場株式以外の株式、保有目的が純投資目的以外の目的である投資株式、投資株式計上額が次に大きい会社
	CarryingAmountSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany = '' #貸借対照表計上額、非上場株式以外の株式、保有目的が純投資目的以外の目的である投資株式、投資株式計上額が次に大きい会社
	NumberOfIssuesWhoseNumberOfSharesIncreasedSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany = '' #株式数が増加した銘柄数、非上場株式以外の株式、保有目的が純投資目的以外の目的である投資株式、投資株式計上額が次に大きい会社
	TotalAcquisitionCostForIncreasedSharesSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany = '' #株式数の増加に係る取得価額の合計額、非上場株式以外の株式、保有目的が純投資目的以外の目的である投資株式、投資株式計上額が次に大きい会社
	ReasonForIncreaseInNumberOfSharesSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany = '' #株式数が増加した理由、非上場株式以外の株式、保有目的が純投資目的以外の目的である投資株式、投資株式計上額が次に大きい会社
	NumberOfIssuesWhoseNumberOfSharesDecreasedSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany = '' #株式数が減少した銘柄数、非上場株式以外の株式、保有目的が純投資目的以外の目的である投資株式、投資株式計上額が次に大きい会社
	TotalSaleAmountForDecreasedSharesSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany = '' #株式数の減少に係る売却価額の合計額、非上場株式以外の株式、保有目的が純投資目的以外の目的である投資株式、投資株式計上額が次に大きい会社
	ShareholdingsHeading = '' #株式の保有状況 [目次項目]
	GroupCompanyHoldingSecondLargestAmountOfInvestmentEquitySecuritiesInGroupEquitySecuritiesHeldAbstract = '' #投資株式計上額が次に大きい会社（提出会社でない場合）、株式の保有状況 [タイトル項目]
	DetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompanyTable = '' #保有目的が純投資目的以外の目的である特定投資株式の明細、投資株式計上額が次に大きい会社 [表]
	SequentialNumbersAxis = '' #連番 [軸]
	Row1Member = '' #1件目 [メンバー]
	Row2Member = '' #2件目 [メンバー]
	Row3Member = '' #3件目 [メンバー]
	Row4Member = '' #4件目 [メンバー]
	Row5Member = '' #5件目 [メンバー]
	Row6Member = '' #6件目 [メンバー]
	Row7Member = '' #7件目 [メンバー]
	Row8Member = '' #8件目 [メンバー]
	Row9Member = '' #9件目 [メンバー]
	Row10Member = '' #10件目 [メンバー]
	DetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompanyLineItems = '' #保有目的が純投資目的以外の目的である特定投資株式の明細、投資株式計上額が次に大きい会社 [表示項目]
	NameOfSecuritiesDetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany = '' #銘柄、保有目的が純投資目的以外の目的である特定投資株式の明細、投資株式計上額が次に大きい会社
	NumberOfSharesHeldDetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany = '' #株式数、保有目的が純投資目的以外の目的である特定投資株式の明細、投資株式計上額が次に大きい会社
	NumberOfSharesNotDisclosedAsBelowThresholdDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany = '' #株式数（記載省略）、保有目的が純投資目的以外の目的である特定投資株式の明細、投資株式計上額が次に大きい会社
	BookValueDetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany = '' #貸借対照表計上額、保有目的が純投資目的以外の目的である特定投資株式の明細、投資株式計上額が次に大きい会社
	CarryingAmountNotDisclosedAsBelowThresholdDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany = '' #貸借対照表計上額（記載省略）、保有目的が純投資目的以外の目的である特定投資株式の明細、投資株式計上額が次に大きい会社
	PurposesOfHoldingDetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany = '' #保有目的、保有目的が純投資目的以外の目的である特定投資株式の明細、投資株式計上額が次に大きい会社
	QuantitativeEffectsOfShareholdingDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany = '' #定量的な保有効果、保有目的が純投資目的以外の目的である特定投資株式の明細、投資株式計上額が次に大きい会社
	ReasonForIncreaseInNumberOfSharesDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany = '' #株式数が増加した理由、保有目的が純投資目的以外の目的である特定投資株式の明細、投資株式計上額が次に大きい会社
	PurposeOfShareholdingQuantitativeEffectsOfShareholdingAndReasonForIncreaseInNumberOfSharesDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany = '' #保有目的、定量的な保有効果及び株式数が増加した理由、保有目的が純投資目的以外の目的である特定投資株式の明細、投資株式計上額が次に大きい会社
	WhetherIssuerOfAforementionedSharesHoldsReportingCompanysSharesDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany = '' #当該株式の発行者による提出会社の株式の保有の有無、保有目的が純投資目的以外の目的である特定投資株式の明細、投資株式計上額が次に大きい会社
	ShareholdingsHeading = '' #株式の保有状況 [目次項目]
	GroupCompanyHoldingSecondLargestAmountOfInvestmentEquitySecuritiesInGroupEquitySecuritiesHeldAbstract = '' #投資株式計上額が次に大きい会社（提出会社でない場合）、株式の保有状況 [タイトル項目]
	DetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompanyTable = '' #保有目的が純投資目的以外の目的であるみなし保有株式の明細、投資株式計上額が次に大きい会社 [表]
	SequentialNumbersAxis = '' #連番 [軸]
	Row1Member = '' #1件目 [メンバー]
	Row2Member = '' #2件目 [メンバー]
	Row3Member = '' #3件目 [メンバー]
	Row4Member = '' #4件目 [メンバー]
	Row5Member = '' #5件目 [メンバー]
	Row6Member = '' #6件目 [メンバー]
	Row7Member = '' #7件目 [メンバー]
	Row8Member = '' #8件目 [メンバー]
	Row9Member = '' #9件目 [メンバー]
	Row10Member = '' #10件目 [メンバー]
	DetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompanyLineItems = '' #保有目的が純投資目的以外の目的であるみなし保有株式の明細、投資株式計上額が次に大きい会社 [表示項目]
	NameOfSecuritiesDetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany = '' #銘柄、保有目的が純投資目的以外の目的であるみなし保有株式の明細、投資株式計上額が次に大きい会社
	NumberOfSharesHeldDetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany = '' #株式数、保有目的が純投資目的以外の目的であるみなし保有株式の明細、投資株式計上額が次に大きい会社
	NumberOfSharesNotDisclosedAsBelowThresholdDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany = '' #株式数（記載省略）、保有目的が純投資目的以外の目的であるみなし保有株式の明細、投資株式計上額が次に大きい会社
	BookValueDetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany = '' #貸借対照表計上額、保有目的が純投資目的以外の目的であるみなし保有株式の明細、投資株式計上額が次に大きい会社
	CarryingAmountNotDisclosedAsBelowThresholdDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany = '' #貸借対照表計上額（記載省略）、保有目的が純投資目的以外の目的であるみなし保有株式の明細、投資株式計上額が次に大きい会社
	PurposesOfHoldingDetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany = '' #保有目的、保有目的が純投資目的以外の目的であるみなし保有株式の明細、投資株式計上額が次に大きい会社
	QuantitativeEffectsOfShareholdingDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany = '' #定量的な保有効果、保有目的が純投資目的以外の目的であるみなし保有株式の明細、投資株式計上額が次に大きい会社
	ReasonForIncreaseInNumberOfSharesDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany = '' #株式数が増加した理由、保有目的が純投資目的以外の目的であるみなし保有株式の明細、投資株式計上額が次に大きい会社
	PurposeOfShareholdingQuantitativeEffectsOfShareholdingAndReasonForIncreaseInNumberOfSharesDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany = '' #保有目的、定量的な保有効果及び株式数が増加した理由、保有目的が純投資目的以外の目的であるみなし保有株式の明細、投資株式計上額が次に大きい会社
	WhetherIssuerOfAforementionedSharesHoldsReportingCompanysSharesDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany = '' #当該株式の発行者による提出会社の株式の保有の有無、保有目的が純投資目的以外の目的であるみなし保有株式の明細、投資株式計上額が次に大きい会社
	ShareholdingsHeading = '' #株式の保有状況 [目次項目]
	GroupCompanyHoldingSecondLargestAmountOfInvestmentEquitySecuritiesInGroupEquitySecuritiesHeldAbstract = '' #投資株式計上額が次に大きい会社（提出会社でない場合）、株式の保有状況 [タイトル項目]
	InvestmentEquitySecuritiesHeldForPureInvestmentSecondLargestHoldingCompanyAbstract = '' #保有目的が純投資目的である投資株式、投資株式計上額が次に大きい会社 [タイトル項目]
	EquitySecuritiesNotListedInvestmentEquitySecuritiesHeldForPureInvestmentSecondLargestHoldingCompanyAbstract = '' #非上場株式、保有目的が純投資目的である投資株式、投資株式計上額が次に大きい会社 [タイトル項目]
	NumberOfIssuesSharesNotListedInvestmentSharesHeldForPureInvestmentSecondLargestHoldingCompany = '' #銘柄数、非上場株式、保有目的が純投資目的である投資株式、投資株式計上額が次に大きい会社
	BookValueEquitySecuritiesNotListedInvestmentEquitySecuritiesHeldForPureInvestmentSecondLargestHoldingCompany = '' #貸借対照表計上額の合計額、非上場株式、保有目的が純投資目的である投資株式、投資株式計上額が次に大きい会社
	TotalOfDividendsReceivedEquitySecuritiesNotListedInvestmentEquitySecuritiesHeldForPureInvestmentSecondLargestHoldingCompany = '' #受取配当金の合計額、非上場株式、保有目的が純投資目的である投資株式、投資株式計上額が次に大きい会社
	TotalOfGainLossOnSaleEquitySecuritiesNotListedInvestmentEquitySecuritiesHeldForPureInvestmentSecondLargestHoldingCompany = '' #売却損益の合計額、非上場株式、保有目的が純投資目的である投資株式、投資株式計上額が次に大きい会社
	TotalOfValuationGainLossEquitySecuritiesNotListedInvestmentEquitySecuritiesHeldForPureInvestmentSecondLargestHoldingCompany = '' #評価損益の合計額、非上場株式、保有目的が純投資目的である投資株式、投資株式計上額が次に大きい会社
	EquitySecuritiesOtherThanThoseNotListedInvestmentEquitySecuritiesHeldForPureInvestmentSecondLargestHoldingCompanyAbstract = '' #非上場株式以外の株式、保有目的が純投資目的である投資株式、投資株式計上額が次に大きい会社 [タイトル項目]
	NumberOfIssuesSharesOtherThanThoseNotListedInvestmentSharesHeldForPureInvestmentSecondLargestHoldingCompany = '' #銘柄数、非上場株式以外の株式、保有目的が純投資目的である投資株式、投資株式計上額が次に大きい会社
	BookValueEquitySecuritiesOtherThanThoseNotListedInvestmentEquitySecuritiesHeldForPureInvestmentSecondLargestHoldingCompany = '' #貸借対照表計上額の合計額、非上場株式以外の株式、保有目的が純投資目的である投資株式、投資株式計上額が次に大きい会社
	TotalOfDividendsReceivedEquitySecuritiesOtherThanThoseNotListedInvestmentEquitySecuritiesHeldForPureInvestmentSecondLargestHoldingCompany = '' #受取配当金の合計額、非上場株式以外の株式、保有目的が純投資目的である投資株式、投資株式計上額が次に大きい会社
	TotalOfGainLossOnSaleEquitySecuritiesOtherThanThoseNotListedInvestmentEquitySecuritiesHeldForPureInvestmentSecondLargestHoldingCompany = '' #売却損益の合計額、非上場株式以外の株式、保有目的が純投資目的である投資株式、投資株式計上額が次に大きい会社
	TotalOfValuationGainLossEquitySecuritiesOtherThanThoseNotListedInvestmentEquitySecuritiesHeldForPureInvestmentSecondLargestHoldingCompany = '' #評価損益の合計額、非上場株式以外の株式、保有目的が純投資目的である投資株式、投資株式計上額が次に大きい会社
	ShareholdingsHeading = '' #株式の保有状況 [目次項目]
	GroupCompanyHoldingSecondLargestAmountOfInvestmentEquitySecuritiesInGroupEquitySecuritiesHeldAbstract = '' #投資株式計上額が次に大きい会社（提出会社でない場合）、株式の保有状況 [タイトル項目]
	InvestmentEquitySecuritiesReclassifiedFromHeldForPureInvestmentToHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompanyTable = '' #投資株式の保有目的を純投資目的から純投資目的以外の目的に変更したもの、投資株式計上額が次に大きい会社 [表]
	SequentialNumbersAxis = '' #連番 [軸]
	Row1Member = '' #1件目 [メンバー]
	Row2Member = '' #2件目 [メンバー]
	Row3Member = '' #3件目 [メンバー]
	InvestmentEquitySecuritiesReclassifiedFromHeldForPureInvestmentToHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompanyLineItems = '' #投資株式の保有目的を純投資目的から純投資目的以外の目的に変更したもの、投資株式計上額が次に大きい会社 [表示項目]
	NameOfSecuritiesInvestmentEquitySecuritiesReclassifiedFromHeldForPureInvestmentToHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany = '' #銘柄、投資株式の保有目的を純投資目的から純投資目的以外の目的に変更したもの、投資株式計上額が次に大きい会社
	NumberOfSharesHeldInvestmentEquitySecuritiesReclassifiedFromHeldForPureInvestmentToHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany = '' #株式数、投資株式の保有目的を純投資目的から純投資目的以外の目的に変更したもの、投資株式計上額が次に大きい会社
	BookValueInvestmentEquitySecuritiesReclassifiedFromHeldForPureInvestmentToHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany = '' #貸借対照表計上額、投資株式の保有目的を純投資目的から純投資目的以外の目的に変更したもの、投資株式計上額が次に大きい会社
	ShareholdingsHeading = '' #株式の保有状況 [目次項目]
	GroupCompanyHoldingSecondLargestAmountOfInvestmentEquitySecuritiesInGroupEquitySecuritiesHeldAbstract = '' #投資株式計上額が次に大きい会社（提出会社でない場合）、株式の保有状況 [タイトル項目]
	InvestmentEquitySecuritiesReclassifiedFromHeldForPurposesOtherThanPureInvestmentToHeldForPureInvestmentSecondLargestHoldingCompanyTable = '' #投資株式の保有目的を純投資以外の目的から純投資目的に変更したもの、投資株式計上額が次に大きい会社 [表]
	SequentialNumbersAxis = '' #連番 [軸]
	Row1Member = '' #1件目 [メンバー]
	Row2Member = '' #2件目 [メンバー]
	Row3Member = '' #3件目 [メンバー]
	InvestmentEquitySecuritiesReclassifiedFromHeldForPurposesOtherThanPureInvestmentToHeldForPureInvestmentSecondLargestHoldingCompanyLineItems = '' #投資株式の保有目的を純投資以外の目的から純投資目的に変更したもの、投資株式計上額が次に大きい会社 [表示項目]
	NameOfSecuritiesInvestmentEquitySecuritiesReclassifiedFromHeldForPurposesOtherThanPureInvestmentToHeldForPureInvestmentSecondLargestHoldingCompany = '' #銘柄、投資株式の保有目的を純投資以外の目的から純投資目的に変更したもの、投資株式計上額が次に大きい会社
	NumberOfSharesHeldInvestmentEquitySecuritiesReclassifiedFromHeldForPurposesOtherThanPureInvestmentToHeldForPureInvestmentSecondLargestHoldingCompany = '' #株式数、投資株式の保有目的を純投資以外の目的から純投資目的に変更したもの、投資株式計上額が次に大きい会社
	BookValueInvestmentEquitySecuritiesReclassifiedFromHeldForPurposesOtherThanPureInvestmentToHeldForPureInvestmentSecondLargestHoldingCompany = '' #貸借対照表計上額、投資株式の保有目的を純投資以外の目的から純投資目的に変更したもの、投資株式計上額が次に大きい会社
	NameOfGroupCompanyHoldingLargestAmountOfInvestmentSharesInGroup = '' #最大保有会社（提出会社でない場合）の名称
	NameOfGroupCompanyHoldingSecondLargestAmountOfInvestmentSharesInGroup = '' #投資株式計上額が次に大きい会社（提出会社でない場合）の名称
	FinancialInformationHeading = '' #経理の状況 [目次項目]
	FinancialInformationHeading = '' #経理の状況 [目次項目]
	RegulationsInAccordanceWithWhichConsolidatedFinancialStatementsHaveBeenPreparedFinancialInformation = '' #連結財務諸表が基づく規則、経理の状況
	RegulationsInAccordanceWithWhichFinancialStatementsHaveBeenPreparedFinancialInformation = '' #財務諸表が基づく規則、経理の状況
	DescriptionOfFactThatCompanyEngagesSpecifiedBusinessAndHasPreparedItsSemiAnnualConsolidatedFinancialStatementsFinancialInformation = '' #特定事業会社であり、中間連結財務諸表等を作成した場合の記載、経理の状況
	DescriptionOfFactThatConsolidatedFinancialStatementsHaveBeenPreparedInAccordanceWithSpecialOrdinanceOrRegulationsForIndustryInAppendedListFinancialInformation = '' #連結財務諸表が別記事業の特別の法令若しくは準則に基づく場合の記載、経理の状況
	DescriptionOfFactThatFinancialStatementsHaveBeenPreparedInAccordanceWithSpecialOrdinanceOrRegulationsForIndustryInAppendedListFinancialInformation = '' #財務諸表が別記事業の特別の法令若しくは準則に基づく場合の記載、経理の状況
	DescriptionOfFactThatConsolidatedFinancialStatementsHaveBeenPreparedInAccordanceWithIFRSFinancialInformation = '' #指定国際会計基準により連結財務諸表を作成した場合の記載、経理の状況
	DescriptionOfFactThatConsolidatedFinancialStatementsHaveBeenPreparedInAccordanceWithJMISFinancialInformation = '' #修正国際基準により連結財務諸表を作成した場合の記載、経理の状況
	DescriptionOfFactThatConsolidatedFinancialStatementsHaveBeenPreparedInAccordanceWithUSGAAPFinancialInformation = '' #米国会計基準により連結財務諸表を作成した場合の記載、経理の状況
	DescriptionOfFactThatConsolidatedFinancialStatementsHaveNotBeenPreparedFinancialInformation = '' #連結財務諸表を作成していない場合の記載、経理の状況
	DescriptionOfFactThatConsolidatedFinancialStatementsHaveNotBeenPreparedAndFinancialStatementsHaveBeenPreparedInAccordanceWithIFRSFinancialInformation = '' #連結財務諸表を作成していない場合で指定国際会計基準により財務諸表を作成する場合の記載、経理の状況
	DescriptionOfFactThatFinancialStatementsHaveBeenPreparedInAccordanceWithSpecialProvisionFinancialInformation = '' #特例財務諸表を作成する場合の記載、経理の状況
	DescriptionOfFactThatQuarterlySecuritiesReportForFirstQuarterOrThirdQuarterPresentsStatementOfCashFlowsFinancialInformation = '' #第１四半期又は第３四半期に係る四半期報告書において四半期キャッシュ・フロー計算書を記載する場合の記載、経理の状況
	DescriptionOfFactThatQuarterlySecuritiesReportForFirstQuarterOrThirdQuarterPresentsConsolidatedStatementOfCashFlowsFinancialInformation = '' #第１四半期又は第３四半期に係る四半期報告書において四半期連結キャッシュ・フロー計算書を記載する場合の記載、経理の状況
	DescriptionOfFactThatQuarterlySecuritiesReportPresentsQuarterPeriodStatementOfIncomeFinancialInformation = '' #四半期報告書において四半期会計期間に係る四半期損益計算書を記載する場合の記載、経理の状況
	DescriptionOfFactThatQuarterlySecuritiesReportPresentsQuarterPeriodConsolidatedStatementOfComprehensiveIncomeFinancialInformation = '' #四半期報告書において四半期連結会計期間に係る四半期連結損益計算書及び四半期連結包括利益計算書又は四半期連結損益及び包括利益計算書を記載する場合の記載、経理の状況
	RemarkableEffortsToEnsureFairPresentationOfConsolidatedFinancialStatementsEtcFinancialInformation = '' #連結財務諸表等の適正性を確保するための特段の取組み、経理の状況
	RemarkableEffortsToEnsureFairPresentationOfConsolidatedFinancialStatementsEtcInAccordanceWithIFRSFinancialInformation = '' #指定国際会計基準に基づいて連結財務諸表等を適正に作成することができる体制、経理の状況
	RemarkableEffortsToEnsureFairPresentationOfConsolidatedFinancialStatementsEtcAndInternalSystemToPrepareConsolidatedFinancialStatementsEtcFairlyInAccordanceWithIFRSFinancialInformation = '' #連結財務諸表等の適正性を確保するための特段の取組み及び指定国際会計基準に基づいて連結財務諸表等を適正に作成することができる体制、経理の状況
	RemarkableEffortsToEnsureFairPresentationOfConsolidatedFinancialStatementsEtcInAccordanceWithJMISFinancialInformation = '' #修正国際基準に基づいて連結財務諸表等を適正に作成することができる体制、経理の状況
	NoteOnIndependentAuditFinancialInformation = '' #監査証明について、経理の状況
	NoteOnChangeOfIndependentAuditorsFinancialInformation = '' #監査人の交代、経理の状況
	NoteOnChangeInFiscalYearEndsFinancialInformation = '' #決算期変更について、経理の状況
	ConsolidatedFinancialStatementsEtcHeading = '' #連結財務諸表等 [目次項目]
	ConsolidatedFinancialStatementsHeading = '' #連結財務諸表 [目次項目]
	ConsolidatedBalanceSheetHeading = '' #連結貸借対照表 [目次項目]
	ConsolidatedBalanceSheetTextBlock = '' #連結貸借対照表 [テキストブロック]
	ConsolidatedStatementOfFinancialPositionJMISTextBlock = '' #連結財政状態計算書（JMIS） [テキストブロック]
	ConsolidatedBalanceSheetUSGAAPTextBlock = '' #連結貸借対照表 （US GAAP） [テキストブロック]
	ConsolidatedStatementOfIncomeAndConsolidatedStatementOfComprehensiveIncomeHeading = '' #連結損益計算書及び連結包括利益計算書 [目次項目]
	ConsolidatedStatementOfIncomeHeading = '' #連結損益計算書 [目次項目]
	ConsolidatedStatementOfIncomeTextBlock = '' #連結損益計算書 [テキストブロック]
	ConsolidatedStatementOfIncomeJMISTextBlock = '' #連結損益計算書（JMIS） [テキストブロック]
	ConsolidatedStatementOfIncomeUSGAAPTextBlock = '' #連結損益計算書（US GAAP） [テキストブロック]
	ConsolidatedStatementOfComprehensiveIncomeHeading = '' #連結包括利益計算書 [目次項目]
	ConsolidatedStatementOfComprehensiveIncomeTextBlock = '' #連結包括利益計算書 [テキストブロック]
	ConsolidatedStatementOfComprehensiveIncomeJMISTextBlock = '' #連結包括利益計算書（2計算書）（JMIS） [テキストブロック]
	ConsolidatedStatementOfComprehensiveIncomeUSGAAPTextBlock = '' #連結包括利益計算書（US GAAP） [テキストブロック]
	ConsolidatedStatementOfComprehensiveIncomeSingleStatementHeading = '' #連結損益及び包括利益計算書 [目次項目]
	ConsolidatedStatementOfComprehensiveIncomeSingleStatementTextBlock = '' #連結損益及び包括利益計算書 [テキストブロック]
	ConsolidatedStatementOfComprehensiveIncomeSingleStatementJMISTextBlock = '' #連結包括利益計算書（１計算書）（JMIS） [テキストブロック]
	ConsolidatedStatementOfComprehensiveIncomeSingleStatementUSGAAPTextBlock = '' #連結損益及び包括利益計算書（US GAAP） [テキストブロック]
	ConsolidatedStatementOfChangesInEquityHeading = '' #連結株主資本等変動計算書 [目次項目]
	ConsolidatedStatementOfChangesInEquityTextBlock = '' #連結株主資本等変動計算書 [テキストブロック]
	ConsolidatedStatementOfChangesInEquityJMISTextBlock = '' #連結持分変動計算書（JMIS） [テキストブロック]
	ConsolidatedStatementOfEquityUSGAAPTextBlock = '' #連結資本勘定計算書（US GAAP） [テキストブロック]
	ConsolidatedStatementOfCashFlowsHeading = '' #連結キャッシュ・フロー計算書 [目次項目]
	ConsolidatedStatementOfCashFlowsTextBlock = '' #連結キャッシュ・フロー計算書 [テキストブロック]
	ConsolidatedStatementOfCashFlowsJMISTextBlock = '' #連結キャッシュ・フロー計算書（JMIS） [テキストブロック]
	ConsolidatedStatementOfCashFlowsUSGAAPTextBlock = '' #連結キャッシュ・フロー計算書（US GAAP） [テキストブロック]
	NotesConsolidatedFinancialStatementsHeading = '' #注記事項、連結財務諸表 [目次項目]
	NotesUncertaintiesOfEntitysAbilityToContinueAsGoingConcernConsolidatedFinancialStatementsHeading = '' #継続企業の前提に関する事項、連結財務諸表 [目次項目]
	NotesUncertaintiesOfEntitysAbilityToContinueAsGoingConcernConsolidatedFinancialStatementsTextBlock = '' #継続企業の前提に関する事項、連結財務諸表 [テキストブロック]
	NotesSignificantAccountingPoliciesForPreparationOfConsolidatedFinancialStatementsHeading = '' #連結財務諸表作成のための基本となる重要な事項 [目次項目]
	NotesSignificantAccountingPoliciesForPreparationOfConsolidatedFinancialStatementsTextBlock = '' #連結財務諸表作成のための基本となる重要な事項 [テキストブロック]
	NotesSignificantAccountingPoliciesForPreparationOfConsolidatedFinancialStatementsHeading = '' #連結財務諸表作成のための基本となる重要な事項 [目次項目]
	NotesSignificantAccountingPoliciesForPreparationOfConsolidatedFinancialStatementsTable = '' #連結財務諸表作成のための基本となる重要な事項 [表]
	ConsolidatedOrNonConsolidatedAxis = '' #連結個別 [軸]
	ConsolidatedMember = '' #連結 [メンバー] ※ディメンションデフォルト
	NotesSignificantAccountingPoliciesForPreparationOfConsolidatedFinancialStatementsLineItems = '' #連結財務諸表作成のための基本となる重要な事項 [表示項目]
	DisclosureOfScopeOfConsolidationAbstract = '' #連結の範囲に関する事項 [タイトル項目]
	NumberOfConsolidatedSubsidiariesAndNamesOfMajorConsolidatedSubsidiariesTextBlock = '' #連結子会社の数及び主要な連結子会社の名称 [テキストブロック]
	NumberOfConsolidatedSubsidiaries = '' #連結子会社の数
	ChangesInScopeOfConsolidationTextBlock = '' #連結の範囲の変更 [テキストブロック]
	NamesOfMajorUnconsolidatedSubsidiariesAndReasonsForExclusionFromScopeOfConsolidationTextBlock = '' #主要な非連結子会社の名称及び連結の範囲から除いた理由 [テキストブロック]
	NamesOfCompaniesEtcAndReasonsForNotBeingDeemedAsSubsidiariesEvenThoughMoreThanHalfOfVotingRightsAreOwnedByReportingCompanyTextBlock = '' #他の会社等の議決権の過半数を自己の計算において所有しているにもかかわらず当該他の会社等を子会社としなかった場合には、当該他の会社等の名称及び子会社としなかった理由 [テキストブロック]
	SummaryOfSpecialPurposeEntitiesSubjectToDisclosureOverviewAndAmountsOfTransactionsWithSuchEntitiesAndOtherRelevantMaterialInformationTextBlock = '' #開示対象特別目的会社の概要、開示対象特別目的会社との取引の概要及び取引金額その他の重要な事項 [テキストブロック]
	DisclosureAboutApplicationOfEquityMethodAbstract = '' #持分法の適用に関する事項 [タイトル項目]
	NumberOfUnconsolidatedSubsidiariesAndAssociatesAccountedForUsingEquityMethodAndNamesOfMajorEntitiesAccountedForUsingEquityMethodTextBlock = '' #持分法を適用した非連結子会社又は関連会社の数及びこれらのうち主要な会社等の名称 [テキストブロック]
	NumberOfUnconsolidatedSubsidiariesAndAssociatesAccountedForUsingEquityMethod = '' #持分法を適用した非連結子会社又は関連会社の数
	ChangesInScopeOfApplicationOfEquityMethodTextBlock = '' #持分法適用の範囲の変更 [テキストブロック]
	NumberOfUnconsolidatedSubsidiariesAccountedForUsingEquityMethod = '' #持分法を適用した非連結子会社の数
	ChangesInScopeOfApplicationOfEquityMethodUnconsolidatedSubsidiariesTextBlock = '' #持分法適用の範囲の変更－非連結子会社 [テキストブロック]
	NumberOfAssociatesAccountedForUsingEquityMethod = '' #持分法を適用した関連会社の数
	ChangesInScopeOfApplicationOfEquityMethodAssociatesTextBlock = '' #持分法適用の範囲の変更－関連会社 [テキストブロック]
	NamesOfMajorUnconsolidatedSubsidiariesAndAssociatesAndReasonsForNotBeingAccountedForUsingEquityMethodTextBlock = '' #持分法を適用しない非連結子会社又は関連会社がある場合には、これらのうち主要な会社等の名称及び持分法を適用しない理由 [テキストブロック]
	NamesOfCompaniesEtcAndReasonsForNotBeingDeemedAsAssociatesEvenThoughMoreThan20PerCentAndLessThanHalfOfVotingRightsAreOwnedByReportingCompanyTextBlock = '' #他の会社等の議決権の百分の二十以上、百分の五十以下を自己の計算において所有しているにもかかわらず当該他の会社等を関連会社としなかった場合には、当該他の会社等の名称及び関連会社としなかった理由 [テキストブロック]
	OtherSpecificInformationIfDeemedNecessaryAboutApplicationOfEquityMethodTextBlock = '' #持分法の適用の手続について特に記載する必要があると認められる事項がある場合には、その内容 [テキストブロック]
	DisclosureAboutFiscalYearsEtcOfConsolidatedSubsidiariesTextBlock = '' #連結子会社の事業年度等に関する事項 [テキストブロック]
	DisclosureOfAccountingPoliciesAbstract = '' #会計処理基準に関する事項 [タイトル項目]
	DisclosureOfAccountingPoliciesTextBlock = '' #会計方針に関する事項 [テキストブロック]
	SignificantAccountingEstimatesConsolidatedFinancialStatementsHeading = '' #重要な会計上の見積り、連結財務諸表 [目次項目]
	SignificantAccountingEstimatesConsolidatedFinancialStatementsTextBlock = '' #重要な会計上の見積り、連結財務諸表 [テキストブロック]
	NotesChangesInAccountingPoliciesConsolidatedFinancialStatementsHeading = '' #会計方針の変更、連結財務諸表 [目次項目]
	NotesChangesInAccountingPoliciesInAccordanceWithChangesInAccountingStandardsEtcConsolidatedFinancialStatementsTextBlock = '' #会計基準等の改正等に伴う会計方針の変更、連結財務諸表 [テキストブロック]
	NotesVoluntaryChangesInAccountingPoliciesConsolidatedFinancialStatementsTextBlock = '' #会計基準等の改正等以外の正当な理由による会計方針の変更、連結財務諸表 [テキストブロック]
	NotesChangesInAccountingPoliciesWhichAreDifficultToDistinguishFromChangesInAccountingEstimatesConsolidatedFinancialStatementsTextBlock = '' #会計上の見積りの変更と区別することが困難な会計方針の変更、連結財務諸表 [テキストブロック]
	NotesNewAccountingStandardsNotYetAppliedConsolidatedFinancialStatementsHeading = '' #未適用の会計基準等、連結財務諸表 [目次項目]
	NotesNewAccountingStandardsNotYetAppliedConsolidatedFinancialStatementsTextBlock = '' #未適用の会計基準等、連結財務諸表 [テキストブロック]
	NotesChangesInPresentationConsolidatedFinancialStatementsHeading = '' #表示方法の変更、連結財務諸表 [目次項目]
	NotesChangesInPresentationConsolidatedFinancialStatementsTextBlock = '' #表示方法の変更、連結財務諸表 [テキストブロック]
	NotesChangesInAccountingEstimatesConsolidatedFinancialStatementsHeading = '' #会計上の見積りの変更、連結財務諸表 [目次項目]
	NotesChangesInAccountingEstimatesConsolidatedFinancialStatementsTextBlock = '' #会計上の見積りの変更、連結財務諸表 [テキストブロック]
	NotesRestatementConsolidatedFinancialStatementsHeading = '' #修正再表示、連結財務諸表 [目次項目]
	NotesRestatementConsolidatedFinancialStatementsTextBlock = '' #修正再表示、連結財務諸表 [テキストブロック]
	NotesAdditionalInformationConsolidatedFinancialStatementsHeading = '' #追加情報、連結財務諸表 [目次項目]
	NotesAdditionalInformationConsolidatedFinancialStatementsTextBlock = '' #追加情報、連結財務諸表 [テキストブロック]
	NotesConsolidatedBalanceSheetHeading = '' #連結貸借対照表関係 [目次項目]
	NotesConsolidatedBalanceSheetHeading = '' #連結貸借対照表関係 [目次項目]
	NotesConsolidatedBalanceSheetTable = '' #連結貸借対照表関係 [表]
	ConsolidatedOrNonConsolidatedAxis = '' #連結個別 [軸]
	ConsolidatedMember = '' #連結 [メンバー] ※ディメンションデフォルト
	NotesConsolidatedBalanceSheetLineItems = '' #連結貸借対照表関係 [表示項目]
	NotesRegardingInventoriesTextBlock = '' #棚卸資産の内訳の注記 [テキストブロック]
	MerchandiseAndFinishedGoods = '' #商品及び製品
	WorkInProcess = '' #仕掛品
	RawMaterialsAndSupplies = '' #原材料及び貯蔵品
	Inventories = '' #棚卸資産
	NotesRegardingAmountsOfNotesAndAccountsReceivableTradeAndContractAssetsTextBlock = '' #受取手形、売掛金及び契約資産の金額の注記 [テキストブロック]
	NotesReceivableTrade = '' #受取手形
	AllowanceForDoubtfulAccountsNotesReceivableTrade = '' #貸倒引当金、受取手形
	NotesReceivableTradeNet = '' #受取手形（純額）
	AccountsReceivableTrade = '' #売掛金
	AllowanceForDoubtfulAccountsAccountsReceivableTrade = '' #貸倒引当金、売掛金
	AccountsReceivableTradeNet = '' #売掛金（純額）
	ContractAssets = '' #契約資産
	AllowanceForDoubtfulAccountsContractAssets = '' #貸倒引当金、契約資産
	ContractAssetsNet = '' #契約資産（純額）
	NotesRegardingAllowancesDirectlyDeductedFromBalancesOfAssetsTextBlock = '' #資産の金額から直接控除している引当金の注記 [テキストブロック]
	AllowanceForDoubtfulAccountsCA = '' #貸倒引当金、流動資産、一括控除
	AllowanceForDoubtfulAccountsIOAByGroup = '' #貸倒引当金、投資その他の資産、一括控除
	AllowanceForDoubtfulAccountsAccountsReceivableTrade = '' #貸倒引当金、売掛金
	AllowanceForDoubtfulAccountsLongTermLoansReceivable = '' #貸倒引当金、長期貸付金
	AllowanceForDoubtfulAccountsClaimsInBankruptcyReorganizationClaimsAndOther = '' #貸倒引当金、破産更生債権等
	NotesRegardingAccumulatedDepreciationOfPropertyPlantAndEquipmentTextBlock = '' #有形固定資産の減価償却累計額の注記 [テキストブロック]
	AccumulatedDepreciationPPEByGroup = '' #減価償却累計額、有形固定資産、一括控除
	AccumulatedDepreciationBuildings = '' #減価償却累計額、建物
	AccumulatedDepreciationStructures = '' #減価償却累計額、構築物
	AccumulatedDepreciationMachineryAndEquipment = '' #減価償却累計額、機械及び装置
	NotesRegardingAmountsOfReductionEntryOfPropertyPlantAndEquipmentTextBlock = '' #有形固定資産の圧縮記帳額の注記 [テキストブロック]
	NotesRegardingPresentationOfAccumulatedImpairmentLossTextBlock = '' #減損損失累計額の表示に関する注記 [テキストブロック]
	NotesRegardingSharesAndBondsEtcOfUnconsolidatedSubsidiariesAndAssociatesTextBlock = '' #非連結子会社及び関連会社の株式及び社債等 [テキストブロック]
	NotesRegardingRevaluationOfLandForBusinessTextBlock = '' #事業用土地の再評価に関する注記 [テキストブロック]
	NotesRegardingPledgedAssetsTextBlock = '' #担保に供している資産の注記 [テキストブロック]
	NotesRegardingAmountOfContractLiabilitiesTextBlock = '' #契約負債の金額の注記 [テキストブロック]
	ContractLiabilities = '' #契約負債
	NotesRegardingPresentationOfGoodwillAndNegativeGoodwillTextBlock = '' #のれん及び負ののれんの表示に関する注記 [テキストブロック]
	NotesRegardingPresentationOfInventoriesAndProvisionForLossOnConstructionContractsTextBlock = '' #棚卸資産及び工事損失引当金の表示に関する注記 [テキストブロック]
	NotesRegardingReservesUnderSpecialLawsTextBlock = '' #特別法上の準備金等に関する注記 [テキストブロック]
	NotesRegardingProvisionIncurredFromBusinessCombinationTextBlock = '' #企業結合に係る特定勘定の注記 [テキストブロック]
	NotesRegardingGuaranteeObligationsTextBlock = '' #保証債務の注記 [テキストブロック]
	NotesRegardingTradeNotesReceivableDiscountedOrTransferredByEndorsementTextBlock = '' #受取手形割引高及び（又は）受取手形裏書譲渡高 [テキストブロック]
	DiscountedTradeNotesReceivable = '' #受取手形割引高
	TradeNotesReceivableTransferredByEndorsement = '' #受取手形裏書譲渡高
	NotesRegardingLiabilitiesEtcOfSpecialPurposeEntitiesTextBlock = '' #特別目的会社の債務等に関する注記 [テキストブロック]
	NotesRegardingReservesRequiredByContractsTextBlock = '' #契約による積立金の注記 [テキストブロック]
	NotesRegardingPresentationOfNetAssetsOfDesignatedCorporationTextBlock = '' #指定法人の純資産の記載に関する注記 [テキストブロック]
	NotesRegardingClassificationOfAssetsAndLiabilitiesOfIndustryInAppendedListTextBlock = '' #別記事業の資産及び負債の分類に関する注記 [テキストブロック]
	NotesRegardingPromissoryNotesDueOnBalanceSheetDateTextBlock = '' #期末日満期手形の会計処理 [テキストブロック]
	OtherElementsForNotesBalanceSheetAbstract = '' #貸借対照表関係のその他の要素 [タイトル項目]
	NotesRegardingLoanedWhichBorrowerHasRightToSellOrRepledgeTextBlock = '' #消費貸借契約及び（又は）消費寄託契約により貸し付けている有価証券に関する注記 [テキストブロック]
	NotesRegardingFinancialAssetsBorrowedWhichBorrowerHasRightToSellOrRepledgeTextBlock = '' #自由処分権を有する担保受入金融資産に関する注記 [テキストブロック]
	NotesRegardingLoanedSecuritiesAndFinancialAssetsBorrowedWhichBorrowerHasRightToSellOrRepledgeTextBlock = '' #有価証券の消費貸借契約・消費寄託契約及び自由処分権を有する担保受入金融資産に関する注記 [テキストブロック]
	NotesRegardingLoanParticipationsTextBlock = '' #ローン・パーティシペーションに関する注記 [テキストブロック]
	CreditorsNotesRegardingOverdraftContractsAndOrLoanCommitmentsTextBlock = '' #当座貸越契約及び（又は）貸出コミットメントに関する貸手の注記 [テキストブロック]
	DebtorsNotesRegardingOverdraftContractsAndOrLoanCommitmentsTextBlock = '' #当座貸越契約及び（又は）貸出コミットメントに関する借手の注記 [テキストブロック]
	NotesRegardingTotalAmountsOfSharesOfAndOrLoansToAffiliatedEntitiesTextBlock = '' #関係会社の株式及び（又は）出資金の総額 [テキストブロック]
	NotesRegardingTotalAmountsOfSharesOfAndOrLoansToUnconsolidatedSubsidiariesAndAssociatesTextBlock = '' #非連結子会社及び関連会社の株式及び（又は）出資金の総額 [テキストブロック]
	NotesRegardingSubordinatedBorrowingsTextBlock = '' #劣後特約付借入金に関する注記 [テキストブロック]
	NotesRegardingSubordinatedBondsPayableTextBlock = '' #劣後特約付社債に関する注記 [テキストブロック]
	NotesRegardingGuaranteeObligationForCorporateBondsIncludedInAssetsTextBlock = '' #資産の部の社債に係る保証債務に関する注記 [テキストブロック]
	OtherElementsForNotesBalanceSheetOfBankAbstract = '' #銀行業の貸借対照表関係のその他の要素 [タイトル項目]
	NotesRegardingLoansBasedOnBankingActAndActOnEmergencyMeasuresForRevitalizationOfFinancialFunctionsBNKTextBlock = '' #銀行法及び金融機能の再生のための緊急措置に関する法律に基づく債権に関する注記、銀行業 [テキストブロック]
	NotesRegardingBillsDiscountedInBankingIndustryBNKTextBlock = '' #銀行業における手形割引に関する注記、銀行業 [テキストブロック]
	OtherElementsForNotesBalanceSheetOfSecuritiesRelatedBusinessAbstract = '' #第一種金融商品取引業の貸借対照表関係のその他の要素 [タイトル項目]
	NotesRegardingMarketValueOfSecuritiesPledgedToCounterpartiesSECTextBlock = '' #差し入れた有価証券等の時価の注記、第一種金融商品取引業 [テキストブロック]
	NotesRegardingMarketValueOfSecuritiesReceivedAsCollateralFromCounterpartiesSECTextBlock = '' #差し入れを受けた有価証券等の時価の注記、第一種金融商品取引業 [テキストブロック]
	BreakdownOfTradingAccountSecuritiesEtcSECTextBlock = '' #商品有価証券等の内訳、第一種金融商品取引業 [テキストブロック]
	OtherElementsForNotesBalanceSheetOfInsuranceAbstract = '' #保険業の貸借対照表関係のその他の要素 [タイトル項目]
	NotesRegardingLoansBasedOnInsuranceBusinessActINSTextBlock = '' #保険業法に基づく債権に関する注記、保険業 [テキストブロック]
	NotesRegardingAssetsAndLiabilitiesIncludedInSpecificAccountsSpecifiedByArticle118OfInsuranceBusinessActINSTextBlock = '' #保険業法第118条に規定する特別勘定の資産及び負債に関する注記、保険業 [テキストブロック]
	NotesRegardingDeferredAssetsIncludedInOtherAssetsSpecifiedByArticle113OfInsuranceBusinessActTextBlock = '' #その他資産に含まれている保険業法第113条に規定する事業費の繰延額の注記 [テキストブロック]
	NotesRegardingIncreaseAndDecreaseInReserveForPolicyholderDividendsAndPaymentsOfPolicyholderDividendsINSTextBlock = '' #契約者配当準備金の増減異動及び契約者配当金の支払額に関する注記、保険業 [テキストブロック]
	NotesRegardingSurplusFromOrganizationChangeSpecifiedByArticle91OfInsuranceBusinessActINSTextBlock = '' #保険業法第91条の規定による組織変更剰余金額の注記、保険業 [テキストブロック]
	NotesRegardingReservesForOutstandingClaimsReinsuredINSTextBlock = '' #保険業法施行規則第73条第3項において準用する同規則第71条第1項に規定する再保険を付した部分に相当する支払備金の金額の注記、保険業 [テキストブロック]
	NotesRegardingPolicyReservesReinsuredINSTextBlock = '' #保険業法施行規則第71条第1項に規定する再保険を付した部分に相当する責任準備金の金額の注記、保険業 [テキストブロック]
	NotesRegardingObligationsToLifeInsurancePolicyholdersProtectionCorporationOfJapanINSTextBlock = '' #保険業法第259条の規定に基づく生命保険契約者保護機構に対する今後の負担見積額、保険業 [テキストブロック]
	BreakdownOfOutstandingClaimsINSTextBlock = '' #支払備金の内訳、保険業 [テキストブロック]
	BreakdownOfPolicyReserveINSTextBlock = '' #責任準備金の内訳、保険業 [テキストブロック]
	OtherElementsForNotesBalanceSheetOfSpecificFinanceAbstract = '' #特定金融業の貸借対照表関係のその他の要素 [タイトル項目]
	NotesRegardingBadLoansSPFTextBlock = '' #不良債権に関する注記、特定金融業 [テキストブロック]
	OtherElementsForNotesBalanceSheetOfCommodityFutureTradingAbstract = '' #商品先物取引業の貸借対照表関係のその他の要素 [タイトル項目]
	ExplanationOfFuturesTransactionMarginCustomerCMDTextBlock = '' #委託者先物取引差金の説明、商品先物取引業 [テキストブロック]
	NotesConsolidatedStatementOfIncomeHeading = '' #連結損益計算書関係 [目次項目]
	NotesConsolidatedStatementOfIncomeHeading = '' #連結損益計算書関係 [目次項目]
	NotesConsolidatedStatementOfIncomeTable = '' #連結損益計算書関係 [表]
	ConsolidatedOrNonConsolidatedAxis = '' #連結個別 [軸]
	ConsolidatedMember = '' #連結 [メンバー] ※ディメンションデフォルト
	NotesConsolidatedStatementOfIncomeLineItems = '' #連結損益計算書関係 [表示項目]
	NotesRegardingAmountOfRevenueFromContractsWithCustomersTextBlock = '' #顧客との契約から生じる収益の金額の注記 [テキストブロック]
	RevenueFromContractsWithCustomers = '' #顧客との契約から生じる収益
	NotesRegardingLossOnConstructionContractsTextBlock = '' #工事損失引当金繰入額の注記 [テキストブロック]
	NotesRegardingWriteDownsOfInventoriesTextBlock = '' #棚卸資産の帳簿価額の切下げに関する注記 [テキストブロック]
	WriteDownsOfInventories = '' #棚卸資産帳簿価額切下額
	MajorComponentsOfSellingGeneralAndAdministrativeExpensesTextBlock = '' #主要な販売費及び一般管理費 [テキストブロック]
	DepreciationSGA = '' #減価償却費、販売費及び一般管理費
	ProvisionOfAllowanceForDoubtfulAccountsSGA = '' #貸倒引当金繰入額、販売費及び一般管理費
	ResearchAndDevelopmentExpensesIncludedInGeneralAndAdministrativeExpensesAndManufacturingCostForCurrentPeriodTextBlock = '' #一般管理費及び当期製造費用に含まれる研究開発費 [テキストブロック]
	ResearchAndDevelopmentExpensesIncludedInGeneralAndAdministrativeExpensesAndManufacturingCostForCurrentPeriod = '' #一般管理費及び当期製造費用に含まれる研究開発費
	ResearchAndDevelopmentExpensesSGA = '' #研究開発費、販売費及び一般管理費
	NotesRegardingImpairmentLossTextBlock = '' #減損損失に関する注記 [テキストブロック]
	NotesRegardingReversalOfProvisionIncurredFromBusinessCombinationTextBlock = '' #企業結合に係る特定勘定の取崩益の注記 [テキストブロック]
	NotesRegardingGainOnSalesOfPropertyPlantAndEquipmentTextBlock = '' #固定資産売却益の注記 [テキストブロック]
	NotesRegardingLossOnSalesOfPropertyPlantAndEquipmentTextBlock = '' #固定資産売却損の注記 [テキストブロック]
	NotesRegardingLossOnDisposalOfPropertyPlantAndEquipmentTextBlock = '' #固定資産除却損の注記 [テキストブロック]
	NotesRegardingLossOnDisposalAndSalesOfPropertyPlantAndEquipmentTextBlock = '' #固定資産除売却損の注記 [テキストブロック]
	NotesRegardingClassificationOfRevenuesAndExpensesOfIndustryInAppendedListTextBlock = '' #別記事業の収益及び費用の分類に関する注記 [テキストブロック]
	OtherElementsForNotesStatementOfIncomeAbstract = '' #損益計算書関係のその他の要素 [タイトル項目]
	BreakdownOfBusinessCostTextBlock = '' #事業費の内訳 [テキストブロック]
	BreakdownOfPersonnelExpensesTextBlock = '' #人件費の内訳 [テキストブロック]
	BreakdownOfGainOnSalesOfSecuritiesTextBlock = '' #有価証券売却益の内訳 [テキストブロック]
	BreakdownOfLossOnSalesOfSecuritiesTextBlock = '' #有価証券売却損の内訳 [テキストブロック]
	BreakdownOfLossOnValuationOfSecuritiesTextBlock = '' #有価証券評価損の内訳 [テキストブロック]
	NotesRegardingTransactionsWithAffiliatedEntitiesTextBlock = '' #関係会社との取引に関する注記 [テキストブロック]
	OtherElementsForNotesStatementOfIncomeOfBankAbstract = '' #銀行業の損益計算書関係のその他の要素 [タイトル項目]
	MajorComponentsOfOtherIncomeBNKTextBlock = '' #その他の経常収益の主要な内訳、銀行業 [テキストブロック]
	MajorComponentsOfOtherExpensesBNKTextBlock = '' #その他の経常費用の主要な内訳、銀行業 [テキストブロック]
	OtherElementsForNotesStatementOfIncomeOfSecuritiesRelatedBusinessAbstract = '' #第一種金融商品取引業の損益計算書関係のその他の要素 [タイトル項目]
	BreakdownOfNetTradingIncomeSECTextBlock = '' #トレーディング損益の内訳、第一種金融商品取引業 [テキストブロック]
	BreakdownOfFinancialRevenueSECTextBlock = '' #金融収益の内訳、第一種金融商品取引業 [テキストブロック]
	BreakdownOfFinancialExpensesSECTextBlock = '' #金融費用の内訳、第一種金融商品取引業 [テキストブロック]
	OtherElementsForNotesStatementOfIncomeOfInsuranceAbstract = '' #保険業の損益計算書関係のその他の要素 [タイトル項目]
	MajorComponentsOfBusinessCostTextBlock = '' #事業費の主な内訳 [テキストブロック]
	AgentFeeEtcINSNonlife = '' #代理店手数料等、損害保険業
	SalariesINSNonlife = '' #給与、損害保険業
	BreakdownOfNetPremiumsWrittenINSTextBlock = '' #正味収入保険料の内訳、保険業 [テキストブロック]
	BreakdownOfNetClaimsPaidINSTextBlock = '' #正味支払保険金の内訳、保険業 [テキストブロック]
	BreakdownOfCommissionsAndCollectionFeesINSTextBlock = '' #諸手数料及び集金費の内訳、保険業 [テキストブロック]
	BreakdownOfProvisionForOrReversalOfOutstandingClaimsINSTextBlock = '' #支払備金繰入額又は支払備金戻入額の内訳、保険業 [テキストブロック]
	BreakdownOfProvisionForOrReversalOfUnderwritingReservesINSTextBlock = '' #責任準備金繰入額又は責任準備金戻入額の内訳、保険業 [テキストブロック]
	NotesRegardingReversalOfOrProvisionForReservesForOutstandingClaimsReinsuredINSTextBlock = '' #支払備金繰入額又は支払備金戻入額の計算上、差し引かれた又は足し上げられた出再支払備金繰入額又は出再支払備金戻入額の注記、保険業 [テキストブロック]
	NotesRegardingReversalOfOrProvisionForPolicyReservesReinsuredINSTextBlock = '' #責任準備金繰入額又は責任準備金戻入額の計算上、差し引かれた又は足し上げられた出再責任準備金繰入額又は出再責任準備金戻入額の注記、保険業 [テキストブロック]
	BreakdownOfInterestAndDividendIncomeBySourceAssetINSTextBlock = '' #利息及び配当金収入の資産源泉別内訳、保険業 [テキストブロック]
	InterestAndDividendIncomeGainLossOnSalesAndUnrealizedGainLossForEachOfTradingAccountSecuritiesINSTextBlock = '' #商品有価証券及び売買目的有価証券に係るそれぞれの利息及び配当金収入、売却損益及び評価損益の金額、保険業 [テキストブロック]
	NotesRegardingUnrealizedGainLossForMoneyTrustINSTextBlock = '' #金銭の信託に係る評価損益の金額の注記、保険業 [テキストブロック]
	NotesRegardingUnrealizedGainLossForDerivativesINSTextBlock = '' #金融派生商品に係る評価損益の金額の注記、保険業 [テキストブロック]
	MajorComponentsOfOtherExtraordinaryIncomeINSTextBlock = '' #その他特別利益の主な内訳、保険業 [テキストブロック]
	MajorComponentsOfOtherExtraordinaryLossesINSTextBlock = '' #その他特別損失の主な内訳、保険業 [テキストブロック]
	OtherElementsForNotesStatementOfIncomeOfCommodityFutureTradingAbstract = '' #商品先物取引業の損益計算書関係のその他の要素 [タイトル項目]
	BreakdownOfBrokerageIncomeCMDTextBlock = '' #受取手数料の内訳、商品先物取引業 [テキストブロック]
	BreakdownOfNetGainOnTradingCMDTextBlock = '' #売買損益の内訳、商品先物取引業 [テキストブロック]
	ExchangeRelatedExpensesCMDTextBlock = '' #取引所等関係費の内訳、商品先物取引業 [テキストブロック]
	NotesConsolidatedStatementOfComprehensiveIncomeHeading = '' #連結包括利益計算書関係 [目次項目]
	NotesConsolidatedStatementOfComprehensiveIncomeHeading = '' #連結包括利益計算書関係 [目次項目]
	NotesConsolidatedStatementOfComprehensiveIncomeTable = '' #連結包括利益計算書関係 [表]
	ConsolidatedOrNonConsolidatedAxis = '' #連結個別 [軸]
	ConsolidatedMember = '' #連結 [メンバー] ※ディメンションデフォルト
	NotesConsolidatedStatementOfComprehensiveIncomeLineItems = '' #連結包括利益計算書関係 [表示項目]
	NotesRegardingTaxEffectsRelatingToOtherComprehensiveIncomeTextBlock = '' #その他の包括利益に係る税効果額 [テキストブロック]
	NotesRegardingReclassificationAdjustmentsRelatingToOtherComprehensiveIncomeTextBlock = '' #その他の包括利益に係る組替調整額 [テキストブロック]
	NotesRegardingReclassificationAdjustmentsAndTaxEffectsRelatingToOtherComprehensiveIncomeTextBlock = '' #その他の包括利益に係る組替調整額及び税効果額 [テキストブロック]
	NotesConsolidatedStatementOfComprehensiveIncomeSingleStatementHeading = '' #連結損益及び包括利益計算書関係 [目次項目]
	NotesConsolidatedStatementOfComprehensiveIncomeSingleStatementHeading = '' #連結損益及び包括利益計算書関係 [目次項目]
	NotesConsolidatedStatementOfComprehensiveIncomeSingleStatementTable = '' #連結損益及び包括利益計算書関係 [表]
	ConsolidatedOrNonConsolidatedAxis = '' #連結個別 [軸]
	ConsolidatedMember = '' #連結 [メンバー] ※ディメンションデフォルト
	NotesConsolidatedStatementOfComprehensiveIncomeSingleStatementLineItems = '' #連結損益及び包括利益計算書関係 [表示項目]
	NotesRegardingAmountOfRevenueFromContractsWithCustomersTextBlock = '' #顧客との契約から生じる収益の金額の注記 [テキストブロック]
	RevenueFromContractsWithCustomers = '' #顧客との契約から生じる収益
	NotesRegardingLossOnConstructionContractsTextBlock = '' #工事損失引当金繰入額の注記 [テキストブロック]
	NotesRegardingWriteDownsOfInventoriesTextBlock = '' #棚卸資産の帳簿価額の切下げに関する注記 [テキストブロック]
	WriteDownsOfInventories = '' #棚卸資産帳簿価額切下額
	MajorComponentsOfSellingGeneralAndAdministrativeExpensesTextBlock = '' #主要な販売費及び一般管理費 [テキストブロック]
	DepreciationSGA = '' #減価償却費、販売費及び一般管理費
	ProvisionOfAllowanceForDoubtfulAccountsSGA = '' #貸倒引当金繰入額、販売費及び一般管理費
	ResearchAndDevelopmentExpensesIncludedInGeneralAndAdministrativeExpensesAndManufacturingCostForCurrentPeriodTextBlock = '' #一般管理費及び当期製造費用に含まれる研究開発費 [テキストブロック]
	ResearchAndDevelopmentExpensesIncludedInGeneralAndAdministrativeExpensesAndManufacturingCostForCurrentPeriod = '' #一般管理費及び当期製造費用に含まれる研究開発費
	ResearchAndDevelopmentExpensesSGA = '' #研究開発費、販売費及び一般管理費
	NotesRegardingImpairmentLossTextBlock = '' #減損損失に関する注記 [テキストブロック]
	NotesRegardingReversalOfProvisionIncurredFromBusinessCombinationTextBlock = '' #企業結合に係る特定勘定の取崩益の注記 [テキストブロック]
	NotesRegardingClassificationOfRevenuesAndExpensesOfIndustryInAppendedListTextBlock = '' #別記事業の収益及び費用の分類に関する注記 [テキストブロック]
	NotesRegardingTaxEffectsRelatingToOtherComprehensiveIncomeTextBlock = '' #その他の包括利益に係る税効果額 [テキストブロック]
	NotesRegardingReclassificationAdjustmentsRelatingToOtherComprehensiveIncomeTextBlock = '' #その他の包括利益に係る組替調整額 [テキストブロック]
	NotesRegardingReclassificationAdjustmentsAndTaxEffectsRelatingToOtherComprehensiveIncomeTextBlock = '' #その他の包括利益に係る組替調整額及び税効果額 [テキストブロック]
	NotesConsolidatedStatementOfChangesInEquityHeading = '' #連結株主資本等変動計算書関係 [目次項目]
	NotesConsolidatedStatementOfChangesInEquityHeading = '' #連結株主資本等変動計算書関係 [目次項目]
	NotesConsolidatedStatementOfChangesInEquityTable = '' #連結株主資本等変動計算書関係 [表]
	ConsolidatedOrNonConsolidatedAxis = '' #連結個別 [軸]
	ConsolidatedMember = '' #連結 [メンバー] ※ディメンションデフォルト
	NotesConsolidatedStatementOfChangesInEquityLineItems = '' #連結株主資本等変動計算書関係 [表示項目]
	NotesRegardingIssuedSharesAndTreasurySharesTextBlock = '' #発行済株式及び自己株式に関する注記 [テキストブロック]
	NotesRegardingNewShareSubscriptionRightsEtcTextBlock = '' #新株予約権等に関する注記 [テキストブロック]
	NotesRegardingDividendTextBlock = '' #配当に関する注記 [テキストブロック]
	NotesConsolidatedStatementOfCashFlowsHeading = '' #連結キャッシュ・フロー計算書関係 [目次項目]
	NotesConsolidatedStatementOfCashFlowsHeading = '' #連結キャッシュ・フロー計算書関係 [目次項目]
	NotesConsolidatedStatementOfCashFlowsTable = '' #連結キャッシュ・フロー計算書関係 [表]
	ConsolidatedOrNonConsolidatedAxis = '' #連結個別 [軸]
	ConsolidatedMember = '' #連結 [メンバー] ※ディメンションデフォルト
	NotesConsolidatedStatementOfCashFlowsLineItems = '' #連結キャッシュ・フロー計算書関係 [表示項目]
	ReconciliationOfEndingBalanceOfCashAndCashEquivalentsWithAccountBalancesPerBalanceSheetTextBlock = '' #現金及び現金同等物の期末残高と貸借対照表に掲記されている科目の金額との関係 [テキストブロック]
	MajorComponentsOfAssetsAndLiabilitiesOfConsolidatedSubsidiaryAcquiredByPurchaseOfSharesDuringReportingPeriodTextBlock = '' #株式の取得により新たに連結子会社となった会社がある場合には、当該会社の資産及び負債の主な内訳 [テキストブロック]
	MajorComponentsOfAssetsAndLiabilitiesOfConsolidatedSubsidiaryDisposedOfBySalesOfSharesDuringReportingPeriodTextBlock = '' #株式の売却により連結子会社でなくなった会社がある場合には、当該会社の資産及び負債の主な内訳 [テキストブロック]
	MajorComponentsOfAssetsAndLiabilitiesIncreasedOrDecreasedAsResultOfAcquisitionOrDisposalOfBusinessOrMergerEtcWherebyCashWasPaidOrReceivedAsConsiderationTextBlock = '' #現金及び現金同等物を対価とする事業の譲受け若しくは譲渡又は合併等を行った場合には、当該事業の譲受け若しくは譲渡又は合併等により増加又は減少した資産及び負債の主な内訳 [テキストブロック]
	DescriptionOfSignificantTransactionsNotRequiringUseOfCashOrCashEquivalentsTextBlock = '' #重要な非資金取引の内容 [テキストブロック]
	DescriptionOfFactThatCashFlowsFromUsedInInvestingActivitiesIncludeCashFlowsFromAssetManagementActivitiesRelatedToInsuranceBusinessINSTextBlock = '' #投資活動によるキャッシュ・フローには、保険事業に係る資産運用業務から生じるキャッシュ・フローを含んでいる旨、保険業 [テキストブロック]
	NotesLeasesConsolidatedFinancialStatementsHeading = '' #リース取引関係、連結財務諸表 [目次項目]
	NotesLeasesConsolidatedFinancialStatementsTextBlock = '' #リース取引関係、連結財務諸表 [テキストブロック]
	NotesFinancialInstrumentsConsolidatedFinancialStatementsHeading = '' #金融商品関係、連結財務諸表 [目次項目]
	NotesFinancialInstrumentsConsolidatedFinancialStatementsTextBlock = '' #金融商品関係、連結財務諸表 [テキストブロック]
	NotesSecuritiesConsolidatedFinancialStatementsHeading = '' #有価証券関係、連結財務諸表 [目次項目]
	NotesSecuritiesConsolidatedFinancialStatementsTextBlock = '' #有価証券関係、連結財務諸表 [テキストブロック]
	NotesMoneyHeldInTrustConsolidatedFinancialStatementsHeading = '' #金銭の信託関係、連結財務諸表 [目次項目]
	NotesMoneyHeldInTrustConsolidatedFinancialStatementsTextBlock = '' #金銭の信託関係、連結財務諸表 [テキストブロック]
	NotesValuationDifferenceOnAvailableForSaleSecuritiesConsolidatedFinancialStatementsHeading = '' #その他有価証券評価差額金、連結財務諸表 [目次項目]
	NotesValuationDifferenceOnAvailableForSaleSecuritiesConsolidatedFinancialStatementsTextBlock = '' #その他有価証券評価差額金、連結財務諸表 [テキストブロック]
	NotesDerivativesConsolidatedFinancialStatementsHeading = '' #デリバティブ取引関係、連結財務諸表 [目次項目]
	NotesDerivativesConsolidatedFinancialStatementsTextBlock = '' #デリバティブ取引関係、連結財務諸表 [テキストブロック]
	NotesRetirementBenefitsConsolidatedFinancialStatementsHeading = '' #退職給付関係、連結財務諸表 [目次項目]
	NotesRetirementBenefitsConsolidatedFinancialStatementsTextBlock = '' #退職給付関係、連結財務諸表 [テキストブロック]
	NotesShareOptionsEtcConsolidatedFinancialStatementsHeading = '' #ストック・オプション等関係、連結財務諸表 [目次項目]
	NotesShareOptionsEtcConsolidatedFinancialStatementsTextBlock = '' #ストック・オプション等関係、連結財務諸表 [テキストブロック]
	NotesTaxEffectAccountingConsolidatedFinancialStatementsHeading = '' #税効果会計関係、連結財務諸表 [目次項目]
	NotesTaxEffectAccountingConsolidatedFinancialStatementsTextBlock = '' #税効果会計関係、連結財務諸表 [テキストブロック]
	NotesBusinessCombinationsConsolidatedFinancialStatementsHeading = '' #企業結合等関係、連結財務諸表 [目次項目]
	NotesBusinessCombinationsConsolidatedFinancialStatementsTextBlock = '' #企業結合等関係、連結財務諸表 [テキストブロック]
	NotesAssetRetirementObligationsConsolidatedFinancialStatementsHeading = '' #資産除去債務関係、連結財務諸表 [目次項目]
	NotesAssetRetirementObligationsConsolidatedFinancialStatementsTextBlock = '' #資産除去債務関係、連結財務諸表 [テキストブロック]
	NotesRealEstateForLeaseEtcConsolidatedFinancialStatementsHeading = '' #賃貸等不動産関係、連結財務諸表 [目次項目]
	NotesRealEstateForLeaseEtcConsolidatedFinancialStatementsTextBlock = '' #賃貸等不動産関係、連結財務諸表 [テキストブロック]
	NotesRevenueRecognitionConsolidatedFinancialStatementsHeading = '' #収益認識関係、連結財務諸表 [目次項目]
	NotesRevenueRecognitionConsolidatedFinancialStatementsTextBlock = '' #収益認識関係、連結財務諸表 [テキストブロック]
	NotesInventoriesConsolidatedFinancialStatementsHeading = '' #棚卸資産関係、連結財務諸表 [目次項目]
	NotesInventoriesConsolidatedFinancialStatementsTextBlock = '' #棚卸資産関係、連結財務諸表 [テキストブロック]
	NotesSegmentInformationEtcConsolidatedFinancialStatementsHeading = '' #セグメント情報等、連結財務諸表 [目次項目]
	NotesSegmentInformationEtcConsolidatedFinancialStatementsTextBlock = '' #セグメント情報等、連結財務諸表 [テキストブロック]
	NotesSegmentInformationEtcConsolidatedFinancialStatementsHeading = '' #セグメント情報等、連結財務諸表 [目次項目]
	NotesSegmentInformationEtcConsolidatedFinancialStatementsTable = '' #セグメント情報等、連結財務諸表 [表]
	ConsolidatedOrNonConsolidatedAxis = '' #連結個別 [軸]
	ConsolidatedMember = '' #連結 [メンバー] ※ディメンションデフォルト
	NotesSegmentInformationEtcConsolidatedFinancialStatementsLineItems = '' #セグメント情報等、連結財務諸表 [表示項目]
	SegmentInformationAbstract = '' #セグメント情報 [タイトル項目]
	DescriptionOfReportableSegmentsTextBlock = '' #報告セグメントの概要 [テキストブロック]
	DisclosureOfChangesInReportableSegmentsTextBlock = '' #報告セグメントの変更に関する事項 [テキストブロック]
	DescriptionOfFactThatCompanysBusinessComprisesSingleSegment = '' #単一セグメントである旨
	ExplanationOfMeasurementsOfSalesProfitLossAssetLiabilityAndOtherItemsForEachReportableSegmentTextBlock = '' #報告セグメントごとの売上高、利益又は損失、資産、負債その他の項目の金額の算定方法 [テキストブロック]
	NotesSegmentInformationEtcConsolidatedFinancialStatementsHeading = '' #セグメント情報等、連結財務諸表 [目次項目]
	SegmentInformationAbstract = '' #セグメント情報 [タイトル項目]
	DisclosureOfSalesProfitLossAssetLiabilityAndOtherItemsForEachReportableSegmentTable = '' #報告セグメントごとの売上高、利益又は損失、資産、負債その他の項目の金額に関する情報 [表]
	ConsolidatedOrNonConsolidatedAxis = '' #連結個別 [軸]
	ConsolidatedMember = '' #連結 [メンバー] ※ディメンションデフォルト
	OperatingSegmentsAxis = '' #事業セグメント [軸]
	EntityTotalMember = '' #連結合計又は会社合計 [メンバー] ※ディメンションデフォルト
	TotalOfReportableSegmentsAndOthersMember = '' #報告セグメント及びその他の合計 [メンバー]
	ReportableSegmentsMember = '' #報告セグメント [メンバー]
	OtherReportableSegmentsMember = '' #その他の報告セグメント [メンバー]
	OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember = '' #報告セグメント以外の全てのセグメント [メンバー]
	ReconcilingItemsMember = '' #調整項目 [メンバー]
	DisclosureOfSalesProfitLossAssetLiabilityAndOtherItemsForEachReportableSegmentLineItems = '' #報告セグメントごとの売上高、利益又は損失、資産、負債その他の項目の金額に関する情報 [表示項目]
	SalesSegmentInformationAbstract = '' #売上高、セグメント情報 [タイトル項目]
	RevenuesFromExternalCustomers = '' #外部顧客への売上高
	TransactionsWithOtherSegments = '' #セグメント間の内部売上高又は振替高
	NetSales = '' #売上高
	Revenue = '' #売上収益
	OperatingRevenue1 = '' #営業収益
	OperatingRevenue2 = '' #営業収入
	GrossOperatingRevenue = '' #営業総収入
	OrdinaryIncomeBNK = '' #経常収益、銀行業
	OperatingIncomeINS = '' #経常収益、保険業
	SegmentProfitLossAbstract = '' #セグメント利益又は損失（△） [タイトル項目]
	OperatingIncome = '' #営業利益又は営業損失（△）
	OrdinaryIncome = '' #経常利益又は経常損失（△）
	IncomeBeforeIncomeTaxes = '' #税引前当期純利益又は税引前当期純損失（△）
	ProfitLossAttributableToOwnersOfParent = '' #親会社株主に帰属する当期純利益又は親会社株主に帰属する当期純損失（△）
	ProfitLoss = '' #当期純利益又は当期純損失（△）（平成26年3月28日財規等改正後）
	Assets = '' #資産
	Liabilities = '' #負債
	OtherItemsSegmentInformationAbstract = '' #その他の項目、セグメント情報 [タイトル項目]
	DepreciationSegmentInformation = '' #減価償却費、セグメント情報
	AmortizationOfGoodwillSGA = '' #のれん償却額、販売費及び一般管理費
	InterestIncomeNOI = '' #受取利息、営業外収益
	InterestExpensesNOE = '' #支払利息、営業外費用
	EquityInEarningsLossesOfAffiliates = '' #持分法投資利益又は損失（△）
	ExtraordinaryIncome = '' #特別利益
	GainOnNegativeGoodwillEI = '' #負ののれん発生益、特別利益
	ExtraordinaryLoss = '' #特別損失
	ImpairmentLossEL = '' #減損損失、特別損失
	IncomeTaxExpense = '' #税金費用
	InvestmentsInEntitiesAccountedForUsingEquityMethod = '' #持分法適用会社への投資額
	IncreaseInPropertyPlantAndEquipmentAndIntangibleAssets = '' #有形固定資産及び無形固定資産の増加額
	NotesSegmentInformationEtcConsolidatedFinancialStatementsHeading = '' #セグメント情報等、連結財務諸表 [目次項目]
	NotesSegmentInformationEtcConsolidatedFinancialStatementsTable = '' #セグメント情報等、連結財務諸表 [表]
	ConsolidatedOrNonConsolidatedAxis = '' #連結個別 [軸]
	ConsolidatedMember = '' #連結 [メンバー] ※ディメンションデフォルト
	NotesSegmentInformationEtcConsolidatedFinancialStatementsLineItems = '' #セグメント情報等、連結財務諸表 [表示項目]
	SegmentInformationAbstract = '' #セグメント情報 [タイトル項目]
	FootnotesRegardingSegmentInformationTableTextBlock = '' #セグメント表の脚注 [テキストブロック]
	DescriptionOfNatureAndAmountsOfDifferencesBetweenReportableSegmentsTotalAndFinancialStatementsTextBlock = '' #報告セグメント合計額と財務諸表計上額との差額及び当該差額の主な内容（差異調整に関する事項） [テキストブロック]
	NotesInformationAssociatedWithReportableSegmentsAbstract = '' #関連情報 [タイトル項目]
	InformationForEachProductOrServiceTextBlock = '' #製品及びサービスごとの情報 [テキストブロック]
	InformationForEachRegionAbstract = '' #地域ごとの情報 [タイトル項目]
	RevenuesFromExternalCustomersInformationForEachRegionTextBlock = '' #売上高、地域ごとの情報 [テキストブロック]
	PropertyPlantAndEquipmentInformationForEachRegionTextBlock = '' #有形固定資産、地域ごとの情報 [テキストブロック]
	InformationForEachOfMainCustomersTextBlock = '' #主要な顧客ごとの情報 [テキストブロック]
	NotesSegmentInformationEtcConsolidatedFinancialStatementsHeading = '' #セグメント情報等、連結財務諸表 [目次項目]
	DisclosureOfImpairmentLossOnNonCurrentAssetsForEachReportableSegmentAbstract = '' #報告セグメントごとの固定資産の減損損失に関する情報 [タイトル項目]
	DisclosureOfImpairmentLossOnNonCurrentAssetsForEachReportableSegmentTable = '' #報告セグメントごとの固定資産の減損損失に関する情報 [表]
	ConsolidatedOrNonConsolidatedAxis = '' #連結個別 [軸]
	ConsolidatedMember = '' #連結 [メンバー] ※ディメンションデフォルト
	OperatingSegmentsAxis = '' #事業セグメント [軸]
	EntityTotalMember = '' #連結合計又は会社合計 [メンバー] ※ディメンションデフォルト
	ReportableSegmentsMember = '' #報告セグメント [メンバー]
	OtherReportableSegmentsMember = '' #その他の報告セグメント [メンバー]
	OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember = '' #報告セグメント以外の全てのセグメント [メンバー]
	UnallocatedAmountsAndEliminationMember = '' #全社・消去 [メンバー]
	DisclosureOfImpairmentLossOnNonCurrentAssetsForEachReportableSegmentLineItems = '' #報告セグメントごとの固定資産の減損損失に関する情報 [表示項目]
	ImpairmentLossEL = '' #減損損失、特別損失
	NotesSegmentInformationEtcConsolidatedFinancialStatementsHeading = '' #セグメント情報等、連結財務諸表 [目次項目]
	NotesSegmentInformationEtcConsolidatedFinancialStatementsTable = '' #セグメント情報等、連結財務諸表 [表]
	ConsolidatedOrNonConsolidatedAxis = '' #連結個別 [軸]
	ConsolidatedMember = '' #連結 [メンバー] ※ディメンションデフォルト
	NotesSegmentInformationEtcConsolidatedFinancialStatementsLineItems = '' #セグメント情報等、連結財務諸表 [表示項目]
	DescriptionOfImpairmentLossNotAllocatedToReportableSegments = '' #報告セグメントに配分されていない減損損失の内容
	NotesSegmentInformationEtcConsolidatedFinancialStatementsHeading = '' #セグメント情報等、連結財務諸表 [目次項目]
	AmortizationAndUnamortizedBalanceOfGoodwillForEachReportableSegmentAbstract = '' #報告セグメントごとののれんの償却額及び未償却残高に関する情報 [タイトル項目]
	AmortizationAndUnamortizedBalanceOfGoodwillForEachReportableSegmentTable = '' #報告セグメントごとののれんの償却額及び未償却残高に関する情報 [表]
	ConsolidatedOrNonConsolidatedAxis = '' #連結個別 [軸]
	ConsolidatedMember = '' #連結 [メンバー] ※ディメンションデフォルト
	OperatingSegmentsAxis = '' #事業セグメント [軸]
	EntityTotalMember = '' #連結合計又は会社合計 [メンバー] ※ディメンションデフォルト
	ReportableSegmentsMember = '' #報告セグメント [メンバー]
	OtherReportableSegmentsMember = '' #その他の報告セグメント [メンバー]
	OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember = '' #報告セグメント以外の全てのセグメント [メンバー]
	UnallocatedAmountsAndEliminationMember = '' #全社・消去 [メンバー]
	AmortizationAndUnamortizedBalanceOfGoodwillForEachReportableSegmentLineItems = '' #報告セグメントごとののれんの償却額及び未償却残高に関する情報 [表示項目]
	AmortizationOfGoodwillSGA = '' #のれん償却額、販売費及び一般管理費
	Goodwill = '' #のれん
	GoodwillBeforeOffsetting = '' #のれん（相殺前）
	NotesSegmentInformationEtcConsolidatedFinancialStatementsHeading = '' #セグメント情報等、連結財務諸表 [目次項目]
	AmortizationAndUnamortizedBalanceOfNegativeGoodwillForEachReportableSegmentAbstract = '' #報告セグメントごとの負ののれんの償却額及び未償却残高に関する情報 [タイトル項目]
	AmortizationAndUnamortizedBalanceOfNegativeGoodwillForEachReportableSegmentTable = '' #報告セグメントごとの負ののれんの償却額及び未償却残高に関する情報 [表]
	ConsolidatedOrNonConsolidatedAxis = '' #連結個別 [軸]
	ConsolidatedMember = '' #連結 [メンバー] ※ディメンションデフォルト
	OperatingSegmentsAxis = '' #事業セグメント [軸]
	EntityTotalMember = '' #連結合計又は会社合計 [メンバー] ※ディメンションデフォルト
	ReportableSegmentsMember = '' #報告セグメント [メンバー]
	OtherReportableSegmentsMember = '' #その他の報告セグメント [メンバー]
	OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember = '' #報告セグメント以外の全てのセグメント [メンバー]
	UnallocatedAmountsAndEliminationMember = '' #全社・消去 [メンバー]
	AmortizationAndUnamortizedBalanceOfNegativeGoodwillForEachReportableSegmentLineItems = '' #報告セグメントごとの負ののれんの償却額及び未償却残高に関する情報 [表示項目]
	AmortizationOfNegativeGoodwillNOI = '' #負ののれん償却額、営業外収益
	NegativeGoodwill = '' #負ののれん
	NegativeGoodwillBeforeOffsetting = '' #負ののれん（相殺前）
	NotesSegmentInformationEtcConsolidatedFinancialStatementsHeading = '' #セグメント情報等、連結財務諸表 [目次項目]
	NotesSegmentInformationEtcConsolidatedFinancialStatementsTable = '' #セグメント情報等、連結財務諸表 [表]
	ConsolidatedOrNonConsolidatedAxis = '' #連結個別 [軸]
	ConsolidatedMember = '' #連結 [メンバー] ※ディメンションデフォルト
	NotesSegmentInformationEtcConsolidatedFinancialStatementsLineItems = '' #セグメント情報等、連結財務諸表 [表示項目]
	DescriptionOfAmortizationOfGoodwillOrUnamortizedBalanceOfGoodwillNotAllocatedToReportableSegments = '' #報告セグメントに配分されていないのれんの償却額又は未償却残高の内容
	NotesSegmentInformationEtcConsolidatedFinancialStatementsHeading = '' #セグメント情報等、連結財務諸表 [目次項目]
	InformationAboutGainOnBargainPurchaseForEachReportableSegmentTable = '' #報告セグメントごとの負ののれん発生益に関する情報 [表]
	ConsolidatedOrNonConsolidatedAxis = '' #連結個別 [軸]
	ConsolidatedMember = '' #連結 [メンバー] ※ディメンションデフォルト
	OperatingSegmentsAxis = '' #事業セグメント [軸]
	EntityTotalMember = '' #連結合計又は会社合計 [メンバー] ※ディメンションデフォルト
	ReportableSegmentsMember = '' #報告セグメント [メンバー]
	OtherReportableSegmentsMember = '' #その他の報告セグメント [メンバー]
	OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember = '' #報告セグメント以外の全てのセグメント [メンバー]
	UnallocatedAmountsAndEliminationMember = '' #全社・消去 [メンバー]
	InformationAboutGainOnBargainPurchaseForEachReportableSegmentLineItems = '' #報告セグメントごとの負ののれん発生益に関する情報 [表示項目]
	DescriptionOfFactorsWhichLedToRecognitionOfGainOnBargainPurchaseTextBlock = '' #報告セグメントごとの負ののれん発生益を認識する要因となった事象の概要 [テキストブロック]
	NotesOperationOfPublicFacilitiesConsolidatedFinancialStatementsHeading = '' #公共施設等運営事業関係、連結財務諸表 [目次項目]
	NotesOperationOfPublicFacilitiesConsolidatedFinancialStatementsTextBlock = '' #公共施設等運営事業関係、連結財務諸表 [テキストブロック]
	NotesRelatedPartiesConsolidatedFinancialStatementsHeading = '' #関連当事者情報、連結財務諸表 [目次項目]
	NotesRelatedPartiesConsolidatedFinancialStatementsTextBlock = '' #関連当事者情報、連結財務諸表 [テキストブロック]
	NotesSpecialPurposeEntitiesSubjectToDisclosureConsolidatedFinancialStatementsHeading = '' #開示対象特別目的会社関係、連結財務諸表 [目次項目]
	NotesSpecialPurposeEntitiesSubjectToDisclosureConsolidatedFinancialStatementsTextBlock = '' #開示対象特別目的会社関係、連結財務諸表 [テキストブロック]
	NotesPerShareInformationConsolidatedFinancialStatementsHeading = '' #１株当たり情報、連結財務諸表 [目次項目]
	NotesPerShareInformationConsolidatedFinancialStatementsTextBlock = '' #１株当たり情報、連結財務諸表 [テキストブロック]
	NotesSignificantEventsAfterReportingPeriodConsolidatedFinancialStatementsHeading = '' #重要な後発事象、連結財務諸表 [目次項目]
	NotesSignificantEventsAfterReportingPeriodConsolidatedFinancialStatementsTextBlock = '' #重要な後発事象、連結財務諸表 [テキストブロック]
	NotesToConsolidatedFinancialStatementsJMISHeading = '' #連結財務諸表注記事項（JMIS） [目次項目]
	NotesToConsolidatedFinancialStatementsJMISTextBlock = '' #連結財務諸表注記事項（JMIS） [テキストブロック]
	NotesToConsolidatedFinancialStatementsUSGAAPHeading = '' #連結財務諸表注記事項（US GAAP） [目次項目]
	NotesToConsolidatedFinancialStatementsUSGAAPTextBlock = '' #連結財務諸表注記事項（US GAAP） [テキストブロック]
	AnnexedConsolidatedDetailedSchedulesHeading = '' #連結附属明細表 [目次項目]
	AnnexedConsolidatedDetailedScheduleOfCorporateBondsHeading = '' #社債明細表、連結財務諸表 [目次項目]
	AnnexedConsolidatedDetailedScheduleOfCorporateBondsTextBlock = '' #社債明細表、連結財務諸表 [テキストブロック]
	AnnexedConsolidatedDetailedScheduleOfBorrowingsHeading = '' #借入金等明細表、連結財務諸表 [目次項目]
	AnnexedConsolidatedDetailedScheduleOfBorrowingsTextBlock = '' #借入金等明細表、連結財務諸表 [テキストブロック]
	AnnexedConsolidatedDetailedScheduleOfAssetRetirementObligationsHeading = '' #資産除去債務明細表、連結財務諸表 [目次項目]
	AnnexedConsolidatedDetailedScheduleOfAssetRetirementObligationsTextBlock = '' #資産除去債務明細表、連結財務諸表 [テキストブロック]
	OtherInformationConsolidatedFinancialStatementsEtcHeading = '' #その他、連結財務諸表等 [目次項目]
	OtherInformationConsolidatedFinancialStatementsEtcTextBlock = '' #その他、連結財務諸表等 [テキストブロック]
	FinancialStatementsEtcHeading = '' #財務諸表等 [目次項目]
	FinancialStatementsHeading = '' #財務諸表 [目次項目]
	BalanceSheetHeading = '' #貸借対照表 [目次項目]
	BalanceSheetTextBlock = '' #貸借対照表 [テキストブロック]
	StatementOfIncomeHeading = '' #損益計算書 [目次項目]
	StatementOfIncomeTextBlock = '' #損益計算書 [テキストブロック]
	DetailedScheduleOfManufacturingCostTextBlock = '' #製造原価明細書 [テキストブロック]
	DetailedScheduleOfCostOfSalesTextBlock = '' #売上原価明細書 [テキストブロック]
	DetailedScheduleOfOperatingExpensesForRailwayBusinessTextBlock = '' #鉄道事業営業費明細表 [テキストブロック]
	DetailedScheduleOfOperatingExpensesForMotorwayBusinessTextBlock = '' #自動車道事業営業費明細表 [テキストブロック]
	DetailedScheduleOfOperatingExpensesTelecommunicationsBusinessTextBlock = '' #電気通信事業営業費用明細表 [テキストブロック]
	DetailedScheduleOfElectricUtilityOperatingExpensesTextBlock = '' #電気事業営業費用明細表 [テキストブロック]
	DetailedScheduleOfOperatingExpensesGASTextBlock = '' #営業費明細表、ガス事業 [テキストブロック]
	DetailedScheduleOfOperatingExpensesNonOperatingExpensesExtraordinaryLossesEtcForHighwayBusinessTextBlock = '' #高速道路事業営業費用、営業外費用及び特別損失等明細表 [テキストブロック]
	DetailedScheduleOfOperatingExpensesEDUTextBlock = '' #事業費用明細表、学校法人 [テキストブロック]
	StatementOfChangesInEquityHeading = '' #株主資本等変動計算書 [目次項目]
	StatementOfChangesInEquityTextBlock = '' #株主資本等変動計算書 [テキストブロック]
	StatementOfCashFlowsHeading = '' #キャッシュ・フロー計算書 [目次項目]
	StatementOfCashFlowsTextBlock = '' #キャッシュ・フロー計算書 [テキストブロック]
	NotesFinancialStatementsHeading = '' #注記事項、財務諸表 [目次項目]
	NotesUncertaintiesOfEntitysAbilityToContinueAsGoingConcernFinancialStatementsHeading = '' #継続企業の前提に関する事項、財務諸表 [目次項目]
	NotesUncertaintiesOfEntitysAbilityToContinueAsGoingConcernFinancialStatementsTextBlock = '' #継続企業の前提に関する事項、財務諸表 [テキストブロック]
	NotesSignificantAccountingPoliciesFinancialStatementsHeading = '' #重要な会計方針、財務諸表 [目次項目]
	NotesSignificantAccountingPoliciesFinancialStatementsTextBlock = '' #重要な会計方針、財務諸表 [テキストブロック]
	SignificantAccountingEstimatesFinancialStatementsHeading = '' #重要な会計上の見積り、財務諸表 [目次項目]
	SignificantAccountingEstimatesFinancialStatementsTextBlock = '' #重要な会計上の見積り、財務諸表 [テキストブロック]
	NotesChangesInAccountingPoliciesFinancialStatementsHeading = '' #会計方針の変更、財務諸表 [目次項目]
	NotesChangesInAccountingPoliciesInAccordanceWithChangesInAccountingStandardsEtcFinancialStatementsTextBlock = '' #会計基準等の改正等に伴う会計方針の変更、財務諸表 [テキストブロック]
	NotesVoluntaryChangesInAccountingPoliciesFinancialStatementsTextBlock = '' #会計基準等の改正等以外の正当な理由による会計方針の変更、財務諸表 [テキストブロック]
	NotesChangesInAccountingPoliciesWhichAreDifficultToDistinguishFromChangesInAccountingEstimatesFinancialStatementsTextBlock = '' #会計上の見積りの変更と区別することが困難な会計方針の変更、財務諸表 [テキストブロック]
	NotesNewAccountingStandardsNotYetAppliedFinancialStatementsHeading = '' #未適用の会計基準等、財務諸表 [目次項目]
	NotesNewAccountingStandardsNotYetAppliedFinancialStatementsTextBlock = '' #未適用の会計基準等、財務諸表 [テキストブロック]
	NotesChangesInPresentationFinancialStatementsHeading = '' #表示方法の変更、財務諸表 [目次項目]
	NotesChangesInPresentationFinancialStatementsTextBlock = '' #表示方法の変更、財務諸表 [テキストブロック]
	NotesChangesInAccountingEstimatesFinancialStatementsHeading = '' #会計上の見積りの変更、財務諸表 [目次項目]
	NotesChangesInAccountingEstimatesFinancialStatementsTextBlock = '' #会計上の見積りの変更、財務諸表 [テキストブロック]
	NotesRestatementFinancialStatementsHeading = '' #修正再表示、財務諸表 [目次項目]
	NotesRestatementFinancialStatementsTextBlock = '' #修正再表示、財務諸表 [テキストブロック]
	NotesAdditionalInformationFinancialStatementsHeading = '' #追加情報、財務諸表 [目次項目]
	NotesAdditionalInformationFinancialStatementsTextBlock = '' #追加情報、財務諸表 [テキストブロック]
	NotesBalanceSheetHeading = '' #貸借対照表関係 [目次項目]
	NotesBalanceSheetHeading = '' #貸借対照表関係 [目次項目]
	NotesBalanceSheetTable = '' #貸借対照表関係 [表]
	ConsolidatedOrNonConsolidatedAxis = '' #連結個別 [軸]
	NonConsolidatedMember = '' #非連結又は個別 [メンバー]
	NotesBalanceSheetLineItems = '' #貸借対照表関係 [表示項目]
	NotesRegardingInventoriesTextBlock = '' #棚卸資産の内訳の注記 [テキストブロック]
	MerchandiseAndFinishedGoods = '' #商品及び製品
	WorkInProcess = '' #仕掛品
	RawMaterialsAndSupplies = '' #原材料及び貯蔵品
	Inventories = '' #棚卸資産
	NotesRegardingAmountsOfNotesAndAccountsReceivableTradeAndContractAssetsTextBlock = '' #受取手形、売掛金及び契約資産の金額の注記 [テキストブロック]
	NotesReceivableTrade = '' #受取手形
	AllowanceForDoubtfulAccountsNotesReceivableTrade = '' #貸倒引当金、受取手形
	NotesReceivableTradeNet = '' #受取手形（純額）
	AccountsReceivableTrade = '' #売掛金
	AllowanceForDoubtfulAccountsAccountsReceivableTrade = '' #貸倒引当金、売掛金
	AccountsReceivableTradeNet = '' #売掛金（純額）
	ContractAssets = '' #契約資産
	AllowanceForDoubtfulAccountsContractAssets = '' #貸倒引当金、契約資産
	ContractAssetsNet = '' #契約資産（純額）
	NotesRegardingAllowancesDirectlyDeductedFromBalancesOfAssetsTextBlock = '' #資産の金額から直接控除している引当金の注記 [テキストブロック]
	AllowanceForDoubtfulAccountsCA = '' #貸倒引当金、流動資産、一括控除
	AllowanceForDoubtfulAccountsIOAByGroup = '' #貸倒引当金、投資その他の資産、一括控除
	AllowanceForDoubtfulAccountsAccountsReceivableTrade = '' #貸倒引当金、売掛金
	AllowanceForDoubtfulAccountsLongTermLoansReceivable = '' #貸倒引当金、長期貸付金
	AllowanceForDoubtfulAccountsClaimsInBankruptcyReorganizationClaimsAndOther = '' #貸倒引当金、破産更生債権等
	NotesRegardingAccumulatedDepreciationOfPropertyPlantAndEquipmentTextBlock = '' #有形固定資産の減価償却累計額の注記 [テキストブロック]
	AccumulatedDepreciationPPEByGroup = '' #減価償却累計額、有形固定資産、一括控除
	AccumulatedDepreciationBuildings = '' #減価償却累計額、建物
	AccumulatedDepreciationStructures = '' #減価償却累計額、構築物
	AccumulatedDepreciationMachineryAndEquipment = '' #減価償却累計額、機械及び装置
	NotesRegardingAmountsOfReductionEntryOfPropertyPlantAndEquipmentTextBlock = '' #有形固定資産の圧縮記帳額の注記 [テキストブロック]
	NotesRegardingPresentationOfAccumulatedImpairmentLossTextBlock = '' #減損損失累計額の表示に関する注記 [テキストブロック]
	NotesRegardingAssetsAndLiabilitiesIncurredFromTransactionsWithAffiliatedEntitiesTextBlock = '' #関係会社に関する資産・負債の注記 [テキストブロック]
	NotesRegardingRevaluationOfNonCurrentAssetsTextBlock = '' #固定資産の再評価に関する注記 [テキストブロック]
	NotesRegardingRevaluationOfLandForBusinessTextBlock = '' #事業用土地の再評価に関する注記 [テキストブロック]
	NotesRegardingPledgedAssetsTextBlock = '' #担保に供している資産の注記 [テキストブロック]
	NotesRegardingPresentationOfInventoriesAndProvisionForLossOnConstructionContractsTextBlock = '' #棚卸資産及び工事損失引当金の表示に関する注記 [テキストブロック]
	NotesRegardingAmountOfContractLiabilitiesTextBlock = '' #契約負債の金額の注記 [テキストブロック]
	ContractLiabilities = '' #契約負債
	NotesRegardingReservesUnderSpecialLawsTextBlock = '' #特別法上の準備金等に関する注記 [テキストブロック]
	NotesRegardingProvisionIncurredFromBusinessCombinationTextBlock = '' #企業結合に係る特定勘定の注記 [テキストブロック]
	NotesRegardingGuaranteeObligationsTextBlock = '' #保証債務の注記 [テキストブロック]
	NotesRegardingTradeNotesReceivableDiscountedOrTransferredByEndorsementTextBlock = '' #受取手形割引高及び（又は）受取手形裏書譲渡高 [テキストブロック]
	DiscountedTradeNotesReceivable = '' #受取手形割引高
	TradeNotesReceivableTransferredByEndorsement = '' #受取手形裏書譲渡高
	NotesRegardingDepositForSubscriptionsToSharesTextBlock = '' #新株式申込証拠金に関する注記 [テキストブロック]
	NotesRegardingLimitationsOnDividendTextBlock = '' #配当制限に関する注記 [テキストブロック]
	NotesRegardingPresentationOfNetAssetsOfDesignatedCorporationTextBlock = '' #指定法人の純資産の記載に関する注記 [テキストブロック]
	NotesRegardingPromissoryNotesDueOnBalanceSheetDateTextBlock = '' #期末日満期手形の会計処理 [テキストブロック]
	OtherElementsForNotesBalanceSheetAbstract = '' #貸借対照表関係のその他の要素 [タイトル項目]
	NotesRegardingLoanedWhichBorrowerHasRightToSellOrRepledgeTextBlock = '' #消費貸借契約及び（又は）消費寄託契約により貸し付けている有価証券に関する注記 [テキストブロック]
	NotesRegardingFinancialAssetsBorrowedWhichBorrowerHasRightToSellOrRepledgeTextBlock = '' #自由処分権を有する担保受入金融資産に関する注記 [テキストブロック]
	NotesRegardingLoanedSecuritiesAndFinancialAssetsBorrowedWhichBorrowerHasRightToSellOrRepledgeTextBlock = '' #有価証券の消費貸借契約・消費寄託契約及び自由処分権を有する担保受入金融資産に関する注記 [テキストブロック]
	NotesRegardingLoanParticipationsTextBlock = '' #ローン・パーティシペーションに関する注記 [テキストブロック]
	CreditorsNotesRegardingOverdraftContractsAndOrLoanCommitmentsTextBlock = '' #当座貸越契約及び（又は）貸出コミットメントに関する貸手の注記 [テキストブロック]
	DebtorsNotesRegardingOverdraftContractsAndOrLoanCommitmentsTextBlock = '' #当座貸越契約及び（又は）貸出コミットメントに関する借手の注記 [テキストブロック]
	NotesRegardingTotalAmountsOfSharesOfAndOrLoansToAffiliatedEntitiesTextBlock = '' #関係会社の株式及び（又は）出資金の総額 [テキストブロック]
	NotesRegardingTotalAmountsOfSharesOfAndOrLoansToUnconsolidatedSubsidiariesAndAssociatesTextBlock = '' #非連結子会社及び関連会社の株式及び（又は）出資金の総額 [テキストブロック]
	NotesRegardingSubordinatedBorrowingsTextBlock = '' #劣後特約付借入金に関する注記 [テキストブロック]
	NotesRegardingSubordinatedBondsPayableTextBlock = '' #劣後特約付社債に関する注記 [テキストブロック]
	NotesRegardingGuaranteeObligationForCorporateBondsIncludedInAssetsTextBlock = '' #資産の部の社債に係る保証債務に関する注記 [テキストブロック]
	OtherElementsForNotesBalanceSheetOfBankAbstract = '' #銀行業の貸借対照表関係のその他の要素 [タイトル項目]
	NotesRegardingLoansBasedOnBankingActAndActOnEmergencyMeasuresForRevitalizationOfFinancialFunctionsBNKTextBlock = '' #銀行法及び金融機能の再生のための緊急措置に関する法律に基づく債権に関する注記、銀行業 [テキストブロック]
	NotesRegardingBillsDiscountedInBankingIndustryBNKTextBlock = '' #銀行業における手形割引に関する注記、銀行業 [テキストブロック]
	OtherElementsForNotesBalanceSheetOfSecuritiesRelatedBusinessAbstract = '' #第一種金融商品取引業の貸借対照表関係のその他の要素 [タイトル項目]
	NotesRegardingMarketValueOfSecuritiesPledgedToCounterpartiesSECTextBlock = '' #差し入れた有価証券等の時価の注記、第一種金融商品取引業 [テキストブロック]
	NotesRegardingMarketValueOfSecuritiesReceivedAsCollateralFromCounterpartiesSECTextBlock = '' #差し入れを受けた有価証券等の時価の注記、第一種金融商品取引業 [テキストブロック]
	BreakdownOfTradingAccountSecuritiesEtcSECTextBlock = '' #商品有価証券等の内訳、第一種金融商品取引業 [テキストブロック]
	OtherElementsForNotesBalanceSheetOfInsuranceAbstract = '' #保険業の貸借対照表関係のその他の要素 [タイトル項目]
	NotesRegardingLoansBasedOnInsuranceBusinessActINSTextBlock = '' #保険業法に基づく債権に関する注記、保険業 [テキストブロック]
	NotesRegardingAssetsAndLiabilitiesIncludedInSpecificAccountsSpecifiedByArticle118OfInsuranceBusinessActINSTextBlock = '' #保険業法第118条に規定する特別勘定の資産及び負債に関する注記、保険業 [テキストブロック]
	NotesRegardingDeferredAssetsIncludedInOtherAssetsSpecifiedByArticle113OfInsuranceBusinessActTextBlock = '' #その他資産に含まれている保険業法第113条に規定する事業費の繰延額の注記 [テキストブロック]
	NotesRegardingIncreaseAndDecreaseInReserveForPolicyholderDividendsAndPaymentsOfPolicyholderDividendsINSTextBlock = '' #契約者配当準備金の増減異動及び契約者配当金の支払額に関する注記、保険業 [テキストブロック]
	NotesRegardingSurplusFromOrganizationChangeSpecifiedByArticle91OfInsuranceBusinessActINSTextBlock = '' #保険業法第91条の規定による組織変更剰余金額の注記、保険業 [テキストブロック]
	NotesRegardingReservesForOutstandingClaimsReinsuredINSTextBlock = '' #保険業法施行規則第73条第3項において準用する同規則第71条第1項に規定する再保険を付した部分に相当する支払備金の金額の注記、保険業 [テキストブロック]
	NotesRegardingPolicyReservesReinsuredINSTextBlock = '' #保険業法施行規則第71条第1項に規定する再保険を付した部分に相当する責任準備金の金額の注記、保険業 [テキストブロック]
	NotesRegardingObligationsToLifeInsurancePolicyholdersProtectionCorporationOfJapanINSTextBlock = '' #保険業法第259条の規定に基づく生命保険契約者保護機構に対する今後の負担見積額、保険業 [テキストブロック]
	BreakdownOfOutstandingClaimsINSTextBlock = '' #支払備金の内訳、保険業 [テキストブロック]
	BreakdownOfPolicyReserveINSTextBlock = '' #責任準備金の内訳、保険業 [テキストブロック]
	OtherElementsForNotesBalanceSheetOfSpecificFinanceAbstract = '' #特定金融業の貸借対照表関係のその他の要素 [タイトル項目]
	NotesRegardingBadLoansSPFTextBlock = '' #不良債権に関する注記、特定金融業 [テキストブロック]
	OtherElementsForNotesBalanceSheetOfCommodityFutureTradingAbstract = '' #商品先物取引業の貸借対照表関係のその他の要素 [タイトル項目]
	ExplanationOfFuturesTransactionMarginCustomerCMDTextBlock = '' #委託者先物取引差金の説明、商品先物取引業 [テキストブロック]
	NotesStatementOfIncomeHeading = '' #損益計算書関係 [目次項目]
	NotesStatementOfIncomeHeading = '' #損益計算書関係 [目次項目]
	NotesStatementOfIncomeTable = '' #損益計算書関係 [表]
	ConsolidatedOrNonConsolidatedAxis = '' #連結個別 [軸]
	NonConsolidatedMember = '' #非連結又は個別 [メンバー]
	NotesStatementOfIncomeLineItems = '' #損益計算書関係 [表示項目]
	NotesRegardingAmountOfRevenueFromContractsWithCustomersTextBlock = '' #顧客との契約から生じる収益の金額の注記 [テキストブロック]
	RevenueFromContractsWithCustomers = '' #顧客との契約から生じる収益
	NotesRegardingRevenueFromAffiliatedEntitiesTextBlock = '' #関係会社に対する売上高の注記 [テキストブロック]
	NotesRegardingLossOnConstructionContractsTextBlock = '' #工事損失引当金繰入額の注記 [テキストブロック]
	NotesRegardingWriteDownsOfInventoriesTextBlock = '' #棚卸資産の帳簿価額の切下げに関する注記 [テキストブロック]
	WriteDownsOfInventories = '' #棚卸資産帳簿価額切下額
	MajorComponentsOfSellingGeneralAndAdministrativeExpensesTextBlock = '' #主要な販売費及び一般管理費 [テキストブロック]
	DepreciationSGA = '' #減価償却費、販売費及び一般管理費
	ProvisionOfAllowanceForDoubtfulAccountsSGA = '' #貸倒引当金繰入額、販売費及び一般管理費
	MajorComponentsOfSellingExpensesAbstract = '' #主要な販売費 [タイトル項目]
	RetirementBenefitExpensesSellingExpenses = '' #退職給付費用、販売費
	DepreciationSellingExpenses = '' #減価償却費、販売費
	ProvisionForBonusesSellingExpenses = '' #賞与引当金繰入額、販売費
	MajorComponentsOfGeneralAndAdministrativeExpensesAbstract = '' #主要な一般管理費 [タイトル項目]
	RetirementBenefitExpensesGA = '' #退職給付費用、一般管理費
	DepreciationGA = '' #減価償却費、一般管理費
	ProvisionForBonusesGA = '' #賞与引当金繰入額、一般管理費
	ResearchAndDevelopmentExpensesIncludedInGeneralAndAdministrativeExpensesAndManufacturingCostForCurrentPeriodTextBlock = '' #一般管理費及び当期製造費用に含まれる研究開発費 [テキストブロック]
	ResearchAndDevelopmentExpensesIncludedInGeneralAndAdministrativeExpensesAndManufacturingCostForCurrentPeriod = '' #一般管理費及び当期製造費用に含まれる研究開発費
	ResearchAndDevelopmentExpensesSGA = '' #研究開発費、販売費及び一般管理費
	NotesRegardingOperatingExpensesIncurredFromTransactionsWithAffiliatedEntitiesTextBlock = '' #関係会社に係る営業費用の注記 [テキストブロック]
	NotesRegardingNonOperatingIncomeAndNonOperatingExpensesIncurredFromTransactionsWithAffiliatedEntitiesTextBlock = '' #関係会社に係る営業外収益・営業外費用の注記 [テキストブロック]
	NotesRegardingTotalAmountOfOperatingTransactionsFromOrToAffiliatedEntitiesAndTotalAmountOfNonOperatingTransactionsFromOrToAffiliatedEntitiesTextBlock = '' #関係会社との営業取引による取引高の総額及び営業取引以外の取引による取引高の総額の注記 [テキストブロック]
	NotesRegardingImpairmentLossTextBlock = '' #減損損失に関する注記 [テキストブロック]
	NotesRegardingReversalOfProvisionIncurredFromBusinessCombinationTextBlock = '' #企業結合に係る特定勘定の取崩益の注記 [テキストブロック]
	NotesRegardingGainOnSalesOfPropertyPlantAndEquipmentTextBlock = '' #固定資産売却益の注記 [テキストブロック]
	NotesRegardingLossOnSalesOfPropertyPlantAndEquipmentTextBlock = '' #固定資産売却損の注記 [テキストブロック]
	NotesRegardingLossOnDisposalOfPropertyPlantAndEquipmentTextBlock = '' #固定資産除却損の注記 [テキストブロック]
	NotesRegardingLossOnDisposalAndSalesOfPropertyPlantAndEquipmentTextBlock = '' #固定資産除売却損の注記 [テキストブロック]
	OtherElementsForNotesStatementOfIncomeAbstract = '' #損益計算書関係のその他の要素 [タイトル項目]
	BreakdownOfBusinessCostTextBlock = '' #事業費の内訳 [テキストブロック]
	BreakdownOfPersonnelExpensesTextBlock = '' #人件費の内訳 [テキストブロック]
	BreakdownOfGainOnSalesOfSecuritiesTextBlock = '' #有価証券売却益の内訳 [テキストブロック]
	BreakdownOfLossOnSalesOfSecuritiesTextBlock = '' #有価証券売却損の内訳 [テキストブロック]
	BreakdownOfLossOnValuationOfSecuritiesTextBlock = '' #有価証券評価損の内訳 [テキストブロック]
	NotesRegardingTransactionsWithAffiliatedEntitiesTextBlock = '' #関係会社との取引に関する注記 [テキストブロック]
	OtherElementsForNotesStatementOfIncomeOfBankAbstract = '' #銀行業の損益計算書関係のその他の要素 [タイトル項目]
	MajorComponentsOfOtherIncomeBNKTextBlock = '' #その他の経常収益の主要な内訳、銀行業 [テキストブロック]
	MajorComponentsOfOtherExpensesBNKTextBlock = '' #その他の経常費用の主要な内訳、銀行業 [テキストブロック]
	OtherElementsForNotesStatementOfIncomeOfSecuritiesRelatedBusinessAbstract = '' #第一種金融商品取引業の損益計算書関係のその他の要素 [タイトル項目]
	BreakdownOfNetTradingIncomeSECTextBlock = '' #トレーディング損益の内訳、第一種金融商品取引業 [テキストブロック]
	BreakdownOfFinancialRevenueSECTextBlock = '' #金融収益の内訳、第一種金融商品取引業 [テキストブロック]
	BreakdownOfFinancialExpensesSECTextBlock = '' #金融費用の内訳、第一種金融商品取引業 [テキストブロック]
	OtherElementsForNotesStatementOfIncomeOfInsuranceAbstract = '' #保険業の損益計算書関係のその他の要素 [タイトル項目]
	MajorComponentsOfBusinessCostTextBlock = '' #事業費の主な内訳 [テキストブロック]
	AgentFeeEtcINSNonlife = '' #代理店手数料等、損害保険業
	SalariesINSNonlife = '' #給与、損害保険業
	BreakdownOfNetPremiumsWrittenINSTextBlock = '' #正味収入保険料の内訳、保険業 [テキストブロック]
	BreakdownOfNetClaimsPaidINSTextBlock = '' #正味支払保険金の内訳、保険業 [テキストブロック]
	BreakdownOfCommissionsAndCollectionFeesINSTextBlock = '' #諸手数料及び集金費の内訳、保険業 [テキストブロック]
	BreakdownOfProvisionForOrReversalOfOutstandingClaimsINSTextBlock = '' #支払備金繰入額又は支払備金戻入額の内訳、保険業 [テキストブロック]
	BreakdownOfProvisionForOrReversalOfUnderwritingReservesINSTextBlock = '' #責任準備金繰入額又は責任準備金戻入額の内訳、保険業 [テキストブロック]
	NotesRegardingReversalOfOrProvisionForReservesForOutstandingClaimsReinsuredINSTextBlock = '' #支払備金繰入額又は支払備金戻入額の計算上、差し引かれた又は足し上げられた出再支払備金繰入額又は出再支払備金戻入額の注記、保険業 [テキストブロック]
	NotesRegardingReversalOfOrProvisionForPolicyReservesReinsuredINSTextBlock = '' #責任準備金繰入額又は責任準備金戻入額の計算上、差し引かれた又は足し上げられた出再責任準備金繰入額又は出再責任準備金戻入額の注記、保険業 [テキストブロック]
	BreakdownOfInterestAndDividendIncomeBySourceAssetINSTextBlock = '' #利息及び配当金収入の資産源泉別内訳、保険業 [テキストブロック]
	InterestAndDividendIncomeGainLossOnSalesAndUnrealizedGainLossForEachOfTradingAccountSecuritiesINSTextBlock = '' #商品有価証券及び売買目的有価証券に係るそれぞれの利息及び配当金収入、売却損益及び評価損益の金額、保険業 [テキストブロック]
	NotesRegardingUnrealizedGainLossForMoneyTrustINSTextBlock = '' #金銭の信託に係る評価損益の金額の注記、保険業 [テキストブロック]
	NotesRegardingUnrealizedGainLossForDerivativesINSTextBlock = '' #金融派生商品に係る評価損益の金額の注記、保険業 [テキストブロック]
	MajorComponentsOfOtherExtraordinaryIncomeINSTextBlock = '' #その他特別利益の主な内訳、保険業 [テキストブロック]
	MajorComponentsOfOtherExtraordinaryLossesINSTextBlock = '' #その他特別損失の主な内訳、保険業 [テキストブロック]
	OtherElementsForNotesStatementOfIncomeOfCommodityFutureTradingAbstract = '' #商品先物取引業の損益計算書関係のその他の要素 [タイトル項目]
	BreakdownOfBrokerageIncomeCMDTextBlock = '' #受取手数料の内訳、商品先物取引業 [テキストブロック]
	BreakdownOfNetGainOnTradingCMDTextBlock = '' #売買損益の内訳、商品先物取引業 [テキストブロック]
	ExchangeRelatedExpensesCMDTextBlock = '' #取引所等関係費の内訳、商品先物取引業 [テキストブロック]
	NotesStatementOfChangesInEquityHeading = '' #株主資本等変動計算書関係 [目次項目]
	NotesStatementOfChangesInEquityHeading = '' #株主資本等変動計算書関係 [目次項目]
	NotesStatementOfChangesInEquityTable = '' #株主資本等変動計算書関係 [表]
	ConsolidatedOrNonConsolidatedAxis = '' #連結個別 [軸]
	NonConsolidatedMember = '' #非連結又は個別 [メンバー]
	NotesStatementOfChangesInEquityLineItems = '' #株主資本等変動計算書関係 [表示項目]
	NotesRegardingIssuedSharesAndTreasurySharesTextBlock = '' #発行済株式及び自己株式に関する注記 [テキストブロック]
	NotesRegardingTreasurySharesTextBlock = '' #自己株式に関する注記 [テキストブロック]
	NotesRegardingNewShareSubscriptionRightsEtcTextBlock = '' #新株予約権等に関する注記 [テキストブロック]
	NotesRegardingDividendTextBlock = '' #配当に関する注記 [テキストブロック]
	NotesStatementOfCashFlowsHeading = '' #キャッシュ・フロー計算書関係 [目次項目]
	NotesStatementOfCashFlowsHeading = '' #キャッシュ・フロー計算書関係 [目次項目]
	NotesStatementOfCashFlowsTable = '' #キャッシュ・フロー計算書関係 [表]
	ConsolidatedOrNonConsolidatedAxis = '' #連結個別 [軸]
	NonConsolidatedMember = '' #非連結又は個別 [メンバー]
	NotesStatementOfCashFlowsLineItems = '' #キャッシュ・フロー計算書関係 [表示項目]
	ReconciliationOfEndingBalanceOfCashAndCashEquivalentsWithAccountBalancesPerBalanceSheetTextBlock = '' #現金及び現金同等物の期末残高と貸借対照表に掲記されている科目の金額との関係 [テキストブロック]
	MajorComponentsOfAssetsAndLiabilitiesIncreasedOrDecreasedAsResultOfAcquisitionOrDisposalOfBusinessOrMergerEtcWherebyCashWasPaidOrReceivedAsConsiderationTextBlock = '' #現金及び現金同等物を対価とする事業の譲受け若しくは譲渡又は合併等を行った場合には、当該事業の譲受け若しくは譲渡又は合併等により増加又は減少した資産及び負債の主な内訳 [テキストブロック]
	DescriptionOfSignificantTransactionsNotRequiringUseOfCashOrCashEquivalentsTextBlock = '' #重要な非資金取引の内容 [テキストブロック]
	DescriptionOfFactThatCashFlowsFromUsedInInvestingActivitiesIncludeCashFlowsFromAssetManagementActivitiesRelatedToInsuranceBusinessINSTextBlock = '' #投資活動によるキャッシュ・フローには、保険事業に係る資産運用業務から生じるキャッシュ・フローを含んでいる旨、保険業 [テキストブロック]
	NotesLeasesFinancialStatementsHeading = '' #リース取引関係、財務諸表 [目次項目]
	NotesLeasesFinancialStatementsTextBlock = '' #リース取引関係、財務諸表 [テキストブロック]
	NotesFinancialInstrumentsFinancialStatementsHeading = '' #金融商品関係、財務諸表 [目次項目]
	NotesFinancialInstrumentsFinancialStatementsTextBlock = '' #金融商品関係、財務諸表 [テキストブロック]
	NotesSecuritiesFinancialStatementsHeading = '' #有価証券関係、財務諸表 [目次項目]
	NotesSecuritiesFinancialStatementsTextBlock = '' #有価証券関係、財務諸表 [テキストブロック]
	NotesMoneyHeldInTrustFinancialStatementsHeading = '' #金銭の信託関係、財務諸表 [目次項目]
	NotesMoneyHeldInTrustFinancialStatementsTextBlock = '' #金銭の信託関係、財務諸表 [テキストブロック]
	NotesValuationDifferenceOnAvailableForSaleSecuritiesFinancialStatementsHeading = '' #その他有価証券評価差額金、財務諸表 [目次項目]
	NotesValuationDifferenceOnAvailableForSaleSecuritiesFinancialStatementsTextBlock = '' #その他有価証券評価差額金、財務諸表 [テキストブロック]
	NotesDerivativesFinancialStatementsHeading = '' #デリバティブ取引関係、財務諸表 [目次項目]
	NotesDerivativesFinancialStatementsTextBlock = '' #デリバティブ取引関係、財務諸表 [テキストブロック]
	NotesRetirementBenefitsFinancialStatementsHeading = '' #退職給付関係、財務諸表 [目次項目]
	NotesRetirementBenefitsFinancialStatementsTextBlock = '' #退職給付関係、財務諸表 [テキストブロック]
	NotesShareOptionsEtcFinancialStatementsHeading = '' #ストック・オプション等関係、財務諸表 [目次項目]
	NotesShareOptionsEtcFinancialStatementsTextBlock = '' #ストック・オプション等関係、財務諸表 [テキストブロック]
	NotesTaxEffectAccountingFinancialStatementsHeading = '' #税効果会計関係、財務諸表 [目次項目]
	NotesTaxEffectAccountingFinancialStatementsTextBlock = '' #税効果会計関係、財務諸表 [テキストブロック]
	NotesBusinessCombinationsFinancialStatementsHeading = '' #企業結合等関係、財務諸表 [目次項目]
	NotesBusinessCombinationsFinancialStatementsTextBlock = '' #企業結合等関係、財務諸表 [テキストブロック]
	NotesAssetRetirementObligationsFinancialStatementsHeading = '' #資産除去債務関係、財務諸表 [目次項目]
	NotesAssetRetirementObligationsFinancialStatementsTextBlock = '' #資産除去債務関係、財務諸表 [テキストブロック]
	NotesRealEstateForLeaseEtcFinancialStatementsHeading = '' #賃貸等不動産関係、財務諸表 [目次項目]
	NotesRealEstateForLeaseEtcFinancialStatementsTextBlock = '' #賃貸等不動産関係、財務諸表 [テキストブロック]
	NotesRevenueRecognitionFinancialStatementsHeading = '' #収益認識関係、財務諸表 [目次項目]
	NotesRevenueRecognitionFinancialStatementsTextBlock = '' #収益認識関係、財務諸表 [テキストブロック]
	NotesInventoriesFinancialStatementsHeading = '' #棚卸資産関係、財務諸表 [目次項目]
	NotesInventoriesFinancialStatementsTextBlock = '' #棚卸資産関係、財務諸表 [テキストブロック]
	NotesSegmentInformationEtcFinancialStatementsHeading = '' #セグメント情報等、財務諸表 [目次項目]
	NotesSegmentInformationEtcFinancialStatementsTextBlock = '' #セグメント情報等、財務諸表 [テキストブロック]
	NotesSegmentInformationEtcFinancialStatementsHeading = '' #セグメント情報等、財務諸表 [目次項目]
	NotesSegmentInformationEtcFinancialStatementsTable = '' #セグメント情報等、財務諸表 [表]
	ConsolidatedOrNonConsolidatedAxis = '' #連結個別 [軸]
	NonConsolidatedMember = '' #非連結又は個別 [メンバー]
	NotesSegmentInformationEtcFinancialStatementsLineItems = '' #セグメント情報等、財務諸表 [表示項目]
	SegmentInformationAbstract = '' #セグメント情報 [タイトル項目]
	DescriptionOfReportableSegmentsTextBlock = '' #報告セグメントの概要 [テキストブロック]
	DisclosureOfChangesInReportableSegmentsTextBlock = '' #報告セグメントの変更に関する事項 [テキストブロック]
	DescriptionOfFactThatCompanysBusinessComprisesSingleSegment = '' #単一セグメントである旨
	ExplanationOfMeasurementsOfSalesProfitLossAssetLiabilityAndOtherItemsForEachReportableSegmentTextBlock = '' #報告セグメントごとの売上高、利益又は損失、資産、負債その他の項目の金額の算定方法 [テキストブロック]
	NotesSegmentInformationEtcFinancialStatementsHeading = '' #セグメント情報等、財務諸表 [目次項目]
	SegmentInformationAbstract = '' #セグメント情報 [タイトル項目]
	DisclosureOfSalesProfitLossAssetLiabilityAndOtherItemsForEachReportableSegmentTable = '' #報告セグメントごとの売上高、利益又は損失、資産、負債その他の項目の金額に関する情報 [表]
	ConsolidatedOrNonConsolidatedAxis = '' #連結個別 [軸]
	NonConsolidatedMember = '' #非連結又は個別 [メンバー]
	OperatingSegmentsAxis = '' #事業セグメント [軸]
	EntityTotalMember = '' #連結合計又は会社合計 [メンバー] ※ディメンションデフォルト
	TotalOfReportableSegmentsAndOthersMember = '' #報告セグメント及びその他の合計 [メンバー]
	ReportableSegmentsMember = '' #報告セグメント [メンバー]
	OtherReportableSegmentsMember = '' #その他の報告セグメント [メンバー]
	OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember = '' #報告セグメント以外の全てのセグメント [メンバー]
	ReconcilingItemsMember = '' #調整項目 [メンバー]
	DisclosureOfSalesProfitLossAssetLiabilityAndOtherItemsForEachReportableSegmentLineItems = '' #報告セグメントごとの売上高、利益又は損失、資産、負債その他の項目の金額に関する情報 [表示項目]
	SalesSegmentInformationAbstract = '' #売上高、セグメント情報 [タイトル項目]
	RevenuesFromExternalCustomers = '' #外部顧客への売上高
	TransactionsWithOtherSegments = '' #セグメント間の内部売上高又は振替高
	NetSales = '' #売上高
	OperatingRevenue1 = '' #営業収益
	OperatingRevenue2 = '' #営業収入
	GrossOperatingRevenue = '' #営業総収入
	OrdinaryIncomeBNK = '' #経常収益、銀行業
	OperatingIncomeINS = '' #経常収益、保険業
	SegmentProfitLossAbstract = '' #セグメント利益又は損失（△） [タイトル項目]
	OperatingIncome = '' #営業利益又は営業損失（△）
	OrdinaryIncome = '' #経常利益又は経常損失（△）
	IncomeBeforeIncomeTaxes = '' #税引前当期純利益又は税引前当期純損失（△）
	ProfitLoss = '' #当期純利益又は当期純損失（△）（平成26年3月28日財規等改正後）
	Assets = '' #資産
	Liabilities = '' #負債
	OtherItemsSegmentInformationAbstract = '' #その他の項目、セグメント情報 [タイトル項目]
	DepreciationSegmentInformation = '' #減価償却費、セグメント情報
	AmortizationOfGoodwillSGA = '' #のれん償却額、販売費及び一般管理費
	InterestIncomeNOI = '' #受取利息、営業外収益
	InterestExpensesNOE = '' #支払利息、営業外費用
	ExtraordinaryIncome = '' #特別利益
	GainOnNegativeGoodwillEI = '' #負ののれん発生益、特別利益
	ExtraordinaryLoss = '' #特別損失
	ImpairmentLossEL = '' #減損損失、特別損失
	IncomeTaxExpense = '' #税金費用
	IncreaseInPropertyPlantAndEquipmentAndIntangibleAssets = '' #有形固定資産及び無形固定資産の増加額
	NotesSegmentInformationEtcFinancialStatementsHeading = '' #セグメント情報等、財務諸表 [目次項目]
	NotesSegmentInformationEtcFinancialStatementsTable = '' #セグメント情報等、財務諸表 [表]
	ConsolidatedOrNonConsolidatedAxis = '' #連結個別 [軸]
	NonConsolidatedMember = '' #非連結又は個別 [メンバー]
	NotesSegmentInformationEtcFinancialStatementsLineItems = '' #セグメント情報等、財務諸表 [表示項目]
	SegmentInformationAbstract = '' #セグメント情報 [タイトル項目]
	FootnotesRegardingSegmentInformationTableTextBlock = '' #セグメント表の脚注 [テキストブロック]
	DescriptionOfNatureAndAmountsOfDifferencesBetweenReportableSegmentsTotalAndFinancialStatementsTextBlock = '' #報告セグメント合計額と財務諸表計上額との差額及び当該差額の主な内容（差異調整に関する事項） [テキストブロック]
	NotesInformationAssociatedWithReportableSegmentsAbstract = '' #関連情報 [タイトル項目]
	InformationForEachProductOrServiceTextBlock = '' #製品及びサービスごとの情報 [テキストブロック]
	InformationForEachRegionAbstract = '' #地域ごとの情報 [タイトル項目]
	RevenuesFromExternalCustomersInformationForEachRegionTextBlock = '' #売上高、地域ごとの情報 [テキストブロック]
	PropertyPlantAndEquipmentInformationForEachRegionTextBlock = '' #有形固定資産、地域ごとの情報 [テキストブロック]
	InformationForEachOfMainCustomersTextBlock = '' #主要な顧客ごとの情報 [テキストブロック]
	NotesSegmentInformationEtcFinancialStatementsHeading = '' #セグメント情報等、財務諸表 [目次項目]
	DisclosureOfImpairmentLossOnNonCurrentAssetsForEachReportableSegmentAbstract = '' #報告セグメントごとの固定資産の減損損失に関する情報 [タイトル項目]
	DisclosureOfImpairmentLossOnNonCurrentAssetsForEachReportableSegmentTable = '' #報告セグメントごとの固定資産の減損損失に関する情報 [表]
	ConsolidatedOrNonConsolidatedAxis = '' #連結個別 [軸]
	NonConsolidatedMember = '' #非連結又は個別 [メンバー]
	OperatingSegmentsAxis = '' #事業セグメント [軸]
	EntityTotalMember = '' #連結合計又は会社合計 [メンバー] ※ディメンションデフォルト
	ReportableSegmentsMember = '' #報告セグメント [メンバー]
	OtherReportableSegmentsMember = '' #その他の報告セグメント [メンバー]
	OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember = '' #報告セグメント以外の全てのセグメント [メンバー]
	UnallocatedAmountsAndEliminationMember = '' #全社・消去 [メンバー]
	DisclosureOfImpairmentLossOnNonCurrentAssetsForEachReportableSegmentLineItems = '' #報告セグメントごとの固定資産の減損損失に関する情報 [表示項目]
	ImpairmentLossEL = '' #減損損失、特別損失
	NotesSegmentInformationEtcFinancialStatementsHeading = '' #セグメント情報等、財務諸表 [目次項目]
	NotesSegmentInformationEtcFinancialStatementsTable = '' #セグメント情報等、財務諸表 [表]
	ConsolidatedOrNonConsolidatedAxis = '' #連結個別 [軸]
	NonConsolidatedMember = '' #非連結又は個別 [メンバー]
	NotesSegmentInformationEtcFinancialStatementsLineItems = '' #セグメント情報等、財務諸表 [表示項目]
	DescriptionOfImpairmentLossNotAllocatedToReportableSegments = '' #報告セグメントに配分されていない減損損失の内容
	NotesSegmentInformationEtcFinancialStatementsHeading = '' #セグメント情報等、財務諸表 [目次項目]
	AmortizationAndUnamortizedBalanceOfGoodwillForEachReportableSegmentAbstract = '' #報告セグメントごとののれんの償却額及び未償却残高に関する情報 [タイトル項目]
	AmortizationAndUnamortizedBalanceOfGoodwillForEachReportableSegmentTable = '' #報告セグメントごとののれんの償却額及び未償却残高に関する情報 [表]
	ConsolidatedOrNonConsolidatedAxis = '' #連結個別 [軸]
	NonConsolidatedMember = '' #非連結又は個別 [メンバー]
	OperatingSegmentsAxis = '' #事業セグメント [軸]
	EntityTotalMember = '' #連結合計又は会社合計 [メンバー] ※ディメンションデフォルト
	ReportableSegmentsMember = '' #報告セグメント [メンバー]
	OtherReportableSegmentsMember = '' #その他の報告セグメント [メンバー]
	OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember = '' #報告セグメント以外の全てのセグメント [メンバー]
	UnallocatedAmountsAndEliminationMember = '' #全社・消去 [メンバー]
	AmortizationAndUnamortizedBalanceOfGoodwillForEachReportableSegmentLineItems = '' #報告セグメントごとののれんの償却額及び未償却残高に関する情報 [表示項目]
	AmortizationOfGoodwillSGA = '' #のれん償却額、販売費及び一般管理費
	Goodwill = '' #のれん
	GoodwillBeforeOffsetting = '' #のれん（相殺前）
	NotesSegmentInformationEtcFinancialStatementsHeading = '' #セグメント情報等、財務諸表 [目次項目]
	AmortizationAndUnamortizedBalanceOfNegativeGoodwillForEachReportableSegmentAbstract = '' #報告セグメントごとの負ののれんの償却額及び未償却残高に関する情報 [タイトル項目]
	AmortizationAndUnamortizedBalanceOfNegativeGoodwillForEachReportableSegmentTable = '' #報告セグメントごとの負ののれんの償却額及び未償却残高に関する情報 [表]
	ConsolidatedOrNonConsolidatedAxis = '' #連結個別 [軸]
	NonConsolidatedMember = '' #非連結又は個別 [メンバー]
	OperatingSegmentsAxis = '' #事業セグメント [軸]
	EntityTotalMember = '' #連結合計又は会社合計 [メンバー] ※ディメンションデフォルト
	ReportableSegmentsMember = '' #報告セグメント [メンバー]
	OtherReportableSegmentsMember = '' #その他の報告セグメント [メンバー]
	OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember = '' #報告セグメント以外の全てのセグメント [メンバー]
	UnallocatedAmountsAndEliminationMember = '' #全社・消去 [メンバー]
	AmortizationAndUnamortizedBalanceOfNegativeGoodwillForEachReportableSegmentLineItems = '' #報告セグメントごとの負ののれんの償却額及び未償却残高に関する情報 [表示項目]
	AmortizationOfNegativeGoodwillNOI = '' #負ののれん償却額、営業外収益
	NegativeGoodwill = '' #負ののれん
	NegativeGoodwillBeforeOffsetting = '' #負ののれん（相殺前）
	NotesSegmentInformationEtcFinancialStatementsHeading = '' #セグメント情報等、財務諸表 [目次項目]
	NotesSegmentInformationEtcFinancialStatementsTable = '' #セグメント情報等、財務諸表 [表]
	ConsolidatedOrNonConsolidatedAxis = '' #連結個別 [軸]
	NonConsolidatedMember = '' #非連結又は個別 [メンバー]
	NotesSegmentInformationEtcFinancialStatementsLineItems = '' #セグメント情報等、財務諸表 [表示項目]
	DescriptionOfAmortizationOfGoodwillOrUnamortizedBalanceOfGoodwillNotAllocatedToReportableSegments = '' #報告セグメントに配分されていないのれんの償却額又は未償却残高の内容
	NotesSegmentInformationEtcFinancialStatementsHeading = '' #セグメント情報等、財務諸表 [目次項目]
	InformationAboutGainOnBargainPurchaseForEachReportableSegmentTable = '' #報告セグメントごとの負ののれん発生益に関する情報 [表]
	ConsolidatedOrNonConsolidatedAxis = '' #連結個別 [軸]
	NonConsolidatedMember = '' #非連結又は個別 [メンバー]
	OperatingSegmentsAxis = '' #事業セグメント [軸]
	EntityTotalMember = '' #連結合計又は会社合計 [メンバー] ※ディメンションデフォルト
	ReportableSegmentsMember = '' #報告セグメント [メンバー]
	OtherReportableSegmentsMember = '' #その他の報告セグメント [メンバー]
	OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember = '' #報告セグメント以外の全てのセグメント [メンバー]
	UnallocatedAmountsAndEliminationMember = '' #全社・消去 [メンバー]
	InformationAboutGainOnBargainPurchaseForEachReportableSegmentLineItems = '' #報告セグメントごとの負ののれん発生益に関する情報 [表示項目]
	DescriptionOfFactorsWhichLedToRecognitionOfGainOnBargainPurchaseTextBlock = '' #報告セグメントごとの負ののれん発生益を認識する要因となった事象の概要 [テキストブロック]
	NotesOperationOfPublicFacilitiesFinancialStatementsHeading = '' #公共施設等運営事業関係、財務諸表 [目次項目]
	NotesOperationOfPublicFacilitiesFinancialStatementsTextBlock = '' #公共施設等運営事業関係、財務諸表 [テキストブロック]
	NotesRelatedPartiesFinancialStatementsHeading = '' #関連当事者情報、財務諸表 [目次項目]
	NotesRelatedPartiesFinancialStatementsTextBlock = '' #関連当事者情報、財務諸表 [テキストブロック]
	NotesEquityInEarningsLossesOfAffiliatesIfEquityMethodIsAppliedFinancialStatementsHeading = '' #持分法損益等、財務諸表 [目次項目]
	NotesEquityInEarningsLossesOfAffiliatesIfEquityMethodIsAppliedFinancialStatementsTextBlock = '' #持分法損益等、財務諸表 [テキストブロック]
	NotesSpecialPurposeEntitiesSubjectToDisclosureFinancialStatementsHeading = '' #開示対象特別目的会社関係、財務諸表 [目次項目]
	NotesSpecialPurposeEntitiesSubjectToDisclosureFinancialStatementsTextBlock = '' #開示対象特別目的会社関係、財務諸表 [テキストブロック]
	NotesPerShareInformationFinancialStatementsHeading = '' #１株当たり情報、財務諸表 [目次項目]
	NotesPerShareInformationFinancialStatementsTextBlock = '' #１株当たり情報、財務諸表 [テキストブロック]
	NotesSignificantEventsAfterReportingPeriodFinancialStatementsHeading = '' #重要な後発事象、財務諸表 [目次項目]
	NotesSignificantEventsAfterReportingPeriodFinancialStatementsTextBlock = '' #重要な後発事象、財務諸表 [テキストブロック]
	AnnexedDetailedSchedulesHeading = '' #附属明細表 [目次項目]
	AnnexedDetailedScheduleOfSecuritiesHeading = '' #有価証券明細表 [目次項目]
	AnnexedDetailedScheduleOfSecuritiesTextBlock = '' #有価証券明細表 [テキストブロック]
	AnnexedDetailedScheduleOfPropertyPlantAndEquipmentEtcHeading = '' #有形固定資産等明細表 [目次項目]
	AnnexedDetailedScheduleOfPropertyPlantAndEquipmentEtcTextBlock = '' #有形固定資産等明細表 [テキストブロック]
	AnnexedDetailedScheduleOfCorporateBondsFinancialStatementsHeading = '' #社債明細表、財務諸表 [目次項目]
	AnnexedDetailedScheduleOfCorporateBondsFinancialStatementsTextBlock = '' #社債明細表、財務諸表 [テキストブロック]
	AnnexedDetailedScheduleOfBorrowingsFinancialStatementsHeading = '' #借入金等明細表、財務諸表 [目次項目]
	AnnexedDetailedScheduleOfBorrowingsFinancialStatementsTextBlock = '' #借入金等明細表、財務諸表 [テキストブロック]
	AnnexedDetailedScheduleOfProvisionsHeading = '' #引当金明細表 [目次項目]
	AnnexedDetailedScheduleOfProvisionsTextBlock = '' #引当金明細表 [テキストブロック]
	AnnexedDetailedScheduleOfAssetRetirementObligationsFinancialStatementsHeading = '' #資産除去債務明細表、財務諸表 [目次項目]
	AnnexedDetailedScheduleOfAssetRetirementObligationsFinancialStatementsTextBlock = '' #資産除去債務明細表、財務諸表 [テキストブロック]
	AnnexedDetailedScheduleOfWaterTransportationRevenuesAndExpensesHeading = '' #海運業収益及び費用明細表 [目次項目]
	AnnexedDetailedScheduleOfWaterTransportationRevenuesAndExpensesTextBlock = '' #海運業収益及び費用明細表 [テキストブロック]
	AnnexedDetailedScheduleOfSecuritiesInTrustCNAHeading = '' #信託有価証券明細表、建設保証業 [目次項目]
	AnnexedDetailedScheduleOfSecuritiesInTrustCNATextBlock = '' #信託有価証券明細表、建設保証業 [テキストブロック]
	AnnexedDetailedScheduleOfBusinessCostINSHeading = '' #事業費明細表、保険業 [目次項目]
	AnnexedDetailedScheduleOfBusinessCostINSTextBlock = '' #事業費明細表、保険業 [テキストブロック]
	AnnexedDetailedScheduleOfNonCurrentAssetsELCHeading = '' #固定資産等明細表、電気通信事業 [目次項目]
	AnnexedDetailedScheduleOfNonCurrentAssetsELCTextBlock = '' #固定資産等明細表、電気通信事業 [テキストブロック]
	AnnexedDetailedScheduleOfNonCurrentAssetsGASHeading = '' #固定資産等明細表、ガス事業 [目次項目]
	AnnexedDetailedScheduleOfNonCurrentAssetsGASTextBlock = '' #固定資産等明細表、ガス事業 [テキストブロック]
	AnnexedDetailedScheduleOfNonCurrentAssetsHWYHeading = '' #固定資産等明細表、高速道路事業 [目次項目]
	AnnexedDetailedScheduleOfNonCurrentAssetsHWYTextBlock = '' #固定資産等明細表、高速道路事業 [テキストブロック]
	AnnexedDetailedScheduleOfIncreaseAndDecreaseOfNonCurrentAssetsELEHeading = '' #固定資産期中増減明細表、電気事業 [目次項目]
	AnnexedDetailedScheduleOfIncreaseAndDecreaseOfNonCurrentAssetsELETextBlock = '' #固定資産期中増減明細表、電気事業 [テキストブロック]
	AnnexedDetailedScheduleOfIncreaseAndDecreaseOfNonCurrentAssetsPart2IntangibleAssetsELEHeading = '' #固定資産期中増減明細表（無形固定資産再掲）、電気事業 [目次項目]
	AnnexedDetailedScheduleOfIncreaseAndDecreaseOfNonCurrentAssetsPart2IntangibleAssetsELETextBlock = '' #固定資産期中増減明細表（無形固定資産再掲）、電気事業 [テキストブロック]
	AnnexedDetailedScheduleOfDepreciationEtcELEHeading = '' #減価償却費等明細表、電気事業 [目次項目]
	AnnexedDetailedScheduleOfDepreciationEtcELETextBlock = '' #減価償却費等明細表、電気事業 [テキストブロック]
	AnnexedDetailedScheduleOfLongTermAndShortTermInvestmentsELEHeading = '' #長期投資及び短期投資明細表、電気事業 [目次項目]
	AnnexedDetailedScheduleOfLongTermAndShortTermInvestmentsELETextBlock = '' #長期投資及び短期投資明細表、電気事業 [テキストブロック]
	AnnexedDetailedScheduleOfBorrowingsLongTermPayablesLeaseObligationsOtherNonCurrentLiabilitiesAndCommercialPapersELEHeading = '' #借入金、長期未払債務、リース債務、雑固定負債及びコマーシャル・ペーパー明細表、電気事業 [目次項目]
	AnnexedDetailedScheduleOfBorrowingsLongTermPayablesLeaseObligationsOtherNonCurrentLiabilitiesAndCommercialPapersELETextBlock = '' #借入金、長期未払債務、リース債務、雑固定負債及びコマーシャル・ペーパー明細表、電気事業 [テキストブロック]
	AnnexedDetailedScheduleOfCorporateBondsAndShortTermAndLongTermBorrowingsHWYHeading = '' #社債、長期借入金及び短期借入金の増減明細表、高速道路事業 [目次項目]
	AnnexedDetailedScheduleOfCorporateBondsAndShortTermAndLongTermBorrowingsHWYTextBlock = '' #社債、長期借入金及び短期借入金の増減明細表、高速道路事業 [テキストブロック]
	AnnexedDetailedScheduleOfMedicalCorporationBondsHeading = '' #社会医療法人債明細表 [目次項目]
	AnnexedDetailedScheduleOfMedicalCorporationBondsTextBlock = '' #社会医療法人債明細表 [テキストブロック]
	AnnexedDetailedScheduleOfSchoolBondsHeading = '' #学校債明細表 [目次項目]
	AnnexedDetailedScheduleOfSchoolBondsTextBlock = '' #学校債明細表 [テキストブロック]
	ComponentsOfMajorAssetsAndLiabilitiesHeading = '' #主な資産及び負債の内容 [目次項目]
	ComponentsOfMajorAssetsAndLiabilitiesTextBlock = '' #主な資産及び負債の内容 [テキストブロック]
	OtherInformationFinancialStatementsEtcHeading = '' #その他、財務諸表等 [目次項目]
	OtherInformationFinancialStatementsEtcTextBlock = '' #その他、財務諸表等 [テキストブロック]
	OverviewOfOperationalProceduresForSharesHeading = '' #提出会社の株式事務の概要 [目次項目]
	OverviewOfOperationalProceduresForSharesTextBlock = '' #提出会社の株式事務の概要 [テキストブロック]
	ReferenceInformationOfReportingCompanyHeading = '' #提出会社の参考情報 [目次項目]
	InformationAboutParentCompanyEtcOfReportingCompanyHeading = '' #提出会社の親会社等の情報 [目次項目]
	InformationAboutParentCompanyEtcOfReportingCompanyTextBlock = '' #提出会社の親会社等の情報 [テキストブロック]
	OtherReferenceInformationHeading = '' #その他の参考情報 [目次項目]
	OtherReferenceInformationTextBlock = '' #その他の参考情報 [テキストブロック]
	InformationAboutCompanyWhichProvidesGuaranteeToReportingCompanyHeading = '' #提出会社の保証会社等の情報 [目次項目]
	InformationAboutCompanyWhichProvidesGuaranteeToReportingCompanyTextBlock = '' #提出会社の保証会社等の情報 [テキストブロック]
	InformationAboutGuaranteeCompanyHeading = '' #保証会社情報 [目次項目]
	InformationAboutGuaranteeCompanyTextBlock = '' #保証会社情報 [テキストブロック]
	CorporateBondsUnderGuaranteeHeading = '' #保証の対象となっている社債 [目次項目]
	CorporateBondsUnderGuaranteeTextBlock = '' #保証の対象となっている社債 [テキストブロック]
	InformationAboutGuaranteeCompanySubjectToOngoingDisclosureHeading = '' #継続開示会社たる保証会社に関する事項 [目次項目]
	InformationAboutGuaranteeCompanySubjectToOngoingDisclosureTextBlock = '' #継続開示会社たる保証会社に関する事項 [テキストブロック]
	DocumentsSubmittedByGuaranteeCompanyHeading = '' #保証会社が提出した書類 [目次項目]
	AnnualSecuritiesReportAndAttachedDocumentsQuarterlySecuritiesReportOrSemiAnnualSecuritiesReportDocumentsSubmittedByGuaranteeCompanyHeading = '' #有価証券報告書及びその添付書類又は四半期報告書若しくは半期報告書、保証会社が提出した書類 [目次項目]
	AnnualSecuritiesReportAndAttachedDocumentsQuarterlySecuritiesReportOrSemiAnnualSecuritiesReportDocumentsSubmittedByGuaranteeCompanyTextBlock = '' #有価証券報告書及びその添付書類又は四半期報告書若しくは半期報告書、保証会社が提出した書類 [テキストブロック]
	ExtraordinarySecuritiesReportDocumentsSubmittedByGuaranteeCompanyHeading = '' #臨時報告書、保証会社が提出した書類 [目次項目]
	ExtraordinarySecuritiesReportDocumentsSubmittedByGuaranteeCompanyTextBlock = '' #臨時報告書、保証会社が提出した書類 [テキストブロック]
	AmendmentReportDocumentsSubmittedByGuaranteeCompanyHeading = '' #訂正報告書、保証会社が提出した書類 [目次項目]
	AmendmentReportDocumentsSubmittedByGuaranteeCompanyTextBlock = '' #訂正報告書、保証会社が提出した書類 [テキストブロック]
	PlaceForPublicInspectionDocumentsSubmittedByGuaranteeCompanyHeading = '' #上記書類を縦覧に供している場所、保証会社が提出した書類 [目次項目]
	PlaceForPublicInspectionDocumentsSubmittedByGuaranteeCompanyTextBlock = '' #上記書類を縦覧に供している場所、保証会社が提出した書類 [テキストブロック]
	InformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureHeading = '' #継続開示会社に該当しない保証会社に関する事項 [目次項目]
	InformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureTextBlock = '' #継続開示会社に該当しない保証会社に関する事項 [テキストブロック]
	CompanyNameTitleAndNameOfRepresentativeAndAddressOfRegisteredHeadquarterHeading = '' #会社名・代表者の役職氏名及び本店の所在の場所 [目次項目]
	CompanyNameTitleAndNameOfRepresentativeAndAddressOfRegisteredHeadquarterTextBlock = '' #会社名・代表者の役職氏名及び本店の所在の場所 [テキストブロック]
	OverviewOfCompanyInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureHeading = '' #企業の概況、継続開示会社に該当しない保証会社に関する事項 [目次項目]
	OverviewOfCompanyInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureTextBlock = '' #企業の概況、継続開示会社に該当しない保証会社に関する事項 [テキストブロック]
	OverviewOfBusinessInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureHeading = '' #事業の状況、継続開示会社に該当しない保証会社に関する事項 [目次項目]
	OverviewOfBusinessInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureTextBlock = '' #事業の状況、継続開示会社に該当しない保証会社に関する事項 [テキストブロック]
	InformationAboutFacilitiesInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureHeading = '' #設備の状況、継続開示会社に該当しない保証会社に関する事項 [目次項目]
	InformationAboutFacilitiesInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureTextBlock = '' #設備の状況、継続開示会社に該当しない保証会社に関する事項 [テキストブロック]
	GuaranteeCompanyInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureHeading = '' #保証会社の状況、継続開示会社に該当しない保証会社に関する事項 [目次項目]
	GuaranteeCompanyInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureTextBlock = '' #保証会社の状況、継続開示会社に該当しない保証会社に関する事項 [テキストブロック]
	FinancialInformationInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureHeading = '' #経理の状況、継続開示会社に該当しない保証会社に関する事項 [目次項目]
	FinancialInformationInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureTextBlock = '' #経理の状況、継続開示会社に該当しない保証会社に関する事項 [テキストブロック]
	InformationAboutCompaniesOtherThanGuaranteeCompanyHeading = '' #保証会社以外の会社の情報 [目次項目]
	InformationAboutCompaniesOtherThanGuaranteeCompanyTextBlock = '' #保証会社以外の会社の情報 [テキストブロック]
	ReasonForDisclosureOfInformationOfCompanyConcernedHeading = '' #当該会社の情報の開示を必要とする理由 [目次項目]
	ReasonForDisclosureOfInformationOfCompanyConcernedTextBlock = '' #当該会社の情報の開示を必要とする理由 [テキストブロック]
	InformationAboutCompanyConcernedSubjectToOngoingDisclosureHeading = '' #継続開示会社たる当該会社に関する事項 [目次項目]
	InformationAboutCompanyConcernedSubjectToOngoingDisclosureTextBlock = '' #継続開示会社たる当該会社に関する事項 [テキストブロック]
	InformationAboutCompanyConcernedNotSubjectToOngoingDisclosureHeading = '' #継続開示会社に該当しない当該会社に関する事項 [目次項目]
	InformationAboutCompanyConcernedNotSubjectToOngoingDisclosureTextBlock = '' #継続開示会社に該当しない当該会社に関する事項 [テキストブロック]
	InformationAboutIndexEtcHeading = '' #指数等の情報 [目次項目]
	InformationAboutIndexEtcTextBlock = '' #指数等の情報 [テキストブロック]
	ReasonForDisclosureOfSaidIndexEtcHeading = '' #当該指数等の情報の開示を必要とする理由 [目次項目]
	ReasonForDisclosureOfSaidIndexEtcTextBlock = '' #当該指数等の情報の開示を必要とする理由 [テキストブロック]
	HistoricalRecordsOfIndexEtcHeading = '' #当該指数等の推移 [目次項目]
	HistoricalRecordsOfIndexEtcTextBlock = '' #当該指数等の推移 [テキストブロック]
	IndependentAuditorsReportHeading = '' #独立監査人の報告書 [目次項目]
	IndependentAuditorsReportConsolidatedTextBlock = '' #独立監査人の報告書、連結 [テキストブロック]
	IndependentAuditorsReportNonConsolidatedTextBlock = '' #独立監査人の報告書、個別 [テキストブロック]
	IndependentAuditorsReportHeading = '' #独立監査人の報告書 [目次項目]
	IndependentAuditorsReportConsolidatedTextBlock = '' #独立監査人の報告書、連結 [テキストブロック]
	AuditFirm1Consolidated = '' #監査法人１、連結
	CPA1AuditFirm1Consolidated = '' #公認会計士１、監査法人１、連結
	CPA2AuditFirm1Consolidated = '' #公認会計士２、監査法人１、連結
	CPA3AuditFirm1Consolidated = '' #公認会計士３、監査法人１、連結
	CPA4AuditFirm1Consolidated = '' #公認会計士４、監査法人１、連結
	CPA5AuditFirm1Consolidated = '' #公認会計士５、監査法人１、連結
	AuditFirm2Consolidated = '' #監査法人２、連結
	CPA1AuditFirm2Consolidated = '' #公認会計士１、監査法人２、連結
	CPA2AuditFirm2Consolidated = '' #公認会計士２、監査法人２、連結
	KeyAuditMattersConsolidatedTextBlock = '' #監査上の主要な検討事項、連結 [テキストブロック]
	OverviewKAMConsolidatedTextBlock = '' #全体概要、監査上の主要な検討事項、連結 [テキストブロック]
	OtherInformationConsolidatedTextBlock = '' #その他の記載内容、連結 [テキストブロック]
	UncorrectedMaterialMisstatementOtherInformationConsolidatedTextBlock = '' #未修正の重要な誤り、その他の記載内容、連結 [テキストブロック]
	IndependentAuditorsReportNonConsolidatedTextBlock = '' #独立監査人の報告書、個別 [テキストブロック]
	AuditFirm1NonConsolidated = '' #監査法人１、個別
	CPA1AuditFirm1NonConsolidated = '' #公認会計士１、監査法人１、個別
	CPA2AuditFirm1NonConsolidated = '' #公認会計士２、監査法人１、個別
	CPA3AuditFirm1NonConsolidated = '' #公認会計士３、監査法人１、個別
	CPA4AuditFirm1NonConsolidated = '' #公認会計士４、監査法人１、個別
	CPA5AuditFirm1NonConsolidated = '' #公認会計士５、監査法人１、個別
	AuditFirm2NonConsolidated = '' #監査法人２、個別
	CPA1AuditFirm2NonConsolidated = '' #公認会計士１、監査法人２、個別
	CPA2AuditFirm2NonConsolidated = '' #公認会計士２、監査法人２、個別
	KeyAuditMattersNonConsolidatedTextBlock = '' #監査上の主要な検討事項、個別 [テキストブロック]
	OverviewKAMNonConsolidatedTextBlock = '' #全体概要、監査上の主要な検討事項、個別 [テキストブロック]
	OtherInformationNonConsolidatedTextBlock = '' #その他の記載内容、個別 [テキストブロック]
	UncorrectedMaterialMisstatementOtherInformationNonConsolidatedTextBlock = '' #未修正の重要な誤り、その他の記載内容、個別 [テキストブロック]
	IndependentAuditorsReportHeading = '' #独立監査人の報告書 [目次項目]
	KeyAuditMattersDetailAbstract = '' #監査上の主要な検討事項（個別説明） [タイトル項目]
	KeyAuditMattersTable = '' #監査上の主要な検討事項 [表]
	SequentialNumbersAxis = '' #連番 [軸]
	Row1Member = '' #1件目 [メンバー]
	Row2Member = '' #2件目 [メンバー]
	Row3Member = '' #3件目 [メンバー]
	KeyAuditMattersConsolidatedLineItems = '' #監査上の主要な検討事項、連結 [表示項目]
	ShortDescriptionKAMConsolidated = '' #見出し、監査上の主要な検討事項、連結
	ReferenceKAMConsolidated = '' #開示への参照、監査上の主要な検討事項、連結
	Reference2KAMConsolidated = '' #開示への参照２、監査上の主要な検討事項、連結
	Reference3KAMConsolidated = '' #開示への参照３、監査上の主要な検討事項、連結
	Reference4KAMConsolidated = '' #開示への参照４、監査上の主要な検討事項、連結
	Reference5KAMConsolidated = '' #開示への参照５、監査上の主要な検討事項、連結
	DescriptionIncludingReasonKAMConsolidatedTextBlock = '' #内容及び理由、監査上の主要な検討事項、連結 [テキストブロック]
	AuditorsResponseKAMConsolidatedTextBlock = '' #監査上の対応、監査上の主要な検討事項、連結 [テキストブロック]
	KeyAuditMattersNonConsolidatedLineItems = '' #監査上の主要な検討事項、個別 [表示項目]
	ShortDescriptionKAMNonConsolidated = '' #見出し、監査上の主要な検討事項、個別
	ReferenceKAMNonConsolidated = '' #開示への参照、監査上の主要な検討事項、個別
	Reference2KAMNonConsolidated = '' #開示への参照２、監査上の主要な検討事項、個別
	Reference3KAMNonConsolidated = '' #開示への参照３、監査上の主要な検討事項、個別
	Reference4KAMNonConsolidated = '' #開示への参照４、監査上の主要な検討事項、個別
	Reference5KAMNonConsolidated = '' #開示への参照５、監査上の主要な検討事項、個別
	DescriptionIncludingReasonKAMNonConsolidatedTextBlock = '' #内容及び理由、監査上の主要な検討事項、個別 [テキストブロック]
	AuditorsResponseKAMNonConsolidatedTextBlock = '' #監査上の対応、監査上の主要な検討事項、個別 [テキストブロック]
	SameAsKAMForConsolidatedFSKAMNonConsolidatedTextBlock = '' #連結と同一内容である旨、監査上の主要な検討事項、個別 [テキストブロック]

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
			elif fact.concept.qname.localName == 'CabinetOfficeOrdinanceOnDisclosureOfCorporateInformationEtcFormNo3AnnualSecuritiesReportHeading': #企業内容等の開示に関する内閣府令 第三号様式 有価証券報告書 [目次項目]
				self.CabinetOfficeOrdinanceOnDisclosureOfCorporateInformationEtcFormNo3AnnualSecuritiesReportHeading = fact.value

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

			elif fact.concept.qname.localName == 'FiscalYearCoverPage': #事業年度、表紙
				self.FiscalYearCoverPage = fact.value

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

			elif fact.concept.qname.localName == 'NameOfContactPersonAddressOfRegisteredHeadquarterCoverPage': #事務連絡者氏名、本店の所在の場所、表紙
				self.NameOfContactPersonAddressOfRegisteredHeadquarterCoverPage = fact.value

			elif fact.concept.qname.localName == 'NearestPlaceOfContactCoverPage': #最寄りの連絡場所、表紙
				self.NearestPlaceOfContactCoverPage = fact.value

			elif fact.concept.qname.localName == 'TelephoneNumberNearestPlaceOfContactCoverPage': #電話番号、最寄りの連絡場所、表紙
				self.TelephoneNumberNearestPlaceOfContactCoverPage = fact.value

			elif fact.concept.qname.localName == 'NameOfContactPersonNearestPlaceOfContactCoverPage': #事務連絡者氏名、最寄りの連絡場所、表紙
				self.NameOfContactPersonNearestPlaceOfContactCoverPage = fact.value

			elif fact.concept.qname.localName == 'PlaceForPublicInspectionCoverPageTextBlock': #縦覧に供する場所、表紙 [テキストブロック]
				self.PlaceForPublicInspectionCoverPageTextBlock = fact.value

			elif fact.concept.qname.localName == 'FootnotesCoverPageTextBlock': #脚注、表紙 [テキストブロック]
				self.FootnotesCoverPageTextBlock = fact.value

			elif fact.concept.qname.localName == 'CompanyInformationHeading': #企業情報 [目次項目]
				self.CompanyInformationHeading = fact.value

			elif fact.concept.qname.localName == 'OverviewOfCompanyHeading': #企業の概況 [目次項目]
				self.OverviewOfCompanyHeading = fact.value

			elif fact.concept.qname.localName == 'SummaryOfBusinessResultsHeading': #主要な経営指標等の推移 [目次項目]
				self.SummaryOfBusinessResultsHeading = fact.value

			elif fact.concept.qname.localName == 'BusinessResultsOfGroupHeading': #連結経営指標等 [目次項目]
				self.BusinessResultsOfGroupHeading = fact.value

			elif fact.concept.qname.localName == 'BusinessResultsOfGroupTextBlock': #連結経営指標等 [テキストブロック]
				self.BusinessResultsOfGroupTextBlock = fact.value

			elif fact.concept.qname.localName == 'BusinessResultsOfGroupHeading': #連結経営指標等 [目次項目]
				self.BusinessResultsOfGroupHeading = fact.value

			elif fact.concept.qname.localName == 'BusinessResultsOfGroupTable': #連結経営指標等 [表]
				self.BusinessResultsOfGroupTable = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedOrNonConsolidatedAxis': #連結個別 [軸]
				self.ConsolidatedOrNonConsolidatedAxis = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedMember': #連結 [メンバー] ※ディメンションデフォルト
				self.ConsolidatedMember = fact.value

			elif fact.concept.qname.localName == 'BusinessResultsOfGroupLineItems': #連結経営指標等 [表示項目]
				self.BusinessResultsOfGroupLineItems = fact.value

			elif fact.concept.qname.localName == 'NetSalesSummaryOfBusinessResults': #売上高、経営指標等
				self.NetSalesSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'RevenueKeyFinancialData': #売上収益、経営指標等
				self.RevenueKeyFinancialData = fact.value

			elif fact.concept.qname.localName == 'OperatingRevenue1SummaryOfBusinessResults': #営業収益、経営指標等
				self.OperatingRevenue1SummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'OperatingRevenue2SummaryOfBusinessResults': #営業収入、経営指標等
				self.OperatingRevenue2SummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'GrossOperatingRevenueSummaryOfBusinessResults': #営業総収入、経営指標等
				self.GrossOperatingRevenueSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'OrdinaryIncomeSummaryOfBusinessResults': #経常収益、経営指標等
				self.OrdinaryIncomeSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'NetPremiumsWrittenSummaryOfBusinessResultsINS': #正味収入保険料、経営指標等、保険業
				self.NetPremiumsWrittenSummaryOfBusinessResultsINS = fact.value

			elif fact.concept.qname.localName == 'OrdinaryIncomeLossSummaryOfBusinessResults': #経常利益又は経常損失（△）、経営指標等
				self.OrdinaryIncomeLossSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'ProfitLossAttributableToOwnersOfParentSummaryOfBusinessResults': #親会社株主に帰属する当期純利益又は親会社株主に帰属する当期純損失（△）、経営指標等
				self.ProfitLossAttributableToOwnersOfParentSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'ComprehensiveIncomeSummaryOfBusinessResults': #包括利益、経営指標等
				self.ComprehensiveIncomeSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'NetAssetsSummaryOfBusinessResults': #純資産額、経営指標等
				self.NetAssetsSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'TotalAssetsSummaryOfBusinessResults': #総資産額、経営指標等
				self.TotalAssetsSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'NetAssetsPerShareSummaryOfBusinessResults': #１株当たり純資産額、経営指標等
				self.NetAssetsPerShareSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'BasicEarningsLossPerShareSummaryOfBusinessResults': #１株当たり当期純利益又は当期純損失（△）、経営指標等
				self.BasicEarningsLossPerShareSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'DilutedEarningsPerShareSummaryOfBusinessResults': #潜在株式調整後１株当たり当期純利益、経営指標等
				self.DilutedEarningsPerShareSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'EquityToAssetRatioSummaryOfBusinessResults': #自己資本比率、経営指標等
				self.EquityToAssetRatioSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'CapitalAdequacyRatioInternationalStandardSummaryOfBusinessResults': #自己資本比率（国際統一基準）、経営指標等
				self.CapitalAdequacyRatioInternationalStandardSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'CapitalAdequacyRatioDomesticStandardSummaryOfBusinessResults': #自己資本比率（国内基準）、経営指標等
				self.CapitalAdequacyRatioDomesticStandardSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'CapitalAdequacyRatioBISStandardSummaryOfBusinessResults': #自己資本比率（第一基準）、経営指標等
				self.CapitalAdequacyRatioBISStandardSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'CapitalAdequacyRatioDomesticStandard2SummaryOfBusinessResults': #自己資本比率（第二基準）、経営指標等
				self.CapitalAdequacyRatioDomesticStandard2SummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'RateOfReturnOnEquitySummaryOfBusinessResults': #自己資本利益率、経営指標等
				self.RateOfReturnOnEquitySummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'PriceEarningsRatioSummaryOfBusinessResults': #株価収益率、経営指標等
				self.PriceEarningsRatioSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'NetCashProvidedByUsedInOperatingActivitiesSummaryOfBusinessResults': #営業活動によるキャッシュ・フロー、経営指標等
				self.NetCashProvidedByUsedInOperatingActivitiesSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'NetCashProvidedByUsedInInvestingActivitiesSummaryOfBusinessResults': #投資活動によるキャッシュ・フロー、経営指標等
				self.NetCashProvidedByUsedInInvestingActivitiesSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'NetCashProvidedByUsedInFinancingActivitiesSummaryOfBusinessResults': #財務活動によるキャッシュ・フロー、経営指標等
				self.NetCashProvidedByUsedInFinancingActivitiesSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'CashAndCashEquivalentsSummaryOfBusinessResults': #現金及び現金同等物の残高、経営指標等
				self.CashAndCashEquivalentsSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'NumberOfEmployees': #従業員数
				self.NumberOfEmployees = fact.value

			elif fact.concept.qname.localName == 'AverageNumberOfTemporaryWorkers': #平均臨時雇用人員
				self.AverageNumberOfTemporaryWorkers = fact.value

			elif fact.concept.qname.localName == 'RevenueIFRSSummaryOfBusinessResults': #売上収益（IFRS）、経営指標等
				self.RevenueIFRSSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'ProfitLossBeforeTaxIFRSSummaryOfBusinessResults': #税引前利益又は税引前損失（△）（IFRS）、経営指標等
				self.ProfitLossBeforeTaxIFRSSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'ProfitLossFromContinuingOperationsIFRSSummaryOfBusinessResults': #継続事業からの当期利益又は当期損失（△）（IFRS）、経営指標等
				self.ProfitLossFromContinuingOperationsIFRSSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'ProfitLossIFRSSummaryOfBusinessResults': #当期利益又は当期損失（△）（IFRS）、経営指標等
				self.ProfitLossIFRSSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'ProfitLossAttributableToOwnersOfParentIFRSSummaryOfBusinessResults': #当期利益又は当期損失（△）：親会社の所有者に帰属（IFRS）、経営指標等
				self.ProfitLossAttributableToOwnersOfParentIFRSSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'ComprehensiveIncomeIFRSSummaryOfBusinessResults': #当期包括利益（IFRS）、経営指標等
				self.ComprehensiveIncomeIFRSSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'ComprehensiveIncomeAttributableToOwnersOfParentIFRSSummaryOfBusinessResults': #当期包括利益：親会社の所有者に帰属（IFRS）、経営指標等
				self.ComprehensiveIncomeAttributableToOwnersOfParentIFRSSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'EquityAttributableToOwnersOfParentIFRSSummaryOfBusinessResults': #親会社の所有者に帰属する持分（IFRS）、経営指標等
				self.EquityAttributableToOwnersOfParentIFRSSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'TotalAssetsIFRSSummaryOfBusinessResults': #総資産額（IFRS）、経営指標等
				self.TotalAssetsIFRSSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'EquityToAssetRatioIFRSSummaryOfBusinessResults': #１株当たり親会社所有者帰属持分（IFRS）、経営指標等
				self.EquityToAssetRatioIFRSSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'BasicEarningsLossPerShareIFRSSummaryOfBusinessResults': #基本的１株当たり利益又は損失（△）（IFRS）、経営指標等
				self.BasicEarningsLossPerShareIFRSSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'DilutedEarningsLossPerShareIFRSSummaryOfBusinessResults': #希薄化後１株当たり利益又は損失（△）（IFRS）、経営指標等
				self.DilutedEarningsLossPerShareIFRSSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'RatioOfOwnersEquityToGrossAssetsIFRSSummaryOfBusinessResults': #親会社所有者帰属持分比率（IFRS）、経営指標等
				self.RatioOfOwnersEquityToGrossAssetsIFRSSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'RateOfReturnOnEquityIFRSSummaryOfBusinessResults': #親会社所有者帰属持分利益率（IFRS）、経営指標等
				self.RateOfReturnOnEquityIFRSSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'PriceEarningsRatioIFRSSummaryOfBusinessResults': #株価収益率（IFRS）、経営指標等
				self.PriceEarningsRatioIFRSSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'CashFlowsFromUsedInOperatingActivitiesIFRSSummaryOfBusinessResults': #営業活動によるキャッシュ・フロー（IFRS）、経営指標等
				self.CashFlowsFromUsedInOperatingActivitiesIFRSSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'CashFlowsFromUsedInInvestingActivitiesIFRSSummaryOfBusinessResults': #投資活動によるキャッシュ・フロー（IFRS）、経営指標等
				self.CashFlowsFromUsedInInvestingActivitiesIFRSSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'CashFlowsFromUsedInFinancingActivitiesIFRSSummaryOfBusinessResults': #財務活動によるキャッシュ・フロー（IFRS）、経営指標等
				self.CashFlowsFromUsedInFinancingActivitiesIFRSSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'CashAndCashEquivalentsIFRSSummaryOfBusinessResults': #現金及び現金同等物（IFRS）、経営指標等
				self.CashAndCashEquivalentsIFRSSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'RevenueJMISSummaryOfBusinessResults': #売上収益（JMIS）、経営指標等
				self.RevenueJMISSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'ProfitLossBeforeTaxJMISSummaryOfBusinessResults': #税引前利益又は税引前損失（△）（JMIS）、経営指標等
				self.ProfitLossBeforeTaxJMISSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'ProfitLossFromContinuingOperationsJMISSummaryOfBusinessResults': #継続事業からの当期利益又は当期損失（△）（JMIS）、経営指標等
				self.ProfitLossFromContinuingOperationsJMISSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'ProfitLossJMISSummaryOfBusinessResults': #当期利益又は当期損失（△）（JMIS）、経営指標等
				self.ProfitLossJMISSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'ProfitLossAttributableToOwnersOfParentJMISSummaryOfBusinessResults': #当期利益又は当期損失（△）：親会社の所有者に帰属（JMIS）、経営指標等
				self.ProfitLossAttributableToOwnersOfParentJMISSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'ComprehensiveIncomeJMISSummaryOfBusinessResults': #当期包括利益（JMIS）、経営指標等
				self.ComprehensiveIncomeJMISSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'ComprehensiveIncomeAttributableToOwnersOfParentJMISSummaryOfBusinessResults': #当期包括利益：親会社の所有者に帰属（JMIS）、経営指標等
				self.ComprehensiveIncomeAttributableToOwnersOfParentJMISSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'EquityAttributableToOwnersOfParentJMISSummaryOfBusinessResults': #親会社の所有者に帰属する持分（JMIS）、経営指標等
				self.EquityAttributableToOwnersOfParentJMISSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'TotalAssetsJMISSummaryOfBusinessResults': #総資産額（JMIS）、経営指標等
				self.TotalAssetsJMISSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'EquityToAssetRatioJMISSummaryOfBusinessResults': #１株当たり親会社所有者帰属持分（JMIS）、経営指標等
				self.EquityToAssetRatioJMISSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'BasicEarningsLossPerShareJMISSummaryOfBusinessResults': #基本的１株当たり利益又は損失（△）（JMIS）、経営指標等
				self.BasicEarningsLossPerShareJMISSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'DilutedEarningsLossPerShareJMISSummaryOfBusinessResults': #希薄化後１株当たり利益又は損失（△）（JMIS）、経営指標等
				self.DilutedEarningsLossPerShareJMISSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'RatioOfOwnersEquityToGrossAssetsJMISSummaryOfBusinessResults': #親会社所有者帰属持分比率（JMIS）、経営指標等
				self.RatioOfOwnersEquityToGrossAssetsJMISSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'RateOfReturnOnEquityJMISSummaryOfBusinessResults': #親会社所有者帰属持分利益率（JMIS）、経営指標等
				self.RateOfReturnOnEquityJMISSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'PriceEarningsRatioJMISSummaryOfBusinessResults': #株価収益率（JMIS）、経営指標等
				self.PriceEarningsRatioJMISSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'CashFlowsFromUsedInOperatingActivitiesJMISSummaryOfBusinessResults': #営業活動によるキャッシュ・フロー（JMIS）、経営指標等
				self.CashFlowsFromUsedInOperatingActivitiesJMISSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'CashFlowsFromUsedInInvestingActivitiesJMISSummaryOfBusinessResults': #投資活動によるキャッシュ・フロー（JMIS）、経営指標等
				self.CashFlowsFromUsedInInvestingActivitiesJMISSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'CashFlowsFromUsedInFinancingActivitiesJMISSummaryOfBusinessResults': #財務活動によるキャッシュ・フロー（JMIS）、経営指標等
				self.CashFlowsFromUsedInFinancingActivitiesJMISSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'CashAndCashEquivalentsJMISSummaryOfBusinessResults': #現金及び現金同等物（JMIS）、経営指標等
				self.CashAndCashEquivalentsJMISSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'RevenuesUSGAAPSummaryOfBusinessResults': #売上高（US GAAP）、経営指標等
				self.RevenuesUSGAAPSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'OperatingIncomeLossUSGAAPSummaryOfBusinessResults': #営業利益又は営業損失（△）（US GAAP）、経営指標等
				self.OperatingIncomeLossUSGAAPSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'ProfitLossBeforeTaxUSGAAPSummaryOfBusinessResults': #税引前利益又は税引前損失（△）（US GAAP）、経営指標等
				self.ProfitLossBeforeTaxUSGAAPSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'NetIncomeLossAttributableToOwnersOfParentUSGAAPSummaryOfBusinessResults': #当社株主に帰属する純利益又は純損失（△）（US GAAP）、経営指標等
				self.NetIncomeLossAttributableToOwnersOfParentUSGAAPSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'ComprehensiveIncomeUSGAAPSummaryOfBusinessResults': #包括利益（US GAAP）、経営指標等
				self.ComprehensiveIncomeUSGAAPSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'ComprehensiveIncomeAttributableToOwnersOfParentUSGAAPSummaryOfBusinessResults': #当社株主に帰属する包括利益（US GAAP）、経営指標等
				self.ComprehensiveIncomeAttributableToOwnersOfParentUSGAAPSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'EquityAttributableToOwnersOfParentUSGAAPSummaryOfBusinessResults': #株主資本（US GAAP）、経営指標等
				self.EquityAttributableToOwnersOfParentUSGAAPSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'EquityIncludingPortionAttributableToNonControllingInterestUSGAAPSummaryOfBusinessResults': #純資産額（US GAAP）、経営指標等
				self.EquityIncludingPortionAttributableToNonControllingInterestUSGAAPSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'TotalAssetsUSGAAPSummaryOfBusinessResults': #総資産額（US GAAP）、経営指標等
				self.TotalAssetsUSGAAPSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'EquityAttributableToOwnersOfParentPerShareUSGAAPSummaryOfBusinessResults': #１株当たり株主資本（US GAAP）、経営指標等
				self.EquityAttributableToOwnersOfParentPerShareUSGAAPSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'BasicEarningsLossPerShareUSGAAPSummaryOfBusinessResults': #基本的１株当たり当社株主に帰属する利益又は損失（△）（US GAAP）、経営指標等
				self.BasicEarningsLossPerShareUSGAAPSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'DilutedEarningsLossPerShareUSGAAPSummaryOfBusinessResults': #希薄化後１株当たり当社株主に帰属する利益又は損失（△）（US GAAP）、経営指標等
				self.DilutedEarningsLossPerShareUSGAAPSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'EquityToAssetRatioUSGAAPSummaryOfBusinessResults': #自己資本比率（US GAAP）、経営指標等
				self.EquityToAssetRatioUSGAAPSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'PriceEarningsRatioUSGAAPSummaryOfBusinessResults': #株価収益率（US GAAP）、経営指標等
				self.PriceEarningsRatioUSGAAPSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'RateOfReturnOnEquityUSGAAPSummaryOfBusinessResults': #株主資本利益率（US GAAP）、経営指標等
				self.RateOfReturnOnEquityUSGAAPSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'CashFlowsFromUsedInOperatingActivitiesUSGAAPSummaryOfBusinessResults': #営業活動によるキャッシュ・フロー（US GAAP）、経営指標等
				self.CashFlowsFromUsedInOperatingActivitiesUSGAAPSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'CashFlowsFromUsedInInvestingActivitiesUSGAAPSummaryOfBusinessResults': #投資活動によるキャッシュ・フロー（US GAAP）、経営指標等
				self.CashFlowsFromUsedInInvestingActivitiesUSGAAPSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'CashFlowsFromUsedInFinancingActivitiesUSGAAPSummaryOfBusinessResults': #財務活動によるキャッシュ・フロー（US GAAP）、経営指標等
				self.CashFlowsFromUsedInFinancingActivitiesUSGAAPSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'CashAndCashEquivalentsUSGAAPSummaryOfBusinessResults': #現金及び現金同等物（US GAAP）、経営指標等
				self.CashAndCashEquivalentsUSGAAPSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'BusinessResultsOfReportingCompanyHeading': #提出会社の経営指標等 [目次項目]
				self.BusinessResultsOfReportingCompanyHeading = fact.value

			elif fact.concept.qname.localName == 'BusinessResultsOfReportingCompanyTextBlock': #提出会社の経営指標等 [テキストブロック]
				self.BusinessResultsOfReportingCompanyTextBlock = fact.value

			elif fact.concept.qname.localName == 'BusinessResultsOfReportingCompanyHeading': #提出会社の経営指標等 [目次項目]
				self.BusinessResultsOfReportingCompanyHeading = fact.value

			elif fact.concept.qname.localName == 'BusinessResultsOfReportingCompanyTable': #提出会社の経営指標等 [表]
				self.BusinessResultsOfReportingCompanyTable = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedOrNonConsolidatedAxis': #連結個別 [軸]
				self.ConsolidatedOrNonConsolidatedAxis = fact.value

			elif fact.concept.qname.localName == 'NonConsolidatedMember': #非連結又は個別 [メンバー]
				self.NonConsolidatedMember = fact.value

			elif fact.concept.qname.localName == 'BusinessResultsOfReportingCompanyLineItems': #提出会社の経営指標等 [表示項目]
				self.BusinessResultsOfReportingCompanyLineItems = fact.value

			elif fact.concept.qname.localName == 'NetSalesSummaryOfBusinessResults': #売上高、経営指標等
				self.NetSalesSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'RevenueKeyFinancialData': #売上収益、経営指標等
				self.RevenueKeyFinancialData = fact.value

			elif fact.concept.qname.localName == 'OperatingRevenue1SummaryOfBusinessResults': #営業収益、経営指標等
				self.OperatingRevenue1SummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'OperatingRevenue2SummaryOfBusinessResults': #営業収入、経営指標等
				self.OperatingRevenue2SummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'GrossOperatingRevenueSummaryOfBusinessResults': #営業総収入、経営指標等
				self.GrossOperatingRevenueSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'OrdinaryIncomeSummaryOfBusinessResults': #経常収益、経営指標等
				self.OrdinaryIncomeSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'NetPremiumsWrittenSummaryOfBusinessResultsINS': #正味収入保険料、経営指標等、保険業
				self.NetPremiumsWrittenSummaryOfBusinessResultsINS = fact.value

			elif fact.concept.qname.localName == 'OrdinaryIncomeLossSummaryOfBusinessResults': #経常利益又は経常損失（△）、経営指標等
				self.OrdinaryIncomeLossSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'NetIncomeLossSummaryOfBusinessResults': #当期純利益又は当期純損失（△）、経営指標等
				self.NetIncomeLossSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'NetLossRatioSummaryOfBusinessResultsINS': #正味損害率、経営指標等、保険業
				self.NetLossRatioSummaryOfBusinessResultsINS = fact.value

			elif fact.concept.qname.localName == 'NetOperatingExpenseRatioSummaryOfBusinessResultsINS': #正味事業費率、経営指標等、保険業
				self.NetOperatingExpenseRatioSummaryOfBusinessResultsINS = fact.value

			elif fact.concept.qname.localName == 'InterestAndDividendIncomeSummaryOfBusinessResultsINS': #利息及び配当金収入、経営指標等、保険業
				self.InterestAndDividendIncomeSummaryOfBusinessResultsINS = fact.value

			elif fact.concept.qname.localName == 'InvestmentAssetsYieldIncomeYieldSummaryOfBusinessResultsINS': #運用資産利回り（インカム利回り）、経営指標等、保険業
				self.InvestmentAssetsYieldIncomeYieldSummaryOfBusinessResultsINS = fact.value

			elif fact.concept.qname.localName == 'InvestmentYieldRealizedYieldSummaryOfBusinessResultsINS': #資産運用利回り（実現利回り）、経営指標等、保険業
				self.InvestmentYieldRealizedYieldSummaryOfBusinessResultsINS = fact.value

			elif fact.concept.qname.localName == 'EquityInEarningsLossesOfAffiliatesIfEquityMethodIsAppliedSummaryOfBusinessResults': #持分法を適用した場合の投資利益又は投資損失（△）、経営指標等
				self.EquityInEarningsLossesOfAffiliatesIfEquityMethodIsAppliedSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'CapitalStockSummaryOfBusinessResults': #資本金、経営指標等
				self.CapitalStockSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'TotalNumberOfIssuedSharesSummaryOfBusinessResults': #発行済株式総数（普通株式）、経営指標等
				self.TotalNumberOfIssuedSharesSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'NetAssetsSummaryOfBusinessResults': #純資産額、経営指標等
				self.NetAssetsSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'TotalAssetsSummaryOfBusinessResults': #総資産額、経営指標等
				self.TotalAssetsSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'DepositsSummaryOfBusinessResults': #預金残高、経営指標等
				self.DepositsSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'LoansAndBillsDiscountedSummaryOfBusinessResults': #貸出金残高、経営指標等
				self.LoansAndBillsDiscountedSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'SecuritiesSummaryOfBusinessResults': #有価証券残高、経営指標等
				self.SecuritiesSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'NetAssetsPerShareSummaryOfBusinessResults': #１株当たり純資産額、経営指標等
				self.NetAssetsPerShareSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'DividendPaidPerShareSummaryOfBusinessResults': #１株当たり配当額、経営指標等
				self.DividendPaidPerShareSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'InterimDividendPaidPerShareSummaryOfBusinessResults': #１株当たり中間配当額、経営指標等
				self.InterimDividendPaidPerShareSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'FirstQuarterDividendPaidPerShareSummaryOfBusinessResults': #１株当たり第１四半期配当額、経営指標等
				self.FirstQuarterDividendPaidPerShareSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'SecondQuarterDividendPaidPerShareSummaryOfBusinessResults': #１株当たり第２四半期配当額、経営指標等
				self.SecondQuarterDividendPaidPerShareSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'ThirdQuarterDividendPaidPerShareSummaryOfBusinessResults': #１株当たり第３四半期配当額、経営指標等
				self.ThirdQuarterDividendPaidPerShareSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'FourthQuarterDividendPaidPerShareSummaryOfBusinessResults': #１株当たり第４四半期配当額、経営指標等
				self.FourthQuarterDividendPaidPerShareSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'FifthQuarterDividendPaidPerShareSummaryOfBusinessResults': #１株当たり第５四半期配当額、経営指標等
				self.FifthQuarterDividendPaidPerShareSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'BasicEarningsLossPerShareSummaryOfBusinessResults': #１株当たり当期純利益又は当期純損失（△）、経営指標等
				self.BasicEarningsLossPerShareSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'DilutedEarningsPerShareSummaryOfBusinessResults': #潜在株式調整後１株当たり当期純利益、経営指標等
				self.DilutedEarningsPerShareSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'EquityToAssetRatioSummaryOfBusinessResults': #自己資本比率、経営指標等
				self.EquityToAssetRatioSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'CapitalAdequacyRatioInternationalStandardSummaryOfBusinessResults': #自己資本比率（国際統一基準）、経営指標等
				self.CapitalAdequacyRatioInternationalStandardSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'CapitalAdequacyRatioDomesticStandardSummaryOfBusinessResults': #自己資本比率（国内基準）、経営指標等
				self.CapitalAdequacyRatioDomesticStandardSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'CapitalAdequacyRatioBISStandardSummaryOfBusinessResults': #自己資本比率（第一基準）、経営指標等
				self.CapitalAdequacyRatioBISStandardSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'CapitalAdequacyRatioDomesticStandard2SummaryOfBusinessResults': #自己資本比率（第二基準）、経営指標等
				self.CapitalAdequacyRatioDomesticStandard2SummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'RateOfReturnOnEquitySummaryOfBusinessResults': #自己資本利益率、経営指標等
				self.RateOfReturnOnEquitySummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'PriceEarningsRatioSummaryOfBusinessResults': #株価収益率、経営指標等
				self.PriceEarningsRatioSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'PayoutRatioSummaryOfBusinessResults': #配当性向、経営指標等
				self.PayoutRatioSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'NetCashProvidedByUsedInOperatingActivitiesSummaryOfBusinessResults': #営業活動によるキャッシュ・フロー、経営指標等
				self.NetCashProvidedByUsedInOperatingActivitiesSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'NetCashProvidedByUsedInInvestingActivitiesSummaryOfBusinessResults': #投資活動によるキャッシュ・フロー、経営指標等
				self.NetCashProvidedByUsedInInvestingActivitiesSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'NetCashProvidedByUsedInFinancingActivitiesSummaryOfBusinessResults': #財務活動によるキャッシュ・フロー、経営指標等
				self.NetCashProvidedByUsedInFinancingActivitiesSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'CashAndCashEquivalentsSummaryOfBusinessResults': #現金及び現金同等物の残高、経営指標等
				self.CashAndCashEquivalentsSummaryOfBusinessResults = fact.value

			elif fact.concept.qname.localName == 'NumberOfEmployees': #従業員数
				self.NumberOfEmployees = fact.value

			elif fact.concept.qname.localName == 'AverageNumberOfTemporaryWorkers': #平均臨時雇用人員
				self.AverageNumberOfTemporaryWorkers = fact.value

			elif fact.concept.qname.localName == 'TotalShareholderReturn': #株主総利回り
				self.TotalShareholderReturn = fact.value

			elif fact.concept.qname.localName == 'TotalReturnOnSharePriceIndex': #株価指数における総利回り
				self.TotalReturnOnSharePriceIndex = fact.value

			elif fact.concept.qname.localName == 'CompanyHistoryHeading': #沿革 [目次項目]
				self.CompanyHistoryHeading = fact.value

			elif fact.concept.qname.localName == 'CompanyHistoryTextBlock': #沿革 [テキストブロック]
				self.CompanyHistoryTextBlock = fact.value

			elif fact.concept.qname.localName == 'DescriptionOfBusinessHeading': #事業の内容 [目次項目]
				self.DescriptionOfBusinessHeading = fact.value

			elif fact.concept.qname.localName == 'DescriptionOfBusinessTextBlock': #事業の内容 [テキストブロック]
				self.DescriptionOfBusinessTextBlock = fact.value

			elif fact.concept.qname.localName == 'OverviewOfAffiliatedEntitiesHeading': #関係会社の状況 [目次項目]
				self.OverviewOfAffiliatedEntitiesHeading = fact.value

			elif fact.concept.qname.localName == 'OverviewOfAffiliatedEntitiesTextBlock': #関係会社の状況 [テキストブロック]
				self.OverviewOfAffiliatedEntitiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'InformationAboutEmployeesHeading': #従業員の状況 [目次項目]
				self.InformationAboutEmployeesHeading = fact.value

			elif fact.concept.qname.localName == 'InformationAboutEmployeesTextBlock': #従業員の状況 [テキストブロック]
				self.InformationAboutEmployeesTextBlock = fact.value

			elif fact.concept.qname.localName == 'InformationAboutEmployeesHeading': #従業員の状況 [目次項目]
				self.InformationAboutEmployeesHeading = fact.value

			elif fact.concept.qname.localName == 'InformationAboutGroupInformationAboutEmployeesAbstract': #連結会社の状況、従業員の状況 [タイトル項目]
				self.InformationAboutGroupInformationAboutEmployeesAbstract = fact.value

			elif fact.concept.qname.localName == 'NumberOfEmployeesOfGroupTable': #連結会社の従業員数 [表]
				self.NumberOfEmployeesOfGroupTable = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedOrNonConsolidatedAxis': #連結個別 [軸]
				self.ConsolidatedOrNonConsolidatedAxis = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedMember': #連結 [メンバー] ※ディメンションデフォルト
				self.ConsolidatedMember = fact.value

			elif fact.concept.qname.localName == 'OperatingSegmentsAxis': #事業セグメント [軸]
				self.OperatingSegmentsAxis = fact.value

			elif fact.concept.qname.localName == 'EntityTotalMember': #連結合計又は会社合計 [メンバー] ※ディメンションデフォルト
				self.EntityTotalMember = fact.value

			elif fact.concept.qname.localName == 'ReportableSegmentsMember': #報告セグメント [メンバー]
				self.ReportableSegmentsMember = fact.value

			elif fact.concept.qname.localName == 'OtherReportableSegmentsMember': #その他の報告セグメント [メンバー]
				self.OtherReportableSegmentsMember = fact.value

			elif fact.concept.qname.localName == 'OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember': #報告セグメント以外の全てのセグメント [メンバー]
				self.OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember = fact.value

			elif fact.concept.qname.localName == 'CorporateSharedMember': #全社（共通） [メンバー]
				self.CorporateSharedMember = fact.value

			elif fact.concept.qname.localName == 'OtherOperatingSegmentsAxisMember': #その他、事業セグメント軸 [メンバー]
				self.OtherOperatingSegmentsAxisMember = fact.value

			elif fact.concept.qname.localName == 'NumberOfEmployeesOfGroupLineItems': #連結会社の従業員数 [表示項目]
				self.NumberOfEmployeesOfGroupLineItems = fact.value

			elif fact.concept.qname.localName == 'NumberOfEmployees': #従業員数
				self.NumberOfEmployees = fact.value

			elif fact.concept.qname.localName == 'AverageNumberOfTemporaryWorkers': #平均臨時雇用人員
				self.AverageNumberOfTemporaryWorkers = fact.value

			elif fact.concept.qname.localName == 'InformationAboutEmployeesHeading': #従業員の状況 [目次項目]
				self.InformationAboutEmployeesHeading = fact.value

			elif fact.concept.qname.localName == 'InformationAboutReportingCompanyInformationAboutEmployeesAbstract': #提出会社の状況、従業員の状況 [タイトル項目]
				self.InformationAboutReportingCompanyInformationAboutEmployeesAbstract = fact.value

			elif fact.concept.qname.localName == 'InformationAboutEmployeesOfReportingCompanyTable': #提出会社の従業員の状況 [表]
				self.InformationAboutEmployeesOfReportingCompanyTable = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedOrNonConsolidatedAxis': #連結個別 [軸]
				self.ConsolidatedOrNonConsolidatedAxis = fact.value

			elif fact.concept.qname.localName == 'NonConsolidatedMember': #非連結又は個別 [メンバー]
				self.NonConsolidatedMember = fact.value

			elif fact.concept.qname.localName == 'InformationAboutEmployeesOfReportingCompanyLineItems': #提出会社の従業員の状況 [表示項目]
				self.InformationAboutEmployeesOfReportingCompanyLineItems = fact.value

			elif fact.concept.qname.localName == 'NumberOfEmployees': #従業員数
				self.NumberOfEmployees = fact.value

			elif fact.concept.qname.localName == 'AverageNumberOfTemporaryWorkers': #平均臨時雇用人員
				self.AverageNumberOfTemporaryWorkers = fact.value

			elif fact.concept.qname.localName == 'AverageAgeYearsInformationAboutReportingCompanyInformationAboutEmployees': #平均年齢（年）、提出会社の状況、従業員の状況
				self.AverageAgeYearsInformationAboutReportingCompanyInformationAboutEmployees = fact.value

			elif fact.concept.qname.localName == 'AverageAgeMonthsInformationAboutReportingCompanyInformationAboutEmployees': #平均年齢（月）、提出会社の状況、従業員の状況
				self.AverageAgeMonthsInformationAboutReportingCompanyInformationAboutEmployees = fact.value

			elif fact.concept.qname.localName == 'AverageLengthOfServiceYearsInformationAboutReportingCompanyInformationAboutEmployees': #平均勤続年数（年）、提出会社の状況、従業員の状況
				self.AverageLengthOfServiceYearsInformationAboutReportingCompanyInformationAboutEmployees = fact.value

			elif fact.concept.qname.localName == 'AverageLengthOfServiceMonthsInformationAboutReportingCompanyInformationAboutEmployees': #平均勤続年数（月）、提出会社の状況、従業員の状況
				self.AverageLengthOfServiceMonthsInformationAboutReportingCompanyInformationAboutEmployees = fact.value

			elif fact.concept.qname.localName == 'AverageAnnualSalaryInformationAboutReportingCompanyInformationAboutEmployees': #平均年間給与、提出会社の状況、従業員の状況
				self.AverageAnnualSalaryInformationAboutReportingCompanyInformationAboutEmployees = fact.value

			elif fact.concept.qname.localName == 'InformationAboutEmployeesHeading': #従業員の状況 [目次項目]
				self.InformationAboutEmployeesHeading = fact.value

			elif fact.concept.qname.localName == 'InformationAboutReportingCompanyInformationAboutEmployeesAbstract': #提出会社の状況、従業員の状況 [タイトル項目]
				self.InformationAboutReportingCompanyInformationAboutEmployeesAbstract = fact.value

			elif fact.concept.qname.localName == 'NumberOfEmployeesOfReportingCompanyTable': #提出会社の従業員数 [表]
				self.NumberOfEmployeesOfReportingCompanyTable = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedOrNonConsolidatedAxis': #連結個別 [軸]
				self.ConsolidatedOrNonConsolidatedAxis = fact.value

			elif fact.concept.qname.localName == 'NonConsolidatedMember': #非連結又は個別 [メンバー]
				self.NonConsolidatedMember = fact.value

			elif fact.concept.qname.localName == 'OperatingSegmentsAxis': #事業セグメント [軸]
				self.OperatingSegmentsAxis = fact.value

			elif fact.concept.qname.localName == 'EntityTotalMember': #連結合計又は会社合計 [メンバー] ※ディメンションデフォルト
				self.EntityTotalMember = fact.value

			elif fact.concept.qname.localName == 'ReportableSegmentsMember': #報告セグメント [メンバー]
				self.ReportableSegmentsMember = fact.value

			elif fact.concept.qname.localName == 'OtherReportableSegmentsMember': #その他の報告セグメント [メンバー]
				self.OtherReportableSegmentsMember = fact.value

			elif fact.concept.qname.localName == 'OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember': #報告セグメント以外の全てのセグメント [メンバー]
				self.OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember = fact.value

			elif fact.concept.qname.localName == 'CorporateSharedMember': #全社（共通） [メンバー]
				self.CorporateSharedMember = fact.value

			elif fact.concept.qname.localName == 'OtherOperatingSegmentsAxisMember': #その他、事業セグメント軸 [メンバー]
				self.OtherOperatingSegmentsAxisMember = fact.value

			elif fact.concept.qname.localName == 'NumberOfEmployeesOfReportingCompanyLineItems': #提出会社の従業員数 [表示項目]
				self.NumberOfEmployeesOfReportingCompanyLineItems = fact.value

			elif fact.concept.qname.localName == 'NumberOfEmployees': #従業員数
				self.NumberOfEmployees = fact.value

			elif fact.concept.qname.localName == 'AverageNumberOfTemporaryWorkers': #平均臨時雇用人員
				self.AverageNumberOfTemporaryWorkers = fact.value

			elif fact.concept.qname.localName == 'OverviewOfBusinessHeading': #事業の状況 [目次項目]
				self.OverviewOfBusinessHeading = fact.value

			elif fact.concept.qname.localName == 'BusinessPolicyBusinessEnvironmentIssuesToAddressEtcHeading': #経営方針、経営環境及び対処すべき課題等 [目次項目]
				self.BusinessPolicyBusinessEnvironmentIssuesToAddressEtcHeading = fact.value

			elif fact.concept.qname.localName == 'BusinessPolicyBusinessEnvironmentIssuesToAddressEtcTextBlock': #経営方針、経営環境及び対処すべき課題等 [テキストブロック]
				self.BusinessPolicyBusinessEnvironmentIssuesToAddressEtcTextBlock = fact.value

			elif fact.concept.qname.localName == 'BusinessRisksHeading': #事業等のリスク [目次項目]
				self.BusinessRisksHeading = fact.value

			elif fact.concept.qname.localName == 'BusinessRisksTextBlock': #事業等のリスク [テキストブロック]
				self.BusinessRisksTextBlock = fact.value

			elif fact.concept.qname.localName == 'MaterialMattersRelatingToGoingConcernEtcBusinessRisksTextBlock': #重要事象等の内容、分析及び対応策、事業等のリスク [テキストブロック]
				self.MaterialMattersRelatingToGoingConcernEtcBusinessRisksTextBlock = fact.value

			elif fact.concept.qname.localName == 'ManagementAnalysisOfFinancialPositionOperatingResultsAndCashFlowsHeading': #経営者による財政状態、経営成績及びキャッシュ・フローの状況の分析 [目次項目]
				self.ManagementAnalysisOfFinancialPositionOperatingResultsAndCashFlowsHeading = fact.value

			elif fact.concept.qname.localName == 'ManagementAnalysisOfFinancialPositionOperatingResultsAndCashFlowsTextBlock': #経営者による財政状態、経営成績及びキャッシュ・フローの状況の分析 [テキストブロック]
				self.ManagementAnalysisOfFinancialPositionOperatingResultsAndCashFlowsTextBlock = fact.value

			elif fact.concept.qname.localName == 'CriticalContractsForOperationHeading': #経営上の重要な契約等 [目次項目]
				self.CriticalContractsForOperationHeading = fact.value

			elif fact.concept.qname.localName == 'CriticalContractsForOperationTextBlock': #経営上の重要な契約等 [テキストブロック]
				self.CriticalContractsForOperationTextBlock = fact.value

			elif fact.concept.qname.localName == 'ResearchAndDevelopmentActivitiesHeading': #研究開発活動 [目次項目]
				self.ResearchAndDevelopmentActivitiesHeading = fact.value

			elif fact.concept.qname.localName == 'ResearchAndDevelopmentActivitiesTextBlock': #研究開発活動 [テキストブロック]
				self.ResearchAndDevelopmentActivitiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'ResearchAndDevelopmentActivitiesHeading': #研究開発活動 [目次項目]
				self.ResearchAndDevelopmentActivitiesHeading = fact.value

			elif fact.concept.qname.localName == 'ResearchAndDevelopmentExpensesResearchAndDevelopmentActivitiesTable': #研究開発費、研究開発活動 [表]
				self.ResearchAndDevelopmentExpensesResearchAndDevelopmentActivitiesTable = fact.value

			elif fact.concept.qname.localName == 'OperatingSegmentsAxis': #事業セグメント [軸]
				self.OperatingSegmentsAxis = fact.value

			elif fact.concept.qname.localName == 'EntityTotalMember': #連結合計又は会社合計 [メンバー] ※ディメンションデフォルト
				self.EntityTotalMember = fact.value

			elif fact.concept.qname.localName == 'ReportableSegmentsMember': #報告セグメント [メンバー]
				self.ReportableSegmentsMember = fact.value

			elif fact.concept.qname.localName == 'OtherReportableSegmentsMember': #その他の報告セグメント [メンバー]
				self.OtherReportableSegmentsMember = fact.value

			elif fact.concept.qname.localName == 'ResearchAndDevelopmentExpensesResearchAndDevelopmentActivitiesLineItems': #研究開発費、研究開発活動 [表示項目]
				self.ResearchAndDevelopmentExpensesResearchAndDevelopmentActivitiesLineItems = fact.value

			elif fact.concept.qname.localName == 'ResearchAndDevelopmentExpensesResearchAndDevelopmentActivities': #研究開発費、研究開発活動
				self.ResearchAndDevelopmentExpensesResearchAndDevelopmentActivities = fact.value

			elif fact.concept.qname.localName == 'InformationAboutFacilitiesHeading': #設備の状況 [目次項目]
				self.InformationAboutFacilitiesHeading = fact.value

			elif fact.concept.qname.localName == 'OverviewOfCapitalExpendituresEtcHeading': #設備投資等の概要 [目次項目]
				self.OverviewOfCapitalExpendituresEtcHeading = fact.value

			elif fact.concept.qname.localName == 'OverviewOfCapitalExpendituresEtcTextBlock': #設備投資等の概要 [テキストブロック]
				self.OverviewOfCapitalExpendituresEtcTextBlock = fact.value

			elif fact.concept.qname.localName == 'OverviewOfCapitalExpendituresEtcHeading': #設備投資等の概要 [目次項目]
				self.OverviewOfCapitalExpendituresEtcHeading = fact.value

			elif fact.concept.qname.localName == 'CapitalExpendituresOverviewOfCapitalExpendituresEtcTable': #設備投資額、設備投資等の概要 [表]
				self.CapitalExpendituresOverviewOfCapitalExpendituresEtcTable = fact.value

			elif fact.concept.qname.localName == 'OperatingSegmentsAxis': #事業セグメント [軸]
				self.OperatingSegmentsAxis = fact.value

			elif fact.concept.qname.localName == 'EntityTotalMember': #連結合計又は会社合計 [メンバー] ※ディメンションデフォルト
				self.EntityTotalMember = fact.value

			elif fact.concept.qname.localName == 'ReportableSegmentsMember': #報告セグメント [メンバー]
				self.ReportableSegmentsMember = fact.value

			elif fact.concept.qname.localName == 'OtherReportableSegmentsMember': #その他の報告セグメント [メンバー]
				self.OtherReportableSegmentsMember = fact.value

			elif fact.concept.qname.localName == 'CapitalExpendituresOverviewOfCapitalExpendituresEtcLineItems': #設備投資額、設備投資等の概要 [表示項目]
				self.CapitalExpendituresOverviewOfCapitalExpendituresEtcLineItems = fact.value

			elif fact.concept.qname.localName == 'CapitalExpendituresOverviewOfCapitalExpendituresEtc': #設備投資額、設備投資等の概要
				self.CapitalExpendituresOverviewOfCapitalExpendituresEtc = fact.value

			elif fact.concept.qname.localName == 'MajorFacilitiesHeading': #主要な設備の状況 [目次項目]
				self.MajorFacilitiesHeading = fact.value

			elif fact.concept.qname.localName == 'MajorFacilitiesTextBlock': #主要な設備の状況 [テキストブロック]
				self.MajorFacilitiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'PlannedAdditionsRetirementsEtcOfFacilitiesHeading': #設備の新設、除却等の計画 [目次項目]
				self.PlannedAdditionsRetirementsEtcOfFacilitiesHeading = fact.value

			elif fact.concept.qname.localName == 'PlannedAdditionsRetirementsEtcOfFacilitiesTextBlock': #設備の新設、除却等の計画 [テキストブロック]
				self.PlannedAdditionsRetirementsEtcOfFacilitiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'AssetsForLeaseLEAHeading': #賃貸資産、リース事業 [目次項目]
				self.AssetsForLeaseLEAHeading = fact.value

			elif fact.concept.qname.localName == 'OverviewOfCapitalExpendituresEtcAssetsForLeaseLEAHeading': #設備投資等の概要、賃貸資産、リース事業 [目次項目]
				self.OverviewOfCapitalExpendituresEtcAssetsForLeaseLEAHeading = fact.value

			elif fact.concept.qname.localName == 'OverviewOfCapitalExpendituresEtcAssetsForLeaseLEATextBlock': #設備投資等の概要、賃貸資産、リース事業 [テキストブロック]
				self.OverviewOfCapitalExpendituresEtcAssetsForLeaseLEATextBlock = fact.value

			elif fact.concept.qname.localName == 'MajorFacilitiesAssetsForLeaseLEAHeading': #主要な設備の状況、賃貸資産、リース事業 [目次項目]
				self.MajorFacilitiesAssetsForLeaseLEAHeading = fact.value

			elif fact.concept.qname.localName == 'MajorFacilitiesAssetsForLeaseLEATextBlock': #主要な設備の状況、賃貸資産、リース事業 [テキストブロック]
				self.MajorFacilitiesAssetsForLeaseLEATextBlock = fact.value

			elif fact.concept.qname.localName == 'PlannedAdditionsRetirementsEtcOfFacilitiesAssetsForLeaseLEAHeading': #設備の新設、除却等の計画、賃貸資産、リース事業 [目次項目]
				self.PlannedAdditionsRetirementsEtcOfFacilitiesAssetsForLeaseLEAHeading = fact.value

			elif fact.concept.qname.localName == 'PlannedAdditionsRetirementsEtcOfFacilitiesAssetsForLeaseLEATextBlock': #設備の新設、除却等の計画、賃貸資産、リース事業 [テキストブロック]
				self.PlannedAdditionsRetirementsEtcOfFacilitiesAssetsForLeaseLEATextBlock = fact.value

			elif fact.concept.qname.localName == 'OwnUsedAssetsLEAHeading': #自社用資産、リース事業 [目次項目]
				self.OwnUsedAssetsLEAHeading = fact.value

			elif fact.concept.qname.localName == 'OverviewOfCapitalExpendituresEtcOwnUsedAssetsLEAHeading': #設備投資等の概要、自社用資産、リース事業 [目次項目]
				self.OverviewOfCapitalExpendituresEtcOwnUsedAssetsLEAHeading = fact.value

			elif fact.concept.qname.localName == 'OverviewOfCapitalExpendituresEtcOwnUsedAssetsLEATextBlock': #設備投資等の概要、自社用資産、リース事業 [テキストブロック]
				self.OverviewOfCapitalExpendituresEtcOwnUsedAssetsLEATextBlock = fact.value

			elif fact.concept.qname.localName == 'MajorFacilitiesOwnUsedAssetsLEAHeading': #主要な設備の状況、自社用資産、リース事業 [目次項目]
				self.MajorFacilitiesOwnUsedAssetsLEAHeading = fact.value

			elif fact.concept.qname.localName == 'MajorFacilitiesOwnUsedAssetsLEATextBlock': #主要な設備の状況、自社用資産、リース事業 [テキストブロック]
				self.MajorFacilitiesOwnUsedAssetsLEATextBlock = fact.value

			elif fact.concept.qname.localName == 'PlannedAdditionsRetirementsEtcOfFacilitiesOwnUsedAssetsLEAHeading': #設備の新設、除却等の計画、自社用資産、リース事業 [目次項目]
				self.PlannedAdditionsRetirementsEtcOfFacilitiesOwnUsedAssetsLEAHeading = fact.value

			elif fact.concept.qname.localName == 'PlannedAdditionsRetirementsEtcOfFacilitiesOwnUsedAssetsLEATextBlock': #設備の新設、除却等の計画、自社用資産、リース事業 [テキストブロック]
				self.PlannedAdditionsRetirementsEtcOfFacilitiesOwnUsedAssetsLEATextBlock = fact.value

			elif fact.concept.qname.localName == 'InformationAboutReportingCompanyHeading': #提出会社の状況 [目次項目]
				self.InformationAboutReportingCompanyHeading = fact.value

			elif fact.concept.qname.localName == 'InformationAboutSharesEtcHeading': #株式等の状況 [目次項目]
				self.InformationAboutSharesEtcHeading = fact.value

			elif fact.concept.qname.localName == 'TotalNumberOfSharesEtcHeading': #株式の総数等 [目次項目]
				self.TotalNumberOfSharesEtcHeading = fact.value

			elif fact.concept.qname.localName == 'TotalNumberOfSharesHeading': #株式の総数 [目次項目]
				self.TotalNumberOfSharesHeading = fact.value

			elif fact.concept.qname.localName == 'TotalNumberOfSharesTextBlock': #株式の総数 [テキストブロック]
				self.TotalNumberOfSharesTextBlock = fact.value

			elif fact.concept.qname.localName == 'IssuedSharesTotalNumberOfSharesEtcHeading': #発行済株式、株式の総数等 [目次項目]
				self.IssuedSharesTotalNumberOfSharesEtcHeading = fact.value

			elif fact.concept.qname.localName == 'IssuedSharesTotalNumberOfSharesEtcTextBlock': #発行済株式、株式の総数等 [テキストブロック]
				self.IssuedSharesTotalNumberOfSharesEtcTextBlock = fact.value

			elif fact.concept.qname.localName == 'IssuedSharesTotalNumberOfSharesEtcHeading': #発行済株式、株式の総数等 [目次項目]
				self.IssuedSharesTotalNumberOfSharesEtcHeading = fact.value

			elif fact.concept.qname.localName == 'IssuedSharesTotalNumberOfSharesEtcTable': #発行済株式、株式の総数等 [表]
				self.IssuedSharesTotalNumberOfSharesEtcTable = fact.value

			elif fact.concept.qname.localName == 'ClassesOfSharesAxis': #株式種類 [軸]
				self.ClassesOfSharesAxis = fact.value

			elif fact.concept.qname.localName == 'TotalClassesOfSharesMember': #合計、株式種類 [メンバー] ※ディメンションデフォルト
				self.TotalClassesOfSharesMember = fact.value

			elif fact.concept.qname.localName == 'OrdinaryShareMember': #普通株式 [メンバー]
				self.OrdinaryShareMember = fact.value

			elif fact.concept.qname.localName == 'ClassAPreferredSharesMember': #Ａ種優先株式 [メンバー]
				self.ClassAPreferredSharesMember = fact.value

			elif fact.concept.qname.localName == 'ClassBPreferredSharesMember': #Ｂ種優先株式 [メンバー]
				self.ClassBPreferredSharesMember = fact.value

			elif fact.concept.qname.localName == 'ClassOnePreferredSharesMember': #第一種優先株式 [メンバー]
				self.ClassOnePreferredSharesMember = fact.value

			elif fact.concept.qname.localName == 'ClassTwoPreferredSharesMember': #第二種優先株式 [メンバー]
				self.ClassTwoPreferredSharesMember = fact.value

			elif fact.concept.qname.localName == 'ClassASharesMember': #Ａ種種類株式 [メンバー]
				self.ClassASharesMember = fact.value

			elif fact.concept.qname.localName == 'IssuedSharesTotalNumberOfSharesEtcLineItems': #発行済株式、株式の総数等 [表示項目]
				self.IssuedSharesTotalNumberOfSharesEtcLineItems = fact.value

			elif fact.concept.qname.localName == 'ClassIssuedSharesTotalNumberOfSharesEtc': #種類、発行済株式、株式の総数等
				self.ClassIssuedSharesTotalNumberOfSharesEtc = fact.value

			elif fact.concept.qname.localName == 'NumberOfIssuedSharesIssuedSharesTotalNumberOfSharesEtc': #発行数（株）、発行済株式、株式の総数等
				self.NumberOfIssuedSharesIssuedSharesTotalNumberOfSharesEtc = fact.value

			elif fact.concept.qname.localName == 'NumberOfIssuedSharesAsOfFiscalYearEndIssuedSharesTotalNumberOfSharesEtc': #事業年度末現在発行数（株）、発行済株式、株式の総数等
				self.NumberOfIssuedSharesAsOfFiscalYearEndIssuedSharesTotalNumberOfSharesEtc = fact.value

			elif fact.concept.qname.localName == 'NumberOfIssuedSharesAsOfFilingDateIssuedSharesTotalNumberOfSharesEtc': #提出日現在発行数（株）、発行済株式、株式の総数等
				self.NumberOfIssuedSharesAsOfFilingDateIssuedSharesTotalNumberOfSharesEtc = fact.value

			elif fact.concept.qname.localName == 'NameOfFinancialInstrumentsExchangeOnWhichSecuritiesAreListedOrAuthorizedFinancialInstrumentsBusinessAssociationToWhichSecuritiesAreRegistered': #上場金融商品取引所名又は登録認可金融商品取引業協会名
				self.NameOfFinancialInstrumentsExchangeOnWhichSecuritiesAreListedOrAuthorizedFinancialInstrumentsBusinessAssociationToWhichSecuritiesAreRegistered = fact.value

			elif fact.concept.qname.localName == 'DescriptionIssuedSharesTotalNumberOfSharesEtc': #内容、発行済株式、株式の総数等
				self.DescriptionIssuedSharesTotalNumberOfSharesEtc = fact.value

			elif fact.concept.qname.localName == 'SubscriptionRightsToSharesEtcHeading': #新株予約権等の状況 [目次項目]
				self.SubscriptionRightsToSharesEtcHeading = fact.value

			elif fact.concept.qname.localName == 'DetailsOfEmployeeShareOptionProgramHeading': #ストックオプション制度の内容 [目次項目]
				self.DetailsOfEmployeeShareOptionProgramHeading = fact.value

			elif fact.concept.qname.localName == 'DetailsOfEmployeeShareOptionProgramTextBlock': #ストックオプション制度の内容 [テキストブロック]
				self.DetailsOfEmployeeShareOptionProgramTextBlock = fact.value

			elif fact.concept.qname.localName == 'DescriptionOfRightsPlanHeading': #ライツプランの内容 [目次項目]
				self.DescriptionOfRightsPlanHeading = fact.value

			elif fact.concept.qname.localName == 'DescriptionOfRightsPlanTextBlock': #ライツプランの内容 [テキストブロック]
				self.DescriptionOfRightsPlanTextBlock = fact.value

			elif fact.concept.qname.localName == 'OtherInformationOnShareAcquisitionRightsHeading': #その他の新株予約権等の状況 [目次項目]
				self.OtherInformationOnShareAcquisitionRightsHeading = fact.value

			elif fact.concept.qname.localName == 'OtherInformationOnShareAcquisitionRightsTextBlock': #その他の新株予約権等の状況 [テキストブロック]
				self.OtherInformationOnShareAcquisitionRightsTextBlock = fact.value

			elif fact.concept.qname.localName == 'ExercisesEtcOfMovingStrikeConvertibleBondsEtcHeading': #行使価額修正条項付新株予約権付社債券等の行使状況等 [目次項目]
				self.ExercisesEtcOfMovingStrikeConvertibleBondsEtcHeading = fact.value

			elif fact.concept.qname.localName == 'ExercisesEtcOfMovingStrikeConvertibleBondsEtcTextBlock': #行使価額修正条項付新株予約権付社債券等の行使状況等 [テキストブロック]
				self.ExercisesEtcOfMovingStrikeConvertibleBondsEtcTextBlock = fact.value

			elif fact.concept.qname.localName == 'ChangesInNumberOfIssuedSharesStatedCapitalEtcHeading': #発行済株式総数、資本金等の推移 [目次項目]
				self.ChangesInNumberOfIssuedSharesStatedCapitalEtcHeading = fact.value

			elif fact.concept.qname.localName == 'ChangesInNumberOfIssuedSharesStatedCapitalEtcTextBlock': #発行済株式総数、資本金等の推移 [テキストブロック]
				self.ChangesInNumberOfIssuedSharesStatedCapitalEtcTextBlock = fact.value

			elif fact.concept.qname.localName == 'ShareholdingByShareholderCategoryHeading': #所有者別状況 [目次項目]
				self.ShareholdingByShareholderCategoryHeading = fact.value

			elif fact.concept.qname.localName == 'ShareholdingByShareholderCategoryTextBlock': #所有者別状況 [テキストブロック]
				self.ShareholdingByShareholderCategoryTextBlock = fact.value

			elif fact.concept.qname.localName == 'ShareholdingByShareholderCategoryHeading': #所有者別状況 [目次項目]
				self.ShareholdingByShareholderCategoryHeading = fact.value

			elif fact.concept.qname.localName == 'ShareholdingByShareholderCategoryTable': #所有者別状況 [表]
				self.ShareholdingByShareholderCategoryTable = fact.value

			elif fact.concept.qname.localName == 'ClassesOfSharesAxis': #株式種類 [軸]
				self.ClassesOfSharesAxis = fact.value

			elif fact.concept.qname.localName == 'TotalClassesOfSharesMember': #合計、株式種類 [メンバー] ※ディメンションデフォルト
				self.TotalClassesOfSharesMember = fact.value

			elif fact.concept.qname.localName == 'OrdinaryShareMember': #普通株式 [メンバー]
				self.OrdinaryShareMember = fact.value

			elif fact.concept.qname.localName == 'ClassAPreferredSharesMember': #Ａ種優先株式 [メンバー]
				self.ClassAPreferredSharesMember = fact.value

			elif fact.concept.qname.localName == 'ClassBPreferredSharesMember': #Ｂ種優先株式 [メンバー]
				self.ClassBPreferredSharesMember = fact.value

			elif fact.concept.qname.localName == 'ClassOnePreferredSharesMember': #第一種優先株式 [メンバー]
				self.ClassOnePreferredSharesMember = fact.value

			elif fact.concept.qname.localName == 'ClassTwoPreferredSharesMember': #第二種優先株式 [メンバー]
				self.ClassTwoPreferredSharesMember = fact.value

			elif fact.concept.qname.localName == 'ClassASharesMember': #Ａ種種類株式 [メンバー]
				self.ClassASharesMember = fact.value

			elif fact.concept.qname.localName == 'ShareholdingByShareholderCategoryLineItems': #所有者別状況 [表示項目]
				self.ShareholdingByShareholderCategoryLineItems = fact.value

			elif fact.concept.qname.localName == 'NumberOfSharesConstitutingOneUnit': #１単元の株式数
				self.NumberOfSharesConstitutingOneUnit = fact.value

			elif fact.concept.qname.localName == 'NumberOfShareholdersNationalAndLocalGovernments': #株主数－政府及び地方公共団体
				self.NumberOfShareholdersNationalAndLocalGovernments = fact.value

			elif fact.concept.qname.localName == 'NumberOfShareholdersFinancialInstitutions': #株主数－金融機関
				self.NumberOfShareholdersFinancialInstitutions = fact.value

			elif fact.concept.qname.localName == 'NumberOfShareholdersFinancialServiceProviders': #株主数－金融商品取引業者
				self.NumberOfShareholdersFinancialServiceProviders = fact.value

			elif fact.concept.qname.localName == 'NumberOfShareholdersOtherCorporations': #株主数－その他の法人
				self.NumberOfShareholdersOtherCorporations = fact.value

			elif fact.concept.qname.localName == 'NumberOfShareholdersForeignInvestorsOtherThanIndividuals': #株主数－外国法人等－個人以外
				self.NumberOfShareholdersForeignInvestorsOtherThanIndividuals = fact.value

			elif fact.concept.qname.localName == 'NumberOfShareholdersForeignIndividualInvestors': #株主数－外国法人等－個人
				self.NumberOfShareholdersForeignIndividualInvestors = fact.value

			elif fact.concept.qname.localName == 'NumberOfShareholdersIndividualsAndOthers': #株主数－個人その他
				self.NumberOfShareholdersIndividualsAndOthers = fact.value

			elif fact.concept.qname.localName == 'NumberOfShareholdersTotal': #株主数－計
				self.NumberOfShareholdersTotal = fact.value

			elif fact.concept.qname.localName == 'NumberOfSharesHeldNumberOfUnitsNationalAndLocalGovernments': #所有株式数（単元）－政府及び地方公共団体
				self.NumberOfSharesHeldNumberOfUnitsNationalAndLocalGovernments = fact.value

			elif fact.concept.qname.localName == 'NumberOfSharesHeldNumberOfUnitsFinancialInstitutions': #所有株式数（単元）－金融機関
				self.NumberOfSharesHeldNumberOfUnitsFinancialInstitutions = fact.value

			elif fact.concept.qname.localName == 'NumberOfSharesHeldNumberOfUnitsFinancialServiceProviders': #所有株式数（単元）－金融商品取引業者
				self.NumberOfSharesHeldNumberOfUnitsFinancialServiceProviders = fact.value

			elif fact.concept.qname.localName == 'NumberOfSharesHeldNumberOfUnitsOtherCorporations': #所有株式数（単元）－その他の法人
				self.NumberOfSharesHeldNumberOfUnitsOtherCorporations = fact.value

			elif fact.concept.qname.localName == 'NumberOfSharesHeldNumberOfUnitsForeignInvestorsOtherThanIndividuals': #所有株式数（単元）－外国法人等－個人以外
				self.NumberOfSharesHeldNumberOfUnitsForeignInvestorsOtherThanIndividuals = fact.value

			elif fact.concept.qname.localName == 'NumberOfSharesHeldNumberOfUnitsForeignIndividualInvestors': #所有株式数（単元）－外国法人等－個人
				self.NumberOfSharesHeldNumberOfUnitsForeignIndividualInvestors = fact.value

			elif fact.concept.qname.localName == 'NumberOfSharesHeldNumberOfUnitsIndividualsAndOthers': #所有株式数（単元）－個人その他
				self.NumberOfSharesHeldNumberOfUnitsIndividualsAndOthers = fact.value

			elif fact.concept.qname.localName == 'NumberOfSharesHeldNumberOfUnitsTotal': #所有株式数（単元）－計
				self.NumberOfSharesHeldNumberOfUnitsTotal = fact.value

			elif fact.concept.qname.localName == 'NumberOfSharesHeldSharesLessThanOneUnit': #所有株式数－単元未満株式の状況（株）
				self.NumberOfSharesHeldSharesLessThanOneUnit = fact.value

			elif fact.concept.qname.localName == 'PercentageOfShareholdingsNationalAndLocalGovernments': #所有株式数の割合（％）－政府及び地方公共団体
				self.PercentageOfShareholdingsNationalAndLocalGovernments = fact.value

			elif fact.concept.qname.localName == 'PercentageOfShareholdingsFinancialInstitutions': #所有株式数の割合（％）－金融機関
				self.PercentageOfShareholdingsFinancialInstitutions = fact.value

			elif fact.concept.qname.localName == 'PercentageOfShareholdingsFinancialServiceProviders': #所有株式数の割合（％）－金融商品取引業者
				self.PercentageOfShareholdingsFinancialServiceProviders = fact.value

			elif fact.concept.qname.localName == 'PercentageOfShareholdingsOtherCorporations': #所有株式数の割合（％）－その他の法人
				self.PercentageOfShareholdingsOtherCorporations = fact.value

			elif fact.concept.qname.localName == 'PercentageOfShareholdingsForeignersOtherThanIndividuals': #所有株式数の割合（％）－外国法人等－個人以外
				self.PercentageOfShareholdingsForeignersOtherThanIndividuals = fact.value

			elif fact.concept.qname.localName == 'PercentageOfShareholdingsForeignIndividuals': #所有株式数の割合（％）－外国法人等－個人
				self.PercentageOfShareholdingsForeignIndividuals = fact.value

			elif fact.concept.qname.localName == 'PercentageOfShareholdingsIndividualsAndOthers': #所有株式数の割合（％）－個人その他
				self.PercentageOfShareholdingsIndividualsAndOthers = fact.value

			elif fact.concept.qname.localName == 'MajorShareholdersHeading': #大株主の状況 [目次項目]
				self.MajorShareholdersHeading = fact.value

			elif fact.concept.qname.localName == 'MajorShareholdersTextBlock': #大株主の状況 [テキストブロック]
				self.MajorShareholdersTextBlock = fact.value

			elif fact.concept.qname.localName == 'MajorShareholdersHeading': #大株主の状況 [目次項目]
				self.MajorShareholdersHeading = fact.value

			elif fact.concept.qname.localName == 'MajorShareholdersTable': #大株主の状況 [表]
				self.MajorShareholdersTable = fact.value

			elif fact.concept.qname.localName == 'MajorShareholdersAxis': #大株主 [軸]
				self.MajorShareholdersAxis = fact.value

			elif fact.concept.qname.localName == 'MajorShareholdersMember': #大株主 [メンバー] ※ディメンションデフォルト
				self.MajorShareholdersMember = fact.value

			elif fact.concept.qname.localName == 'No1MajorShareholdersMember': #第1位、大株主 [メンバー]
				self.No1MajorShareholdersMember = fact.value

			elif fact.concept.qname.localName == 'No2MajorShareholdersMember': #第2位、大株主 [メンバー]
				self.No2MajorShareholdersMember = fact.value

			elif fact.concept.qname.localName == 'No3MajorShareholdersMember': #第3位、大株主 [メンバー]
				self.No3MajorShareholdersMember = fact.value

			elif fact.concept.qname.localName == 'No4MajorShareholdersMember': #第4位、大株主 [メンバー]
				self.No4MajorShareholdersMember = fact.value

			elif fact.concept.qname.localName == 'No5MajorShareholdersMember': #第5位、大株主 [メンバー]
				self.No5MajorShareholdersMember = fact.value

			elif fact.concept.qname.localName == 'No6MajorShareholdersMember': #第6位、大株主 [メンバー]
				self.No6MajorShareholdersMember = fact.value

			elif fact.concept.qname.localName == 'No7MajorShareholdersMember': #第7位、大株主 [メンバー]
				self.No7MajorShareholdersMember = fact.value

			elif fact.concept.qname.localName == 'No8MajorShareholdersMember': #第8位、大株主 [メンバー]
				self.No8MajorShareholdersMember = fact.value

			elif fact.concept.qname.localName == 'No9MajorShareholdersMember': #第9位、大株主 [メンバー]
				self.No9MajorShareholdersMember = fact.value

			elif fact.concept.qname.localName == 'No10MajorShareholdersMember': #第10位、大株主 [メンバー]
				self.No10MajorShareholdersMember = fact.value

			elif fact.concept.qname.localName == 'No11MajorShareholdersMember': #第11位、大株主 [メンバー]
				self.No11MajorShareholdersMember = fact.value

			elif fact.concept.qname.localName == 'No12MajorShareholdersMember': #第12位、大株主 [メンバー]
				self.No12MajorShareholdersMember = fact.value

			elif fact.concept.qname.localName == 'No13MajorShareholdersMember': #第13位、大株主 [メンバー]
				self.No13MajorShareholdersMember = fact.value

			elif fact.concept.qname.localName == 'No14MajorShareholdersMember': #第14位、大株主 [メンバー]
				self.No14MajorShareholdersMember = fact.value

			elif fact.concept.qname.localName == 'No15MajorShareholdersMember': #第15位、大株主 [メンバー]
				self.No15MajorShareholdersMember = fact.value

			elif fact.concept.qname.localName == 'MajorShareholdersLineItems': #大株主の状況 [表示項目]
				self.MajorShareholdersLineItems = fact.value

			elif fact.concept.qname.localName == 'NameMajorShareholders': #氏名又は名称、大株主の状況
				self.NameMajorShareholders = fact.value

			elif fact.concept.qname.localName == 'AddressMajorShareholders': #住所、大株主の状況
				self.AddressMajorShareholders = fact.value

			elif fact.concept.qname.localName == 'NumberOfSharesHeld': #所有株式数
				self.NumberOfSharesHeld = fact.value

			elif fact.concept.qname.localName == 'ShareholdingRatio': #発行済株式（自己株式を除く。）の総数に対する所有株式数の割合
				self.ShareholdingRatio = fact.value

			elif fact.concept.qname.localName == 'MajorShareholdersHeading': #大株主の状況 [目次項目]
				self.MajorShareholdersHeading = fact.value

			elif fact.concept.qname.localName == 'MajorShareholdersVotingRightsTable': #所有株式に係る議決権上位者の状況 [表]
				self.MajorShareholdersVotingRightsTable = fact.value

			elif fact.concept.qname.localName == 'MajorShareholdersVotingRightsAxis': #議決権上位 [軸]
				self.MajorShareholdersVotingRightsAxis = fact.value

			elif fact.concept.qname.localName == 'MajorShareholdersVotingRightsMember': #議決権上位 [メンバー] ※ディメンションデフォルト
				self.MajorShareholdersVotingRightsMember = fact.value

			elif fact.concept.qname.localName == 'No1MajorShareholdersVotingRightsMember': #第1位、議決権上位 [メンバー]
				self.No1MajorShareholdersVotingRightsMember = fact.value

			elif fact.concept.qname.localName == 'No2MajorShareholdersVotingRightsMember': #第2位、議決権上位 [メンバー]
				self.No2MajorShareholdersVotingRightsMember = fact.value

			elif fact.concept.qname.localName == 'No3MajorShareholdersVotingRightsMember': #第3位、議決権上位 [メンバー]
				self.No3MajorShareholdersVotingRightsMember = fact.value

			elif fact.concept.qname.localName == 'No4MajorShareholdersVotingRightsMember': #第4位、議決権上位 [メンバー]
				self.No4MajorShareholdersVotingRightsMember = fact.value

			elif fact.concept.qname.localName == 'No5MajorShareholdersVotingRightsMember': #第5位、議決権上位 [メンバー]
				self.No5MajorShareholdersVotingRightsMember = fact.value

			elif fact.concept.qname.localName == 'No6MajorShareholdersVotingRightsMember': #第6位、議決権上位 [メンバー]
				self.No6MajorShareholdersVotingRightsMember = fact.value

			elif fact.concept.qname.localName == 'No7MajorShareholdersVotingRightsMember': #第7位、議決権上位 [メンバー]
				self.No7MajorShareholdersVotingRightsMember = fact.value

			elif fact.concept.qname.localName == 'No8MajorShareholdersVotingRightsMember': #第8位、議決権上位 [メンバー]
				self.No8MajorShareholdersVotingRightsMember = fact.value

			elif fact.concept.qname.localName == 'No9MajorShareholdersVotingRightsMember': #第9位、議決権上位 [メンバー]
				self.No9MajorShareholdersVotingRightsMember = fact.value

			elif fact.concept.qname.localName == 'No10MajorShareholdersVotingRightsMember': #第10位、議決権上位 [メンバー]
				self.No10MajorShareholdersVotingRightsMember = fact.value

			elif fact.concept.qname.localName == 'No11MajorShareholdersVotingRightsMember': #第11位、議決権上位 [メンバー]
				self.No11MajorShareholdersVotingRightsMember = fact.value

			elif fact.concept.qname.localName == 'No12MajorShareholdersVotingRightsMember': #第12位、議決権上位 [メンバー]
				self.No12MajorShareholdersVotingRightsMember = fact.value

			elif fact.concept.qname.localName == 'No13MajorShareholdersVotingRightsMember': #第13位、議決権上位 [メンバー]
				self.No13MajorShareholdersVotingRightsMember = fact.value

			elif fact.concept.qname.localName == 'No14MajorShareholdersVotingRightsMember': #第14位、議決権上位 [メンバー]
				self.No14MajorShareholdersVotingRightsMember = fact.value

			elif fact.concept.qname.localName == 'No15MajorShareholdersVotingRightsMember': #第15位、議決権上位 [メンバー]
				self.No15MajorShareholdersVotingRightsMember = fact.value

			elif fact.concept.qname.localName == 'MajorShareholdersVotingRightsLineItems': #所有株式に係る議決権上位者の状況 [表示項目]
				self.MajorShareholdersVotingRightsLineItems = fact.value

			elif fact.concept.qname.localName == 'NameMajorShareholdersVotingRights': #氏名又は名称、所有株式に係る議決権上位者の状況
				self.NameMajorShareholdersVotingRights = fact.value

			elif fact.concept.qname.localName == 'AddressMajorShareholdersVotingRights': #住所、所有株式に係る議決権上位者の状況
				self.AddressMajorShareholdersVotingRights = fact.value

			elif fact.concept.qname.localName == 'NumberOfVotingRightsHeld': #所有議決権数（個）
				self.NumberOfVotingRightsHeld = fact.value

			elif fact.concept.qname.localName == 'RatioOfVotingRightsHeld': #総株主の議決権に対する所有議決権数の割合
				self.RatioOfVotingRightsHeld = fact.value

			elif fact.concept.qname.localName == 'VotingRightsHeading': #議決権の状況 [目次項目]
				self.VotingRightsHeading = fact.value

			elif fact.concept.qname.localName == 'VotingRightsTextBlock': #議決権の状況 [テキストブロック]
				self.VotingRightsTextBlock = fact.value

			elif fact.concept.qname.localName == 'IssuedSharesVotingRightsHeading': #発行済株式、議決権の状況 [目次項目]
				self.IssuedSharesVotingRightsHeading = fact.value

			elif fact.concept.qname.localName == 'IssuedSharesVotingRightsTextBlock': #発行済株式、議決権の状況 [テキストブロック]
				self.IssuedSharesVotingRightsTextBlock = fact.value

			elif fact.concept.qname.localName == 'IssuedSharesVotingRightsHeading': #発行済株式、議決権の状況 [目次項目]
				self.IssuedSharesVotingRightsHeading = fact.value

			elif fact.concept.qname.localName == 'IssuedSharesVotingRightsTable': #発行済株式、議決権の状況 [表]
				self.IssuedSharesVotingRightsTable = fact.value

			elif fact.concept.qname.localName == 'CategoriesIssuedSharesAxis': #区分、発行済株式 [軸]
				self.CategoriesIssuedSharesAxis = fact.value

			elif fact.concept.qname.localName == 'TotalNumberOfIssuedSharesNumberOfVotingRightsHeldByAllShareholdersMember': #発行済株式総数／総株主の議決権 [メンバー] ※ディメンションデフォルト
				self.TotalNumberOfIssuedSharesNumberOfVotingRightsHeldByAllShareholdersMember = fact.value

			elif fact.concept.qname.localName == 'SharesWithNoVotingRightsMember': #無議決権株式 [メンバー]
				self.SharesWithNoVotingRightsMember = fact.value

			elif fact.concept.qname.localName == 'SharesWithRestrictedVotingRightsTreasurySharesEtcMember': #議決権制限株式（自己株式等） [メンバー]
				self.SharesWithRestrictedVotingRightsTreasurySharesEtcMember = fact.value

			elif fact.concept.qname.localName == 'SharesWithRestrictedVotingRightsOtherMember': #議決権制限株式（その他） [メンバー]
				self.SharesWithRestrictedVotingRightsOtherMember = fact.value

			elif fact.concept.qname.localName == 'SharesWithFullVotingRightsTreasurySharesEtcMember': #完全議決権株式（自己株式等） [メンバー]
				self.SharesWithFullVotingRightsTreasurySharesEtcMember = fact.value

			elif fact.concept.qname.localName == 'OrdinarySharesSharesWithFullVotingRightsTreasurySharesEtcMember': #普通株式、完全議決権株式（自己株式等） [メンバー]
				self.OrdinarySharesSharesWithFullVotingRightsTreasurySharesEtcMember = fact.value

			elif fact.concept.qname.localName == 'OrdinarySharesTreasurySharesSharesWithFullVotingRightsTreasurySharesEtcMember': #（自己保有株式）普通株式、完全議決権株式（自己株式等） [メンバー]
				self.OrdinarySharesTreasurySharesSharesWithFullVotingRightsTreasurySharesEtcMember = fact.value

			elif fact.concept.qname.localName == 'OrdinarySharesReciprocalHoldingSharesWithFullVotingRightsTreasurySharesEtcMember': #（相互保有株式）普通株式、完全議決権株式（自己株式等） [メンバー]
				self.OrdinarySharesReciprocalHoldingSharesWithFullVotingRightsTreasurySharesEtcMember = fact.value

			elif fact.concept.qname.localName == 'SharesWithFullVotingRightsOtherMember': #完全議決権株式（その他） [メンバー]
				self.SharesWithFullVotingRightsOtherMember = fact.value

			elif fact.concept.qname.localName == 'OrdinarySharesSharesWithFullVotingRightsOtherMember': #普通株式、完全議決権株式（その他） [メンバー]
				self.OrdinarySharesSharesWithFullVotingRightsOtherMember = fact.value

			elif fact.concept.qname.localName == 'SharesLessThanOneUnitMember': #単元未満株式 [メンバー]
				self.SharesLessThanOneUnitMember = fact.value

			elif fact.concept.qname.localName == 'OrdinarySharesSharesLessThanOneUnitMember': #普通株式、単元未満株式 [メンバー]
				self.OrdinarySharesSharesLessThanOneUnitMember = fact.value

			elif fact.concept.qname.localName == 'IssuedSharesVotingRightsLineItems': #発行済株式、議決権の状況 [表示項目]
				self.IssuedSharesVotingRightsLineItems = fact.value

			elif fact.concept.qname.localName == 'NumberOfSharesIssuedSharesVotingRights': #株式数（株）、発行済株式、議決権の状況
				self.NumberOfSharesIssuedSharesVotingRights = fact.value

			elif fact.concept.qname.localName == 'NumberOfVotingRightsIssuedSharesVotingRights': #議決権の数（個）、発行済株式、議決権の状況
				self.NumberOfVotingRightsIssuedSharesVotingRights = fact.value

			elif fact.concept.qname.localName == 'DescriptionIssuedSharesVotingRights': #内容、発行済株式、議決権の状況
				self.DescriptionIssuedSharesVotingRights = fact.value

			elif fact.concept.qname.localName == 'TreasurySharesEtcHeading': #自己株式等 [目次項目]
				self.TreasurySharesEtcHeading = fact.value

			elif fact.concept.qname.localName == 'TreasurySharesEtcTextBlock': #自己株式等 [テキストブロック]
				self.TreasurySharesEtcTextBlock = fact.value

			elif fact.concept.qname.localName == 'TreasurySharesEtcHeading': #自己株式等 [目次項目]
				self.TreasurySharesEtcHeading = fact.value

			elif fact.concept.qname.localName == 'TreasurySharesEtcTable': #自己株式等 [表]
				self.TreasurySharesEtcTable = fact.value

			elif fact.concept.qname.localName == 'SequentialNumbersAxis': #連番 [軸]
				self.SequentialNumbersAxis = fact.value

			elif fact.concept.qname.localName == 'TotalSequentialNumbersMember': #合計、連番 [メンバー] ※ディメンションデフォルト
				self.TotalSequentialNumbersMember = fact.value

			elif fact.concept.qname.localName == 'Row1Member': #1件目 [メンバー]
				self.Row1Member = fact.value

			elif fact.concept.qname.localName == 'Row2Member': #2件目 [メンバー]
				self.Row2Member = fact.value

			elif fact.concept.qname.localName == 'Row3Member': #3件目 [メンバー]
				self.Row3Member = fact.value

			elif fact.concept.qname.localName == 'Row4Member': #4件目 [メンバー]
				self.Row4Member = fact.value

			elif fact.concept.qname.localName == 'TreasurySharesEtcLineItems': #自己株式等 [表示項目]
				self.TreasurySharesEtcLineItems = fact.value

			elif fact.concept.qname.localName == 'NameOfShareholderTreasurySharesEtc': #所有者の氏名又は名称、自己株式等
				self.NameOfShareholderTreasurySharesEtc = fact.value

			elif fact.concept.qname.localName == 'AddressOfShareholderTreasurySharesEtc': #所有者の住所、自己株式等
				self.AddressOfShareholderTreasurySharesEtc = fact.value

			elif fact.concept.qname.localName == 'NumberOfSharesHeldInOwnNameTreasurySharesEtc': #自己名義所有株式数（株）、自己株式等
				self.NumberOfSharesHeldInOwnNameTreasurySharesEtc = fact.value

			elif fact.concept.qname.localName == 'NumberOfSharesHeldInOthersNamesTreasurySharesEtc': #他人名義所有株式数（株）、自己株式等
				self.NumberOfSharesHeldInOthersNamesTreasurySharesEtc = fact.value

			elif fact.concept.qname.localName == 'TotalNumberOfSharesHeldTreasurySharesEtc': #所有株式数の合計（株）、自己株式等
				self.TotalNumberOfSharesHeldTreasurySharesEtc = fact.value

			elif fact.concept.qname.localName == 'ShareholdingRatioTreasurySharesEtc': #発行済株式総数に対する所有株式数の割合（％）、自己株式等
				self.ShareholdingRatioTreasurySharesEtc = fact.value

			elif fact.concept.qname.localName == 'DetailsOfTransfersOfSharesEtcByAcquirerHeading': #取得者の株式等の移動状況 [目次項目]
				self.DetailsOfTransfersOfSharesEtcByAcquirerHeading = fact.value

			elif fact.concept.qname.localName == 'DetailsOfTransfersOfSharesEtcByAcquirerTextBlock': #取得者の株式等の移動状況 [テキストブロック]
				self.DetailsOfTransfersOfSharesEtcByAcquirerTextBlock = fact.value

			elif fact.concept.qname.localName == 'ShareOwnershipPlansForDirectorsAndOtherOfficersAndEmployeesHeading': #役員・従業員株式所有制度の内容 [目次項目]
				self.ShareOwnershipPlansForDirectorsAndOtherOfficersAndEmployeesHeading = fact.value

			elif fact.concept.qname.localName == 'ShareOwnershipPlansForDirectorsAndOtherOfficersAndEmployeesTextBlock': #役員・従業員株式所有制度の内容 [テキストブロック]
				self.ShareOwnershipPlansForDirectorsAndOtherOfficersAndEmployeesTextBlock = fact.value

			elif fact.concept.qname.localName == 'AcquisitionsEtcOfTreasurySharesHeading': #自己株式の取得等の状況 [目次項目]
				self.AcquisitionsEtcOfTreasurySharesHeading = fact.value

			elif fact.concept.qname.localName == 'AcquisitionsEtcOfTreasurySharesTextBlock': #自己株式の取得等の状況 [テキストブロック]
				self.AcquisitionsEtcOfTreasurySharesTextBlock = fact.value

			elif fact.concept.qname.localName == 'ClassesOfSharesEtcHeading': #株式の種類等 [目次項目]
				self.ClassesOfSharesEtcHeading = fact.value

			elif fact.concept.qname.localName == 'ClassesOfSharesEtcTextBlock': #株式の種類等 [テキストブロック]
				self.ClassesOfSharesEtcTextBlock = fact.value

			elif fact.concept.qname.localName == 'AcquisitionsByResolutionOfShareholdersMeetingHeading': #株主総会決議による取得の状況 [目次項目]
				self.AcquisitionsByResolutionOfShareholdersMeetingHeading = fact.value

			elif fact.concept.qname.localName == 'AcquisitionsByResolutionOfShareholdersMeetingTextBlock': #株主総会決議による取得の状況 [テキストブロック]
				self.AcquisitionsByResolutionOfShareholdersMeetingTextBlock = fact.value

			elif fact.concept.qname.localName == 'AcquisitionsByResolutionOfBoardOfDirectorsMeetingHeading': #取締役会決議による取得の状況 [目次項目]
				self.AcquisitionsByResolutionOfBoardOfDirectorsMeetingHeading = fact.value

			elif fact.concept.qname.localName == 'AcquisitionsByResolutionOfBoardOfDirectorsMeetingTextBlock': #取締役会決議による取得の状況 [テキストブロック]
				self.AcquisitionsByResolutionOfBoardOfDirectorsMeetingTextBlock = fact.value

			elif fact.concept.qname.localName == 'AcquisitionsNotBasedOnResolutionOfShareholdersMeetingOrBoardOfDirectorsMeetingHeading': #株主総会決議又は取締役会決議に基づかないものの内容 [目次項目]
				self.AcquisitionsNotBasedOnResolutionOfShareholdersMeetingOrBoardOfDirectorsMeetingHeading = fact.value

			elif fact.concept.qname.localName == 'AcquisitionsNotBasedOnResolutionOfShareholdersMeetingOrBoardOfDirectorsMeetingTextBlock': #株主総会決議又は取締役会決議に基づかないものの内容 [テキストブロック]
				self.AcquisitionsNotBasedOnResolutionOfShareholdersMeetingOrBoardOfDirectorsMeetingTextBlock = fact.value

			elif fact.concept.qname.localName == 'DisposalsOrHoldingOfAcquiredTreasurySharesHeading': #取得自己株式の処理状況及び保有状況 [目次項目]
				self.DisposalsOrHoldingOfAcquiredTreasurySharesHeading = fact.value

			elif fact.concept.qname.localName == 'DisposalsOrHoldingOfAcquiredTreasurySharesTextBlock': #取得自己株式の処理状況及び保有状況 [テキストブロック]
				self.DisposalsOrHoldingOfAcquiredTreasurySharesTextBlock = fact.value

			elif fact.concept.qname.localName == 'DividendPolicyHeading': #配当政策 [目次項目]
				self.DividendPolicyHeading = fact.value

			elif fact.concept.qname.localName == 'DividendPolicyTextBlock': #配当政策 [テキストブロック]
				self.DividendPolicyTextBlock = fact.value

			elif fact.concept.qname.localName == 'DividendPolicyHeading': #配当政策 [目次項目]
				self.DividendPolicyHeading = fact.value

			elif fact.concept.qname.localName == 'DividendsOfSurplusTable': #剰余金の配当 [表]
				self.DividendsOfSurplusTable = fact.value

			elif fact.concept.qname.localName == 'SequentialNumbersAxis': #連番 [軸]
				self.SequentialNumbersAxis = fact.value

			elif fact.concept.qname.localName == 'Row1Member': #1件目 [メンバー]
				self.Row1Member = fact.value

			elif fact.concept.qname.localName == 'Row2Member': #2件目 [メンバー]
				self.Row2Member = fact.value

			elif fact.concept.qname.localName == 'Row3Member': #3件目 [メンバー]
				self.Row3Member = fact.value

			elif fact.concept.qname.localName == 'Row4Member': #4件目 [メンバー]
				self.Row4Member = fact.value

			elif fact.concept.qname.localName == 'DividendsOfSurplusLineItems': #剰余金の配当 [表示項目]
				self.DividendsOfSurplusLineItems = fact.value

			elif fact.concept.qname.localName == 'DateOfResolutionDividendsOfSurplus': #決議日付、剰余金の配当
				self.DateOfResolutionDividendsOfSurplus = fact.value

			elif fact.concept.qname.localName == 'ResolutionDividendsOfSurplus': #決議、剰余金の配当
				self.ResolutionDividendsOfSurplus = fact.value

			elif fact.concept.qname.localName == 'RecordDateDividendsOfSurplus': #基準日、剰余金の配当
				self.RecordDateDividendsOfSurplus = fact.value

			elif fact.concept.qname.localName == 'TotalAmountOfDividendsDividendsOfSurplus': #配当金の総額、剰余金の配当
				self.TotalAmountOfDividendsDividendsOfSurplus = fact.value

			elif fact.concept.qname.localName == 'DividendPerShareDividendsOfSurplus': #１株当たり配当額、剰余金の配当
				self.DividendPerShareDividendsOfSurplus = fact.value

			elif fact.concept.qname.localName == 'ExplanationAboutCorporateGovernanceEtcHeading': #コーポレート・ガバナンスの状況等 [目次項目]
				self.ExplanationAboutCorporateGovernanceEtcHeading = fact.value

			elif fact.concept.qname.localName == 'OverviewOfCorporateGovernanceHeading': #コーポレート・ガバナンスの概要 [目次項目]
				self.OverviewOfCorporateGovernanceHeading = fact.value

			elif fact.concept.qname.localName == 'OverviewOfCorporateGovernanceTextBlock': #コーポレート・ガバナンスの概要 [テキストブロック]
				self.OverviewOfCorporateGovernanceTextBlock = fact.value

			elif fact.concept.qname.localName == 'DescriptionOfFactThatCorporateGovernanceSystemChoiceFromThreeCategoriesWasChangedTextBlock': #企業統治の組織形態（３分類）の変更 [テキストブロック]
				self.DescriptionOfFactThatCorporateGovernanceSystemChoiceFromThreeCategoriesWasChangedTextBlock = fact.value

			elif fact.concept.qname.localName == 'CorporateGovernanceCompanyWithCorporateAuditorsTextBlock': #企業統治の体制の概要（監査役設置会社） [テキストブロック]
				self.CorporateGovernanceCompanyWithCorporateAuditorsTextBlock = fact.value

			elif fact.concept.qname.localName == 'CorporateGovernanceCompanyWithAuditAndSupervisoryCommitteeTextBlock': #企業統治の体制の概要（監査等委員会設置会社） [テキストブロック]
				self.CorporateGovernanceCompanyWithAuditAndSupervisoryCommitteeTextBlock = fact.value

			elif fact.concept.qname.localName == 'CorporateGovernanceCompanyWithNominatingAndOtherCommitteesTextBlock': #企業統治の体制の概要（指名委員会等設置会社） [テキストブロック]
				self.CorporateGovernanceCompanyWithNominatingAndOtherCommitteesTextBlock = fact.value

			elif fact.concept.qname.localName == 'BasicPolicyRegardingControlOfCompanyTextBlock': #会社の支配に関する基本方針 [テキストブロック]
				self.BasicPolicyRegardingControlOfCompanyTextBlock = fact.value

			elif fact.concept.qname.localName == 'InformationAboutOfficersHeading': #役員の状況 [目次項目]
				self.InformationAboutOfficersHeading = fact.value

			elif fact.concept.qname.localName == 'InformationAboutOfficersTextBlock': #役員の状況 [テキストブロック]
				self.InformationAboutOfficersTextBlock = fact.value

			elif fact.concept.qname.localName == 'InformationAboutOfficersHeading': #役員の状況 [目次項目]
				self.InformationAboutOfficersHeading = fact.value

			elif fact.concept.qname.localName == 'NumberOfMaleDirectorsAndOtherOfficers': #役員のうち男性の人数
				self.NumberOfMaleDirectorsAndOtherOfficers = fact.value

			elif fact.concept.qname.localName == 'NumberOfFemaleDirectorsAndOtherOfficers': #役員のうち女性の人数
				self.NumberOfFemaleDirectorsAndOtherOfficers = fact.value

			elif fact.concept.qname.localName == 'RatioOfFemaleDirectorsAndOtherOfficers': #役員のうち女性の比率
				self.RatioOfFemaleDirectorsAndOtherOfficers = fact.value

			elif fact.concept.qname.localName == 'InformationAboutOfficersHeading': #役員の状況 [目次項目]
				self.InformationAboutOfficersHeading = fact.value

			elif fact.concept.qname.localName == 'InformationAboutDirectorsAndCorporateAuditorsTable': #役員の状況（取締役（及び監査役）） [表]
				self.InformationAboutDirectorsAndCorporateAuditorsTable = fact.value

			elif fact.concept.qname.localName == 'DirectorsAndOtherOfficersAxis': #役員 [軸]
				self.DirectorsAndOtherOfficersAxis = fact.value

			elif fact.concept.qname.localName == 'DirectorsAndOtherOfficersMember': #役員 [メンバー] ※ディメンションデフォルト
				self.DirectorsAndOtherOfficersMember = fact.value

			elif fact.concept.qname.localName == 'InformationAboutDirectorsAndCorporateAuditorsLineItems': #役員の状況（取締役（及び監査役）） [表示項目]
				self.InformationAboutDirectorsAndCorporateAuditorsLineItems = fact.value

			elif fact.concept.qname.localName == 'OfficialTitleOrPositionInformationAboutDirectorsAndCorporateAuditors': #役職名、役員の状況（取締役（及び監査役））
				self.OfficialTitleOrPositionInformationAboutDirectorsAndCorporateAuditors = fact.value

			elif fact.concept.qname.localName == 'NameInformationAboutDirectorsAndCorporateAuditors': #氏名、役員の状況（取締役（及び監査役））
				self.NameInformationAboutDirectorsAndCorporateAuditors = fact.value

			elif fact.concept.qname.localName == 'DateOfBirthInformationAboutDirectorsAndCorporateAuditors': #生年月日、役員の状況（取締役（及び監査役））
				self.DateOfBirthInformationAboutDirectorsAndCorporateAuditors = fact.value

			elif fact.concept.qname.localName == 'CareerSummaryInformationAboutDirectorsAndCorporateAuditorsTextBlock': #略歴、役員の状況（取締役（及び監査役）） [テキストブロック]
				self.CareerSummaryInformationAboutDirectorsAndCorporateAuditorsTextBlock = fact.value

			elif fact.concept.qname.localName == 'TermOfOfficeInformationAboutDirectorsAndCorporateAuditors': #任期、役員の状況（取締役（及び監査役））
				self.TermOfOfficeInformationAboutDirectorsAndCorporateAuditors = fact.value

			elif fact.concept.qname.localName == 'NumberOfSharesHeldOrdinarySharesInformationAboutDirectorsAndCorporateAuditors': #所有株式数（普通株式）、役員の状況（取締役（及び監査役））
				self.NumberOfSharesHeldOrdinarySharesInformationAboutDirectorsAndCorporateAuditors = fact.value

			elif fact.concept.qname.localName == 'NumberOfSharesHeldOtherThanOrdinarySharesInformationAboutDirectorsAndCorporateAuditors': #所有株式数（普通株式以外）、役員の状況（取締役（及び監査役））
				self.NumberOfSharesHeldOtherThanOrdinarySharesInformationAboutDirectorsAndCorporateAuditors = fact.value

			elif fact.concept.qname.localName == 'InformationAboutOfficersHeading': #役員の状況 [目次項目]
				self.InformationAboutOfficersHeading = fact.value

			elif fact.concept.qname.localName == 'FootnotesDirectorsAndCorporateAuditorsTable': #脚注（取締役（及び監査役）） [表]
				self.FootnotesDirectorsAndCorporateAuditorsTable = fact.value

			elif fact.concept.qname.localName == 'SequentialNumbersAxis': #連番 [軸]
				self.SequentialNumbersAxis = fact.value

			elif fact.concept.qname.localName == 'Row1Member': #1件目 [メンバー]
				self.Row1Member = fact.value

			elif fact.concept.qname.localName == 'Row2Member': #2件目 [メンバー]
				self.Row2Member = fact.value

			elif fact.concept.qname.localName == 'Row3Member': #3件目 [メンバー]
				self.Row3Member = fact.value

			elif fact.concept.qname.localName == 'Row4Member': #4件目 [メンバー]
				self.Row4Member = fact.value

			elif fact.concept.qname.localName == 'Row5Member': #5件目 [メンバー]
				self.Row5Member = fact.value

			elif fact.concept.qname.localName == 'FootnotesDirectorsAndCorporateAuditorsLineItems': #脚注（取締役（及び監査役）） [表示項目]
				self.FootnotesDirectorsAndCorporateAuditorsLineItems = fact.value

			elif fact.concept.qname.localName == 'FootnotesDirectorsAndCorporateAuditorsTextBlock': #脚注（取締役（及び監査役） [テキストブロック]
				self.FootnotesDirectorsAndCorporateAuditorsTextBlock = fact.value

			elif fact.concept.qname.localName == 'InformationAboutOfficersHeading': #役員の状況 [目次項目]
				self.InformationAboutOfficersHeading = fact.value

			elif fact.concept.qname.localName == 'InformationAboutExecutiveDirectorsTable': #役員の状況（執行役） [表]
				self.InformationAboutExecutiveDirectorsTable = fact.value

			elif fact.concept.qname.localName == 'DirectorsAndOtherOfficersAxis': #役員 [軸]
				self.DirectorsAndOtherOfficersAxis = fact.value

			elif fact.concept.qname.localName == 'DirectorsAndOtherOfficersMember': #役員 [メンバー] ※ディメンションデフォルト
				self.DirectorsAndOtherOfficersMember = fact.value

			elif fact.concept.qname.localName == 'InformationAboutExecutiveDirectorsLineItems': #役員の状況（執行役） [表示項目]
				self.InformationAboutExecutiveDirectorsLineItems = fact.value

			elif fact.concept.qname.localName == 'OfficialTitleOrPositionInformationAboutExecutiveDirectors': #役職名、役員の状況（執行役）
				self.OfficialTitleOrPositionInformationAboutExecutiveDirectors = fact.value

			elif fact.concept.qname.localName == 'NameInformationAboutExecutiveDirectors': #氏名、役員の状況（執行役）
				self.NameInformationAboutExecutiveDirectors = fact.value

			elif fact.concept.qname.localName == 'DateOfBirthInformationAboutExecutiveDirectors': #生年月日、役員の状況（執行役）
				self.DateOfBirthInformationAboutExecutiveDirectors = fact.value

			elif fact.concept.qname.localName == 'CareerSummaryInformationAboutExecutiveDirectorsTextBlock': #略歴、役員の状況（執行役） [テキストブロック]
				self.CareerSummaryInformationAboutExecutiveDirectorsTextBlock = fact.value

			elif fact.concept.qname.localName == 'TermOfOfficeInformationAboutExecutiveDirectors': #任期、役員の状況（執行役）
				self.TermOfOfficeInformationAboutExecutiveDirectors = fact.value

			elif fact.concept.qname.localName == 'NumberOfSharesHeldOrdinarySharesInformationAboutExecutiveDirectors': #所有株式数（普通株式）、役員の状況（執行役）
				self.NumberOfSharesHeldOrdinarySharesInformationAboutExecutiveDirectors = fact.value

			elif fact.concept.qname.localName == 'NumberOfSharesHeldOtherThanOrdinarySharesInformationAboutExecutiveDirectors': #所有株式数（普通株式以外）、役員の状況（執行役）
				self.NumberOfSharesHeldOtherThanOrdinarySharesInformationAboutExecutiveDirectors = fact.value

			elif fact.concept.qname.localName == 'InformationAboutOfficersHeading': #役員の状況 [目次項目]
				self.InformationAboutOfficersHeading = fact.value

			elif fact.concept.qname.localName == 'FootnotesExecutiveOfficersTable': #脚注（執行役） [表]
				self.FootnotesExecutiveOfficersTable = fact.value

			elif fact.concept.qname.localName == 'SequentialNumbersAxis': #連番 [軸]
				self.SequentialNumbersAxis = fact.value

			elif fact.concept.qname.localName == 'Row1Member': #1件目 [メンバー]
				self.Row1Member = fact.value

			elif fact.concept.qname.localName == 'Row2Member': #2件目 [メンバー]
				self.Row2Member = fact.value

			elif fact.concept.qname.localName == 'Row3Member': #3件目 [メンバー]
				self.Row3Member = fact.value

			elif fact.concept.qname.localName == 'Row4Member': #4件目 [メンバー]
				self.Row4Member = fact.value

			elif fact.concept.qname.localName == 'Row5Member': #5件目 [メンバー]
				self.Row5Member = fact.value

			elif fact.concept.qname.localName == 'FootnotesExecutiveOfficersLineItems': #脚注（執行役） [表示項目]
				self.FootnotesExecutiveOfficersLineItems = fact.value

			elif fact.concept.qname.localName == 'FootnotesExecutiveOfficersTextBlock': #脚注（執行役） [テキストブロック]
				self.FootnotesExecutiveOfficersTextBlock = fact.value

			elif fact.concept.qname.localName == 'InformationAboutOfficersHeading': #役員の状況 [目次項目]
				self.InformationAboutOfficersHeading = fact.value

			elif fact.concept.qname.localName == 'NumberOfMaleDirectorsAndOtherOfficersProposal': #役員のうち男性の人数（議案）
				self.NumberOfMaleDirectorsAndOtherOfficersProposal = fact.value

			elif fact.concept.qname.localName == 'NumberOfFemaleDirectorsAndOtherOfficersProposal': #役員のうち女性の人数（議案）
				self.NumberOfFemaleDirectorsAndOtherOfficersProposal = fact.value

			elif fact.concept.qname.localName == 'RatioOfFemaleDirectorsAndOtherOfficersProposal': #役員のうち女性の比率（議案）
				self.RatioOfFemaleDirectorsAndOtherOfficersProposal = fact.value

			elif fact.concept.qname.localName == 'InformationAboutOfficersHeading': #役員の状況 [目次項目]
				self.InformationAboutOfficersHeading = fact.value

			elif fact.concept.qname.localName == 'InformationAboutDirectorsAndCorporateAuditorsProposalTable': #役員の状況（取締役（及び監査役））（議案） [表]
				self.InformationAboutDirectorsAndCorporateAuditorsProposalTable = fact.value

			elif fact.concept.qname.localName == 'DirectorsAndOtherOfficersAxis': #役員 [軸]
				self.DirectorsAndOtherOfficersAxis = fact.value

			elif fact.concept.qname.localName == 'DirectorsAndOtherOfficersMember': #役員 [メンバー] ※ディメンションデフォルト
				self.DirectorsAndOtherOfficersMember = fact.value

			elif fact.concept.qname.localName == 'InformationAboutDirectorsAndCorporateAuditorsProposalLineItems': #役員の状況（取締役（及び監査役））（議案） [表示項目]
				self.InformationAboutDirectorsAndCorporateAuditorsProposalLineItems = fact.value

			elif fact.concept.qname.localName == 'OfficialTitleOrPositionInformationAboutDirectorsAndCorporateAuditorsProposal': #役職名、役員の状況（取締役（及び監査役））（議案）
				self.OfficialTitleOrPositionInformationAboutDirectorsAndCorporateAuditorsProposal = fact.value

			elif fact.concept.qname.localName == 'NameInformationAboutDirectorsAndCorporateAuditorsProposal': #氏名、役員の状況（取締役（及び監査役））（議案）
				self.NameInformationAboutDirectorsAndCorporateAuditorsProposal = fact.value

			elif fact.concept.qname.localName == 'DateOfBirthInformationAboutDirectorsAndCorporateAuditorsProposal': #生年月日、役員の状況（取締役（及び監査役））（議案）
				self.DateOfBirthInformationAboutDirectorsAndCorporateAuditorsProposal = fact.value

			elif fact.concept.qname.localName == 'CareerSummaryInformationAboutDirectorsAndCorporateAuditorsProposalTextBlock': #略歴、役員の状況（取締役（及び監査役））（議案） [テキストブロック]
				self.CareerSummaryInformationAboutDirectorsAndCorporateAuditorsProposalTextBlock = fact.value

			elif fact.concept.qname.localName == 'TermOfOfficeInformationAboutDirectorsAndCorporateAuditorsProposal': #任期、役員の状況（取締役（及び監査役））（議案）
				self.TermOfOfficeInformationAboutDirectorsAndCorporateAuditorsProposal = fact.value

			elif fact.concept.qname.localName == 'NumberOfSharesHeldOrdinarySharesInformationAboutDirectorsAndCorporateAuditorsProposal': #所有株式数（普通株式）、役員の状況（取締役（及び監査役））（議案）
				self.NumberOfSharesHeldOrdinarySharesInformationAboutDirectorsAndCorporateAuditorsProposal = fact.value

			elif fact.concept.qname.localName == 'NumberOfSharesHeldOtherThanOrdinarySharesInformationAboutDirectorsAndCorporateAuditorsProposal': #所有株式数（普通株式以外）、役員の状況（取締役（及び監査役））（議案）
				self.NumberOfSharesHeldOtherThanOrdinarySharesInformationAboutDirectorsAndCorporateAuditorsProposal = fact.value

			elif fact.concept.qname.localName == 'InformationAboutOfficersHeading': #役員の状況 [目次項目]
				self.InformationAboutOfficersHeading = fact.value

			elif fact.concept.qname.localName == 'FootnotesDirectorsAndCorporateAuditorsProposalTable': #脚注（取締役（及び監査役））（議案） [表]
				self.FootnotesDirectorsAndCorporateAuditorsProposalTable = fact.value

			elif fact.concept.qname.localName == 'SequentialNumbersAxis': #連番 [軸]
				self.SequentialNumbersAxis = fact.value

			elif fact.concept.qname.localName == 'Row1Member': #1件目 [メンバー]
				self.Row1Member = fact.value

			elif fact.concept.qname.localName == 'Row2Member': #2件目 [メンバー]
				self.Row2Member = fact.value

			elif fact.concept.qname.localName == 'Row3Member': #3件目 [メンバー]
				self.Row3Member = fact.value

			elif fact.concept.qname.localName == 'Row4Member': #4件目 [メンバー]
				self.Row4Member = fact.value

			elif fact.concept.qname.localName == 'Row5Member': #5件目 [メンバー]
				self.Row5Member = fact.value

			elif fact.concept.qname.localName == 'FootnotesDirectorsAndCorporateAuditorsProposalLineItems': #脚注（取締役（及び監査役））（議案） [表示項目]
				self.FootnotesDirectorsAndCorporateAuditorsProposalLineItems = fact.value

			elif fact.concept.qname.localName == 'FootnotesDirectorsAndCorporateAuditorsProposalTextBlock': #脚注（取締役（及び監査役））（議案） [テキストブロック]
				self.FootnotesDirectorsAndCorporateAuditorsProposalTextBlock = fact.value

			elif fact.concept.qname.localName == 'InformationAboutOfficersHeading': #役員の状況 [目次項目]
				self.InformationAboutOfficersHeading = fact.value

			elif fact.concept.qname.localName == 'InformationAboutExecutiveDirectorsProposalTable': #役員の状況（執行役）（議案） [表]
				self.InformationAboutExecutiveDirectorsProposalTable = fact.value

			elif fact.concept.qname.localName == 'DirectorsAndOtherOfficersAxis': #役員 [軸]
				self.DirectorsAndOtherOfficersAxis = fact.value

			elif fact.concept.qname.localName == 'DirectorsAndOtherOfficersMember': #役員 [メンバー] ※ディメンションデフォルト
				self.DirectorsAndOtherOfficersMember = fact.value

			elif fact.concept.qname.localName == 'InformationAboutExecutiveDirectorsProposalLineItems': #役員の状況（執行役）（議案） [表示項目]
				self.InformationAboutExecutiveDirectorsProposalLineItems = fact.value

			elif fact.concept.qname.localName == 'OfficialTitleOrPositionInformationAboutExecutiveDirectorsProposal': #役職名、役員の状況（執行役）（議案）
				self.OfficialTitleOrPositionInformationAboutExecutiveDirectorsProposal = fact.value

			elif fact.concept.qname.localName == 'NameInformationAboutExecutiveDirectorsProposal': #氏名、役員の状況（執行役）（議案）
				self.NameInformationAboutExecutiveDirectorsProposal = fact.value

			elif fact.concept.qname.localName == 'DateOfBirthInformationAboutExecutiveDirectorsProposal': #生年月日、役員の状況（執行役）（議案）
				self.DateOfBirthInformationAboutExecutiveDirectorsProposal = fact.value

			elif fact.concept.qname.localName == 'CareerSummaryInformationAboutExecutiveDirectorsProposalTextBlock': #略歴、役員の状況（執行役）（議案） [テキストブロック]
				self.CareerSummaryInformationAboutExecutiveDirectorsProposalTextBlock = fact.value

			elif fact.concept.qname.localName == 'TermOfOfficeInformationAboutExecutiveDirectorsProposal': #任期、役員の状況（執行役）（議案）
				self.TermOfOfficeInformationAboutExecutiveDirectorsProposal = fact.value

			elif fact.concept.qname.localName == 'NumberOfSharesHeldOrdinarySharesInformationAboutExecutiveDirectorsProposal': #所有株式数（普通株式）、役員の状況（執行役）（議案）
				self.NumberOfSharesHeldOrdinarySharesInformationAboutExecutiveDirectorsProposal = fact.value

			elif fact.concept.qname.localName == 'NumberOfSharesHeldOtherThanOrdinarySharesInformationAboutExecutiveDirectorsProposal': #所有株式数（普通株式以外）、役員の状況（執行役）（議案）
				self.NumberOfSharesHeldOtherThanOrdinarySharesInformationAboutExecutiveDirectorsProposal = fact.value

			elif fact.concept.qname.localName == 'InformationAboutOfficersHeading': #役員の状況 [目次項目]
				self.InformationAboutOfficersHeading = fact.value

			elif fact.concept.qname.localName == 'FootnotesExecutiveOfficersProposalTable': #脚注（執行役）（議案） [表]
				self.FootnotesExecutiveOfficersProposalTable = fact.value

			elif fact.concept.qname.localName == 'SequentialNumbersAxis': #連番 [軸]
				self.SequentialNumbersAxis = fact.value

			elif fact.concept.qname.localName == 'Row1Member': #1件目 [メンバー]
				self.Row1Member = fact.value

			elif fact.concept.qname.localName == 'Row2Member': #2件目 [メンバー]
				self.Row2Member = fact.value

			elif fact.concept.qname.localName == 'Row3Member': #3件目 [メンバー]
				self.Row3Member = fact.value

			elif fact.concept.qname.localName == 'Row4Member': #4件目 [メンバー]
				self.Row4Member = fact.value

			elif fact.concept.qname.localName == 'Row5Member': #5件目 [メンバー]
				self.Row5Member = fact.value

			elif fact.concept.qname.localName == 'FootnotesExecutiveOfficersProposalLineItems': #脚注（執行役）（議案） [表示項目]
				self.FootnotesExecutiveOfficersProposalLineItems = fact.value

			elif fact.concept.qname.localName == 'FootnotesExecutiveOfficersProposalTextBlock': #脚注（執行役）（議案） [テキストブロック]
				self.FootnotesExecutiveOfficersProposalTextBlock = fact.value

			elif fact.concept.qname.localName == 'OutsideDirectorsAndOutsideCorporateAuditorsTextBlock': #社外取締役（及び社外監査役） [テキストブロック]
				self.OutsideDirectorsAndOutsideCorporateAuditorsTextBlock = fact.value

			elif fact.concept.qname.localName == 'AuditsHeading': #監査の状況 [目次項目]
				self.AuditsHeading = fact.value

			elif fact.concept.qname.localName == 'AuditsTextBlock': #監査の状況 [テキストブロック]
				self.AuditsTextBlock = fact.value

			elif fact.concept.qname.localName == 'AuditsHeading': #監査の状況 [目次項目]
				self.AuditsHeading = fact.value

			elif fact.concept.qname.localName == 'NoteOnChangeOfIndependentAuditorsAuditsTextBlock': #監査公認会計士等の異動について、監査の状況 [テキストブロック]
				self.NoteOnChangeOfIndependentAuditorsAuditsTextBlock = fact.value

			elif fact.concept.qname.localName == 'FeesToPrimaryAuditorAbstract': #監査公認会計士等に対する報酬の内容 [タイトル項目]
				self.FeesToPrimaryAuditorAbstract = fact.value

			elif fact.concept.qname.localName == 'AuditFeesReportingCompany': #監査証明業務に基づく報酬－提出会社、監査公認会計士等
				self.AuditFeesReportingCompany = fact.value

			elif fact.concept.qname.localName == 'NonAuditFeesReportingCompany': #非監査業務に基づく報酬－提出会社、監査公認会計士等
				self.NonAuditFeesReportingCompany = fact.value

			elif fact.concept.qname.localName == 'AuditFeesConsolidatedSubsidiaries': #監査証明業務に基づく報酬－連結子会社、監査公認会計士等
				self.AuditFeesConsolidatedSubsidiaries = fact.value

			elif fact.concept.qname.localName == 'NonAuditFeesConsolidatedSubsidiaries': #非監査業務に基づく報酬－連結子会社、監査公認会計士等
				self.NonAuditFeesConsolidatedSubsidiaries = fact.value

			elif fact.concept.qname.localName == 'AuditFeesTotal': #監査証明業務に基づく報酬－計、監査公認会計士等
				self.AuditFeesTotal = fact.value

			elif fact.concept.qname.localName == 'NonAuditFeesTotal': #非監査業務に基づく報酬－計、監査公認会計士等
				self.NonAuditFeesTotal = fact.value

			elif fact.concept.qname.localName == 'FeesToNetworkFirmsAbstract': #ネットワークファームに対する報酬の内容 [タイトル項目]
				self.FeesToNetworkFirmsAbstract = fact.value

			elif fact.concept.qname.localName == 'AuditFeesReportingCompanyNetworkFirms': #監査証明業務に基づく報酬－提出会社、ネットワークファーム
				self.AuditFeesReportingCompanyNetworkFirms = fact.value

			elif fact.concept.qname.localName == 'NonAuditFeesReportingCompanyNetworkFirms': #非監査業務に基づく報酬－提出会社、ネットワークファーム
				self.NonAuditFeesReportingCompanyNetworkFirms = fact.value

			elif fact.concept.qname.localName == 'AuditFeesConsolidatedSubsidiariesNetworkFirms': #監査証明業務に基づく報酬－連結子会社、ネットワークファーム
				self.AuditFeesConsolidatedSubsidiariesNetworkFirms = fact.value

			elif fact.concept.qname.localName == 'NonAuditFeesConsolidatedSubsidiariesNetworkFirms': #非監査業務に基づく報酬－連結子会社、ネットワークファーム
				self.NonAuditFeesConsolidatedSubsidiariesNetworkFirms = fact.value

			elif fact.concept.qname.localName == 'AuditFeesTotalNetworkFirms': #監査証明業務に基づく報酬－計、ネットワークファーム
				self.AuditFeesTotalNetworkFirms = fact.value

			elif fact.concept.qname.localName == 'NonAuditFeesTotalNetworkFirms': #非監査業務に基づく報酬－計、ネットワークファーム
				self.NonAuditFeesTotalNetworkFirms = fact.value

			elif fact.concept.qname.localName == 'RemunerationForDirectorsAndOtherOfficersHeading': #役員の報酬等 [目次項目]
				self.RemunerationForDirectorsAndOtherOfficersHeading = fact.value

			elif fact.concept.qname.localName == 'RemunerationForDirectorsAndOtherOfficersTextBlock': #役員の報酬等 [テキストブロック]
				self.RemunerationForDirectorsAndOtherOfficersTextBlock = fact.value

			elif fact.concept.qname.localName == 'RemunerationForDirectorsAndOtherOfficersHeading': #役員の報酬等 [目次項目]
				self.RemunerationForDirectorsAndOtherOfficersHeading = fact.value

			elif fact.concept.qname.localName == 'RemunerationEtcByCategoryOfDirectorsAndOtherOfficersAbstract': #役員区分ごとの報酬等 [タイトル項目]
				self.RemunerationEtcByCategoryOfDirectorsAndOtherOfficersAbstract = fact.value

			elif fact.concept.qname.localName == 'RemunerationEtcByCategoryOfDirectorsAndOtherOfficersTable': #役員区分ごとの報酬等 [表]
				self.RemunerationEtcByCategoryOfDirectorsAndOtherOfficersTable = fact.value

			elif fact.concept.qname.localName == 'CategoriesOfDirectorsAndOtherOfficersAxis': #役員区分 [軸]
				self.CategoriesOfDirectorsAndOtherOfficersAxis = fact.value

			elif fact.concept.qname.localName == 'DirectorsExcludingOutsideDirectorsMember': #取締役（社外取締役を除く） [メンバー]
				self.DirectorsExcludingOutsideDirectorsMember = fact.value

			elif fact.concept.qname.localName == 'DirectorsExcludingAuditAndSupervisoryCommitteeMembersAndOutsideDirectorsMember': #取締役（監査等委員及び社外取締役を除く） [メンバー]
				self.DirectorsExcludingAuditAndSupervisoryCommitteeMembersAndOutsideDirectorsMember = fact.value

			elif fact.concept.qname.localName == 'DirectorsAppointedAsAuditAndSupervisoryCommitteeMembersExcludingOutsideDirectorsMember': #監査等委員（社外取締役を除く） [メンバー]
				self.DirectorsAppointedAsAuditAndSupervisoryCommitteeMembersExcludingOutsideDirectorsMember = fact.value

			elif fact.concept.qname.localName == 'CorporateAuditorsExcludingOutsideCorporateAuditorsMember': #監査役（社外監査役を除く） [メンバー]
				self.CorporateAuditorsExcludingOutsideCorporateAuditorsMember = fact.value

			elif fact.concept.qname.localName == 'ExecutiveOfficersMember': #執行役 [メンバー]
				self.ExecutiveOfficersMember = fact.value

			elif fact.concept.qname.localName == 'OutsideDirectorsAndOtherOfficersMember': #社外役員 [メンバー]
				self.OutsideDirectorsAndOtherOfficersMember = fact.value

			elif fact.concept.qname.localName == 'OutsideDirectorsMember': #社外取締役 [メンバー]
				self.OutsideDirectorsMember = fact.value

			elif fact.concept.qname.localName == 'OutsideCorporateAuditorsMember': #社外監査役 [メンバー]
				self.OutsideCorporateAuditorsMember = fact.value

			elif fact.concept.qname.localName == 'RemunerationEtcByCategoryOfDirectorsAndOtherOfficersLineItems': #役員区分ごとの報酬等 [表示項目]
				self.RemunerationEtcByCategoryOfDirectorsAndOtherOfficersLineItems = fact.value

			elif fact.concept.qname.localName == 'TotalAmountOfRemunerationEtcRemunerationEtcByCategoryOfDirectorsAndOtherOfficers': #報酬等の総額、役員区分ごとの報酬等
				self.TotalAmountOfRemunerationEtcRemunerationEtcByCategoryOfDirectorsAndOtherOfficers = fact.value

			elif fact.concept.qname.localName == 'TotalAmountByTypeOfRemunerationRemunerationEtcByCategoryOfDirectorsAndOtherOfficersAbstract': #報酬等の種類別の総額、役員区分ごとの報酬等 [タイトル項目]
				self.TotalAmountByTypeOfRemunerationRemunerationEtcByCategoryOfDirectorsAndOtherOfficersAbstract = fact.value

			elif fact.concept.qname.localName == 'FixedRemunerationRemunerationByCategoryOfDirectorsAndOtherOfficers': #固定報酬、役員区分ごとの報酬等
				self.FixedRemunerationRemunerationByCategoryOfDirectorsAndOtherOfficers = fact.value

			elif fact.concept.qname.localName == 'PerformanceBasedRemunerationRemunerationByCategoryOfDirectorsAndOtherOfficers': #業績連動報酬、役員区分ごとの報酬等
				self.PerformanceBasedRemunerationRemunerationByCategoryOfDirectorsAndOtherOfficers = fact.value

			elif fact.concept.qname.localName == 'BaseRemunerationRemunerationEtcByCategoryOfDirectorsAndOtherOfficers': #基本報酬、役員区分ごとの報酬等
				self.BaseRemunerationRemunerationEtcByCategoryOfDirectorsAndOtherOfficers = fact.value

			elif fact.concept.qname.localName == 'ShareAwardsRemunerationEtcByCategoryOfDirectorsAndOtherOfficers': #株式報酬、役員区分ごとの報酬等
				self.ShareAwardsRemunerationEtcByCategoryOfDirectorsAndOtherOfficers = fact.value

			elif fact.concept.qname.localName == 'RestrictedShareAwardsRemunerationEtcByCategoryOfDirectorsAndOtherOfficers': #譲渡制限付株式報酬、役員区分ごとの報酬等
				self.RestrictedShareAwardsRemunerationEtcByCategoryOfDirectorsAndOtherOfficers = fact.value

			elif fact.concept.qname.localName == 'PerformanceLinkedShareAwardsRemunerationEtcByCategoryOfDirectorsAndOtherOfficers': #業績連動型株式報酬、役員区分ごとの報酬等
				self.PerformanceLinkedShareAwardsRemunerationEtcByCategoryOfDirectorsAndOtherOfficers = fact.value

			elif fact.concept.qname.localName == 'ShareOptionRemunerationEtcByCategoryOfDirectorsAndOtherOfficers': #ストックオプション、役員区分ごとの報酬等
				self.ShareOptionRemunerationEtcByCategoryOfDirectorsAndOtherOfficers = fact.value

			elif fact.concept.qname.localName == 'BonusRemunerationEtcByCategoryOfDirectorsAndOtherOfficers': #賞与、役員区分ごとの報酬等
				self.BonusRemunerationEtcByCategoryOfDirectorsAndOtherOfficers = fact.value

			elif fact.concept.qname.localName == 'RetirementBenefitsRemunerationEtcByCategoryOfDirectorsAndOtherOfficers': #退職慰労金、役員区分ごとの報酬等
				self.RetirementBenefitsRemunerationEtcByCategoryOfDirectorsAndOtherOfficers = fact.value

			elif fact.concept.qname.localName == 'NonMonetaryRemunerationRemunerationByCategoryOfDirectorsAndOtherOfficers': #非金銭報酬等、役員区分ごとの報酬等
				self.NonMonetaryRemunerationRemunerationByCategoryOfDirectorsAndOtherOfficers = fact.value

			elif fact.concept.qname.localName == 'OtherRemunerationEtcByCategoryOfDirectorsAndOtherOfficers': #その他、役員区分ごとの報酬等
				self.OtherRemunerationEtcByCategoryOfDirectorsAndOtherOfficers = fact.value

			elif fact.concept.qname.localName == 'NumberOfDirectorsAndOtherOfficersRemunerationEtcByCategoryOfDirectorsAndOtherOfficers': #対象となる役員の員数、役員区分ごとの報酬等
				self.NumberOfDirectorsAndOtherOfficersRemunerationEtcByCategoryOfDirectorsAndOtherOfficers = fact.value

			elif fact.concept.qname.localName == 'RemunerationEtcPaidByGroupToEachDirectorOrOtherOfficerTextBlock': #役員ごとの連結報酬等 [テキストブロック]
				self.RemunerationEtcPaidByGroupToEachDirectorOrOtherOfficerTextBlock = fact.value

			elif fact.concept.qname.localName == 'RemunerationForDirectorsAndOtherOfficersHeading': #役員の報酬等 [目次項目]
				self.RemunerationForDirectorsAndOtherOfficersHeading = fact.value

			elif fact.concept.qname.localName == 'RemunerationEtcPaidByGroupToEachDirectorOrOtherOfficerAbstract': #役員ごとの連結報酬等 [タイトル項目]
				self.RemunerationEtcPaidByGroupToEachDirectorOrOtherOfficerAbstract = fact.value

			elif fact.concept.qname.localName == 'RemunerationEtcPaidByGroupToEachDirectorOrOtherOfficerTable': #役員ごとの連結報酬等 [表]
				self.RemunerationEtcPaidByGroupToEachDirectorOrOtherOfficerTable = fact.value

			elif fact.concept.qname.localName == 'DirectorsAndOtherOfficersAxis': #役員 [軸]
				self.DirectorsAndOtherOfficersAxis = fact.value

			elif fact.concept.qname.localName == 'DirectorsAndOtherOfficersMember': #役員 [メンバー] ※ディメンションデフォルト
				self.DirectorsAndOtherOfficersMember = fact.value

			elif fact.concept.qname.localName == 'RemunerationEtcPaidByGroupToEachDirectorOrOtherOfficerLineItems': #役員ごとの連結報酬等 [表示項目]
				self.RemunerationEtcPaidByGroupToEachDirectorOrOtherOfficerLineItems = fact.value

			elif fact.concept.qname.localName == 'TotalAmountOfRemunerationEtcPaidByGroupRemunerationEtcPaidByGroupToEachDirectorOrOtherOfficer': #連結報酬等の総額、役員ごとの連結報酬等
				self.TotalAmountOfRemunerationEtcPaidByGroupRemunerationEtcPaidByGroupToEachDirectorOrOtherOfficer = fact.value

			elif fact.concept.qname.localName == 'ShareholdingsHeading': #株式の保有状況 [目次項目]
				self.ShareholdingsHeading = fact.value

			elif fact.concept.qname.localName == 'ShareholdingsTextBlock': #株式の保有状況 [テキストブロック]
				self.ShareholdingsTextBlock = fact.value

			elif fact.concept.qname.localName == 'ShareholdingsHeading': #株式の保有状況 [目次項目]
				self.ShareholdingsHeading = fact.value

			elif fact.concept.qname.localName == 'ReportingCompanyEquitySecuritiesHeldAbstract': #提出会社、株式の保有状況 [タイトル項目]
				self.ReportingCompanyEquitySecuritiesHeldAbstract = fact.value

			elif fact.concept.qname.localName == 'InvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentReportingCompanyAbstract': #保有目的が純投資目的以外の目的である投資株式、提出会社 [タイトル項目]
				self.InvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentReportingCompanyAbstract = fact.value

			elif fact.concept.qname.localName == 'SharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompanyAbstract': #非上場株式、保有目的が純投資目的以外の目的である投資株式、提出会社 [タイトル項目]
				self.SharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompanyAbstract = fact.value

			elif fact.concept.qname.localName == 'NumberOfIssuesSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany': #銘柄数、非上場株式、保有目的が純投資目的以外の目的である投資株式、提出会社
				self.NumberOfIssuesSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany = fact.value

			elif fact.concept.qname.localName == 'CarryingAmountSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany': #貸借対照表計上額、非上場株式、保有目的が純投資目的以外の目的である投資株式、提出会社
				self.CarryingAmountSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany = fact.value

			elif fact.concept.qname.localName == 'NumberOfIssuesWhoseNumberOfSharesIncreasedSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany': #株式数が増加した銘柄数、非上場株式、保有目的が純投資目的以外の目的である投資株式、提出会社
				self.NumberOfIssuesWhoseNumberOfSharesIncreasedSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany = fact.value

			elif fact.concept.qname.localName == 'TotalAcquisitionCostForIncreasedSharesSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany': #株式数の増加に係る取得価額の合計額、非上場株式、保有目的が純投資目的以外の目的である投資株式、提出会社
				self.TotalAcquisitionCostForIncreasedSharesSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany = fact.value

			elif fact.concept.qname.localName == 'ReasonForIncreaseInNumberOfSharesSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany': #株式数が増加した理由、非上場株式、保有目的が純投資目的以外の目的である投資株式、提出会社
				self.ReasonForIncreaseInNumberOfSharesSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany = fact.value

			elif fact.concept.qname.localName == 'NumberOfIssuesWhoseNumberOfSharesDecreasedSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany': #株式数が減少した銘柄数、非上場株式、保有目的が純投資目的以外の目的である投資株式、提出会社
				self.NumberOfIssuesWhoseNumberOfSharesDecreasedSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany = fact.value

			elif fact.concept.qname.localName == 'TotalSaleAmountForDecreasedSharesSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany': #株式数の減少に係る売却価額の合計額、非上場株式、保有目的が純投資目的以外の目的である投資株式、提出会社
				self.TotalSaleAmountForDecreasedSharesSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany = fact.value

			elif fact.concept.qname.localName == 'SharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompanyAbstract': #非上場株式以外の株式、保有目的が純投資目的以外の目的である投資株式、提出会社 [タイトル項目]
				self.SharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompanyAbstract = fact.value

			elif fact.concept.qname.localName == 'NumberOfIssuesSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany': #銘柄数、非上場株式以外の株式、保有目的が純投資目的以外の目的である投資株式、提出会社
				self.NumberOfIssuesSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany = fact.value

			elif fact.concept.qname.localName == 'CarryingAmountSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany': #貸借対照表計上額、非上場株式以外の株式、保有目的が純投資目的以外の目的である投資株式、提出会社
				self.CarryingAmountSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany = fact.value

			elif fact.concept.qname.localName == 'NumberOfIssuesWhoseNumberOfSharesIncreasedSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany': #株式数が増加した銘柄数、非上場株式以外の株式、保有目的が純投資目的以外の目的である投資株式、提出会社
				self.NumberOfIssuesWhoseNumberOfSharesIncreasedSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany = fact.value

			elif fact.concept.qname.localName == 'TotalAcquisitionCostForIncreasedSharesSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany': #株式数の増加に係る取得価額の合計額、非上場株式以外の株式、保有目的が純投資目的以外の目的である投資株式、提出会社
				self.TotalAcquisitionCostForIncreasedSharesSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany = fact.value

			elif fact.concept.qname.localName == 'ReasonForIncreaseInNumberOfSharesSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany': #株式数が増加した理由、非上場株式以外の株式、保有目的が純投資目的以外の目的である投資株式、提出会社
				self.ReasonForIncreaseInNumberOfSharesSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany = fact.value

			elif fact.concept.qname.localName == 'NumberOfIssuesWhoseNumberOfSharesDecreasedSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany': #株式数が減少した銘柄数、非上場株式以外の株式、保有目的が純投資目的以外の目的である投資株式、提出会社
				self.NumberOfIssuesWhoseNumberOfSharesDecreasedSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany = fact.value

			elif fact.concept.qname.localName == 'TotalSaleAmountForDecreasedSharesSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany': #株式数の減少に係る売却価額の合計額、非上場株式以外の株式、保有目的が純投資目的以外の目的である投資株式、提出会社
				self.TotalSaleAmountForDecreasedSharesSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany = fact.value

			elif fact.concept.qname.localName == 'ShareholdingsHeading': #株式の保有状況 [目次項目]
				self.ShareholdingsHeading = fact.value

			elif fact.concept.qname.localName == 'ReportingCompanyEquitySecuritiesHeldAbstract': #提出会社、株式の保有状況 [タイトル項目]
				self.ReportingCompanyEquitySecuritiesHeldAbstract = fact.value

			elif fact.concept.qname.localName == 'DetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentReportingCompanyTable': #保有目的が純投資目的以外の目的である特定投資株式の明細、提出会社 [表]
				self.DetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentReportingCompanyTable = fact.value

			elif fact.concept.qname.localName == 'SequentialNumbersAxis': #連番 [軸]
				self.SequentialNumbersAxis = fact.value

			elif fact.concept.qname.localName == 'Row1Member': #1件目 [メンバー]
				self.Row1Member = fact.value

			elif fact.concept.qname.localName == 'Row2Member': #2件目 [メンバー]
				self.Row2Member = fact.value

			elif fact.concept.qname.localName == 'Row3Member': #3件目 [メンバー]
				self.Row3Member = fact.value

			elif fact.concept.qname.localName == 'Row4Member': #4件目 [メンバー]
				self.Row4Member = fact.value

			elif fact.concept.qname.localName == 'Row5Member': #5件目 [メンバー]
				self.Row5Member = fact.value

			elif fact.concept.qname.localName == 'Row6Member': #6件目 [メンバー]
				self.Row6Member = fact.value

			elif fact.concept.qname.localName == 'Row7Member': #7件目 [メンバー]
				self.Row7Member = fact.value

			elif fact.concept.qname.localName == 'Row8Member': #8件目 [メンバー]
				self.Row8Member = fact.value

			elif fact.concept.qname.localName == 'Row9Member': #9件目 [メンバー]
				self.Row9Member = fact.value

			elif fact.concept.qname.localName == 'Row10Member': #10件目 [メンバー]
				self.Row10Member = fact.value

			elif fact.concept.qname.localName == 'Row11Member': #11件目 [メンバー]
				self.Row11Member = fact.value

			elif fact.concept.qname.localName == 'Row12Member': #12件目 [メンバー]
				self.Row12Member = fact.value

			elif fact.concept.qname.localName == 'Row13Member': #13件目 [メンバー]
				self.Row13Member = fact.value

			elif fact.concept.qname.localName == 'Row14Member': #14件目 [メンバー]
				self.Row14Member = fact.value

			elif fact.concept.qname.localName == 'Row15Member': #15件目 [メンバー]
				self.Row15Member = fact.value

			elif fact.concept.qname.localName == 'Row16Member': #16件目 [メンバー]
				self.Row16Member = fact.value

			elif fact.concept.qname.localName == 'Row17Member': #17件目 [メンバー]
				self.Row17Member = fact.value

			elif fact.concept.qname.localName == 'Row18Member': #18件目 [メンバー]
				self.Row18Member = fact.value

			elif fact.concept.qname.localName == 'Row19Member': #19件目 [メンバー]
				self.Row19Member = fact.value

			elif fact.concept.qname.localName == 'Row20Member': #20件目 [メンバー]
				self.Row20Member = fact.value

			elif fact.concept.qname.localName == 'Row21Member': #21件目 [メンバー]
				self.Row21Member = fact.value

			elif fact.concept.qname.localName == 'Row22Member': #22件目 [メンバー]
				self.Row22Member = fact.value

			elif fact.concept.qname.localName == 'Row23Member': #23件目 [メンバー]
				self.Row23Member = fact.value

			elif fact.concept.qname.localName == 'Row24Member': #24件目 [メンバー]
				self.Row24Member = fact.value

			elif fact.concept.qname.localName == 'Row25Member': #25件目 [メンバー]
				self.Row25Member = fact.value

			elif fact.concept.qname.localName == 'Row26Member': #26件目 [メンバー]
				self.Row26Member = fact.value

			elif fact.concept.qname.localName == 'Row27Member': #27件目 [メンバー]
				self.Row27Member = fact.value

			elif fact.concept.qname.localName == 'Row28Member': #28件目 [メンバー]
				self.Row28Member = fact.value

			elif fact.concept.qname.localName == 'Row29Member': #29件目 [メンバー]
				self.Row29Member = fact.value

			elif fact.concept.qname.localName == 'Row30Member': #30件目 [メンバー]
				self.Row30Member = fact.value

			elif fact.concept.qname.localName == 'Row31Member': #31件目 [メンバー]
				self.Row31Member = fact.value

			elif fact.concept.qname.localName == 'Row32Member': #32件目 [メンバー]
				self.Row32Member = fact.value

			elif fact.concept.qname.localName == 'Row33Member': #33件目 [メンバー]
				self.Row33Member = fact.value

			elif fact.concept.qname.localName == 'Row34Member': #34件目 [メンバー]
				self.Row34Member = fact.value

			elif fact.concept.qname.localName == 'Row35Member': #35件目 [メンバー]
				self.Row35Member = fact.value

			elif fact.concept.qname.localName == 'Row36Member': #36件目 [メンバー]
				self.Row36Member = fact.value

			elif fact.concept.qname.localName == 'Row37Member': #37件目 [メンバー]
				self.Row37Member = fact.value

			elif fact.concept.qname.localName == 'Row38Member': #38件目 [メンバー]
				self.Row38Member = fact.value

			elif fact.concept.qname.localName == 'Row39Member': #39件目 [メンバー]
				self.Row39Member = fact.value

			elif fact.concept.qname.localName == 'Row40Member': #40件目 [メンバー]
				self.Row40Member = fact.value

			elif fact.concept.qname.localName == 'Row41Member': #41件目 [メンバー]
				self.Row41Member = fact.value

			elif fact.concept.qname.localName == 'Row42Member': #42件目 [メンバー]
				self.Row42Member = fact.value

			elif fact.concept.qname.localName == 'Row43Member': #43件目 [メンバー]
				self.Row43Member = fact.value

			elif fact.concept.qname.localName == 'Row44Member': #44件目 [メンバー]
				self.Row44Member = fact.value

			elif fact.concept.qname.localName == 'Row45Member': #45件目 [メンバー]
				self.Row45Member = fact.value

			elif fact.concept.qname.localName == 'Row46Member': #46件目 [メンバー]
				self.Row46Member = fact.value

			elif fact.concept.qname.localName == 'Row47Member': #47件目 [メンバー]
				self.Row47Member = fact.value

			elif fact.concept.qname.localName == 'Row48Member': #48件目 [メンバー]
				self.Row48Member = fact.value

			elif fact.concept.qname.localName == 'Row49Member': #49件目 [メンバー]
				self.Row49Member = fact.value

			elif fact.concept.qname.localName == 'Row50Member': #50件目 [メンバー]
				self.Row50Member = fact.value

			elif fact.concept.qname.localName == 'Row51Member': #51件目 [メンバー]
				self.Row51Member = fact.value

			elif fact.concept.qname.localName == 'Row52Member': #52件目 [メンバー]
				self.Row52Member = fact.value

			elif fact.concept.qname.localName == 'Row53Member': #53件目 [メンバー]
				self.Row53Member = fact.value

			elif fact.concept.qname.localName == 'Row54Member': #54件目 [メンバー]
				self.Row54Member = fact.value

			elif fact.concept.qname.localName == 'Row55Member': #55件目 [メンバー]
				self.Row55Member = fact.value

			elif fact.concept.qname.localName == 'Row56Member': #56件目 [メンバー]
				self.Row56Member = fact.value

			elif fact.concept.qname.localName == 'Row57Member': #57件目 [メンバー]
				self.Row57Member = fact.value

			elif fact.concept.qname.localName == 'Row58Member': #58件目 [メンバー]
				self.Row58Member = fact.value

			elif fact.concept.qname.localName == 'Row59Member': #59件目 [メンバー]
				self.Row59Member = fact.value

			elif fact.concept.qname.localName == 'Row60Member': #60件目 [メンバー]
				self.Row60Member = fact.value

			elif fact.concept.qname.localName == 'DetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentReportingCompanyLineItems': #保有目的が純投資目的以外の目的である特定投資株式の明細、提出会社 [表示項目]
				self.DetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentReportingCompanyLineItems = fact.value

			elif fact.concept.qname.localName == 'NameOfSecuritiesDetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentReportingCompany': #銘柄、保有目的が純投資目的以外の目的である特定投資株式の明細、提出会社
				self.NameOfSecuritiesDetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentReportingCompany = fact.value

			elif fact.concept.qname.localName == 'NumberOfSharesHeldDetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentReportingCompany': #株式数、保有目的が純投資目的以外の目的である特定投資株式の明細、提出会社
				self.NumberOfSharesHeldDetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentReportingCompany = fact.value

			elif fact.concept.qname.localName == 'NumberOfSharesNotDisclosedAsBelowThresholdDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany': #株式数（記載省略）、保有目的が純投資目的以外の目的である特定投資株式の明細、提出会社
				self.NumberOfSharesNotDisclosedAsBelowThresholdDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany = fact.value

			elif fact.concept.qname.localName == 'BookValueDetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentReportingCompany': #貸借対照表計上額、保有目的が純投資目的以外の目的である特定投資株式の明細、提出会社
				self.BookValueDetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentReportingCompany = fact.value

			elif fact.concept.qname.localName == 'CarryingAmountNotDisclosedAsBelowThresholdDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany': #貸借対照表計上額（記載省略）、保有目的が純投資目的以外の目的である特定投資株式の明細、提出会社
				self.CarryingAmountNotDisclosedAsBelowThresholdDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany = fact.value

			elif fact.concept.qname.localName == 'PurposesOfHoldingDetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentReportingCompany': #保有目的、保有目的が純投資目的以外の目的である特定投資株式の明細、提出会社
				self.PurposesOfHoldingDetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentReportingCompany = fact.value

			elif fact.concept.qname.localName == 'QuantitativeEffectsOfShareholdingDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany': #定量的な保有効果、保有目的が純投資目的以外の目的である特定投資株式の明細、提出会社
				self.QuantitativeEffectsOfShareholdingDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany = fact.value

			elif fact.concept.qname.localName == 'ReasonForIncreaseInNumberOfSharesDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany': #株式数が増加した理由、保有目的が純投資目的以外の目的である特定投資株式の明細、提出会社
				self.ReasonForIncreaseInNumberOfSharesDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany = fact.value

			elif fact.concept.qname.localName == 'PurposeOfShareholdingQuantitativeEffectsOfShareholdingAndReasonForIncreaseInNumberOfSharesDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany': #保有目的、定量的な保有効果及び株式数が増加した理由、保有目的が純投資目的以外の目的である特定投資株式の明細、提出会社
				self.PurposeOfShareholdingQuantitativeEffectsOfShareholdingAndReasonForIncreaseInNumberOfSharesDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany = fact.value

			elif fact.concept.qname.localName == 'WhetherIssuerOfAforementionedSharesHoldsReportingCompanysSharesDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany': #当該株式の発行者による提出会社の株式の保有の有無、保有目的が純投資目的以外の目的である特定投資株式の明細、提出会社
				self.WhetherIssuerOfAforementionedSharesHoldsReportingCompanysSharesDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany = fact.value

			elif fact.concept.qname.localName == 'ShareholdingsHeading': #株式の保有状況 [目次項目]
				self.ShareholdingsHeading = fact.value

			elif fact.concept.qname.localName == 'ReportingCompanyEquitySecuritiesHeldAbstract': #提出会社、株式の保有状況 [タイトル項目]
				self.ReportingCompanyEquitySecuritiesHeldAbstract = fact.value

			elif fact.concept.qname.localName == 'DetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentReportingCompanyTable': #保有目的が純投資目的以外の目的であるみなし保有株式の明細、提出会社 [表]
				self.DetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentReportingCompanyTable = fact.value

			elif fact.concept.qname.localName == 'SequentialNumbersAxis': #連番 [軸]
				self.SequentialNumbersAxis = fact.value

			elif fact.concept.qname.localName == 'Row1Member': #1件目 [メンバー]
				self.Row1Member = fact.value

			elif fact.concept.qname.localName == 'Row2Member': #2件目 [メンバー]
				self.Row2Member = fact.value

			elif fact.concept.qname.localName == 'Row3Member': #3件目 [メンバー]
				self.Row3Member = fact.value

			elif fact.concept.qname.localName == 'Row4Member': #4件目 [メンバー]
				self.Row4Member = fact.value

			elif fact.concept.qname.localName == 'Row5Member': #5件目 [メンバー]
				self.Row5Member = fact.value

			elif fact.concept.qname.localName == 'Row6Member': #6件目 [メンバー]
				self.Row6Member = fact.value

			elif fact.concept.qname.localName == 'Row7Member': #7件目 [メンバー]
				self.Row7Member = fact.value

			elif fact.concept.qname.localName == 'Row8Member': #8件目 [メンバー]
				self.Row8Member = fact.value

			elif fact.concept.qname.localName == 'Row9Member': #9件目 [メンバー]
				self.Row9Member = fact.value

			elif fact.concept.qname.localName == 'Row10Member': #10件目 [メンバー]
				self.Row10Member = fact.value

			elif fact.concept.qname.localName == 'DetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentReportingCompanyLineItems': #保有目的が純投資目的以外の目的であるみなし保有株式の明細、提出会社 [表示項目]
				self.DetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentReportingCompanyLineItems = fact.value

			elif fact.concept.qname.localName == 'NameOfSecuritiesDetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentReportingCompany': #銘柄、保有目的が純投資目的以外の目的であるみなし保有株式の明細、提出会社
				self.NameOfSecuritiesDetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentReportingCompany = fact.value

			elif fact.concept.qname.localName == 'NumberOfSharesHeldDetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentReportingCompany': #株式数、保有目的が純投資目的以外の目的であるみなし保有株式の明細、提出会社
				self.NumberOfSharesHeldDetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentReportingCompany = fact.value

			elif fact.concept.qname.localName == 'NumberOfSharesNotDisclosedAsBelowThresholdDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentReportingCompany': #株式数（記載省略）、保有目的が純投資目的以外の目的であるみなし保有株式の明細、提出会社
				self.NumberOfSharesNotDisclosedAsBelowThresholdDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentReportingCompany = fact.value

			elif fact.concept.qname.localName == 'BookValueDetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentReportingCompany': #貸借対照表計上額、保有目的が純投資目的以外の目的であるみなし保有株式の明細、提出会社
				self.BookValueDetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentReportingCompany = fact.value

			elif fact.concept.qname.localName == 'CarryingAmountNotDisclosedAsBelowThresholdDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentReportingCompany': #貸借対照表計上額（記載省略）、保有目的が純投資目的以外の目的であるみなし保有株式の明細、提出会社
				self.CarryingAmountNotDisclosedAsBelowThresholdDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentReportingCompany = fact.value

			elif fact.concept.qname.localName == 'PurposesOfHoldingDetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentReportingCompany': #保有目的、保有目的が純投資目的以外の目的であるみなし保有株式の明細、提出会社
				self.PurposesOfHoldingDetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentReportingCompany = fact.value

			elif fact.concept.qname.localName == 'QuantitativeEffectsOfShareholdingDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentReportingCompany': #定量的な保有効果、保有目的が純投資目的以外の目的であるみなし保有株式の明細、提出会社
				self.QuantitativeEffectsOfShareholdingDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentReportingCompany = fact.value

			elif fact.concept.qname.localName == 'ReasonForIncreaseInNumberOfSharesDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentReportingCompany': #株式数が増加した理由、保有目的が純投資目的以外の目的であるみなし保有株式の明細、提出会社
				self.ReasonForIncreaseInNumberOfSharesDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentReportingCompany = fact.value

			elif fact.concept.qname.localName == 'PurposeOfShareholdingQuantitativeEffectsOfShareholdingAndReasonForIncreaseInNumberOfSharesDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentReportingCompany': #保有目的、定量的な保有効果及び株式数が増加した理由、保有目的が純投資目的以外の目的であるみなし保有株式の明細、提出会社
				self.PurposeOfShareholdingQuantitativeEffectsOfShareholdingAndReasonForIncreaseInNumberOfSharesDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentReportingCompany = fact.value

			elif fact.concept.qname.localName == 'WhetherIssuerOfAforementionedSharesHoldsReportingCompanysSharesDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentReportingCompany': #当該株式の発行者による提出会社の株式の保有の有無、保有目的が純投資目的以外の目的であるみなし保有株式の明細、提出会社
				self.WhetherIssuerOfAforementionedSharesHoldsReportingCompanysSharesDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentReportingCompany = fact.value

			elif fact.concept.qname.localName == 'ShareholdingsHeading': #株式の保有状況 [目次項目]
				self.ShareholdingsHeading = fact.value

			elif fact.concept.qname.localName == 'ReportingCompanyEquitySecuritiesHeldAbstract': #提出会社、株式の保有状況 [タイトル項目]
				self.ReportingCompanyEquitySecuritiesHeldAbstract = fact.value

			elif fact.concept.qname.localName == 'InvestmentEquitySecuritiesHeldForPureInvestmentReportingCompanyAbstract': #保有目的が純投資目的である投資株式、提出会社 [タイトル項目]
				self.InvestmentEquitySecuritiesHeldForPureInvestmentReportingCompanyAbstract = fact.value

			elif fact.concept.qname.localName == 'EquitySecuritiesNotListedInvestmentEquitySecuritiesHeldForPureInvestmentReportingCompanyAbstract': #非上場株式、保有目的が純投資目的である投資株式、提出会社 [タイトル項目]
				self.EquitySecuritiesNotListedInvestmentEquitySecuritiesHeldForPureInvestmentReportingCompanyAbstract = fact.value

			elif fact.concept.qname.localName == 'NumberOfIssuesSharesNotListedInvestmentSharesHeldForPureInvestmentReportingCompany': #銘柄数、非上場株式、保有目的が純投資目的である投資株式、提出会社
				self.NumberOfIssuesSharesNotListedInvestmentSharesHeldForPureInvestmentReportingCompany = fact.value

			elif fact.concept.qname.localName == 'BookValueEquitySecuritiesNotListedInvestmentEquitySecuritiesHeldForPureInvestmentReportingCompany': #貸借対照表計上額の合計額、非上場株式、保有目的が純投資目的である投資株式、提出会社
				self.BookValueEquitySecuritiesNotListedInvestmentEquitySecuritiesHeldForPureInvestmentReportingCompany = fact.value

			elif fact.concept.qname.localName == 'TotalOfDividendsReceivedEquitySecuritiesNotListedInvestmentEquitySecuritiesHeldForPureInvestmentReportingCompany': #受取配当金の合計額、非上場株式、保有目的が純投資目的である投資株式、提出会社
				self.TotalOfDividendsReceivedEquitySecuritiesNotListedInvestmentEquitySecuritiesHeldForPureInvestmentReportingCompany = fact.value

			elif fact.concept.qname.localName == 'TotalOfGainLossOnSaleEquitySecuritiesNotListedInvestmentEquitySecuritiesHeldForPureInvestmentReportingCompany': #売却損益の合計額、非上場株式、保有目的が純投資目的である投資株式、提出会社
				self.TotalOfGainLossOnSaleEquitySecuritiesNotListedInvestmentEquitySecuritiesHeldForPureInvestmentReportingCompany = fact.value

			elif fact.concept.qname.localName == 'TotalOfValuationGainLossEquitySecuritiesNotListedInvestmentEquitySecuritiesHeldForPureInvestmentReportingCompany': #評価損益の合計額、非上場株式、保有目的が純投資目的である投資株式、提出会社
				self.TotalOfValuationGainLossEquitySecuritiesNotListedInvestmentEquitySecuritiesHeldForPureInvestmentReportingCompany = fact.value

			elif fact.concept.qname.localName == 'EquitySecuritiesOtherThanThoseNotListedInvestmentEquitySecuritiesHeldForPureInvestmentReportingCompanyAbstract': #非上場株式以外の株式、保有目的が純投資目的である投資株式、提出会社 [タイトル項目]
				self.EquitySecuritiesOtherThanThoseNotListedInvestmentEquitySecuritiesHeldForPureInvestmentReportingCompanyAbstract = fact.value

			elif fact.concept.qname.localName == 'NumberOfIssuesSharesOtherThanThoseNotListedInvestmentSharesHeldForPureInvestmentReportingCompany': #銘柄数、非上場株式以外の株式、保有目的が純投資目的である投資株式、提出会社
				self.NumberOfIssuesSharesOtherThanThoseNotListedInvestmentSharesHeldForPureInvestmentReportingCompany = fact.value

			elif fact.concept.qname.localName == 'BookValueEquitySecuritiesOtherThanThoseNotListedInvestmentEquitySecuritiesHeldForPureInvestmentReportingCompany': #貸借対照表計上額の合計額、非上場株式以外の株式、保有目的が純投資目的である投資株式、提出会社
				self.BookValueEquitySecuritiesOtherThanThoseNotListedInvestmentEquitySecuritiesHeldForPureInvestmentReportingCompany = fact.value

			elif fact.concept.qname.localName == 'TotalOfDividendsReceivedEquitySecuritiesOtherThanThoseNotListedInvestmentEquitySecuritiesHeldForPureInvestmentReportingCompany': #受取配当金の合計額、非上場株式以外の株式、保有目的が純投資目的である投資株式、提出会社
				self.TotalOfDividendsReceivedEquitySecuritiesOtherThanThoseNotListedInvestmentEquitySecuritiesHeldForPureInvestmentReportingCompany = fact.value

			elif fact.concept.qname.localName == 'TotalOfGainLossOnSaleEquitySecuritiesOtherThanThoseNotListedInvestmentEquitySecuritiesHeldForPureInvestmentReportingCompany': #売却損益の合計額、非上場株式以外の株式、保有目的が純投資目的である投資株式、提出会社
				self.TotalOfGainLossOnSaleEquitySecuritiesOtherThanThoseNotListedInvestmentEquitySecuritiesHeldForPureInvestmentReportingCompany = fact.value

			elif fact.concept.qname.localName == 'TotalOfValuationGainLossEquitySecuritiesOtherThanThoseNotListedInvestmentEquitySecuritiesHeldForPureInvestmentReportingCompany': #評価損益の合計額、非上場株式以外の株式、保有目的が純投資目的である投資株式、提出会社
				self.TotalOfValuationGainLossEquitySecuritiesOtherThanThoseNotListedInvestmentEquitySecuritiesHeldForPureInvestmentReportingCompany = fact.value

			elif fact.concept.qname.localName == 'ShareholdingsHeading': #株式の保有状況 [目次項目]
				self.ShareholdingsHeading = fact.value

			elif fact.concept.qname.localName == 'ReportingCompanyEquitySecuritiesHeldAbstract': #提出会社、株式の保有状況 [タイトル項目]
				self.ReportingCompanyEquitySecuritiesHeldAbstract = fact.value

			elif fact.concept.qname.localName == 'InvestmentEquitySecuritiesReclassifiedFromHeldForPureInvestmentToHeldForPurposesOtherThanPureInvestmentReportingCompanyTable': #投資株式の保有目的を純投資目的から純投資目的以外の目的に変更したもの、提出会社 [表]
				self.InvestmentEquitySecuritiesReclassifiedFromHeldForPureInvestmentToHeldForPurposesOtherThanPureInvestmentReportingCompanyTable = fact.value

			elif fact.concept.qname.localName == 'SequentialNumbersAxis': #連番 [軸]
				self.SequentialNumbersAxis = fact.value

			elif fact.concept.qname.localName == 'Row1Member': #1件目 [メンバー]
				self.Row1Member = fact.value

			elif fact.concept.qname.localName == 'Row2Member': #2件目 [メンバー]
				self.Row2Member = fact.value

			elif fact.concept.qname.localName == 'Row3Member': #3件目 [メンバー]
				self.Row3Member = fact.value

			elif fact.concept.qname.localName == 'InvestmentEquitySecuritiesReclassifiedFromHeldForPureInvestmentToHeldForPurposesOtherThanPureInvestmentReportingCompanyLineItems': #投資株式の保有目的を純投資目的から純投資目的以外の目的に変更したもの、提出会社 [表示項目]
				self.InvestmentEquitySecuritiesReclassifiedFromHeldForPureInvestmentToHeldForPurposesOtherThanPureInvestmentReportingCompanyLineItems = fact.value

			elif fact.concept.qname.localName == 'SecurityNameInvestmentEquitySecuritiesReclassifiedFromHeldForPureInvestmentToHeldForPurposesOtherThanPureInvestmentReportingCompany': #銘柄、投資株式の保有目的を純投資目的から純投資目的以外の目的に変更したもの、提出会社
				self.SecurityNameInvestmentEquitySecuritiesReclassifiedFromHeldForPureInvestmentToHeldForPurposesOtherThanPureInvestmentReportingCompany = fact.value

			elif fact.concept.qname.localName == 'NumberOfSharesHeldInvestmentEquitySecuritiesReclassifiedFromHeldForPureInvestmentToHeldForPurposesOtherThanPureInvestmentReportingCompany': #株式数、投資株式の保有目的を純投資目的から純投資目的以外の目的に変更したもの、提出会社
				self.NumberOfSharesHeldInvestmentEquitySecuritiesReclassifiedFromHeldForPureInvestmentToHeldForPurposesOtherThanPureInvestmentReportingCompany = fact.value

			elif fact.concept.qname.localName == 'BookValueInvestmentEquitySecuritiesReclassifiedFromHeldForPureInvestmentToHeldForPurposesOtherThanPureInvestmentReportingCompany': #貸借対照表計上額、投資株式の保有目的を純投資目的から純投資目的以外の目的に変更したもの、提出会社
				self.BookValueInvestmentEquitySecuritiesReclassifiedFromHeldForPureInvestmentToHeldForPurposesOtherThanPureInvestmentReportingCompany = fact.value

			elif fact.concept.qname.localName == 'ShareholdingsHeading': #株式の保有状況 [目次項目]
				self.ShareholdingsHeading = fact.value

			elif fact.concept.qname.localName == 'ReportingCompanyEquitySecuritiesHeldAbstract': #提出会社、株式の保有状況 [タイトル項目]
				self.ReportingCompanyEquitySecuritiesHeldAbstract = fact.value

			elif fact.concept.qname.localName == 'InvestmentEquitySecuritiesReclassifiedFromHeldForPurposesOtherThanPureInvestmentToHeldForPureInvestmentReportingCompanyTable': #投資株式の保有目的を純投資以外の目的から純投資目的に変更したもの、提出会社 [表]
				self.InvestmentEquitySecuritiesReclassifiedFromHeldForPurposesOtherThanPureInvestmentToHeldForPureInvestmentReportingCompanyTable = fact.value

			elif fact.concept.qname.localName == 'SequentialNumbersAxis': #連番 [軸]
				self.SequentialNumbersAxis = fact.value

			elif fact.concept.qname.localName == 'Row1Member': #1件目 [メンバー]
				self.Row1Member = fact.value

			elif fact.concept.qname.localName == 'Row2Member': #2件目 [メンバー]
				self.Row2Member = fact.value

			elif fact.concept.qname.localName == 'Row3Member': #3件目 [メンバー]
				self.Row3Member = fact.value

			elif fact.concept.qname.localName == 'InvestmentEquitySecuritiesReclassifiedFromHeldForPurposesOtherThanPureInvestmentToHeldForPureInvestmentReportingCompanyLineItems': #投資株式の保有目的を純投資以外の目的から純投資目的に変更したもの、提出会社 [表示項目]
				self.InvestmentEquitySecuritiesReclassifiedFromHeldForPurposesOtherThanPureInvestmentToHeldForPureInvestmentReportingCompanyLineItems = fact.value

			elif fact.concept.qname.localName == 'NameOfSecuritiesInvestmentEquitySecuritiesReclassifiedFromHeldForPurposesOtherThanPureInvestmentToHeldForPureInvestmentReportingCompany': #銘柄、投資株式の保有目的を純投資以外の目的から純投資目的に変更したもの、提出会社
				self.NameOfSecuritiesInvestmentEquitySecuritiesReclassifiedFromHeldForPurposesOtherThanPureInvestmentToHeldForPureInvestmentReportingCompany = fact.value

			elif fact.concept.qname.localName == 'NumberOfSharesHeldInvestmentEquitySecuritiesReclassifiedFromHeldForPurposesOtherThanPureInvestmentToHeldForPureInvestmentReportingCompany': #株式数、投資株式の保有目的を純投資以外の目的から純投資目的に変更したもの、提出会社
				self.NumberOfSharesHeldInvestmentEquitySecuritiesReclassifiedFromHeldForPurposesOtherThanPureInvestmentToHeldForPureInvestmentReportingCompany = fact.value

			elif fact.concept.qname.localName == 'BookValueInvestmentEquitySecuritiesReclassifiedFromHeldForPurposesOtherThanPureInvestmentToHeldForPureInvestmentReportingCompany': #貸借対照表計上額、投資株式の保有目的を純投資以外の目的から純投資目的に変更したもの、提出会社
				self.BookValueInvestmentEquitySecuritiesReclassifiedFromHeldForPurposesOtherThanPureInvestmentToHeldForPureInvestmentReportingCompany = fact.value

			elif fact.concept.qname.localName == 'ShareholdingsHeading': #株式の保有状況 [目次項目]
				self.ShareholdingsHeading = fact.value

			elif fact.concept.qname.localName == 'GroupCompanyHoldingLargestAmountOfInvestmentEquitySecuritiesInGroupEquitySecuritiesHeldAbstract': #最大保有会社（提出会社でない場合）、株式の保有状況 [タイトル項目]
				self.GroupCompanyHoldingLargestAmountOfInvestmentEquitySecuritiesInGroupEquitySecuritiesHeldAbstract = fact.value

			elif fact.concept.qname.localName == 'InvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompanyAbstract': #保有目的が純投資目的以外の目的である投資株式、最大保有会社 [タイトル項目]
				self.InvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompanyAbstract = fact.value

			elif fact.concept.qname.localName == 'SharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompanyAbstract': #非上場株式、保有目的が純投資目的以外の目的である投資株式、最大保有会社 [タイトル項目]
				self.SharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompanyAbstract = fact.value

			elif fact.concept.qname.localName == 'NumberOfIssuesSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany': #銘柄数、非上場株式、保有目的が純投資目的以外の目的である投資株式、最大保有会社
				self.NumberOfIssuesSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'CarryingAmountSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany': #貸借対照表計上額、非上場株式、保有目的が純投資目的以外の目的である投資株式、最大保有会社
				self.CarryingAmountSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'NumberOfIssuesWhoseNumberOfSharesIncreasedSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany': #株式数が増加した銘柄数、非上場株式、保有目的が純投資目的以外の目的である投資株式、最大保有会社
				self.NumberOfIssuesWhoseNumberOfSharesIncreasedSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'TotalAcquisitionCostForIncreasedSharesSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany': #株式数の増加に係る取得価額の合計額、非上場株式、保有目的が純投資目的以外の目的である投資株式、最大保有会社
				self.TotalAcquisitionCostForIncreasedSharesSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'ReasonForIncreaseInNumberOfSharesSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany': #株式数が増加した理由、非上場株式、保有目的が純投資目的以外の目的である投資株式、最大保有会社
				self.ReasonForIncreaseInNumberOfSharesSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'NumberOfIssuesWhoseNumberOfSharesDecreasedSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany': #株式数が減少した銘柄数、非上場株式、保有目的が純投資目的以外の目的である投資株式、最大保有会社
				self.NumberOfIssuesWhoseNumberOfSharesDecreasedSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'TotalSaleAmountForDecreasedSharesSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany': #株式数の減少に係る売却価額の合計額、非上場株式、保有目的が純投資目的以外の目的である投資株式、最大保有会社
				self.TotalSaleAmountForDecreasedSharesSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'SharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompanyAbstract': #非上場株式以外の株式、保有目的が純投資目的以外の目的である投資株式、最大保有会社 [タイトル項目]
				self.SharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompanyAbstract = fact.value

			elif fact.concept.qname.localName == 'NumberOfIssuesSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany': #銘柄数、非上場株式以外の株式、保有目的が純投資目的以外の目的である投資株式、最大保有会社
				self.NumberOfIssuesSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'CarryingAmountSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany': #貸借対照表計上額、非上場株式以外の株式、保有目的が純投資目的以外の目的である投資株式、最大保有会社
				self.CarryingAmountSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'NumberOfIssuesWhoseNumberOfSharesIncreasedSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany': #株式数が増加した銘柄数、非上場株式以外の株式、保有目的が純投資目的以外の目的である投資株式、最大保有会社
				self.NumberOfIssuesWhoseNumberOfSharesIncreasedSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'TotalAcquisitionCostForIncreasedSharesSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany': #株式数の増加に係る取得価額の合計額、非上場株式以外の株式、保有目的が純投資目的以外の目的である投資株式、最大保有会社
				self.TotalAcquisitionCostForIncreasedSharesSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'ReasonForIncreaseInNumberOfSharesSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany': #株式数が増加した理由、非上場株式以外の株式、保有目的が純投資目的以外の目的である投資株式、最大保有会社
				self.ReasonForIncreaseInNumberOfSharesSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'NumberOfIssuesWhoseNumberOfSharesDecreasedSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany': #株式数が減少した銘柄数、非上場株式以外の株式、保有目的が純投資目的以外の目的である投資株式、最大保有会社
				self.NumberOfIssuesWhoseNumberOfSharesDecreasedSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'TotalSaleAmountForDecreasedSharesSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany': #株式数の減少に係る売却価額の合計額、非上場株式以外の株式、保有目的が純投資目的以外の目的である投資株式、最大保有会社
				self.TotalSaleAmountForDecreasedSharesSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'ShareholdingsHeading': #株式の保有状況 [目次項目]
				self.ShareholdingsHeading = fact.value

			elif fact.concept.qname.localName == 'GroupCompanyHoldingLargestAmountOfInvestmentEquitySecuritiesInGroupEquitySecuritiesHeldAbstract': #最大保有会社（提出会社でない場合）、株式の保有状況 [タイトル項目]
				self.GroupCompanyHoldingLargestAmountOfInvestmentEquitySecuritiesInGroupEquitySecuritiesHeldAbstract = fact.value

			elif fact.concept.qname.localName == 'DetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompanyTable': #保有目的が純投資目的以外の目的である特定投資株式の明細、最大保有会社 [表]
				self.DetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompanyTable = fact.value

			elif fact.concept.qname.localName == 'SequentialNumbersAxis': #連番 [軸]
				self.SequentialNumbersAxis = fact.value

			elif fact.concept.qname.localName == 'Row1Member': #1件目 [メンバー]
				self.Row1Member = fact.value

			elif fact.concept.qname.localName == 'Row2Member': #2件目 [メンバー]
				self.Row2Member = fact.value

			elif fact.concept.qname.localName == 'Row3Member': #3件目 [メンバー]
				self.Row3Member = fact.value

			elif fact.concept.qname.localName == 'Row4Member': #4件目 [メンバー]
				self.Row4Member = fact.value

			elif fact.concept.qname.localName == 'Row5Member': #5件目 [メンバー]
				self.Row5Member = fact.value

			elif fact.concept.qname.localName == 'Row6Member': #6件目 [メンバー]
				self.Row6Member = fact.value

			elif fact.concept.qname.localName == 'Row7Member': #7件目 [メンバー]
				self.Row7Member = fact.value

			elif fact.concept.qname.localName == 'Row8Member': #8件目 [メンバー]
				self.Row8Member = fact.value

			elif fact.concept.qname.localName == 'Row9Member': #9件目 [メンバー]
				self.Row9Member = fact.value

			elif fact.concept.qname.localName == 'Row10Member': #10件目 [メンバー]
				self.Row10Member = fact.value

			elif fact.concept.qname.localName == 'Row11Member': #11件目 [メンバー]
				self.Row11Member = fact.value

			elif fact.concept.qname.localName == 'Row12Member': #12件目 [メンバー]
				self.Row12Member = fact.value

			elif fact.concept.qname.localName == 'Row13Member': #13件目 [メンバー]
				self.Row13Member = fact.value

			elif fact.concept.qname.localName == 'Row14Member': #14件目 [メンバー]
				self.Row14Member = fact.value

			elif fact.concept.qname.localName == 'Row15Member': #15件目 [メンバー]
				self.Row15Member = fact.value

			elif fact.concept.qname.localName == 'Row16Member': #16件目 [メンバー]
				self.Row16Member = fact.value

			elif fact.concept.qname.localName == 'Row17Member': #17件目 [メンバー]
				self.Row17Member = fact.value

			elif fact.concept.qname.localName == 'Row18Member': #18件目 [メンバー]
				self.Row18Member = fact.value

			elif fact.concept.qname.localName == 'Row19Member': #19件目 [メンバー]
				self.Row19Member = fact.value

			elif fact.concept.qname.localName == 'Row20Member': #20件目 [メンバー]
				self.Row20Member = fact.value

			elif fact.concept.qname.localName == 'Row21Member': #21件目 [メンバー]
				self.Row21Member = fact.value

			elif fact.concept.qname.localName == 'Row22Member': #22件目 [メンバー]
				self.Row22Member = fact.value

			elif fact.concept.qname.localName == 'Row23Member': #23件目 [メンバー]
				self.Row23Member = fact.value

			elif fact.concept.qname.localName == 'Row24Member': #24件目 [メンバー]
				self.Row24Member = fact.value

			elif fact.concept.qname.localName == 'Row25Member': #25件目 [メンバー]
				self.Row25Member = fact.value

			elif fact.concept.qname.localName == 'Row26Member': #26件目 [メンバー]
				self.Row26Member = fact.value

			elif fact.concept.qname.localName == 'Row27Member': #27件目 [メンバー]
				self.Row27Member = fact.value

			elif fact.concept.qname.localName == 'Row28Member': #28件目 [メンバー]
				self.Row28Member = fact.value

			elif fact.concept.qname.localName == 'Row29Member': #29件目 [メンバー]
				self.Row29Member = fact.value

			elif fact.concept.qname.localName == 'Row30Member': #30件目 [メンバー]
				self.Row30Member = fact.value

			elif fact.concept.qname.localName == 'Row31Member': #31件目 [メンバー]
				self.Row31Member = fact.value

			elif fact.concept.qname.localName == 'Row32Member': #32件目 [メンバー]
				self.Row32Member = fact.value

			elif fact.concept.qname.localName == 'Row33Member': #33件目 [メンバー]
				self.Row33Member = fact.value

			elif fact.concept.qname.localName == 'Row34Member': #34件目 [メンバー]
				self.Row34Member = fact.value

			elif fact.concept.qname.localName == 'Row35Member': #35件目 [メンバー]
				self.Row35Member = fact.value

			elif fact.concept.qname.localName == 'Row36Member': #36件目 [メンバー]
				self.Row36Member = fact.value

			elif fact.concept.qname.localName == 'Row37Member': #37件目 [メンバー]
				self.Row37Member = fact.value

			elif fact.concept.qname.localName == 'Row38Member': #38件目 [メンバー]
				self.Row38Member = fact.value

			elif fact.concept.qname.localName == 'Row39Member': #39件目 [メンバー]
				self.Row39Member = fact.value

			elif fact.concept.qname.localName == 'Row40Member': #40件目 [メンバー]
				self.Row40Member = fact.value

			elif fact.concept.qname.localName == 'Row41Member': #41件目 [メンバー]
				self.Row41Member = fact.value

			elif fact.concept.qname.localName == 'Row42Member': #42件目 [メンバー]
				self.Row42Member = fact.value

			elif fact.concept.qname.localName == 'Row43Member': #43件目 [メンバー]
				self.Row43Member = fact.value

			elif fact.concept.qname.localName == 'Row44Member': #44件目 [メンバー]
				self.Row44Member = fact.value

			elif fact.concept.qname.localName == 'Row45Member': #45件目 [メンバー]
				self.Row45Member = fact.value

			elif fact.concept.qname.localName == 'Row46Member': #46件目 [メンバー]
				self.Row46Member = fact.value

			elif fact.concept.qname.localName == 'Row47Member': #47件目 [メンバー]
				self.Row47Member = fact.value

			elif fact.concept.qname.localName == 'Row48Member': #48件目 [メンバー]
				self.Row48Member = fact.value

			elif fact.concept.qname.localName == 'Row49Member': #49件目 [メンバー]
				self.Row49Member = fact.value

			elif fact.concept.qname.localName == 'Row50Member': #50件目 [メンバー]
				self.Row50Member = fact.value

			elif fact.concept.qname.localName == 'Row51Member': #51件目 [メンバー]
				self.Row51Member = fact.value

			elif fact.concept.qname.localName == 'Row52Member': #52件目 [メンバー]
				self.Row52Member = fact.value

			elif fact.concept.qname.localName == 'Row53Member': #53件目 [メンバー]
				self.Row53Member = fact.value

			elif fact.concept.qname.localName == 'Row54Member': #54件目 [メンバー]
				self.Row54Member = fact.value

			elif fact.concept.qname.localName == 'Row55Member': #55件目 [メンバー]
				self.Row55Member = fact.value

			elif fact.concept.qname.localName == 'Row56Member': #56件目 [メンバー]
				self.Row56Member = fact.value

			elif fact.concept.qname.localName == 'Row57Member': #57件目 [メンバー]
				self.Row57Member = fact.value

			elif fact.concept.qname.localName == 'Row58Member': #58件目 [メンバー]
				self.Row58Member = fact.value

			elif fact.concept.qname.localName == 'Row59Member': #59件目 [メンバー]
				self.Row59Member = fact.value

			elif fact.concept.qname.localName == 'Row60Member': #60件目 [メンバー]
				self.Row60Member = fact.value

			elif fact.concept.qname.localName == 'DetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompanyLineItems': #保有目的が純投資目的以外の目的である特定投資株式の明細、最大保有会社 [表示項目]
				self.DetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompanyLineItems = fact.value

			elif fact.concept.qname.localName == 'NameOfSecuritiesDetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany': #銘柄、保有目的が純投資目的以外の目的である特定投資株式の明細、最大保有会社
				self.NameOfSecuritiesDetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'NumberOfSharesHeldDetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany': #株式数、保有目的が純投資目的以外の目的である特定投資株式の明細、最大保有会社
				self.NumberOfSharesHeldDetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'NumberOfSharesNotDisclosedAsBelowThresholdDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany': #株式数（記載省略）、保有目的が純投資目的以外の目的である特定投資株式の明細、最大保有会社
				self.NumberOfSharesNotDisclosedAsBelowThresholdDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'BookValueDetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany': #貸借対照表計上額、保有目的が純投資目的以外の目的である特定投資株式の明細、最大保有会社
				self.BookValueDetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'CarryingAmountNotDisclosedAsBelowThresholdDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany': #貸借対照表計上額（記載省略）、保有目的が純投資目的以外の目的である特定投資株式の明細、最大保有会社
				self.CarryingAmountNotDisclosedAsBelowThresholdDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'PurposesOfHoldingDetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany': #保有目的、保有目的が純投資目的以外の目的である特定投資株式の明細、最大保有会社
				self.PurposesOfHoldingDetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'QuantitativeEffectsOfShareholdingDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany': #定量的な保有効果、保有目的が純投資目的以外の目的である特定投資株式の明細、最大保有会社
				self.QuantitativeEffectsOfShareholdingDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'ReasonForIncreaseInNumberOfSharesDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany': #株式数が増加した理由、保有目的が純投資目的以外の目的である特定投資株式の明細、最大保有会社
				self.ReasonForIncreaseInNumberOfSharesDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'PurposeOfShareholdingQuantitativeEffectsOfShareholdingAndReasonForIncreaseInNumberOfSharesDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany': #保有目的、定量的な保有効果及び株式数が増加した理由、保有目的が純投資目的以外の目的である特定投資株式の明細、最大保有会社
				self.PurposeOfShareholdingQuantitativeEffectsOfShareholdingAndReasonForIncreaseInNumberOfSharesDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'WhetherIssuerOfAforementionedSharesHoldsReportingCompanysSharesDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany': #当該株式の発行者による提出会社の株式の保有の有無、保有目的が純投資目的以外の目的である特定投資株式の明細、最大保有会社
				self.WhetherIssuerOfAforementionedSharesHoldsReportingCompanysSharesDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'ShareholdingsHeading': #株式の保有状況 [目次項目]
				self.ShareholdingsHeading = fact.value

			elif fact.concept.qname.localName == 'GroupCompanyHoldingLargestAmountOfInvestmentEquitySecuritiesInGroupEquitySecuritiesHeldAbstract': #最大保有会社（提出会社でない場合）、株式の保有状況 [タイトル項目]
				self.GroupCompanyHoldingLargestAmountOfInvestmentEquitySecuritiesInGroupEquitySecuritiesHeldAbstract = fact.value

			elif fact.concept.qname.localName == 'DetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompanyTable': #保有目的が純投資目的以外の目的であるみなし保有株式の明細、最大保有会社 [表]
				self.DetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompanyTable = fact.value

			elif fact.concept.qname.localName == 'SequentialNumbersAxis': #連番 [軸]
				self.SequentialNumbersAxis = fact.value

			elif fact.concept.qname.localName == 'Row1Member': #1件目 [メンバー]
				self.Row1Member = fact.value

			elif fact.concept.qname.localName == 'Row2Member': #2件目 [メンバー]
				self.Row2Member = fact.value

			elif fact.concept.qname.localName == 'Row3Member': #3件目 [メンバー]
				self.Row3Member = fact.value

			elif fact.concept.qname.localName == 'Row4Member': #4件目 [メンバー]
				self.Row4Member = fact.value

			elif fact.concept.qname.localName == 'Row5Member': #5件目 [メンバー]
				self.Row5Member = fact.value

			elif fact.concept.qname.localName == 'Row6Member': #6件目 [メンバー]
				self.Row6Member = fact.value

			elif fact.concept.qname.localName == 'Row7Member': #7件目 [メンバー]
				self.Row7Member = fact.value

			elif fact.concept.qname.localName == 'Row8Member': #8件目 [メンバー]
				self.Row8Member = fact.value

			elif fact.concept.qname.localName == 'Row9Member': #9件目 [メンバー]
				self.Row9Member = fact.value

			elif fact.concept.qname.localName == 'Row10Member': #10件目 [メンバー]
				self.Row10Member = fact.value

			elif fact.concept.qname.localName == 'DetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompanyLineItems': #保有目的が純投資目的以外の目的であるみなし保有株式の明細、最大保有会社 [表示項目]
				self.DetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompanyLineItems = fact.value

			elif fact.concept.qname.localName == 'NameOfSecuritiesDetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany': #銘柄、保有目的が純投資目的以外の目的であるみなし保有株式の明細、最大保有会社
				self.NameOfSecuritiesDetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'NumberOfSharesHeldDetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany': #株式数、保有目的が純投資目的以外の目的であるみなし保有株式の明細、最大保有会社
				self.NumberOfSharesHeldDetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'NumberOfSharesNotDisclosedAsBelowThresholdDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany': #株式数（記載省略）、保有目的が純投資目的以外の目的であるみなし保有株式の明細、最大保有会社
				self.NumberOfSharesNotDisclosedAsBelowThresholdDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'BookValueDetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany': #貸借対照表計上額、保有目的が純投資目的以外の目的であるみなし保有株式の明細、最大保有会社
				self.BookValueDetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'CarryingAmountNotDisclosedAsBelowThresholdDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany': #貸借対照表計上額（記載省略）、保有目的が純投資目的以外の目的であるみなし保有株式の明細、最大保有会社
				self.CarryingAmountNotDisclosedAsBelowThresholdDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'PurposesOfHoldingDetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany': #保有目的、保有目的が純投資目的以外の目的であるみなし保有株式の明細、最大保有会社
				self.PurposesOfHoldingDetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'QuantitativeEffectsOfShareholdingDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany': #定量的な保有効果、保有目的が純投資目的以外の目的であるみなし保有株式の明細、最大保有会社
				self.QuantitativeEffectsOfShareholdingDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'ReasonForIncreaseInNumberOfSharesDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany': #株式数が増加した理由、保有目的が純投資目的以外の目的であるみなし保有株式の明細、最大保有会社
				self.ReasonForIncreaseInNumberOfSharesDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'PurposeOfShareholdingQuantitativeEffectsOfShareholdingAndReasonForIncreaseInNumberOfSharesDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany': #保有目的、定量的な保有効果及び株式数が増加した理由、保有目的が純投資目的以外の目的であるみなし保有株式の明細、最大保有会社
				self.PurposeOfShareholdingQuantitativeEffectsOfShareholdingAndReasonForIncreaseInNumberOfSharesDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'WhetherIssuerOfAforementionedSharesHoldsReportingCompanysSharesDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany': #当該株式の発行者による提出会社の株式の保有の有無、保有目的が純投資目的以外の目的であるみなし保有株式の明細、最大保有会社
				self.WhetherIssuerOfAforementionedSharesHoldsReportingCompanysSharesDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'ShareholdingsHeading': #株式の保有状況 [目次項目]
				self.ShareholdingsHeading = fact.value

			elif fact.concept.qname.localName == 'GroupCompanyHoldingLargestAmountOfInvestmentEquitySecuritiesInGroupEquitySecuritiesHeldAbstract': #最大保有会社（提出会社でない場合）、株式の保有状況 [タイトル項目]
				self.GroupCompanyHoldingLargestAmountOfInvestmentEquitySecuritiesInGroupEquitySecuritiesHeldAbstract = fact.value

			elif fact.concept.qname.localName == 'InvestmentEquitySecuritiesHeldForPureInvestmentLargestHoldingCompanyAbstract': #保有目的が純投資目的である投資株式、最大保有会社 [タイトル項目]
				self.InvestmentEquitySecuritiesHeldForPureInvestmentLargestHoldingCompanyAbstract = fact.value

			elif fact.concept.qname.localName == 'EquitySecuritiesNotListedInvestmentEquitySecuritiesHeldForPureInvestmentLargestHoldingCompanyAbstract': #非上場株式、保有目的が純投資目的である投資株式、最大保有会社 [タイトル項目]
				self.EquitySecuritiesNotListedInvestmentEquitySecuritiesHeldForPureInvestmentLargestHoldingCompanyAbstract = fact.value

			elif fact.concept.qname.localName == 'NumberOfIssuesSharesNotListedInvestmentSharesHeldForPureInvestmentLargestHoldingCompany': #銘柄数、非上場株式、保有目的が純投資目的である投資株式、最大保有会社
				self.NumberOfIssuesSharesNotListedInvestmentSharesHeldForPureInvestmentLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'BookValueEquitySecuritiesNotListedInvestmentEquitySecuritiesHeldForPureInvestmentLargestHoldingCompany': #貸借対照表計上額の合計額、非上場株式、保有目的が純投資目的である投資株式、最大保有会社
				self.BookValueEquitySecuritiesNotListedInvestmentEquitySecuritiesHeldForPureInvestmentLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'TotalOfDividendsReceivedEquitySecuritiesNotListedInvestmentEquitySecuritiesHeldForPureInvestmentLargestHoldingCompany': #受取配当金の合計額、非上場株式、保有目的が純投資目的である投資株式、最大保有会社
				self.TotalOfDividendsReceivedEquitySecuritiesNotListedInvestmentEquitySecuritiesHeldForPureInvestmentLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'TotalOfGainLossOnSaleEquitySecuritiesNotListedInvestmentEquitySecuritiesHeldForPureInvestmentLargestHoldingCompany': #売却損益の合計額、非上場株式、保有目的が純投資目的である投資株式、最大保有会社
				self.TotalOfGainLossOnSaleEquitySecuritiesNotListedInvestmentEquitySecuritiesHeldForPureInvestmentLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'TotalOfValuationGainLossEquitySecuritiesNotListedInvestmentEquitySecuritiesHeldForPureInvestmentLargestHoldingCompany': #評価損益の合計額、非上場株式、保有目的が純投資目的である投資株式、最大保有会社
				self.TotalOfValuationGainLossEquitySecuritiesNotListedInvestmentEquitySecuritiesHeldForPureInvestmentLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'EquitySecuritiesOtherThanThoseNotListedInvestmentEquitySecuritiesHeldForPureInvestmentLargestHoldingCompanyAbstract': #非上場株式以外の株式、保有目的が純投資目的である投資株式、最大保有会社 [タイトル項目]
				self.EquitySecuritiesOtherThanThoseNotListedInvestmentEquitySecuritiesHeldForPureInvestmentLargestHoldingCompanyAbstract = fact.value

			elif fact.concept.qname.localName == 'NumberOfIssuesSharesOtherThanThoseNotListedInvestmentSharesHeldForPureInvestmentLargestHoldingCompany': #銘柄数、非上場株式以外の株式、保有目的が純投資目的である投資株式、最大保有会社
				self.NumberOfIssuesSharesOtherThanThoseNotListedInvestmentSharesHeldForPureInvestmentLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'BookValueEquitySecuritiesOtherThanThoseNotListedInvestmentEquitySecuritiesHeldForPureInvestmentLargestHoldingCompany': #貸借対照表計上額の合計額、非上場株式以外の株式、保有目的が純投資目的である投資株式、最大保有会社
				self.BookValueEquitySecuritiesOtherThanThoseNotListedInvestmentEquitySecuritiesHeldForPureInvestmentLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'TotalOfDividendsReceivedEquitySecuritiesOtherThanThoseNotListedInvestmentEquitySecuritiesHeldForPureInvestmentLargestHoldingCompany': #受取配当金の合計額、非上場株式以外の株式、保有目的が純投資目的である投資株式、最大保有会社
				self.TotalOfDividendsReceivedEquitySecuritiesOtherThanThoseNotListedInvestmentEquitySecuritiesHeldForPureInvestmentLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'TotalOfGainLossOnSaleEquitySecuritiesOtherThanThoseNotListedInvestmentEquitySecuritiesHeldForPureInvestmentLargestHoldingCompany': #売却損益の合計額、非上場株式以外の株式、保有目的が純投資目的である投資株式、最大保有会社
				self.TotalOfGainLossOnSaleEquitySecuritiesOtherThanThoseNotListedInvestmentEquitySecuritiesHeldForPureInvestmentLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'TotalOfValuationGainLossEquitySecuritiesOtherThanThoseNotListedInvestmentEquitySecuritiesHeldForPureInvestmentLargestHoldingCompany': #評価損益の合計額、非上場株式以外の株式、保有目的が純投資目的である投資株式、最大保有会社
				self.TotalOfValuationGainLossEquitySecuritiesOtherThanThoseNotListedInvestmentEquitySecuritiesHeldForPureInvestmentLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'ShareholdingsHeading': #株式の保有状況 [目次項目]
				self.ShareholdingsHeading = fact.value

			elif fact.concept.qname.localName == 'GroupCompanyHoldingLargestAmountOfInvestmentEquitySecuritiesInGroupEquitySecuritiesHeldAbstract': #最大保有会社（提出会社でない場合）、株式の保有状況 [タイトル項目]
				self.GroupCompanyHoldingLargestAmountOfInvestmentEquitySecuritiesInGroupEquitySecuritiesHeldAbstract = fact.value

			elif fact.concept.qname.localName == 'InvestmentEquitySecuritiesReclassifiedFromHeldForPureInvestmentToHeldForPurposesOtherThanPureInvestmentLargestHoldingCompanyTable': #投資株式の保有目的を純投資目的から純投資目的以外の目的に変更したもの、最大保有会社 [表]
				self.InvestmentEquitySecuritiesReclassifiedFromHeldForPureInvestmentToHeldForPurposesOtherThanPureInvestmentLargestHoldingCompanyTable = fact.value

			elif fact.concept.qname.localName == 'SequentialNumbersAxis': #連番 [軸]
				self.SequentialNumbersAxis = fact.value

			elif fact.concept.qname.localName == 'Row1Member': #1件目 [メンバー]
				self.Row1Member = fact.value

			elif fact.concept.qname.localName == 'Row2Member': #2件目 [メンバー]
				self.Row2Member = fact.value

			elif fact.concept.qname.localName == 'Row3Member': #3件目 [メンバー]
				self.Row3Member = fact.value

			elif fact.concept.qname.localName == 'InvestmentEquitySecuritiesReclassifiedFromHeldForPureInvestmentToHeldForPurposesOtherThanPureInvestmentLargestHoldingCompanyLineItems': #投資株式の保有目的を純投資目的から純投資目的以外の目的に変更したもの、最大保有会社 [表示項目]
				self.InvestmentEquitySecuritiesReclassifiedFromHeldForPureInvestmentToHeldForPurposesOtherThanPureInvestmentLargestHoldingCompanyLineItems = fact.value

			elif fact.concept.qname.localName == 'NameOfSecuritiesInvestmentEquitySecuritiesReclassifiedFromHeldForPureInvestmentToHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany': #銘柄、投資株式の保有目的を純投資目的から純投資目的以外の目的に変更したもの、最大保有会社
				self.NameOfSecuritiesInvestmentEquitySecuritiesReclassifiedFromHeldForPureInvestmentToHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'NumberOfSharesHeldInvestmentEquitySecuritiesReclassifiedFromHeldForPureInvestmentToHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany': #株式数、投資株式の保有目的を純投資目的から純投資目的以外の目的に変更したもの、最大保有会社
				self.NumberOfSharesHeldInvestmentEquitySecuritiesReclassifiedFromHeldForPureInvestmentToHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'BookValueInvestmentEquitySecuritiesReclassifiedFromHeldForPureInvestmentToHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany': #貸借対照表計上額、投資株式の保有目的を純投資目的から純投資目的以外の目的に変更したもの、最大保有会社
				self.BookValueInvestmentEquitySecuritiesReclassifiedFromHeldForPureInvestmentToHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'ShareholdingsHeading': #株式の保有状況 [目次項目]
				self.ShareholdingsHeading = fact.value

			elif fact.concept.qname.localName == 'GroupCompanyHoldingLargestAmountOfInvestmentEquitySecuritiesInGroupEquitySecuritiesHeldAbstract': #最大保有会社（提出会社でない場合）、株式の保有状況 [タイトル項目]
				self.GroupCompanyHoldingLargestAmountOfInvestmentEquitySecuritiesInGroupEquitySecuritiesHeldAbstract = fact.value

			elif fact.concept.qname.localName == 'InvestmentEquitySecuritiesReclassifiedFromHeldForPurposesOtherThanPureInvestmentToHeldForPureInvestmentLargestHoldingCompanyTable': #投資株式の保有目的を純投資以外の目的から純投資目的に変更したもの、最大保有会社 [表]
				self.InvestmentEquitySecuritiesReclassifiedFromHeldForPurposesOtherThanPureInvestmentToHeldForPureInvestmentLargestHoldingCompanyTable = fact.value

			elif fact.concept.qname.localName == 'SequentialNumbersAxis': #連番 [軸]
				self.SequentialNumbersAxis = fact.value

			elif fact.concept.qname.localName == 'Row1Member': #1件目 [メンバー]
				self.Row1Member = fact.value

			elif fact.concept.qname.localName == 'Row2Member': #2件目 [メンバー]
				self.Row2Member = fact.value

			elif fact.concept.qname.localName == 'Row3Member': #3件目 [メンバー]
				self.Row3Member = fact.value

			elif fact.concept.qname.localName == 'InvestmentEquitySecuritiesReclassifiedFromHeldForPurposesOtherThanPureInvestmentToHeldForPureInvestmentLargestHoldingCompanyLineItems': #投資株式の保有目的を純投資以外の目的から純投資目的に変更したもの、最大保有会社 [表示項目]
				self.InvestmentEquitySecuritiesReclassifiedFromHeldForPurposesOtherThanPureInvestmentToHeldForPureInvestmentLargestHoldingCompanyLineItems = fact.value

			elif fact.concept.qname.localName == 'NameOfSecuritiesInvestmentEquitySecuritiesReclassifiedFromHeldForPurposesOtherThanPureInvestmentToHeldForPureInvestmentLargestHoldingCompany': #銘柄、投資株式の保有目的を純投資以外の目的から純投資目的に変更したもの、最大保有会社
				self.NameOfSecuritiesInvestmentEquitySecuritiesReclassifiedFromHeldForPurposesOtherThanPureInvestmentToHeldForPureInvestmentLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'NumberOfSharesHeldInvestmentEquitySecuritiesReclassifiedFromHeldForPurposesOtherThanPureInvestmentToHeldForPureInvestmentLargestHoldingCompany': #株式数、投資株式の保有目的を純投資以外の目的から純投資目的に変更したもの、最大保有会社
				self.NumberOfSharesHeldInvestmentEquitySecuritiesReclassifiedFromHeldForPurposesOtherThanPureInvestmentToHeldForPureInvestmentLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'BookValueInvestmentEquitySecuritiesReclassifiedFromHeldForPurposesOtherThanPureInvestmentToHeldForPureInvestmentLargestHoldingCompany': #貸借対照表計上額、投資株式の保有目的を純投資以外の目的から純投資目的に変更したもの、最大保有会社
				self.BookValueInvestmentEquitySecuritiesReclassifiedFromHeldForPurposesOtherThanPureInvestmentToHeldForPureInvestmentLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'ShareholdingsHeading': #株式の保有状況 [目次項目]
				self.ShareholdingsHeading = fact.value

			elif fact.concept.qname.localName == 'GroupCompanyHoldingSecondLargestAmountOfInvestmentEquitySecuritiesInGroupEquitySecuritiesHeldAbstract': #投資株式計上額が次に大きい会社（提出会社でない場合）、株式の保有状況 [タイトル項目]
				self.GroupCompanyHoldingSecondLargestAmountOfInvestmentEquitySecuritiesInGroupEquitySecuritiesHeldAbstract = fact.value

			elif fact.concept.qname.localName == 'InvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompanyAbstract': #保有目的が純投資目的以外の目的である投資株式、投資株式計上額が次に大きい会社 [タイトル項目]
				self.InvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompanyAbstract = fact.value

			elif fact.concept.qname.localName == 'SharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompanyAbstract': #非上場株式、保有目的が純投資目的以外の目的である投資株式、投資株式計上額が次に大きい会社 [タイトル項目]
				self.SharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompanyAbstract = fact.value

			elif fact.concept.qname.localName == 'NumberOfIssuesSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany': #銘柄数、非上場株式、保有目的が純投資目的以外の目的である投資株式、投資株式計上額が次に大きい会社
				self.NumberOfIssuesSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'CarryingAmountSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany': #貸借対照表計上額、非上場株式、保有目的が純投資目的以外の目的である投資株式、投資株式計上額が次に大きい会社
				self.CarryingAmountSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'NumberOfIssuesWhoseNumberOfSharesIncreasedSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany': #株式数が増加した銘柄数、非上場株式、保有目的が純投資目的以外の目的である投資株式、投資株式計上額が次に大きい会社
				self.NumberOfIssuesWhoseNumberOfSharesIncreasedSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'TotalAcquisitionCostForIncreasedSharesSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany': #株式数の増加に係る取得価額の合計額、非上場株式、保有目的が純投資目的以外の目的である投資株式、投資株式計上額が次に大きい会社
				self.TotalAcquisitionCostForIncreasedSharesSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'ReasonForIncreaseInNumberOfSharesSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany': #株式数が増加した理由、非上場株式、保有目的が純投資目的以外の目的である投資株式、投資株式計上額が次に大きい会社
				self.ReasonForIncreaseInNumberOfSharesSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'NumberOfIssuesWhoseNumberOfSharesDecreasedSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany': #株式数が減少した銘柄数、非上場株式、保有目的が純投資目的以外の目的である投資株式、投資株式計上額が次に大きい会社
				self.NumberOfIssuesWhoseNumberOfSharesDecreasedSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'TotalSaleAmountForDecreasedSharesSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany': #株式数の減少に係る売却価額の合計額、非上場株式、保有目的が純投資目的以外の目的である投資株式、投資株式計上額が次に大きい会社
				self.TotalSaleAmountForDecreasedSharesSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'SharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompanyAbstract': #非上場株式以外の株式、保有目的が純投資目的以外の目的である投資株式、投資株式計上額が次に大きい会社 [タイトル項目]
				self.SharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompanyAbstract = fact.value

			elif fact.concept.qname.localName == 'NumberOfIssuesSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany': #銘柄数、非上場株式以外の株式、保有目的が純投資目的以外の目的である投資株式、投資株式計上額が次に大きい会社
				self.NumberOfIssuesSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'CarryingAmountSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany': #貸借対照表計上額、非上場株式以外の株式、保有目的が純投資目的以外の目的である投資株式、投資株式計上額が次に大きい会社
				self.CarryingAmountSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'NumberOfIssuesWhoseNumberOfSharesIncreasedSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany': #株式数が増加した銘柄数、非上場株式以外の株式、保有目的が純投資目的以外の目的である投資株式、投資株式計上額が次に大きい会社
				self.NumberOfIssuesWhoseNumberOfSharesIncreasedSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'TotalAcquisitionCostForIncreasedSharesSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany': #株式数の増加に係る取得価額の合計額、非上場株式以外の株式、保有目的が純投資目的以外の目的である投資株式、投資株式計上額が次に大きい会社
				self.TotalAcquisitionCostForIncreasedSharesSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'ReasonForIncreaseInNumberOfSharesSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany': #株式数が増加した理由、非上場株式以外の株式、保有目的が純投資目的以外の目的である投資株式、投資株式計上額が次に大きい会社
				self.ReasonForIncreaseInNumberOfSharesSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'NumberOfIssuesWhoseNumberOfSharesDecreasedSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany': #株式数が減少した銘柄数、非上場株式以外の株式、保有目的が純投資目的以外の目的である投資株式、投資株式計上額が次に大きい会社
				self.NumberOfIssuesWhoseNumberOfSharesDecreasedSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'TotalSaleAmountForDecreasedSharesSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany': #株式数の減少に係る売却価額の合計額、非上場株式以外の株式、保有目的が純投資目的以外の目的である投資株式、投資株式計上額が次に大きい会社
				self.TotalSaleAmountForDecreasedSharesSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'ShareholdingsHeading': #株式の保有状況 [目次項目]
				self.ShareholdingsHeading = fact.value

			elif fact.concept.qname.localName == 'GroupCompanyHoldingSecondLargestAmountOfInvestmentEquitySecuritiesInGroupEquitySecuritiesHeldAbstract': #投資株式計上額が次に大きい会社（提出会社でない場合）、株式の保有状況 [タイトル項目]
				self.GroupCompanyHoldingSecondLargestAmountOfInvestmentEquitySecuritiesInGroupEquitySecuritiesHeldAbstract = fact.value

			elif fact.concept.qname.localName == 'DetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompanyTable': #保有目的が純投資目的以外の目的である特定投資株式の明細、投資株式計上額が次に大きい会社 [表]
				self.DetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompanyTable = fact.value

			elif fact.concept.qname.localName == 'SequentialNumbersAxis': #連番 [軸]
				self.SequentialNumbersAxis = fact.value

			elif fact.concept.qname.localName == 'Row1Member': #1件目 [メンバー]
				self.Row1Member = fact.value

			elif fact.concept.qname.localName == 'Row2Member': #2件目 [メンバー]
				self.Row2Member = fact.value

			elif fact.concept.qname.localName == 'Row3Member': #3件目 [メンバー]
				self.Row3Member = fact.value

			elif fact.concept.qname.localName == 'Row4Member': #4件目 [メンバー]
				self.Row4Member = fact.value

			elif fact.concept.qname.localName == 'Row5Member': #5件目 [メンバー]
				self.Row5Member = fact.value

			elif fact.concept.qname.localName == 'Row6Member': #6件目 [メンバー]
				self.Row6Member = fact.value

			elif fact.concept.qname.localName == 'Row7Member': #7件目 [メンバー]
				self.Row7Member = fact.value

			elif fact.concept.qname.localName == 'Row8Member': #8件目 [メンバー]
				self.Row8Member = fact.value

			elif fact.concept.qname.localName == 'Row9Member': #9件目 [メンバー]
				self.Row9Member = fact.value

			elif fact.concept.qname.localName == 'Row10Member': #10件目 [メンバー]
				self.Row10Member = fact.value

			elif fact.concept.qname.localName == 'DetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompanyLineItems': #保有目的が純投資目的以外の目的である特定投資株式の明細、投資株式計上額が次に大きい会社 [表示項目]
				self.DetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompanyLineItems = fact.value

			elif fact.concept.qname.localName == 'NameOfSecuritiesDetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany': #銘柄、保有目的が純投資目的以外の目的である特定投資株式の明細、投資株式計上額が次に大きい会社
				self.NameOfSecuritiesDetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'NumberOfSharesHeldDetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany': #株式数、保有目的が純投資目的以外の目的である特定投資株式の明細、投資株式計上額が次に大きい会社
				self.NumberOfSharesHeldDetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'NumberOfSharesNotDisclosedAsBelowThresholdDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany': #株式数（記載省略）、保有目的が純投資目的以外の目的である特定投資株式の明細、投資株式計上額が次に大きい会社
				self.NumberOfSharesNotDisclosedAsBelowThresholdDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'BookValueDetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany': #貸借対照表計上額、保有目的が純投資目的以外の目的である特定投資株式の明細、投資株式計上額が次に大きい会社
				self.BookValueDetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'CarryingAmountNotDisclosedAsBelowThresholdDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany': #貸借対照表計上額（記載省略）、保有目的が純投資目的以外の目的である特定投資株式の明細、投資株式計上額が次に大きい会社
				self.CarryingAmountNotDisclosedAsBelowThresholdDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'PurposesOfHoldingDetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany': #保有目的、保有目的が純投資目的以外の目的である特定投資株式の明細、投資株式計上額が次に大きい会社
				self.PurposesOfHoldingDetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'QuantitativeEffectsOfShareholdingDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany': #定量的な保有効果、保有目的が純投資目的以外の目的である特定投資株式の明細、投資株式計上額が次に大きい会社
				self.QuantitativeEffectsOfShareholdingDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'ReasonForIncreaseInNumberOfSharesDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany': #株式数が増加した理由、保有目的が純投資目的以外の目的である特定投資株式の明細、投資株式計上額が次に大きい会社
				self.ReasonForIncreaseInNumberOfSharesDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'PurposeOfShareholdingQuantitativeEffectsOfShareholdingAndReasonForIncreaseInNumberOfSharesDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany': #保有目的、定量的な保有効果及び株式数が増加した理由、保有目的が純投資目的以外の目的である特定投資株式の明細、投資株式計上額が次に大きい会社
				self.PurposeOfShareholdingQuantitativeEffectsOfShareholdingAndReasonForIncreaseInNumberOfSharesDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'WhetherIssuerOfAforementionedSharesHoldsReportingCompanysSharesDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany': #当該株式の発行者による提出会社の株式の保有の有無、保有目的が純投資目的以外の目的である特定投資株式の明細、投資株式計上額が次に大きい会社
				self.WhetherIssuerOfAforementionedSharesHoldsReportingCompanysSharesDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'ShareholdingsHeading': #株式の保有状況 [目次項目]
				self.ShareholdingsHeading = fact.value

			elif fact.concept.qname.localName == 'GroupCompanyHoldingSecondLargestAmountOfInvestmentEquitySecuritiesInGroupEquitySecuritiesHeldAbstract': #投資株式計上額が次に大きい会社（提出会社でない場合）、株式の保有状況 [タイトル項目]
				self.GroupCompanyHoldingSecondLargestAmountOfInvestmentEquitySecuritiesInGroupEquitySecuritiesHeldAbstract = fact.value

			elif fact.concept.qname.localName == 'DetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompanyTable': #保有目的が純投資目的以外の目的であるみなし保有株式の明細、投資株式計上額が次に大きい会社 [表]
				self.DetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompanyTable = fact.value

			elif fact.concept.qname.localName == 'SequentialNumbersAxis': #連番 [軸]
				self.SequentialNumbersAxis = fact.value

			elif fact.concept.qname.localName == 'Row1Member': #1件目 [メンバー]
				self.Row1Member = fact.value

			elif fact.concept.qname.localName == 'Row2Member': #2件目 [メンバー]
				self.Row2Member = fact.value

			elif fact.concept.qname.localName == 'Row3Member': #3件目 [メンバー]
				self.Row3Member = fact.value

			elif fact.concept.qname.localName == 'Row4Member': #4件目 [メンバー]
				self.Row4Member = fact.value

			elif fact.concept.qname.localName == 'Row5Member': #5件目 [メンバー]
				self.Row5Member = fact.value

			elif fact.concept.qname.localName == 'Row6Member': #6件目 [メンバー]
				self.Row6Member = fact.value

			elif fact.concept.qname.localName == 'Row7Member': #7件目 [メンバー]
				self.Row7Member = fact.value

			elif fact.concept.qname.localName == 'Row8Member': #8件目 [メンバー]
				self.Row8Member = fact.value

			elif fact.concept.qname.localName == 'Row9Member': #9件目 [メンバー]
				self.Row9Member = fact.value

			elif fact.concept.qname.localName == 'Row10Member': #10件目 [メンバー]
				self.Row10Member = fact.value

			elif fact.concept.qname.localName == 'DetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompanyLineItems': #保有目的が純投資目的以外の目的であるみなし保有株式の明細、投資株式計上額が次に大きい会社 [表示項目]
				self.DetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompanyLineItems = fact.value

			elif fact.concept.qname.localName == 'NameOfSecuritiesDetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany': #銘柄、保有目的が純投資目的以外の目的であるみなし保有株式の明細、投資株式計上額が次に大きい会社
				self.NameOfSecuritiesDetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'NumberOfSharesHeldDetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany': #株式数、保有目的が純投資目的以外の目的であるみなし保有株式の明細、投資株式計上額が次に大きい会社
				self.NumberOfSharesHeldDetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'NumberOfSharesNotDisclosedAsBelowThresholdDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany': #株式数（記載省略）、保有目的が純投資目的以外の目的であるみなし保有株式の明細、投資株式計上額が次に大きい会社
				self.NumberOfSharesNotDisclosedAsBelowThresholdDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'BookValueDetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany': #貸借対照表計上額、保有目的が純投資目的以外の目的であるみなし保有株式の明細、投資株式計上額が次に大きい会社
				self.BookValueDetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'CarryingAmountNotDisclosedAsBelowThresholdDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany': #貸借対照表計上額（記載省略）、保有目的が純投資目的以外の目的であるみなし保有株式の明細、投資株式計上額が次に大きい会社
				self.CarryingAmountNotDisclosedAsBelowThresholdDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'PurposesOfHoldingDetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany': #保有目的、保有目的が純投資目的以外の目的であるみなし保有株式の明細、投資株式計上額が次に大きい会社
				self.PurposesOfHoldingDetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'QuantitativeEffectsOfShareholdingDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany': #定量的な保有効果、保有目的が純投資目的以外の目的であるみなし保有株式の明細、投資株式計上額が次に大きい会社
				self.QuantitativeEffectsOfShareholdingDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'ReasonForIncreaseInNumberOfSharesDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany': #株式数が増加した理由、保有目的が純投資目的以外の目的であるみなし保有株式の明細、投資株式計上額が次に大きい会社
				self.ReasonForIncreaseInNumberOfSharesDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'PurposeOfShareholdingQuantitativeEffectsOfShareholdingAndReasonForIncreaseInNumberOfSharesDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany': #保有目的、定量的な保有効果及び株式数が増加した理由、保有目的が純投資目的以外の目的であるみなし保有株式の明細、投資株式計上額が次に大きい会社
				self.PurposeOfShareholdingQuantitativeEffectsOfShareholdingAndReasonForIncreaseInNumberOfSharesDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'WhetherIssuerOfAforementionedSharesHoldsReportingCompanysSharesDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany': #当該株式の発行者による提出会社の株式の保有の有無、保有目的が純投資目的以外の目的であるみなし保有株式の明細、投資株式計上額が次に大きい会社
				self.WhetherIssuerOfAforementionedSharesHoldsReportingCompanysSharesDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'ShareholdingsHeading': #株式の保有状況 [目次項目]
				self.ShareholdingsHeading = fact.value

			elif fact.concept.qname.localName == 'GroupCompanyHoldingSecondLargestAmountOfInvestmentEquitySecuritiesInGroupEquitySecuritiesHeldAbstract': #投資株式計上額が次に大きい会社（提出会社でない場合）、株式の保有状況 [タイトル項目]
				self.GroupCompanyHoldingSecondLargestAmountOfInvestmentEquitySecuritiesInGroupEquitySecuritiesHeldAbstract = fact.value

			elif fact.concept.qname.localName == 'InvestmentEquitySecuritiesHeldForPureInvestmentSecondLargestHoldingCompanyAbstract': #保有目的が純投資目的である投資株式、投資株式計上額が次に大きい会社 [タイトル項目]
				self.InvestmentEquitySecuritiesHeldForPureInvestmentSecondLargestHoldingCompanyAbstract = fact.value

			elif fact.concept.qname.localName == 'EquitySecuritiesNotListedInvestmentEquitySecuritiesHeldForPureInvestmentSecondLargestHoldingCompanyAbstract': #非上場株式、保有目的が純投資目的である投資株式、投資株式計上額が次に大きい会社 [タイトル項目]
				self.EquitySecuritiesNotListedInvestmentEquitySecuritiesHeldForPureInvestmentSecondLargestHoldingCompanyAbstract = fact.value

			elif fact.concept.qname.localName == 'NumberOfIssuesSharesNotListedInvestmentSharesHeldForPureInvestmentSecondLargestHoldingCompany': #銘柄数、非上場株式、保有目的が純投資目的である投資株式、投資株式計上額が次に大きい会社
				self.NumberOfIssuesSharesNotListedInvestmentSharesHeldForPureInvestmentSecondLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'BookValueEquitySecuritiesNotListedInvestmentEquitySecuritiesHeldForPureInvestmentSecondLargestHoldingCompany': #貸借対照表計上額の合計額、非上場株式、保有目的が純投資目的である投資株式、投資株式計上額が次に大きい会社
				self.BookValueEquitySecuritiesNotListedInvestmentEquitySecuritiesHeldForPureInvestmentSecondLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'TotalOfDividendsReceivedEquitySecuritiesNotListedInvestmentEquitySecuritiesHeldForPureInvestmentSecondLargestHoldingCompany': #受取配当金の合計額、非上場株式、保有目的が純投資目的である投資株式、投資株式計上額が次に大きい会社
				self.TotalOfDividendsReceivedEquitySecuritiesNotListedInvestmentEquitySecuritiesHeldForPureInvestmentSecondLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'TotalOfGainLossOnSaleEquitySecuritiesNotListedInvestmentEquitySecuritiesHeldForPureInvestmentSecondLargestHoldingCompany': #売却損益の合計額、非上場株式、保有目的が純投資目的である投資株式、投資株式計上額が次に大きい会社
				self.TotalOfGainLossOnSaleEquitySecuritiesNotListedInvestmentEquitySecuritiesHeldForPureInvestmentSecondLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'TotalOfValuationGainLossEquitySecuritiesNotListedInvestmentEquitySecuritiesHeldForPureInvestmentSecondLargestHoldingCompany': #評価損益の合計額、非上場株式、保有目的が純投資目的である投資株式、投資株式計上額が次に大きい会社
				self.TotalOfValuationGainLossEquitySecuritiesNotListedInvestmentEquitySecuritiesHeldForPureInvestmentSecondLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'EquitySecuritiesOtherThanThoseNotListedInvestmentEquitySecuritiesHeldForPureInvestmentSecondLargestHoldingCompanyAbstract': #非上場株式以外の株式、保有目的が純投資目的である投資株式、投資株式計上額が次に大きい会社 [タイトル項目]
				self.EquitySecuritiesOtherThanThoseNotListedInvestmentEquitySecuritiesHeldForPureInvestmentSecondLargestHoldingCompanyAbstract = fact.value

			elif fact.concept.qname.localName == 'NumberOfIssuesSharesOtherThanThoseNotListedInvestmentSharesHeldForPureInvestmentSecondLargestHoldingCompany': #銘柄数、非上場株式以外の株式、保有目的が純投資目的である投資株式、投資株式計上額が次に大きい会社
				self.NumberOfIssuesSharesOtherThanThoseNotListedInvestmentSharesHeldForPureInvestmentSecondLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'BookValueEquitySecuritiesOtherThanThoseNotListedInvestmentEquitySecuritiesHeldForPureInvestmentSecondLargestHoldingCompany': #貸借対照表計上額の合計額、非上場株式以外の株式、保有目的が純投資目的である投資株式、投資株式計上額が次に大きい会社
				self.BookValueEquitySecuritiesOtherThanThoseNotListedInvestmentEquitySecuritiesHeldForPureInvestmentSecondLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'TotalOfDividendsReceivedEquitySecuritiesOtherThanThoseNotListedInvestmentEquitySecuritiesHeldForPureInvestmentSecondLargestHoldingCompany': #受取配当金の合計額、非上場株式以外の株式、保有目的が純投資目的である投資株式、投資株式計上額が次に大きい会社
				self.TotalOfDividendsReceivedEquitySecuritiesOtherThanThoseNotListedInvestmentEquitySecuritiesHeldForPureInvestmentSecondLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'TotalOfGainLossOnSaleEquitySecuritiesOtherThanThoseNotListedInvestmentEquitySecuritiesHeldForPureInvestmentSecondLargestHoldingCompany': #売却損益の合計額、非上場株式以外の株式、保有目的が純投資目的である投資株式、投資株式計上額が次に大きい会社
				self.TotalOfGainLossOnSaleEquitySecuritiesOtherThanThoseNotListedInvestmentEquitySecuritiesHeldForPureInvestmentSecondLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'TotalOfValuationGainLossEquitySecuritiesOtherThanThoseNotListedInvestmentEquitySecuritiesHeldForPureInvestmentSecondLargestHoldingCompany': #評価損益の合計額、非上場株式以外の株式、保有目的が純投資目的である投資株式、投資株式計上額が次に大きい会社
				self.TotalOfValuationGainLossEquitySecuritiesOtherThanThoseNotListedInvestmentEquitySecuritiesHeldForPureInvestmentSecondLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'ShareholdingsHeading': #株式の保有状況 [目次項目]
				self.ShareholdingsHeading = fact.value

			elif fact.concept.qname.localName == 'GroupCompanyHoldingSecondLargestAmountOfInvestmentEquitySecuritiesInGroupEquitySecuritiesHeldAbstract': #投資株式計上額が次に大きい会社（提出会社でない場合）、株式の保有状況 [タイトル項目]
				self.GroupCompanyHoldingSecondLargestAmountOfInvestmentEquitySecuritiesInGroupEquitySecuritiesHeldAbstract = fact.value

			elif fact.concept.qname.localName == 'InvestmentEquitySecuritiesReclassifiedFromHeldForPureInvestmentToHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompanyTable': #投資株式の保有目的を純投資目的から純投資目的以外の目的に変更したもの、投資株式計上額が次に大きい会社 [表]
				self.InvestmentEquitySecuritiesReclassifiedFromHeldForPureInvestmentToHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompanyTable = fact.value

			elif fact.concept.qname.localName == 'SequentialNumbersAxis': #連番 [軸]
				self.SequentialNumbersAxis = fact.value

			elif fact.concept.qname.localName == 'Row1Member': #1件目 [メンバー]
				self.Row1Member = fact.value

			elif fact.concept.qname.localName == 'Row2Member': #2件目 [メンバー]
				self.Row2Member = fact.value

			elif fact.concept.qname.localName == 'Row3Member': #3件目 [メンバー]
				self.Row3Member = fact.value

			elif fact.concept.qname.localName == 'InvestmentEquitySecuritiesReclassifiedFromHeldForPureInvestmentToHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompanyLineItems': #投資株式の保有目的を純投資目的から純投資目的以外の目的に変更したもの、投資株式計上額が次に大きい会社 [表示項目]
				self.InvestmentEquitySecuritiesReclassifiedFromHeldForPureInvestmentToHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompanyLineItems = fact.value

			elif fact.concept.qname.localName == 'NameOfSecuritiesInvestmentEquitySecuritiesReclassifiedFromHeldForPureInvestmentToHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany': #銘柄、投資株式の保有目的を純投資目的から純投資目的以外の目的に変更したもの、投資株式計上額が次に大きい会社
				self.NameOfSecuritiesInvestmentEquitySecuritiesReclassifiedFromHeldForPureInvestmentToHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'NumberOfSharesHeldInvestmentEquitySecuritiesReclassifiedFromHeldForPureInvestmentToHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany': #株式数、投資株式の保有目的を純投資目的から純投資目的以外の目的に変更したもの、投資株式計上額が次に大きい会社
				self.NumberOfSharesHeldInvestmentEquitySecuritiesReclassifiedFromHeldForPureInvestmentToHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'BookValueInvestmentEquitySecuritiesReclassifiedFromHeldForPureInvestmentToHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany': #貸借対照表計上額、投資株式の保有目的を純投資目的から純投資目的以外の目的に変更したもの、投資株式計上額が次に大きい会社
				self.BookValueInvestmentEquitySecuritiesReclassifiedFromHeldForPureInvestmentToHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'ShareholdingsHeading': #株式の保有状況 [目次項目]
				self.ShareholdingsHeading = fact.value

			elif fact.concept.qname.localName == 'GroupCompanyHoldingSecondLargestAmountOfInvestmentEquitySecuritiesInGroupEquitySecuritiesHeldAbstract': #投資株式計上額が次に大きい会社（提出会社でない場合）、株式の保有状況 [タイトル項目]
				self.GroupCompanyHoldingSecondLargestAmountOfInvestmentEquitySecuritiesInGroupEquitySecuritiesHeldAbstract = fact.value

			elif fact.concept.qname.localName == 'InvestmentEquitySecuritiesReclassifiedFromHeldForPurposesOtherThanPureInvestmentToHeldForPureInvestmentSecondLargestHoldingCompanyTable': #投資株式の保有目的を純投資以外の目的から純投資目的に変更したもの、投資株式計上額が次に大きい会社 [表]
				self.InvestmentEquitySecuritiesReclassifiedFromHeldForPurposesOtherThanPureInvestmentToHeldForPureInvestmentSecondLargestHoldingCompanyTable = fact.value

			elif fact.concept.qname.localName == 'SequentialNumbersAxis': #連番 [軸]
				self.SequentialNumbersAxis = fact.value

			elif fact.concept.qname.localName == 'Row1Member': #1件目 [メンバー]
				self.Row1Member = fact.value

			elif fact.concept.qname.localName == 'Row2Member': #2件目 [メンバー]
				self.Row2Member = fact.value

			elif fact.concept.qname.localName == 'Row3Member': #3件目 [メンバー]
				self.Row3Member = fact.value

			elif fact.concept.qname.localName == 'InvestmentEquitySecuritiesReclassifiedFromHeldForPurposesOtherThanPureInvestmentToHeldForPureInvestmentSecondLargestHoldingCompanyLineItems': #投資株式の保有目的を純投資以外の目的から純投資目的に変更したもの、投資株式計上額が次に大きい会社 [表示項目]
				self.InvestmentEquitySecuritiesReclassifiedFromHeldForPurposesOtherThanPureInvestmentToHeldForPureInvestmentSecondLargestHoldingCompanyLineItems = fact.value

			elif fact.concept.qname.localName == 'NameOfSecuritiesInvestmentEquitySecuritiesReclassifiedFromHeldForPurposesOtherThanPureInvestmentToHeldForPureInvestmentSecondLargestHoldingCompany': #銘柄、投資株式の保有目的を純投資以外の目的から純投資目的に変更したもの、投資株式計上額が次に大きい会社
				self.NameOfSecuritiesInvestmentEquitySecuritiesReclassifiedFromHeldForPurposesOtherThanPureInvestmentToHeldForPureInvestmentSecondLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'NumberOfSharesHeldInvestmentEquitySecuritiesReclassifiedFromHeldForPurposesOtherThanPureInvestmentToHeldForPureInvestmentSecondLargestHoldingCompany': #株式数、投資株式の保有目的を純投資以外の目的から純投資目的に変更したもの、投資株式計上額が次に大きい会社
				self.NumberOfSharesHeldInvestmentEquitySecuritiesReclassifiedFromHeldForPurposesOtherThanPureInvestmentToHeldForPureInvestmentSecondLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'BookValueInvestmentEquitySecuritiesReclassifiedFromHeldForPurposesOtherThanPureInvestmentToHeldForPureInvestmentSecondLargestHoldingCompany': #貸借対照表計上額、投資株式の保有目的を純投資以外の目的から純投資目的に変更したもの、投資株式計上額が次に大きい会社
				self.BookValueInvestmentEquitySecuritiesReclassifiedFromHeldForPurposesOtherThanPureInvestmentToHeldForPureInvestmentSecondLargestHoldingCompany = fact.value

			elif fact.concept.qname.localName == 'NameOfGroupCompanyHoldingLargestAmountOfInvestmentSharesInGroup': #最大保有会社（提出会社でない場合）の名称
				self.NameOfGroupCompanyHoldingLargestAmountOfInvestmentSharesInGroup = fact.value

			elif fact.concept.qname.localName == 'NameOfGroupCompanyHoldingSecondLargestAmountOfInvestmentSharesInGroup': #投資株式計上額が次に大きい会社（提出会社でない場合）の名称
				self.NameOfGroupCompanyHoldingSecondLargestAmountOfInvestmentSharesInGroup = fact.value

			elif fact.concept.qname.localName == 'FinancialInformationHeading': #経理の状況 [目次項目]
				self.FinancialInformationHeading = fact.value

			elif fact.concept.qname.localName == 'FinancialInformationHeading': #経理の状況 [目次項目]
				self.FinancialInformationHeading = fact.value

			elif fact.concept.qname.localName == 'RegulationsInAccordanceWithWhichConsolidatedFinancialStatementsHaveBeenPreparedFinancialInformation': #連結財務諸表が基づく規則、経理の状況
				self.RegulationsInAccordanceWithWhichConsolidatedFinancialStatementsHaveBeenPreparedFinancialInformation = fact.value

			elif fact.concept.qname.localName == 'RegulationsInAccordanceWithWhichFinancialStatementsHaveBeenPreparedFinancialInformation': #財務諸表が基づく規則、経理の状況
				self.RegulationsInAccordanceWithWhichFinancialStatementsHaveBeenPreparedFinancialInformation = fact.value

			elif fact.concept.qname.localName == 'DescriptionOfFactThatCompanyEngagesSpecifiedBusinessAndHasPreparedItsSemiAnnualConsolidatedFinancialStatementsFinancialInformation': #特定事業会社であり、中間連結財務諸表等を作成した場合の記載、経理の状況
				self.DescriptionOfFactThatCompanyEngagesSpecifiedBusinessAndHasPreparedItsSemiAnnualConsolidatedFinancialStatementsFinancialInformation = fact.value

			elif fact.concept.qname.localName == 'DescriptionOfFactThatConsolidatedFinancialStatementsHaveBeenPreparedInAccordanceWithSpecialOrdinanceOrRegulationsForIndustryInAppendedListFinancialInformation': #連結財務諸表が別記事業の特別の法令若しくは準則に基づく場合の記載、経理の状況
				self.DescriptionOfFactThatConsolidatedFinancialStatementsHaveBeenPreparedInAccordanceWithSpecialOrdinanceOrRegulationsForIndustryInAppendedListFinancialInformation = fact.value

			elif fact.concept.qname.localName == 'DescriptionOfFactThatFinancialStatementsHaveBeenPreparedInAccordanceWithSpecialOrdinanceOrRegulationsForIndustryInAppendedListFinancialInformation': #財務諸表が別記事業の特別の法令若しくは準則に基づく場合の記載、経理の状況
				self.DescriptionOfFactThatFinancialStatementsHaveBeenPreparedInAccordanceWithSpecialOrdinanceOrRegulationsForIndustryInAppendedListFinancialInformation = fact.value

			elif fact.concept.qname.localName == 'DescriptionOfFactThatConsolidatedFinancialStatementsHaveBeenPreparedInAccordanceWithIFRSFinancialInformation': #指定国際会計基準により連結財務諸表を作成した場合の記載、経理の状況
				self.DescriptionOfFactThatConsolidatedFinancialStatementsHaveBeenPreparedInAccordanceWithIFRSFinancialInformation = fact.value

			elif fact.concept.qname.localName == 'DescriptionOfFactThatConsolidatedFinancialStatementsHaveBeenPreparedInAccordanceWithJMISFinancialInformation': #修正国際基準により連結財務諸表を作成した場合の記載、経理の状況
				self.DescriptionOfFactThatConsolidatedFinancialStatementsHaveBeenPreparedInAccordanceWithJMISFinancialInformation = fact.value

			elif fact.concept.qname.localName == 'DescriptionOfFactThatConsolidatedFinancialStatementsHaveBeenPreparedInAccordanceWithUSGAAPFinancialInformation': #米国会計基準により連結財務諸表を作成した場合の記載、経理の状況
				self.DescriptionOfFactThatConsolidatedFinancialStatementsHaveBeenPreparedInAccordanceWithUSGAAPFinancialInformation = fact.value

			elif fact.concept.qname.localName == 'DescriptionOfFactThatConsolidatedFinancialStatementsHaveNotBeenPreparedFinancialInformation': #連結財務諸表を作成していない場合の記載、経理の状況
				self.DescriptionOfFactThatConsolidatedFinancialStatementsHaveNotBeenPreparedFinancialInformation = fact.value

			elif fact.concept.qname.localName == 'DescriptionOfFactThatConsolidatedFinancialStatementsHaveNotBeenPreparedAndFinancialStatementsHaveBeenPreparedInAccordanceWithIFRSFinancialInformation': #連結財務諸表を作成していない場合で指定国際会計基準により財務諸表を作成する場合の記載、経理の状況
				self.DescriptionOfFactThatConsolidatedFinancialStatementsHaveNotBeenPreparedAndFinancialStatementsHaveBeenPreparedInAccordanceWithIFRSFinancialInformation = fact.value

			elif fact.concept.qname.localName == 'DescriptionOfFactThatFinancialStatementsHaveBeenPreparedInAccordanceWithSpecialProvisionFinancialInformation': #特例財務諸表を作成する場合の記載、経理の状況
				self.DescriptionOfFactThatFinancialStatementsHaveBeenPreparedInAccordanceWithSpecialProvisionFinancialInformation = fact.value

			elif fact.concept.qname.localName == 'DescriptionOfFactThatQuarterlySecuritiesReportForFirstQuarterOrThirdQuarterPresentsStatementOfCashFlowsFinancialInformation': #第１四半期又は第３四半期に係る四半期報告書において四半期キャッシュ・フロー計算書を記載する場合の記載、経理の状況
				self.DescriptionOfFactThatQuarterlySecuritiesReportForFirstQuarterOrThirdQuarterPresentsStatementOfCashFlowsFinancialInformation = fact.value

			elif fact.concept.qname.localName == 'DescriptionOfFactThatQuarterlySecuritiesReportForFirstQuarterOrThirdQuarterPresentsConsolidatedStatementOfCashFlowsFinancialInformation': #第１四半期又は第３四半期に係る四半期報告書において四半期連結キャッシュ・フロー計算書を記載する場合の記載、経理の状況
				self.DescriptionOfFactThatQuarterlySecuritiesReportForFirstQuarterOrThirdQuarterPresentsConsolidatedStatementOfCashFlowsFinancialInformation = fact.value

			elif fact.concept.qname.localName == 'DescriptionOfFactThatQuarterlySecuritiesReportPresentsQuarterPeriodStatementOfIncomeFinancialInformation': #四半期報告書において四半期会計期間に係る四半期損益計算書を記載する場合の記載、経理の状況
				self.DescriptionOfFactThatQuarterlySecuritiesReportPresentsQuarterPeriodStatementOfIncomeFinancialInformation = fact.value

			elif fact.concept.qname.localName == 'DescriptionOfFactThatQuarterlySecuritiesReportPresentsQuarterPeriodConsolidatedStatementOfComprehensiveIncomeFinancialInformation': #四半期報告書において四半期連結会計期間に係る四半期連結損益計算書及び四半期連結包括利益計算書又は四半期連結損益及び包括利益計算書を記載する場合の記載、経理の状況
				self.DescriptionOfFactThatQuarterlySecuritiesReportPresentsQuarterPeriodConsolidatedStatementOfComprehensiveIncomeFinancialInformation = fact.value

			elif fact.concept.qname.localName == 'RemarkableEffortsToEnsureFairPresentationOfConsolidatedFinancialStatementsEtcFinancialInformation': #連結財務諸表等の適正性を確保するための特段の取組み、経理の状況
				self.RemarkableEffortsToEnsureFairPresentationOfConsolidatedFinancialStatementsEtcFinancialInformation = fact.value

			elif fact.concept.qname.localName == 'RemarkableEffortsToEnsureFairPresentationOfConsolidatedFinancialStatementsEtcInAccordanceWithIFRSFinancialInformation': #指定国際会計基準に基づいて連結財務諸表等を適正に作成することができる体制、経理の状況
				self.RemarkableEffortsToEnsureFairPresentationOfConsolidatedFinancialStatementsEtcInAccordanceWithIFRSFinancialInformation = fact.value

			elif fact.concept.qname.localName == 'RemarkableEffortsToEnsureFairPresentationOfConsolidatedFinancialStatementsEtcAndInternalSystemToPrepareConsolidatedFinancialStatementsEtcFairlyInAccordanceWithIFRSFinancialInformation': #連結財務諸表等の適正性を確保するための特段の取組み及び指定国際会計基準に基づいて連結財務諸表等を適正に作成することができる体制、経理の状況
				self.RemarkableEffortsToEnsureFairPresentationOfConsolidatedFinancialStatementsEtcAndInternalSystemToPrepareConsolidatedFinancialStatementsEtcFairlyInAccordanceWithIFRSFinancialInformation = fact.value

			elif fact.concept.qname.localName == 'RemarkableEffortsToEnsureFairPresentationOfConsolidatedFinancialStatementsEtcInAccordanceWithJMISFinancialInformation': #修正国際基準に基づいて連結財務諸表等を適正に作成することができる体制、経理の状況
				self.RemarkableEffortsToEnsureFairPresentationOfConsolidatedFinancialStatementsEtcInAccordanceWithJMISFinancialInformation = fact.value

			elif fact.concept.qname.localName == 'NoteOnIndependentAuditFinancialInformation': #監査証明について、経理の状況
				self.NoteOnIndependentAuditFinancialInformation = fact.value

			elif fact.concept.qname.localName == 'NoteOnChangeOfIndependentAuditorsFinancialInformation': #監査人の交代、経理の状況
				self.NoteOnChangeOfIndependentAuditorsFinancialInformation = fact.value

			elif fact.concept.qname.localName == 'NoteOnChangeInFiscalYearEndsFinancialInformation': #決算期変更について、経理の状況
				self.NoteOnChangeInFiscalYearEndsFinancialInformation = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedFinancialStatementsEtcHeading': #連結財務諸表等 [目次項目]
				self.ConsolidatedFinancialStatementsEtcHeading = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedFinancialStatementsHeading': #連結財務諸表 [目次項目]
				self.ConsolidatedFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedBalanceSheetHeading': #連結貸借対照表 [目次項目]
				self.ConsolidatedBalanceSheetHeading = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedBalanceSheetTextBlock': #連結貸借対照表 [テキストブロック]
				self.ConsolidatedBalanceSheetTextBlock = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedStatementOfFinancialPositionJMISTextBlock': #連結財政状態計算書（JMIS） [テキストブロック]
				self.ConsolidatedStatementOfFinancialPositionJMISTextBlock = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedBalanceSheetUSGAAPTextBlock': #連結貸借対照表 （US GAAP） [テキストブロック]
				self.ConsolidatedBalanceSheetUSGAAPTextBlock = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedStatementOfIncomeAndConsolidatedStatementOfComprehensiveIncomeHeading': #連結損益計算書及び連結包括利益計算書 [目次項目]
				self.ConsolidatedStatementOfIncomeAndConsolidatedStatementOfComprehensiveIncomeHeading = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedStatementOfIncomeHeading': #連結損益計算書 [目次項目]
				self.ConsolidatedStatementOfIncomeHeading = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedStatementOfIncomeTextBlock': #連結損益計算書 [テキストブロック]
				self.ConsolidatedStatementOfIncomeTextBlock = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedStatementOfIncomeJMISTextBlock': #連結損益計算書（JMIS） [テキストブロック]
				self.ConsolidatedStatementOfIncomeJMISTextBlock = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedStatementOfIncomeUSGAAPTextBlock': #連結損益計算書（US GAAP） [テキストブロック]
				self.ConsolidatedStatementOfIncomeUSGAAPTextBlock = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedStatementOfComprehensiveIncomeHeading': #連結包括利益計算書 [目次項目]
				self.ConsolidatedStatementOfComprehensiveIncomeHeading = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedStatementOfComprehensiveIncomeTextBlock': #連結包括利益計算書 [テキストブロック]
				self.ConsolidatedStatementOfComprehensiveIncomeTextBlock = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedStatementOfComprehensiveIncomeJMISTextBlock': #連結包括利益計算書（2計算書）（JMIS） [テキストブロック]
				self.ConsolidatedStatementOfComprehensiveIncomeJMISTextBlock = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedStatementOfComprehensiveIncomeUSGAAPTextBlock': #連結包括利益計算書（US GAAP） [テキストブロック]
				self.ConsolidatedStatementOfComprehensiveIncomeUSGAAPTextBlock = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedStatementOfComprehensiveIncomeSingleStatementHeading': #連結損益及び包括利益計算書 [目次項目]
				self.ConsolidatedStatementOfComprehensiveIncomeSingleStatementHeading = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedStatementOfComprehensiveIncomeSingleStatementTextBlock': #連結損益及び包括利益計算書 [テキストブロック]
				self.ConsolidatedStatementOfComprehensiveIncomeSingleStatementTextBlock = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedStatementOfComprehensiveIncomeSingleStatementJMISTextBlock': #連結包括利益計算書（１計算書）（JMIS） [テキストブロック]
				self.ConsolidatedStatementOfComprehensiveIncomeSingleStatementJMISTextBlock = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedStatementOfComprehensiveIncomeSingleStatementUSGAAPTextBlock': #連結損益及び包括利益計算書（US GAAP） [テキストブロック]
				self.ConsolidatedStatementOfComprehensiveIncomeSingleStatementUSGAAPTextBlock = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedStatementOfChangesInEquityHeading': #連結株主資本等変動計算書 [目次項目]
				self.ConsolidatedStatementOfChangesInEquityHeading = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedStatementOfChangesInEquityTextBlock': #連結株主資本等変動計算書 [テキストブロック]
				self.ConsolidatedStatementOfChangesInEquityTextBlock = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedStatementOfChangesInEquityJMISTextBlock': #連結持分変動計算書（JMIS） [テキストブロック]
				self.ConsolidatedStatementOfChangesInEquityJMISTextBlock = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedStatementOfEquityUSGAAPTextBlock': #連結資本勘定計算書（US GAAP） [テキストブロック]
				self.ConsolidatedStatementOfEquityUSGAAPTextBlock = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedStatementOfCashFlowsHeading': #連結キャッシュ・フロー計算書 [目次項目]
				self.ConsolidatedStatementOfCashFlowsHeading = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedStatementOfCashFlowsTextBlock': #連結キャッシュ・フロー計算書 [テキストブロック]
				self.ConsolidatedStatementOfCashFlowsTextBlock = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedStatementOfCashFlowsJMISTextBlock': #連結キャッシュ・フロー計算書（JMIS） [テキストブロック]
				self.ConsolidatedStatementOfCashFlowsJMISTextBlock = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedStatementOfCashFlowsUSGAAPTextBlock': #連結キャッシュ・フロー計算書（US GAAP） [テキストブロック]
				self.ConsolidatedStatementOfCashFlowsUSGAAPTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesConsolidatedFinancialStatementsHeading': #注記事項、連結財務諸表 [目次項目]
				self.NotesConsolidatedFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesUncertaintiesOfEntitysAbilityToContinueAsGoingConcernConsolidatedFinancialStatementsHeading': #継続企業の前提に関する事項、連結財務諸表 [目次項目]
				self.NotesUncertaintiesOfEntitysAbilityToContinueAsGoingConcernConsolidatedFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesUncertaintiesOfEntitysAbilityToContinueAsGoingConcernConsolidatedFinancialStatementsTextBlock': #継続企業の前提に関する事項、連結財務諸表 [テキストブロック]
				self.NotesUncertaintiesOfEntitysAbilityToContinueAsGoingConcernConsolidatedFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesSignificantAccountingPoliciesForPreparationOfConsolidatedFinancialStatementsHeading': #連結財務諸表作成のための基本となる重要な事項 [目次項目]
				self.NotesSignificantAccountingPoliciesForPreparationOfConsolidatedFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesSignificantAccountingPoliciesForPreparationOfConsolidatedFinancialStatementsTextBlock': #連結財務諸表作成のための基本となる重要な事項 [テキストブロック]
				self.NotesSignificantAccountingPoliciesForPreparationOfConsolidatedFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesSignificantAccountingPoliciesForPreparationOfConsolidatedFinancialStatementsHeading': #連結財務諸表作成のための基本となる重要な事項 [目次項目]
				self.NotesSignificantAccountingPoliciesForPreparationOfConsolidatedFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesSignificantAccountingPoliciesForPreparationOfConsolidatedFinancialStatementsTable': #連結財務諸表作成のための基本となる重要な事項 [表]
				self.NotesSignificantAccountingPoliciesForPreparationOfConsolidatedFinancialStatementsTable = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedOrNonConsolidatedAxis': #連結個別 [軸]
				self.ConsolidatedOrNonConsolidatedAxis = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedMember': #連結 [メンバー] ※ディメンションデフォルト
				self.ConsolidatedMember = fact.value

			elif fact.concept.qname.localName == 'NotesSignificantAccountingPoliciesForPreparationOfConsolidatedFinancialStatementsLineItems': #連結財務諸表作成のための基本となる重要な事項 [表示項目]
				self.NotesSignificantAccountingPoliciesForPreparationOfConsolidatedFinancialStatementsLineItems = fact.value

			elif fact.concept.qname.localName == 'DisclosureOfScopeOfConsolidationAbstract': #連結の範囲に関する事項 [タイトル項目]
				self.DisclosureOfScopeOfConsolidationAbstract = fact.value

			elif fact.concept.qname.localName == 'NumberOfConsolidatedSubsidiariesAndNamesOfMajorConsolidatedSubsidiariesTextBlock': #連結子会社の数及び主要な連結子会社の名称 [テキストブロック]
				self.NumberOfConsolidatedSubsidiariesAndNamesOfMajorConsolidatedSubsidiariesTextBlock = fact.value

			elif fact.concept.qname.localName == 'NumberOfConsolidatedSubsidiaries': #連結子会社の数
				self.NumberOfConsolidatedSubsidiaries = fact.value

			elif fact.concept.qname.localName == 'ChangesInScopeOfConsolidationTextBlock': #連結の範囲の変更 [テキストブロック]
				self.ChangesInScopeOfConsolidationTextBlock = fact.value

			elif fact.concept.qname.localName == 'NamesOfMajorUnconsolidatedSubsidiariesAndReasonsForExclusionFromScopeOfConsolidationTextBlock': #主要な非連結子会社の名称及び連結の範囲から除いた理由 [テキストブロック]
				self.NamesOfMajorUnconsolidatedSubsidiariesAndReasonsForExclusionFromScopeOfConsolidationTextBlock = fact.value

			elif fact.concept.qname.localName == 'NamesOfCompaniesEtcAndReasonsForNotBeingDeemedAsSubsidiariesEvenThoughMoreThanHalfOfVotingRightsAreOwnedByReportingCompanyTextBlock': #他の会社等の議決権の過半数を自己の計算において所有しているにもかかわらず当該他の会社等を子会社としなかった場合には、当該他の会社等の名称及び子会社としなかった理由 [テキストブロック]
				self.NamesOfCompaniesEtcAndReasonsForNotBeingDeemedAsSubsidiariesEvenThoughMoreThanHalfOfVotingRightsAreOwnedByReportingCompanyTextBlock = fact.value

			elif fact.concept.qname.localName == 'SummaryOfSpecialPurposeEntitiesSubjectToDisclosureOverviewAndAmountsOfTransactionsWithSuchEntitiesAndOtherRelevantMaterialInformationTextBlock': #開示対象特別目的会社の概要、開示対象特別目的会社との取引の概要及び取引金額その他の重要な事項 [テキストブロック]
				self.SummaryOfSpecialPurposeEntitiesSubjectToDisclosureOverviewAndAmountsOfTransactionsWithSuchEntitiesAndOtherRelevantMaterialInformationTextBlock = fact.value

			elif fact.concept.qname.localName == 'DisclosureAboutApplicationOfEquityMethodAbstract': #持分法の適用に関する事項 [タイトル項目]
				self.DisclosureAboutApplicationOfEquityMethodAbstract = fact.value

			elif fact.concept.qname.localName == 'NumberOfUnconsolidatedSubsidiariesAndAssociatesAccountedForUsingEquityMethodAndNamesOfMajorEntitiesAccountedForUsingEquityMethodTextBlock': #持分法を適用した非連結子会社又は関連会社の数及びこれらのうち主要な会社等の名称 [テキストブロック]
				self.NumberOfUnconsolidatedSubsidiariesAndAssociatesAccountedForUsingEquityMethodAndNamesOfMajorEntitiesAccountedForUsingEquityMethodTextBlock = fact.value

			elif fact.concept.qname.localName == 'NumberOfUnconsolidatedSubsidiariesAndAssociatesAccountedForUsingEquityMethod': #持分法を適用した非連結子会社又は関連会社の数
				self.NumberOfUnconsolidatedSubsidiariesAndAssociatesAccountedForUsingEquityMethod = fact.value

			elif fact.concept.qname.localName == 'ChangesInScopeOfApplicationOfEquityMethodTextBlock': #持分法適用の範囲の変更 [テキストブロック]
				self.ChangesInScopeOfApplicationOfEquityMethodTextBlock = fact.value

			elif fact.concept.qname.localName == 'NumberOfUnconsolidatedSubsidiariesAccountedForUsingEquityMethod': #持分法を適用した非連結子会社の数
				self.NumberOfUnconsolidatedSubsidiariesAccountedForUsingEquityMethod = fact.value

			elif fact.concept.qname.localName == 'ChangesInScopeOfApplicationOfEquityMethodUnconsolidatedSubsidiariesTextBlock': #持分法適用の範囲の変更－非連結子会社 [テキストブロック]
				self.ChangesInScopeOfApplicationOfEquityMethodUnconsolidatedSubsidiariesTextBlock = fact.value

			elif fact.concept.qname.localName == 'NumberOfAssociatesAccountedForUsingEquityMethod': #持分法を適用した関連会社の数
				self.NumberOfAssociatesAccountedForUsingEquityMethod = fact.value

			elif fact.concept.qname.localName == 'ChangesInScopeOfApplicationOfEquityMethodAssociatesTextBlock': #持分法適用の範囲の変更－関連会社 [テキストブロック]
				self.ChangesInScopeOfApplicationOfEquityMethodAssociatesTextBlock = fact.value

			elif fact.concept.qname.localName == 'NamesOfMajorUnconsolidatedSubsidiariesAndAssociatesAndReasonsForNotBeingAccountedForUsingEquityMethodTextBlock': #持分法を適用しない非連結子会社又は関連会社がある場合には、これらのうち主要な会社等の名称及び持分法を適用しない理由 [テキストブロック]
				self.NamesOfMajorUnconsolidatedSubsidiariesAndAssociatesAndReasonsForNotBeingAccountedForUsingEquityMethodTextBlock = fact.value

			elif fact.concept.qname.localName == 'NamesOfCompaniesEtcAndReasonsForNotBeingDeemedAsAssociatesEvenThoughMoreThan20PerCentAndLessThanHalfOfVotingRightsAreOwnedByReportingCompanyTextBlock': #他の会社等の議決権の百分の二十以上、百分の五十以下を自己の計算において所有しているにもかかわらず当該他の会社等を関連会社としなかった場合には、当該他の会社等の名称及び関連会社としなかった理由 [テキストブロック]
				self.NamesOfCompaniesEtcAndReasonsForNotBeingDeemedAsAssociatesEvenThoughMoreThan20PerCentAndLessThanHalfOfVotingRightsAreOwnedByReportingCompanyTextBlock = fact.value

			elif fact.concept.qname.localName == 'OtherSpecificInformationIfDeemedNecessaryAboutApplicationOfEquityMethodTextBlock': #持分法の適用の手続について特に記載する必要があると認められる事項がある場合には、その内容 [テキストブロック]
				self.OtherSpecificInformationIfDeemedNecessaryAboutApplicationOfEquityMethodTextBlock = fact.value

			elif fact.concept.qname.localName == 'DisclosureAboutFiscalYearsEtcOfConsolidatedSubsidiariesTextBlock': #連結子会社の事業年度等に関する事項 [テキストブロック]
				self.DisclosureAboutFiscalYearsEtcOfConsolidatedSubsidiariesTextBlock = fact.value

			elif fact.concept.qname.localName == 'DisclosureOfAccountingPoliciesAbstract': #会計処理基準に関する事項 [タイトル項目]
				self.DisclosureOfAccountingPoliciesAbstract = fact.value

			elif fact.concept.qname.localName == 'DisclosureOfAccountingPoliciesTextBlock': #会計方針に関する事項 [テキストブロック]
				self.DisclosureOfAccountingPoliciesTextBlock = fact.value

			elif fact.concept.qname.localName == 'SignificantAccountingEstimatesConsolidatedFinancialStatementsHeading': #重要な会計上の見積り、連結財務諸表 [目次項目]
				self.SignificantAccountingEstimatesConsolidatedFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'SignificantAccountingEstimatesConsolidatedFinancialStatementsTextBlock': #重要な会計上の見積り、連結財務諸表 [テキストブロック]
				self.SignificantAccountingEstimatesConsolidatedFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesChangesInAccountingPoliciesConsolidatedFinancialStatementsHeading': #会計方針の変更、連結財務諸表 [目次項目]
				self.NotesChangesInAccountingPoliciesConsolidatedFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesChangesInAccountingPoliciesInAccordanceWithChangesInAccountingStandardsEtcConsolidatedFinancialStatementsTextBlock': #会計基準等の改正等に伴う会計方針の変更、連結財務諸表 [テキストブロック]
				self.NotesChangesInAccountingPoliciesInAccordanceWithChangesInAccountingStandardsEtcConsolidatedFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesVoluntaryChangesInAccountingPoliciesConsolidatedFinancialStatementsTextBlock': #会計基準等の改正等以外の正当な理由による会計方針の変更、連結財務諸表 [テキストブロック]
				self.NotesVoluntaryChangesInAccountingPoliciesConsolidatedFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesChangesInAccountingPoliciesWhichAreDifficultToDistinguishFromChangesInAccountingEstimatesConsolidatedFinancialStatementsTextBlock': #会計上の見積りの変更と区別することが困難な会計方針の変更、連結財務諸表 [テキストブロック]
				self.NotesChangesInAccountingPoliciesWhichAreDifficultToDistinguishFromChangesInAccountingEstimatesConsolidatedFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesNewAccountingStandardsNotYetAppliedConsolidatedFinancialStatementsHeading': #未適用の会計基準等、連結財務諸表 [目次項目]
				self.NotesNewAccountingStandardsNotYetAppliedConsolidatedFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesNewAccountingStandardsNotYetAppliedConsolidatedFinancialStatementsTextBlock': #未適用の会計基準等、連結財務諸表 [テキストブロック]
				self.NotesNewAccountingStandardsNotYetAppliedConsolidatedFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesChangesInPresentationConsolidatedFinancialStatementsHeading': #表示方法の変更、連結財務諸表 [目次項目]
				self.NotesChangesInPresentationConsolidatedFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesChangesInPresentationConsolidatedFinancialStatementsTextBlock': #表示方法の変更、連結財務諸表 [テキストブロック]
				self.NotesChangesInPresentationConsolidatedFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesChangesInAccountingEstimatesConsolidatedFinancialStatementsHeading': #会計上の見積りの変更、連結財務諸表 [目次項目]
				self.NotesChangesInAccountingEstimatesConsolidatedFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesChangesInAccountingEstimatesConsolidatedFinancialStatementsTextBlock': #会計上の見積りの変更、連結財務諸表 [テキストブロック]
				self.NotesChangesInAccountingEstimatesConsolidatedFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRestatementConsolidatedFinancialStatementsHeading': #修正再表示、連結財務諸表 [目次項目]
				self.NotesRestatementConsolidatedFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesRestatementConsolidatedFinancialStatementsTextBlock': #修正再表示、連結財務諸表 [テキストブロック]
				self.NotesRestatementConsolidatedFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesAdditionalInformationConsolidatedFinancialStatementsHeading': #追加情報、連結財務諸表 [目次項目]
				self.NotesAdditionalInformationConsolidatedFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesAdditionalInformationConsolidatedFinancialStatementsTextBlock': #追加情報、連結財務諸表 [テキストブロック]
				self.NotesAdditionalInformationConsolidatedFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesConsolidatedBalanceSheetHeading': #連結貸借対照表関係 [目次項目]
				self.NotesConsolidatedBalanceSheetHeading = fact.value

			elif fact.concept.qname.localName == 'NotesConsolidatedBalanceSheetHeading': #連結貸借対照表関係 [目次項目]
				self.NotesConsolidatedBalanceSheetHeading = fact.value

			elif fact.concept.qname.localName == 'NotesConsolidatedBalanceSheetTable': #連結貸借対照表関係 [表]
				self.NotesConsolidatedBalanceSheetTable = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedOrNonConsolidatedAxis': #連結個別 [軸]
				self.ConsolidatedOrNonConsolidatedAxis = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedMember': #連結 [メンバー] ※ディメンションデフォルト
				self.ConsolidatedMember = fact.value

			elif fact.concept.qname.localName == 'NotesConsolidatedBalanceSheetLineItems': #連結貸借対照表関係 [表示項目]
				self.NotesConsolidatedBalanceSheetLineItems = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingInventoriesTextBlock': #棚卸資産の内訳の注記 [テキストブロック]
				self.NotesRegardingInventoriesTextBlock = fact.value

			elif fact.concept.qname.localName == 'MerchandiseAndFinishedGoods': #商品及び製品
				self.MerchandiseAndFinishedGoods = fact.value

			elif fact.concept.qname.localName == 'WorkInProcess': #仕掛品
				self.WorkInProcess = fact.value

			elif fact.concept.qname.localName == 'RawMaterialsAndSupplies': #原材料及び貯蔵品
				self.RawMaterialsAndSupplies = fact.value

			elif fact.concept.qname.localName == 'Inventories': #棚卸資産
				self.Inventories = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingAmountsOfNotesAndAccountsReceivableTradeAndContractAssetsTextBlock': #受取手形、売掛金及び契約資産の金額の注記 [テキストブロック]
				self.NotesRegardingAmountsOfNotesAndAccountsReceivableTradeAndContractAssetsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesReceivableTrade': #受取手形
				self.NotesReceivableTrade = fact.value

			elif fact.concept.qname.localName == 'AllowanceForDoubtfulAccountsNotesReceivableTrade': #貸倒引当金、受取手形
				self.AllowanceForDoubtfulAccountsNotesReceivableTrade = fact.value

			elif fact.concept.qname.localName == 'NotesReceivableTradeNet': #受取手形（純額）
				self.NotesReceivableTradeNet = fact.value

			elif fact.concept.qname.localName == 'AccountsReceivableTrade': #売掛金
				self.AccountsReceivableTrade = fact.value

			elif fact.concept.qname.localName == 'AllowanceForDoubtfulAccountsAccountsReceivableTrade': #貸倒引当金、売掛金
				self.AllowanceForDoubtfulAccountsAccountsReceivableTrade = fact.value

			elif fact.concept.qname.localName == 'AccountsReceivableTradeNet': #売掛金（純額）
				self.AccountsReceivableTradeNet = fact.value

			elif fact.concept.qname.localName == 'ContractAssets': #契約資産
				self.ContractAssets = fact.value

			elif fact.concept.qname.localName == 'AllowanceForDoubtfulAccountsContractAssets': #貸倒引当金、契約資産
				self.AllowanceForDoubtfulAccountsContractAssets = fact.value

			elif fact.concept.qname.localName == 'ContractAssetsNet': #契約資産（純額）
				self.ContractAssetsNet = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingAllowancesDirectlyDeductedFromBalancesOfAssetsTextBlock': #資産の金額から直接控除している引当金の注記 [テキストブロック]
				self.NotesRegardingAllowancesDirectlyDeductedFromBalancesOfAssetsTextBlock = fact.value

			elif fact.concept.qname.localName == 'AllowanceForDoubtfulAccountsCA': #貸倒引当金、流動資産、一括控除
				self.AllowanceForDoubtfulAccountsCA = fact.value

			elif fact.concept.qname.localName == 'AllowanceForDoubtfulAccountsIOAByGroup': #貸倒引当金、投資その他の資産、一括控除
				self.AllowanceForDoubtfulAccountsIOAByGroup = fact.value

			elif fact.concept.qname.localName == 'AllowanceForDoubtfulAccountsAccountsReceivableTrade': #貸倒引当金、売掛金
				self.AllowanceForDoubtfulAccountsAccountsReceivableTrade = fact.value

			elif fact.concept.qname.localName == 'AllowanceForDoubtfulAccountsLongTermLoansReceivable': #貸倒引当金、長期貸付金
				self.AllowanceForDoubtfulAccountsLongTermLoansReceivable = fact.value

			elif fact.concept.qname.localName == 'AllowanceForDoubtfulAccountsClaimsInBankruptcyReorganizationClaimsAndOther': #貸倒引当金、破産更生債権等
				self.AllowanceForDoubtfulAccountsClaimsInBankruptcyReorganizationClaimsAndOther = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingAccumulatedDepreciationOfPropertyPlantAndEquipmentTextBlock': #有形固定資産の減価償却累計額の注記 [テキストブロック]
				self.NotesRegardingAccumulatedDepreciationOfPropertyPlantAndEquipmentTextBlock = fact.value

			elif fact.concept.qname.localName == 'AccumulatedDepreciationPPEByGroup': #減価償却累計額、有形固定資産、一括控除
				self.AccumulatedDepreciationPPEByGroup = fact.value

			elif fact.concept.qname.localName == 'AccumulatedDepreciationBuildings': #減価償却累計額、建物
				self.AccumulatedDepreciationBuildings = fact.value

			elif fact.concept.qname.localName == 'AccumulatedDepreciationStructures': #減価償却累計額、構築物
				self.AccumulatedDepreciationStructures = fact.value

			elif fact.concept.qname.localName == 'AccumulatedDepreciationMachineryAndEquipment': #減価償却累計額、機械及び装置
				self.AccumulatedDepreciationMachineryAndEquipment = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingAmountsOfReductionEntryOfPropertyPlantAndEquipmentTextBlock': #有形固定資産の圧縮記帳額の注記 [テキストブロック]
				self.NotesRegardingAmountsOfReductionEntryOfPropertyPlantAndEquipmentTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingPresentationOfAccumulatedImpairmentLossTextBlock': #減損損失累計額の表示に関する注記 [テキストブロック]
				self.NotesRegardingPresentationOfAccumulatedImpairmentLossTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingSharesAndBondsEtcOfUnconsolidatedSubsidiariesAndAssociatesTextBlock': #非連結子会社及び関連会社の株式及び社債等 [テキストブロック]
				self.NotesRegardingSharesAndBondsEtcOfUnconsolidatedSubsidiariesAndAssociatesTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingRevaluationOfLandForBusinessTextBlock': #事業用土地の再評価に関する注記 [テキストブロック]
				self.NotesRegardingRevaluationOfLandForBusinessTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingPledgedAssetsTextBlock': #担保に供している資産の注記 [テキストブロック]
				self.NotesRegardingPledgedAssetsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingAmountOfContractLiabilitiesTextBlock': #契約負債の金額の注記 [テキストブロック]
				self.NotesRegardingAmountOfContractLiabilitiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'ContractLiabilities': #契約負債
				self.ContractLiabilities = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingPresentationOfGoodwillAndNegativeGoodwillTextBlock': #のれん及び負ののれんの表示に関する注記 [テキストブロック]
				self.NotesRegardingPresentationOfGoodwillAndNegativeGoodwillTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingPresentationOfInventoriesAndProvisionForLossOnConstructionContractsTextBlock': #棚卸資産及び工事損失引当金の表示に関する注記 [テキストブロック]
				self.NotesRegardingPresentationOfInventoriesAndProvisionForLossOnConstructionContractsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingReservesUnderSpecialLawsTextBlock': #特別法上の準備金等に関する注記 [テキストブロック]
				self.NotesRegardingReservesUnderSpecialLawsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingProvisionIncurredFromBusinessCombinationTextBlock': #企業結合に係る特定勘定の注記 [テキストブロック]
				self.NotesRegardingProvisionIncurredFromBusinessCombinationTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingGuaranteeObligationsTextBlock': #保証債務の注記 [テキストブロック]
				self.NotesRegardingGuaranteeObligationsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingTradeNotesReceivableDiscountedOrTransferredByEndorsementTextBlock': #受取手形割引高及び（又は）受取手形裏書譲渡高 [テキストブロック]
				self.NotesRegardingTradeNotesReceivableDiscountedOrTransferredByEndorsementTextBlock = fact.value

			elif fact.concept.qname.localName == 'DiscountedTradeNotesReceivable': #受取手形割引高
				self.DiscountedTradeNotesReceivable = fact.value

			elif fact.concept.qname.localName == 'TradeNotesReceivableTransferredByEndorsement': #受取手形裏書譲渡高
				self.TradeNotesReceivableTransferredByEndorsement = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingLiabilitiesEtcOfSpecialPurposeEntitiesTextBlock': #特別目的会社の債務等に関する注記 [テキストブロック]
				self.NotesRegardingLiabilitiesEtcOfSpecialPurposeEntitiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingReservesRequiredByContractsTextBlock': #契約による積立金の注記 [テキストブロック]
				self.NotesRegardingReservesRequiredByContractsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingPresentationOfNetAssetsOfDesignatedCorporationTextBlock': #指定法人の純資産の記載に関する注記 [テキストブロック]
				self.NotesRegardingPresentationOfNetAssetsOfDesignatedCorporationTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingClassificationOfAssetsAndLiabilitiesOfIndustryInAppendedListTextBlock': #別記事業の資産及び負債の分類に関する注記 [テキストブロック]
				self.NotesRegardingClassificationOfAssetsAndLiabilitiesOfIndustryInAppendedListTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingPromissoryNotesDueOnBalanceSheetDateTextBlock': #期末日満期手形の会計処理 [テキストブロック]
				self.NotesRegardingPromissoryNotesDueOnBalanceSheetDateTextBlock = fact.value

			elif fact.concept.qname.localName == 'OtherElementsForNotesBalanceSheetAbstract': #貸借対照表関係のその他の要素 [タイトル項目]
				self.OtherElementsForNotesBalanceSheetAbstract = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingLoanedWhichBorrowerHasRightToSellOrRepledgeTextBlock': #消費貸借契約及び（又は）消費寄託契約により貸し付けている有価証券に関する注記 [テキストブロック]
				self.NotesRegardingLoanedWhichBorrowerHasRightToSellOrRepledgeTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingFinancialAssetsBorrowedWhichBorrowerHasRightToSellOrRepledgeTextBlock': #自由処分権を有する担保受入金融資産に関する注記 [テキストブロック]
				self.NotesRegardingFinancialAssetsBorrowedWhichBorrowerHasRightToSellOrRepledgeTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingLoanedSecuritiesAndFinancialAssetsBorrowedWhichBorrowerHasRightToSellOrRepledgeTextBlock': #有価証券の消費貸借契約・消費寄託契約及び自由処分権を有する担保受入金融資産に関する注記 [テキストブロック]
				self.NotesRegardingLoanedSecuritiesAndFinancialAssetsBorrowedWhichBorrowerHasRightToSellOrRepledgeTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingLoanParticipationsTextBlock': #ローン・パーティシペーションに関する注記 [テキストブロック]
				self.NotesRegardingLoanParticipationsTextBlock = fact.value

			elif fact.concept.qname.localName == 'CreditorsNotesRegardingOverdraftContractsAndOrLoanCommitmentsTextBlock': #当座貸越契約及び（又は）貸出コミットメントに関する貸手の注記 [テキストブロック]
				self.CreditorsNotesRegardingOverdraftContractsAndOrLoanCommitmentsTextBlock = fact.value

			elif fact.concept.qname.localName == 'DebtorsNotesRegardingOverdraftContractsAndOrLoanCommitmentsTextBlock': #当座貸越契約及び（又は）貸出コミットメントに関する借手の注記 [テキストブロック]
				self.DebtorsNotesRegardingOverdraftContractsAndOrLoanCommitmentsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingTotalAmountsOfSharesOfAndOrLoansToAffiliatedEntitiesTextBlock': #関係会社の株式及び（又は）出資金の総額 [テキストブロック]
				self.NotesRegardingTotalAmountsOfSharesOfAndOrLoansToAffiliatedEntitiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingTotalAmountsOfSharesOfAndOrLoansToUnconsolidatedSubsidiariesAndAssociatesTextBlock': #非連結子会社及び関連会社の株式及び（又は）出資金の総額 [テキストブロック]
				self.NotesRegardingTotalAmountsOfSharesOfAndOrLoansToUnconsolidatedSubsidiariesAndAssociatesTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingSubordinatedBorrowingsTextBlock': #劣後特約付借入金に関する注記 [テキストブロック]
				self.NotesRegardingSubordinatedBorrowingsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingSubordinatedBondsPayableTextBlock': #劣後特約付社債に関する注記 [テキストブロック]
				self.NotesRegardingSubordinatedBondsPayableTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingGuaranteeObligationForCorporateBondsIncludedInAssetsTextBlock': #資産の部の社債に係る保証債務に関する注記 [テキストブロック]
				self.NotesRegardingGuaranteeObligationForCorporateBondsIncludedInAssetsTextBlock = fact.value

			elif fact.concept.qname.localName == 'OtherElementsForNotesBalanceSheetOfBankAbstract': #銀行業の貸借対照表関係のその他の要素 [タイトル項目]
				self.OtherElementsForNotesBalanceSheetOfBankAbstract = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingLoansBasedOnBankingActAndActOnEmergencyMeasuresForRevitalizationOfFinancialFunctionsBNKTextBlock': #銀行法及び金融機能の再生のための緊急措置に関する法律に基づく債権に関する注記、銀行業 [テキストブロック]
				self.NotesRegardingLoansBasedOnBankingActAndActOnEmergencyMeasuresForRevitalizationOfFinancialFunctionsBNKTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingBillsDiscountedInBankingIndustryBNKTextBlock': #銀行業における手形割引に関する注記、銀行業 [テキストブロック]
				self.NotesRegardingBillsDiscountedInBankingIndustryBNKTextBlock = fact.value

			elif fact.concept.qname.localName == 'OtherElementsForNotesBalanceSheetOfSecuritiesRelatedBusinessAbstract': #第一種金融商品取引業の貸借対照表関係のその他の要素 [タイトル項目]
				self.OtherElementsForNotesBalanceSheetOfSecuritiesRelatedBusinessAbstract = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingMarketValueOfSecuritiesPledgedToCounterpartiesSECTextBlock': #差し入れた有価証券等の時価の注記、第一種金融商品取引業 [テキストブロック]
				self.NotesRegardingMarketValueOfSecuritiesPledgedToCounterpartiesSECTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingMarketValueOfSecuritiesReceivedAsCollateralFromCounterpartiesSECTextBlock': #差し入れを受けた有価証券等の時価の注記、第一種金融商品取引業 [テキストブロック]
				self.NotesRegardingMarketValueOfSecuritiesReceivedAsCollateralFromCounterpartiesSECTextBlock = fact.value

			elif fact.concept.qname.localName == 'BreakdownOfTradingAccountSecuritiesEtcSECTextBlock': #商品有価証券等の内訳、第一種金融商品取引業 [テキストブロック]
				self.BreakdownOfTradingAccountSecuritiesEtcSECTextBlock = fact.value

			elif fact.concept.qname.localName == 'OtherElementsForNotesBalanceSheetOfInsuranceAbstract': #保険業の貸借対照表関係のその他の要素 [タイトル項目]
				self.OtherElementsForNotesBalanceSheetOfInsuranceAbstract = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingLoansBasedOnInsuranceBusinessActINSTextBlock': #保険業法に基づく債権に関する注記、保険業 [テキストブロック]
				self.NotesRegardingLoansBasedOnInsuranceBusinessActINSTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingAssetsAndLiabilitiesIncludedInSpecificAccountsSpecifiedByArticle118OfInsuranceBusinessActINSTextBlock': #保険業法第118条に規定する特別勘定の資産及び負債に関する注記、保険業 [テキストブロック]
				self.NotesRegardingAssetsAndLiabilitiesIncludedInSpecificAccountsSpecifiedByArticle118OfInsuranceBusinessActINSTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingDeferredAssetsIncludedInOtherAssetsSpecifiedByArticle113OfInsuranceBusinessActTextBlock': #その他資産に含まれている保険業法第113条に規定する事業費の繰延額の注記 [テキストブロック]
				self.NotesRegardingDeferredAssetsIncludedInOtherAssetsSpecifiedByArticle113OfInsuranceBusinessActTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingIncreaseAndDecreaseInReserveForPolicyholderDividendsAndPaymentsOfPolicyholderDividendsINSTextBlock': #契約者配当準備金の増減異動及び契約者配当金の支払額に関する注記、保険業 [テキストブロック]
				self.NotesRegardingIncreaseAndDecreaseInReserveForPolicyholderDividendsAndPaymentsOfPolicyholderDividendsINSTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingSurplusFromOrganizationChangeSpecifiedByArticle91OfInsuranceBusinessActINSTextBlock': #保険業法第91条の規定による組織変更剰余金額の注記、保険業 [テキストブロック]
				self.NotesRegardingSurplusFromOrganizationChangeSpecifiedByArticle91OfInsuranceBusinessActINSTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingReservesForOutstandingClaimsReinsuredINSTextBlock': #保険業法施行規則第73条第3項において準用する同規則第71条第1項に規定する再保険を付した部分に相当する支払備金の金額の注記、保険業 [テキストブロック]
				self.NotesRegardingReservesForOutstandingClaimsReinsuredINSTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingPolicyReservesReinsuredINSTextBlock': #保険業法施行規則第71条第1項に規定する再保険を付した部分に相当する責任準備金の金額の注記、保険業 [テキストブロック]
				self.NotesRegardingPolicyReservesReinsuredINSTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingObligationsToLifeInsurancePolicyholdersProtectionCorporationOfJapanINSTextBlock': #保険業法第259条の規定に基づく生命保険契約者保護機構に対する今後の負担見積額、保険業 [テキストブロック]
				self.NotesRegardingObligationsToLifeInsurancePolicyholdersProtectionCorporationOfJapanINSTextBlock = fact.value

			elif fact.concept.qname.localName == 'BreakdownOfOutstandingClaimsINSTextBlock': #支払備金の内訳、保険業 [テキストブロック]
				self.BreakdownOfOutstandingClaimsINSTextBlock = fact.value

			elif fact.concept.qname.localName == 'BreakdownOfPolicyReserveINSTextBlock': #責任準備金の内訳、保険業 [テキストブロック]
				self.BreakdownOfPolicyReserveINSTextBlock = fact.value

			elif fact.concept.qname.localName == 'OtherElementsForNotesBalanceSheetOfSpecificFinanceAbstract': #特定金融業の貸借対照表関係のその他の要素 [タイトル項目]
				self.OtherElementsForNotesBalanceSheetOfSpecificFinanceAbstract = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingBadLoansSPFTextBlock': #不良債権に関する注記、特定金融業 [テキストブロック]
				self.NotesRegardingBadLoansSPFTextBlock = fact.value

			elif fact.concept.qname.localName == 'OtherElementsForNotesBalanceSheetOfCommodityFutureTradingAbstract': #商品先物取引業の貸借対照表関係のその他の要素 [タイトル項目]
				self.OtherElementsForNotesBalanceSheetOfCommodityFutureTradingAbstract = fact.value

			elif fact.concept.qname.localName == 'ExplanationOfFuturesTransactionMarginCustomerCMDTextBlock': #委託者先物取引差金の説明、商品先物取引業 [テキストブロック]
				self.ExplanationOfFuturesTransactionMarginCustomerCMDTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesConsolidatedStatementOfIncomeHeading': #連結損益計算書関係 [目次項目]
				self.NotesConsolidatedStatementOfIncomeHeading = fact.value

			elif fact.concept.qname.localName == 'NotesConsolidatedStatementOfIncomeHeading': #連結損益計算書関係 [目次項目]
				self.NotesConsolidatedStatementOfIncomeHeading = fact.value

			elif fact.concept.qname.localName == 'NotesConsolidatedStatementOfIncomeTable': #連結損益計算書関係 [表]
				self.NotesConsolidatedStatementOfIncomeTable = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedOrNonConsolidatedAxis': #連結個別 [軸]
				self.ConsolidatedOrNonConsolidatedAxis = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedMember': #連結 [メンバー] ※ディメンションデフォルト
				self.ConsolidatedMember = fact.value

			elif fact.concept.qname.localName == 'NotesConsolidatedStatementOfIncomeLineItems': #連結損益計算書関係 [表示項目]
				self.NotesConsolidatedStatementOfIncomeLineItems = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingAmountOfRevenueFromContractsWithCustomersTextBlock': #顧客との契約から生じる収益の金額の注記 [テキストブロック]
				self.NotesRegardingAmountOfRevenueFromContractsWithCustomersTextBlock = fact.value

			elif fact.concept.qname.localName == 'RevenueFromContractsWithCustomers': #顧客との契約から生じる収益
				self.RevenueFromContractsWithCustomers = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingLossOnConstructionContractsTextBlock': #工事損失引当金繰入額の注記 [テキストブロック]
				self.NotesRegardingLossOnConstructionContractsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingWriteDownsOfInventoriesTextBlock': #棚卸資産の帳簿価額の切下げに関する注記 [テキストブロック]
				self.NotesRegardingWriteDownsOfInventoriesTextBlock = fact.value

			elif fact.concept.qname.localName == 'WriteDownsOfInventories': #棚卸資産帳簿価額切下額
				self.WriteDownsOfInventories = fact.value

			elif fact.concept.qname.localName == 'MajorComponentsOfSellingGeneralAndAdministrativeExpensesTextBlock': #主要な販売費及び一般管理費 [テキストブロック]
				self.MajorComponentsOfSellingGeneralAndAdministrativeExpensesTextBlock = fact.value

			elif fact.concept.qname.localName == 'DepreciationSGA': #減価償却費、販売費及び一般管理費
				self.DepreciationSGA = fact.value

			elif fact.concept.qname.localName == 'ProvisionOfAllowanceForDoubtfulAccountsSGA': #貸倒引当金繰入額、販売費及び一般管理費
				self.ProvisionOfAllowanceForDoubtfulAccountsSGA = fact.value

			elif fact.concept.qname.localName == 'ResearchAndDevelopmentExpensesIncludedInGeneralAndAdministrativeExpensesAndManufacturingCostForCurrentPeriodTextBlock': #一般管理費及び当期製造費用に含まれる研究開発費 [テキストブロック]
				self.ResearchAndDevelopmentExpensesIncludedInGeneralAndAdministrativeExpensesAndManufacturingCostForCurrentPeriodTextBlock = fact.value

			elif fact.concept.qname.localName == 'ResearchAndDevelopmentExpensesIncludedInGeneralAndAdministrativeExpensesAndManufacturingCostForCurrentPeriod': #一般管理費及び当期製造費用に含まれる研究開発費
				self.ResearchAndDevelopmentExpensesIncludedInGeneralAndAdministrativeExpensesAndManufacturingCostForCurrentPeriod = fact.value

			elif fact.concept.qname.localName == 'ResearchAndDevelopmentExpensesSGA': #研究開発費、販売費及び一般管理費
				self.ResearchAndDevelopmentExpensesSGA = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingImpairmentLossTextBlock': #減損損失に関する注記 [テキストブロック]
				self.NotesRegardingImpairmentLossTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingReversalOfProvisionIncurredFromBusinessCombinationTextBlock': #企業結合に係る特定勘定の取崩益の注記 [テキストブロック]
				self.NotesRegardingReversalOfProvisionIncurredFromBusinessCombinationTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingGainOnSalesOfPropertyPlantAndEquipmentTextBlock': #固定資産売却益の注記 [テキストブロック]
				self.NotesRegardingGainOnSalesOfPropertyPlantAndEquipmentTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingLossOnSalesOfPropertyPlantAndEquipmentTextBlock': #固定資産売却損の注記 [テキストブロック]
				self.NotesRegardingLossOnSalesOfPropertyPlantAndEquipmentTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingLossOnDisposalOfPropertyPlantAndEquipmentTextBlock': #固定資産除却損の注記 [テキストブロック]
				self.NotesRegardingLossOnDisposalOfPropertyPlantAndEquipmentTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingLossOnDisposalAndSalesOfPropertyPlantAndEquipmentTextBlock': #固定資産除売却損の注記 [テキストブロック]
				self.NotesRegardingLossOnDisposalAndSalesOfPropertyPlantAndEquipmentTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingClassificationOfRevenuesAndExpensesOfIndustryInAppendedListTextBlock': #別記事業の収益及び費用の分類に関する注記 [テキストブロック]
				self.NotesRegardingClassificationOfRevenuesAndExpensesOfIndustryInAppendedListTextBlock = fact.value

			elif fact.concept.qname.localName == 'OtherElementsForNotesStatementOfIncomeAbstract': #損益計算書関係のその他の要素 [タイトル項目]
				self.OtherElementsForNotesStatementOfIncomeAbstract = fact.value

			elif fact.concept.qname.localName == 'BreakdownOfBusinessCostTextBlock': #事業費の内訳 [テキストブロック]
				self.BreakdownOfBusinessCostTextBlock = fact.value

			elif fact.concept.qname.localName == 'BreakdownOfPersonnelExpensesTextBlock': #人件費の内訳 [テキストブロック]
				self.BreakdownOfPersonnelExpensesTextBlock = fact.value

			elif fact.concept.qname.localName == 'BreakdownOfGainOnSalesOfSecuritiesTextBlock': #有価証券売却益の内訳 [テキストブロック]
				self.BreakdownOfGainOnSalesOfSecuritiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'BreakdownOfLossOnSalesOfSecuritiesTextBlock': #有価証券売却損の内訳 [テキストブロック]
				self.BreakdownOfLossOnSalesOfSecuritiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'BreakdownOfLossOnValuationOfSecuritiesTextBlock': #有価証券評価損の内訳 [テキストブロック]
				self.BreakdownOfLossOnValuationOfSecuritiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingTransactionsWithAffiliatedEntitiesTextBlock': #関係会社との取引に関する注記 [テキストブロック]
				self.NotesRegardingTransactionsWithAffiliatedEntitiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'OtherElementsForNotesStatementOfIncomeOfBankAbstract': #銀行業の損益計算書関係のその他の要素 [タイトル項目]
				self.OtherElementsForNotesStatementOfIncomeOfBankAbstract = fact.value

			elif fact.concept.qname.localName == 'MajorComponentsOfOtherIncomeBNKTextBlock': #その他の経常収益の主要な内訳、銀行業 [テキストブロック]
				self.MajorComponentsOfOtherIncomeBNKTextBlock = fact.value

			elif fact.concept.qname.localName == 'MajorComponentsOfOtherExpensesBNKTextBlock': #その他の経常費用の主要な内訳、銀行業 [テキストブロック]
				self.MajorComponentsOfOtherExpensesBNKTextBlock = fact.value

			elif fact.concept.qname.localName == 'OtherElementsForNotesStatementOfIncomeOfSecuritiesRelatedBusinessAbstract': #第一種金融商品取引業の損益計算書関係のその他の要素 [タイトル項目]
				self.OtherElementsForNotesStatementOfIncomeOfSecuritiesRelatedBusinessAbstract = fact.value

			elif fact.concept.qname.localName == 'BreakdownOfNetTradingIncomeSECTextBlock': #トレーディング損益の内訳、第一種金融商品取引業 [テキストブロック]
				self.BreakdownOfNetTradingIncomeSECTextBlock = fact.value

			elif fact.concept.qname.localName == 'BreakdownOfFinancialRevenueSECTextBlock': #金融収益の内訳、第一種金融商品取引業 [テキストブロック]
				self.BreakdownOfFinancialRevenueSECTextBlock = fact.value

			elif fact.concept.qname.localName == 'BreakdownOfFinancialExpensesSECTextBlock': #金融費用の内訳、第一種金融商品取引業 [テキストブロック]
				self.BreakdownOfFinancialExpensesSECTextBlock = fact.value

			elif fact.concept.qname.localName == 'OtherElementsForNotesStatementOfIncomeOfInsuranceAbstract': #保険業の損益計算書関係のその他の要素 [タイトル項目]
				self.OtherElementsForNotesStatementOfIncomeOfInsuranceAbstract = fact.value

			elif fact.concept.qname.localName == 'MajorComponentsOfBusinessCostTextBlock': #事業費の主な内訳 [テキストブロック]
				self.MajorComponentsOfBusinessCostTextBlock = fact.value

			elif fact.concept.qname.localName == 'AgentFeeEtcINSNonlife': #代理店手数料等、損害保険業
				self.AgentFeeEtcINSNonlife = fact.value

			elif fact.concept.qname.localName == 'SalariesINSNonlife': #給与、損害保険業
				self.SalariesINSNonlife = fact.value

			elif fact.concept.qname.localName == 'BreakdownOfNetPremiumsWrittenINSTextBlock': #正味収入保険料の内訳、保険業 [テキストブロック]
				self.BreakdownOfNetPremiumsWrittenINSTextBlock = fact.value

			elif fact.concept.qname.localName == 'BreakdownOfNetClaimsPaidINSTextBlock': #正味支払保険金の内訳、保険業 [テキストブロック]
				self.BreakdownOfNetClaimsPaidINSTextBlock = fact.value

			elif fact.concept.qname.localName == 'BreakdownOfCommissionsAndCollectionFeesINSTextBlock': #諸手数料及び集金費の内訳、保険業 [テキストブロック]
				self.BreakdownOfCommissionsAndCollectionFeesINSTextBlock = fact.value

			elif fact.concept.qname.localName == 'BreakdownOfProvisionForOrReversalOfOutstandingClaimsINSTextBlock': #支払備金繰入額又は支払備金戻入額の内訳、保険業 [テキストブロック]
				self.BreakdownOfProvisionForOrReversalOfOutstandingClaimsINSTextBlock = fact.value

			elif fact.concept.qname.localName == 'BreakdownOfProvisionForOrReversalOfUnderwritingReservesINSTextBlock': #責任準備金繰入額又は責任準備金戻入額の内訳、保険業 [テキストブロック]
				self.BreakdownOfProvisionForOrReversalOfUnderwritingReservesINSTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingReversalOfOrProvisionForReservesForOutstandingClaimsReinsuredINSTextBlock': #支払備金繰入額又は支払備金戻入額の計算上、差し引かれた又は足し上げられた出再支払備金繰入額又は出再支払備金戻入額の注記、保険業 [テキストブロック]
				self.NotesRegardingReversalOfOrProvisionForReservesForOutstandingClaimsReinsuredINSTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingReversalOfOrProvisionForPolicyReservesReinsuredINSTextBlock': #責任準備金繰入額又は責任準備金戻入額の計算上、差し引かれた又は足し上げられた出再責任準備金繰入額又は出再責任準備金戻入額の注記、保険業 [テキストブロック]
				self.NotesRegardingReversalOfOrProvisionForPolicyReservesReinsuredINSTextBlock = fact.value

			elif fact.concept.qname.localName == 'BreakdownOfInterestAndDividendIncomeBySourceAssetINSTextBlock': #利息及び配当金収入の資産源泉別内訳、保険業 [テキストブロック]
				self.BreakdownOfInterestAndDividendIncomeBySourceAssetINSTextBlock = fact.value

			elif fact.concept.qname.localName == 'InterestAndDividendIncomeGainLossOnSalesAndUnrealizedGainLossForEachOfTradingAccountSecuritiesINSTextBlock': #商品有価証券及び売買目的有価証券に係るそれぞれの利息及び配当金収入、売却損益及び評価損益の金額、保険業 [テキストブロック]
				self.InterestAndDividendIncomeGainLossOnSalesAndUnrealizedGainLossForEachOfTradingAccountSecuritiesINSTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingUnrealizedGainLossForMoneyTrustINSTextBlock': #金銭の信託に係る評価損益の金額の注記、保険業 [テキストブロック]
				self.NotesRegardingUnrealizedGainLossForMoneyTrustINSTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingUnrealizedGainLossForDerivativesINSTextBlock': #金融派生商品に係る評価損益の金額の注記、保険業 [テキストブロック]
				self.NotesRegardingUnrealizedGainLossForDerivativesINSTextBlock = fact.value

			elif fact.concept.qname.localName == 'MajorComponentsOfOtherExtraordinaryIncomeINSTextBlock': #その他特別利益の主な内訳、保険業 [テキストブロック]
				self.MajorComponentsOfOtherExtraordinaryIncomeINSTextBlock = fact.value

			elif fact.concept.qname.localName == 'MajorComponentsOfOtherExtraordinaryLossesINSTextBlock': #その他特別損失の主な内訳、保険業 [テキストブロック]
				self.MajorComponentsOfOtherExtraordinaryLossesINSTextBlock = fact.value

			elif fact.concept.qname.localName == 'OtherElementsForNotesStatementOfIncomeOfCommodityFutureTradingAbstract': #商品先物取引業の損益計算書関係のその他の要素 [タイトル項目]
				self.OtherElementsForNotesStatementOfIncomeOfCommodityFutureTradingAbstract = fact.value

			elif fact.concept.qname.localName == 'BreakdownOfBrokerageIncomeCMDTextBlock': #受取手数料の内訳、商品先物取引業 [テキストブロック]
				self.BreakdownOfBrokerageIncomeCMDTextBlock = fact.value

			elif fact.concept.qname.localName == 'BreakdownOfNetGainOnTradingCMDTextBlock': #売買損益の内訳、商品先物取引業 [テキストブロック]
				self.BreakdownOfNetGainOnTradingCMDTextBlock = fact.value

			elif fact.concept.qname.localName == 'ExchangeRelatedExpensesCMDTextBlock': #取引所等関係費の内訳、商品先物取引業 [テキストブロック]
				self.ExchangeRelatedExpensesCMDTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesConsolidatedStatementOfComprehensiveIncomeHeading': #連結包括利益計算書関係 [目次項目]
				self.NotesConsolidatedStatementOfComprehensiveIncomeHeading = fact.value

			elif fact.concept.qname.localName == 'NotesConsolidatedStatementOfComprehensiveIncomeHeading': #連結包括利益計算書関係 [目次項目]
				self.NotesConsolidatedStatementOfComprehensiveIncomeHeading = fact.value

			elif fact.concept.qname.localName == 'NotesConsolidatedStatementOfComprehensiveIncomeTable': #連結包括利益計算書関係 [表]
				self.NotesConsolidatedStatementOfComprehensiveIncomeTable = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedOrNonConsolidatedAxis': #連結個別 [軸]
				self.ConsolidatedOrNonConsolidatedAxis = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedMember': #連結 [メンバー] ※ディメンションデフォルト
				self.ConsolidatedMember = fact.value

			elif fact.concept.qname.localName == 'NotesConsolidatedStatementOfComprehensiveIncomeLineItems': #連結包括利益計算書関係 [表示項目]
				self.NotesConsolidatedStatementOfComprehensiveIncomeLineItems = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingTaxEffectsRelatingToOtherComprehensiveIncomeTextBlock': #その他の包括利益に係る税効果額 [テキストブロック]
				self.NotesRegardingTaxEffectsRelatingToOtherComprehensiveIncomeTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingReclassificationAdjustmentsRelatingToOtherComprehensiveIncomeTextBlock': #その他の包括利益に係る組替調整額 [テキストブロック]
				self.NotesRegardingReclassificationAdjustmentsRelatingToOtherComprehensiveIncomeTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingReclassificationAdjustmentsAndTaxEffectsRelatingToOtherComprehensiveIncomeTextBlock': #その他の包括利益に係る組替調整額及び税効果額 [テキストブロック]
				self.NotesRegardingReclassificationAdjustmentsAndTaxEffectsRelatingToOtherComprehensiveIncomeTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesConsolidatedStatementOfComprehensiveIncomeSingleStatementHeading': #連結損益及び包括利益計算書関係 [目次項目]
				self.NotesConsolidatedStatementOfComprehensiveIncomeSingleStatementHeading = fact.value

			elif fact.concept.qname.localName == 'NotesConsolidatedStatementOfComprehensiveIncomeSingleStatementHeading': #連結損益及び包括利益計算書関係 [目次項目]
				self.NotesConsolidatedStatementOfComprehensiveIncomeSingleStatementHeading = fact.value

			elif fact.concept.qname.localName == 'NotesConsolidatedStatementOfComprehensiveIncomeSingleStatementTable': #連結損益及び包括利益計算書関係 [表]
				self.NotesConsolidatedStatementOfComprehensiveIncomeSingleStatementTable = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedOrNonConsolidatedAxis': #連結個別 [軸]
				self.ConsolidatedOrNonConsolidatedAxis = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedMember': #連結 [メンバー] ※ディメンションデフォルト
				self.ConsolidatedMember = fact.value

			elif fact.concept.qname.localName == 'NotesConsolidatedStatementOfComprehensiveIncomeSingleStatementLineItems': #連結損益及び包括利益計算書関係 [表示項目]
				self.NotesConsolidatedStatementOfComprehensiveIncomeSingleStatementLineItems = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingAmountOfRevenueFromContractsWithCustomersTextBlock': #顧客との契約から生じる収益の金額の注記 [テキストブロック]
				self.NotesRegardingAmountOfRevenueFromContractsWithCustomersTextBlock = fact.value

			elif fact.concept.qname.localName == 'RevenueFromContractsWithCustomers': #顧客との契約から生じる収益
				self.RevenueFromContractsWithCustomers = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingLossOnConstructionContractsTextBlock': #工事損失引当金繰入額の注記 [テキストブロック]
				self.NotesRegardingLossOnConstructionContractsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingWriteDownsOfInventoriesTextBlock': #棚卸資産の帳簿価額の切下げに関する注記 [テキストブロック]
				self.NotesRegardingWriteDownsOfInventoriesTextBlock = fact.value

			elif fact.concept.qname.localName == 'WriteDownsOfInventories': #棚卸資産帳簿価額切下額
				self.WriteDownsOfInventories = fact.value

			elif fact.concept.qname.localName == 'MajorComponentsOfSellingGeneralAndAdministrativeExpensesTextBlock': #主要な販売費及び一般管理費 [テキストブロック]
				self.MajorComponentsOfSellingGeneralAndAdministrativeExpensesTextBlock = fact.value

			elif fact.concept.qname.localName == 'DepreciationSGA': #減価償却費、販売費及び一般管理費
				self.DepreciationSGA = fact.value

			elif fact.concept.qname.localName == 'ProvisionOfAllowanceForDoubtfulAccountsSGA': #貸倒引当金繰入額、販売費及び一般管理費
				self.ProvisionOfAllowanceForDoubtfulAccountsSGA = fact.value

			elif fact.concept.qname.localName == 'ResearchAndDevelopmentExpensesIncludedInGeneralAndAdministrativeExpensesAndManufacturingCostForCurrentPeriodTextBlock': #一般管理費及び当期製造費用に含まれる研究開発費 [テキストブロック]
				self.ResearchAndDevelopmentExpensesIncludedInGeneralAndAdministrativeExpensesAndManufacturingCostForCurrentPeriodTextBlock = fact.value

			elif fact.concept.qname.localName == 'ResearchAndDevelopmentExpensesIncludedInGeneralAndAdministrativeExpensesAndManufacturingCostForCurrentPeriod': #一般管理費及び当期製造費用に含まれる研究開発費
				self.ResearchAndDevelopmentExpensesIncludedInGeneralAndAdministrativeExpensesAndManufacturingCostForCurrentPeriod = fact.value

			elif fact.concept.qname.localName == 'ResearchAndDevelopmentExpensesSGA': #研究開発費、販売費及び一般管理費
				self.ResearchAndDevelopmentExpensesSGA = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingImpairmentLossTextBlock': #減損損失に関する注記 [テキストブロック]
				self.NotesRegardingImpairmentLossTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingReversalOfProvisionIncurredFromBusinessCombinationTextBlock': #企業結合に係る特定勘定の取崩益の注記 [テキストブロック]
				self.NotesRegardingReversalOfProvisionIncurredFromBusinessCombinationTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingClassificationOfRevenuesAndExpensesOfIndustryInAppendedListTextBlock': #別記事業の収益及び費用の分類に関する注記 [テキストブロック]
				self.NotesRegardingClassificationOfRevenuesAndExpensesOfIndustryInAppendedListTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingTaxEffectsRelatingToOtherComprehensiveIncomeTextBlock': #その他の包括利益に係る税効果額 [テキストブロック]
				self.NotesRegardingTaxEffectsRelatingToOtherComprehensiveIncomeTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingReclassificationAdjustmentsRelatingToOtherComprehensiveIncomeTextBlock': #その他の包括利益に係る組替調整額 [テキストブロック]
				self.NotesRegardingReclassificationAdjustmentsRelatingToOtherComprehensiveIncomeTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingReclassificationAdjustmentsAndTaxEffectsRelatingToOtherComprehensiveIncomeTextBlock': #その他の包括利益に係る組替調整額及び税効果額 [テキストブロック]
				self.NotesRegardingReclassificationAdjustmentsAndTaxEffectsRelatingToOtherComprehensiveIncomeTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesConsolidatedStatementOfChangesInEquityHeading': #連結株主資本等変動計算書関係 [目次項目]
				self.NotesConsolidatedStatementOfChangesInEquityHeading = fact.value

			elif fact.concept.qname.localName == 'NotesConsolidatedStatementOfChangesInEquityHeading': #連結株主資本等変動計算書関係 [目次項目]
				self.NotesConsolidatedStatementOfChangesInEquityHeading = fact.value

			elif fact.concept.qname.localName == 'NotesConsolidatedStatementOfChangesInEquityTable': #連結株主資本等変動計算書関係 [表]
				self.NotesConsolidatedStatementOfChangesInEquityTable = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedOrNonConsolidatedAxis': #連結個別 [軸]
				self.ConsolidatedOrNonConsolidatedAxis = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedMember': #連結 [メンバー] ※ディメンションデフォルト
				self.ConsolidatedMember = fact.value

			elif fact.concept.qname.localName == 'NotesConsolidatedStatementOfChangesInEquityLineItems': #連結株主資本等変動計算書関係 [表示項目]
				self.NotesConsolidatedStatementOfChangesInEquityLineItems = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingIssuedSharesAndTreasurySharesTextBlock': #発行済株式及び自己株式に関する注記 [テキストブロック]
				self.NotesRegardingIssuedSharesAndTreasurySharesTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingNewShareSubscriptionRightsEtcTextBlock': #新株予約権等に関する注記 [テキストブロック]
				self.NotesRegardingNewShareSubscriptionRightsEtcTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingDividendTextBlock': #配当に関する注記 [テキストブロック]
				self.NotesRegardingDividendTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesConsolidatedStatementOfCashFlowsHeading': #連結キャッシュ・フロー計算書関係 [目次項目]
				self.NotesConsolidatedStatementOfCashFlowsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesConsolidatedStatementOfCashFlowsHeading': #連結キャッシュ・フロー計算書関係 [目次項目]
				self.NotesConsolidatedStatementOfCashFlowsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesConsolidatedStatementOfCashFlowsTable': #連結キャッシュ・フロー計算書関係 [表]
				self.NotesConsolidatedStatementOfCashFlowsTable = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedOrNonConsolidatedAxis': #連結個別 [軸]
				self.ConsolidatedOrNonConsolidatedAxis = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedMember': #連結 [メンバー] ※ディメンションデフォルト
				self.ConsolidatedMember = fact.value

			elif fact.concept.qname.localName == 'NotesConsolidatedStatementOfCashFlowsLineItems': #連結キャッシュ・フロー計算書関係 [表示項目]
				self.NotesConsolidatedStatementOfCashFlowsLineItems = fact.value

			elif fact.concept.qname.localName == 'ReconciliationOfEndingBalanceOfCashAndCashEquivalentsWithAccountBalancesPerBalanceSheetTextBlock': #現金及び現金同等物の期末残高と貸借対照表に掲記されている科目の金額との関係 [テキストブロック]
				self.ReconciliationOfEndingBalanceOfCashAndCashEquivalentsWithAccountBalancesPerBalanceSheetTextBlock = fact.value

			elif fact.concept.qname.localName == 'MajorComponentsOfAssetsAndLiabilitiesOfConsolidatedSubsidiaryAcquiredByPurchaseOfSharesDuringReportingPeriodTextBlock': #株式の取得により新たに連結子会社となった会社がある場合には、当該会社の資産及び負債の主な内訳 [テキストブロック]
				self.MajorComponentsOfAssetsAndLiabilitiesOfConsolidatedSubsidiaryAcquiredByPurchaseOfSharesDuringReportingPeriodTextBlock = fact.value

			elif fact.concept.qname.localName == 'MajorComponentsOfAssetsAndLiabilitiesOfConsolidatedSubsidiaryDisposedOfBySalesOfSharesDuringReportingPeriodTextBlock': #株式の売却により連結子会社でなくなった会社がある場合には、当該会社の資産及び負債の主な内訳 [テキストブロック]
				self.MajorComponentsOfAssetsAndLiabilitiesOfConsolidatedSubsidiaryDisposedOfBySalesOfSharesDuringReportingPeriodTextBlock = fact.value

			elif fact.concept.qname.localName == 'MajorComponentsOfAssetsAndLiabilitiesIncreasedOrDecreasedAsResultOfAcquisitionOrDisposalOfBusinessOrMergerEtcWherebyCashWasPaidOrReceivedAsConsiderationTextBlock': #現金及び現金同等物を対価とする事業の譲受け若しくは譲渡又は合併等を行った場合には、当該事業の譲受け若しくは譲渡又は合併等により増加又は減少した資産及び負債の主な内訳 [テキストブロック]
				self.MajorComponentsOfAssetsAndLiabilitiesIncreasedOrDecreasedAsResultOfAcquisitionOrDisposalOfBusinessOrMergerEtcWherebyCashWasPaidOrReceivedAsConsiderationTextBlock = fact.value

			elif fact.concept.qname.localName == 'DescriptionOfSignificantTransactionsNotRequiringUseOfCashOrCashEquivalentsTextBlock': #重要な非資金取引の内容 [テキストブロック]
				self.DescriptionOfSignificantTransactionsNotRequiringUseOfCashOrCashEquivalentsTextBlock = fact.value

			elif fact.concept.qname.localName == 'DescriptionOfFactThatCashFlowsFromUsedInInvestingActivitiesIncludeCashFlowsFromAssetManagementActivitiesRelatedToInsuranceBusinessINSTextBlock': #投資活動によるキャッシュ・フローには、保険事業に係る資産運用業務から生じるキャッシュ・フローを含んでいる旨、保険業 [テキストブロック]
				self.DescriptionOfFactThatCashFlowsFromUsedInInvestingActivitiesIncludeCashFlowsFromAssetManagementActivitiesRelatedToInsuranceBusinessINSTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesLeasesConsolidatedFinancialStatementsHeading': #リース取引関係、連結財務諸表 [目次項目]
				self.NotesLeasesConsolidatedFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesLeasesConsolidatedFinancialStatementsTextBlock': #リース取引関係、連結財務諸表 [テキストブロック]
				self.NotesLeasesConsolidatedFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesFinancialInstrumentsConsolidatedFinancialStatementsHeading': #金融商品関係、連結財務諸表 [目次項目]
				self.NotesFinancialInstrumentsConsolidatedFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesFinancialInstrumentsConsolidatedFinancialStatementsTextBlock': #金融商品関係、連結財務諸表 [テキストブロック]
				self.NotesFinancialInstrumentsConsolidatedFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesSecuritiesConsolidatedFinancialStatementsHeading': #有価証券関係、連結財務諸表 [目次項目]
				self.NotesSecuritiesConsolidatedFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesSecuritiesConsolidatedFinancialStatementsTextBlock': #有価証券関係、連結財務諸表 [テキストブロック]
				self.NotesSecuritiesConsolidatedFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesMoneyHeldInTrustConsolidatedFinancialStatementsHeading': #金銭の信託関係、連結財務諸表 [目次項目]
				self.NotesMoneyHeldInTrustConsolidatedFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesMoneyHeldInTrustConsolidatedFinancialStatementsTextBlock': #金銭の信託関係、連結財務諸表 [テキストブロック]
				self.NotesMoneyHeldInTrustConsolidatedFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesValuationDifferenceOnAvailableForSaleSecuritiesConsolidatedFinancialStatementsHeading': #その他有価証券評価差額金、連結財務諸表 [目次項目]
				self.NotesValuationDifferenceOnAvailableForSaleSecuritiesConsolidatedFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesValuationDifferenceOnAvailableForSaleSecuritiesConsolidatedFinancialStatementsTextBlock': #その他有価証券評価差額金、連結財務諸表 [テキストブロック]
				self.NotesValuationDifferenceOnAvailableForSaleSecuritiesConsolidatedFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesDerivativesConsolidatedFinancialStatementsHeading': #デリバティブ取引関係、連結財務諸表 [目次項目]
				self.NotesDerivativesConsolidatedFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesDerivativesConsolidatedFinancialStatementsTextBlock': #デリバティブ取引関係、連結財務諸表 [テキストブロック]
				self.NotesDerivativesConsolidatedFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRetirementBenefitsConsolidatedFinancialStatementsHeading': #退職給付関係、連結財務諸表 [目次項目]
				self.NotesRetirementBenefitsConsolidatedFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesRetirementBenefitsConsolidatedFinancialStatementsTextBlock': #退職給付関係、連結財務諸表 [テキストブロック]
				self.NotesRetirementBenefitsConsolidatedFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesShareOptionsEtcConsolidatedFinancialStatementsHeading': #ストック・オプション等関係、連結財務諸表 [目次項目]
				self.NotesShareOptionsEtcConsolidatedFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesShareOptionsEtcConsolidatedFinancialStatementsTextBlock': #ストック・オプション等関係、連結財務諸表 [テキストブロック]
				self.NotesShareOptionsEtcConsolidatedFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesTaxEffectAccountingConsolidatedFinancialStatementsHeading': #税効果会計関係、連結財務諸表 [目次項目]
				self.NotesTaxEffectAccountingConsolidatedFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesTaxEffectAccountingConsolidatedFinancialStatementsTextBlock': #税効果会計関係、連結財務諸表 [テキストブロック]
				self.NotesTaxEffectAccountingConsolidatedFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesBusinessCombinationsConsolidatedFinancialStatementsHeading': #企業結合等関係、連結財務諸表 [目次項目]
				self.NotesBusinessCombinationsConsolidatedFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesBusinessCombinationsConsolidatedFinancialStatementsTextBlock': #企業結合等関係、連結財務諸表 [テキストブロック]
				self.NotesBusinessCombinationsConsolidatedFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesAssetRetirementObligationsConsolidatedFinancialStatementsHeading': #資産除去債務関係、連結財務諸表 [目次項目]
				self.NotesAssetRetirementObligationsConsolidatedFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesAssetRetirementObligationsConsolidatedFinancialStatementsTextBlock': #資産除去債務関係、連結財務諸表 [テキストブロック]
				self.NotesAssetRetirementObligationsConsolidatedFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRealEstateForLeaseEtcConsolidatedFinancialStatementsHeading': #賃貸等不動産関係、連結財務諸表 [目次項目]
				self.NotesRealEstateForLeaseEtcConsolidatedFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesRealEstateForLeaseEtcConsolidatedFinancialStatementsTextBlock': #賃貸等不動産関係、連結財務諸表 [テキストブロック]
				self.NotesRealEstateForLeaseEtcConsolidatedFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRevenueRecognitionConsolidatedFinancialStatementsHeading': #収益認識関係、連結財務諸表 [目次項目]
				self.NotesRevenueRecognitionConsolidatedFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesRevenueRecognitionConsolidatedFinancialStatementsTextBlock': #収益認識関係、連結財務諸表 [テキストブロック]
				self.NotesRevenueRecognitionConsolidatedFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesInventoriesConsolidatedFinancialStatementsHeading': #棚卸資産関係、連結財務諸表 [目次項目]
				self.NotesInventoriesConsolidatedFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesInventoriesConsolidatedFinancialStatementsTextBlock': #棚卸資産関係、連結財務諸表 [テキストブロック]
				self.NotesInventoriesConsolidatedFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesSegmentInformationEtcConsolidatedFinancialStatementsHeading': #セグメント情報等、連結財務諸表 [目次項目]
				self.NotesSegmentInformationEtcConsolidatedFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesSegmentInformationEtcConsolidatedFinancialStatementsTextBlock': #セグメント情報等、連結財務諸表 [テキストブロック]
				self.NotesSegmentInformationEtcConsolidatedFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesSegmentInformationEtcConsolidatedFinancialStatementsHeading': #セグメント情報等、連結財務諸表 [目次項目]
				self.NotesSegmentInformationEtcConsolidatedFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesSegmentInformationEtcConsolidatedFinancialStatementsTable': #セグメント情報等、連結財務諸表 [表]
				self.NotesSegmentInformationEtcConsolidatedFinancialStatementsTable = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedOrNonConsolidatedAxis': #連結個別 [軸]
				self.ConsolidatedOrNonConsolidatedAxis = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedMember': #連結 [メンバー] ※ディメンションデフォルト
				self.ConsolidatedMember = fact.value

			elif fact.concept.qname.localName == 'NotesSegmentInformationEtcConsolidatedFinancialStatementsLineItems': #セグメント情報等、連結財務諸表 [表示項目]
				self.NotesSegmentInformationEtcConsolidatedFinancialStatementsLineItems = fact.value

			elif fact.concept.qname.localName == 'SegmentInformationAbstract': #セグメント情報 [タイトル項目]
				self.SegmentInformationAbstract = fact.value

			elif fact.concept.qname.localName == 'DescriptionOfReportableSegmentsTextBlock': #報告セグメントの概要 [テキストブロック]
				self.DescriptionOfReportableSegmentsTextBlock = fact.value

			elif fact.concept.qname.localName == 'DisclosureOfChangesInReportableSegmentsTextBlock': #報告セグメントの変更に関する事項 [テキストブロック]
				self.DisclosureOfChangesInReportableSegmentsTextBlock = fact.value

			elif fact.concept.qname.localName == 'DescriptionOfFactThatCompanysBusinessComprisesSingleSegment': #単一セグメントである旨
				self.DescriptionOfFactThatCompanysBusinessComprisesSingleSegment = fact.value

			elif fact.concept.qname.localName == 'ExplanationOfMeasurementsOfSalesProfitLossAssetLiabilityAndOtherItemsForEachReportableSegmentTextBlock': #報告セグメントごとの売上高、利益又は損失、資産、負債その他の項目の金額の算定方法 [テキストブロック]
				self.ExplanationOfMeasurementsOfSalesProfitLossAssetLiabilityAndOtherItemsForEachReportableSegmentTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesSegmentInformationEtcConsolidatedFinancialStatementsHeading': #セグメント情報等、連結財務諸表 [目次項目]
				self.NotesSegmentInformationEtcConsolidatedFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'SegmentInformationAbstract': #セグメント情報 [タイトル項目]
				self.SegmentInformationAbstract = fact.value

			elif fact.concept.qname.localName == 'DisclosureOfSalesProfitLossAssetLiabilityAndOtherItemsForEachReportableSegmentTable': #報告セグメントごとの売上高、利益又は損失、資産、負債その他の項目の金額に関する情報 [表]
				self.DisclosureOfSalesProfitLossAssetLiabilityAndOtherItemsForEachReportableSegmentTable = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedOrNonConsolidatedAxis': #連結個別 [軸]
				self.ConsolidatedOrNonConsolidatedAxis = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedMember': #連結 [メンバー] ※ディメンションデフォルト
				self.ConsolidatedMember = fact.value

			elif fact.concept.qname.localName == 'OperatingSegmentsAxis': #事業セグメント [軸]
				self.OperatingSegmentsAxis = fact.value

			elif fact.concept.qname.localName == 'EntityTotalMember': #連結合計又は会社合計 [メンバー] ※ディメンションデフォルト
				self.EntityTotalMember = fact.value

			elif fact.concept.qname.localName == 'TotalOfReportableSegmentsAndOthersMember': #報告セグメント及びその他の合計 [メンバー]
				self.TotalOfReportableSegmentsAndOthersMember = fact.value

			elif fact.concept.qname.localName == 'ReportableSegmentsMember': #報告セグメント [メンバー]
				self.ReportableSegmentsMember = fact.value

			elif fact.concept.qname.localName == 'OtherReportableSegmentsMember': #その他の報告セグメント [メンバー]
				self.OtherReportableSegmentsMember = fact.value

			elif fact.concept.qname.localName == 'OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember': #報告セグメント以外の全てのセグメント [メンバー]
				self.OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember = fact.value

			elif fact.concept.qname.localName == 'ReconcilingItemsMember': #調整項目 [メンバー]
				self.ReconcilingItemsMember = fact.value

			elif fact.concept.qname.localName == 'DisclosureOfSalesProfitLossAssetLiabilityAndOtherItemsForEachReportableSegmentLineItems': #報告セグメントごとの売上高、利益又は損失、資産、負債その他の項目の金額に関する情報 [表示項目]
				self.DisclosureOfSalesProfitLossAssetLiabilityAndOtherItemsForEachReportableSegmentLineItems = fact.value

			elif fact.concept.qname.localName == 'SalesSegmentInformationAbstract': #売上高、セグメント情報 [タイトル項目]
				self.SalesSegmentInformationAbstract = fact.value

			elif fact.concept.qname.localName == 'RevenuesFromExternalCustomers': #外部顧客への売上高
				self.RevenuesFromExternalCustomers = fact.value

			elif fact.concept.qname.localName == 'TransactionsWithOtherSegments': #セグメント間の内部売上高又は振替高
				self.TransactionsWithOtherSegments = fact.value

			elif fact.concept.qname.localName == 'NetSales': #売上高
				self.NetSales = fact.value

			elif fact.concept.qname.localName == 'Revenue': #売上収益
				self.Revenue = fact.value

			elif fact.concept.qname.localName == 'OperatingRevenue1': #営業収益
				self.OperatingRevenue1 = fact.value

			elif fact.concept.qname.localName == 'OperatingRevenue2': #営業収入
				self.OperatingRevenue2 = fact.value

			elif fact.concept.qname.localName == 'GrossOperatingRevenue': #営業総収入
				self.GrossOperatingRevenue = fact.value

			elif fact.concept.qname.localName == 'OrdinaryIncomeBNK': #経常収益、銀行業
				self.OrdinaryIncomeBNK = fact.value

			elif fact.concept.qname.localName == 'OperatingIncomeINS': #経常収益、保険業
				self.OperatingIncomeINS = fact.value

			elif fact.concept.qname.localName == 'SegmentProfitLossAbstract': #セグメント利益又は損失（△） [タイトル項目]
				self.SegmentProfitLossAbstract = fact.value

			elif fact.concept.qname.localName == 'OperatingIncome': #営業利益又は営業損失（△）
				self.OperatingIncome = fact.value

			elif fact.concept.qname.localName == 'OrdinaryIncome': #経常利益又は経常損失（△）
				self.OrdinaryIncome = fact.value

			elif fact.concept.qname.localName == 'IncomeBeforeIncomeTaxes': #税引前当期純利益又は税引前当期純損失（△）
				self.IncomeBeforeIncomeTaxes = fact.value

			elif fact.concept.qname.localName == 'ProfitLossAttributableToOwnersOfParent': #親会社株主に帰属する当期純利益又は親会社株主に帰属する当期純損失（△）
				self.ProfitLossAttributableToOwnersOfParent = fact.value

			elif fact.concept.qname.localName == 'ProfitLoss': #当期純利益又は当期純損失（△）（平成26年3月28日財規等改正後）
				self.ProfitLoss = fact.value

			elif fact.concept.qname.localName == 'Assets': #資産
				self.Assets = fact.value

			elif fact.concept.qname.localName == 'Liabilities': #負債
				self.Liabilities = fact.value

			elif fact.concept.qname.localName == 'OtherItemsSegmentInformationAbstract': #その他の項目、セグメント情報 [タイトル項目]
				self.OtherItemsSegmentInformationAbstract = fact.value

			elif fact.concept.qname.localName == 'DepreciationSegmentInformation': #減価償却費、セグメント情報
				self.DepreciationSegmentInformation = fact.value

			elif fact.concept.qname.localName == 'AmortizationOfGoodwillSGA': #のれん償却額、販売費及び一般管理費
				self.AmortizationOfGoodwillSGA = fact.value

			elif fact.concept.qname.localName == 'InterestIncomeNOI': #受取利息、営業外収益
				self.InterestIncomeNOI = fact.value

			elif fact.concept.qname.localName == 'InterestExpensesNOE': #支払利息、営業外費用
				self.InterestExpensesNOE = fact.value

			elif fact.concept.qname.localName == 'EquityInEarningsLossesOfAffiliates': #持分法投資利益又は損失（△）
				self.EquityInEarningsLossesOfAffiliates = fact.value

			elif fact.concept.qname.localName == 'ExtraordinaryIncome': #特別利益
				self.ExtraordinaryIncome = fact.value

			elif fact.concept.qname.localName == 'GainOnNegativeGoodwillEI': #負ののれん発生益、特別利益
				self.GainOnNegativeGoodwillEI = fact.value

			elif fact.concept.qname.localName == 'ExtraordinaryLoss': #特別損失
				self.ExtraordinaryLoss = fact.value

			elif fact.concept.qname.localName == 'ImpairmentLossEL': #減損損失、特別損失
				self.ImpairmentLossEL = fact.value

			elif fact.concept.qname.localName == 'IncomeTaxExpense': #税金費用
				self.IncomeTaxExpense = fact.value

			elif fact.concept.qname.localName == 'InvestmentsInEntitiesAccountedForUsingEquityMethod': #持分法適用会社への投資額
				self.InvestmentsInEntitiesAccountedForUsingEquityMethod = fact.value

			elif fact.concept.qname.localName == 'IncreaseInPropertyPlantAndEquipmentAndIntangibleAssets': #有形固定資産及び無形固定資産の増加額
				self.IncreaseInPropertyPlantAndEquipmentAndIntangibleAssets = fact.value

			elif fact.concept.qname.localName == 'NotesSegmentInformationEtcConsolidatedFinancialStatementsHeading': #セグメント情報等、連結財務諸表 [目次項目]
				self.NotesSegmentInformationEtcConsolidatedFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesSegmentInformationEtcConsolidatedFinancialStatementsTable': #セグメント情報等、連結財務諸表 [表]
				self.NotesSegmentInformationEtcConsolidatedFinancialStatementsTable = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedOrNonConsolidatedAxis': #連結個別 [軸]
				self.ConsolidatedOrNonConsolidatedAxis = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedMember': #連結 [メンバー] ※ディメンションデフォルト
				self.ConsolidatedMember = fact.value

			elif fact.concept.qname.localName == 'NotesSegmentInformationEtcConsolidatedFinancialStatementsLineItems': #セグメント情報等、連結財務諸表 [表示項目]
				self.NotesSegmentInformationEtcConsolidatedFinancialStatementsLineItems = fact.value

			elif fact.concept.qname.localName == 'SegmentInformationAbstract': #セグメント情報 [タイトル項目]
				self.SegmentInformationAbstract = fact.value

			elif fact.concept.qname.localName == 'FootnotesRegardingSegmentInformationTableTextBlock': #セグメント表の脚注 [テキストブロック]
				self.FootnotesRegardingSegmentInformationTableTextBlock = fact.value

			elif fact.concept.qname.localName == 'DescriptionOfNatureAndAmountsOfDifferencesBetweenReportableSegmentsTotalAndFinancialStatementsTextBlock': #報告セグメント合計額と財務諸表計上額との差額及び当該差額の主な内容（差異調整に関する事項） [テキストブロック]
				self.DescriptionOfNatureAndAmountsOfDifferencesBetweenReportableSegmentsTotalAndFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesInformationAssociatedWithReportableSegmentsAbstract': #関連情報 [タイトル項目]
				self.NotesInformationAssociatedWithReportableSegmentsAbstract = fact.value

			elif fact.concept.qname.localName == 'InformationForEachProductOrServiceTextBlock': #製品及びサービスごとの情報 [テキストブロック]
				self.InformationForEachProductOrServiceTextBlock = fact.value

			elif fact.concept.qname.localName == 'InformationForEachRegionAbstract': #地域ごとの情報 [タイトル項目]
				self.InformationForEachRegionAbstract = fact.value

			elif fact.concept.qname.localName == 'RevenuesFromExternalCustomersInformationForEachRegionTextBlock': #売上高、地域ごとの情報 [テキストブロック]
				self.RevenuesFromExternalCustomersInformationForEachRegionTextBlock = fact.value

			elif fact.concept.qname.localName == 'PropertyPlantAndEquipmentInformationForEachRegionTextBlock': #有形固定資産、地域ごとの情報 [テキストブロック]
				self.PropertyPlantAndEquipmentInformationForEachRegionTextBlock = fact.value

			elif fact.concept.qname.localName == 'InformationForEachOfMainCustomersTextBlock': #主要な顧客ごとの情報 [テキストブロック]
				self.InformationForEachOfMainCustomersTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesSegmentInformationEtcConsolidatedFinancialStatementsHeading': #セグメント情報等、連結財務諸表 [目次項目]
				self.NotesSegmentInformationEtcConsolidatedFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'DisclosureOfImpairmentLossOnNonCurrentAssetsForEachReportableSegmentAbstract': #報告セグメントごとの固定資産の減損損失に関する情報 [タイトル項目]
				self.DisclosureOfImpairmentLossOnNonCurrentAssetsForEachReportableSegmentAbstract = fact.value

			elif fact.concept.qname.localName == 'DisclosureOfImpairmentLossOnNonCurrentAssetsForEachReportableSegmentTable': #報告セグメントごとの固定資産の減損損失に関する情報 [表]
				self.DisclosureOfImpairmentLossOnNonCurrentAssetsForEachReportableSegmentTable = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedOrNonConsolidatedAxis': #連結個別 [軸]
				self.ConsolidatedOrNonConsolidatedAxis = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedMember': #連結 [メンバー] ※ディメンションデフォルト
				self.ConsolidatedMember = fact.value

			elif fact.concept.qname.localName == 'OperatingSegmentsAxis': #事業セグメント [軸]
				self.OperatingSegmentsAxis = fact.value

			elif fact.concept.qname.localName == 'EntityTotalMember': #連結合計又は会社合計 [メンバー] ※ディメンションデフォルト
				self.EntityTotalMember = fact.value

			elif fact.concept.qname.localName == 'ReportableSegmentsMember': #報告セグメント [メンバー]
				self.ReportableSegmentsMember = fact.value

			elif fact.concept.qname.localName == 'OtherReportableSegmentsMember': #その他の報告セグメント [メンバー]
				self.OtherReportableSegmentsMember = fact.value

			elif fact.concept.qname.localName == 'OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember': #報告セグメント以外の全てのセグメント [メンバー]
				self.OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember = fact.value

			elif fact.concept.qname.localName == 'UnallocatedAmountsAndEliminationMember': #全社・消去 [メンバー]
				self.UnallocatedAmountsAndEliminationMember = fact.value

			elif fact.concept.qname.localName == 'DisclosureOfImpairmentLossOnNonCurrentAssetsForEachReportableSegmentLineItems': #報告セグメントごとの固定資産の減損損失に関する情報 [表示項目]
				self.DisclosureOfImpairmentLossOnNonCurrentAssetsForEachReportableSegmentLineItems = fact.value

			elif fact.concept.qname.localName == 'ImpairmentLossEL': #減損損失、特別損失
				self.ImpairmentLossEL = fact.value

			elif fact.concept.qname.localName == 'NotesSegmentInformationEtcConsolidatedFinancialStatementsHeading': #セグメント情報等、連結財務諸表 [目次項目]
				self.NotesSegmentInformationEtcConsolidatedFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesSegmentInformationEtcConsolidatedFinancialStatementsTable': #セグメント情報等、連結財務諸表 [表]
				self.NotesSegmentInformationEtcConsolidatedFinancialStatementsTable = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedOrNonConsolidatedAxis': #連結個別 [軸]
				self.ConsolidatedOrNonConsolidatedAxis = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedMember': #連結 [メンバー] ※ディメンションデフォルト
				self.ConsolidatedMember = fact.value

			elif fact.concept.qname.localName == 'NotesSegmentInformationEtcConsolidatedFinancialStatementsLineItems': #セグメント情報等、連結財務諸表 [表示項目]
				self.NotesSegmentInformationEtcConsolidatedFinancialStatementsLineItems = fact.value

			elif fact.concept.qname.localName == 'DescriptionOfImpairmentLossNotAllocatedToReportableSegments': #報告セグメントに配分されていない減損損失の内容
				self.DescriptionOfImpairmentLossNotAllocatedToReportableSegments = fact.value

			elif fact.concept.qname.localName == 'NotesSegmentInformationEtcConsolidatedFinancialStatementsHeading': #セグメント情報等、連結財務諸表 [目次項目]
				self.NotesSegmentInformationEtcConsolidatedFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'AmortizationAndUnamortizedBalanceOfGoodwillForEachReportableSegmentAbstract': #報告セグメントごとののれんの償却額及び未償却残高に関する情報 [タイトル項目]
				self.AmortizationAndUnamortizedBalanceOfGoodwillForEachReportableSegmentAbstract = fact.value

			elif fact.concept.qname.localName == 'AmortizationAndUnamortizedBalanceOfGoodwillForEachReportableSegmentTable': #報告セグメントごとののれんの償却額及び未償却残高に関する情報 [表]
				self.AmortizationAndUnamortizedBalanceOfGoodwillForEachReportableSegmentTable = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedOrNonConsolidatedAxis': #連結個別 [軸]
				self.ConsolidatedOrNonConsolidatedAxis = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedMember': #連結 [メンバー] ※ディメンションデフォルト
				self.ConsolidatedMember = fact.value

			elif fact.concept.qname.localName == 'OperatingSegmentsAxis': #事業セグメント [軸]
				self.OperatingSegmentsAxis = fact.value

			elif fact.concept.qname.localName == 'EntityTotalMember': #連結合計又は会社合計 [メンバー] ※ディメンションデフォルト
				self.EntityTotalMember = fact.value

			elif fact.concept.qname.localName == 'ReportableSegmentsMember': #報告セグメント [メンバー]
				self.ReportableSegmentsMember = fact.value

			elif fact.concept.qname.localName == 'OtherReportableSegmentsMember': #その他の報告セグメント [メンバー]
				self.OtherReportableSegmentsMember = fact.value

			elif fact.concept.qname.localName == 'OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember': #報告セグメント以外の全てのセグメント [メンバー]
				self.OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember = fact.value

			elif fact.concept.qname.localName == 'UnallocatedAmountsAndEliminationMember': #全社・消去 [メンバー]
				self.UnallocatedAmountsAndEliminationMember = fact.value

			elif fact.concept.qname.localName == 'AmortizationAndUnamortizedBalanceOfGoodwillForEachReportableSegmentLineItems': #報告セグメントごとののれんの償却額及び未償却残高に関する情報 [表示項目]
				self.AmortizationAndUnamortizedBalanceOfGoodwillForEachReportableSegmentLineItems = fact.value

			elif fact.concept.qname.localName == 'AmortizationOfGoodwillSGA': #のれん償却額、販売費及び一般管理費
				self.AmortizationOfGoodwillSGA = fact.value

			elif fact.concept.qname.localName == 'Goodwill': #のれん
				self.Goodwill = fact.value

			elif fact.concept.qname.localName == 'GoodwillBeforeOffsetting': #のれん（相殺前）
				self.GoodwillBeforeOffsetting = fact.value

			elif fact.concept.qname.localName == 'NotesSegmentInformationEtcConsolidatedFinancialStatementsHeading': #セグメント情報等、連結財務諸表 [目次項目]
				self.NotesSegmentInformationEtcConsolidatedFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'AmortizationAndUnamortizedBalanceOfNegativeGoodwillForEachReportableSegmentAbstract': #報告セグメントごとの負ののれんの償却額及び未償却残高に関する情報 [タイトル項目]
				self.AmortizationAndUnamortizedBalanceOfNegativeGoodwillForEachReportableSegmentAbstract = fact.value

			elif fact.concept.qname.localName == 'AmortizationAndUnamortizedBalanceOfNegativeGoodwillForEachReportableSegmentTable': #報告セグメントごとの負ののれんの償却額及び未償却残高に関する情報 [表]
				self.AmortizationAndUnamortizedBalanceOfNegativeGoodwillForEachReportableSegmentTable = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedOrNonConsolidatedAxis': #連結個別 [軸]
				self.ConsolidatedOrNonConsolidatedAxis = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedMember': #連結 [メンバー] ※ディメンションデフォルト
				self.ConsolidatedMember = fact.value

			elif fact.concept.qname.localName == 'OperatingSegmentsAxis': #事業セグメント [軸]
				self.OperatingSegmentsAxis = fact.value

			elif fact.concept.qname.localName == 'EntityTotalMember': #連結合計又は会社合計 [メンバー] ※ディメンションデフォルト
				self.EntityTotalMember = fact.value

			elif fact.concept.qname.localName == 'ReportableSegmentsMember': #報告セグメント [メンバー]
				self.ReportableSegmentsMember = fact.value

			elif fact.concept.qname.localName == 'OtherReportableSegmentsMember': #その他の報告セグメント [メンバー]
				self.OtherReportableSegmentsMember = fact.value

			elif fact.concept.qname.localName == 'OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember': #報告セグメント以外の全てのセグメント [メンバー]
				self.OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember = fact.value

			elif fact.concept.qname.localName == 'UnallocatedAmountsAndEliminationMember': #全社・消去 [メンバー]
				self.UnallocatedAmountsAndEliminationMember = fact.value

			elif fact.concept.qname.localName == 'AmortizationAndUnamortizedBalanceOfNegativeGoodwillForEachReportableSegmentLineItems': #報告セグメントごとの負ののれんの償却額及び未償却残高に関する情報 [表示項目]
				self.AmortizationAndUnamortizedBalanceOfNegativeGoodwillForEachReportableSegmentLineItems = fact.value

			elif fact.concept.qname.localName == 'AmortizationOfNegativeGoodwillNOI': #負ののれん償却額、営業外収益
				self.AmortizationOfNegativeGoodwillNOI = fact.value

			elif fact.concept.qname.localName == 'NegativeGoodwill': #負ののれん
				self.NegativeGoodwill = fact.value

			elif fact.concept.qname.localName == 'NegativeGoodwillBeforeOffsetting': #負ののれん（相殺前）
				self.NegativeGoodwillBeforeOffsetting = fact.value

			elif fact.concept.qname.localName == 'NotesSegmentInformationEtcConsolidatedFinancialStatementsHeading': #セグメント情報等、連結財務諸表 [目次項目]
				self.NotesSegmentInformationEtcConsolidatedFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesSegmentInformationEtcConsolidatedFinancialStatementsTable': #セグメント情報等、連結財務諸表 [表]
				self.NotesSegmentInformationEtcConsolidatedFinancialStatementsTable = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedOrNonConsolidatedAxis': #連結個別 [軸]
				self.ConsolidatedOrNonConsolidatedAxis = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedMember': #連結 [メンバー] ※ディメンションデフォルト
				self.ConsolidatedMember = fact.value

			elif fact.concept.qname.localName == 'NotesSegmentInformationEtcConsolidatedFinancialStatementsLineItems': #セグメント情報等、連結財務諸表 [表示項目]
				self.NotesSegmentInformationEtcConsolidatedFinancialStatementsLineItems = fact.value

			elif fact.concept.qname.localName == 'DescriptionOfAmortizationOfGoodwillOrUnamortizedBalanceOfGoodwillNotAllocatedToReportableSegments': #報告セグメントに配分されていないのれんの償却額又は未償却残高の内容
				self.DescriptionOfAmortizationOfGoodwillOrUnamortizedBalanceOfGoodwillNotAllocatedToReportableSegments = fact.value

			elif fact.concept.qname.localName == 'NotesSegmentInformationEtcConsolidatedFinancialStatementsHeading': #セグメント情報等、連結財務諸表 [目次項目]
				self.NotesSegmentInformationEtcConsolidatedFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'InformationAboutGainOnBargainPurchaseForEachReportableSegmentTable': #報告セグメントごとの負ののれん発生益に関する情報 [表]
				self.InformationAboutGainOnBargainPurchaseForEachReportableSegmentTable = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedOrNonConsolidatedAxis': #連結個別 [軸]
				self.ConsolidatedOrNonConsolidatedAxis = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedMember': #連結 [メンバー] ※ディメンションデフォルト
				self.ConsolidatedMember = fact.value

			elif fact.concept.qname.localName == 'OperatingSegmentsAxis': #事業セグメント [軸]
				self.OperatingSegmentsAxis = fact.value

			elif fact.concept.qname.localName == 'EntityTotalMember': #連結合計又は会社合計 [メンバー] ※ディメンションデフォルト
				self.EntityTotalMember = fact.value

			elif fact.concept.qname.localName == 'ReportableSegmentsMember': #報告セグメント [メンバー]
				self.ReportableSegmentsMember = fact.value

			elif fact.concept.qname.localName == 'OtherReportableSegmentsMember': #その他の報告セグメント [メンバー]
				self.OtherReportableSegmentsMember = fact.value

			elif fact.concept.qname.localName == 'OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember': #報告セグメント以外の全てのセグメント [メンバー]
				self.OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember = fact.value

			elif fact.concept.qname.localName == 'UnallocatedAmountsAndEliminationMember': #全社・消去 [メンバー]
				self.UnallocatedAmountsAndEliminationMember = fact.value

			elif fact.concept.qname.localName == 'InformationAboutGainOnBargainPurchaseForEachReportableSegmentLineItems': #報告セグメントごとの負ののれん発生益に関する情報 [表示項目]
				self.InformationAboutGainOnBargainPurchaseForEachReportableSegmentLineItems = fact.value

			elif fact.concept.qname.localName == 'DescriptionOfFactorsWhichLedToRecognitionOfGainOnBargainPurchaseTextBlock': #報告セグメントごとの負ののれん発生益を認識する要因となった事象の概要 [テキストブロック]
				self.DescriptionOfFactorsWhichLedToRecognitionOfGainOnBargainPurchaseTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesOperationOfPublicFacilitiesConsolidatedFinancialStatementsHeading': #公共施設等運営事業関係、連結財務諸表 [目次項目]
				self.NotesOperationOfPublicFacilitiesConsolidatedFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesOperationOfPublicFacilitiesConsolidatedFinancialStatementsTextBlock': #公共施設等運営事業関係、連結財務諸表 [テキストブロック]
				self.NotesOperationOfPublicFacilitiesConsolidatedFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRelatedPartiesConsolidatedFinancialStatementsHeading': #関連当事者情報、連結財務諸表 [目次項目]
				self.NotesRelatedPartiesConsolidatedFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesRelatedPartiesConsolidatedFinancialStatementsTextBlock': #関連当事者情報、連結財務諸表 [テキストブロック]
				self.NotesRelatedPartiesConsolidatedFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesSpecialPurposeEntitiesSubjectToDisclosureConsolidatedFinancialStatementsHeading': #開示対象特別目的会社関係、連結財務諸表 [目次項目]
				self.NotesSpecialPurposeEntitiesSubjectToDisclosureConsolidatedFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesSpecialPurposeEntitiesSubjectToDisclosureConsolidatedFinancialStatementsTextBlock': #開示対象特別目的会社関係、連結財務諸表 [テキストブロック]
				self.NotesSpecialPurposeEntitiesSubjectToDisclosureConsolidatedFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesPerShareInformationConsolidatedFinancialStatementsHeading': #１株当たり情報、連結財務諸表 [目次項目]
				self.NotesPerShareInformationConsolidatedFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesPerShareInformationConsolidatedFinancialStatementsTextBlock': #１株当たり情報、連結財務諸表 [テキストブロック]
				self.NotesPerShareInformationConsolidatedFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesSignificantEventsAfterReportingPeriodConsolidatedFinancialStatementsHeading': #重要な後発事象、連結財務諸表 [目次項目]
				self.NotesSignificantEventsAfterReportingPeriodConsolidatedFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesSignificantEventsAfterReportingPeriodConsolidatedFinancialStatementsTextBlock': #重要な後発事象、連結財務諸表 [テキストブロック]
				self.NotesSignificantEventsAfterReportingPeriodConsolidatedFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesToConsolidatedFinancialStatementsJMISHeading': #連結財務諸表注記事項（JMIS） [目次項目]
				self.NotesToConsolidatedFinancialStatementsJMISHeading = fact.value

			elif fact.concept.qname.localName == 'NotesToConsolidatedFinancialStatementsJMISTextBlock': #連結財務諸表注記事項（JMIS） [テキストブロック]
				self.NotesToConsolidatedFinancialStatementsJMISTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesToConsolidatedFinancialStatementsUSGAAPHeading': #連結財務諸表注記事項（US GAAP） [目次項目]
				self.NotesToConsolidatedFinancialStatementsUSGAAPHeading = fact.value

			elif fact.concept.qname.localName == 'NotesToConsolidatedFinancialStatementsUSGAAPTextBlock': #連結財務諸表注記事項（US GAAP） [テキストブロック]
				self.NotesToConsolidatedFinancialStatementsUSGAAPTextBlock = fact.value

			elif fact.concept.qname.localName == 'AnnexedConsolidatedDetailedSchedulesHeading': #連結附属明細表 [目次項目]
				self.AnnexedConsolidatedDetailedSchedulesHeading = fact.value

			elif fact.concept.qname.localName == 'AnnexedConsolidatedDetailedScheduleOfCorporateBondsHeading': #社債明細表、連結財務諸表 [目次項目]
				self.AnnexedConsolidatedDetailedScheduleOfCorporateBondsHeading = fact.value

			elif fact.concept.qname.localName == 'AnnexedConsolidatedDetailedScheduleOfCorporateBondsTextBlock': #社債明細表、連結財務諸表 [テキストブロック]
				self.AnnexedConsolidatedDetailedScheduleOfCorporateBondsTextBlock = fact.value

			elif fact.concept.qname.localName == 'AnnexedConsolidatedDetailedScheduleOfBorrowingsHeading': #借入金等明細表、連結財務諸表 [目次項目]
				self.AnnexedConsolidatedDetailedScheduleOfBorrowingsHeading = fact.value

			elif fact.concept.qname.localName == 'AnnexedConsolidatedDetailedScheduleOfBorrowingsTextBlock': #借入金等明細表、連結財務諸表 [テキストブロック]
				self.AnnexedConsolidatedDetailedScheduleOfBorrowingsTextBlock = fact.value

			elif fact.concept.qname.localName == 'AnnexedConsolidatedDetailedScheduleOfAssetRetirementObligationsHeading': #資産除去債務明細表、連結財務諸表 [目次項目]
				self.AnnexedConsolidatedDetailedScheduleOfAssetRetirementObligationsHeading = fact.value

			elif fact.concept.qname.localName == 'AnnexedConsolidatedDetailedScheduleOfAssetRetirementObligationsTextBlock': #資産除去債務明細表、連結財務諸表 [テキストブロック]
				self.AnnexedConsolidatedDetailedScheduleOfAssetRetirementObligationsTextBlock = fact.value

			elif fact.concept.qname.localName == 'OtherInformationConsolidatedFinancialStatementsEtcHeading': #その他、連結財務諸表等 [目次項目]
				self.OtherInformationConsolidatedFinancialStatementsEtcHeading = fact.value

			elif fact.concept.qname.localName == 'OtherInformationConsolidatedFinancialStatementsEtcTextBlock': #その他、連結財務諸表等 [テキストブロック]
				self.OtherInformationConsolidatedFinancialStatementsEtcTextBlock = fact.value

			elif fact.concept.qname.localName == 'FinancialStatementsEtcHeading': #財務諸表等 [目次項目]
				self.FinancialStatementsEtcHeading = fact.value

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

			elif fact.concept.qname.localName == 'DetailedScheduleOfManufacturingCostTextBlock': #製造原価明細書 [テキストブロック]
				self.DetailedScheduleOfManufacturingCostTextBlock = fact.value

			elif fact.concept.qname.localName == 'DetailedScheduleOfCostOfSalesTextBlock': #売上原価明細書 [テキストブロック]
				self.DetailedScheduleOfCostOfSalesTextBlock = fact.value

			elif fact.concept.qname.localName == 'DetailedScheduleOfOperatingExpensesForRailwayBusinessTextBlock': #鉄道事業営業費明細表 [テキストブロック]
				self.DetailedScheduleOfOperatingExpensesForRailwayBusinessTextBlock = fact.value

			elif fact.concept.qname.localName == 'DetailedScheduleOfOperatingExpensesForMotorwayBusinessTextBlock': #自動車道事業営業費明細表 [テキストブロック]
				self.DetailedScheduleOfOperatingExpensesForMotorwayBusinessTextBlock = fact.value

			elif fact.concept.qname.localName == 'DetailedScheduleOfOperatingExpensesTelecommunicationsBusinessTextBlock': #電気通信事業営業費用明細表 [テキストブロック]
				self.DetailedScheduleOfOperatingExpensesTelecommunicationsBusinessTextBlock = fact.value

			elif fact.concept.qname.localName == 'DetailedScheduleOfElectricUtilityOperatingExpensesTextBlock': #電気事業営業費用明細表 [テキストブロック]
				self.DetailedScheduleOfElectricUtilityOperatingExpensesTextBlock = fact.value

			elif fact.concept.qname.localName == 'DetailedScheduleOfOperatingExpensesGASTextBlock': #営業費明細表、ガス事業 [テキストブロック]
				self.DetailedScheduleOfOperatingExpensesGASTextBlock = fact.value

			elif fact.concept.qname.localName == 'DetailedScheduleOfOperatingExpensesNonOperatingExpensesExtraordinaryLossesEtcForHighwayBusinessTextBlock': #高速道路事業営業費用、営業外費用及び特別損失等明細表 [テキストブロック]
				self.DetailedScheduleOfOperatingExpensesNonOperatingExpensesExtraordinaryLossesEtcForHighwayBusinessTextBlock = fact.value

			elif fact.concept.qname.localName == 'DetailedScheduleOfOperatingExpensesEDUTextBlock': #事業費用明細表、学校法人 [テキストブロック]
				self.DetailedScheduleOfOperatingExpensesEDUTextBlock = fact.value

			elif fact.concept.qname.localName == 'StatementOfChangesInEquityHeading': #株主資本等変動計算書 [目次項目]
				self.StatementOfChangesInEquityHeading = fact.value

			elif fact.concept.qname.localName == 'StatementOfChangesInEquityTextBlock': #株主資本等変動計算書 [テキストブロック]
				self.StatementOfChangesInEquityTextBlock = fact.value

			elif fact.concept.qname.localName == 'StatementOfCashFlowsHeading': #キャッシュ・フロー計算書 [目次項目]
				self.StatementOfCashFlowsHeading = fact.value

			elif fact.concept.qname.localName == 'StatementOfCashFlowsTextBlock': #キャッシュ・フロー計算書 [テキストブロック]
				self.StatementOfCashFlowsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesFinancialStatementsHeading': #注記事項、財務諸表 [目次項目]
				self.NotesFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesUncertaintiesOfEntitysAbilityToContinueAsGoingConcernFinancialStatementsHeading': #継続企業の前提に関する事項、財務諸表 [目次項目]
				self.NotesUncertaintiesOfEntitysAbilityToContinueAsGoingConcernFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesUncertaintiesOfEntitysAbilityToContinueAsGoingConcernFinancialStatementsTextBlock': #継続企業の前提に関する事項、財務諸表 [テキストブロック]
				self.NotesUncertaintiesOfEntitysAbilityToContinueAsGoingConcernFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesSignificantAccountingPoliciesFinancialStatementsHeading': #重要な会計方針、財務諸表 [目次項目]
				self.NotesSignificantAccountingPoliciesFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesSignificantAccountingPoliciesFinancialStatementsTextBlock': #重要な会計方針、財務諸表 [テキストブロック]
				self.NotesSignificantAccountingPoliciesFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'SignificantAccountingEstimatesFinancialStatementsHeading': #重要な会計上の見積り、財務諸表 [目次項目]
				self.SignificantAccountingEstimatesFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'SignificantAccountingEstimatesFinancialStatementsTextBlock': #重要な会計上の見積り、財務諸表 [テキストブロック]
				self.SignificantAccountingEstimatesFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesChangesInAccountingPoliciesFinancialStatementsHeading': #会計方針の変更、財務諸表 [目次項目]
				self.NotesChangesInAccountingPoliciesFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesChangesInAccountingPoliciesInAccordanceWithChangesInAccountingStandardsEtcFinancialStatementsTextBlock': #会計基準等の改正等に伴う会計方針の変更、財務諸表 [テキストブロック]
				self.NotesChangesInAccountingPoliciesInAccordanceWithChangesInAccountingStandardsEtcFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesVoluntaryChangesInAccountingPoliciesFinancialStatementsTextBlock': #会計基準等の改正等以外の正当な理由による会計方針の変更、財務諸表 [テキストブロック]
				self.NotesVoluntaryChangesInAccountingPoliciesFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesChangesInAccountingPoliciesWhichAreDifficultToDistinguishFromChangesInAccountingEstimatesFinancialStatementsTextBlock': #会計上の見積りの変更と区別することが困難な会計方針の変更、財務諸表 [テキストブロック]
				self.NotesChangesInAccountingPoliciesWhichAreDifficultToDistinguishFromChangesInAccountingEstimatesFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesNewAccountingStandardsNotYetAppliedFinancialStatementsHeading': #未適用の会計基準等、財務諸表 [目次項目]
				self.NotesNewAccountingStandardsNotYetAppliedFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesNewAccountingStandardsNotYetAppliedFinancialStatementsTextBlock': #未適用の会計基準等、財務諸表 [テキストブロック]
				self.NotesNewAccountingStandardsNotYetAppliedFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesChangesInPresentationFinancialStatementsHeading': #表示方法の変更、財務諸表 [目次項目]
				self.NotesChangesInPresentationFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesChangesInPresentationFinancialStatementsTextBlock': #表示方法の変更、財務諸表 [テキストブロック]
				self.NotesChangesInPresentationFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesChangesInAccountingEstimatesFinancialStatementsHeading': #会計上の見積りの変更、財務諸表 [目次項目]
				self.NotesChangesInAccountingEstimatesFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesChangesInAccountingEstimatesFinancialStatementsTextBlock': #会計上の見積りの変更、財務諸表 [テキストブロック]
				self.NotesChangesInAccountingEstimatesFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRestatementFinancialStatementsHeading': #修正再表示、財務諸表 [目次項目]
				self.NotesRestatementFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesRestatementFinancialStatementsTextBlock': #修正再表示、財務諸表 [テキストブロック]
				self.NotesRestatementFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesAdditionalInformationFinancialStatementsHeading': #追加情報、財務諸表 [目次項目]
				self.NotesAdditionalInformationFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesAdditionalInformationFinancialStatementsTextBlock': #追加情報、財務諸表 [テキストブロック]
				self.NotesAdditionalInformationFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesBalanceSheetHeading': #貸借対照表関係 [目次項目]
				self.NotesBalanceSheetHeading = fact.value

			elif fact.concept.qname.localName == 'NotesBalanceSheetHeading': #貸借対照表関係 [目次項目]
				self.NotesBalanceSheetHeading = fact.value

			elif fact.concept.qname.localName == 'NotesBalanceSheetTable': #貸借対照表関係 [表]
				self.NotesBalanceSheetTable = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedOrNonConsolidatedAxis': #連結個別 [軸]
				self.ConsolidatedOrNonConsolidatedAxis = fact.value

			elif fact.concept.qname.localName == 'NonConsolidatedMember': #非連結又は個別 [メンバー]
				self.NonConsolidatedMember = fact.value

			elif fact.concept.qname.localName == 'NotesBalanceSheetLineItems': #貸借対照表関係 [表示項目]
				self.NotesBalanceSheetLineItems = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingInventoriesTextBlock': #棚卸資産の内訳の注記 [テキストブロック]
				self.NotesRegardingInventoriesTextBlock = fact.value

			elif fact.concept.qname.localName == 'MerchandiseAndFinishedGoods': #商品及び製品
				self.MerchandiseAndFinishedGoods = fact.value

			elif fact.concept.qname.localName == 'WorkInProcess': #仕掛品
				self.WorkInProcess = fact.value

			elif fact.concept.qname.localName == 'RawMaterialsAndSupplies': #原材料及び貯蔵品
				self.RawMaterialsAndSupplies = fact.value

			elif fact.concept.qname.localName == 'Inventories': #棚卸資産
				self.Inventories = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingAmountsOfNotesAndAccountsReceivableTradeAndContractAssetsTextBlock': #受取手形、売掛金及び契約資産の金額の注記 [テキストブロック]
				self.NotesRegardingAmountsOfNotesAndAccountsReceivableTradeAndContractAssetsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesReceivableTrade': #受取手形
				self.NotesReceivableTrade = fact.value

			elif fact.concept.qname.localName == 'AllowanceForDoubtfulAccountsNotesReceivableTrade': #貸倒引当金、受取手形
				self.AllowanceForDoubtfulAccountsNotesReceivableTrade = fact.value

			elif fact.concept.qname.localName == 'NotesReceivableTradeNet': #受取手形（純額）
				self.NotesReceivableTradeNet = fact.value

			elif fact.concept.qname.localName == 'AccountsReceivableTrade': #売掛金
				self.AccountsReceivableTrade = fact.value

			elif fact.concept.qname.localName == 'AllowanceForDoubtfulAccountsAccountsReceivableTrade': #貸倒引当金、売掛金
				self.AllowanceForDoubtfulAccountsAccountsReceivableTrade = fact.value

			elif fact.concept.qname.localName == 'AccountsReceivableTradeNet': #売掛金（純額）
				self.AccountsReceivableTradeNet = fact.value

			elif fact.concept.qname.localName == 'ContractAssets': #契約資産
				self.ContractAssets = fact.value

			elif fact.concept.qname.localName == 'AllowanceForDoubtfulAccountsContractAssets': #貸倒引当金、契約資産
				self.AllowanceForDoubtfulAccountsContractAssets = fact.value

			elif fact.concept.qname.localName == 'ContractAssetsNet': #契約資産（純額）
				self.ContractAssetsNet = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingAllowancesDirectlyDeductedFromBalancesOfAssetsTextBlock': #資産の金額から直接控除している引当金の注記 [テキストブロック]
				self.NotesRegardingAllowancesDirectlyDeductedFromBalancesOfAssetsTextBlock = fact.value

			elif fact.concept.qname.localName == 'AllowanceForDoubtfulAccountsCA': #貸倒引当金、流動資産、一括控除
				self.AllowanceForDoubtfulAccountsCA = fact.value

			elif fact.concept.qname.localName == 'AllowanceForDoubtfulAccountsIOAByGroup': #貸倒引当金、投資その他の資産、一括控除
				self.AllowanceForDoubtfulAccountsIOAByGroup = fact.value

			elif fact.concept.qname.localName == 'AllowanceForDoubtfulAccountsAccountsReceivableTrade': #貸倒引当金、売掛金
				self.AllowanceForDoubtfulAccountsAccountsReceivableTrade = fact.value

			elif fact.concept.qname.localName == 'AllowanceForDoubtfulAccountsLongTermLoansReceivable': #貸倒引当金、長期貸付金
				self.AllowanceForDoubtfulAccountsLongTermLoansReceivable = fact.value

			elif fact.concept.qname.localName == 'AllowanceForDoubtfulAccountsClaimsInBankruptcyReorganizationClaimsAndOther': #貸倒引当金、破産更生債権等
				self.AllowanceForDoubtfulAccountsClaimsInBankruptcyReorganizationClaimsAndOther = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingAccumulatedDepreciationOfPropertyPlantAndEquipmentTextBlock': #有形固定資産の減価償却累計額の注記 [テキストブロック]
				self.NotesRegardingAccumulatedDepreciationOfPropertyPlantAndEquipmentTextBlock = fact.value

			elif fact.concept.qname.localName == 'AccumulatedDepreciationPPEByGroup': #減価償却累計額、有形固定資産、一括控除
				self.AccumulatedDepreciationPPEByGroup = fact.value

			elif fact.concept.qname.localName == 'AccumulatedDepreciationBuildings': #減価償却累計額、建物
				self.AccumulatedDepreciationBuildings = fact.value

			elif fact.concept.qname.localName == 'AccumulatedDepreciationStructures': #減価償却累計額、構築物
				self.AccumulatedDepreciationStructures = fact.value

			elif fact.concept.qname.localName == 'AccumulatedDepreciationMachineryAndEquipment': #減価償却累計額、機械及び装置
				self.AccumulatedDepreciationMachineryAndEquipment = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingAmountsOfReductionEntryOfPropertyPlantAndEquipmentTextBlock': #有形固定資産の圧縮記帳額の注記 [テキストブロック]
				self.NotesRegardingAmountsOfReductionEntryOfPropertyPlantAndEquipmentTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingPresentationOfAccumulatedImpairmentLossTextBlock': #減損損失累計額の表示に関する注記 [テキストブロック]
				self.NotesRegardingPresentationOfAccumulatedImpairmentLossTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingAssetsAndLiabilitiesIncurredFromTransactionsWithAffiliatedEntitiesTextBlock': #関係会社に関する資産・負債の注記 [テキストブロック]
				self.NotesRegardingAssetsAndLiabilitiesIncurredFromTransactionsWithAffiliatedEntitiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingRevaluationOfNonCurrentAssetsTextBlock': #固定資産の再評価に関する注記 [テキストブロック]
				self.NotesRegardingRevaluationOfNonCurrentAssetsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingRevaluationOfLandForBusinessTextBlock': #事業用土地の再評価に関する注記 [テキストブロック]
				self.NotesRegardingRevaluationOfLandForBusinessTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingPledgedAssetsTextBlock': #担保に供している資産の注記 [テキストブロック]
				self.NotesRegardingPledgedAssetsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingPresentationOfInventoriesAndProvisionForLossOnConstructionContractsTextBlock': #棚卸資産及び工事損失引当金の表示に関する注記 [テキストブロック]
				self.NotesRegardingPresentationOfInventoriesAndProvisionForLossOnConstructionContractsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingAmountOfContractLiabilitiesTextBlock': #契約負債の金額の注記 [テキストブロック]
				self.NotesRegardingAmountOfContractLiabilitiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'ContractLiabilities': #契約負債
				self.ContractLiabilities = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingReservesUnderSpecialLawsTextBlock': #特別法上の準備金等に関する注記 [テキストブロック]
				self.NotesRegardingReservesUnderSpecialLawsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingProvisionIncurredFromBusinessCombinationTextBlock': #企業結合に係る特定勘定の注記 [テキストブロック]
				self.NotesRegardingProvisionIncurredFromBusinessCombinationTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingGuaranteeObligationsTextBlock': #保証債務の注記 [テキストブロック]
				self.NotesRegardingGuaranteeObligationsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingTradeNotesReceivableDiscountedOrTransferredByEndorsementTextBlock': #受取手形割引高及び（又は）受取手形裏書譲渡高 [テキストブロック]
				self.NotesRegardingTradeNotesReceivableDiscountedOrTransferredByEndorsementTextBlock = fact.value

			elif fact.concept.qname.localName == 'DiscountedTradeNotesReceivable': #受取手形割引高
				self.DiscountedTradeNotesReceivable = fact.value

			elif fact.concept.qname.localName == 'TradeNotesReceivableTransferredByEndorsement': #受取手形裏書譲渡高
				self.TradeNotesReceivableTransferredByEndorsement = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingDepositForSubscriptionsToSharesTextBlock': #新株式申込証拠金に関する注記 [テキストブロック]
				self.NotesRegardingDepositForSubscriptionsToSharesTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingLimitationsOnDividendTextBlock': #配当制限に関する注記 [テキストブロック]
				self.NotesRegardingLimitationsOnDividendTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingPresentationOfNetAssetsOfDesignatedCorporationTextBlock': #指定法人の純資産の記載に関する注記 [テキストブロック]
				self.NotesRegardingPresentationOfNetAssetsOfDesignatedCorporationTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingPromissoryNotesDueOnBalanceSheetDateTextBlock': #期末日満期手形の会計処理 [テキストブロック]
				self.NotesRegardingPromissoryNotesDueOnBalanceSheetDateTextBlock = fact.value

			elif fact.concept.qname.localName == 'OtherElementsForNotesBalanceSheetAbstract': #貸借対照表関係のその他の要素 [タイトル項目]
				self.OtherElementsForNotesBalanceSheetAbstract = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingLoanedWhichBorrowerHasRightToSellOrRepledgeTextBlock': #消費貸借契約及び（又は）消費寄託契約により貸し付けている有価証券に関する注記 [テキストブロック]
				self.NotesRegardingLoanedWhichBorrowerHasRightToSellOrRepledgeTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingFinancialAssetsBorrowedWhichBorrowerHasRightToSellOrRepledgeTextBlock': #自由処分権を有する担保受入金融資産に関する注記 [テキストブロック]
				self.NotesRegardingFinancialAssetsBorrowedWhichBorrowerHasRightToSellOrRepledgeTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingLoanedSecuritiesAndFinancialAssetsBorrowedWhichBorrowerHasRightToSellOrRepledgeTextBlock': #有価証券の消費貸借契約・消費寄託契約及び自由処分権を有する担保受入金融資産に関する注記 [テキストブロック]
				self.NotesRegardingLoanedSecuritiesAndFinancialAssetsBorrowedWhichBorrowerHasRightToSellOrRepledgeTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingLoanParticipationsTextBlock': #ローン・パーティシペーションに関する注記 [テキストブロック]
				self.NotesRegardingLoanParticipationsTextBlock = fact.value

			elif fact.concept.qname.localName == 'CreditorsNotesRegardingOverdraftContractsAndOrLoanCommitmentsTextBlock': #当座貸越契約及び（又は）貸出コミットメントに関する貸手の注記 [テキストブロック]
				self.CreditorsNotesRegardingOverdraftContractsAndOrLoanCommitmentsTextBlock = fact.value

			elif fact.concept.qname.localName == 'DebtorsNotesRegardingOverdraftContractsAndOrLoanCommitmentsTextBlock': #当座貸越契約及び（又は）貸出コミットメントに関する借手の注記 [テキストブロック]
				self.DebtorsNotesRegardingOverdraftContractsAndOrLoanCommitmentsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingTotalAmountsOfSharesOfAndOrLoansToAffiliatedEntitiesTextBlock': #関係会社の株式及び（又は）出資金の総額 [テキストブロック]
				self.NotesRegardingTotalAmountsOfSharesOfAndOrLoansToAffiliatedEntitiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingTotalAmountsOfSharesOfAndOrLoansToUnconsolidatedSubsidiariesAndAssociatesTextBlock': #非連結子会社及び関連会社の株式及び（又は）出資金の総額 [テキストブロック]
				self.NotesRegardingTotalAmountsOfSharesOfAndOrLoansToUnconsolidatedSubsidiariesAndAssociatesTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingSubordinatedBorrowingsTextBlock': #劣後特約付借入金に関する注記 [テキストブロック]
				self.NotesRegardingSubordinatedBorrowingsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingSubordinatedBondsPayableTextBlock': #劣後特約付社債に関する注記 [テキストブロック]
				self.NotesRegardingSubordinatedBondsPayableTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingGuaranteeObligationForCorporateBondsIncludedInAssetsTextBlock': #資産の部の社債に係る保証債務に関する注記 [テキストブロック]
				self.NotesRegardingGuaranteeObligationForCorporateBondsIncludedInAssetsTextBlock = fact.value

			elif fact.concept.qname.localName == 'OtherElementsForNotesBalanceSheetOfBankAbstract': #銀行業の貸借対照表関係のその他の要素 [タイトル項目]
				self.OtherElementsForNotesBalanceSheetOfBankAbstract = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingLoansBasedOnBankingActAndActOnEmergencyMeasuresForRevitalizationOfFinancialFunctionsBNKTextBlock': #銀行法及び金融機能の再生のための緊急措置に関する法律に基づく債権に関する注記、銀行業 [テキストブロック]
				self.NotesRegardingLoansBasedOnBankingActAndActOnEmergencyMeasuresForRevitalizationOfFinancialFunctionsBNKTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingBillsDiscountedInBankingIndustryBNKTextBlock': #銀行業における手形割引に関する注記、銀行業 [テキストブロック]
				self.NotesRegardingBillsDiscountedInBankingIndustryBNKTextBlock = fact.value

			elif fact.concept.qname.localName == 'OtherElementsForNotesBalanceSheetOfSecuritiesRelatedBusinessAbstract': #第一種金融商品取引業の貸借対照表関係のその他の要素 [タイトル項目]
				self.OtherElementsForNotesBalanceSheetOfSecuritiesRelatedBusinessAbstract = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingMarketValueOfSecuritiesPledgedToCounterpartiesSECTextBlock': #差し入れた有価証券等の時価の注記、第一種金融商品取引業 [テキストブロック]
				self.NotesRegardingMarketValueOfSecuritiesPledgedToCounterpartiesSECTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingMarketValueOfSecuritiesReceivedAsCollateralFromCounterpartiesSECTextBlock': #差し入れを受けた有価証券等の時価の注記、第一種金融商品取引業 [テキストブロック]
				self.NotesRegardingMarketValueOfSecuritiesReceivedAsCollateralFromCounterpartiesSECTextBlock = fact.value

			elif fact.concept.qname.localName == 'BreakdownOfTradingAccountSecuritiesEtcSECTextBlock': #商品有価証券等の内訳、第一種金融商品取引業 [テキストブロック]
				self.BreakdownOfTradingAccountSecuritiesEtcSECTextBlock = fact.value

			elif fact.concept.qname.localName == 'OtherElementsForNotesBalanceSheetOfInsuranceAbstract': #保険業の貸借対照表関係のその他の要素 [タイトル項目]
				self.OtherElementsForNotesBalanceSheetOfInsuranceAbstract = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingLoansBasedOnInsuranceBusinessActINSTextBlock': #保険業法に基づく債権に関する注記、保険業 [テキストブロック]
				self.NotesRegardingLoansBasedOnInsuranceBusinessActINSTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingAssetsAndLiabilitiesIncludedInSpecificAccountsSpecifiedByArticle118OfInsuranceBusinessActINSTextBlock': #保険業法第118条に規定する特別勘定の資産及び負債に関する注記、保険業 [テキストブロック]
				self.NotesRegardingAssetsAndLiabilitiesIncludedInSpecificAccountsSpecifiedByArticle118OfInsuranceBusinessActINSTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingDeferredAssetsIncludedInOtherAssetsSpecifiedByArticle113OfInsuranceBusinessActTextBlock': #その他資産に含まれている保険業法第113条に規定する事業費の繰延額の注記 [テキストブロック]
				self.NotesRegardingDeferredAssetsIncludedInOtherAssetsSpecifiedByArticle113OfInsuranceBusinessActTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingIncreaseAndDecreaseInReserveForPolicyholderDividendsAndPaymentsOfPolicyholderDividendsINSTextBlock': #契約者配当準備金の増減異動及び契約者配当金の支払額に関する注記、保険業 [テキストブロック]
				self.NotesRegardingIncreaseAndDecreaseInReserveForPolicyholderDividendsAndPaymentsOfPolicyholderDividendsINSTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingSurplusFromOrganizationChangeSpecifiedByArticle91OfInsuranceBusinessActINSTextBlock': #保険業法第91条の規定による組織変更剰余金額の注記、保険業 [テキストブロック]
				self.NotesRegardingSurplusFromOrganizationChangeSpecifiedByArticle91OfInsuranceBusinessActINSTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingReservesForOutstandingClaimsReinsuredINSTextBlock': #保険業法施行規則第73条第3項において準用する同規則第71条第1項に規定する再保険を付した部分に相当する支払備金の金額の注記、保険業 [テキストブロック]
				self.NotesRegardingReservesForOutstandingClaimsReinsuredINSTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingPolicyReservesReinsuredINSTextBlock': #保険業法施行規則第71条第1項に規定する再保険を付した部分に相当する責任準備金の金額の注記、保険業 [テキストブロック]
				self.NotesRegardingPolicyReservesReinsuredINSTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingObligationsToLifeInsurancePolicyholdersProtectionCorporationOfJapanINSTextBlock': #保険業法第259条の規定に基づく生命保険契約者保護機構に対する今後の負担見積額、保険業 [テキストブロック]
				self.NotesRegardingObligationsToLifeInsurancePolicyholdersProtectionCorporationOfJapanINSTextBlock = fact.value

			elif fact.concept.qname.localName == 'BreakdownOfOutstandingClaimsINSTextBlock': #支払備金の内訳、保険業 [テキストブロック]
				self.BreakdownOfOutstandingClaimsINSTextBlock = fact.value

			elif fact.concept.qname.localName == 'BreakdownOfPolicyReserveINSTextBlock': #責任準備金の内訳、保険業 [テキストブロック]
				self.BreakdownOfPolicyReserveINSTextBlock = fact.value

			elif fact.concept.qname.localName == 'OtherElementsForNotesBalanceSheetOfSpecificFinanceAbstract': #特定金融業の貸借対照表関係のその他の要素 [タイトル項目]
				self.OtherElementsForNotesBalanceSheetOfSpecificFinanceAbstract = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingBadLoansSPFTextBlock': #不良債権に関する注記、特定金融業 [テキストブロック]
				self.NotesRegardingBadLoansSPFTextBlock = fact.value

			elif fact.concept.qname.localName == 'OtherElementsForNotesBalanceSheetOfCommodityFutureTradingAbstract': #商品先物取引業の貸借対照表関係のその他の要素 [タイトル項目]
				self.OtherElementsForNotesBalanceSheetOfCommodityFutureTradingAbstract = fact.value

			elif fact.concept.qname.localName == 'ExplanationOfFuturesTransactionMarginCustomerCMDTextBlock': #委託者先物取引差金の説明、商品先物取引業 [テキストブロック]
				self.ExplanationOfFuturesTransactionMarginCustomerCMDTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesStatementOfIncomeHeading': #損益計算書関係 [目次項目]
				self.NotesStatementOfIncomeHeading = fact.value

			elif fact.concept.qname.localName == 'NotesStatementOfIncomeHeading': #損益計算書関係 [目次項目]
				self.NotesStatementOfIncomeHeading = fact.value

			elif fact.concept.qname.localName == 'NotesStatementOfIncomeTable': #損益計算書関係 [表]
				self.NotesStatementOfIncomeTable = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedOrNonConsolidatedAxis': #連結個別 [軸]
				self.ConsolidatedOrNonConsolidatedAxis = fact.value

			elif fact.concept.qname.localName == 'NonConsolidatedMember': #非連結又は個別 [メンバー]
				self.NonConsolidatedMember = fact.value

			elif fact.concept.qname.localName == 'NotesStatementOfIncomeLineItems': #損益計算書関係 [表示項目]
				self.NotesStatementOfIncomeLineItems = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingAmountOfRevenueFromContractsWithCustomersTextBlock': #顧客との契約から生じる収益の金額の注記 [テキストブロック]
				self.NotesRegardingAmountOfRevenueFromContractsWithCustomersTextBlock = fact.value

			elif fact.concept.qname.localName == 'RevenueFromContractsWithCustomers': #顧客との契約から生じる収益
				self.RevenueFromContractsWithCustomers = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingRevenueFromAffiliatedEntitiesTextBlock': #関係会社に対する売上高の注記 [テキストブロック]
				self.NotesRegardingRevenueFromAffiliatedEntitiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingLossOnConstructionContractsTextBlock': #工事損失引当金繰入額の注記 [テキストブロック]
				self.NotesRegardingLossOnConstructionContractsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingWriteDownsOfInventoriesTextBlock': #棚卸資産の帳簿価額の切下げに関する注記 [テキストブロック]
				self.NotesRegardingWriteDownsOfInventoriesTextBlock = fact.value

			elif fact.concept.qname.localName == 'WriteDownsOfInventories': #棚卸資産帳簿価額切下額
				self.WriteDownsOfInventories = fact.value

			elif fact.concept.qname.localName == 'MajorComponentsOfSellingGeneralAndAdministrativeExpensesTextBlock': #主要な販売費及び一般管理費 [テキストブロック]
				self.MajorComponentsOfSellingGeneralAndAdministrativeExpensesTextBlock = fact.value

			elif fact.concept.qname.localName == 'DepreciationSGA': #減価償却費、販売費及び一般管理費
				self.DepreciationSGA = fact.value

			elif fact.concept.qname.localName == 'ProvisionOfAllowanceForDoubtfulAccountsSGA': #貸倒引当金繰入額、販売費及び一般管理費
				self.ProvisionOfAllowanceForDoubtfulAccountsSGA = fact.value

			elif fact.concept.qname.localName == 'MajorComponentsOfSellingExpensesAbstract': #主要な販売費 [タイトル項目]
				self.MajorComponentsOfSellingExpensesAbstract = fact.value

			elif fact.concept.qname.localName == 'RetirementBenefitExpensesSellingExpenses': #退職給付費用、販売費
				self.RetirementBenefitExpensesSellingExpenses = fact.value

			elif fact.concept.qname.localName == 'DepreciationSellingExpenses': #減価償却費、販売費
				self.DepreciationSellingExpenses = fact.value

			elif fact.concept.qname.localName == 'ProvisionForBonusesSellingExpenses': #賞与引当金繰入額、販売費
				self.ProvisionForBonusesSellingExpenses = fact.value

			elif fact.concept.qname.localName == 'MajorComponentsOfGeneralAndAdministrativeExpensesAbstract': #主要な一般管理費 [タイトル項目]
				self.MajorComponentsOfGeneralAndAdministrativeExpensesAbstract = fact.value

			elif fact.concept.qname.localName == 'RetirementBenefitExpensesGA': #退職給付費用、一般管理費
				self.RetirementBenefitExpensesGA = fact.value

			elif fact.concept.qname.localName == 'DepreciationGA': #減価償却費、一般管理費
				self.DepreciationGA = fact.value

			elif fact.concept.qname.localName == 'ProvisionForBonusesGA': #賞与引当金繰入額、一般管理費
				self.ProvisionForBonusesGA = fact.value

			elif fact.concept.qname.localName == 'ResearchAndDevelopmentExpensesIncludedInGeneralAndAdministrativeExpensesAndManufacturingCostForCurrentPeriodTextBlock': #一般管理費及び当期製造費用に含まれる研究開発費 [テキストブロック]
				self.ResearchAndDevelopmentExpensesIncludedInGeneralAndAdministrativeExpensesAndManufacturingCostForCurrentPeriodTextBlock = fact.value

			elif fact.concept.qname.localName == 'ResearchAndDevelopmentExpensesIncludedInGeneralAndAdministrativeExpensesAndManufacturingCostForCurrentPeriod': #一般管理費及び当期製造費用に含まれる研究開発費
				self.ResearchAndDevelopmentExpensesIncludedInGeneralAndAdministrativeExpensesAndManufacturingCostForCurrentPeriod = fact.value

			elif fact.concept.qname.localName == 'ResearchAndDevelopmentExpensesSGA': #研究開発費、販売費及び一般管理費
				self.ResearchAndDevelopmentExpensesSGA = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingOperatingExpensesIncurredFromTransactionsWithAffiliatedEntitiesTextBlock': #関係会社に係る営業費用の注記 [テキストブロック]
				self.NotesRegardingOperatingExpensesIncurredFromTransactionsWithAffiliatedEntitiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingNonOperatingIncomeAndNonOperatingExpensesIncurredFromTransactionsWithAffiliatedEntitiesTextBlock': #関係会社に係る営業外収益・営業外費用の注記 [テキストブロック]
				self.NotesRegardingNonOperatingIncomeAndNonOperatingExpensesIncurredFromTransactionsWithAffiliatedEntitiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingTotalAmountOfOperatingTransactionsFromOrToAffiliatedEntitiesAndTotalAmountOfNonOperatingTransactionsFromOrToAffiliatedEntitiesTextBlock': #関係会社との営業取引による取引高の総額及び営業取引以外の取引による取引高の総額の注記 [テキストブロック]
				self.NotesRegardingTotalAmountOfOperatingTransactionsFromOrToAffiliatedEntitiesAndTotalAmountOfNonOperatingTransactionsFromOrToAffiliatedEntitiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingImpairmentLossTextBlock': #減損損失に関する注記 [テキストブロック]
				self.NotesRegardingImpairmentLossTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingReversalOfProvisionIncurredFromBusinessCombinationTextBlock': #企業結合に係る特定勘定の取崩益の注記 [テキストブロック]
				self.NotesRegardingReversalOfProvisionIncurredFromBusinessCombinationTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingGainOnSalesOfPropertyPlantAndEquipmentTextBlock': #固定資産売却益の注記 [テキストブロック]
				self.NotesRegardingGainOnSalesOfPropertyPlantAndEquipmentTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingLossOnSalesOfPropertyPlantAndEquipmentTextBlock': #固定資産売却損の注記 [テキストブロック]
				self.NotesRegardingLossOnSalesOfPropertyPlantAndEquipmentTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingLossOnDisposalOfPropertyPlantAndEquipmentTextBlock': #固定資産除却損の注記 [テキストブロック]
				self.NotesRegardingLossOnDisposalOfPropertyPlantAndEquipmentTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingLossOnDisposalAndSalesOfPropertyPlantAndEquipmentTextBlock': #固定資産除売却損の注記 [テキストブロック]
				self.NotesRegardingLossOnDisposalAndSalesOfPropertyPlantAndEquipmentTextBlock = fact.value

			elif fact.concept.qname.localName == 'OtherElementsForNotesStatementOfIncomeAbstract': #損益計算書関係のその他の要素 [タイトル項目]
				self.OtherElementsForNotesStatementOfIncomeAbstract = fact.value

			elif fact.concept.qname.localName == 'BreakdownOfBusinessCostTextBlock': #事業費の内訳 [テキストブロック]
				self.BreakdownOfBusinessCostTextBlock = fact.value

			elif fact.concept.qname.localName == 'BreakdownOfPersonnelExpensesTextBlock': #人件費の内訳 [テキストブロック]
				self.BreakdownOfPersonnelExpensesTextBlock = fact.value

			elif fact.concept.qname.localName == 'BreakdownOfGainOnSalesOfSecuritiesTextBlock': #有価証券売却益の内訳 [テキストブロック]
				self.BreakdownOfGainOnSalesOfSecuritiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'BreakdownOfLossOnSalesOfSecuritiesTextBlock': #有価証券売却損の内訳 [テキストブロック]
				self.BreakdownOfLossOnSalesOfSecuritiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'BreakdownOfLossOnValuationOfSecuritiesTextBlock': #有価証券評価損の内訳 [テキストブロック]
				self.BreakdownOfLossOnValuationOfSecuritiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingTransactionsWithAffiliatedEntitiesTextBlock': #関係会社との取引に関する注記 [テキストブロック]
				self.NotesRegardingTransactionsWithAffiliatedEntitiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'OtherElementsForNotesStatementOfIncomeOfBankAbstract': #銀行業の損益計算書関係のその他の要素 [タイトル項目]
				self.OtherElementsForNotesStatementOfIncomeOfBankAbstract = fact.value

			elif fact.concept.qname.localName == 'MajorComponentsOfOtherIncomeBNKTextBlock': #その他の経常収益の主要な内訳、銀行業 [テキストブロック]
				self.MajorComponentsOfOtherIncomeBNKTextBlock = fact.value

			elif fact.concept.qname.localName == 'MajorComponentsOfOtherExpensesBNKTextBlock': #その他の経常費用の主要な内訳、銀行業 [テキストブロック]
				self.MajorComponentsOfOtherExpensesBNKTextBlock = fact.value

			elif fact.concept.qname.localName == 'OtherElementsForNotesStatementOfIncomeOfSecuritiesRelatedBusinessAbstract': #第一種金融商品取引業の損益計算書関係のその他の要素 [タイトル項目]
				self.OtherElementsForNotesStatementOfIncomeOfSecuritiesRelatedBusinessAbstract = fact.value

			elif fact.concept.qname.localName == 'BreakdownOfNetTradingIncomeSECTextBlock': #トレーディング損益の内訳、第一種金融商品取引業 [テキストブロック]
				self.BreakdownOfNetTradingIncomeSECTextBlock = fact.value

			elif fact.concept.qname.localName == 'BreakdownOfFinancialRevenueSECTextBlock': #金融収益の内訳、第一種金融商品取引業 [テキストブロック]
				self.BreakdownOfFinancialRevenueSECTextBlock = fact.value

			elif fact.concept.qname.localName == 'BreakdownOfFinancialExpensesSECTextBlock': #金融費用の内訳、第一種金融商品取引業 [テキストブロック]
				self.BreakdownOfFinancialExpensesSECTextBlock = fact.value

			elif fact.concept.qname.localName == 'OtherElementsForNotesStatementOfIncomeOfInsuranceAbstract': #保険業の損益計算書関係のその他の要素 [タイトル項目]
				self.OtherElementsForNotesStatementOfIncomeOfInsuranceAbstract = fact.value

			elif fact.concept.qname.localName == 'MajorComponentsOfBusinessCostTextBlock': #事業費の主な内訳 [テキストブロック]
				self.MajorComponentsOfBusinessCostTextBlock = fact.value

			elif fact.concept.qname.localName == 'AgentFeeEtcINSNonlife': #代理店手数料等、損害保険業
				self.AgentFeeEtcINSNonlife = fact.value

			elif fact.concept.qname.localName == 'SalariesINSNonlife': #給与、損害保険業
				self.SalariesINSNonlife = fact.value

			elif fact.concept.qname.localName == 'BreakdownOfNetPremiumsWrittenINSTextBlock': #正味収入保険料の内訳、保険業 [テキストブロック]
				self.BreakdownOfNetPremiumsWrittenINSTextBlock = fact.value

			elif fact.concept.qname.localName == 'BreakdownOfNetClaimsPaidINSTextBlock': #正味支払保険金の内訳、保険業 [テキストブロック]
				self.BreakdownOfNetClaimsPaidINSTextBlock = fact.value

			elif fact.concept.qname.localName == 'BreakdownOfCommissionsAndCollectionFeesINSTextBlock': #諸手数料及び集金費の内訳、保険業 [テキストブロック]
				self.BreakdownOfCommissionsAndCollectionFeesINSTextBlock = fact.value

			elif fact.concept.qname.localName == 'BreakdownOfProvisionForOrReversalOfOutstandingClaimsINSTextBlock': #支払備金繰入額又は支払備金戻入額の内訳、保険業 [テキストブロック]
				self.BreakdownOfProvisionForOrReversalOfOutstandingClaimsINSTextBlock = fact.value

			elif fact.concept.qname.localName == 'BreakdownOfProvisionForOrReversalOfUnderwritingReservesINSTextBlock': #責任準備金繰入額又は責任準備金戻入額の内訳、保険業 [テキストブロック]
				self.BreakdownOfProvisionForOrReversalOfUnderwritingReservesINSTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingReversalOfOrProvisionForReservesForOutstandingClaimsReinsuredINSTextBlock': #支払備金繰入額又は支払備金戻入額の計算上、差し引かれた又は足し上げられた出再支払備金繰入額又は出再支払備金戻入額の注記、保険業 [テキストブロック]
				self.NotesRegardingReversalOfOrProvisionForReservesForOutstandingClaimsReinsuredINSTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingReversalOfOrProvisionForPolicyReservesReinsuredINSTextBlock': #責任準備金繰入額又は責任準備金戻入額の計算上、差し引かれた又は足し上げられた出再責任準備金繰入額又は出再責任準備金戻入額の注記、保険業 [テキストブロック]
				self.NotesRegardingReversalOfOrProvisionForPolicyReservesReinsuredINSTextBlock = fact.value

			elif fact.concept.qname.localName == 'BreakdownOfInterestAndDividendIncomeBySourceAssetINSTextBlock': #利息及び配当金収入の資産源泉別内訳、保険業 [テキストブロック]
				self.BreakdownOfInterestAndDividendIncomeBySourceAssetINSTextBlock = fact.value

			elif fact.concept.qname.localName == 'InterestAndDividendIncomeGainLossOnSalesAndUnrealizedGainLossForEachOfTradingAccountSecuritiesINSTextBlock': #商品有価証券及び売買目的有価証券に係るそれぞれの利息及び配当金収入、売却損益及び評価損益の金額、保険業 [テキストブロック]
				self.InterestAndDividendIncomeGainLossOnSalesAndUnrealizedGainLossForEachOfTradingAccountSecuritiesINSTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingUnrealizedGainLossForMoneyTrustINSTextBlock': #金銭の信託に係る評価損益の金額の注記、保険業 [テキストブロック]
				self.NotesRegardingUnrealizedGainLossForMoneyTrustINSTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingUnrealizedGainLossForDerivativesINSTextBlock': #金融派生商品に係る評価損益の金額の注記、保険業 [テキストブロック]
				self.NotesRegardingUnrealizedGainLossForDerivativesINSTextBlock = fact.value

			elif fact.concept.qname.localName == 'MajorComponentsOfOtherExtraordinaryIncomeINSTextBlock': #その他特別利益の主な内訳、保険業 [テキストブロック]
				self.MajorComponentsOfOtherExtraordinaryIncomeINSTextBlock = fact.value

			elif fact.concept.qname.localName == 'MajorComponentsOfOtherExtraordinaryLossesINSTextBlock': #その他特別損失の主な内訳、保険業 [テキストブロック]
				self.MajorComponentsOfOtherExtraordinaryLossesINSTextBlock = fact.value

			elif fact.concept.qname.localName == 'OtherElementsForNotesStatementOfIncomeOfCommodityFutureTradingAbstract': #商品先物取引業の損益計算書関係のその他の要素 [タイトル項目]
				self.OtherElementsForNotesStatementOfIncomeOfCommodityFutureTradingAbstract = fact.value

			elif fact.concept.qname.localName == 'BreakdownOfBrokerageIncomeCMDTextBlock': #受取手数料の内訳、商品先物取引業 [テキストブロック]
				self.BreakdownOfBrokerageIncomeCMDTextBlock = fact.value

			elif fact.concept.qname.localName == 'BreakdownOfNetGainOnTradingCMDTextBlock': #売買損益の内訳、商品先物取引業 [テキストブロック]
				self.BreakdownOfNetGainOnTradingCMDTextBlock = fact.value

			elif fact.concept.qname.localName == 'ExchangeRelatedExpensesCMDTextBlock': #取引所等関係費の内訳、商品先物取引業 [テキストブロック]
				self.ExchangeRelatedExpensesCMDTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesStatementOfChangesInEquityHeading': #株主資本等変動計算書関係 [目次項目]
				self.NotesStatementOfChangesInEquityHeading = fact.value

			elif fact.concept.qname.localName == 'NotesStatementOfChangesInEquityHeading': #株主資本等変動計算書関係 [目次項目]
				self.NotesStatementOfChangesInEquityHeading = fact.value

			elif fact.concept.qname.localName == 'NotesStatementOfChangesInEquityTable': #株主資本等変動計算書関係 [表]
				self.NotesStatementOfChangesInEquityTable = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedOrNonConsolidatedAxis': #連結個別 [軸]
				self.ConsolidatedOrNonConsolidatedAxis = fact.value

			elif fact.concept.qname.localName == 'NonConsolidatedMember': #非連結又は個別 [メンバー]
				self.NonConsolidatedMember = fact.value

			elif fact.concept.qname.localName == 'NotesStatementOfChangesInEquityLineItems': #株主資本等変動計算書関係 [表示項目]
				self.NotesStatementOfChangesInEquityLineItems = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingIssuedSharesAndTreasurySharesTextBlock': #発行済株式及び自己株式に関する注記 [テキストブロック]
				self.NotesRegardingIssuedSharesAndTreasurySharesTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingTreasurySharesTextBlock': #自己株式に関する注記 [テキストブロック]
				self.NotesRegardingTreasurySharesTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingNewShareSubscriptionRightsEtcTextBlock': #新株予約権等に関する注記 [テキストブロック]
				self.NotesRegardingNewShareSubscriptionRightsEtcTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRegardingDividendTextBlock': #配当に関する注記 [テキストブロック]
				self.NotesRegardingDividendTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesStatementOfCashFlowsHeading': #キャッシュ・フロー計算書関係 [目次項目]
				self.NotesStatementOfCashFlowsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesStatementOfCashFlowsHeading': #キャッシュ・フロー計算書関係 [目次項目]
				self.NotesStatementOfCashFlowsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesStatementOfCashFlowsTable': #キャッシュ・フロー計算書関係 [表]
				self.NotesStatementOfCashFlowsTable = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedOrNonConsolidatedAxis': #連結個別 [軸]
				self.ConsolidatedOrNonConsolidatedAxis = fact.value

			elif fact.concept.qname.localName == 'NonConsolidatedMember': #非連結又は個別 [メンバー]
				self.NonConsolidatedMember = fact.value

			elif fact.concept.qname.localName == 'NotesStatementOfCashFlowsLineItems': #キャッシュ・フロー計算書関係 [表示項目]
				self.NotesStatementOfCashFlowsLineItems = fact.value

			elif fact.concept.qname.localName == 'ReconciliationOfEndingBalanceOfCashAndCashEquivalentsWithAccountBalancesPerBalanceSheetTextBlock': #現金及び現金同等物の期末残高と貸借対照表に掲記されている科目の金額との関係 [テキストブロック]
				self.ReconciliationOfEndingBalanceOfCashAndCashEquivalentsWithAccountBalancesPerBalanceSheetTextBlock = fact.value

			elif fact.concept.qname.localName == 'MajorComponentsOfAssetsAndLiabilitiesIncreasedOrDecreasedAsResultOfAcquisitionOrDisposalOfBusinessOrMergerEtcWherebyCashWasPaidOrReceivedAsConsiderationTextBlock': #現金及び現金同等物を対価とする事業の譲受け若しくは譲渡又は合併等を行った場合には、当該事業の譲受け若しくは譲渡又は合併等により増加又は減少した資産及び負債の主な内訳 [テキストブロック]
				self.MajorComponentsOfAssetsAndLiabilitiesIncreasedOrDecreasedAsResultOfAcquisitionOrDisposalOfBusinessOrMergerEtcWherebyCashWasPaidOrReceivedAsConsiderationTextBlock = fact.value

			elif fact.concept.qname.localName == 'DescriptionOfSignificantTransactionsNotRequiringUseOfCashOrCashEquivalentsTextBlock': #重要な非資金取引の内容 [テキストブロック]
				self.DescriptionOfSignificantTransactionsNotRequiringUseOfCashOrCashEquivalentsTextBlock = fact.value

			elif fact.concept.qname.localName == 'DescriptionOfFactThatCashFlowsFromUsedInInvestingActivitiesIncludeCashFlowsFromAssetManagementActivitiesRelatedToInsuranceBusinessINSTextBlock': #投資活動によるキャッシュ・フローには、保険事業に係る資産運用業務から生じるキャッシュ・フローを含んでいる旨、保険業 [テキストブロック]
				self.DescriptionOfFactThatCashFlowsFromUsedInInvestingActivitiesIncludeCashFlowsFromAssetManagementActivitiesRelatedToInsuranceBusinessINSTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesLeasesFinancialStatementsHeading': #リース取引関係、財務諸表 [目次項目]
				self.NotesLeasesFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesLeasesFinancialStatementsTextBlock': #リース取引関係、財務諸表 [テキストブロック]
				self.NotesLeasesFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesFinancialInstrumentsFinancialStatementsHeading': #金融商品関係、財務諸表 [目次項目]
				self.NotesFinancialInstrumentsFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesFinancialInstrumentsFinancialStatementsTextBlock': #金融商品関係、財務諸表 [テキストブロック]
				self.NotesFinancialInstrumentsFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesSecuritiesFinancialStatementsHeading': #有価証券関係、財務諸表 [目次項目]
				self.NotesSecuritiesFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesSecuritiesFinancialStatementsTextBlock': #有価証券関係、財務諸表 [テキストブロック]
				self.NotesSecuritiesFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesMoneyHeldInTrustFinancialStatementsHeading': #金銭の信託関係、財務諸表 [目次項目]
				self.NotesMoneyHeldInTrustFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesMoneyHeldInTrustFinancialStatementsTextBlock': #金銭の信託関係、財務諸表 [テキストブロック]
				self.NotesMoneyHeldInTrustFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesValuationDifferenceOnAvailableForSaleSecuritiesFinancialStatementsHeading': #その他有価証券評価差額金、財務諸表 [目次項目]
				self.NotesValuationDifferenceOnAvailableForSaleSecuritiesFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesValuationDifferenceOnAvailableForSaleSecuritiesFinancialStatementsTextBlock': #その他有価証券評価差額金、財務諸表 [テキストブロック]
				self.NotesValuationDifferenceOnAvailableForSaleSecuritiesFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesDerivativesFinancialStatementsHeading': #デリバティブ取引関係、財務諸表 [目次項目]
				self.NotesDerivativesFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesDerivativesFinancialStatementsTextBlock': #デリバティブ取引関係、財務諸表 [テキストブロック]
				self.NotesDerivativesFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRetirementBenefitsFinancialStatementsHeading': #退職給付関係、財務諸表 [目次項目]
				self.NotesRetirementBenefitsFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesRetirementBenefitsFinancialStatementsTextBlock': #退職給付関係、財務諸表 [テキストブロック]
				self.NotesRetirementBenefitsFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesShareOptionsEtcFinancialStatementsHeading': #ストック・オプション等関係、財務諸表 [目次項目]
				self.NotesShareOptionsEtcFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesShareOptionsEtcFinancialStatementsTextBlock': #ストック・オプション等関係、財務諸表 [テキストブロック]
				self.NotesShareOptionsEtcFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesTaxEffectAccountingFinancialStatementsHeading': #税効果会計関係、財務諸表 [目次項目]
				self.NotesTaxEffectAccountingFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesTaxEffectAccountingFinancialStatementsTextBlock': #税効果会計関係、財務諸表 [テキストブロック]
				self.NotesTaxEffectAccountingFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesBusinessCombinationsFinancialStatementsHeading': #企業結合等関係、財務諸表 [目次項目]
				self.NotesBusinessCombinationsFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesBusinessCombinationsFinancialStatementsTextBlock': #企業結合等関係、財務諸表 [テキストブロック]
				self.NotesBusinessCombinationsFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesAssetRetirementObligationsFinancialStatementsHeading': #資産除去債務関係、財務諸表 [目次項目]
				self.NotesAssetRetirementObligationsFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesAssetRetirementObligationsFinancialStatementsTextBlock': #資産除去債務関係、財務諸表 [テキストブロック]
				self.NotesAssetRetirementObligationsFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRealEstateForLeaseEtcFinancialStatementsHeading': #賃貸等不動産関係、財務諸表 [目次項目]
				self.NotesRealEstateForLeaseEtcFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesRealEstateForLeaseEtcFinancialStatementsTextBlock': #賃貸等不動産関係、財務諸表 [テキストブロック]
				self.NotesRealEstateForLeaseEtcFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRevenueRecognitionFinancialStatementsHeading': #収益認識関係、財務諸表 [目次項目]
				self.NotesRevenueRecognitionFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesRevenueRecognitionFinancialStatementsTextBlock': #収益認識関係、財務諸表 [テキストブロック]
				self.NotesRevenueRecognitionFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesInventoriesFinancialStatementsHeading': #棚卸資産関係、財務諸表 [目次項目]
				self.NotesInventoriesFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesInventoriesFinancialStatementsTextBlock': #棚卸資産関係、財務諸表 [テキストブロック]
				self.NotesInventoriesFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesSegmentInformationEtcFinancialStatementsHeading': #セグメント情報等、財務諸表 [目次項目]
				self.NotesSegmentInformationEtcFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesSegmentInformationEtcFinancialStatementsTextBlock': #セグメント情報等、財務諸表 [テキストブロック]
				self.NotesSegmentInformationEtcFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesSegmentInformationEtcFinancialStatementsHeading': #セグメント情報等、財務諸表 [目次項目]
				self.NotesSegmentInformationEtcFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesSegmentInformationEtcFinancialStatementsTable': #セグメント情報等、財務諸表 [表]
				self.NotesSegmentInformationEtcFinancialStatementsTable = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedOrNonConsolidatedAxis': #連結個別 [軸]
				self.ConsolidatedOrNonConsolidatedAxis = fact.value

			elif fact.concept.qname.localName == 'NonConsolidatedMember': #非連結又は個別 [メンバー]
				self.NonConsolidatedMember = fact.value

			elif fact.concept.qname.localName == 'NotesSegmentInformationEtcFinancialStatementsLineItems': #セグメント情報等、財務諸表 [表示項目]
				self.NotesSegmentInformationEtcFinancialStatementsLineItems = fact.value

			elif fact.concept.qname.localName == 'SegmentInformationAbstract': #セグメント情報 [タイトル項目]
				self.SegmentInformationAbstract = fact.value

			elif fact.concept.qname.localName == 'DescriptionOfReportableSegmentsTextBlock': #報告セグメントの概要 [テキストブロック]
				self.DescriptionOfReportableSegmentsTextBlock = fact.value

			elif fact.concept.qname.localName == 'DisclosureOfChangesInReportableSegmentsTextBlock': #報告セグメントの変更に関する事項 [テキストブロック]
				self.DisclosureOfChangesInReportableSegmentsTextBlock = fact.value

			elif fact.concept.qname.localName == 'DescriptionOfFactThatCompanysBusinessComprisesSingleSegment': #単一セグメントである旨
				self.DescriptionOfFactThatCompanysBusinessComprisesSingleSegment = fact.value

			elif fact.concept.qname.localName == 'ExplanationOfMeasurementsOfSalesProfitLossAssetLiabilityAndOtherItemsForEachReportableSegmentTextBlock': #報告セグメントごとの売上高、利益又は損失、資産、負債その他の項目の金額の算定方法 [テキストブロック]
				self.ExplanationOfMeasurementsOfSalesProfitLossAssetLiabilityAndOtherItemsForEachReportableSegmentTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesSegmentInformationEtcFinancialStatementsHeading': #セグメント情報等、財務諸表 [目次項目]
				self.NotesSegmentInformationEtcFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'SegmentInformationAbstract': #セグメント情報 [タイトル項目]
				self.SegmentInformationAbstract = fact.value

			elif fact.concept.qname.localName == 'DisclosureOfSalesProfitLossAssetLiabilityAndOtherItemsForEachReportableSegmentTable': #報告セグメントごとの売上高、利益又は損失、資産、負債その他の項目の金額に関する情報 [表]
				self.DisclosureOfSalesProfitLossAssetLiabilityAndOtherItemsForEachReportableSegmentTable = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedOrNonConsolidatedAxis': #連結個別 [軸]
				self.ConsolidatedOrNonConsolidatedAxis = fact.value

			elif fact.concept.qname.localName == 'NonConsolidatedMember': #非連結又は個別 [メンバー]
				self.NonConsolidatedMember = fact.value

			elif fact.concept.qname.localName == 'OperatingSegmentsAxis': #事業セグメント [軸]
				self.OperatingSegmentsAxis = fact.value

			elif fact.concept.qname.localName == 'EntityTotalMember': #連結合計又は会社合計 [メンバー] ※ディメンションデフォルト
				self.EntityTotalMember = fact.value

			elif fact.concept.qname.localName == 'TotalOfReportableSegmentsAndOthersMember': #報告セグメント及びその他の合計 [メンバー]
				self.TotalOfReportableSegmentsAndOthersMember = fact.value

			elif fact.concept.qname.localName == 'ReportableSegmentsMember': #報告セグメント [メンバー]
				self.ReportableSegmentsMember = fact.value

			elif fact.concept.qname.localName == 'OtherReportableSegmentsMember': #その他の報告セグメント [メンバー]
				self.OtherReportableSegmentsMember = fact.value

			elif fact.concept.qname.localName == 'OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember': #報告セグメント以外の全てのセグメント [メンバー]
				self.OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember = fact.value

			elif fact.concept.qname.localName == 'ReconcilingItemsMember': #調整項目 [メンバー]
				self.ReconcilingItemsMember = fact.value

			elif fact.concept.qname.localName == 'DisclosureOfSalesProfitLossAssetLiabilityAndOtherItemsForEachReportableSegmentLineItems': #報告セグメントごとの売上高、利益又は損失、資産、負債その他の項目の金額に関する情報 [表示項目]
				self.DisclosureOfSalesProfitLossAssetLiabilityAndOtherItemsForEachReportableSegmentLineItems = fact.value

			elif fact.concept.qname.localName == 'SalesSegmentInformationAbstract': #売上高、セグメント情報 [タイトル項目]
				self.SalesSegmentInformationAbstract = fact.value

			elif fact.concept.qname.localName == 'RevenuesFromExternalCustomers': #外部顧客への売上高
				self.RevenuesFromExternalCustomers = fact.value

			elif fact.concept.qname.localName == 'TransactionsWithOtherSegments': #セグメント間の内部売上高又は振替高
				self.TransactionsWithOtherSegments = fact.value

			elif fact.concept.qname.localName == 'NetSales': #売上高
				self.NetSales = fact.value

			elif fact.concept.qname.localName == 'OperatingRevenue1': #営業収益
				self.OperatingRevenue1 = fact.value

			elif fact.concept.qname.localName == 'OperatingRevenue2': #営業収入
				self.OperatingRevenue2 = fact.value

			elif fact.concept.qname.localName == 'GrossOperatingRevenue': #営業総収入
				self.GrossOperatingRevenue = fact.value

			elif fact.concept.qname.localName == 'OrdinaryIncomeBNK': #経常収益、銀行業
				self.OrdinaryIncomeBNK = fact.value

			elif fact.concept.qname.localName == 'OperatingIncomeINS': #経常収益、保険業
				self.OperatingIncomeINS = fact.value

			elif fact.concept.qname.localName == 'SegmentProfitLossAbstract': #セグメント利益又は損失（△） [タイトル項目]
				self.SegmentProfitLossAbstract = fact.value

			elif fact.concept.qname.localName == 'OperatingIncome': #営業利益又は営業損失（△）
				self.OperatingIncome = fact.value

			elif fact.concept.qname.localName == 'OrdinaryIncome': #経常利益又は経常損失（△）
				self.OrdinaryIncome = fact.value

			elif fact.concept.qname.localName == 'IncomeBeforeIncomeTaxes': #税引前当期純利益又は税引前当期純損失（△）
				self.IncomeBeforeIncomeTaxes = fact.value

			elif fact.concept.qname.localName == 'ProfitLoss': #当期純利益又は当期純損失（△）（平成26年3月28日財規等改正後）
				self.ProfitLoss = fact.value

			elif fact.concept.qname.localName == 'Assets': #資産
				self.Assets = fact.value

			elif fact.concept.qname.localName == 'Liabilities': #負債
				self.Liabilities = fact.value

			elif fact.concept.qname.localName == 'OtherItemsSegmentInformationAbstract': #その他の項目、セグメント情報 [タイトル項目]
				self.OtherItemsSegmentInformationAbstract = fact.value

			elif fact.concept.qname.localName == 'DepreciationSegmentInformation': #減価償却費、セグメント情報
				self.DepreciationSegmentInformation = fact.value

			elif fact.concept.qname.localName == 'AmortizationOfGoodwillSGA': #のれん償却額、販売費及び一般管理費
				self.AmortizationOfGoodwillSGA = fact.value

			elif fact.concept.qname.localName == 'InterestIncomeNOI': #受取利息、営業外収益
				self.InterestIncomeNOI = fact.value

			elif fact.concept.qname.localName == 'InterestExpensesNOE': #支払利息、営業外費用
				self.InterestExpensesNOE = fact.value

			elif fact.concept.qname.localName == 'ExtraordinaryIncome': #特別利益
				self.ExtraordinaryIncome = fact.value

			elif fact.concept.qname.localName == 'GainOnNegativeGoodwillEI': #負ののれん発生益、特別利益
				self.GainOnNegativeGoodwillEI = fact.value

			elif fact.concept.qname.localName == 'ExtraordinaryLoss': #特別損失
				self.ExtraordinaryLoss = fact.value

			elif fact.concept.qname.localName == 'ImpairmentLossEL': #減損損失、特別損失
				self.ImpairmentLossEL = fact.value

			elif fact.concept.qname.localName == 'IncomeTaxExpense': #税金費用
				self.IncomeTaxExpense = fact.value

			elif fact.concept.qname.localName == 'IncreaseInPropertyPlantAndEquipmentAndIntangibleAssets': #有形固定資産及び無形固定資産の増加額
				self.IncreaseInPropertyPlantAndEquipmentAndIntangibleAssets = fact.value

			elif fact.concept.qname.localName == 'NotesSegmentInformationEtcFinancialStatementsHeading': #セグメント情報等、財務諸表 [目次項目]
				self.NotesSegmentInformationEtcFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesSegmentInformationEtcFinancialStatementsTable': #セグメント情報等、財務諸表 [表]
				self.NotesSegmentInformationEtcFinancialStatementsTable = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedOrNonConsolidatedAxis': #連結個別 [軸]
				self.ConsolidatedOrNonConsolidatedAxis = fact.value

			elif fact.concept.qname.localName == 'NonConsolidatedMember': #非連結又は個別 [メンバー]
				self.NonConsolidatedMember = fact.value

			elif fact.concept.qname.localName == 'NotesSegmentInformationEtcFinancialStatementsLineItems': #セグメント情報等、財務諸表 [表示項目]
				self.NotesSegmentInformationEtcFinancialStatementsLineItems = fact.value

			elif fact.concept.qname.localName == 'SegmentInformationAbstract': #セグメント情報 [タイトル項目]
				self.SegmentInformationAbstract = fact.value

			elif fact.concept.qname.localName == 'FootnotesRegardingSegmentInformationTableTextBlock': #セグメント表の脚注 [テキストブロック]
				self.FootnotesRegardingSegmentInformationTableTextBlock = fact.value

			elif fact.concept.qname.localName == 'DescriptionOfNatureAndAmountsOfDifferencesBetweenReportableSegmentsTotalAndFinancialStatementsTextBlock': #報告セグメント合計額と財務諸表計上額との差額及び当該差額の主な内容（差異調整に関する事項） [テキストブロック]
				self.DescriptionOfNatureAndAmountsOfDifferencesBetweenReportableSegmentsTotalAndFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesInformationAssociatedWithReportableSegmentsAbstract': #関連情報 [タイトル項目]
				self.NotesInformationAssociatedWithReportableSegmentsAbstract = fact.value

			elif fact.concept.qname.localName == 'InformationForEachProductOrServiceTextBlock': #製品及びサービスごとの情報 [テキストブロック]
				self.InformationForEachProductOrServiceTextBlock = fact.value

			elif fact.concept.qname.localName == 'InformationForEachRegionAbstract': #地域ごとの情報 [タイトル項目]
				self.InformationForEachRegionAbstract = fact.value

			elif fact.concept.qname.localName == 'RevenuesFromExternalCustomersInformationForEachRegionTextBlock': #売上高、地域ごとの情報 [テキストブロック]
				self.RevenuesFromExternalCustomersInformationForEachRegionTextBlock = fact.value

			elif fact.concept.qname.localName == 'PropertyPlantAndEquipmentInformationForEachRegionTextBlock': #有形固定資産、地域ごとの情報 [テキストブロック]
				self.PropertyPlantAndEquipmentInformationForEachRegionTextBlock = fact.value

			elif fact.concept.qname.localName == 'InformationForEachOfMainCustomersTextBlock': #主要な顧客ごとの情報 [テキストブロック]
				self.InformationForEachOfMainCustomersTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesSegmentInformationEtcFinancialStatementsHeading': #セグメント情報等、財務諸表 [目次項目]
				self.NotesSegmentInformationEtcFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'DisclosureOfImpairmentLossOnNonCurrentAssetsForEachReportableSegmentAbstract': #報告セグメントごとの固定資産の減損損失に関する情報 [タイトル項目]
				self.DisclosureOfImpairmentLossOnNonCurrentAssetsForEachReportableSegmentAbstract = fact.value

			elif fact.concept.qname.localName == 'DisclosureOfImpairmentLossOnNonCurrentAssetsForEachReportableSegmentTable': #報告セグメントごとの固定資産の減損損失に関する情報 [表]
				self.DisclosureOfImpairmentLossOnNonCurrentAssetsForEachReportableSegmentTable = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedOrNonConsolidatedAxis': #連結個別 [軸]
				self.ConsolidatedOrNonConsolidatedAxis = fact.value

			elif fact.concept.qname.localName == 'NonConsolidatedMember': #非連結又は個別 [メンバー]
				self.NonConsolidatedMember = fact.value

			elif fact.concept.qname.localName == 'OperatingSegmentsAxis': #事業セグメント [軸]
				self.OperatingSegmentsAxis = fact.value

			elif fact.concept.qname.localName == 'EntityTotalMember': #連結合計又は会社合計 [メンバー] ※ディメンションデフォルト
				self.EntityTotalMember = fact.value

			elif fact.concept.qname.localName == 'ReportableSegmentsMember': #報告セグメント [メンバー]
				self.ReportableSegmentsMember = fact.value

			elif fact.concept.qname.localName == 'OtherReportableSegmentsMember': #その他の報告セグメント [メンバー]
				self.OtherReportableSegmentsMember = fact.value

			elif fact.concept.qname.localName == 'OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember': #報告セグメント以外の全てのセグメント [メンバー]
				self.OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember = fact.value

			elif fact.concept.qname.localName == 'UnallocatedAmountsAndEliminationMember': #全社・消去 [メンバー]
				self.UnallocatedAmountsAndEliminationMember = fact.value

			elif fact.concept.qname.localName == 'DisclosureOfImpairmentLossOnNonCurrentAssetsForEachReportableSegmentLineItems': #報告セグメントごとの固定資産の減損損失に関する情報 [表示項目]
				self.DisclosureOfImpairmentLossOnNonCurrentAssetsForEachReportableSegmentLineItems = fact.value

			elif fact.concept.qname.localName == 'ImpairmentLossEL': #減損損失、特別損失
				self.ImpairmentLossEL = fact.value

			elif fact.concept.qname.localName == 'NotesSegmentInformationEtcFinancialStatementsHeading': #セグメント情報等、財務諸表 [目次項目]
				self.NotesSegmentInformationEtcFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesSegmentInformationEtcFinancialStatementsTable': #セグメント情報等、財務諸表 [表]
				self.NotesSegmentInformationEtcFinancialStatementsTable = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedOrNonConsolidatedAxis': #連結個別 [軸]
				self.ConsolidatedOrNonConsolidatedAxis = fact.value

			elif fact.concept.qname.localName == 'NonConsolidatedMember': #非連結又は個別 [メンバー]
				self.NonConsolidatedMember = fact.value

			elif fact.concept.qname.localName == 'NotesSegmentInformationEtcFinancialStatementsLineItems': #セグメント情報等、財務諸表 [表示項目]
				self.NotesSegmentInformationEtcFinancialStatementsLineItems = fact.value

			elif fact.concept.qname.localName == 'DescriptionOfImpairmentLossNotAllocatedToReportableSegments': #報告セグメントに配分されていない減損損失の内容
				self.DescriptionOfImpairmentLossNotAllocatedToReportableSegments = fact.value

			elif fact.concept.qname.localName == 'NotesSegmentInformationEtcFinancialStatementsHeading': #セグメント情報等、財務諸表 [目次項目]
				self.NotesSegmentInformationEtcFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'AmortizationAndUnamortizedBalanceOfGoodwillForEachReportableSegmentAbstract': #報告セグメントごとののれんの償却額及び未償却残高に関する情報 [タイトル項目]
				self.AmortizationAndUnamortizedBalanceOfGoodwillForEachReportableSegmentAbstract = fact.value

			elif fact.concept.qname.localName == 'AmortizationAndUnamortizedBalanceOfGoodwillForEachReportableSegmentTable': #報告セグメントごとののれんの償却額及び未償却残高に関する情報 [表]
				self.AmortizationAndUnamortizedBalanceOfGoodwillForEachReportableSegmentTable = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedOrNonConsolidatedAxis': #連結個別 [軸]
				self.ConsolidatedOrNonConsolidatedAxis = fact.value

			elif fact.concept.qname.localName == 'NonConsolidatedMember': #非連結又は個別 [メンバー]
				self.NonConsolidatedMember = fact.value

			elif fact.concept.qname.localName == 'OperatingSegmentsAxis': #事業セグメント [軸]
				self.OperatingSegmentsAxis = fact.value

			elif fact.concept.qname.localName == 'EntityTotalMember': #連結合計又は会社合計 [メンバー] ※ディメンションデフォルト
				self.EntityTotalMember = fact.value

			elif fact.concept.qname.localName == 'ReportableSegmentsMember': #報告セグメント [メンバー]
				self.ReportableSegmentsMember = fact.value

			elif fact.concept.qname.localName == 'OtherReportableSegmentsMember': #その他の報告セグメント [メンバー]
				self.OtherReportableSegmentsMember = fact.value

			elif fact.concept.qname.localName == 'OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember': #報告セグメント以外の全てのセグメント [メンバー]
				self.OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember = fact.value

			elif fact.concept.qname.localName == 'UnallocatedAmountsAndEliminationMember': #全社・消去 [メンバー]
				self.UnallocatedAmountsAndEliminationMember = fact.value

			elif fact.concept.qname.localName == 'AmortizationAndUnamortizedBalanceOfGoodwillForEachReportableSegmentLineItems': #報告セグメントごとののれんの償却額及び未償却残高に関する情報 [表示項目]
				self.AmortizationAndUnamortizedBalanceOfGoodwillForEachReportableSegmentLineItems = fact.value

			elif fact.concept.qname.localName == 'AmortizationOfGoodwillSGA': #のれん償却額、販売費及び一般管理費
				self.AmortizationOfGoodwillSGA = fact.value

			elif fact.concept.qname.localName == 'Goodwill': #のれん
				self.Goodwill = fact.value

			elif fact.concept.qname.localName == 'GoodwillBeforeOffsetting': #のれん（相殺前）
				self.GoodwillBeforeOffsetting = fact.value

			elif fact.concept.qname.localName == 'NotesSegmentInformationEtcFinancialStatementsHeading': #セグメント情報等、財務諸表 [目次項目]
				self.NotesSegmentInformationEtcFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'AmortizationAndUnamortizedBalanceOfNegativeGoodwillForEachReportableSegmentAbstract': #報告セグメントごとの負ののれんの償却額及び未償却残高に関する情報 [タイトル項目]
				self.AmortizationAndUnamortizedBalanceOfNegativeGoodwillForEachReportableSegmentAbstract = fact.value

			elif fact.concept.qname.localName == 'AmortizationAndUnamortizedBalanceOfNegativeGoodwillForEachReportableSegmentTable': #報告セグメントごとの負ののれんの償却額及び未償却残高に関する情報 [表]
				self.AmortizationAndUnamortizedBalanceOfNegativeGoodwillForEachReportableSegmentTable = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedOrNonConsolidatedAxis': #連結個別 [軸]
				self.ConsolidatedOrNonConsolidatedAxis = fact.value

			elif fact.concept.qname.localName == 'NonConsolidatedMember': #非連結又は個別 [メンバー]
				self.NonConsolidatedMember = fact.value

			elif fact.concept.qname.localName == 'OperatingSegmentsAxis': #事業セグメント [軸]
				self.OperatingSegmentsAxis = fact.value

			elif fact.concept.qname.localName == 'EntityTotalMember': #連結合計又は会社合計 [メンバー] ※ディメンションデフォルト
				self.EntityTotalMember = fact.value

			elif fact.concept.qname.localName == 'ReportableSegmentsMember': #報告セグメント [メンバー]
				self.ReportableSegmentsMember = fact.value

			elif fact.concept.qname.localName == 'OtherReportableSegmentsMember': #その他の報告セグメント [メンバー]
				self.OtherReportableSegmentsMember = fact.value

			elif fact.concept.qname.localName == 'OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember': #報告セグメント以外の全てのセグメント [メンバー]
				self.OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember = fact.value

			elif fact.concept.qname.localName == 'UnallocatedAmountsAndEliminationMember': #全社・消去 [メンバー]
				self.UnallocatedAmountsAndEliminationMember = fact.value

			elif fact.concept.qname.localName == 'AmortizationAndUnamortizedBalanceOfNegativeGoodwillForEachReportableSegmentLineItems': #報告セグメントごとの負ののれんの償却額及び未償却残高に関する情報 [表示項目]
				self.AmortizationAndUnamortizedBalanceOfNegativeGoodwillForEachReportableSegmentLineItems = fact.value

			elif fact.concept.qname.localName == 'AmortizationOfNegativeGoodwillNOI': #負ののれん償却額、営業外収益
				self.AmortizationOfNegativeGoodwillNOI = fact.value

			elif fact.concept.qname.localName == 'NegativeGoodwill': #負ののれん
				self.NegativeGoodwill = fact.value

			elif fact.concept.qname.localName == 'NegativeGoodwillBeforeOffsetting': #負ののれん（相殺前）
				self.NegativeGoodwillBeforeOffsetting = fact.value

			elif fact.concept.qname.localName == 'NotesSegmentInformationEtcFinancialStatementsHeading': #セグメント情報等、財務諸表 [目次項目]
				self.NotesSegmentInformationEtcFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesSegmentInformationEtcFinancialStatementsTable': #セグメント情報等、財務諸表 [表]
				self.NotesSegmentInformationEtcFinancialStatementsTable = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedOrNonConsolidatedAxis': #連結個別 [軸]
				self.ConsolidatedOrNonConsolidatedAxis = fact.value

			elif fact.concept.qname.localName == 'NonConsolidatedMember': #非連結又は個別 [メンバー]
				self.NonConsolidatedMember = fact.value

			elif fact.concept.qname.localName == 'NotesSegmentInformationEtcFinancialStatementsLineItems': #セグメント情報等、財務諸表 [表示項目]
				self.NotesSegmentInformationEtcFinancialStatementsLineItems = fact.value

			elif fact.concept.qname.localName == 'DescriptionOfAmortizationOfGoodwillOrUnamortizedBalanceOfGoodwillNotAllocatedToReportableSegments': #報告セグメントに配分されていないのれんの償却額又は未償却残高の内容
				self.DescriptionOfAmortizationOfGoodwillOrUnamortizedBalanceOfGoodwillNotAllocatedToReportableSegments = fact.value

			elif fact.concept.qname.localName == 'NotesSegmentInformationEtcFinancialStatementsHeading': #セグメント情報等、財務諸表 [目次項目]
				self.NotesSegmentInformationEtcFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'InformationAboutGainOnBargainPurchaseForEachReportableSegmentTable': #報告セグメントごとの負ののれん発生益に関する情報 [表]
				self.InformationAboutGainOnBargainPurchaseForEachReportableSegmentTable = fact.value

			elif fact.concept.qname.localName == 'ConsolidatedOrNonConsolidatedAxis': #連結個別 [軸]
				self.ConsolidatedOrNonConsolidatedAxis = fact.value

			elif fact.concept.qname.localName == 'NonConsolidatedMember': #非連結又は個別 [メンバー]
				self.NonConsolidatedMember = fact.value

			elif fact.concept.qname.localName == 'OperatingSegmentsAxis': #事業セグメント [軸]
				self.OperatingSegmentsAxis = fact.value

			elif fact.concept.qname.localName == 'EntityTotalMember': #連結合計又は会社合計 [メンバー] ※ディメンションデフォルト
				self.EntityTotalMember = fact.value

			elif fact.concept.qname.localName == 'ReportableSegmentsMember': #報告セグメント [メンバー]
				self.ReportableSegmentsMember = fact.value

			elif fact.concept.qname.localName == 'OtherReportableSegmentsMember': #その他の報告セグメント [メンバー]
				self.OtherReportableSegmentsMember = fact.value

			elif fact.concept.qname.localName == 'OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember': #報告セグメント以外の全てのセグメント [メンバー]
				self.OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember = fact.value

			elif fact.concept.qname.localName == 'UnallocatedAmountsAndEliminationMember': #全社・消去 [メンバー]
				self.UnallocatedAmountsAndEliminationMember = fact.value

			elif fact.concept.qname.localName == 'InformationAboutGainOnBargainPurchaseForEachReportableSegmentLineItems': #報告セグメントごとの負ののれん発生益に関する情報 [表示項目]
				self.InformationAboutGainOnBargainPurchaseForEachReportableSegmentLineItems = fact.value

			elif fact.concept.qname.localName == 'DescriptionOfFactorsWhichLedToRecognitionOfGainOnBargainPurchaseTextBlock': #報告セグメントごとの負ののれん発生益を認識する要因となった事象の概要 [テキストブロック]
				self.DescriptionOfFactorsWhichLedToRecognitionOfGainOnBargainPurchaseTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesOperationOfPublicFacilitiesFinancialStatementsHeading': #公共施設等運営事業関係、財務諸表 [目次項目]
				self.NotesOperationOfPublicFacilitiesFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesOperationOfPublicFacilitiesFinancialStatementsTextBlock': #公共施設等運営事業関係、財務諸表 [テキストブロック]
				self.NotesOperationOfPublicFacilitiesFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesRelatedPartiesFinancialStatementsHeading': #関連当事者情報、財務諸表 [目次項目]
				self.NotesRelatedPartiesFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesRelatedPartiesFinancialStatementsTextBlock': #関連当事者情報、財務諸表 [テキストブロック]
				self.NotesRelatedPartiesFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesEquityInEarningsLossesOfAffiliatesIfEquityMethodIsAppliedFinancialStatementsHeading': #持分法損益等、財務諸表 [目次項目]
				self.NotesEquityInEarningsLossesOfAffiliatesIfEquityMethodIsAppliedFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesEquityInEarningsLossesOfAffiliatesIfEquityMethodIsAppliedFinancialStatementsTextBlock': #持分法損益等、財務諸表 [テキストブロック]
				self.NotesEquityInEarningsLossesOfAffiliatesIfEquityMethodIsAppliedFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesSpecialPurposeEntitiesSubjectToDisclosureFinancialStatementsHeading': #開示対象特別目的会社関係、財務諸表 [目次項目]
				self.NotesSpecialPurposeEntitiesSubjectToDisclosureFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesSpecialPurposeEntitiesSubjectToDisclosureFinancialStatementsTextBlock': #開示対象特別目的会社関係、財務諸表 [テキストブロック]
				self.NotesSpecialPurposeEntitiesSubjectToDisclosureFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesPerShareInformationFinancialStatementsHeading': #１株当たり情報、財務諸表 [目次項目]
				self.NotesPerShareInformationFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesPerShareInformationFinancialStatementsTextBlock': #１株当たり情報、財務諸表 [テキストブロック]
				self.NotesPerShareInformationFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'NotesSignificantEventsAfterReportingPeriodFinancialStatementsHeading': #重要な後発事象、財務諸表 [目次項目]
				self.NotesSignificantEventsAfterReportingPeriodFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'NotesSignificantEventsAfterReportingPeriodFinancialStatementsTextBlock': #重要な後発事象、財務諸表 [テキストブロック]
				self.NotesSignificantEventsAfterReportingPeriodFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'AnnexedDetailedSchedulesHeading': #附属明細表 [目次項目]
				self.AnnexedDetailedSchedulesHeading = fact.value

			elif fact.concept.qname.localName == 'AnnexedDetailedScheduleOfSecuritiesHeading': #有価証券明細表 [目次項目]
				self.AnnexedDetailedScheduleOfSecuritiesHeading = fact.value

			elif fact.concept.qname.localName == 'AnnexedDetailedScheduleOfSecuritiesTextBlock': #有価証券明細表 [テキストブロック]
				self.AnnexedDetailedScheduleOfSecuritiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'AnnexedDetailedScheduleOfPropertyPlantAndEquipmentEtcHeading': #有形固定資産等明細表 [目次項目]
				self.AnnexedDetailedScheduleOfPropertyPlantAndEquipmentEtcHeading = fact.value

			elif fact.concept.qname.localName == 'AnnexedDetailedScheduleOfPropertyPlantAndEquipmentEtcTextBlock': #有形固定資産等明細表 [テキストブロック]
				self.AnnexedDetailedScheduleOfPropertyPlantAndEquipmentEtcTextBlock = fact.value

			elif fact.concept.qname.localName == 'AnnexedDetailedScheduleOfCorporateBondsFinancialStatementsHeading': #社債明細表、財務諸表 [目次項目]
				self.AnnexedDetailedScheduleOfCorporateBondsFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'AnnexedDetailedScheduleOfCorporateBondsFinancialStatementsTextBlock': #社債明細表、財務諸表 [テキストブロック]
				self.AnnexedDetailedScheduleOfCorporateBondsFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'AnnexedDetailedScheduleOfBorrowingsFinancialStatementsHeading': #借入金等明細表、財務諸表 [目次項目]
				self.AnnexedDetailedScheduleOfBorrowingsFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'AnnexedDetailedScheduleOfBorrowingsFinancialStatementsTextBlock': #借入金等明細表、財務諸表 [テキストブロック]
				self.AnnexedDetailedScheduleOfBorrowingsFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'AnnexedDetailedScheduleOfProvisionsHeading': #引当金明細表 [目次項目]
				self.AnnexedDetailedScheduleOfProvisionsHeading = fact.value

			elif fact.concept.qname.localName == 'AnnexedDetailedScheduleOfProvisionsTextBlock': #引当金明細表 [テキストブロック]
				self.AnnexedDetailedScheduleOfProvisionsTextBlock = fact.value

			elif fact.concept.qname.localName == 'AnnexedDetailedScheduleOfAssetRetirementObligationsFinancialStatementsHeading': #資産除去債務明細表、財務諸表 [目次項目]
				self.AnnexedDetailedScheduleOfAssetRetirementObligationsFinancialStatementsHeading = fact.value

			elif fact.concept.qname.localName == 'AnnexedDetailedScheduleOfAssetRetirementObligationsFinancialStatementsTextBlock': #資産除去債務明細表、財務諸表 [テキストブロック]
				self.AnnexedDetailedScheduleOfAssetRetirementObligationsFinancialStatementsTextBlock = fact.value

			elif fact.concept.qname.localName == 'AnnexedDetailedScheduleOfWaterTransportationRevenuesAndExpensesHeading': #海運業収益及び費用明細表 [目次項目]
				self.AnnexedDetailedScheduleOfWaterTransportationRevenuesAndExpensesHeading = fact.value

			elif fact.concept.qname.localName == 'AnnexedDetailedScheduleOfWaterTransportationRevenuesAndExpensesTextBlock': #海運業収益及び費用明細表 [テキストブロック]
				self.AnnexedDetailedScheduleOfWaterTransportationRevenuesAndExpensesTextBlock = fact.value

			elif fact.concept.qname.localName == 'AnnexedDetailedScheduleOfSecuritiesInTrustCNAHeading': #信託有価証券明細表、建設保証業 [目次項目]
				self.AnnexedDetailedScheduleOfSecuritiesInTrustCNAHeading = fact.value

			elif fact.concept.qname.localName == 'AnnexedDetailedScheduleOfSecuritiesInTrustCNATextBlock': #信託有価証券明細表、建設保証業 [テキストブロック]
				self.AnnexedDetailedScheduleOfSecuritiesInTrustCNATextBlock = fact.value

			elif fact.concept.qname.localName == 'AnnexedDetailedScheduleOfBusinessCostINSHeading': #事業費明細表、保険業 [目次項目]
				self.AnnexedDetailedScheduleOfBusinessCostINSHeading = fact.value

			elif fact.concept.qname.localName == 'AnnexedDetailedScheduleOfBusinessCostINSTextBlock': #事業費明細表、保険業 [テキストブロック]
				self.AnnexedDetailedScheduleOfBusinessCostINSTextBlock = fact.value

			elif fact.concept.qname.localName == 'AnnexedDetailedScheduleOfNonCurrentAssetsELCHeading': #固定資産等明細表、電気通信事業 [目次項目]
				self.AnnexedDetailedScheduleOfNonCurrentAssetsELCHeading = fact.value

			elif fact.concept.qname.localName == 'AnnexedDetailedScheduleOfNonCurrentAssetsELCTextBlock': #固定資産等明細表、電気通信事業 [テキストブロック]
				self.AnnexedDetailedScheduleOfNonCurrentAssetsELCTextBlock = fact.value

			elif fact.concept.qname.localName == 'AnnexedDetailedScheduleOfNonCurrentAssetsGASHeading': #固定資産等明細表、ガス事業 [目次項目]
				self.AnnexedDetailedScheduleOfNonCurrentAssetsGASHeading = fact.value

			elif fact.concept.qname.localName == 'AnnexedDetailedScheduleOfNonCurrentAssetsGASTextBlock': #固定資産等明細表、ガス事業 [テキストブロック]
				self.AnnexedDetailedScheduleOfNonCurrentAssetsGASTextBlock = fact.value

			elif fact.concept.qname.localName == 'AnnexedDetailedScheduleOfNonCurrentAssetsHWYHeading': #固定資産等明細表、高速道路事業 [目次項目]
				self.AnnexedDetailedScheduleOfNonCurrentAssetsHWYHeading = fact.value

			elif fact.concept.qname.localName == 'AnnexedDetailedScheduleOfNonCurrentAssetsHWYTextBlock': #固定資産等明細表、高速道路事業 [テキストブロック]
				self.AnnexedDetailedScheduleOfNonCurrentAssetsHWYTextBlock = fact.value

			elif fact.concept.qname.localName == 'AnnexedDetailedScheduleOfIncreaseAndDecreaseOfNonCurrentAssetsELEHeading': #固定資産期中増減明細表、電気事業 [目次項目]
				self.AnnexedDetailedScheduleOfIncreaseAndDecreaseOfNonCurrentAssetsELEHeading = fact.value

			elif fact.concept.qname.localName == 'AnnexedDetailedScheduleOfIncreaseAndDecreaseOfNonCurrentAssetsELETextBlock': #固定資産期中増減明細表、電気事業 [テキストブロック]
				self.AnnexedDetailedScheduleOfIncreaseAndDecreaseOfNonCurrentAssetsELETextBlock = fact.value

			elif fact.concept.qname.localName == 'AnnexedDetailedScheduleOfIncreaseAndDecreaseOfNonCurrentAssetsPart2IntangibleAssetsELEHeading': #固定資産期中増減明細表（無形固定資産再掲）、電気事業 [目次項目]
				self.AnnexedDetailedScheduleOfIncreaseAndDecreaseOfNonCurrentAssetsPart2IntangibleAssetsELEHeading = fact.value

			elif fact.concept.qname.localName == 'AnnexedDetailedScheduleOfIncreaseAndDecreaseOfNonCurrentAssetsPart2IntangibleAssetsELETextBlock': #固定資産期中増減明細表（無形固定資産再掲）、電気事業 [テキストブロック]
				self.AnnexedDetailedScheduleOfIncreaseAndDecreaseOfNonCurrentAssetsPart2IntangibleAssetsELETextBlock = fact.value

			elif fact.concept.qname.localName == 'AnnexedDetailedScheduleOfDepreciationEtcELEHeading': #減価償却費等明細表、電気事業 [目次項目]
				self.AnnexedDetailedScheduleOfDepreciationEtcELEHeading = fact.value

			elif fact.concept.qname.localName == 'AnnexedDetailedScheduleOfDepreciationEtcELETextBlock': #減価償却費等明細表、電気事業 [テキストブロック]
				self.AnnexedDetailedScheduleOfDepreciationEtcELETextBlock = fact.value

			elif fact.concept.qname.localName == 'AnnexedDetailedScheduleOfLongTermAndShortTermInvestmentsELEHeading': #長期投資及び短期投資明細表、電気事業 [目次項目]
				self.AnnexedDetailedScheduleOfLongTermAndShortTermInvestmentsELEHeading = fact.value

			elif fact.concept.qname.localName == 'AnnexedDetailedScheduleOfLongTermAndShortTermInvestmentsELETextBlock': #長期投資及び短期投資明細表、電気事業 [テキストブロック]
				self.AnnexedDetailedScheduleOfLongTermAndShortTermInvestmentsELETextBlock = fact.value

			elif fact.concept.qname.localName == 'AnnexedDetailedScheduleOfBorrowingsLongTermPayablesLeaseObligationsOtherNonCurrentLiabilitiesAndCommercialPapersELEHeading': #借入金、長期未払債務、リース債務、雑固定負債及びコマーシャル・ペーパー明細表、電気事業 [目次項目]
				self.AnnexedDetailedScheduleOfBorrowingsLongTermPayablesLeaseObligationsOtherNonCurrentLiabilitiesAndCommercialPapersELEHeading = fact.value

			elif fact.concept.qname.localName == 'AnnexedDetailedScheduleOfBorrowingsLongTermPayablesLeaseObligationsOtherNonCurrentLiabilitiesAndCommercialPapersELETextBlock': #借入金、長期未払債務、リース債務、雑固定負債及びコマーシャル・ペーパー明細表、電気事業 [テキストブロック]
				self.AnnexedDetailedScheduleOfBorrowingsLongTermPayablesLeaseObligationsOtherNonCurrentLiabilitiesAndCommercialPapersELETextBlock = fact.value

			elif fact.concept.qname.localName == 'AnnexedDetailedScheduleOfCorporateBondsAndShortTermAndLongTermBorrowingsHWYHeading': #社債、長期借入金及び短期借入金の増減明細表、高速道路事業 [目次項目]
				self.AnnexedDetailedScheduleOfCorporateBondsAndShortTermAndLongTermBorrowingsHWYHeading = fact.value

			elif fact.concept.qname.localName == 'AnnexedDetailedScheduleOfCorporateBondsAndShortTermAndLongTermBorrowingsHWYTextBlock': #社債、長期借入金及び短期借入金の増減明細表、高速道路事業 [テキストブロック]
				self.AnnexedDetailedScheduleOfCorporateBondsAndShortTermAndLongTermBorrowingsHWYTextBlock = fact.value

			elif fact.concept.qname.localName == 'AnnexedDetailedScheduleOfMedicalCorporationBondsHeading': #社会医療法人債明細表 [目次項目]
				self.AnnexedDetailedScheduleOfMedicalCorporationBondsHeading = fact.value

			elif fact.concept.qname.localName == 'AnnexedDetailedScheduleOfMedicalCorporationBondsTextBlock': #社会医療法人債明細表 [テキストブロック]
				self.AnnexedDetailedScheduleOfMedicalCorporationBondsTextBlock = fact.value

			elif fact.concept.qname.localName == 'AnnexedDetailedScheduleOfSchoolBondsHeading': #学校債明細表 [目次項目]
				self.AnnexedDetailedScheduleOfSchoolBondsHeading = fact.value

			elif fact.concept.qname.localName == 'AnnexedDetailedScheduleOfSchoolBondsTextBlock': #学校債明細表 [テキストブロック]
				self.AnnexedDetailedScheduleOfSchoolBondsTextBlock = fact.value

			elif fact.concept.qname.localName == 'ComponentsOfMajorAssetsAndLiabilitiesHeading': #主な資産及び負債の内容 [目次項目]
				self.ComponentsOfMajorAssetsAndLiabilitiesHeading = fact.value

			elif fact.concept.qname.localName == 'ComponentsOfMajorAssetsAndLiabilitiesTextBlock': #主な資産及び負債の内容 [テキストブロック]
				self.ComponentsOfMajorAssetsAndLiabilitiesTextBlock = fact.value

			elif fact.concept.qname.localName == 'OtherInformationFinancialStatementsEtcHeading': #その他、財務諸表等 [目次項目]
				self.OtherInformationFinancialStatementsEtcHeading = fact.value

			elif fact.concept.qname.localName == 'OtherInformationFinancialStatementsEtcTextBlock': #その他、財務諸表等 [テキストブロック]
				self.OtherInformationFinancialStatementsEtcTextBlock = fact.value

			elif fact.concept.qname.localName == 'OverviewOfOperationalProceduresForSharesHeading': #提出会社の株式事務の概要 [目次項目]
				self.OverviewOfOperationalProceduresForSharesHeading = fact.value

			elif fact.concept.qname.localName == 'OverviewOfOperationalProceduresForSharesTextBlock': #提出会社の株式事務の概要 [テキストブロック]
				self.OverviewOfOperationalProceduresForSharesTextBlock = fact.value

			elif fact.concept.qname.localName == 'ReferenceInformationOfReportingCompanyHeading': #提出会社の参考情報 [目次項目]
				self.ReferenceInformationOfReportingCompanyHeading = fact.value

			elif fact.concept.qname.localName == 'InformationAboutParentCompanyEtcOfReportingCompanyHeading': #提出会社の親会社等の情報 [目次項目]
				self.InformationAboutParentCompanyEtcOfReportingCompanyHeading = fact.value

			elif fact.concept.qname.localName == 'InformationAboutParentCompanyEtcOfReportingCompanyTextBlock': #提出会社の親会社等の情報 [テキストブロック]
				self.InformationAboutParentCompanyEtcOfReportingCompanyTextBlock = fact.value

			elif fact.concept.qname.localName == 'OtherReferenceInformationHeading': #その他の参考情報 [目次項目]
				self.OtherReferenceInformationHeading = fact.value

			elif fact.concept.qname.localName == 'OtherReferenceInformationTextBlock': #その他の参考情報 [テキストブロック]
				self.OtherReferenceInformationTextBlock = fact.value

			elif fact.concept.qname.localName == 'InformationAboutCompanyWhichProvidesGuaranteeToReportingCompanyHeading': #提出会社の保証会社等の情報 [目次項目]
				self.InformationAboutCompanyWhichProvidesGuaranteeToReportingCompanyHeading = fact.value

			elif fact.concept.qname.localName == 'InformationAboutCompanyWhichProvidesGuaranteeToReportingCompanyTextBlock': #提出会社の保証会社等の情報 [テキストブロック]
				self.InformationAboutCompanyWhichProvidesGuaranteeToReportingCompanyTextBlock = fact.value

			elif fact.concept.qname.localName == 'InformationAboutGuaranteeCompanyHeading': #保証会社情報 [目次項目]
				self.InformationAboutGuaranteeCompanyHeading = fact.value

			elif fact.concept.qname.localName == 'InformationAboutGuaranteeCompanyTextBlock': #保証会社情報 [テキストブロック]
				self.InformationAboutGuaranteeCompanyTextBlock = fact.value

			elif fact.concept.qname.localName == 'CorporateBondsUnderGuaranteeHeading': #保証の対象となっている社債 [目次項目]
				self.CorporateBondsUnderGuaranteeHeading = fact.value

			elif fact.concept.qname.localName == 'CorporateBondsUnderGuaranteeTextBlock': #保証の対象となっている社債 [テキストブロック]
				self.CorporateBondsUnderGuaranteeTextBlock = fact.value

			elif fact.concept.qname.localName == 'InformationAboutGuaranteeCompanySubjectToOngoingDisclosureHeading': #継続開示会社たる保証会社に関する事項 [目次項目]
				self.InformationAboutGuaranteeCompanySubjectToOngoingDisclosureHeading = fact.value

			elif fact.concept.qname.localName == 'InformationAboutGuaranteeCompanySubjectToOngoingDisclosureTextBlock': #継続開示会社たる保証会社に関する事項 [テキストブロック]
				self.InformationAboutGuaranteeCompanySubjectToOngoingDisclosureTextBlock = fact.value

			elif fact.concept.qname.localName == 'DocumentsSubmittedByGuaranteeCompanyHeading': #保証会社が提出した書類 [目次項目]
				self.DocumentsSubmittedByGuaranteeCompanyHeading = fact.value

			elif fact.concept.qname.localName == 'AnnualSecuritiesReportAndAttachedDocumentsQuarterlySecuritiesReportOrSemiAnnualSecuritiesReportDocumentsSubmittedByGuaranteeCompanyHeading': #有価証券報告書及びその添付書類又は四半期報告書若しくは半期報告書、保証会社が提出した書類 [目次項目]
				self.AnnualSecuritiesReportAndAttachedDocumentsQuarterlySecuritiesReportOrSemiAnnualSecuritiesReportDocumentsSubmittedByGuaranteeCompanyHeading = fact.value

			elif fact.concept.qname.localName == 'AnnualSecuritiesReportAndAttachedDocumentsQuarterlySecuritiesReportOrSemiAnnualSecuritiesReportDocumentsSubmittedByGuaranteeCompanyTextBlock': #有価証券報告書及びその添付書類又は四半期報告書若しくは半期報告書、保証会社が提出した書類 [テキストブロック]
				self.AnnualSecuritiesReportAndAttachedDocumentsQuarterlySecuritiesReportOrSemiAnnualSecuritiesReportDocumentsSubmittedByGuaranteeCompanyTextBlock = fact.value

			elif fact.concept.qname.localName == 'ExtraordinarySecuritiesReportDocumentsSubmittedByGuaranteeCompanyHeading': #臨時報告書、保証会社が提出した書類 [目次項目]
				self.ExtraordinarySecuritiesReportDocumentsSubmittedByGuaranteeCompanyHeading = fact.value

			elif fact.concept.qname.localName == 'ExtraordinarySecuritiesReportDocumentsSubmittedByGuaranteeCompanyTextBlock': #臨時報告書、保証会社が提出した書類 [テキストブロック]
				self.ExtraordinarySecuritiesReportDocumentsSubmittedByGuaranteeCompanyTextBlock = fact.value

			elif fact.concept.qname.localName == 'AmendmentReportDocumentsSubmittedByGuaranteeCompanyHeading': #訂正報告書、保証会社が提出した書類 [目次項目]
				self.AmendmentReportDocumentsSubmittedByGuaranteeCompanyHeading = fact.value

			elif fact.concept.qname.localName == 'AmendmentReportDocumentsSubmittedByGuaranteeCompanyTextBlock': #訂正報告書、保証会社が提出した書類 [テキストブロック]
				self.AmendmentReportDocumentsSubmittedByGuaranteeCompanyTextBlock = fact.value

			elif fact.concept.qname.localName == 'PlaceForPublicInspectionDocumentsSubmittedByGuaranteeCompanyHeading': #上記書類を縦覧に供している場所、保証会社が提出した書類 [目次項目]
				self.PlaceForPublicInspectionDocumentsSubmittedByGuaranteeCompanyHeading = fact.value

			elif fact.concept.qname.localName == 'PlaceForPublicInspectionDocumentsSubmittedByGuaranteeCompanyTextBlock': #上記書類を縦覧に供している場所、保証会社が提出した書類 [テキストブロック]
				self.PlaceForPublicInspectionDocumentsSubmittedByGuaranteeCompanyTextBlock = fact.value

			elif fact.concept.qname.localName == 'InformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureHeading': #継続開示会社に該当しない保証会社に関する事項 [目次項目]
				self.InformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureHeading = fact.value

			elif fact.concept.qname.localName == 'InformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureTextBlock': #継続開示会社に該当しない保証会社に関する事項 [テキストブロック]
				self.InformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureTextBlock = fact.value

			elif fact.concept.qname.localName == 'CompanyNameTitleAndNameOfRepresentativeAndAddressOfRegisteredHeadquarterHeading': #会社名・代表者の役職氏名及び本店の所在の場所 [目次項目]
				self.CompanyNameTitleAndNameOfRepresentativeAndAddressOfRegisteredHeadquarterHeading = fact.value

			elif fact.concept.qname.localName == 'CompanyNameTitleAndNameOfRepresentativeAndAddressOfRegisteredHeadquarterTextBlock': #会社名・代表者の役職氏名及び本店の所在の場所 [テキストブロック]
				self.CompanyNameTitleAndNameOfRepresentativeAndAddressOfRegisteredHeadquarterTextBlock = fact.value

			elif fact.concept.qname.localName == 'OverviewOfCompanyInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureHeading': #企業の概況、継続開示会社に該当しない保証会社に関する事項 [目次項目]
				self.OverviewOfCompanyInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureHeading = fact.value

			elif fact.concept.qname.localName == 'OverviewOfCompanyInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureTextBlock': #企業の概況、継続開示会社に該当しない保証会社に関する事項 [テキストブロック]
				self.OverviewOfCompanyInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureTextBlock = fact.value

			elif fact.concept.qname.localName == 'OverviewOfBusinessInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureHeading': #事業の状況、継続開示会社に該当しない保証会社に関する事項 [目次項目]
				self.OverviewOfBusinessInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureHeading = fact.value

			elif fact.concept.qname.localName == 'OverviewOfBusinessInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureTextBlock': #事業の状況、継続開示会社に該当しない保証会社に関する事項 [テキストブロック]
				self.OverviewOfBusinessInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureTextBlock = fact.value

			elif fact.concept.qname.localName == 'InformationAboutFacilitiesInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureHeading': #設備の状況、継続開示会社に該当しない保証会社に関する事項 [目次項目]
				self.InformationAboutFacilitiesInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureHeading = fact.value

			elif fact.concept.qname.localName == 'InformationAboutFacilitiesInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureTextBlock': #設備の状況、継続開示会社に該当しない保証会社に関する事項 [テキストブロック]
				self.InformationAboutFacilitiesInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureTextBlock = fact.value

			elif fact.concept.qname.localName == 'GuaranteeCompanyInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureHeading': #保証会社の状況、継続開示会社に該当しない保証会社に関する事項 [目次項目]
				self.GuaranteeCompanyInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureHeading = fact.value

			elif fact.concept.qname.localName == 'GuaranteeCompanyInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureTextBlock': #保証会社の状況、継続開示会社に該当しない保証会社に関する事項 [テキストブロック]
				self.GuaranteeCompanyInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureTextBlock = fact.value

			elif fact.concept.qname.localName == 'FinancialInformationInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureHeading': #経理の状況、継続開示会社に該当しない保証会社に関する事項 [目次項目]
				self.FinancialInformationInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureHeading = fact.value

			elif fact.concept.qname.localName == 'FinancialInformationInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureTextBlock': #経理の状況、継続開示会社に該当しない保証会社に関する事項 [テキストブロック]
				self.FinancialInformationInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureTextBlock = fact.value

			elif fact.concept.qname.localName == 'InformationAboutCompaniesOtherThanGuaranteeCompanyHeading': #保証会社以外の会社の情報 [目次項目]
				self.InformationAboutCompaniesOtherThanGuaranteeCompanyHeading = fact.value

			elif fact.concept.qname.localName == 'InformationAboutCompaniesOtherThanGuaranteeCompanyTextBlock': #保証会社以外の会社の情報 [テキストブロック]
				self.InformationAboutCompaniesOtherThanGuaranteeCompanyTextBlock = fact.value

			elif fact.concept.qname.localName == 'ReasonForDisclosureOfInformationOfCompanyConcernedHeading': #当該会社の情報の開示を必要とする理由 [目次項目]
				self.ReasonForDisclosureOfInformationOfCompanyConcernedHeading = fact.value

			elif fact.concept.qname.localName == 'ReasonForDisclosureOfInformationOfCompanyConcernedTextBlock': #当該会社の情報の開示を必要とする理由 [テキストブロック]
				self.ReasonForDisclosureOfInformationOfCompanyConcernedTextBlock = fact.value

			elif fact.concept.qname.localName == 'InformationAboutCompanyConcernedSubjectToOngoingDisclosureHeading': #継続開示会社たる当該会社に関する事項 [目次項目]
				self.InformationAboutCompanyConcernedSubjectToOngoingDisclosureHeading = fact.value

			elif fact.concept.qname.localName == 'InformationAboutCompanyConcernedSubjectToOngoingDisclosureTextBlock': #継続開示会社たる当該会社に関する事項 [テキストブロック]
				self.InformationAboutCompanyConcernedSubjectToOngoingDisclosureTextBlock = fact.value

			elif fact.concept.qname.localName == 'InformationAboutCompanyConcernedNotSubjectToOngoingDisclosureHeading': #継続開示会社に該当しない当該会社に関する事項 [目次項目]
				self.InformationAboutCompanyConcernedNotSubjectToOngoingDisclosureHeading = fact.value

			elif fact.concept.qname.localName == 'InformationAboutCompanyConcernedNotSubjectToOngoingDisclosureTextBlock': #継続開示会社に該当しない当該会社に関する事項 [テキストブロック]
				self.InformationAboutCompanyConcernedNotSubjectToOngoingDisclosureTextBlock = fact.value

			elif fact.concept.qname.localName == 'InformationAboutIndexEtcHeading': #指数等の情報 [目次項目]
				self.InformationAboutIndexEtcHeading = fact.value

			elif fact.concept.qname.localName == 'InformationAboutIndexEtcTextBlock': #指数等の情報 [テキストブロック]
				self.InformationAboutIndexEtcTextBlock = fact.value

			elif fact.concept.qname.localName == 'ReasonForDisclosureOfSaidIndexEtcHeading': #当該指数等の情報の開示を必要とする理由 [目次項目]
				self.ReasonForDisclosureOfSaidIndexEtcHeading = fact.value

			elif fact.concept.qname.localName == 'ReasonForDisclosureOfSaidIndexEtcTextBlock': #当該指数等の情報の開示を必要とする理由 [テキストブロック]
				self.ReasonForDisclosureOfSaidIndexEtcTextBlock = fact.value

			elif fact.concept.qname.localName == 'HistoricalRecordsOfIndexEtcHeading': #当該指数等の推移 [目次項目]
				self.HistoricalRecordsOfIndexEtcHeading = fact.value

			elif fact.concept.qname.localName == 'HistoricalRecordsOfIndexEtcTextBlock': #当該指数等の推移 [テキストブロック]
				self.HistoricalRecordsOfIndexEtcTextBlock = fact.value

			elif fact.concept.qname.localName == 'IndependentAuditorsReportHeading': #独立監査人の報告書 [目次項目]
				self.IndependentAuditorsReportHeading = fact.value

			elif fact.concept.qname.localName == 'IndependentAuditorsReportConsolidatedTextBlock': #独立監査人の報告書、連結 [テキストブロック]
				self.IndependentAuditorsReportConsolidatedTextBlock = fact.value

			elif fact.concept.qname.localName == 'IndependentAuditorsReportNonConsolidatedTextBlock': #独立監査人の報告書、個別 [テキストブロック]
				self.IndependentAuditorsReportNonConsolidatedTextBlock = fact.value

			elif fact.concept.qname.localName == 'IndependentAuditorsReportHeading': #独立監査人の報告書 [目次項目]
				self.IndependentAuditorsReportHeading = fact.value

			elif fact.concept.qname.localName == 'IndependentAuditorsReportConsolidatedTextBlock': #独立監査人の報告書、連結 [テキストブロック]
				self.IndependentAuditorsReportConsolidatedTextBlock = fact.value

			elif fact.concept.qname.localName == 'AuditFirm1Consolidated': #監査法人１、連結
				self.AuditFirm1Consolidated = fact.value

			elif fact.concept.qname.localName == 'CPA1AuditFirm1Consolidated': #公認会計士１、監査法人１、連結
				self.CPA1AuditFirm1Consolidated = fact.value

			elif fact.concept.qname.localName == 'CPA2AuditFirm1Consolidated': #公認会計士２、監査法人１、連結
				self.CPA2AuditFirm1Consolidated = fact.value

			elif fact.concept.qname.localName == 'CPA3AuditFirm1Consolidated': #公認会計士３、監査法人１、連結
				self.CPA3AuditFirm1Consolidated = fact.value

			elif fact.concept.qname.localName == 'CPA4AuditFirm1Consolidated': #公認会計士４、監査法人１、連結
				self.CPA4AuditFirm1Consolidated = fact.value

			elif fact.concept.qname.localName == 'CPA5AuditFirm1Consolidated': #公認会計士５、監査法人１、連結
				self.CPA5AuditFirm1Consolidated = fact.value

			elif fact.concept.qname.localName == 'AuditFirm2Consolidated': #監査法人２、連結
				self.AuditFirm2Consolidated = fact.value

			elif fact.concept.qname.localName == 'CPA1AuditFirm2Consolidated': #公認会計士１、監査法人２、連結
				self.CPA1AuditFirm2Consolidated = fact.value

			elif fact.concept.qname.localName == 'CPA2AuditFirm2Consolidated': #公認会計士２、監査法人２、連結
				self.CPA2AuditFirm2Consolidated = fact.value

			elif fact.concept.qname.localName == 'KeyAuditMattersConsolidatedTextBlock': #監査上の主要な検討事項、連結 [テキストブロック]
				self.KeyAuditMattersConsolidatedTextBlock = fact.value

			elif fact.concept.qname.localName == 'OverviewKAMConsolidatedTextBlock': #全体概要、監査上の主要な検討事項、連結 [テキストブロック]
				self.OverviewKAMConsolidatedTextBlock = fact.value

			elif fact.concept.qname.localName == 'OtherInformationConsolidatedTextBlock': #その他の記載内容、連結 [テキストブロック]
				self.OtherInformationConsolidatedTextBlock = fact.value

			elif fact.concept.qname.localName == 'UncorrectedMaterialMisstatementOtherInformationConsolidatedTextBlock': #未修正の重要な誤り、その他の記載内容、連結 [テキストブロック]
				self.UncorrectedMaterialMisstatementOtherInformationConsolidatedTextBlock = fact.value

			elif fact.concept.qname.localName == 'IndependentAuditorsReportNonConsolidatedTextBlock': #独立監査人の報告書、個別 [テキストブロック]
				self.IndependentAuditorsReportNonConsolidatedTextBlock = fact.value

			elif fact.concept.qname.localName == 'AuditFirm1NonConsolidated': #監査法人１、個別
				self.AuditFirm1NonConsolidated = fact.value

			elif fact.concept.qname.localName == 'CPA1AuditFirm1NonConsolidated': #公認会計士１、監査法人１、個別
				self.CPA1AuditFirm1NonConsolidated = fact.value

			elif fact.concept.qname.localName == 'CPA2AuditFirm1NonConsolidated': #公認会計士２、監査法人１、個別
				self.CPA2AuditFirm1NonConsolidated = fact.value

			elif fact.concept.qname.localName == 'CPA3AuditFirm1NonConsolidated': #公認会計士３、監査法人１、個別
				self.CPA3AuditFirm1NonConsolidated = fact.value

			elif fact.concept.qname.localName == 'CPA4AuditFirm1NonConsolidated': #公認会計士４、監査法人１、個別
				self.CPA4AuditFirm1NonConsolidated = fact.value

			elif fact.concept.qname.localName == 'CPA5AuditFirm1NonConsolidated': #公認会計士５、監査法人１、個別
				self.CPA5AuditFirm1NonConsolidated = fact.value

			elif fact.concept.qname.localName == 'AuditFirm2NonConsolidated': #監査法人２、個別
				self.AuditFirm2NonConsolidated = fact.value

			elif fact.concept.qname.localName == 'CPA1AuditFirm2NonConsolidated': #公認会計士１、監査法人２、個別
				self.CPA1AuditFirm2NonConsolidated = fact.value

			elif fact.concept.qname.localName == 'CPA2AuditFirm2NonConsolidated': #公認会計士２、監査法人２、個別
				self.CPA2AuditFirm2NonConsolidated = fact.value

			elif fact.concept.qname.localName == 'KeyAuditMattersNonConsolidatedTextBlock': #監査上の主要な検討事項、個別 [テキストブロック]
				self.KeyAuditMattersNonConsolidatedTextBlock = fact.value

			elif fact.concept.qname.localName == 'OverviewKAMNonConsolidatedTextBlock': #全体概要、監査上の主要な検討事項、個別 [テキストブロック]
				self.OverviewKAMNonConsolidatedTextBlock = fact.value

			elif fact.concept.qname.localName == 'OtherInformationNonConsolidatedTextBlock': #その他の記載内容、個別 [テキストブロック]
				self.OtherInformationNonConsolidatedTextBlock = fact.value

			elif fact.concept.qname.localName == 'UncorrectedMaterialMisstatementOtherInformationNonConsolidatedTextBlock': #未修正の重要な誤り、その他の記載内容、個別 [テキストブロック]
				self.UncorrectedMaterialMisstatementOtherInformationNonConsolidatedTextBlock = fact.value

			elif fact.concept.qname.localName == 'IndependentAuditorsReportHeading': #独立監査人の報告書 [目次項目]
				self.IndependentAuditorsReportHeading = fact.value

			elif fact.concept.qname.localName == 'KeyAuditMattersDetailAbstract': #監査上の主要な検討事項（個別説明） [タイトル項目]
				self.KeyAuditMattersDetailAbstract = fact.value

			elif fact.concept.qname.localName == 'KeyAuditMattersTable': #監査上の主要な検討事項 [表]
				self.KeyAuditMattersTable = fact.value

			elif fact.concept.qname.localName == 'SequentialNumbersAxis': #連番 [軸]
				self.SequentialNumbersAxis = fact.value

			elif fact.concept.qname.localName == 'Row1Member': #1件目 [メンバー]
				self.Row1Member = fact.value

			elif fact.concept.qname.localName == 'Row2Member': #2件目 [メンバー]
				self.Row2Member = fact.value

			elif fact.concept.qname.localName == 'Row3Member': #3件目 [メンバー]
				self.Row3Member = fact.value

			elif fact.concept.qname.localName == 'KeyAuditMattersConsolidatedLineItems': #監査上の主要な検討事項、連結 [表示項目]
				self.KeyAuditMattersConsolidatedLineItems = fact.value

			elif fact.concept.qname.localName == 'ShortDescriptionKAMConsolidated': #見出し、監査上の主要な検討事項、連結
				self.ShortDescriptionKAMConsolidated = fact.value

			elif fact.concept.qname.localName == 'ReferenceKAMConsolidated': #開示への参照、監査上の主要な検討事項、連結
				self.ReferenceKAMConsolidated = fact.value

			elif fact.concept.qname.localName == 'Reference2KAMConsolidated': #開示への参照２、監査上の主要な検討事項、連結
				self.Reference2KAMConsolidated = fact.value

			elif fact.concept.qname.localName == 'Reference3KAMConsolidated': #開示への参照３、監査上の主要な検討事項、連結
				self.Reference3KAMConsolidated = fact.value

			elif fact.concept.qname.localName == 'Reference4KAMConsolidated': #開示への参照４、監査上の主要な検討事項、連結
				self.Reference4KAMConsolidated = fact.value

			elif fact.concept.qname.localName == 'Reference5KAMConsolidated': #開示への参照５、監査上の主要な検討事項、連結
				self.Reference5KAMConsolidated = fact.value

			elif fact.concept.qname.localName == 'DescriptionIncludingReasonKAMConsolidatedTextBlock': #内容及び理由、監査上の主要な検討事項、連結 [テキストブロック]
				self.DescriptionIncludingReasonKAMConsolidatedTextBlock = fact.value

			elif fact.concept.qname.localName == 'AuditorsResponseKAMConsolidatedTextBlock': #監査上の対応、監査上の主要な検討事項、連結 [テキストブロック]
				self.AuditorsResponseKAMConsolidatedTextBlock = fact.value

			elif fact.concept.qname.localName == 'KeyAuditMattersNonConsolidatedLineItems': #監査上の主要な検討事項、個別 [表示項目]
				self.KeyAuditMattersNonConsolidatedLineItems = fact.value

			elif fact.concept.qname.localName == 'ShortDescriptionKAMNonConsolidated': #見出し、監査上の主要な検討事項、個別
				self.ShortDescriptionKAMNonConsolidated = fact.value

			elif fact.concept.qname.localName == 'ReferenceKAMNonConsolidated': #開示への参照、監査上の主要な検討事項、個別
				self.ReferenceKAMNonConsolidated = fact.value

			elif fact.concept.qname.localName == 'Reference2KAMNonConsolidated': #開示への参照２、監査上の主要な検討事項、個別
				self.Reference2KAMNonConsolidated = fact.value

			elif fact.concept.qname.localName == 'Reference3KAMNonConsolidated': #開示への参照３、監査上の主要な検討事項、個別
				self.Reference3KAMNonConsolidated = fact.value

			elif fact.concept.qname.localName == 'Reference4KAMNonConsolidated': #開示への参照４、監査上の主要な検討事項、個別
				self.Reference4KAMNonConsolidated = fact.value

			elif fact.concept.qname.localName == 'Reference5KAMNonConsolidated': #開示への参照５、監査上の主要な検討事項、個別
				self.Reference5KAMNonConsolidated = fact.value

			elif fact.concept.qname.localName == 'DescriptionIncludingReasonKAMNonConsolidatedTextBlock': #内容及び理由、監査上の主要な検討事項、個別 [テキストブロック]
				self.DescriptionIncludingReasonKAMNonConsolidatedTextBlock = fact.value

			elif fact.concept.qname.localName == 'AuditorsResponseKAMNonConsolidatedTextBlock': #監査上の対応、監査上の主要な検討事項、個別 [テキストブロック]
				self.AuditorsResponseKAMNonConsolidatedTextBlock = fact.value

			elif fact.concept.qname.localName == 'SameAsKAMForConsolidatedFSKAMNonConsolidatedTextBlock': #連結と同一内容である旨、監査上の主要な検討事項、個別 [テキストブロック]
				self.SameAsKAMForConsolidatedFSKAMNonConsolidatedTextBlock = fact.value


	def getCabinetOfficeOrdinanceOnDisclosureOfCorporateInformationEtcFormNo3AnnualSecuritiesReportHeading(self): #企業内容等の開示に関する内閣府令 第三号様式 有価証券報告書 [目次項目]
		return self.CabinetOfficeOrdinanceOnDisclosureOfCorporateInformationEtcFormNo3AnnualSecuritiesReportHeading

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

	def getFiscalYearCoverPage(self): #事業年度、表紙
		return self.FiscalYearCoverPage

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

	def getNameOfContactPersonAddressOfRegisteredHeadquarterCoverPage(self): #事務連絡者氏名、本店の所在の場所、表紙
		return self.NameOfContactPersonAddressOfRegisteredHeadquarterCoverPage

	def getNearestPlaceOfContactCoverPage(self): #最寄りの連絡場所、表紙
		return self.NearestPlaceOfContactCoverPage

	def getTelephoneNumberNearestPlaceOfContactCoverPage(self): #電話番号、最寄りの連絡場所、表紙
		return self.TelephoneNumberNearestPlaceOfContactCoverPage

	def getNameOfContactPersonNearestPlaceOfContactCoverPage(self): #事務連絡者氏名、最寄りの連絡場所、表紙
		return self.NameOfContactPersonNearestPlaceOfContactCoverPage

	def getPlaceForPublicInspectionCoverPageTextBlock(self): #縦覧に供する場所、表紙 [テキストブロック]
		return self.PlaceForPublicInspectionCoverPageTextBlock

	def getFootnotesCoverPageTextBlock(self): #脚注、表紙 [テキストブロック]
		return self.FootnotesCoverPageTextBlock

	def getCompanyInformationHeading(self): #企業情報 [目次項目]
		return self.CompanyInformationHeading

	def getOverviewOfCompanyHeading(self): #企業の概況 [目次項目]
		return self.OverviewOfCompanyHeading

	def getSummaryOfBusinessResultsHeading(self): #主要な経営指標等の推移 [目次項目]
		return self.SummaryOfBusinessResultsHeading

	def getBusinessResultsOfGroupHeading(self): #連結経営指標等 [目次項目]
		return self.BusinessResultsOfGroupHeading

	def getBusinessResultsOfGroupTextBlock(self): #連結経営指標等 [テキストブロック]
		return self.BusinessResultsOfGroupTextBlock

	def getBusinessResultsOfGroupHeading(self): #連結経営指標等 [目次項目]
		return self.BusinessResultsOfGroupHeading

	def getBusinessResultsOfGroupTable(self): #連結経営指標等 [表]
		return self.BusinessResultsOfGroupTable

	def getConsolidatedOrNonConsolidatedAxis(self): #連結個別 [軸]
		return self.ConsolidatedOrNonConsolidatedAxis

	def getConsolidatedMember(self): #連結 [メンバー] ※ディメンションデフォルト
		return self.ConsolidatedMember

	def getBusinessResultsOfGroupLineItems(self): #連結経営指標等 [表示項目]
		return self.BusinessResultsOfGroupLineItems

	def getNetSalesSummaryOfBusinessResults(self): #売上高、経営指標等
		return self.NetSalesSummaryOfBusinessResults

	def getRevenueKeyFinancialData(self): #売上収益、経営指標等
		return self.RevenueKeyFinancialData

	def getOperatingRevenue1SummaryOfBusinessResults(self): #営業収益、経営指標等
		return self.OperatingRevenue1SummaryOfBusinessResults

	def getOperatingRevenue2SummaryOfBusinessResults(self): #営業収入、経営指標等
		return self.OperatingRevenue2SummaryOfBusinessResults

	def getGrossOperatingRevenueSummaryOfBusinessResults(self): #営業総収入、経営指標等
		return self.GrossOperatingRevenueSummaryOfBusinessResults

	def getOrdinaryIncomeSummaryOfBusinessResults(self): #経常収益、経営指標等
		return self.OrdinaryIncomeSummaryOfBusinessResults

	def getNetPremiumsWrittenSummaryOfBusinessResultsINS(self): #正味収入保険料、経営指標等、保険業
		return self.NetPremiumsWrittenSummaryOfBusinessResultsINS

	def getOrdinaryIncomeLossSummaryOfBusinessResults(self): #経常利益又は経常損失（△）、経営指標等
		return self.OrdinaryIncomeLossSummaryOfBusinessResults

	def getProfitLossAttributableToOwnersOfParentSummaryOfBusinessResults(self): #親会社株主に帰属する当期純利益又は親会社株主に帰属する当期純損失（△）、経営指標等
		return self.ProfitLossAttributableToOwnersOfParentSummaryOfBusinessResults

	def getComprehensiveIncomeSummaryOfBusinessResults(self): #包括利益、経営指標等
		return self.ComprehensiveIncomeSummaryOfBusinessResults

	def getNetAssetsSummaryOfBusinessResults(self): #純資産額、経営指標等
		return self.NetAssetsSummaryOfBusinessResults

	def getTotalAssetsSummaryOfBusinessResults(self): #総資産額、経営指標等
		return self.TotalAssetsSummaryOfBusinessResults

	def getNetAssetsPerShareSummaryOfBusinessResults(self): #１株当たり純資産額、経営指標等
		return self.NetAssetsPerShareSummaryOfBusinessResults

	def getBasicEarningsLossPerShareSummaryOfBusinessResults(self): #１株当たり当期純利益又は当期純損失（△）、経営指標等
		return self.BasicEarningsLossPerShareSummaryOfBusinessResults

	def getDilutedEarningsPerShareSummaryOfBusinessResults(self): #潜在株式調整後１株当たり当期純利益、経営指標等
		return self.DilutedEarningsPerShareSummaryOfBusinessResults

	def getEquityToAssetRatioSummaryOfBusinessResults(self): #自己資本比率、経営指標等
		return self.EquityToAssetRatioSummaryOfBusinessResults

	def getCapitalAdequacyRatioInternationalStandardSummaryOfBusinessResults(self): #自己資本比率（国際統一基準）、経営指標等
		return self.CapitalAdequacyRatioInternationalStandardSummaryOfBusinessResults

	def getCapitalAdequacyRatioDomesticStandardSummaryOfBusinessResults(self): #自己資本比率（国内基準）、経営指標等
		return self.CapitalAdequacyRatioDomesticStandardSummaryOfBusinessResults

	def getCapitalAdequacyRatioBISStandardSummaryOfBusinessResults(self): #自己資本比率（第一基準）、経営指標等
		return self.CapitalAdequacyRatioBISStandardSummaryOfBusinessResults

	def getCapitalAdequacyRatioDomesticStandard2SummaryOfBusinessResults(self): #自己資本比率（第二基準）、経営指標等
		return self.CapitalAdequacyRatioDomesticStandard2SummaryOfBusinessResults

	def getRateOfReturnOnEquitySummaryOfBusinessResults(self): #自己資本利益率、経営指標等
		return self.RateOfReturnOnEquitySummaryOfBusinessResults

	def getPriceEarningsRatioSummaryOfBusinessResults(self): #株価収益率、経営指標等
		return self.PriceEarningsRatioSummaryOfBusinessResults

	def getNetCashProvidedByUsedInOperatingActivitiesSummaryOfBusinessResults(self): #営業活動によるキャッシュ・フロー、経営指標等
		return self.NetCashProvidedByUsedInOperatingActivitiesSummaryOfBusinessResults

	def getNetCashProvidedByUsedInInvestingActivitiesSummaryOfBusinessResults(self): #投資活動によるキャッシュ・フロー、経営指標等
		return self.NetCashProvidedByUsedInInvestingActivitiesSummaryOfBusinessResults

	def getNetCashProvidedByUsedInFinancingActivitiesSummaryOfBusinessResults(self): #財務活動によるキャッシュ・フロー、経営指標等
		return self.NetCashProvidedByUsedInFinancingActivitiesSummaryOfBusinessResults

	def getCashAndCashEquivalentsSummaryOfBusinessResults(self): #現金及び現金同等物の残高、経営指標等
		return self.CashAndCashEquivalentsSummaryOfBusinessResults

	def getNumberOfEmployees(self): #従業員数
		return self.NumberOfEmployees

	def getAverageNumberOfTemporaryWorkers(self): #平均臨時雇用人員
		return self.AverageNumberOfTemporaryWorkers

	def getRevenueIFRSSummaryOfBusinessResults(self): #売上収益（IFRS）、経営指標等
		return self.RevenueIFRSSummaryOfBusinessResults

	def getProfitLossBeforeTaxIFRSSummaryOfBusinessResults(self): #税引前利益又は税引前損失（△）（IFRS）、経営指標等
		return self.ProfitLossBeforeTaxIFRSSummaryOfBusinessResults

	def getProfitLossFromContinuingOperationsIFRSSummaryOfBusinessResults(self): #継続事業からの当期利益又は当期損失（△）（IFRS）、経営指標等
		return self.ProfitLossFromContinuingOperationsIFRSSummaryOfBusinessResults

	def getProfitLossIFRSSummaryOfBusinessResults(self): #当期利益又は当期損失（△）（IFRS）、経営指標等
		return self.ProfitLossIFRSSummaryOfBusinessResults

	def getProfitLossAttributableToOwnersOfParentIFRSSummaryOfBusinessResults(self): #当期利益又は当期損失（△）：親会社の所有者に帰属（IFRS）、経営指標等
		return self.ProfitLossAttributableToOwnersOfParentIFRSSummaryOfBusinessResults

	def getComprehensiveIncomeIFRSSummaryOfBusinessResults(self): #当期包括利益（IFRS）、経営指標等
		return self.ComprehensiveIncomeIFRSSummaryOfBusinessResults

	def getComprehensiveIncomeAttributableToOwnersOfParentIFRSSummaryOfBusinessResults(self): #当期包括利益：親会社の所有者に帰属（IFRS）、経営指標等
		return self.ComprehensiveIncomeAttributableToOwnersOfParentIFRSSummaryOfBusinessResults

	def getEquityAttributableToOwnersOfParentIFRSSummaryOfBusinessResults(self): #親会社の所有者に帰属する持分（IFRS）、経営指標等
		return self.EquityAttributableToOwnersOfParentIFRSSummaryOfBusinessResults

	def getTotalAssetsIFRSSummaryOfBusinessResults(self): #総資産額（IFRS）、経営指標等
		return self.TotalAssetsIFRSSummaryOfBusinessResults

	def getEquityToAssetRatioIFRSSummaryOfBusinessResults(self): #１株当たり親会社所有者帰属持分（IFRS）、経営指標等
		return self.EquityToAssetRatioIFRSSummaryOfBusinessResults

	def getBasicEarningsLossPerShareIFRSSummaryOfBusinessResults(self): #基本的１株当たり利益又は損失（△）（IFRS）、経営指標等
		return self.BasicEarningsLossPerShareIFRSSummaryOfBusinessResults

	def getDilutedEarningsLossPerShareIFRSSummaryOfBusinessResults(self): #希薄化後１株当たり利益又は損失（△）（IFRS）、経営指標等
		return self.DilutedEarningsLossPerShareIFRSSummaryOfBusinessResults

	def getRatioOfOwnersEquityToGrossAssetsIFRSSummaryOfBusinessResults(self): #親会社所有者帰属持分比率（IFRS）、経営指標等
		return self.RatioOfOwnersEquityToGrossAssetsIFRSSummaryOfBusinessResults

	def getRateOfReturnOnEquityIFRSSummaryOfBusinessResults(self): #親会社所有者帰属持分利益率（IFRS）、経営指標等
		return self.RateOfReturnOnEquityIFRSSummaryOfBusinessResults

	def getPriceEarningsRatioIFRSSummaryOfBusinessResults(self): #株価収益率（IFRS）、経営指標等
		return self.PriceEarningsRatioIFRSSummaryOfBusinessResults

	def getCashFlowsFromUsedInOperatingActivitiesIFRSSummaryOfBusinessResults(self): #営業活動によるキャッシュ・フロー（IFRS）、経営指標等
		return self.CashFlowsFromUsedInOperatingActivitiesIFRSSummaryOfBusinessResults

	def getCashFlowsFromUsedInInvestingActivitiesIFRSSummaryOfBusinessResults(self): #投資活動によるキャッシュ・フロー（IFRS）、経営指標等
		return self.CashFlowsFromUsedInInvestingActivitiesIFRSSummaryOfBusinessResults

	def getCashFlowsFromUsedInFinancingActivitiesIFRSSummaryOfBusinessResults(self): #財務活動によるキャッシュ・フロー（IFRS）、経営指標等
		return self.CashFlowsFromUsedInFinancingActivitiesIFRSSummaryOfBusinessResults

	def getCashAndCashEquivalentsIFRSSummaryOfBusinessResults(self): #現金及び現金同等物（IFRS）、経営指標等
		return self.CashAndCashEquivalentsIFRSSummaryOfBusinessResults

	def getRevenueJMISSummaryOfBusinessResults(self): #売上収益（JMIS）、経営指標等
		return self.RevenueJMISSummaryOfBusinessResults

	def getProfitLossBeforeTaxJMISSummaryOfBusinessResults(self): #税引前利益又は税引前損失（△）（JMIS）、経営指標等
		return self.ProfitLossBeforeTaxJMISSummaryOfBusinessResults

	def getProfitLossFromContinuingOperationsJMISSummaryOfBusinessResults(self): #継続事業からの当期利益又は当期損失（△）（JMIS）、経営指標等
		return self.ProfitLossFromContinuingOperationsJMISSummaryOfBusinessResults

	def getProfitLossJMISSummaryOfBusinessResults(self): #当期利益又は当期損失（△）（JMIS）、経営指標等
		return self.ProfitLossJMISSummaryOfBusinessResults

	def getProfitLossAttributableToOwnersOfParentJMISSummaryOfBusinessResults(self): #当期利益又は当期損失（△）：親会社の所有者に帰属（JMIS）、経営指標等
		return self.ProfitLossAttributableToOwnersOfParentJMISSummaryOfBusinessResults

	def getComprehensiveIncomeJMISSummaryOfBusinessResults(self): #当期包括利益（JMIS）、経営指標等
		return self.ComprehensiveIncomeJMISSummaryOfBusinessResults

	def getComprehensiveIncomeAttributableToOwnersOfParentJMISSummaryOfBusinessResults(self): #当期包括利益：親会社の所有者に帰属（JMIS）、経営指標等
		return self.ComprehensiveIncomeAttributableToOwnersOfParentJMISSummaryOfBusinessResults

	def getEquityAttributableToOwnersOfParentJMISSummaryOfBusinessResults(self): #親会社の所有者に帰属する持分（JMIS）、経営指標等
		return self.EquityAttributableToOwnersOfParentJMISSummaryOfBusinessResults

	def getTotalAssetsJMISSummaryOfBusinessResults(self): #総資産額（JMIS）、経営指標等
		return self.TotalAssetsJMISSummaryOfBusinessResults

	def getEquityToAssetRatioJMISSummaryOfBusinessResults(self): #１株当たり親会社所有者帰属持分（JMIS）、経営指標等
		return self.EquityToAssetRatioJMISSummaryOfBusinessResults

	def getBasicEarningsLossPerShareJMISSummaryOfBusinessResults(self): #基本的１株当たり利益又は損失（△）（JMIS）、経営指標等
		return self.BasicEarningsLossPerShareJMISSummaryOfBusinessResults

	def getDilutedEarningsLossPerShareJMISSummaryOfBusinessResults(self): #希薄化後１株当たり利益又は損失（△）（JMIS）、経営指標等
		return self.DilutedEarningsLossPerShareJMISSummaryOfBusinessResults

	def getRatioOfOwnersEquityToGrossAssetsJMISSummaryOfBusinessResults(self): #親会社所有者帰属持分比率（JMIS）、経営指標等
		return self.RatioOfOwnersEquityToGrossAssetsJMISSummaryOfBusinessResults

	def getRateOfReturnOnEquityJMISSummaryOfBusinessResults(self): #親会社所有者帰属持分利益率（JMIS）、経営指標等
		return self.RateOfReturnOnEquityJMISSummaryOfBusinessResults

	def getPriceEarningsRatioJMISSummaryOfBusinessResults(self): #株価収益率（JMIS）、経営指標等
		return self.PriceEarningsRatioJMISSummaryOfBusinessResults

	def getCashFlowsFromUsedInOperatingActivitiesJMISSummaryOfBusinessResults(self): #営業活動によるキャッシュ・フロー（JMIS）、経営指標等
		return self.CashFlowsFromUsedInOperatingActivitiesJMISSummaryOfBusinessResults

	def getCashFlowsFromUsedInInvestingActivitiesJMISSummaryOfBusinessResults(self): #投資活動によるキャッシュ・フロー（JMIS）、経営指標等
		return self.CashFlowsFromUsedInInvestingActivitiesJMISSummaryOfBusinessResults

	def getCashFlowsFromUsedInFinancingActivitiesJMISSummaryOfBusinessResults(self): #財務活動によるキャッシュ・フロー（JMIS）、経営指標等
		return self.CashFlowsFromUsedInFinancingActivitiesJMISSummaryOfBusinessResults

	def getCashAndCashEquivalentsJMISSummaryOfBusinessResults(self): #現金及び現金同等物（JMIS）、経営指標等
		return self.CashAndCashEquivalentsJMISSummaryOfBusinessResults

	def getRevenuesUSGAAPSummaryOfBusinessResults(self): #売上高（US GAAP）、経営指標等
		return self.RevenuesUSGAAPSummaryOfBusinessResults

	def getOperatingIncomeLossUSGAAPSummaryOfBusinessResults(self): #営業利益又は営業損失（△）（US GAAP）、経営指標等
		return self.OperatingIncomeLossUSGAAPSummaryOfBusinessResults

	def getProfitLossBeforeTaxUSGAAPSummaryOfBusinessResults(self): #税引前利益又は税引前損失（△）（US GAAP）、経営指標等
		return self.ProfitLossBeforeTaxUSGAAPSummaryOfBusinessResults

	def getNetIncomeLossAttributableToOwnersOfParentUSGAAPSummaryOfBusinessResults(self): #当社株主に帰属する純利益又は純損失（△）（US GAAP）、経営指標等
		return self.NetIncomeLossAttributableToOwnersOfParentUSGAAPSummaryOfBusinessResults

	def getComprehensiveIncomeUSGAAPSummaryOfBusinessResults(self): #包括利益（US GAAP）、経営指標等
		return self.ComprehensiveIncomeUSGAAPSummaryOfBusinessResults

	def getComprehensiveIncomeAttributableToOwnersOfParentUSGAAPSummaryOfBusinessResults(self): #当社株主に帰属する包括利益（US GAAP）、経営指標等
		return self.ComprehensiveIncomeAttributableToOwnersOfParentUSGAAPSummaryOfBusinessResults

	def getEquityAttributableToOwnersOfParentUSGAAPSummaryOfBusinessResults(self): #株主資本（US GAAP）、経営指標等
		return self.EquityAttributableToOwnersOfParentUSGAAPSummaryOfBusinessResults

	def getEquityIncludingPortionAttributableToNonControllingInterestUSGAAPSummaryOfBusinessResults(self): #純資産額（US GAAP）、経営指標等
		return self.EquityIncludingPortionAttributableToNonControllingInterestUSGAAPSummaryOfBusinessResults

	def getTotalAssetsUSGAAPSummaryOfBusinessResults(self): #総資産額（US GAAP）、経営指標等
		return self.TotalAssetsUSGAAPSummaryOfBusinessResults

	def getEquityAttributableToOwnersOfParentPerShareUSGAAPSummaryOfBusinessResults(self): #１株当たり株主資本（US GAAP）、経営指標等
		return self.EquityAttributableToOwnersOfParentPerShareUSGAAPSummaryOfBusinessResults

	def getBasicEarningsLossPerShareUSGAAPSummaryOfBusinessResults(self): #基本的１株当たり当社株主に帰属する利益又は損失（△）（US GAAP）、経営指標等
		return self.BasicEarningsLossPerShareUSGAAPSummaryOfBusinessResults

	def getDilutedEarningsLossPerShareUSGAAPSummaryOfBusinessResults(self): #希薄化後１株当たり当社株主に帰属する利益又は損失（△）（US GAAP）、経営指標等
		return self.DilutedEarningsLossPerShareUSGAAPSummaryOfBusinessResults

	def getEquityToAssetRatioUSGAAPSummaryOfBusinessResults(self): #自己資本比率（US GAAP）、経営指標等
		return self.EquityToAssetRatioUSGAAPSummaryOfBusinessResults

	def getPriceEarningsRatioUSGAAPSummaryOfBusinessResults(self): #株価収益率（US GAAP）、経営指標等
		return self.PriceEarningsRatioUSGAAPSummaryOfBusinessResults

	def getRateOfReturnOnEquityUSGAAPSummaryOfBusinessResults(self): #株主資本利益率（US GAAP）、経営指標等
		return self.RateOfReturnOnEquityUSGAAPSummaryOfBusinessResults

	def getCashFlowsFromUsedInOperatingActivitiesUSGAAPSummaryOfBusinessResults(self): #営業活動によるキャッシュ・フロー（US GAAP）、経営指標等
		return self.CashFlowsFromUsedInOperatingActivitiesUSGAAPSummaryOfBusinessResults

	def getCashFlowsFromUsedInInvestingActivitiesUSGAAPSummaryOfBusinessResults(self): #投資活動によるキャッシュ・フロー（US GAAP）、経営指標等
		return self.CashFlowsFromUsedInInvestingActivitiesUSGAAPSummaryOfBusinessResults

	def getCashFlowsFromUsedInFinancingActivitiesUSGAAPSummaryOfBusinessResults(self): #財務活動によるキャッシュ・フロー（US GAAP）、経営指標等
		return self.CashFlowsFromUsedInFinancingActivitiesUSGAAPSummaryOfBusinessResults

	def getCashAndCashEquivalentsUSGAAPSummaryOfBusinessResults(self): #現金及び現金同等物（US GAAP）、経営指標等
		return self.CashAndCashEquivalentsUSGAAPSummaryOfBusinessResults

	def getBusinessResultsOfReportingCompanyHeading(self): #提出会社の経営指標等 [目次項目]
		return self.BusinessResultsOfReportingCompanyHeading

	def getBusinessResultsOfReportingCompanyTextBlock(self): #提出会社の経営指標等 [テキストブロック]
		return self.BusinessResultsOfReportingCompanyTextBlock

	def getBusinessResultsOfReportingCompanyHeading(self): #提出会社の経営指標等 [目次項目]
		return self.BusinessResultsOfReportingCompanyHeading

	def getBusinessResultsOfReportingCompanyTable(self): #提出会社の経営指標等 [表]
		return self.BusinessResultsOfReportingCompanyTable

	def getConsolidatedOrNonConsolidatedAxis(self): #連結個別 [軸]
		return self.ConsolidatedOrNonConsolidatedAxis

	def getNonConsolidatedMember(self): #非連結又は個別 [メンバー]
		return self.NonConsolidatedMember

	def getBusinessResultsOfReportingCompanyLineItems(self): #提出会社の経営指標等 [表示項目]
		return self.BusinessResultsOfReportingCompanyLineItems

	def getNetSalesSummaryOfBusinessResults(self): #売上高、経営指標等
		return self.NetSalesSummaryOfBusinessResults

	def getRevenueKeyFinancialData(self): #売上収益、経営指標等
		return self.RevenueKeyFinancialData

	def getOperatingRevenue1SummaryOfBusinessResults(self): #営業収益、経営指標等
		return self.OperatingRevenue1SummaryOfBusinessResults

	def getOperatingRevenue2SummaryOfBusinessResults(self): #営業収入、経営指標等
		return self.OperatingRevenue2SummaryOfBusinessResults

	def getGrossOperatingRevenueSummaryOfBusinessResults(self): #営業総収入、経営指標等
		return self.GrossOperatingRevenueSummaryOfBusinessResults

	def getOrdinaryIncomeSummaryOfBusinessResults(self): #経常収益、経営指標等
		return self.OrdinaryIncomeSummaryOfBusinessResults

	def getNetPremiumsWrittenSummaryOfBusinessResultsINS(self): #正味収入保険料、経営指標等、保険業
		return self.NetPremiumsWrittenSummaryOfBusinessResultsINS

	def getOrdinaryIncomeLossSummaryOfBusinessResults(self): #経常利益又は経常損失（△）、経営指標等
		return self.OrdinaryIncomeLossSummaryOfBusinessResults

	def getNetIncomeLossSummaryOfBusinessResults(self): #当期純利益又は当期純損失（△）、経営指標等
		return self.NetIncomeLossSummaryOfBusinessResults

	def getNetLossRatioSummaryOfBusinessResultsINS(self): #正味損害率、経営指標等、保険業
		return self.NetLossRatioSummaryOfBusinessResultsINS

	def getNetOperatingExpenseRatioSummaryOfBusinessResultsINS(self): #正味事業費率、経営指標等、保険業
		return self.NetOperatingExpenseRatioSummaryOfBusinessResultsINS

	def getInterestAndDividendIncomeSummaryOfBusinessResultsINS(self): #利息及び配当金収入、経営指標等、保険業
		return self.InterestAndDividendIncomeSummaryOfBusinessResultsINS

	def getInvestmentAssetsYieldIncomeYieldSummaryOfBusinessResultsINS(self): #運用資産利回り（インカム利回り）、経営指標等、保険業
		return self.InvestmentAssetsYieldIncomeYieldSummaryOfBusinessResultsINS

	def getInvestmentYieldRealizedYieldSummaryOfBusinessResultsINS(self): #資産運用利回り（実現利回り）、経営指標等、保険業
		return self.InvestmentYieldRealizedYieldSummaryOfBusinessResultsINS

	def getEquityInEarningsLossesOfAffiliatesIfEquityMethodIsAppliedSummaryOfBusinessResults(self): #持分法を適用した場合の投資利益又は投資損失（△）、経営指標等
		return self.EquityInEarningsLossesOfAffiliatesIfEquityMethodIsAppliedSummaryOfBusinessResults

	def getCapitalStockSummaryOfBusinessResults(self): #資本金、経営指標等
		return self.CapitalStockSummaryOfBusinessResults

	def getTotalNumberOfIssuedSharesSummaryOfBusinessResults(self): #発行済株式総数（普通株式）、経営指標等
		return self.TotalNumberOfIssuedSharesSummaryOfBusinessResults

	def getNetAssetsSummaryOfBusinessResults(self): #純資産額、経営指標等
		return self.NetAssetsSummaryOfBusinessResults

	def getTotalAssetsSummaryOfBusinessResults(self): #総資産額、経営指標等
		return self.TotalAssetsSummaryOfBusinessResults

	def getDepositsSummaryOfBusinessResults(self): #預金残高、経営指標等
		return self.DepositsSummaryOfBusinessResults

	def getLoansAndBillsDiscountedSummaryOfBusinessResults(self): #貸出金残高、経営指標等
		return self.LoansAndBillsDiscountedSummaryOfBusinessResults

	def getSecuritiesSummaryOfBusinessResults(self): #有価証券残高、経営指標等
		return self.SecuritiesSummaryOfBusinessResults

	def getNetAssetsPerShareSummaryOfBusinessResults(self): #１株当たり純資産額、経営指標等
		return self.NetAssetsPerShareSummaryOfBusinessResults

	def getDividendPaidPerShareSummaryOfBusinessResults(self): #１株当たり配当額、経営指標等
		return self.DividendPaidPerShareSummaryOfBusinessResults

	def getInterimDividendPaidPerShareSummaryOfBusinessResults(self): #１株当たり中間配当額、経営指標等
		return self.InterimDividendPaidPerShareSummaryOfBusinessResults

	def getFirstQuarterDividendPaidPerShareSummaryOfBusinessResults(self): #１株当たり第１四半期配当額、経営指標等
		return self.FirstQuarterDividendPaidPerShareSummaryOfBusinessResults

	def getSecondQuarterDividendPaidPerShareSummaryOfBusinessResults(self): #１株当たり第２四半期配当額、経営指標等
		return self.SecondQuarterDividendPaidPerShareSummaryOfBusinessResults

	def getThirdQuarterDividendPaidPerShareSummaryOfBusinessResults(self): #１株当たり第３四半期配当額、経営指標等
		return self.ThirdQuarterDividendPaidPerShareSummaryOfBusinessResults

	def getFourthQuarterDividendPaidPerShareSummaryOfBusinessResults(self): #１株当たり第４四半期配当額、経営指標等
		return self.FourthQuarterDividendPaidPerShareSummaryOfBusinessResults

	def getFifthQuarterDividendPaidPerShareSummaryOfBusinessResults(self): #１株当たり第５四半期配当額、経営指標等
		return self.FifthQuarterDividendPaidPerShareSummaryOfBusinessResults

	def getBasicEarningsLossPerShareSummaryOfBusinessResults(self): #１株当たり当期純利益又は当期純損失（△）、経営指標等
		return self.BasicEarningsLossPerShareSummaryOfBusinessResults

	def getDilutedEarningsPerShareSummaryOfBusinessResults(self): #潜在株式調整後１株当たり当期純利益、経営指標等
		return self.DilutedEarningsPerShareSummaryOfBusinessResults

	def getEquityToAssetRatioSummaryOfBusinessResults(self): #自己資本比率、経営指標等
		return self.EquityToAssetRatioSummaryOfBusinessResults

	def getCapitalAdequacyRatioInternationalStandardSummaryOfBusinessResults(self): #自己資本比率（国際統一基準）、経営指標等
		return self.CapitalAdequacyRatioInternationalStandardSummaryOfBusinessResults

	def getCapitalAdequacyRatioDomesticStandardSummaryOfBusinessResults(self): #自己資本比率（国内基準）、経営指標等
		return self.CapitalAdequacyRatioDomesticStandardSummaryOfBusinessResults

	def getCapitalAdequacyRatioBISStandardSummaryOfBusinessResults(self): #自己資本比率（第一基準）、経営指標等
		return self.CapitalAdequacyRatioBISStandardSummaryOfBusinessResults

	def getCapitalAdequacyRatioDomesticStandard2SummaryOfBusinessResults(self): #自己資本比率（第二基準）、経営指標等
		return self.CapitalAdequacyRatioDomesticStandard2SummaryOfBusinessResults

	def getRateOfReturnOnEquitySummaryOfBusinessResults(self): #自己資本利益率、経営指標等
		return self.RateOfReturnOnEquitySummaryOfBusinessResults

	def getPriceEarningsRatioSummaryOfBusinessResults(self): #株価収益率、経営指標等
		return self.PriceEarningsRatioSummaryOfBusinessResults

	def getPayoutRatioSummaryOfBusinessResults(self): #配当性向、経営指標等
		return self.PayoutRatioSummaryOfBusinessResults

	def getNetCashProvidedByUsedInOperatingActivitiesSummaryOfBusinessResults(self): #営業活動によるキャッシュ・フロー、経営指標等
		return self.NetCashProvidedByUsedInOperatingActivitiesSummaryOfBusinessResults

	def getNetCashProvidedByUsedInInvestingActivitiesSummaryOfBusinessResults(self): #投資活動によるキャッシュ・フロー、経営指標等
		return self.NetCashProvidedByUsedInInvestingActivitiesSummaryOfBusinessResults

	def getNetCashProvidedByUsedInFinancingActivitiesSummaryOfBusinessResults(self): #財務活動によるキャッシュ・フロー、経営指標等
		return self.NetCashProvidedByUsedInFinancingActivitiesSummaryOfBusinessResults

	def getCashAndCashEquivalentsSummaryOfBusinessResults(self): #現金及び現金同等物の残高、経営指標等
		return self.CashAndCashEquivalentsSummaryOfBusinessResults

	def getNumberOfEmployees(self): #従業員数
		return self.NumberOfEmployees

	def getAverageNumberOfTemporaryWorkers(self): #平均臨時雇用人員
		return self.AverageNumberOfTemporaryWorkers

	def getTotalShareholderReturn(self): #株主総利回り
		return self.TotalShareholderReturn

	def getTotalReturnOnSharePriceIndex(self): #株価指数における総利回り
		return self.TotalReturnOnSharePriceIndex

	def getCompanyHistoryHeading(self): #沿革 [目次項目]
		return self.CompanyHistoryHeading

	def getCompanyHistoryTextBlock(self): #沿革 [テキストブロック]
		return self.CompanyHistoryTextBlock

	def getDescriptionOfBusinessHeading(self): #事業の内容 [目次項目]
		return self.DescriptionOfBusinessHeading

	def getDescriptionOfBusinessTextBlock(self): #事業の内容 [テキストブロック]
		return self.DescriptionOfBusinessTextBlock

	def getOverviewOfAffiliatedEntitiesHeading(self): #関係会社の状況 [目次項目]
		return self.OverviewOfAffiliatedEntitiesHeading

	def getOverviewOfAffiliatedEntitiesTextBlock(self): #関係会社の状況 [テキストブロック]
		return self.OverviewOfAffiliatedEntitiesTextBlock

	def getInformationAboutEmployeesHeading(self): #従業員の状況 [目次項目]
		return self.InformationAboutEmployeesHeading

	def getInformationAboutEmployeesTextBlock(self): #従業員の状況 [テキストブロック]
		return self.InformationAboutEmployeesTextBlock

	def getInformationAboutEmployeesHeading(self): #従業員の状況 [目次項目]
		return self.InformationAboutEmployeesHeading

	def getInformationAboutGroupInformationAboutEmployeesAbstract(self): #連結会社の状況、従業員の状況 [タイトル項目]
		return self.InformationAboutGroupInformationAboutEmployeesAbstract

	def getNumberOfEmployeesOfGroupTable(self): #連結会社の従業員数 [表]
		return self.NumberOfEmployeesOfGroupTable

	def getConsolidatedOrNonConsolidatedAxis(self): #連結個別 [軸]
		return self.ConsolidatedOrNonConsolidatedAxis

	def getConsolidatedMember(self): #連結 [メンバー] ※ディメンションデフォルト
		return self.ConsolidatedMember

	def getOperatingSegmentsAxis(self): #事業セグメント [軸]
		return self.OperatingSegmentsAxis

	def getEntityTotalMember(self): #連結合計又は会社合計 [メンバー] ※ディメンションデフォルト
		return self.EntityTotalMember

	def getReportableSegmentsMember(self): #報告セグメント [メンバー]
		return self.ReportableSegmentsMember

	def getOtherReportableSegmentsMember(self): #その他の報告セグメント [メンバー]
		return self.OtherReportableSegmentsMember

	def getOperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember(self): #報告セグメント以外の全てのセグメント [メンバー]
		return self.OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember

	def getCorporateSharedMember(self): #全社（共通） [メンバー]
		return self.CorporateSharedMember

	def getOtherOperatingSegmentsAxisMember(self): #その他、事業セグメント軸 [メンバー]
		return self.OtherOperatingSegmentsAxisMember

	def getNumberOfEmployeesOfGroupLineItems(self): #連結会社の従業員数 [表示項目]
		return self.NumberOfEmployeesOfGroupLineItems

	def getNumberOfEmployees(self): #従業員数
		return self.NumberOfEmployees

	def getAverageNumberOfTemporaryWorkers(self): #平均臨時雇用人員
		return self.AverageNumberOfTemporaryWorkers

	def getInformationAboutEmployeesHeading(self): #従業員の状況 [目次項目]
		return self.InformationAboutEmployeesHeading

	def getInformationAboutReportingCompanyInformationAboutEmployeesAbstract(self): #提出会社の状況、従業員の状況 [タイトル項目]
		return self.InformationAboutReportingCompanyInformationAboutEmployeesAbstract

	def getInformationAboutEmployeesOfReportingCompanyTable(self): #提出会社の従業員の状況 [表]
		return self.InformationAboutEmployeesOfReportingCompanyTable

	def getConsolidatedOrNonConsolidatedAxis(self): #連結個別 [軸]
		return self.ConsolidatedOrNonConsolidatedAxis

	def getNonConsolidatedMember(self): #非連結又は個別 [メンバー]
		return self.NonConsolidatedMember

	def getInformationAboutEmployeesOfReportingCompanyLineItems(self): #提出会社の従業員の状況 [表示項目]
		return self.InformationAboutEmployeesOfReportingCompanyLineItems

	def getNumberOfEmployees(self): #従業員数
		return self.NumberOfEmployees

	def getAverageNumberOfTemporaryWorkers(self): #平均臨時雇用人員
		return self.AverageNumberOfTemporaryWorkers

	def getAverageAgeYearsInformationAboutReportingCompanyInformationAboutEmployees(self): #平均年齢（年）、提出会社の状況、従業員の状況
		return self.AverageAgeYearsInformationAboutReportingCompanyInformationAboutEmployees

	def getAverageAgeMonthsInformationAboutReportingCompanyInformationAboutEmployees(self): #平均年齢（月）、提出会社の状況、従業員の状況
		return self.AverageAgeMonthsInformationAboutReportingCompanyInformationAboutEmployees

	def getAverageLengthOfServiceYearsInformationAboutReportingCompanyInformationAboutEmployees(self): #平均勤続年数（年）、提出会社の状況、従業員の状況
		return self.AverageLengthOfServiceYearsInformationAboutReportingCompanyInformationAboutEmployees

	def getAverageLengthOfServiceMonthsInformationAboutReportingCompanyInformationAboutEmployees(self): #平均勤続年数（月）、提出会社の状況、従業員の状況
		return self.AverageLengthOfServiceMonthsInformationAboutReportingCompanyInformationAboutEmployees

	def getAverageAnnualSalaryInformationAboutReportingCompanyInformationAboutEmployees(self): #平均年間給与、提出会社の状況、従業員の状況
		return self.AverageAnnualSalaryInformationAboutReportingCompanyInformationAboutEmployees

	def getInformationAboutEmployeesHeading(self): #従業員の状況 [目次項目]
		return self.InformationAboutEmployeesHeading

	def getInformationAboutReportingCompanyInformationAboutEmployeesAbstract(self): #提出会社の状況、従業員の状況 [タイトル項目]
		return self.InformationAboutReportingCompanyInformationAboutEmployeesAbstract

	def getNumberOfEmployeesOfReportingCompanyTable(self): #提出会社の従業員数 [表]
		return self.NumberOfEmployeesOfReportingCompanyTable

	def getConsolidatedOrNonConsolidatedAxis(self): #連結個別 [軸]
		return self.ConsolidatedOrNonConsolidatedAxis

	def getNonConsolidatedMember(self): #非連結又は個別 [メンバー]
		return self.NonConsolidatedMember

	def getOperatingSegmentsAxis(self): #事業セグメント [軸]
		return self.OperatingSegmentsAxis

	def getEntityTotalMember(self): #連結合計又は会社合計 [メンバー] ※ディメンションデフォルト
		return self.EntityTotalMember

	def getReportableSegmentsMember(self): #報告セグメント [メンバー]
		return self.ReportableSegmentsMember

	def getOtherReportableSegmentsMember(self): #その他の報告セグメント [メンバー]
		return self.OtherReportableSegmentsMember

	def getOperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember(self): #報告セグメント以外の全てのセグメント [メンバー]
		return self.OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember

	def getCorporateSharedMember(self): #全社（共通） [メンバー]
		return self.CorporateSharedMember

	def getOtherOperatingSegmentsAxisMember(self): #その他、事業セグメント軸 [メンバー]
		return self.OtherOperatingSegmentsAxisMember

	def getNumberOfEmployeesOfReportingCompanyLineItems(self): #提出会社の従業員数 [表示項目]
		return self.NumberOfEmployeesOfReportingCompanyLineItems

	def getNumberOfEmployees(self): #従業員数
		return self.NumberOfEmployees

	def getAverageNumberOfTemporaryWorkers(self): #平均臨時雇用人員
		return self.AverageNumberOfTemporaryWorkers

	def getOverviewOfBusinessHeading(self): #事業の状況 [目次項目]
		return self.OverviewOfBusinessHeading

	def getBusinessPolicyBusinessEnvironmentIssuesToAddressEtcHeading(self): #経営方針、経営環境及び対処すべき課題等 [目次項目]
		return self.BusinessPolicyBusinessEnvironmentIssuesToAddressEtcHeading

	def getBusinessPolicyBusinessEnvironmentIssuesToAddressEtcTextBlock(self): #経営方針、経営環境及び対処すべき課題等 [テキストブロック]
		return self.BusinessPolicyBusinessEnvironmentIssuesToAddressEtcTextBlock

	def getBusinessRisksHeading(self): #事業等のリスク [目次項目]
		return self.BusinessRisksHeading

	def getBusinessRisksTextBlock(self): #事業等のリスク [テキストブロック]
		return self.BusinessRisksTextBlock

	def getMaterialMattersRelatingToGoingConcernEtcBusinessRisksTextBlock(self): #重要事象等の内容、分析及び対応策、事業等のリスク [テキストブロック]
		return self.MaterialMattersRelatingToGoingConcernEtcBusinessRisksTextBlock

	def getManagementAnalysisOfFinancialPositionOperatingResultsAndCashFlowsHeading(self): #経営者による財政状態、経営成績及びキャッシュ・フローの状況の分析 [目次項目]
		return self.ManagementAnalysisOfFinancialPositionOperatingResultsAndCashFlowsHeading

	def getManagementAnalysisOfFinancialPositionOperatingResultsAndCashFlowsTextBlock(self): #経営者による財政状態、経営成績及びキャッシュ・フローの状況の分析 [テキストブロック]
		return self.ManagementAnalysisOfFinancialPositionOperatingResultsAndCashFlowsTextBlock

	def getCriticalContractsForOperationHeading(self): #経営上の重要な契約等 [目次項目]
		return self.CriticalContractsForOperationHeading

	def getCriticalContractsForOperationTextBlock(self): #経営上の重要な契約等 [テキストブロック]
		return self.CriticalContractsForOperationTextBlock

	def getResearchAndDevelopmentActivitiesHeading(self): #研究開発活動 [目次項目]
		return self.ResearchAndDevelopmentActivitiesHeading

	def getResearchAndDevelopmentActivitiesTextBlock(self): #研究開発活動 [テキストブロック]
		return self.ResearchAndDevelopmentActivitiesTextBlock

	def getResearchAndDevelopmentActivitiesHeading(self): #研究開発活動 [目次項目]
		return self.ResearchAndDevelopmentActivitiesHeading

	def getResearchAndDevelopmentExpensesResearchAndDevelopmentActivitiesTable(self): #研究開発費、研究開発活動 [表]
		return self.ResearchAndDevelopmentExpensesResearchAndDevelopmentActivitiesTable

	def getOperatingSegmentsAxis(self): #事業セグメント [軸]
		return self.OperatingSegmentsAxis

	def getEntityTotalMember(self): #連結合計又は会社合計 [メンバー] ※ディメンションデフォルト
		return self.EntityTotalMember

	def getReportableSegmentsMember(self): #報告セグメント [メンバー]
		return self.ReportableSegmentsMember

	def getOtherReportableSegmentsMember(self): #その他の報告セグメント [メンバー]
		return self.OtherReportableSegmentsMember

	def getResearchAndDevelopmentExpensesResearchAndDevelopmentActivitiesLineItems(self): #研究開発費、研究開発活動 [表示項目]
		return self.ResearchAndDevelopmentExpensesResearchAndDevelopmentActivitiesLineItems

	def getResearchAndDevelopmentExpensesResearchAndDevelopmentActivities(self): #研究開発費、研究開発活動
		return self.ResearchAndDevelopmentExpensesResearchAndDevelopmentActivities

	def getInformationAboutFacilitiesHeading(self): #設備の状況 [目次項目]
		return self.InformationAboutFacilitiesHeading

	def getOverviewOfCapitalExpendituresEtcHeading(self): #設備投資等の概要 [目次項目]
		return self.OverviewOfCapitalExpendituresEtcHeading

	def getOverviewOfCapitalExpendituresEtcTextBlock(self): #設備投資等の概要 [テキストブロック]
		return self.OverviewOfCapitalExpendituresEtcTextBlock

	def getOverviewOfCapitalExpendituresEtcHeading(self): #設備投資等の概要 [目次項目]
		return self.OverviewOfCapitalExpendituresEtcHeading

	def getCapitalExpendituresOverviewOfCapitalExpendituresEtcTable(self): #設備投資額、設備投資等の概要 [表]
		return self.CapitalExpendituresOverviewOfCapitalExpendituresEtcTable

	def getOperatingSegmentsAxis(self): #事業セグメント [軸]
		return self.OperatingSegmentsAxis

	def getEntityTotalMember(self): #連結合計又は会社合計 [メンバー] ※ディメンションデフォルト
		return self.EntityTotalMember

	def getReportableSegmentsMember(self): #報告セグメント [メンバー]
		return self.ReportableSegmentsMember

	def getOtherReportableSegmentsMember(self): #その他の報告セグメント [メンバー]
		return self.OtherReportableSegmentsMember

	def getCapitalExpendituresOverviewOfCapitalExpendituresEtcLineItems(self): #設備投資額、設備投資等の概要 [表示項目]
		return self.CapitalExpendituresOverviewOfCapitalExpendituresEtcLineItems

	def getCapitalExpendituresOverviewOfCapitalExpendituresEtc(self): #設備投資額、設備投資等の概要
		return self.CapitalExpendituresOverviewOfCapitalExpendituresEtc

	def getMajorFacilitiesHeading(self): #主要な設備の状況 [目次項目]
		return self.MajorFacilitiesHeading

	def getMajorFacilitiesTextBlock(self): #主要な設備の状況 [テキストブロック]
		return self.MajorFacilitiesTextBlock

	def getPlannedAdditionsRetirementsEtcOfFacilitiesHeading(self): #設備の新設、除却等の計画 [目次項目]
		return self.PlannedAdditionsRetirementsEtcOfFacilitiesHeading

	def getPlannedAdditionsRetirementsEtcOfFacilitiesTextBlock(self): #設備の新設、除却等の計画 [テキストブロック]
		return self.PlannedAdditionsRetirementsEtcOfFacilitiesTextBlock

	def getAssetsForLeaseLEAHeading(self): #賃貸資産、リース事業 [目次項目]
		return self.AssetsForLeaseLEAHeading

	def getOverviewOfCapitalExpendituresEtcAssetsForLeaseLEAHeading(self): #設備投資等の概要、賃貸資産、リース事業 [目次項目]
		return self.OverviewOfCapitalExpendituresEtcAssetsForLeaseLEAHeading

	def getOverviewOfCapitalExpendituresEtcAssetsForLeaseLEATextBlock(self): #設備投資等の概要、賃貸資産、リース事業 [テキストブロック]
		return self.OverviewOfCapitalExpendituresEtcAssetsForLeaseLEATextBlock

	def getMajorFacilitiesAssetsForLeaseLEAHeading(self): #主要な設備の状況、賃貸資産、リース事業 [目次項目]
		return self.MajorFacilitiesAssetsForLeaseLEAHeading

	def getMajorFacilitiesAssetsForLeaseLEATextBlock(self): #主要な設備の状況、賃貸資産、リース事業 [テキストブロック]
		return self.MajorFacilitiesAssetsForLeaseLEATextBlock

	def getPlannedAdditionsRetirementsEtcOfFacilitiesAssetsForLeaseLEAHeading(self): #設備の新設、除却等の計画、賃貸資産、リース事業 [目次項目]
		return self.PlannedAdditionsRetirementsEtcOfFacilitiesAssetsForLeaseLEAHeading

	def getPlannedAdditionsRetirementsEtcOfFacilitiesAssetsForLeaseLEATextBlock(self): #設備の新設、除却等の計画、賃貸資産、リース事業 [テキストブロック]
		return self.PlannedAdditionsRetirementsEtcOfFacilitiesAssetsForLeaseLEATextBlock

	def getOwnUsedAssetsLEAHeading(self): #自社用資産、リース事業 [目次項目]
		return self.OwnUsedAssetsLEAHeading

	def getOverviewOfCapitalExpendituresEtcOwnUsedAssetsLEAHeading(self): #設備投資等の概要、自社用資産、リース事業 [目次項目]
		return self.OverviewOfCapitalExpendituresEtcOwnUsedAssetsLEAHeading

	def getOverviewOfCapitalExpendituresEtcOwnUsedAssetsLEATextBlock(self): #設備投資等の概要、自社用資産、リース事業 [テキストブロック]
		return self.OverviewOfCapitalExpendituresEtcOwnUsedAssetsLEATextBlock

	def getMajorFacilitiesOwnUsedAssetsLEAHeading(self): #主要な設備の状況、自社用資産、リース事業 [目次項目]
		return self.MajorFacilitiesOwnUsedAssetsLEAHeading

	def getMajorFacilitiesOwnUsedAssetsLEATextBlock(self): #主要な設備の状況、自社用資産、リース事業 [テキストブロック]
		return self.MajorFacilitiesOwnUsedAssetsLEATextBlock

	def getPlannedAdditionsRetirementsEtcOfFacilitiesOwnUsedAssetsLEAHeading(self): #設備の新設、除却等の計画、自社用資産、リース事業 [目次項目]
		return self.PlannedAdditionsRetirementsEtcOfFacilitiesOwnUsedAssetsLEAHeading

	def getPlannedAdditionsRetirementsEtcOfFacilitiesOwnUsedAssetsLEATextBlock(self): #設備の新設、除却等の計画、自社用資産、リース事業 [テキストブロック]
		return self.PlannedAdditionsRetirementsEtcOfFacilitiesOwnUsedAssetsLEATextBlock

	def getInformationAboutReportingCompanyHeading(self): #提出会社の状況 [目次項目]
		return self.InformationAboutReportingCompanyHeading

	def getInformationAboutSharesEtcHeading(self): #株式等の状況 [目次項目]
		return self.InformationAboutSharesEtcHeading

	def getTotalNumberOfSharesEtcHeading(self): #株式の総数等 [目次項目]
		return self.TotalNumberOfSharesEtcHeading

	def getTotalNumberOfSharesHeading(self): #株式の総数 [目次項目]
		return self.TotalNumberOfSharesHeading

	def getTotalNumberOfSharesTextBlock(self): #株式の総数 [テキストブロック]
		return self.TotalNumberOfSharesTextBlock

	def getIssuedSharesTotalNumberOfSharesEtcHeading(self): #発行済株式、株式の総数等 [目次項目]
		return self.IssuedSharesTotalNumberOfSharesEtcHeading

	def getIssuedSharesTotalNumberOfSharesEtcTextBlock(self): #発行済株式、株式の総数等 [テキストブロック]
		return self.IssuedSharesTotalNumberOfSharesEtcTextBlock

	def getIssuedSharesTotalNumberOfSharesEtcHeading(self): #発行済株式、株式の総数等 [目次項目]
		return self.IssuedSharesTotalNumberOfSharesEtcHeading

	def getIssuedSharesTotalNumberOfSharesEtcTable(self): #発行済株式、株式の総数等 [表]
		return self.IssuedSharesTotalNumberOfSharesEtcTable

	def getClassesOfSharesAxis(self): #株式種類 [軸]
		return self.ClassesOfSharesAxis

	def getTotalClassesOfSharesMember(self): #合計、株式種類 [メンバー] ※ディメンションデフォルト
		return self.TotalClassesOfSharesMember

	def getOrdinaryShareMember(self): #普通株式 [メンバー]
		return self.OrdinaryShareMember

	def getClassAPreferredSharesMember(self): #Ａ種優先株式 [メンバー]
		return self.ClassAPreferredSharesMember

	def getClassBPreferredSharesMember(self): #Ｂ種優先株式 [メンバー]
		return self.ClassBPreferredSharesMember

	def getClassOnePreferredSharesMember(self): #第一種優先株式 [メンバー]
		return self.ClassOnePreferredSharesMember

	def getClassTwoPreferredSharesMember(self): #第二種優先株式 [メンバー]
		return self.ClassTwoPreferredSharesMember

	def getClassASharesMember(self): #Ａ種種類株式 [メンバー]
		return self.ClassASharesMember

	def getIssuedSharesTotalNumberOfSharesEtcLineItems(self): #発行済株式、株式の総数等 [表示項目]
		return self.IssuedSharesTotalNumberOfSharesEtcLineItems

	def getClassIssuedSharesTotalNumberOfSharesEtc(self): #種類、発行済株式、株式の総数等
		return self.ClassIssuedSharesTotalNumberOfSharesEtc

	def getNumberOfIssuedSharesIssuedSharesTotalNumberOfSharesEtc(self): #発行数（株）、発行済株式、株式の総数等
		return self.NumberOfIssuedSharesIssuedSharesTotalNumberOfSharesEtc

	def getNumberOfIssuedSharesAsOfFiscalYearEndIssuedSharesTotalNumberOfSharesEtc(self): #事業年度末現在発行数（株）、発行済株式、株式の総数等
		return self.NumberOfIssuedSharesAsOfFiscalYearEndIssuedSharesTotalNumberOfSharesEtc

	def getNumberOfIssuedSharesAsOfFilingDateIssuedSharesTotalNumberOfSharesEtc(self): #提出日現在発行数（株）、発行済株式、株式の総数等
		return self.NumberOfIssuedSharesAsOfFilingDateIssuedSharesTotalNumberOfSharesEtc

	def getNameOfFinancialInstrumentsExchangeOnWhichSecuritiesAreListedOrAuthorizedFinancialInstrumentsBusinessAssociationToWhichSecuritiesAreRegistered(self): #上場金融商品取引所名又は登録認可金融商品取引業協会名
		return self.NameOfFinancialInstrumentsExchangeOnWhichSecuritiesAreListedOrAuthorizedFinancialInstrumentsBusinessAssociationToWhichSecuritiesAreRegistered

	def getDescriptionIssuedSharesTotalNumberOfSharesEtc(self): #内容、発行済株式、株式の総数等
		return self.DescriptionIssuedSharesTotalNumberOfSharesEtc

	def getSubscriptionRightsToSharesEtcHeading(self): #新株予約権等の状況 [目次項目]
		return self.SubscriptionRightsToSharesEtcHeading

	def getDetailsOfEmployeeShareOptionProgramHeading(self): #ストックオプション制度の内容 [目次項目]
		return self.DetailsOfEmployeeShareOptionProgramHeading

	def getDetailsOfEmployeeShareOptionProgramTextBlock(self): #ストックオプション制度の内容 [テキストブロック]
		return self.DetailsOfEmployeeShareOptionProgramTextBlock

	def getDescriptionOfRightsPlanHeading(self): #ライツプランの内容 [目次項目]
		return self.DescriptionOfRightsPlanHeading

	def getDescriptionOfRightsPlanTextBlock(self): #ライツプランの内容 [テキストブロック]
		return self.DescriptionOfRightsPlanTextBlock

	def getOtherInformationOnShareAcquisitionRightsHeading(self): #その他の新株予約権等の状況 [目次項目]
		return self.OtherInformationOnShareAcquisitionRightsHeading

	def getOtherInformationOnShareAcquisitionRightsTextBlock(self): #その他の新株予約権等の状況 [テキストブロック]
		return self.OtherInformationOnShareAcquisitionRightsTextBlock

	def getExercisesEtcOfMovingStrikeConvertibleBondsEtcHeading(self): #行使価額修正条項付新株予約権付社債券等の行使状況等 [目次項目]
		return self.ExercisesEtcOfMovingStrikeConvertibleBondsEtcHeading

	def getExercisesEtcOfMovingStrikeConvertibleBondsEtcTextBlock(self): #行使価額修正条項付新株予約権付社債券等の行使状況等 [テキストブロック]
		return self.ExercisesEtcOfMovingStrikeConvertibleBondsEtcTextBlock

	def getChangesInNumberOfIssuedSharesStatedCapitalEtcHeading(self): #発行済株式総数、資本金等の推移 [目次項目]
		return self.ChangesInNumberOfIssuedSharesStatedCapitalEtcHeading

	def getChangesInNumberOfIssuedSharesStatedCapitalEtcTextBlock(self): #発行済株式総数、資本金等の推移 [テキストブロック]
		return self.ChangesInNumberOfIssuedSharesStatedCapitalEtcTextBlock

	def getShareholdingByShareholderCategoryHeading(self): #所有者別状況 [目次項目]
		return self.ShareholdingByShareholderCategoryHeading

	def getShareholdingByShareholderCategoryTextBlock(self): #所有者別状況 [テキストブロック]
		return self.ShareholdingByShareholderCategoryTextBlock

	def getShareholdingByShareholderCategoryHeading(self): #所有者別状況 [目次項目]
		return self.ShareholdingByShareholderCategoryHeading

	def getShareholdingByShareholderCategoryTable(self): #所有者別状況 [表]
		return self.ShareholdingByShareholderCategoryTable

	def getClassesOfSharesAxis(self): #株式種類 [軸]
		return self.ClassesOfSharesAxis

	def getTotalClassesOfSharesMember(self): #合計、株式種類 [メンバー] ※ディメンションデフォルト
		return self.TotalClassesOfSharesMember

	def getOrdinaryShareMember(self): #普通株式 [メンバー]
		return self.OrdinaryShareMember

	def getClassAPreferredSharesMember(self): #Ａ種優先株式 [メンバー]
		return self.ClassAPreferredSharesMember

	def getClassBPreferredSharesMember(self): #Ｂ種優先株式 [メンバー]
		return self.ClassBPreferredSharesMember

	def getClassOnePreferredSharesMember(self): #第一種優先株式 [メンバー]
		return self.ClassOnePreferredSharesMember

	def getClassTwoPreferredSharesMember(self): #第二種優先株式 [メンバー]
		return self.ClassTwoPreferredSharesMember

	def getClassASharesMember(self): #Ａ種種類株式 [メンバー]
		return self.ClassASharesMember

	def getShareholdingByShareholderCategoryLineItems(self): #所有者別状況 [表示項目]
		return self.ShareholdingByShareholderCategoryLineItems

	def getNumberOfSharesConstitutingOneUnit(self): #１単元の株式数
		return self.NumberOfSharesConstitutingOneUnit

	def getNumberOfShareholdersNationalAndLocalGovernments(self): #株主数－政府及び地方公共団体
		return self.NumberOfShareholdersNationalAndLocalGovernments

	def getNumberOfShareholdersFinancialInstitutions(self): #株主数－金融機関
		return self.NumberOfShareholdersFinancialInstitutions

	def getNumberOfShareholdersFinancialServiceProviders(self): #株主数－金融商品取引業者
		return self.NumberOfShareholdersFinancialServiceProviders

	def getNumberOfShareholdersOtherCorporations(self): #株主数－その他の法人
		return self.NumberOfShareholdersOtherCorporations

	def getNumberOfShareholdersForeignInvestorsOtherThanIndividuals(self): #株主数－外国法人等－個人以外
		return self.NumberOfShareholdersForeignInvestorsOtherThanIndividuals

	def getNumberOfShareholdersForeignIndividualInvestors(self): #株主数－外国法人等－個人
		return self.NumberOfShareholdersForeignIndividualInvestors

	def getNumberOfShareholdersIndividualsAndOthers(self): #株主数－個人その他
		return self.NumberOfShareholdersIndividualsAndOthers

	def getNumberOfShareholdersTotal(self): #株主数－計
		return self.NumberOfShareholdersTotal

	def getNumberOfSharesHeldNumberOfUnitsNationalAndLocalGovernments(self): #所有株式数（単元）－政府及び地方公共団体
		return self.NumberOfSharesHeldNumberOfUnitsNationalAndLocalGovernments

	def getNumberOfSharesHeldNumberOfUnitsFinancialInstitutions(self): #所有株式数（単元）－金融機関
		return self.NumberOfSharesHeldNumberOfUnitsFinancialInstitutions

	def getNumberOfSharesHeldNumberOfUnitsFinancialServiceProviders(self): #所有株式数（単元）－金融商品取引業者
		return self.NumberOfSharesHeldNumberOfUnitsFinancialServiceProviders

	def getNumberOfSharesHeldNumberOfUnitsOtherCorporations(self): #所有株式数（単元）－その他の法人
		return self.NumberOfSharesHeldNumberOfUnitsOtherCorporations

	def getNumberOfSharesHeldNumberOfUnitsForeignInvestorsOtherThanIndividuals(self): #所有株式数（単元）－外国法人等－個人以外
		return self.NumberOfSharesHeldNumberOfUnitsForeignInvestorsOtherThanIndividuals

	def getNumberOfSharesHeldNumberOfUnitsForeignIndividualInvestors(self): #所有株式数（単元）－外国法人等－個人
		return self.NumberOfSharesHeldNumberOfUnitsForeignIndividualInvestors

	def getNumberOfSharesHeldNumberOfUnitsIndividualsAndOthers(self): #所有株式数（単元）－個人その他
		return self.NumberOfSharesHeldNumberOfUnitsIndividualsAndOthers

	def getNumberOfSharesHeldNumberOfUnitsTotal(self): #所有株式数（単元）－計
		return self.NumberOfSharesHeldNumberOfUnitsTotal

	def getNumberOfSharesHeldSharesLessThanOneUnit(self): #所有株式数－単元未満株式の状況（株）
		return self.NumberOfSharesHeldSharesLessThanOneUnit

	def getPercentageOfShareholdingsNationalAndLocalGovernments(self): #所有株式数の割合（％）－政府及び地方公共団体
		return self.PercentageOfShareholdingsNationalAndLocalGovernments

	def getPercentageOfShareholdingsFinancialInstitutions(self): #所有株式数の割合（％）－金融機関
		return self.PercentageOfShareholdingsFinancialInstitutions

	def getPercentageOfShareholdingsFinancialServiceProviders(self): #所有株式数の割合（％）－金融商品取引業者
		return self.PercentageOfShareholdingsFinancialServiceProviders

	def getPercentageOfShareholdingsOtherCorporations(self): #所有株式数の割合（％）－その他の法人
		return self.PercentageOfShareholdingsOtherCorporations

	def getPercentageOfShareholdingsForeignersOtherThanIndividuals(self): #所有株式数の割合（％）－外国法人等－個人以外
		return self.PercentageOfShareholdingsForeignersOtherThanIndividuals

	def getPercentageOfShareholdingsForeignIndividuals(self): #所有株式数の割合（％）－外国法人等－個人
		return self.PercentageOfShareholdingsForeignIndividuals

	def getPercentageOfShareholdingsIndividualsAndOthers(self): #所有株式数の割合（％）－個人その他
		return self.PercentageOfShareholdingsIndividualsAndOthers

	def getMajorShareholdersHeading(self): #大株主の状況 [目次項目]
		return self.MajorShareholdersHeading

	def getMajorShareholdersTextBlock(self): #大株主の状況 [テキストブロック]
		return self.MajorShareholdersTextBlock

	def getMajorShareholdersHeading(self): #大株主の状況 [目次項目]
		return self.MajorShareholdersHeading

	def getMajorShareholdersTable(self): #大株主の状況 [表]
		return self.MajorShareholdersTable

	def getMajorShareholdersAxis(self): #大株主 [軸]
		return self.MajorShareholdersAxis

	def getMajorShareholdersMember(self): #大株主 [メンバー] ※ディメンションデフォルト
		return self.MajorShareholdersMember

	def getNo1MajorShareholdersMember(self): #第1位、大株主 [メンバー]
		return self.No1MajorShareholdersMember

	def getNo2MajorShareholdersMember(self): #第2位、大株主 [メンバー]
		return self.No2MajorShareholdersMember

	def getNo3MajorShareholdersMember(self): #第3位、大株主 [メンバー]
		return self.No3MajorShareholdersMember

	def getNo4MajorShareholdersMember(self): #第4位、大株主 [メンバー]
		return self.No4MajorShareholdersMember

	def getNo5MajorShareholdersMember(self): #第5位、大株主 [メンバー]
		return self.No5MajorShareholdersMember

	def getNo6MajorShareholdersMember(self): #第6位、大株主 [メンバー]
		return self.No6MajorShareholdersMember

	def getNo7MajorShareholdersMember(self): #第7位、大株主 [メンバー]
		return self.No7MajorShareholdersMember

	def getNo8MajorShareholdersMember(self): #第8位、大株主 [メンバー]
		return self.No8MajorShareholdersMember

	def getNo9MajorShareholdersMember(self): #第9位、大株主 [メンバー]
		return self.No9MajorShareholdersMember

	def getNo10MajorShareholdersMember(self): #第10位、大株主 [メンバー]
		return self.No10MajorShareholdersMember

	def getNo11MajorShareholdersMember(self): #第11位、大株主 [メンバー]
		return self.No11MajorShareholdersMember

	def getNo12MajorShareholdersMember(self): #第12位、大株主 [メンバー]
		return self.No12MajorShareholdersMember

	def getNo13MajorShareholdersMember(self): #第13位、大株主 [メンバー]
		return self.No13MajorShareholdersMember

	def getNo14MajorShareholdersMember(self): #第14位、大株主 [メンバー]
		return self.No14MajorShareholdersMember

	def getNo15MajorShareholdersMember(self): #第15位、大株主 [メンバー]
		return self.No15MajorShareholdersMember

	def getMajorShareholdersLineItems(self): #大株主の状況 [表示項目]
		return self.MajorShareholdersLineItems

	def getNameMajorShareholders(self): #氏名又は名称、大株主の状況
		return self.NameMajorShareholders

	def getAddressMajorShareholders(self): #住所、大株主の状況
		return self.AddressMajorShareholders

	def getNumberOfSharesHeld(self): #所有株式数
		return self.NumberOfSharesHeld

	def getShareholdingRatio(self): #発行済株式（自己株式を除く。）の総数に対する所有株式数の割合
		return self.ShareholdingRatio

	def getMajorShareholdersHeading(self): #大株主の状況 [目次項目]
		return self.MajorShareholdersHeading

	def getMajorShareholdersVotingRightsTable(self): #所有株式に係る議決権上位者の状況 [表]
		return self.MajorShareholdersVotingRightsTable

	def getMajorShareholdersVotingRightsAxis(self): #議決権上位 [軸]
		return self.MajorShareholdersVotingRightsAxis

	def getMajorShareholdersVotingRightsMember(self): #議決権上位 [メンバー] ※ディメンションデフォルト
		return self.MajorShareholdersVotingRightsMember

	def getNo1MajorShareholdersVotingRightsMember(self): #第1位、議決権上位 [メンバー]
		return self.No1MajorShareholdersVotingRightsMember

	def getNo2MajorShareholdersVotingRightsMember(self): #第2位、議決権上位 [メンバー]
		return self.No2MajorShareholdersVotingRightsMember

	def getNo3MajorShareholdersVotingRightsMember(self): #第3位、議決権上位 [メンバー]
		return self.No3MajorShareholdersVotingRightsMember

	def getNo4MajorShareholdersVotingRightsMember(self): #第4位、議決権上位 [メンバー]
		return self.No4MajorShareholdersVotingRightsMember

	def getNo5MajorShareholdersVotingRightsMember(self): #第5位、議決権上位 [メンバー]
		return self.No5MajorShareholdersVotingRightsMember

	def getNo6MajorShareholdersVotingRightsMember(self): #第6位、議決権上位 [メンバー]
		return self.No6MajorShareholdersVotingRightsMember

	def getNo7MajorShareholdersVotingRightsMember(self): #第7位、議決権上位 [メンバー]
		return self.No7MajorShareholdersVotingRightsMember

	def getNo8MajorShareholdersVotingRightsMember(self): #第8位、議決権上位 [メンバー]
		return self.No8MajorShareholdersVotingRightsMember

	def getNo9MajorShareholdersVotingRightsMember(self): #第9位、議決権上位 [メンバー]
		return self.No9MajorShareholdersVotingRightsMember

	def getNo10MajorShareholdersVotingRightsMember(self): #第10位、議決権上位 [メンバー]
		return self.No10MajorShareholdersVotingRightsMember

	def getNo11MajorShareholdersVotingRightsMember(self): #第11位、議決権上位 [メンバー]
		return self.No11MajorShareholdersVotingRightsMember

	def getNo12MajorShareholdersVotingRightsMember(self): #第12位、議決権上位 [メンバー]
		return self.No12MajorShareholdersVotingRightsMember

	def getNo13MajorShareholdersVotingRightsMember(self): #第13位、議決権上位 [メンバー]
		return self.No13MajorShareholdersVotingRightsMember

	def getNo14MajorShareholdersVotingRightsMember(self): #第14位、議決権上位 [メンバー]
		return self.No14MajorShareholdersVotingRightsMember

	def getNo15MajorShareholdersVotingRightsMember(self): #第15位、議決権上位 [メンバー]
		return self.No15MajorShareholdersVotingRightsMember

	def getMajorShareholdersVotingRightsLineItems(self): #所有株式に係る議決権上位者の状況 [表示項目]
		return self.MajorShareholdersVotingRightsLineItems

	def getNameMajorShareholdersVotingRights(self): #氏名又は名称、所有株式に係る議決権上位者の状況
		return self.NameMajorShareholdersVotingRights

	def getAddressMajorShareholdersVotingRights(self): #住所、所有株式に係る議決権上位者の状況
		return self.AddressMajorShareholdersVotingRights

	def getNumberOfVotingRightsHeld(self): #所有議決権数（個）
		return self.NumberOfVotingRightsHeld

	def getRatioOfVotingRightsHeld(self): #総株主の議決権に対する所有議決権数の割合
		return self.RatioOfVotingRightsHeld

	def getVotingRightsHeading(self): #議決権の状況 [目次項目]
		return self.VotingRightsHeading

	def getVotingRightsTextBlock(self): #議決権の状況 [テキストブロック]
		return self.VotingRightsTextBlock

	def getIssuedSharesVotingRightsHeading(self): #発行済株式、議決権の状況 [目次項目]
		return self.IssuedSharesVotingRightsHeading

	def getIssuedSharesVotingRightsTextBlock(self): #発行済株式、議決権の状況 [テキストブロック]
		return self.IssuedSharesVotingRightsTextBlock

	def getIssuedSharesVotingRightsHeading(self): #発行済株式、議決権の状況 [目次項目]
		return self.IssuedSharesVotingRightsHeading

	def getIssuedSharesVotingRightsTable(self): #発行済株式、議決権の状況 [表]
		return self.IssuedSharesVotingRightsTable

	def getCategoriesIssuedSharesAxis(self): #区分、発行済株式 [軸]
		return self.CategoriesIssuedSharesAxis

	def getTotalNumberOfIssuedSharesNumberOfVotingRightsHeldByAllShareholdersMember(self): #発行済株式総数／総株主の議決権 [メンバー] ※ディメンションデフォルト
		return self.TotalNumberOfIssuedSharesNumberOfVotingRightsHeldByAllShareholdersMember

	def getSharesWithNoVotingRightsMember(self): #無議決権株式 [メンバー]
		return self.SharesWithNoVotingRightsMember

	def getSharesWithRestrictedVotingRightsTreasurySharesEtcMember(self): #議決権制限株式（自己株式等） [メンバー]
		return self.SharesWithRestrictedVotingRightsTreasurySharesEtcMember

	def getSharesWithRestrictedVotingRightsOtherMember(self): #議決権制限株式（その他） [メンバー]
		return self.SharesWithRestrictedVotingRightsOtherMember

	def getSharesWithFullVotingRightsTreasurySharesEtcMember(self): #完全議決権株式（自己株式等） [メンバー]
		return self.SharesWithFullVotingRightsTreasurySharesEtcMember

	def getOrdinarySharesSharesWithFullVotingRightsTreasurySharesEtcMember(self): #普通株式、完全議決権株式（自己株式等） [メンバー]
		return self.OrdinarySharesSharesWithFullVotingRightsTreasurySharesEtcMember

	def getOrdinarySharesTreasurySharesSharesWithFullVotingRightsTreasurySharesEtcMember(self): #（自己保有株式）普通株式、完全議決権株式（自己株式等） [メンバー]
		return self.OrdinarySharesTreasurySharesSharesWithFullVotingRightsTreasurySharesEtcMember

	def getOrdinarySharesReciprocalHoldingSharesWithFullVotingRightsTreasurySharesEtcMember(self): #（相互保有株式）普通株式、完全議決権株式（自己株式等） [メンバー]
		return self.OrdinarySharesReciprocalHoldingSharesWithFullVotingRightsTreasurySharesEtcMember

	def getSharesWithFullVotingRightsOtherMember(self): #完全議決権株式（その他） [メンバー]
		return self.SharesWithFullVotingRightsOtherMember

	def getOrdinarySharesSharesWithFullVotingRightsOtherMember(self): #普通株式、完全議決権株式（その他） [メンバー]
		return self.OrdinarySharesSharesWithFullVotingRightsOtherMember

	def getSharesLessThanOneUnitMember(self): #単元未満株式 [メンバー]
		return self.SharesLessThanOneUnitMember

	def getOrdinarySharesSharesLessThanOneUnitMember(self): #普通株式、単元未満株式 [メンバー]
		return self.OrdinarySharesSharesLessThanOneUnitMember

	def getIssuedSharesVotingRightsLineItems(self): #発行済株式、議決権の状況 [表示項目]
		return self.IssuedSharesVotingRightsLineItems

	def getNumberOfSharesIssuedSharesVotingRights(self): #株式数（株）、発行済株式、議決権の状況
		return self.NumberOfSharesIssuedSharesVotingRights

	def getNumberOfVotingRightsIssuedSharesVotingRights(self): #議決権の数（個）、発行済株式、議決権の状況
		return self.NumberOfVotingRightsIssuedSharesVotingRights

	def getDescriptionIssuedSharesVotingRights(self): #内容、発行済株式、議決権の状況
		return self.DescriptionIssuedSharesVotingRights

	def getTreasurySharesEtcHeading(self): #自己株式等 [目次項目]
		return self.TreasurySharesEtcHeading

	def getTreasurySharesEtcTextBlock(self): #自己株式等 [テキストブロック]
		return self.TreasurySharesEtcTextBlock

	def getTreasurySharesEtcHeading(self): #自己株式等 [目次項目]
		return self.TreasurySharesEtcHeading

	def getTreasurySharesEtcTable(self): #自己株式等 [表]
		return self.TreasurySharesEtcTable

	def getSequentialNumbersAxis(self): #連番 [軸]
		return self.SequentialNumbersAxis

	def getTotalSequentialNumbersMember(self): #合計、連番 [メンバー] ※ディメンションデフォルト
		return self.TotalSequentialNumbersMember

	def getRow1Member(self): #1件目 [メンバー]
		return self.Row1Member

	def getRow2Member(self): #2件目 [メンバー]
		return self.Row2Member

	def getRow3Member(self): #3件目 [メンバー]
		return self.Row3Member

	def getRow4Member(self): #4件目 [メンバー]
		return self.Row4Member

	def getTreasurySharesEtcLineItems(self): #自己株式等 [表示項目]
		return self.TreasurySharesEtcLineItems

	def getNameOfShareholderTreasurySharesEtc(self): #所有者の氏名又は名称、自己株式等
		return self.NameOfShareholderTreasurySharesEtc

	def getAddressOfShareholderTreasurySharesEtc(self): #所有者の住所、自己株式等
		return self.AddressOfShareholderTreasurySharesEtc

	def getNumberOfSharesHeldInOwnNameTreasurySharesEtc(self): #自己名義所有株式数（株）、自己株式等
		return self.NumberOfSharesHeldInOwnNameTreasurySharesEtc

	def getNumberOfSharesHeldInOthersNamesTreasurySharesEtc(self): #他人名義所有株式数（株）、自己株式等
		return self.NumberOfSharesHeldInOthersNamesTreasurySharesEtc

	def getTotalNumberOfSharesHeldTreasurySharesEtc(self): #所有株式数の合計（株）、自己株式等
		return self.TotalNumberOfSharesHeldTreasurySharesEtc

	def getShareholdingRatioTreasurySharesEtc(self): #発行済株式総数に対する所有株式数の割合（％）、自己株式等
		return self.ShareholdingRatioTreasurySharesEtc

	def getDetailsOfTransfersOfSharesEtcByAcquirerHeading(self): #取得者の株式等の移動状況 [目次項目]
		return self.DetailsOfTransfersOfSharesEtcByAcquirerHeading

	def getDetailsOfTransfersOfSharesEtcByAcquirerTextBlock(self): #取得者の株式等の移動状況 [テキストブロック]
		return self.DetailsOfTransfersOfSharesEtcByAcquirerTextBlock

	def getShareOwnershipPlansForDirectorsAndOtherOfficersAndEmployeesHeading(self): #役員・従業員株式所有制度の内容 [目次項目]
		return self.ShareOwnershipPlansForDirectorsAndOtherOfficersAndEmployeesHeading

	def getShareOwnershipPlansForDirectorsAndOtherOfficersAndEmployeesTextBlock(self): #役員・従業員株式所有制度の内容 [テキストブロック]
		return self.ShareOwnershipPlansForDirectorsAndOtherOfficersAndEmployeesTextBlock

	def getAcquisitionsEtcOfTreasurySharesHeading(self): #自己株式の取得等の状況 [目次項目]
		return self.AcquisitionsEtcOfTreasurySharesHeading

	def getAcquisitionsEtcOfTreasurySharesTextBlock(self): #自己株式の取得等の状況 [テキストブロック]
		return self.AcquisitionsEtcOfTreasurySharesTextBlock

	def getClassesOfSharesEtcHeading(self): #株式の種類等 [目次項目]
		return self.ClassesOfSharesEtcHeading

	def getClassesOfSharesEtcTextBlock(self): #株式の種類等 [テキストブロック]
		return self.ClassesOfSharesEtcTextBlock

	def getAcquisitionsByResolutionOfShareholdersMeetingHeading(self): #株主総会決議による取得の状況 [目次項目]
		return self.AcquisitionsByResolutionOfShareholdersMeetingHeading

	def getAcquisitionsByResolutionOfShareholdersMeetingTextBlock(self): #株主総会決議による取得の状況 [テキストブロック]
		return self.AcquisitionsByResolutionOfShareholdersMeetingTextBlock

	def getAcquisitionsByResolutionOfBoardOfDirectorsMeetingHeading(self): #取締役会決議による取得の状況 [目次項目]
		return self.AcquisitionsByResolutionOfBoardOfDirectorsMeetingHeading

	def getAcquisitionsByResolutionOfBoardOfDirectorsMeetingTextBlock(self): #取締役会決議による取得の状況 [テキストブロック]
		return self.AcquisitionsByResolutionOfBoardOfDirectorsMeetingTextBlock

	def getAcquisitionsNotBasedOnResolutionOfShareholdersMeetingOrBoardOfDirectorsMeetingHeading(self): #株主総会決議又は取締役会決議に基づかないものの内容 [目次項目]
		return self.AcquisitionsNotBasedOnResolutionOfShareholdersMeetingOrBoardOfDirectorsMeetingHeading

	def getAcquisitionsNotBasedOnResolutionOfShareholdersMeetingOrBoardOfDirectorsMeetingTextBlock(self): #株主総会決議又は取締役会決議に基づかないものの内容 [テキストブロック]
		return self.AcquisitionsNotBasedOnResolutionOfShareholdersMeetingOrBoardOfDirectorsMeetingTextBlock

	def getDisposalsOrHoldingOfAcquiredTreasurySharesHeading(self): #取得自己株式の処理状況及び保有状況 [目次項目]
		return self.DisposalsOrHoldingOfAcquiredTreasurySharesHeading

	def getDisposalsOrHoldingOfAcquiredTreasurySharesTextBlock(self): #取得自己株式の処理状況及び保有状況 [テキストブロック]
		return self.DisposalsOrHoldingOfAcquiredTreasurySharesTextBlock

	def getDividendPolicyHeading(self): #配当政策 [目次項目]
		return self.DividendPolicyHeading

	def getDividendPolicyTextBlock(self): #配当政策 [テキストブロック]
		return self.DividendPolicyTextBlock

	def getDividendPolicyHeading(self): #配当政策 [目次項目]
		return self.DividendPolicyHeading

	def getDividendsOfSurplusTable(self): #剰余金の配当 [表]
		return self.DividendsOfSurplusTable

	def getSequentialNumbersAxis(self): #連番 [軸]
		return self.SequentialNumbersAxis

	def getRow1Member(self): #1件目 [メンバー]
		return self.Row1Member

	def getRow2Member(self): #2件目 [メンバー]
		return self.Row2Member

	def getRow3Member(self): #3件目 [メンバー]
		return self.Row3Member

	def getRow4Member(self): #4件目 [メンバー]
		return self.Row4Member

	def getDividendsOfSurplusLineItems(self): #剰余金の配当 [表示項目]
		return self.DividendsOfSurplusLineItems

	def getDateOfResolutionDividendsOfSurplus(self): #決議日付、剰余金の配当
		return self.DateOfResolutionDividendsOfSurplus

	def getResolutionDividendsOfSurplus(self): #決議、剰余金の配当
		return self.ResolutionDividendsOfSurplus

	def getRecordDateDividendsOfSurplus(self): #基準日、剰余金の配当
		return self.RecordDateDividendsOfSurplus

	def getTotalAmountOfDividendsDividendsOfSurplus(self): #配当金の総額、剰余金の配当
		return self.TotalAmountOfDividendsDividendsOfSurplus

	def getDividendPerShareDividendsOfSurplus(self): #１株当たり配当額、剰余金の配当
		return self.DividendPerShareDividendsOfSurplus

	def getExplanationAboutCorporateGovernanceEtcHeading(self): #コーポレート・ガバナンスの状況等 [目次項目]
		return self.ExplanationAboutCorporateGovernanceEtcHeading

	def getOverviewOfCorporateGovernanceHeading(self): #コーポレート・ガバナンスの概要 [目次項目]
		return self.OverviewOfCorporateGovernanceHeading

	def getOverviewOfCorporateGovernanceTextBlock(self): #コーポレート・ガバナンスの概要 [テキストブロック]
		return self.OverviewOfCorporateGovernanceTextBlock

	def getDescriptionOfFactThatCorporateGovernanceSystemChoiceFromThreeCategoriesWasChangedTextBlock(self): #企業統治の組織形態（３分類）の変更 [テキストブロック]
		return self.DescriptionOfFactThatCorporateGovernanceSystemChoiceFromThreeCategoriesWasChangedTextBlock

	def getCorporateGovernanceCompanyWithCorporateAuditorsTextBlock(self): #企業統治の体制の概要（監査役設置会社） [テキストブロック]
		return self.CorporateGovernanceCompanyWithCorporateAuditorsTextBlock

	def getCorporateGovernanceCompanyWithAuditAndSupervisoryCommitteeTextBlock(self): #企業統治の体制の概要（監査等委員会設置会社） [テキストブロック]
		return self.CorporateGovernanceCompanyWithAuditAndSupervisoryCommitteeTextBlock

	def getCorporateGovernanceCompanyWithNominatingAndOtherCommitteesTextBlock(self): #企業統治の体制の概要（指名委員会等設置会社） [テキストブロック]
		return self.CorporateGovernanceCompanyWithNominatingAndOtherCommitteesTextBlock

	def getBasicPolicyRegardingControlOfCompanyTextBlock(self): #会社の支配に関する基本方針 [テキストブロック]
		return self.BasicPolicyRegardingControlOfCompanyTextBlock

	def getInformationAboutOfficersHeading(self): #役員の状況 [目次項目]
		return self.InformationAboutOfficersHeading

	def getInformationAboutOfficersTextBlock(self): #役員の状況 [テキストブロック]
		return self.InformationAboutOfficersTextBlock

	def getInformationAboutOfficersHeading(self): #役員の状況 [目次項目]
		return self.InformationAboutOfficersHeading

	def getNumberOfMaleDirectorsAndOtherOfficers(self): #役員のうち男性の人数
		return self.NumberOfMaleDirectorsAndOtherOfficers

	def getNumberOfFemaleDirectorsAndOtherOfficers(self): #役員のうち女性の人数
		return self.NumberOfFemaleDirectorsAndOtherOfficers

	def getRatioOfFemaleDirectorsAndOtherOfficers(self): #役員のうち女性の比率
		return self.RatioOfFemaleDirectorsAndOtherOfficers

	def getInformationAboutOfficersHeading(self): #役員の状況 [目次項目]
		return self.InformationAboutOfficersHeading

	def getInformationAboutDirectorsAndCorporateAuditorsTable(self): #役員の状況（取締役（及び監査役）） [表]
		return self.InformationAboutDirectorsAndCorporateAuditorsTable

	def getDirectorsAndOtherOfficersAxis(self): #役員 [軸]
		return self.DirectorsAndOtherOfficersAxis

	def getDirectorsAndOtherOfficersMember(self): #役員 [メンバー] ※ディメンションデフォルト
		return self.DirectorsAndOtherOfficersMember

	def getInformationAboutDirectorsAndCorporateAuditorsLineItems(self): #役員の状況（取締役（及び監査役）） [表示項目]
		return self.InformationAboutDirectorsAndCorporateAuditorsLineItems

	def getOfficialTitleOrPositionInformationAboutDirectorsAndCorporateAuditors(self): #役職名、役員の状況（取締役（及び監査役））
		return self.OfficialTitleOrPositionInformationAboutDirectorsAndCorporateAuditors

	def getNameInformationAboutDirectorsAndCorporateAuditors(self): #氏名、役員の状況（取締役（及び監査役））
		return self.NameInformationAboutDirectorsAndCorporateAuditors

	def getDateOfBirthInformationAboutDirectorsAndCorporateAuditors(self): #生年月日、役員の状況（取締役（及び監査役））
		return self.DateOfBirthInformationAboutDirectorsAndCorporateAuditors

	def getCareerSummaryInformationAboutDirectorsAndCorporateAuditorsTextBlock(self): #略歴、役員の状況（取締役（及び監査役）） [テキストブロック]
		return self.CareerSummaryInformationAboutDirectorsAndCorporateAuditorsTextBlock

	def getTermOfOfficeInformationAboutDirectorsAndCorporateAuditors(self): #任期、役員の状況（取締役（及び監査役））
		return self.TermOfOfficeInformationAboutDirectorsAndCorporateAuditors

	def getNumberOfSharesHeldOrdinarySharesInformationAboutDirectorsAndCorporateAuditors(self): #所有株式数（普通株式）、役員の状況（取締役（及び監査役））
		return self.NumberOfSharesHeldOrdinarySharesInformationAboutDirectorsAndCorporateAuditors

	def getNumberOfSharesHeldOtherThanOrdinarySharesInformationAboutDirectorsAndCorporateAuditors(self): #所有株式数（普通株式以外）、役員の状況（取締役（及び監査役））
		return self.NumberOfSharesHeldOtherThanOrdinarySharesInformationAboutDirectorsAndCorporateAuditors

	def getInformationAboutOfficersHeading(self): #役員の状況 [目次項目]
		return self.InformationAboutOfficersHeading

	def getFootnotesDirectorsAndCorporateAuditorsTable(self): #脚注（取締役（及び監査役）） [表]
		return self.FootnotesDirectorsAndCorporateAuditorsTable

	def getSequentialNumbersAxis(self): #連番 [軸]
		return self.SequentialNumbersAxis

	def getRow1Member(self): #1件目 [メンバー]
		return self.Row1Member

	def getRow2Member(self): #2件目 [メンバー]
		return self.Row2Member

	def getRow3Member(self): #3件目 [メンバー]
		return self.Row3Member

	def getRow4Member(self): #4件目 [メンバー]
		return self.Row4Member

	def getRow5Member(self): #5件目 [メンバー]
		return self.Row5Member

	def getFootnotesDirectorsAndCorporateAuditorsLineItems(self): #脚注（取締役（及び監査役）） [表示項目]
		return self.FootnotesDirectorsAndCorporateAuditorsLineItems

	def getFootnotesDirectorsAndCorporateAuditorsTextBlock(self): #脚注（取締役（及び監査役） [テキストブロック]
		return self.FootnotesDirectorsAndCorporateAuditorsTextBlock

	def getInformationAboutOfficersHeading(self): #役員の状況 [目次項目]
		return self.InformationAboutOfficersHeading

	def getInformationAboutExecutiveDirectorsTable(self): #役員の状況（執行役） [表]
		return self.InformationAboutExecutiveDirectorsTable

	def getDirectorsAndOtherOfficersAxis(self): #役員 [軸]
		return self.DirectorsAndOtherOfficersAxis

	def getDirectorsAndOtherOfficersMember(self): #役員 [メンバー] ※ディメンションデフォルト
		return self.DirectorsAndOtherOfficersMember

	def getInformationAboutExecutiveDirectorsLineItems(self): #役員の状況（執行役） [表示項目]
		return self.InformationAboutExecutiveDirectorsLineItems

	def getOfficialTitleOrPositionInformationAboutExecutiveDirectors(self): #役職名、役員の状況（執行役）
		return self.OfficialTitleOrPositionInformationAboutExecutiveDirectors

	def getNameInformationAboutExecutiveDirectors(self): #氏名、役員の状況（執行役）
		return self.NameInformationAboutExecutiveDirectors

	def getDateOfBirthInformationAboutExecutiveDirectors(self): #生年月日、役員の状況（執行役）
		return self.DateOfBirthInformationAboutExecutiveDirectors

	def getCareerSummaryInformationAboutExecutiveDirectorsTextBlock(self): #略歴、役員の状況（執行役） [テキストブロック]
		return self.CareerSummaryInformationAboutExecutiveDirectorsTextBlock

	def getTermOfOfficeInformationAboutExecutiveDirectors(self): #任期、役員の状況（執行役）
		return self.TermOfOfficeInformationAboutExecutiveDirectors

	def getNumberOfSharesHeldOrdinarySharesInformationAboutExecutiveDirectors(self): #所有株式数（普通株式）、役員の状況（執行役）
		return self.NumberOfSharesHeldOrdinarySharesInformationAboutExecutiveDirectors

	def getNumberOfSharesHeldOtherThanOrdinarySharesInformationAboutExecutiveDirectors(self): #所有株式数（普通株式以外）、役員の状況（執行役）
		return self.NumberOfSharesHeldOtherThanOrdinarySharesInformationAboutExecutiveDirectors

	def getInformationAboutOfficersHeading(self): #役員の状況 [目次項目]
		return self.InformationAboutOfficersHeading

	def getFootnotesExecutiveOfficersTable(self): #脚注（執行役） [表]
		return self.FootnotesExecutiveOfficersTable

	def getSequentialNumbersAxis(self): #連番 [軸]
		return self.SequentialNumbersAxis

	def getRow1Member(self): #1件目 [メンバー]
		return self.Row1Member

	def getRow2Member(self): #2件目 [メンバー]
		return self.Row2Member

	def getRow3Member(self): #3件目 [メンバー]
		return self.Row3Member

	def getRow4Member(self): #4件目 [メンバー]
		return self.Row4Member

	def getRow5Member(self): #5件目 [メンバー]
		return self.Row5Member

	def getFootnotesExecutiveOfficersLineItems(self): #脚注（執行役） [表示項目]
		return self.FootnotesExecutiveOfficersLineItems

	def getFootnotesExecutiveOfficersTextBlock(self): #脚注（執行役） [テキストブロック]
		return self.FootnotesExecutiveOfficersTextBlock

	def getInformationAboutOfficersHeading(self): #役員の状況 [目次項目]
		return self.InformationAboutOfficersHeading

	def getNumberOfMaleDirectorsAndOtherOfficersProposal(self): #役員のうち男性の人数（議案）
		return self.NumberOfMaleDirectorsAndOtherOfficersProposal

	def getNumberOfFemaleDirectorsAndOtherOfficersProposal(self): #役員のうち女性の人数（議案）
		return self.NumberOfFemaleDirectorsAndOtherOfficersProposal

	def getRatioOfFemaleDirectorsAndOtherOfficersProposal(self): #役員のうち女性の比率（議案）
		return self.RatioOfFemaleDirectorsAndOtherOfficersProposal

	def getInformationAboutOfficersHeading(self): #役員の状況 [目次項目]
		return self.InformationAboutOfficersHeading

	def getInformationAboutDirectorsAndCorporateAuditorsProposalTable(self): #役員の状況（取締役（及び監査役））（議案） [表]
		return self.InformationAboutDirectorsAndCorporateAuditorsProposalTable

	def getDirectorsAndOtherOfficersAxis(self): #役員 [軸]
		return self.DirectorsAndOtherOfficersAxis

	def getDirectorsAndOtherOfficersMember(self): #役員 [メンバー] ※ディメンションデフォルト
		return self.DirectorsAndOtherOfficersMember

	def getInformationAboutDirectorsAndCorporateAuditorsProposalLineItems(self): #役員の状況（取締役（及び監査役））（議案） [表示項目]
		return self.InformationAboutDirectorsAndCorporateAuditorsProposalLineItems

	def getOfficialTitleOrPositionInformationAboutDirectorsAndCorporateAuditorsProposal(self): #役職名、役員の状況（取締役（及び監査役））（議案）
		return self.OfficialTitleOrPositionInformationAboutDirectorsAndCorporateAuditorsProposal

	def getNameInformationAboutDirectorsAndCorporateAuditorsProposal(self): #氏名、役員の状況（取締役（及び監査役））（議案）
		return self.NameInformationAboutDirectorsAndCorporateAuditorsProposal

	def getDateOfBirthInformationAboutDirectorsAndCorporateAuditorsProposal(self): #生年月日、役員の状況（取締役（及び監査役））（議案）
		return self.DateOfBirthInformationAboutDirectorsAndCorporateAuditorsProposal

	def getCareerSummaryInformationAboutDirectorsAndCorporateAuditorsProposalTextBlock(self): #略歴、役員の状況（取締役（及び監査役））（議案） [テキストブロック]
		return self.CareerSummaryInformationAboutDirectorsAndCorporateAuditorsProposalTextBlock

	def getTermOfOfficeInformationAboutDirectorsAndCorporateAuditorsProposal(self): #任期、役員の状況（取締役（及び監査役））（議案）
		return self.TermOfOfficeInformationAboutDirectorsAndCorporateAuditorsProposal

	def getNumberOfSharesHeldOrdinarySharesInformationAboutDirectorsAndCorporateAuditorsProposal(self): #所有株式数（普通株式）、役員の状況（取締役（及び監査役））（議案）
		return self.NumberOfSharesHeldOrdinarySharesInformationAboutDirectorsAndCorporateAuditorsProposal

	def getNumberOfSharesHeldOtherThanOrdinarySharesInformationAboutDirectorsAndCorporateAuditorsProposal(self): #所有株式数（普通株式以外）、役員の状況（取締役（及び監査役））（議案）
		return self.NumberOfSharesHeldOtherThanOrdinarySharesInformationAboutDirectorsAndCorporateAuditorsProposal

	def getInformationAboutOfficersHeading(self): #役員の状況 [目次項目]
		return self.InformationAboutOfficersHeading

	def getFootnotesDirectorsAndCorporateAuditorsProposalTable(self): #脚注（取締役（及び監査役））（議案） [表]
		return self.FootnotesDirectorsAndCorporateAuditorsProposalTable

	def getSequentialNumbersAxis(self): #連番 [軸]
		return self.SequentialNumbersAxis

	def getRow1Member(self): #1件目 [メンバー]
		return self.Row1Member

	def getRow2Member(self): #2件目 [メンバー]
		return self.Row2Member

	def getRow3Member(self): #3件目 [メンバー]
		return self.Row3Member

	def getRow4Member(self): #4件目 [メンバー]
		return self.Row4Member

	def getRow5Member(self): #5件目 [メンバー]
		return self.Row5Member

	def getFootnotesDirectorsAndCorporateAuditorsProposalLineItems(self): #脚注（取締役（及び監査役））（議案） [表示項目]
		return self.FootnotesDirectorsAndCorporateAuditorsProposalLineItems

	def getFootnotesDirectorsAndCorporateAuditorsProposalTextBlock(self): #脚注（取締役（及び監査役））（議案） [テキストブロック]
		return self.FootnotesDirectorsAndCorporateAuditorsProposalTextBlock

	def getInformationAboutOfficersHeading(self): #役員の状況 [目次項目]
		return self.InformationAboutOfficersHeading

	def getInformationAboutExecutiveDirectorsProposalTable(self): #役員の状況（執行役）（議案） [表]
		return self.InformationAboutExecutiveDirectorsProposalTable

	def getDirectorsAndOtherOfficersAxis(self): #役員 [軸]
		return self.DirectorsAndOtherOfficersAxis

	def getDirectorsAndOtherOfficersMember(self): #役員 [メンバー] ※ディメンションデフォルト
		return self.DirectorsAndOtherOfficersMember

	def getInformationAboutExecutiveDirectorsProposalLineItems(self): #役員の状況（執行役）（議案） [表示項目]
		return self.InformationAboutExecutiveDirectorsProposalLineItems

	def getOfficialTitleOrPositionInformationAboutExecutiveDirectorsProposal(self): #役職名、役員の状況（執行役）（議案）
		return self.OfficialTitleOrPositionInformationAboutExecutiveDirectorsProposal

	def getNameInformationAboutExecutiveDirectorsProposal(self): #氏名、役員の状況（執行役）（議案）
		return self.NameInformationAboutExecutiveDirectorsProposal

	def getDateOfBirthInformationAboutExecutiveDirectorsProposal(self): #生年月日、役員の状況（執行役）（議案）
		return self.DateOfBirthInformationAboutExecutiveDirectorsProposal

	def getCareerSummaryInformationAboutExecutiveDirectorsProposalTextBlock(self): #略歴、役員の状況（執行役）（議案） [テキストブロック]
		return self.CareerSummaryInformationAboutExecutiveDirectorsProposalTextBlock

	def getTermOfOfficeInformationAboutExecutiveDirectorsProposal(self): #任期、役員の状況（執行役）（議案）
		return self.TermOfOfficeInformationAboutExecutiveDirectorsProposal

	def getNumberOfSharesHeldOrdinarySharesInformationAboutExecutiveDirectorsProposal(self): #所有株式数（普通株式）、役員の状況（執行役）（議案）
		return self.NumberOfSharesHeldOrdinarySharesInformationAboutExecutiveDirectorsProposal

	def getNumberOfSharesHeldOtherThanOrdinarySharesInformationAboutExecutiveDirectorsProposal(self): #所有株式数（普通株式以外）、役員の状況（執行役）（議案）
		return self.NumberOfSharesHeldOtherThanOrdinarySharesInformationAboutExecutiveDirectorsProposal

	def getInformationAboutOfficersHeading(self): #役員の状況 [目次項目]
		return self.InformationAboutOfficersHeading

	def getFootnotesExecutiveOfficersProposalTable(self): #脚注（執行役）（議案） [表]
		return self.FootnotesExecutiveOfficersProposalTable

	def getSequentialNumbersAxis(self): #連番 [軸]
		return self.SequentialNumbersAxis

	def getRow1Member(self): #1件目 [メンバー]
		return self.Row1Member

	def getRow2Member(self): #2件目 [メンバー]
		return self.Row2Member

	def getRow3Member(self): #3件目 [メンバー]
		return self.Row3Member

	def getRow4Member(self): #4件目 [メンバー]
		return self.Row4Member

	def getRow5Member(self): #5件目 [メンバー]
		return self.Row5Member

	def getFootnotesExecutiveOfficersProposalLineItems(self): #脚注（執行役）（議案） [表示項目]
		return self.FootnotesExecutiveOfficersProposalLineItems

	def getFootnotesExecutiveOfficersProposalTextBlock(self): #脚注（執行役）（議案） [テキストブロック]
		return self.FootnotesExecutiveOfficersProposalTextBlock

	def getOutsideDirectorsAndOutsideCorporateAuditorsTextBlock(self): #社外取締役（及び社外監査役） [テキストブロック]
		return self.OutsideDirectorsAndOutsideCorporateAuditorsTextBlock

	def getAuditsHeading(self): #監査の状況 [目次項目]
		return self.AuditsHeading

	def getAuditsTextBlock(self): #監査の状況 [テキストブロック]
		return self.AuditsTextBlock

	def getAuditsHeading(self): #監査の状況 [目次項目]
		return self.AuditsHeading

	def getNoteOnChangeOfIndependentAuditorsAuditsTextBlock(self): #監査公認会計士等の異動について、監査の状況 [テキストブロック]
		return self.NoteOnChangeOfIndependentAuditorsAuditsTextBlock

	def getFeesToPrimaryAuditorAbstract(self): #監査公認会計士等に対する報酬の内容 [タイトル項目]
		return self.FeesToPrimaryAuditorAbstract

	def getAuditFeesReportingCompany(self): #監査証明業務に基づく報酬－提出会社、監査公認会計士等
		return self.AuditFeesReportingCompany

	def getNonAuditFeesReportingCompany(self): #非監査業務に基づく報酬－提出会社、監査公認会計士等
		return self.NonAuditFeesReportingCompany

	def getAuditFeesConsolidatedSubsidiaries(self): #監査証明業務に基づく報酬－連結子会社、監査公認会計士等
		return self.AuditFeesConsolidatedSubsidiaries

	def getNonAuditFeesConsolidatedSubsidiaries(self): #非監査業務に基づく報酬－連結子会社、監査公認会計士等
		return self.NonAuditFeesConsolidatedSubsidiaries

	def getAuditFeesTotal(self): #監査証明業務に基づく報酬－計、監査公認会計士等
		return self.AuditFeesTotal

	def getNonAuditFeesTotal(self): #非監査業務に基づく報酬－計、監査公認会計士等
		return self.NonAuditFeesTotal

	def getFeesToNetworkFirmsAbstract(self): #ネットワークファームに対する報酬の内容 [タイトル項目]
		return self.FeesToNetworkFirmsAbstract

	def getAuditFeesReportingCompanyNetworkFirms(self): #監査証明業務に基づく報酬－提出会社、ネットワークファーム
		return self.AuditFeesReportingCompanyNetworkFirms

	def getNonAuditFeesReportingCompanyNetworkFirms(self): #非監査業務に基づく報酬－提出会社、ネットワークファーム
		return self.NonAuditFeesReportingCompanyNetworkFirms

	def getAuditFeesConsolidatedSubsidiariesNetworkFirms(self): #監査証明業務に基づく報酬－連結子会社、ネットワークファーム
		return self.AuditFeesConsolidatedSubsidiariesNetworkFirms

	def getNonAuditFeesConsolidatedSubsidiariesNetworkFirms(self): #非監査業務に基づく報酬－連結子会社、ネットワークファーム
		return self.NonAuditFeesConsolidatedSubsidiariesNetworkFirms

	def getAuditFeesTotalNetworkFirms(self): #監査証明業務に基づく報酬－計、ネットワークファーム
		return self.AuditFeesTotalNetworkFirms

	def getNonAuditFeesTotalNetworkFirms(self): #非監査業務に基づく報酬－計、ネットワークファーム
		return self.NonAuditFeesTotalNetworkFirms

	def getRemunerationForDirectorsAndOtherOfficersHeading(self): #役員の報酬等 [目次項目]
		return self.RemunerationForDirectorsAndOtherOfficersHeading

	def getRemunerationForDirectorsAndOtherOfficersTextBlock(self): #役員の報酬等 [テキストブロック]
		return self.RemunerationForDirectorsAndOtherOfficersTextBlock

	def getRemunerationForDirectorsAndOtherOfficersHeading(self): #役員の報酬等 [目次項目]
		return self.RemunerationForDirectorsAndOtherOfficersHeading

	def getRemunerationEtcByCategoryOfDirectorsAndOtherOfficersAbstract(self): #役員区分ごとの報酬等 [タイトル項目]
		return self.RemunerationEtcByCategoryOfDirectorsAndOtherOfficersAbstract

	def getRemunerationEtcByCategoryOfDirectorsAndOtherOfficersTable(self): #役員区分ごとの報酬等 [表]
		return self.RemunerationEtcByCategoryOfDirectorsAndOtherOfficersTable

	def getCategoriesOfDirectorsAndOtherOfficersAxis(self): #役員区分 [軸]
		return self.CategoriesOfDirectorsAndOtherOfficersAxis

	def getDirectorsExcludingOutsideDirectorsMember(self): #取締役（社外取締役を除く） [メンバー]
		return self.DirectorsExcludingOutsideDirectorsMember

	def getDirectorsExcludingAuditAndSupervisoryCommitteeMembersAndOutsideDirectorsMember(self): #取締役（監査等委員及び社外取締役を除く） [メンバー]
		return self.DirectorsExcludingAuditAndSupervisoryCommitteeMembersAndOutsideDirectorsMember

	def getDirectorsAppointedAsAuditAndSupervisoryCommitteeMembersExcludingOutsideDirectorsMember(self): #監査等委員（社外取締役を除く） [メンバー]
		return self.DirectorsAppointedAsAuditAndSupervisoryCommitteeMembersExcludingOutsideDirectorsMember

	def getCorporateAuditorsExcludingOutsideCorporateAuditorsMember(self): #監査役（社外監査役を除く） [メンバー]
		return self.CorporateAuditorsExcludingOutsideCorporateAuditorsMember

	def getExecutiveOfficersMember(self): #執行役 [メンバー]
		return self.ExecutiveOfficersMember

	def getOutsideDirectorsAndOtherOfficersMember(self): #社外役員 [メンバー]
		return self.OutsideDirectorsAndOtherOfficersMember

	def getOutsideDirectorsMember(self): #社外取締役 [メンバー]
		return self.OutsideDirectorsMember

	def getOutsideCorporateAuditorsMember(self): #社外監査役 [メンバー]
		return self.OutsideCorporateAuditorsMember

	def getRemunerationEtcByCategoryOfDirectorsAndOtherOfficersLineItems(self): #役員区分ごとの報酬等 [表示項目]
		return self.RemunerationEtcByCategoryOfDirectorsAndOtherOfficersLineItems

	def getTotalAmountOfRemunerationEtcRemunerationEtcByCategoryOfDirectorsAndOtherOfficers(self): #報酬等の総額、役員区分ごとの報酬等
		return self.TotalAmountOfRemunerationEtcRemunerationEtcByCategoryOfDirectorsAndOtherOfficers

	def getTotalAmountByTypeOfRemunerationRemunerationEtcByCategoryOfDirectorsAndOtherOfficersAbstract(self): #報酬等の種類別の総額、役員区分ごとの報酬等 [タイトル項目]
		return self.TotalAmountByTypeOfRemunerationRemunerationEtcByCategoryOfDirectorsAndOtherOfficersAbstract

	def getFixedRemunerationRemunerationByCategoryOfDirectorsAndOtherOfficers(self): #固定報酬、役員区分ごとの報酬等
		return self.FixedRemunerationRemunerationByCategoryOfDirectorsAndOtherOfficers

	def getPerformanceBasedRemunerationRemunerationByCategoryOfDirectorsAndOtherOfficers(self): #業績連動報酬、役員区分ごとの報酬等
		return self.PerformanceBasedRemunerationRemunerationByCategoryOfDirectorsAndOtherOfficers

	def getBaseRemunerationRemunerationEtcByCategoryOfDirectorsAndOtherOfficers(self): #基本報酬、役員区分ごとの報酬等
		return self.BaseRemunerationRemunerationEtcByCategoryOfDirectorsAndOtherOfficers

	def getShareAwardsRemunerationEtcByCategoryOfDirectorsAndOtherOfficers(self): #株式報酬、役員区分ごとの報酬等
		return self.ShareAwardsRemunerationEtcByCategoryOfDirectorsAndOtherOfficers

	def getRestrictedShareAwardsRemunerationEtcByCategoryOfDirectorsAndOtherOfficers(self): #譲渡制限付株式報酬、役員区分ごとの報酬等
		return self.RestrictedShareAwardsRemunerationEtcByCategoryOfDirectorsAndOtherOfficers

	def getPerformanceLinkedShareAwardsRemunerationEtcByCategoryOfDirectorsAndOtherOfficers(self): #業績連動型株式報酬、役員区分ごとの報酬等
		return self.PerformanceLinkedShareAwardsRemunerationEtcByCategoryOfDirectorsAndOtherOfficers

	def getShareOptionRemunerationEtcByCategoryOfDirectorsAndOtherOfficers(self): #ストックオプション、役員区分ごとの報酬等
		return self.ShareOptionRemunerationEtcByCategoryOfDirectorsAndOtherOfficers

	def getBonusRemunerationEtcByCategoryOfDirectorsAndOtherOfficers(self): #賞与、役員区分ごとの報酬等
		return self.BonusRemunerationEtcByCategoryOfDirectorsAndOtherOfficers

	def getRetirementBenefitsRemunerationEtcByCategoryOfDirectorsAndOtherOfficers(self): #退職慰労金、役員区分ごとの報酬等
		return self.RetirementBenefitsRemunerationEtcByCategoryOfDirectorsAndOtherOfficers

	def getNonMonetaryRemunerationRemunerationByCategoryOfDirectorsAndOtherOfficers(self): #非金銭報酬等、役員区分ごとの報酬等
		return self.NonMonetaryRemunerationRemunerationByCategoryOfDirectorsAndOtherOfficers

	def getOtherRemunerationEtcByCategoryOfDirectorsAndOtherOfficers(self): #その他、役員区分ごとの報酬等
		return self.OtherRemunerationEtcByCategoryOfDirectorsAndOtherOfficers

	def getNumberOfDirectorsAndOtherOfficersRemunerationEtcByCategoryOfDirectorsAndOtherOfficers(self): #対象となる役員の員数、役員区分ごとの報酬等
		return self.NumberOfDirectorsAndOtherOfficersRemunerationEtcByCategoryOfDirectorsAndOtherOfficers

	def getRemunerationEtcPaidByGroupToEachDirectorOrOtherOfficerTextBlock(self): #役員ごとの連結報酬等 [テキストブロック]
		return self.RemunerationEtcPaidByGroupToEachDirectorOrOtherOfficerTextBlock

	def getRemunerationForDirectorsAndOtherOfficersHeading(self): #役員の報酬等 [目次項目]
		return self.RemunerationForDirectorsAndOtherOfficersHeading

	def getRemunerationEtcPaidByGroupToEachDirectorOrOtherOfficerAbstract(self): #役員ごとの連結報酬等 [タイトル項目]
		return self.RemunerationEtcPaidByGroupToEachDirectorOrOtherOfficerAbstract

	def getRemunerationEtcPaidByGroupToEachDirectorOrOtherOfficerTable(self): #役員ごとの連結報酬等 [表]
		return self.RemunerationEtcPaidByGroupToEachDirectorOrOtherOfficerTable

	def getDirectorsAndOtherOfficersAxis(self): #役員 [軸]
		return self.DirectorsAndOtherOfficersAxis

	def getDirectorsAndOtherOfficersMember(self): #役員 [メンバー] ※ディメンションデフォルト
		return self.DirectorsAndOtherOfficersMember

	def getRemunerationEtcPaidByGroupToEachDirectorOrOtherOfficerLineItems(self): #役員ごとの連結報酬等 [表示項目]
		return self.RemunerationEtcPaidByGroupToEachDirectorOrOtherOfficerLineItems

	def getTotalAmountOfRemunerationEtcPaidByGroupRemunerationEtcPaidByGroupToEachDirectorOrOtherOfficer(self): #連結報酬等の総額、役員ごとの連結報酬等
		return self.TotalAmountOfRemunerationEtcPaidByGroupRemunerationEtcPaidByGroupToEachDirectorOrOtherOfficer

	def getShareholdingsHeading(self): #株式の保有状況 [目次項目]
		return self.ShareholdingsHeading

	def getShareholdingsTextBlock(self): #株式の保有状況 [テキストブロック]
		return self.ShareholdingsTextBlock

	def getShareholdingsHeading(self): #株式の保有状況 [目次項目]
		return self.ShareholdingsHeading

	def getReportingCompanyEquitySecuritiesHeldAbstract(self): #提出会社、株式の保有状況 [タイトル項目]
		return self.ReportingCompanyEquitySecuritiesHeldAbstract

	def getInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentReportingCompanyAbstract(self): #保有目的が純投資目的以外の目的である投資株式、提出会社 [タイトル項目]
		return self.InvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentReportingCompanyAbstract

	def getSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompanyAbstract(self): #非上場株式、保有目的が純投資目的以外の目的である投資株式、提出会社 [タイトル項目]
		return self.SharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompanyAbstract

	def getNumberOfIssuesSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany(self): #銘柄数、非上場株式、保有目的が純投資目的以外の目的である投資株式、提出会社
		return self.NumberOfIssuesSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany

	def getCarryingAmountSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany(self): #貸借対照表計上額、非上場株式、保有目的が純投資目的以外の目的である投資株式、提出会社
		return self.CarryingAmountSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany

	def getNumberOfIssuesWhoseNumberOfSharesIncreasedSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany(self): #株式数が増加した銘柄数、非上場株式、保有目的が純投資目的以外の目的である投資株式、提出会社
		return self.NumberOfIssuesWhoseNumberOfSharesIncreasedSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany

	def getTotalAcquisitionCostForIncreasedSharesSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany(self): #株式数の増加に係る取得価額の合計額、非上場株式、保有目的が純投資目的以外の目的である投資株式、提出会社
		return self.TotalAcquisitionCostForIncreasedSharesSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany

	def getReasonForIncreaseInNumberOfSharesSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany(self): #株式数が増加した理由、非上場株式、保有目的が純投資目的以外の目的である投資株式、提出会社
		return self.ReasonForIncreaseInNumberOfSharesSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany

	def getNumberOfIssuesWhoseNumberOfSharesDecreasedSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany(self): #株式数が減少した銘柄数、非上場株式、保有目的が純投資目的以外の目的である投資株式、提出会社
		return self.NumberOfIssuesWhoseNumberOfSharesDecreasedSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany

	def getTotalSaleAmountForDecreasedSharesSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany(self): #株式数の減少に係る売却価額の合計額、非上場株式、保有目的が純投資目的以外の目的である投資株式、提出会社
		return self.TotalSaleAmountForDecreasedSharesSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany

	def getSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompanyAbstract(self): #非上場株式以外の株式、保有目的が純投資目的以外の目的である投資株式、提出会社 [タイトル項目]
		return self.SharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompanyAbstract

	def getNumberOfIssuesSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany(self): #銘柄数、非上場株式以外の株式、保有目的が純投資目的以外の目的である投資株式、提出会社
		return self.NumberOfIssuesSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany

	def getCarryingAmountSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany(self): #貸借対照表計上額、非上場株式以外の株式、保有目的が純投資目的以外の目的である投資株式、提出会社
		return self.CarryingAmountSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany

	def getNumberOfIssuesWhoseNumberOfSharesIncreasedSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany(self): #株式数が増加した銘柄数、非上場株式以外の株式、保有目的が純投資目的以外の目的である投資株式、提出会社
		return self.NumberOfIssuesWhoseNumberOfSharesIncreasedSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany

	def getTotalAcquisitionCostForIncreasedSharesSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany(self): #株式数の増加に係る取得価額の合計額、非上場株式以外の株式、保有目的が純投資目的以外の目的である投資株式、提出会社
		return self.TotalAcquisitionCostForIncreasedSharesSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany

	def getReasonForIncreaseInNumberOfSharesSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany(self): #株式数が増加した理由、非上場株式以外の株式、保有目的が純投資目的以外の目的である投資株式、提出会社
		return self.ReasonForIncreaseInNumberOfSharesSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany

	def getNumberOfIssuesWhoseNumberOfSharesDecreasedSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany(self): #株式数が減少した銘柄数、非上場株式以外の株式、保有目的が純投資目的以外の目的である投資株式、提出会社
		return self.NumberOfIssuesWhoseNumberOfSharesDecreasedSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany

	def getTotalSaleAmountForDecreasedSharesSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany(self): #株式数の減少に係る売却価額の合計額、非上場株式以外の株式、保有目的が純投資目的以外の目的である投資株式、提出会社
		return self.TotalSaleAmountForDecreasedSharesSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany

	def getShareholdingsHeading(self): #株式の保有状況 [目次項目]
		return self.ShareholdingsHeading

	def getReportingCompanyEquitySecuritiesHeldAbstract(self): #提出会社、株式の保有状況 [タイトル項目]
		return self.ReportingCompanyEquitySecuritiesHeldAbstract

	def getDetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentReportingCompanyTable(self): #保有目的が純投資目的以外の目的である特定投資株式の明細、提出会社 [表]
		return self.DetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentReportingCompanyTable

	def getSequentialNumbersAxis(self): #連番 [軸]
		return self.SequentialNumbersAxis

	def getRow1Member(self): #1件目 [メンバー]
		return self.Row1Member

	def getRow2Member(self): #2件目 [メンバー]
		return self.Row2Member

	def getRow3Member(self): #3件目 [メンバー]
		return self.Row3Member

	def getRow4Member(self): #4件目 [メンバー]
		return self.Row4Member

	def getRow5Member(self): #5件目 [メンバー]
		return self.Row5Member

	def getRow6Member(self): #6件目 [メンバー]
		return self.Row6Member

	def getRow7Member(self): #7件目 [メンバー]
		return self.Row7Member

	def getRow8Member(self): #8件目 [メンバー]
		return self.Row8Member

	def getRow9Member(self): #9件目 [メンバー]
		return self.Row9Member

	def getRow10Member(self): #10件目 [メンバー]
		return self.Row10Member

	def getRow11Member(self): #11件目 [メンバー]
		return self.Row11Member

	def getRow12Member(self): #12件目 [メンバー]
		return self.Row12Member

	def getRow13Member(self): #13件目 [メンバー]
		return self.Row13Member

	def getRow14Member(self): #14件目 [メンバー]
		return self.Row14Member

	def getRow15Member(self): #15件目 [メンバー]
		return self.Row15Member

	def getRow16Member(self): #16件目 [メンバー]
		return self.Row16Member

	def getRow17Member(self): #17件目 [メンバー]
		return self.Row17Member

	def getRow18Member(self): #18件目 [メンバー]
		return self.Row18Member

	def getRow19Member(self): #19件目 [メンバー]
		return self.Row19Member

	def getRow20Member(self): #20件目 [メンバー]
		return self.Row20Member

	def getRow21Member(self): #21件目 [メンバー]
		return self.Row21Member

	def getRow22Member(self): #22件目 [メンバー]
		return self.Row22Member

	def getRow23Member(self): #23件目 [メンバー]
		return self.Row23Member

	def getRow24Member(self): #24件目 [メンバー]
		return self.Row24Member

	def getRow25Member(self): #25件目 [メンバー]
		return self.Row25Member

	def getRow26Member(self): #26件目 [メンバー]
		return self.Row26Member

	def getRow27Member(self): #27件目 [メンバー]
		return self.Row27Member

	def getRow28Member(self): #28件目 [メンバー]
		return self.Row28Member

	def getRow29Member(self): #29件目 [メンバー]
		return self.Row29Member

	def getRow30Member(self): #30件目 [メンバー]
		return self.Row30Member

	def getRow31Member(self): #31件目 [メンバー]
		return self.Row31Member

	def getRow32Member(self): #32件目 [メンバー]
		return self.Row32Member

	def getRow33Member(self): #33件目 [メンバー]
		return self.Row33Member

	def getRow34Member(self): #34件目 [メンバー]
		return self.Row34Member

	def getRow35Member(self): #35件目 [メンバー]
		return self.Row35Member

	def getRow36Member(self): #36件目 [メンバー]
		return self.Row36Member

	def getRow37Member(self): #37件目 [メンバー]
		return self.Row37Member

	def getRow38Member(self): #38件目 [メンバー]
		return self.Row38Member

	def getRow39Member(self): #39件目 [メンバー]
		return self.Row39Member

	def getRow40Member(self): #40件目 [メンバー]
		return self.Row40Member

	def getRow41Member(self): #41件目 [メンバー]
		return self.Row41Member

	def getRow42Member(self): #42件目 [メンバー]
		return self.Row42Member

	def getRow43Member(self): #43件目 [メンバー]
		return self.Row43Member

	def getRow44Member(self): #44件目 [メンバー]
		return self.Row44Member

	def getRow45Member(self): #45件目 [メンバー]
		return self.Row45Member

	def getRow46Member(self): #46件目 [メンバー]
		return self.Row46Member

	def getRow47Member(self): #47件目 [メンバー]
		return self.Row47Member

	def getRow48Member(self): #48件目 [メンバー]
		return self.Row48Member

	def getRow49Member(self): #49件目 [メンバー]
		return self.Row49Member

	def getRow50Member(self): #50件目 [メンバー]
		return self.Row50Member

	def getRow51Member(self): #51件目 [メンバー]
		return self.Row51Member

	def getRow52Member(self): #52件目 [メンバー]
		return self.Row52Member

	def getRow53Member(self): #53件目 [メンバー]
		return self.Row53Member

	def getRow54Member(self): #54件目 [メンバー]
		return self.Row54Member

	def getRow55Member(self): #55件目 [メンバー]
		return self.Row55Member

	def getRow56Member(self): #56件目 [メンバー]
		return self.Row56Member

	def getRow57Member(self): #57件目 [メンバー]
		return self.Row57Member

	def getRow58Member(self): #58件目 [メンバー]
		return self.Row58Member

	def getRow59Member(self): #59件目 [メンバー]
		return self.Row59Member

	def getRow60Member(self): #60件目 [メンバー]
		return self.Row60Member

	def getDetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentReportingCompanyLineItems(self): #保有目的が純投資目的以外の目的である特定投資株式の明細、提出会社 [表示項目]
		return self.DetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentReportingCompanyLineItems

	def getNameOfSecuritiesDetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentReportingCompany(self): #銘柄、保有目的が純投資目的以外の目的である特定投資株式の明細、提出会社
		return self.NameOfSecuritiesDetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentReportingCompany

	def getNumberOfSharesHeldDetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentReportingCompany(self): #株式数、保有目的が純投資目的以外の目的である特定投資株式の明細、提出会社
		return self.NumberOfSharesHeldDetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentReportingCompany

	def getNumberOfSharesNotDisclosedAsBelowThresholdDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany(self): #株式数（記載省略）、保有目的が純投資目的以外の目的である特定投資株式の明細、提出会社
		return self.NumberOfSharesNotDisclosedAsBelowThresholdDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany

	def getBookValueDetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentReportingCompany(self): #貸借対照表計上額、保有目的が純投資目的以外の目的である特定投資株式の明細、提出会社
		return self.BookValueDetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentReportingCompany

	def getCarryingAmountNotDisclosedAsBelowThresholdDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany(self): #貸借対照表計上額（記載省略）、保有目的が純投資目的以外の目的である特定投資株式の明細、提出会社
		return self.CarryingAmountNotDisclosedAsBelowThresholdDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany

	def getPurposesOfHoldingDetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentReportingCompany(self): #保有目的、保有目的が純投資目的以外の目的である特定投資株式の明細、提出会社
		return self.PurposesOfHoldingDetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentReportingCompany

	def getQuantitativeEffectsOfShareholdingDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany(self): #定量的な保有効果、保有目的が純投資目的以外の目的である特定投資株式の明細、提出会社
		return self.QuantitativeEffectsOfShareholdingDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany

	def getReasonForIncreaseInNumberOfSharesDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany(self): #株式数が増加した理由、保有目的が純投資目的以外の目的である特定投資株式の明細、提出会社
		return self.ReasonForIncreaseInNumberOfSharesDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany

	def getPurposeOfShareholdingQuantitativeEffectsOfShareholdingAndReasonForIncreaseInNumberOfSharesDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany(self): #保有目的、定量的な保有効果及び株式数が増加した理由、保有目的が純投資目的以外の目的である特定投資株式の明細、提出会社
		return self.PurposeOfShareholdingQuantitativeEffectsOfShareholdingAndReasonForIncreaseInNumberOfSharesDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany

	def getWhetherIssuerOfAforementionedSharesHoldsReportingCompanysSharesDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany(self): #当該株式の発行者による提出会社の株式の保有の有無、保有目的が純投資目的以外の目的である特定投資株式の明細、提出会社
		return self.WhetherIssuerOfAforementionedSharesHoldsReportingCompanysSharesDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentReportingCompany

	def getShareholdingsHeading(self): #株式の保有状況 [目次項目]
		return self.ShareholdingsHeading

	def getReportingCompanyEquitySecuritiesHeldAbstract(self): #提出会社、株式の保有状況 [タイトル項目]
		return self.ReportingCompanyEquitySecuritiesHeldAbstract

	def getDetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentReportingCompanyTable(self): #保有目的が純投資目的以外の目的であるみなし保有株式の明細、提出会社 [表]
		return self.DetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentReportingCompanyTable

	def getSequentialNumbersAxis(self): #連番 [軸]
		return self.SequentialNumbersAxis

	def getRow1Member(self): #1件目 [メンバー]
		return self.Row1Member

	def getRow2Member(self): #2件目 [メンバー]
		return self.Row2Member

	def getRow3Member(self): #3件目 [メンバー]
		return self.Row3Member

	def getRow4Member(self): #4件目 [メンバー]
		return self.Row4Member

	def getRow5Member(self): #5件目 [メンバー]
		return self.Row5Member

	def getRow6Member(self): #6件目 [メンバー]
		return self.Row6Member

	def getRow7Member(self): #7件目 [メンバー]
		return self.Row7Member

	def getRow8Member(self): #8件目 [メンバー]
		return self.Row8Member

	def getRow9Member(self): #9件目 [メンバー]
		return self.Row9Member

	def getRow10Member(self): #10件目 [メンバー]
		return self.Row10Member

	def getDetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentReportingCompanyLineItems(self): #保有目的が純投資目的以外の目的であるみなし保有株式の明細、提出会社 [表示項目]
		return self.DetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentReportingCompanyLineItems

	def getNameOfSecuritiesDetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentReportingCompany(self): #銘柄、保有目的が純投資目的以外の目的であるみなし保有株式の明細、提出会社
		return self.NameOfSecuritiesDetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentReportingCompany

	def getNumberOfSharesHeldDetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentReportingCompany(self): #株式数、保有目的が純投資目的以外の目的であるみなし保有株式の明細、提出会社
		return self.NumberOfSharesHeldDetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentReportingCompany

	def getNumberOfSharesNotDisclosedAsBelowThresholdDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentReportingCompany(self): #株式数（記載省略）、保有目的が純投資目的以外の目的であるみなし保有株式の明細、提出会社
		return self.NumberOfSharesNotDisclosedAsBelowThresholdDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentReportingCompany

	def getBookValueDetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentReportingCompany(self): #貸借対照表計上額、保有目的が純投資目的以外の目的であるみなし保有株式の明細、提出会社
		return self.BookValueDetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentReportingCompany

	def getCarryingAmountNotDisclosedAsBelowThresholdDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentReportingCompany(self): #貸借対照表計上額（記載省略）、保有目的が純投資目的以外の目的であるみなし保有株式の明細、提出会社
		return self.CarryingAmountNotDisclosedAsBelowThresholdDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentReportingCompany

	def getPurposesOfHoldingDetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentReportingCompany(self): #保有目的、保有目的が純投資目的以外の目的であるみなし保有株式の明細、提出会社
		return self.PurposesOfHoldingDetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentReportingCompany

	def getQuantitativeEffectsOfShareholdingDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentReportingCompany(self): #定量的な保有効果、保有目的が純投資目的以外の目的であるみなし保有株式の明細、提出会社
		return self.QuantitativeEffectsOfShareholdingDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentReportingCompany

	def getReasonForIncreaseInNumberOfSharesDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentReportingCompany(self): #株式数が増加した理由、保有目的が純投資目的以外の目的であるみなし保有株式の明細、提出会社
		return self.ReasonForIncreaseInNumberOfSharesDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentReportingCompany

	def getPurposeOfShareholdingQuantitativeEffectsOfShareholdingAndReasonForIncreaseInNumberOfSharesDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentReportingCompany(self): #保有目的、定量的な保有効果及び株式数が増加した理由、保有目的が純投資目的以外の目的であるみなし保有株式の明細、提出会社
		return self.PurposeOfShareholdingQuantitativeEffectsOfShareholdingAndReasonForIncreaseInNumberOfSharesDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentReportingCompany

	def getWhetherIssuerOfAforementionedSharesHoldsReportingCompanysSharesDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentReportingCompany(self): #当該株式の発行者による提出会社の株式の保有の有無、保有目的が純投資目的以外の目的であるみなし保有株式の明細、提出会社
		return self.WhetherIssuerOfAforementionedSharesHoldsReportingCompanysSharesDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentReportingCompany

	def getShareholdingsHeading(self): #株式の保有状況 [目次項目]
		return self.ShareholdingsHeading

	def getReportingCompanyEquitySecuritiesHeldAbstract(self): #提出会社、株式の保有状況 [タイトル項目]
		return self.ReportingCompanyEquitySecuritiesHeldAbstract

	def getInvestmentEquitySecuritiesHeldForPureInvestmentReportingCompanyAbstract(self): #保有目的が純投資目的である投資株式、提出会社 [タイトル項目]
		return self.InvestmentEquitySecuritiesHeldForPureInvestmentReportingCompanyAbstract

	def getEquitySecuritiesNotListedInvestmentEquitySecuritiesHeldForPureInvestmentReportingCompanyAbstract(self): #非上場株式、保有目的が純投資目的である投資株式、提出会社 [タイトル項目]
		return self.EquitySecuritiesNotListedInvestmentEquitySecuritiesHeldForPureInvestmentReportingCompanyAbstract

	def getNumberOfIssuesSharesNotListedInvestmentSharesHeldForPureInvestmentReportingCompany(self): #銘柄数、非上場株式、保有目的が純投資目的である投資株式、提出会社
		return self.NumberOfIssuesSharesNotListedInvestmentSharesHeldForPureInvestmentReportingCompany

	def getBookValueEquitySecuritiesNotListedInvestmentEquitySecuritiesHeldForPureInvestmentReportingCompany(self): #貸借対照表計上額の合計額、非上場株式、保有目的が純投資目的である投資株式、提出会社
		return self.BookValueEquitySecuritiesNotListedInvestmentEquitySecuritiesHeldForPureInvestmentReportingCompany

	def getTotalOfDividendsReceivedEquitySecuritiesNotListedInvestmentEquitySecuritiesHeldForPureInvestmentReportingCompany(self): #受取配当金の合計額、非上場株式、保有目的が純投資目的である投資株式、提出会社
		return self.TotalOfDividendsReceivedEquitySecuritiesNotListedInvestmentEquitySecuritiesHeldForPureInvestmentReportingCompany

	def getTotalOfGainLossOnSaleEquitySecuritiesNotListedInvestmentEquitySecuritiesHeldForPureInvestmentReportingCompany(self): #売却損益の合計額、非上場株式、保有目的が純投資目的である投資株式、提出会社
		return self.TotalOfGainLossOnSaleEquitySecuritiesNotListedInvestmentEquitySecuritiesHeldForPureInvestmentReportingCompany

	def getTotalOfValuationGainLossEquitySecuritiesNotListedInvestmentEquitySecuritiesHeldForPureInvestmentReportingCompany(self): #評価損益の合計額、非上場株式、保有目的が純投資目的である投資株式、提出会社
		return self.TotalOfValuationGainLossEquitySecuritiesNotListedInvestmentEquitySecuritiesHeldForPureInvestmentReportingCompany

	def getEquitySecuritiesOtherThanThoseNotListedInvestmentEquitySecuritiesHeldForPureInvestmentReportingCompanyAbstract(self): #非上場株式以外の株式、保有目的が純投資目的である投資株式、提出会社 [タイトル項目]
		return self.EquitySecuritiesOtherThanThoseNotListedInvestmentEquitySecuritiesHeldForPureInvestmentReportingCompanyAbstract

	def getNumberOfIssuesSharesOtherThanThoseNotListedInvestmentSharesHeldForPureInvestmentReportingCompany(self): #銘柄数、非上場株式以外の株式、保有目的が純投資目的である投資株式、提出会社
		return self.NumberOfIssuesSharesOtherThanThoseNotListedInvestmentSharesHeldForPureInvestmentReportingCompany

	def getBookValueEquitySecuritiesOtherThanThoseNotListedInvestmentEquitySecuritiesHeldForPureInvestmentReportingCompany(self): #貸借対照表計上額の合計額、非上場株式以外の株式、保有目的が純投資目的である投資株式、提出会社
		return self.BookValueEquitySecuritiesOtherThanThoseNotListedInvestmentEquitySecuritiesHeldForPureInvestmentReportingCompany

	def getTotalOfDividendsReceivedEquitySecuritiesOtherThanThoseNotListedInvestmentEquitySecuritiesHeldForPureInvestmentReportingCompany(self): #受取配当金の合計額、非上場株式以外の株式、保有目的が純投資目的である投資株式、提出会社
		return self.TotalOfDividendsReceivedEquitySecuritiesOtherThanThoseNotListedInvestmentEquitySecuritiesHeldForPureInvestmentReportingCompany

	def getTotalOfGainLossOnSaleEquitySecuritiesOtherThanThoseNotListedInvestmentEquitySecuritiesHeldForPureInvestmentReportingCompany(self): #売却損益の合計額、非上場株式以外の株式、保有目的が純投資目的である投資株式、提出会社
		return self.TotalOfGainLossOnSaleEquitySecuritiesOtherThanThoseNotListedInvestmentEquitySecuritiesHeldForPureInvestmentReportingCompany

	def getTotalOfValuationGainLossEquitySecuritiesOtherThanThoseNotListedInvestmentEquitySecuritiesHeldForPureInvestmentReportingCompany(self): #評価損益の合計額、非上場株式以外の株式、保有目的が純投資目的である投資株式、提出会社
		return self.TotalOfValuationGainLossEquitySecuritiesOtherThanThoseNotListedInvestmentEquitySecuritiesHeldForPureInvestmentReportingCompany

	def getShareholdingsHeading(self): #株式の保有状況 [目次項目]
		return self.ShareholdingsHeading

	def getReportingCompanyEquitySecuritiesHeldAbstract(self): #提出会社、株式の保有状況 [タイトル項目]
		return self.ReportingCompanyEquitySecuritiesHeldAbstract

	def getInvestmentEquitySecuritiesReclassifiedFromHeldForPureInvestmentToHeldForPurposesOtherThanPureInvestmentReportingCompanyTable(self): #投資株式の保有目的を純投資目的から純投資目的以外の目的に変更したもの、提出会社 [表]
		return self.InvestmentEquitySecuritiesReclassifiedFromHeldForPureInvestmentToHeldForPurposesOtherThanPureInvestmentReportingCompanyTable

	def getSequentialNumbersAxis(self): #連番 [軸]
		return self.SequentialNumbersAxis

	def getRow1Member(self): #1件目 [メンバー]
		return self.Row1Member

	def getRow2Member(self): #2件目 [メンバー]
		return self.Row2Member

	def getRow3Member(self): #3件目 [メンバー]
		return self.Row3Member

	def getInvestmentEquitySecuritiesReclassifiedFromHeldForPureInvestmentToHeldForPurposesOtherThanPureInvestmentReportingCompanyLineItems(self): #投資株式の保有目的を純投資目的から純投資目的以外の目的に変更したもの、提出会社 [表示項目]
		return self.InvestmentEquitySecuritiesReclassifiedFromHeldForPureInvestmentToHeldForPurposesOtherThanPureInvestmentReportingCompanyLineItems

	def getSecurityNameInvestmentEquitySecuritiesReclassifiedFromHeldForPureInvestmentToHeldForPurposesOtherThanPureInvestmentReportingCompany(self): #銘柄、投資株式の保有目的を純投資目的から純投資目的以外の目的に変更したもの、提出会社
		return self.SecurityNameInvestmentEquitySecuritiesReclassifiedFromHeldForPureInvestmentToHeldForPurposesOtherThanPureInvestmentReportingCompany

	def getNumberOfSharesHeldInvestmentEquitySecuritiesReclassifiedFromHeldForPureInvestmentToHeldForPurposesOtherThanPureInvestmentReportingCompany(self): #株式数、投資株式の保有目的を純投資目的から純投資目的以外の目的に変更したもの、提出会社
		return self.NumberOfSharesHeldInvestmentEquitySecuritiesReclassifiedFromHeldForPureInvestmentToHeldForPurposesOtherThanPureInvestmentReportingCompany

	def getBookValueInvestmentEquitySecuritiesReclassifiedFromHeldForPureInvestmentToHeldForPurposesOtherThanPureInvestmentReportingCompany(self): #貸借対照表計上額、投資株式の保有目的を純投資目的から純投資目的以外の目的に変更したもの、提出会社
		return self.BookValueInvestmentEquitySecuritiesReclassifiedFromHeldForPureInvestmentToHeldForPurposesOtherThanPureInvestmentReportingCompany

	def getShareholdingsHeading(self): #株式の保有状況 [目次項目]
		return self.ShareholdingsHeading

	def getReportingCompanyEquitySecuritiesHeldAbstract(self): #提出会社、株式の保有状況 [タイトル項目]
		return self.ReportingCompanyEquitySecuritiesHeldAbstract

	def getInvestmentEquitySecuritiesReclassifiedFromHeldForPurposesOtherThanPureInvestmentToHeldForPureInvestmentReportingCompanyTable(self): #投資株式の保有目的を純投資以外の目的から純投資目的に変更したもの、提出会社 [表]
		return self.InvestmentEquitySecuritiesReclassifiedFromHeldForPurposesOtherThanPureInvestmentToHeldForPureInvestmentReportingCompanyTable

	def getSequentialNumbersAxis(self): #連番 [軸]
		return self.SequentialNumbersAxis

	def getRow1Member(self): #1件目 [メンバー]
		return self.Row1Member

	def getRow2Member(self): #2件目 [メンバー]
		return self.Row2Member

	def getRow3Member(self): #3件目 [メンバー]
		return self.Row3Member

	def getInvestmentEquitySecuritiesReclassifiedFromHeldForPurposesOtherThanPureInvestmentToHeldForPureInvestmentReportingCompanyLineItems(self): #投資株式の保有目的を純投資以外の目的から純投資目的に変更したもの、提出会社 [表示項目]
		return self.InvestmentEquitySecuritiesReclassifiedFromHeldForPurposesOtherThanPureInvestmentToHeldForPureInvestmentReportingCompanyLineItems

	def getNameOfSecuritiesInvestmentEquitySecuritiesReclassifiedFromHeldForPurposesOtherThanPureInvestmentToHeldForPureInvestmentReportingCompany(self): #銘柄、投資株式の保有目的を純投資以外の目的から純投資目的に変更したもの、提出会社
		return self.NameOfSecuritiesInvestmentEquitySecuritiesReclassifiedFromHeldForPurposesOtherThanPureInvestmentToHeldForPureInvestmentReportingCompany

	def getNumberOfSharesHeldInvestmentEquitySecuritiesReclassifiedFromHeldForPurposesOtherThanPureInvestmentToHeldForPureInvestmentReportingCompany(self): #株式数、投資株式の保有目的を純投資以外の目的から純投資目的に変更したもの、提出会社
		return self.NumberOfSharesHeldInvestmentEquitySecuritiesReclassifiedFromHeldForPurposesOtherThanPureInvestmentToHeldForPureInvestmentReportingCompany

	def getBookValueInvestmentEquitySecuritiesReclassifiedFromHeldForPurposesOtherThanPureInvestmentToHeldForPureInvestmentReportingCompany(self): #貸借対照表計上額、投資株式の保有目的を純投資以外の目的から純投資目的に変更したもの、提出会社
		return self.BookValueInvestmentEquitySecuritiesReclassifiedFromHeldForPurposesOtherThanPureInvestmentToHeldForPureInvestmentReportingCompany

	def getShareholdingsHeading(self): #株式の保有状況 [目次項目]
		return self.ShareholdingsHeading

	def getGroupCompanyHoldingLargestAmountOfInvestmentEquitySecuritiesInGroupEquitySecuritiesHeldAbstract(self): #最大保有会社（提出会社でない場合）、株式の保有状況 [タイトル項目]
		return self.GroupCompanyHoldingLargestAmountOfInvestmentEquitySecuritiesInGroupEquitySecuritiesHeldAbstract

	def getInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompanyAbstract(self): #保有目的が純投資目的以外の目的である投資株式、最大保有会社 [タイトル項目]
		return self.InvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompanyAbstract

	def getSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompanyAbstract(self): #非上場株式、保有目的が純投資目的以外の目的である投資株式、最大保有会社 [タイトル項目]
		return self.SharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompanyAbstract

	def getNumberOfIssuesSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany(self): #銘柄数、非上場株式、保有目的が純投資目的以外の目的である投資株式、最大保有会社
		return self.NumberOfIssuesSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany

	def getCarryingAmountSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany(self): #貸借対照表計上額、非上場株式、保有目的が純投資目的以外の目的である投資株式、最大保有会社
		return self.CarryingAmountSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany

	def getNumberOfIssuesWhoseNumberOfSharesIncreasedSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany(self): #株式数が増加した銘柄数、非上場株式、保有目的が純投資目的以外の目的である投資株式、最大保有会社
		return self.NumberOfIssuesWhoseNumberOfSharesIncreasedSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany

	def getTotalAcquisitionCostForIncreasedSharesSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany(self): #株式数の増加に係る取得価額の合計額、非上場株式、保有目的が純投資目的以外の目的である投資株式、最大保有会社
		return self.TotalAcquisitionCostForIncreasedSharesSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany

	def getReasonForIncreaseInNumberOfSharesSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany(self): #株式数が増加した理由、非上場株式、保有目的が純投資目的以外の目的である投資株式、最大保有会社
		return self.ReasonForIncreaseInNumberOfSharesSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany

	def getNumberOfIssuesWhoseNumberOfSharesDecreasedSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany(self): #株式数が減少した銘柄数、非上場株式、保有目的が純投資目的以外の目的である投資株式、最大保有会社
		return self.NumberOfIssuesWhoseNumberOfSharesDecreasedSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany

	def getTotalSaleAmountForDecreasedSharesSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany(self): #株式数の減少に係る売却価額の合計額、非上場株式、保有目的が純投資目的以外の目的である投資株式、最大保有会社
		return self.TotalSaleAmountForDecreasedSharesSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany

	def getSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompanyAbstract(self): #非上場株式以外の株式、保有目的が純投資目的以外の目的である投資株式、最大保有会社 [タイトル項目]
		return self.SharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompanyAbstract

	def getNumberOfIssuesSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany(self): #銘柄数、非上場株式以外の株式、保有目的が純投資目的以外の目的である投資株式、最大保有会社
		return self.NumberOfIssuesSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany

	def getCarryingAmountSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany(self): #貸借対照表計上額、非上場株式以外の株式、保有目的が純投資目的以外の目的である投資株式、最大保有会社
		return self.CarryingAmountSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany

	def getNumberOfIssuesWhoseNumberOfSharesIncreasedSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany(self): #株式数が増加した銘柄数、非上場株式以外の株式、保有目的が純投資目的以外の目的である投資株式、最大保有会社
		return self.NumberOfIssuesWhoseNumberOfSharesIncreasedSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany

	def getTotalAcquisitionCostForIncreasedSharesSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany(self): #株式数の増加に係る取得価額の合計額、非上場株式以外の株式、保有目的が純投資目的以外の目的である投資株式、最大保有会社
		return self.TotalAcquisitionCostForIncreasedSharesSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany

	def getReasonForIncreaseInNumberOfSharesSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany(self): #株式数が増加した理由、非上場株式以外の株式、保有目的が純投資目的以外の目的である投資株式、最大保有会社
		return self.ReasonForIncreaseInNumberOfSharesSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany

	def getNumberOfIssuesWhoseNumberOfSharesDecreasedSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany(self): #株式数が減少した銘柄数、非上場株式以外の株式、保有目的が純投資目的以外の目的である投資株式、最大保有会社
		return self.NumberOfIssuesWhoseNumberOfSharesDecreasedSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany

	def getTotalSaleAmountForDecreasedSharesSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany(self): #株式数の減少に係る売却価額の合計額、非上場株式以外の株式、保有目的が純投資目的以外の目的である投資株式、最大保有会社
		return self.TotalSaleAmountForDecreasedSharesSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany

	def getShareholdingsHeading(self): #株式の保有状況 [目次項目]
		return self.ShareholdingsHeading

	def getGroupCompanyHoldingLargestAmountOfInvestmentEquitySecuritiesInGroupEquitySecuritiesHeldAbstract(self): #最大保有会社（提出会社でない場合）、株式の保有状況 [タイトル項目]
		return self.GroupCompanyHoldingLargestAmountOfInvestmentEquitySecuritiesInGroupEquitySecuritiesHeldAbstract

	def getDetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompanyTable(self): #保有目的が純投資目的以外の目的である特定投資株式の明細、最大保有会社 [表]
		return self.DetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompanyTable

	def getSequentialNumbersAxis(self): #連番 [軸]
		return self.SequentialNumbersAxis

	def getRow1Member(self): #1件目 [メンバー]
		return self.Row1Member

	def getRow2Member(self): #2件目 [メンバー]
		return self.Row2Member

	def getRow3Member(self): #3件目 [メンバー]
		return self.Row3Member

	def getRow4Member(self): #4件目 [メンバー]
		return self.Row4Member

	def getRow5Member(self): #5件目 [メンバー]
		return self.Row5Member

	def getRow6Member(self): #6件目 [メンバー]
		return self.Row6Member

	def getRow7Member(self): #7件目 [メンバー]
		return self.Row7Member

	def getRow8Member(self): #8件目 [メンバー]
		return self.Row8Member

	def getRow9Member(self): #9件目 [メンバー]
		return self.Row9Member

	def getRow10Member(self): #10件目 [メンバー]
		return self.Row10Member

	def getRow11Member(self): #11件目 [メンバー]
		return self.Row11Member

	def getRow12Member(self): #12件目 [メンバー]
		return self.Row12Member

	def getRow13Member(self): #13件目 [メンバー]
		return self.Row13Member

	def getRow14Member(self): #14件目 [メンバー]
		return self.Row14Member

	def getRow15Member(self): #15件目 [メンバー]
		return self.Row15Member

	def getRow16Member(self): #16件目 [メンバー]
		return self.Row16Member

	def getRow17Member(self): #17件目 [メンバー]
		return self.Row17Member

	def getRow18Member(self): #18件目 [メンバー]
		return self.Row18Member

	def getRow19Member(self): #19件目 [メンバー]
		return self.Row19Member

	def getRow20Member(self): #20件目 [メンバー]
		return self.Row20Member

	def getRow21Member(self): #21件目 [メンバー]
		return self.Row21Member

	def getRow22Member(self): #22件目 [メンバー]
		return self.Row22Member

	def getRow23Member(self): #23件目 [メンバー]
		return self.Row23Member

	def getRow24Member(self): #24件目 [メンバー]
		return self.Row24Member

	def getRow25Member(self): #25件目 [メンバー]
		return self.Row25Member

	def getRow26Member(self): #26件目 [メンバー]
		return self.Row26Member

	def getRow27Member(self): #27件目 [メンバー]
		return self.Row27Member

	def getRow28Member(self): #28件目 [メンバー]
		return self.Row28Member

	def getRow29Member(self): #29件目 [メンバー]
		return self.Row29Member

	def getRow30Member(self): #30件目 [メンバー]
		return self.Row30Member

	def getRow31Member(self): #31件目 [メンバー]
		return self.Row31Member

	def getRow32Member(self): #32件目 [メンバー]
		return self.Row32Member

	def getRow33Member(self): #33件目 [メンバー]
		return self.Row33Member

	def getRow34Member(self): #34件目 [メンバー]
		return self.Row34Member

	def getRow35Member(self): #35件目 [メンバー]
		return self.Row35Member

	def getRow36Member(self): #36件目 [メンバー]
		return self.Row36Member

	def getRow37Member(self): #37件目 [メンバー]
		return self.Row37Member

	def getRow38Member(self): #38件目 [メンバー]
		return self.Row38Member

	def getRow39Member(self): #39件目 [メンバー]
		return self.Row39Member

	def getRow40Member(self): #40件目 [メンバー]
		return self.Row40Member

	def getRow41Member(self): #41件目 [メンバー]
		return self.Row41Member

	def getRow42Member(self): #42件目 [メンバー]
		return self.Row42Member

	def getRow43Member(self): #43件目 [メンバー]
		return self.Row43Member

	def getRow44Member(self): #44件目 [メンバー]
		return self.Row44Member

	def getRow45Member(self): #45件目 [メンバー]
		return self.Row45Member

	def getRow46Member(self): #46件目 [メンバー]
		return self.Row46Member

	def getRow47Member(self): #47件目 [メンバー]
		return self.Row47Member

	def getRow48Member(self): #48件目 [メンバー]
		return self.Row48Member

	def getRow49Member(self): #49件目 [メンバー]
		return self.Row49Member

	def getRow50Member(self): #50件目 [メンバー]
		return self.Row50Member

	def getRow51Member(self): #51件目 [メンバー]
		return self.Row51Member

	def getRow52Member(self): #52件目 [メンバー]
		return self.Row52Member

	def getRow53Member(self): #53件目 [メンバー]
		return self.Row53Member

	def getRow54Member(self): #54件目 [メンバー]
		return self.Row54Member

	def getRow55Member(self): #55件目 [メンバー]
		return self.Row55Member

	def getRow56Member(self): #56件目 [メンバー]
		return self.Row56Member

	def getRow57Member(self): #57件目 [メンバー]
		return self.Row57Member

	def getRow58Member(self): #58件目 [メンバー]
		return self.Row58Member

	def getRow59Member(self): #59件目 [メンバー]
		return self.Row59Member

	def getRow60Member(self): #60件目 [メンバー]
		return self.Row60Member

	def getDetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompanyLineItems(self): #保有目的が純投資目的以外の目的である特定投資株式の明細、最大保有会社 [表示項目]
		return self.DetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompanyLineItems

	def getNameOfSecuritiesDetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany(self): #銘柄、保有目的が純投資目的以外の目的である特定投資株式の明細、最大保有会社
		return self.NameOfSecuritiesDetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany

	def getNumberOfSharesHeldDetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany(self): #株式数、保有目的が純投資目的以外の目的である特定投資株式の明細、最大保有会社
		return self.NumberOfSharesHeldDetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany

	def getNumberOfSharesNotDisclosedAsBelowThresholdDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany(self): #株式数（記載省略）、保有目的が純投資目的以外の目的である特定投資株式の明細、最大保有会社
		return self.NumberOfSharesNotDisclosedAsBelowThresholdDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany

	def getBookValueDetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany(self): #貸借対照表計上額、保有目的が純投資目的以外の目的である特定投資株式の明細、最大保有会社
		return self.BookValueDetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany

	def getCarryingAmountNotDisclosedAsBelowThresholdDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany(self): #貸借対照表計上額（記載省略）、保有目的が純投資目的以外の目的である特定投資株式の明細、最大保有会社
		return self.CarryingAmountNotDisclosedAsBelowThresholdDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany

	def getPurposesOfHoldingDetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany(self): #保有目的、保有目的が純投資目的以外の目的である特定投資株式の明細、最大保有会社
		return self.PurposesOfHoldingDetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany

	def getQuantitativeEffectsOfShareholdingDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany(self): #定量的な保有効果、保有目的が純投資目的以外の目的である特定投資株式の明細、最大保有会社
		return self.QuantitativeEffectsOfShareholdingDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany

	def getReasonForIncreaseInNumberOfSharesDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany(self): #株式数が増加した理由、保有目的が純投資目的以外の目的である特定投資株式の明細、最大保有会社
		return self.ReasonForIncreaseInNumberOfSharesDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany

	def getPurposeOfShareholdingQuantitativeEffectsOfShareholdingAndReasonForIncreaseInNumberOfSharesDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany(self): #保有目的、定量的な保有効果及び株式数が増加した理由、保有目的が純投資目的以外の目的である特定投資株式の明細、最大保有会社
		return self.PurposeOfShareholdingQuantitativeEffectsOfShareholdingAndReasonForIncreaseInNumberOfSharesDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany

	def getWhetherIssuerOfAforementionedSharesHoldsReportingCompanysSharesDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany(self): #当該株式の発行者による提出会社の株式の保有の有無、保有目的が純投資目的以外の目的である特定投資株式の明細、最大保有会社
		return self.WhetherIssuerOfAforementionedSharesHoldsReportingCompanysSharesDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany

	def getShareholdingsHeading(self): #株式の保有状況 [目次項目]
		return self.ShareholdingsHeading

	def getGroupCompanyHoldingLargestAmountOfInvestmentEquitySecuritiesInGroupEquitySecuritiesHeldAbstract(self): #最大保有会社（提出会社でない場合）、株式の保有状況 [タイトル項目]
		return self.GroupCompanyHoldingLargestAmountOfInvestmentEquitySecuritiesInGroupEquitySecuritiesHeldAbstract

	def getDetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompanyTable(self): #保有目的が純投資目的以外の目的であるみなし保有株式の明細、最大保有会社 [表]
		return self.DetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompanyTable

	def getSequentialNumbersAxis(self): #連番 [軸]
		return self.SequentialNumbersAxis

	def getRow1Member(self): #1件目 [メンバー]
		return self.Row1Member

	def getRow2Member(self): #2件目 [メンバー]
		return self.Row2Member

	def getRow3Member(self): #3件目 [メンバー]
		return self.Row3Member

	def getRow4Member(self): #4件目 [メンバー]
		return self.Row4Member

	def getRow5Member(self): #5件目 [メンバー]
		return self.Row5Member

	def getRow6Member(self): #6件目 [メンバー]
		return self.Row6Member

	def getRow7Member(self): #7件目 [メンバー]
		return self.Row7Member

	def getRow8Member(self): #8件目 [メンバー]
		return self.Row8Member

	def getRow9Member(self): #9件目 [メンバー]
		return self.Row9Member

	def getRow10Member(self): #10件目 [メンバー]
		return self.Row10Member

	def getDetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompanyLineItems(self): #保有目的が純投資目的以外の目的であるみなし保有株式の明細、最大保有会社 [表示項目]
		return self.DetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompanyLineItems

	def getNameOfSecuritiesDetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany(self): #銘柄、保有目的が純投資目的以外の目的であるみなし保有株式の明細、最大保有会社
		return self.NameOfSecuritiesDetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany

	def getNumberOfSharesHeldDetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany(self): #株式数、保有目的が純投資目的以外の目的であるみなし保有株式の明細、最大保有会社
		return self.NumberOfSharesHeldDetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany

	def getNumberOfSharesNotDisclosedAsBelowThresholdDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany(self): #株式数（記載省略）、保有目的が純投資目的以外の目的であるみなし保有株式の明細、最大保有会社
		return self.NumberOfSharesNotDisclosedAsBelowThresholdDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany

	def getBookValueDetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany(self): #貸借対照表計上額、保有目的が純投資目的以外の目的であるみなし保有株式の明細、最大保有会社
		return self.BookValueDetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany

	def getCarryingAmountNotDisclosedAsBelowThresholdDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany(self): #貸借対照表計上額（記載省略）、保有目的が純投資目的以外の目的であるみなし保有株式の明細、最大保有会社
		return self.CarryingAmountNotDisclosedAsBelowThresholdDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany

	def getPurposesOfHoldingDetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany(self): #保有目的、保有目的が純投資目的以外の目的であるみなし保有株式の明細、最大保有会社
		return self.PurposesOfHoldingDetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany

	def getQuantitativeEffectsOfShareholdingDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany(self): #定量的な保有効果、保有目的が純投資目的以外の目的であるみなし保有株式の明細、最大保有会社
		return self.QuantitativeEffectsOfShareholdingDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany

	def getReasonForIncreaseInNumberOfSharesDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany(self): #株式数が増加した理由、保有目的が純投資目的以外の目的であるみなし保有株式の明細、最大保有会社
		return self.ReasonForIncreaseInNumberOfSharesDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany

	def getPurposeOfShareholdingQuantitativeEffectsOfShareholdingAndReasonForIncreaseInNumberOfSharesDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany(self): #保有目的、定量的な保有効果及び株式数が増加した理由、保有目的が純投資目的以外の目的であるみなし保有株式の明細、最大保有会社
		return self.PurposeOfShareholdingQuantitativeEffectsOfShareholdingAndReasonForIncreaseInNumberOfSharesDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany

	def getWhetherIssuerOfAforementionedSharesHoldsReportingCompanysSharesDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany(self): #当該株式の発行者による提出会社の株式の保有の有無、保有目的が純投資目的以外の目的であるみなし保有株式の明細、最大保有会社
		return self.WhetherIssuerOfAforementionedSharesHoldsReportingCompanysSharesDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany

	def getShareholdingsHeading(self): #株式の保有状況 [目次項目]
		return self.ShareholdingsHeading

	def getGroupCompanyHoldingLargestAmountOfInvestmentEquitySecuritiesInGroupEquitySecuritiesHeldAbstract(self): #最大保有会社（提出会社でない場合）、株式の保有状況 [タイトル項目]
		return self.GroupCompanyHoldingLargestAmountOfInvestmentEquitySecuritiesInGroupEquitySecuritiesHeldAbstract

	def getInvestmentEquitySecuritiesHeldForPureInvestmentLargestHoldingCompanyAbstract(self): #保有目的が純投資目的である投資株式、最大保有会社 [タイトル項目]
		return self.InvestmentEquitySecuritiesHeldForPureInvestmentLargestHoldingCompanyAbstract

	def getEquitySecuritiesNotListedInvestmentEquitySecuritiesHeldForPureInvestmentLargestHoldingCompanyAbstract(self): #非上場株式、保有目的が純投資目的である投資株式、最大保有会社 [タイトル項目]
		return self.EquitySecuritiesNotListedInvestmentEquitySecuritiesHeldForPureInvestmentLargestHoldingCompanyAbstract

	def getNumberOfIssuesSharesNotListedInvestmentSharesHeldForPureInvestmentLargestHoldingCompany(self): #銘柄数、非上場株式、保有目的が純投資目的である投資株式、最大保有会社
		return self.NumberOfIssuesSharesNotListedInvestmentSharesHeldForPureInvestmentLargestHoldingCompany

	def getBookValueEquitySecuritiesNotListedInvestmentEquitySecuritiesHeldForPureInvestmentLargestHoldingCompany(self): #貸借対照表計上額の合計額、非上場株式、保有目的が純投資目的である投資株式、最大保有会社
		return self.BookValueEquitySecuritiesNotListedInvestmentEquitySecuritiesHeldForPureInvestmentLargestHoldingCompany

	def getTotalOfDividendsReceivedEquitySecuritiesNotListedInvestmentEquitySecuritiesHeldForPureInvestmentLargestHoldingCompany(self): #受取配当金の合計額、非上場株式、保有目的が純投資目的である投資株式、最大保有会社
		return self.TotalOfDividendsReceivedEquitySecuritiesNotListedInvestmentEquitySecuritiesHeldForPureInvestmentLargestHoldingCompany

	def getTotalOfGainLossOnSaleEquitySecuritiesNotListedInvestmentEquitySecuritiesHeldForPureInvestmentLargestHoldingCompany(self): #売却損益の合計額、非上場株式、保有目的が純投資目的である投資株式、最大保有会社
		return self.TotalOfGainLossOnSaleEquitySecuritiesNotListedInvestmentEquitySecuritiesHeldForPureInvestmentLargestHoldingCompany

	def getTotalOfValuationGainLossEquitySecuritiesNotListedInvestmentEquitySecuritiesHeldForPureInvestmentLargestHoldingCompany(self): #評価損益の合計額、非上場株式、保有目的が純投資目的である投資株式、最大保有会社
		return self.TotalOfValuationGainLossEquitySecuritiesNotListedInvestmentEquitySecuritiesHeldForPureInvestmentLargestHoldingCompany

	def getEquitySecuritiesOtherThanThoseNotListedInvestmentEquitySecuritiesHeldForPureInvestmentLargestHoldingCompanyAbstract(self): #非上場株式以外の株式、保有目的が純投資目的である投資株式、最大保有会社 [タイトル項目]
		return self.EquitySecuritiesOtherThanThoseNotListedInvestmentEquitySecuritiesHeldForPureInvestmentLargestHoldingCompanyAbstract

	def getNumberOfIssuesSharesOtherThanThoseNotListedInvestmentSharesHeldForPureInvestmentLargestHoldingCompany(self): #銘柄数、非上場株式以外の株式、保有目的が純投資目的である投資株式、最大保有会社
		return self.NumberOfIssuesSharesOtherThanThoseNotListedInvestmentSharesHeldForPureInvestmentLargestHoldingCompany

	def getBookValueEquitySecuritiesOtherThanThoseNotListedInvestmentEquitySecuritiesHeldForPureInvestmentLargestHoldingCompany(self): #貸借対照表計上額の合計額、非上場株式以外の株式、保有目的が純投資目的である投資株式、最大保有会社
		return self.BookValueEquitySecuritiesOtherThanThoseNotListedInvestmentEquitySecuritiesHeldForPureInvestmentLargestHoldingCompany

	def getTotalOfDividendsReceivedEquitySecuritiesOtherThanThoseNotListedInvestmentEquitySecuritiesHeldForPureInvestmentLargestHoldingCompany(self): #受取配当金の合計額、非上場株式以外の株式、保有目的が純投資目的である投資株式、最大保有会社
		return self.TotalOfDividendsReceivedEquitySecuritiesOtherThanThoseNotListedInvestmentEquitySecuritiesHeldForPureInvestmentLargestHoldingCompany

	def getTotalOfGainLossOnSaleEquitySecuritiesOtherThanThoseNotListedInvestmentEquitySecuritiesHeldForPureInvestmentLargestHoldingCompany(self): #売却損益の合計額、非上場株式以外の株式、保有目的が純投資目的である投資株式、最大保有会社
		return self.TotalOfGainLossOnSaleEquitySecuritiesOtherThanThoseNotListedInvestmentEquitySecuritiesHeldForPureInvestmentLargestHoldingCompany

	def getTotalOfValuationGainLossEquitySecuritiesOtherThanThoseNotListedInvestmentEquitySecuritiesHeldForPureInvestmentLargestHoldingCompany(self): #評価損益の合計額、非上場株式以外の株式、保有目的が純投資目的である投資株式、最大保有会社
		return self.TotalOfValuationGainLossEquitySecuritiesOtherThanThoseNotListedInvestmentEquitySecuritiesHeldForPureInvestmentLargestHoldingCompany

	def getShareholdingsHeading(self): #株式の保有状況 [目次項目]
		return self.ShareholdingsHeading

	def getGroupCompanyHoldingLargestAmountOfInvestmentEquitySecuritiesInGroupEquitySecuritiesHeldAbstract(self): #最大保有会社（提出会社でない場合）、株式の保有状況 [タイトル項目]
		return self.GroupCompanyHoldingLargestAmountOfInvestmentEquitySecuritiesInGroupEquitySecuritiesHeldAbstract

	def getInvestmentEquitySecuritiesReclassifiedFromHeldForPureInvestmentToHeldForPurposesOtherThanPureInvestmentLargestHoldingCompanyTable(self): #投資株式の保有目的を純投資目的から純投資目的以外の目的に変更したもの、最大保有会社 [表]
		return self.InvestmentEquitySecuritiesReclassifiedFromHeldForPureInvestmentToHeldForPurposesOtherThanPureInvestmentLargestHoldingCompanyTable

	def getSequentialNumbersAxis(self): #連番 [軸]
		return self.SequentialNumbersAxis

	def getRow1Member(self): #1件目 [メンバー]
		return self.Row1Member

	def getRow2Member(self): #2件目 [メンバー]
		return self.Row2Member

	def getRow3Member(self): #3件目 [メンバー]
		return self.Row3Member

	def getInvestmentEquitySecuritiesReclassifiedFromHeldForPureInvestmentToHeldForPurposesOtherThanPureInvestmentLargestHoldingCompanyLineItems(self): #投資株式の保有目的を純投資目的から純投資目的以外の目的に変更したもの、最大保有会社 [表示項目]
		return self.InvestmentEquitySecuritiesReclassifiedFromHeldForPureInvestmentToHeldForPurposesOtherThanPureInvestmentLargestHoldingCompanyLineItems

	def getNameOfSecuritiesInvestmentEquitySecuritiesReclassifiedFromHeldForPureInvestmentToHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany(self): #銘柄、投資株式の保有目的を純投資目的から純投資目的以外の目的に変更したもの、最大保有会社
		return self.NameOfSecuritiesInvestmentEquitySecuritiesReclassifiedFromHeldForPureInvestmentToHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany

	def getNumberOfSharesHeldInvestmentEquitySecuritiesReclassifiedFromHeldForPureInvestmentToHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany(self): #株式数、投資株式の保有目的を純投資目的から純投資目的以外の目的に変更したもの、最大保有会社
		return self.NumberOfSharesHeldInvestmentEquitySecuritiesReclassifiedFromHeldForPureInvestmentToHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany

	def getBookValueInvestmentEquitySecuritiesReclassifiedFromHeldForPureInvestmentToHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany(self): #貸借対照表計上額、投資株式の保有目的を純投資目的から純投資目的以外の目的に変更したもの、最大保有会社
		return self.BookValueInvestmentEquitySecuritiesReclassifiedFromHeldForPureInvestmentToHeldForPurposesOtherThanPureInvestmentLargestHoldingCompany

	def getShareholdingsHeading(self): #株式の保有状況 [目次項目]
		return self.ShareholdingsHeading

	def getGroupCompanyHoldingLargestAmountOfInvestmentEquitySecuritiesInGroupEquitySecuritiesHeldAbstract(self): #最大保有会社（提出会社でない場合）、株式の保有状況 [タイトル項目]
		return self.GroupCompanyHoldingLargestAmountOfInvestmentEquitySecuritiesInGroupEquitySecuritiesHeldAbstract

	def getInvestmentEquitySecuritiesReclassifiedFromHeldForPurposesOtherThanPureInvestmentToHeldForPureInvestmentLargestHoldingCompanyTable(self): #投資株式の保有目的を純投資以外の目的から純投資目的に変更したもの、最大保有会社 [表]
		return self.InvestmentEquitySecuritiesReclassifiedFromHeldForPurposesOtherThanPureInvestmentToHeldForPureInvestmentLargestHoldingCompanyTable

	def getSequentialNumbersAxis(self): #連番 [軸]
		return self.SequentialNumbersAxis

	def getRow1Member(self): #1件目 [メンバー]
		return self.Row1Member

	def getRow2Member(self): #2件目 [メンバー]
		return self.Row2Member

	def getRow3Member(self): #3件目 [メンバー]
		return self.Row3Member

	def getInvestmentEquitySecuritiesReclassifiedFromHeldForPurposesOtherThanPureInvestmentToHeldForPureInvestmentLargestHoldingCompanyLineItems(self): #投資株式の保有目的を純投資以外の目的から純投資目的に変更したもの、最大保有会社 [表示項目]
		return self.InvestmentEquitySecuritiesReclassifiedFromHeldForPurposesOtherThanPureInvestmentToHeldForPureInvestmentLargestHoldingCompanyLineItems

	def getNameOfSecuritiesInvestmentEquitySecuritiesReclassifiedFromHeldForPurposesOtherThanPureInvestmentToHeldForPureInvestmentLargestHoldingCompany(self): #銘柄、投資株式の保有目的を純投資以外の目的から純投資目的に変更したもの、最大保有会社
		return self.NameOfSecuritiesInvestmentEquitySecuritiesReclassifiedFromHeldForPurposesOtherThanPureInvestmentToHeldForPureInvestmentLargestHoldingCompany

	def getNumberOfSharesHeldInvestmentEquitySecuritiesReclassifiedFromHeldForPurposesOtherThanPureInvestmentToHeldForPureInvestmentLargestHoldingCompany(self): #株式数、投資株式の保有目的を純投資以外の目的から純投資目的に変更したもの、最大保有会社
		return self.NumberOfSharesHeldInvestmentEquitySecuritiesReclassifiedFromHeldForPurposesOtherThanPureInvestmentToHeldForPureInvestmentLargestHoldingCompany

	def getBookValueInvestmentEquitySecuritiesReclassifiedFromHeldForPurposesOtherThanPureInvestmentToHeldForPureInvestmentLargestHoldingCompany(self): #貸借対照表計上額、投資株式の保有目的を純投資以外の目的から純投資目的に変更したもの、最大保有会社
		return self.BookValueInvestmentEquitySecuritiesReclassifiedFromHeldForPurposesOtherThanPureInvestmentToHeldForPureInvestmentLargestHoldingCompany

	def getShareholdingsHeading(self): #株式の保有状況 [目次項目]
		return self.ShareholdingsHeading

	def getGroupCompanyHoldingSecondLargestAmountOfInvestmentEquitySecuritiesInGroupEquitySecuritiesHeldAbstract(self): #投資株式計上額が次に大きい会社（提出会社でない場合）、株式の保有状況 [タイトル項目]
		return self.GroupCompanyHoldingSecondLargestAmountOfInvestmentEquitySecuritiesInGroupEquitySecuritiesHeldAbstract

	def getInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompanyAbstract(self): #保有目的が純投資目的以外の目的である投資株式、投資株式計上額が次に大きい会社 [タイトル項目]
		return self.InvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompanyAbstract

	def getSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompanyAbstract(self): #非上場株式、保有目的が純投資目的以外の目的である投資株式、投資株式計上額が次に大きい会社 [タイトル項目]
		return self.SharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompanyAbstract

	def getNumberOfIssuesSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany(self): #銘柄数、非上場株式、保有目的が純投資目的以外の目的である投資株式、投資株式計上額が次に大きい会社
		return self.NumberOfIssuesSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany

	def getCarryingAmountSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany(self): #貸借対照表計上額、非上場株式、保有目的が純投資目的以外の目的である投資株式、投資株式計上額が次に大きい会社
		return self.CarryingAmountSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany

	def getNumberOfIssuesWhoseNumberOfSharesIncreasedSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany(self): #株式数が増加した銘柄数、非上場株式、保有目的が純投資目的以外の目的である投資株式、投資株式計上額が次に大きい会社
		return self.NumberOfIssuesWhoseNumberOfSharesIncreasedSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany

	def getTotalAcquisitionCostForIncreasedSharesSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany(self): #株式数の増加に係る取得価額の合計額、非上場株式、保有目的が純投資目的以外の目的である投資株式、投資株式計上額が次に大きい会社
		return self.TotalAcquisitionCostForIncreasedSharesSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany

	def getReasonForIncreaseInNumberOfSharesSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany(self): #株式数が増加した理由、非上場株式、保有目的が純投資目的以外の目的である投資株式、投資株式計上額が次に大きい会社
		return self.ReasonForIncreaseInNumberOfSharesSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany

	def getNumberOfIssuesWhoseNumberOfSharesDecreasedSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany(self): #株式数が減少した銘柄数、非上場株式、保有目的が純投資目的以外の目的である投資株式、投資株式計上額が次に大きい会社
		return self.NumberOfIssuesWhoseNumberOfSharesDecreasedSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany

	def getTotalSaleAmountForDecreasedSharesSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany(self): #株式数の減少に係る売却価額の合計額、非上場株式、保有目的が純投資目的以外の目的である投資株式、投資株式計上額が次に大きい会社
		return self.TotalSaleAmountForDecreasedSharesSharesNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany

	def getSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompanyAbstract(self): #非上場株式以外の株式、保有目的が純投資目的以外の目的である投資株式、投資株式計上額が次に大きい会社 [タイトル項目]
		return self.SharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompanyAbstract

	def getNumberOfIssuesSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany(self): #銘柄数、非上場株式以外の株式、保有目的が純投資目的以外の目的である投資株式、投資株式計上額が次に大きい会社
		return self.NumberOfIssuesSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany

	def getCarryingAmountSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany(self): #貸借対照表計上額、非上場株式以外の株式、保有目的が純投資目的以外の目的である投資株式、投資株式計上額が次に大きい会社
		return self.CarryingAmountSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany

	def getNumberOfIssuesWhoseNumberOfSharesIncreasedSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany(self): #株式数が増加した銘柄数、非上場株式以外の株式、保有目的が純投資目的以外の目的である投資株式、投資株式計上額が次に大きい会社
		return self.NumberOfIssuesWhoseNumberOfSharesIncreasedSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany

	def getTotalAcquisitionCostForIncreasedSharesSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany(self): #株式数の増加に係る取得価額の合計額、非上場株式以外の株式、保有目的が純投資目的以外の目的である投資株式、投資株式計上額が次に大きい会社
		return self.TotalAcquisitionCostForIncreasedSharesSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany

	def getReasonForIncreaseInNumberOfSharesSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany(self): #株式数が増加した理由、非上場株式以外の株式、保有目的が純投資目的以外の目的である投資株式、投資株式計上額が次に大きい会社
		return self.ReasonForIncreaseInNumberOfSharesSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany

	def getNumberOfIssuesWhoseNumberOfSharesDecreasedSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany(self): #株式数が減少した銘柄数、非上場株式以外の株式、保有目的が純投資目的以外の目的である投資株式、投資株式計上額が次に大きい会社
		return self.NumberOfIssuesWhoseNumberOfSharesDecreasedSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany

	def getTotalSaleAmountForDecreasedSharesSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany(self): #株式数の減少に係る売却価額の合計額、非上場株式以外の株式、保有目的が純投資目的以外の目的である投資株式、投資株式計上額が次に大きい会社
		return self.TotalSaleAmountForDecreasedSharesSharesOtherThanThoseNotListedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany

	def getShareholdingsHeading(self): #株式の保有状況 [目次項目]
		return self.ShareholdingsHeading

	def getGroupCompanyHoldingSecondLargestAmountOfInvestmentEquitySecuritiesInGroupEquitySecuritiesHeldAbstract(self): #投資株式計上額が次に大きい会社（提出会社でない場合）、株式の保有状況 [タイトル項目]
		return self.GroupCompanyHoldingSecondLargestAmountOfInvestmentEquitySecuritiesInGroupEquitySecuritiesHeldAbstract

	def getDetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompanyTable(self): #保有目的が純投資目的以外の目的である特定投資株式の明細、投資株式計上額が次に大きい会社 [表]
		return self.DetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompanyTable

	def getSequentialNumbersAxis(self): #連番 [軸]
		return self.SequentialNumbersAxis

	def getRow1Member(self): #1件目 [メンバー]
		return self.Row1Member

	def getRow2Member(self): #2件目 [メンバー]
		return self.Row2Member

	def getRow3Member(self): #3件目 [メンバー]
		return self.Row3Member

	def getRow4Member(self): #4件目 [メンバー]
		return self.Row4Member

	def getRow5Member(self): #5件目 [メンバー]
		return self.Row5Member

	def getRow6Member(self): #6件目 [メンバー]
		return self.Row6Member

	def getRow7Member(self): #7件目 [メンバー]
		return self.Row7Member

	def getRow8Member(self): #8件目 [メンバー]
		return self.Row8Member

	def getRow9Member(self): #9件目 [メンバー]
		return self.Row9Member

	def getRow10Member(self): #10件目 [メンバー]
		return self.Row10Member

	def getDetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompanyLineItems(self): #保有目的が純投資目的以外の目的である特定投資株式の明細、投資株式計上額が次に大きい会社 [表示項目]
		return self.DetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompanyLineItems

	def getNameOfSecuritiesDetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany(self): #銘柄、保有目的が純投資目的以外の目的である特定投資株式の明細、投資株式計上額が次に大きい会社
		return self.NameOfSecuritiesDetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany

	def getNumberOfSharesHeldDetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany(self): #株式数、保有目的が純投資目的以外の目的である特定投資株式の明細、投資株式計上額が次に大きい会社
		return self.NumberOfSharesHeldDetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany

	def getNumberOfSharesNotDisclosedAsBelowThresholdDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany(self): #株式数（記載省略）、保有目的が純投資目的以外の目的である特定投資株式の明細、投資株式計上額が次に大きい会社
		return self.NumberOfSharesNotDisclosedAsBelowThresholdDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany

	def getBookValueDetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany(self): #貸借対照表計上額、保有目的が純投資目的以外の目的である特定投資株式の明細、投資株式計上額が次に大きい会社
		return self.BookValueDetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany

	def getCarryingAmountNotDisclosedAsBelowThresholdDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany(self): #貸借対照表計上額（記載省略）、保有目的が純投資目的以外の目的である特定投資株式の明細、投資株式計上額が次に大きい会社
		return self.CarryingAmountNotDisclosedAsBelowThresholdDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany

	def getPurposesOfHoldingDetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany(self): #保有目的、保有目的が純投資目的以外の目的である特定投資株式の明細、投資株式計上額が次に大きい会社
		return self.PurposesOfHoldingDetailsOfSpecifiedInvestmentEquitySecuritiesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany

	def getQuantitativeEffectsOfShareholdingDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany(self): #定量的な保有効果、保有目的が純投資目的以外の目的である特定投資株式の明細、投資株式計上額が次に大きい会社
		return self.QuantitativeEffectsOfShareholdingDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany

	def getReasonForIncreaseInNumberOfSharesDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany(self): #株式数が増加した理由、保有目的が純投資目的以外の目的である特定投資株式の明細、投資株式計上額が次に大きい会社
		return self.ReasonForIncreaseInNumberOfSharesDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany

	def getPurposeOfShareholdingQuantitativeEffectsOfShareholdingAndReasonForIncreaseInNumberOfSharesDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany(self): #保有目的、定量的な保有効果及び株式数が増加した理由、保有目的が純投資目的以外の目的である特定投資株式の明細、投資株式計上額が次に大きい会社
		return self.PurposeOfShareholdingQuantitativeEffectsOfShareholdingAndReasonForIncreaseInNumberOfSharesDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany

	def getWhetherIssuerOfAforementionedSharesHoldsReportingCompanysSharesDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany(self): #当該株式の発行者による提出会社の株式の保有の有無、保有目的が純投資目的以外の目的である特定投資株式の明細、投資株式計上額が次に大きい会社
		return self.WhetherIssuerOfAforementionedSharesHoldsReportingCompanysSharesDetailsOfSpecifiedInvestmentSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany

	def getShareholdingsHeading(self): #株式の保有状況 [目次項目]
		return self.ShareholdingsHeading

	def getGroupCompanyHoldingSecondLargestAmountOfInvestmentEquitySecuritiesInGroupEquitySecuritiesHeldAbstract(self): #投資株式計上額が次に大きい会社（提出会社でない場合）、株式の保有状況 [タイトル項目]
		return self.GroupCompanyHoldingSecondLargestAmountOfInvestmentEquitySecuritiesInGroupEquitySecuritiesHeldAbstract

	def getDetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompanyTable(self): #保有目的が純投資目的以外の目的であるみなし保有株式の明細、投資株式計上額が次に大きい会社 [表]
		return self.DetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompanyTable

	def getSequentialNumbersAxis(self): #連番 [軸]
		return self.SequentialNumbersAxis

	def getRow1Member(self): #1件目 [メンバー]
		return self.Row1Member

	def getRow2Member(self): #2件目 [メンバー]
		return self.Row2Member

	def getRow3Member(self): #3件目 [メンバー]
		return self.Row3Member

	def getRow4Member(self): #4件目 [メンバー]
		return self.Row4Member

	def getRow5Member(self): #5件目 [メンバー]
		return self.Row5Member

	def getRow6Member(self): #6件目 [メンバー]
		return self.Row6Member

	def getRow7Member(self): #7件目 [メンバー]
		return self.Row7Member

	def getRow8Member(self): #8件目 [メンバー]
		return self.Row8Member

	def getRow9Member(self): #9件目 [メンバー]
		return self.Row9Member

	def getRow10Member(self): #10件目 [メンバー]
		return self.Row10Member

	def getDetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompanyLineItems(self): #保有目的が純投資目的以外の目的であるみなし保有株式の明細、投資株式計上額が次に大きい会社 [表示項目]
		return self.DetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompanyLineItems

	def getNameOfSecuritiesDetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany(self): #銘柄、保有目的が純投資目的以外の目的であるみなし保有株式の明細、投資株式計上額が次に大きい会社
		return self.NameOfSecuritiesDetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany

	def getNumberOfSharesHeldDetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany(self): #株式数、保有目的が純投資目的以外の目的であるみなし保有株式の明細、投資株式計上額が次に大きい会社
		return self.NumberOfSharesHeldDetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany

	def getNumberOfSharesNotDisclosedAsBelowThresholdDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany(self): #株式数（記載省略）、保有目的が純投資目的以外の目的であるみなし保有株式の明細、投資株式計上額が次に大きい会社
		return self.NumberOfSharesNotDisclosedAsBelowThresholdDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany

	def getBookValueDetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany(self): #貸借対照表計上額、保有目的が純投資目的以外の目的であるみなし保有株式の明細、投資株式計上額が次に大きい会社
		return self.BookValueDetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany

	def getCarryingAmountNotDisclosedAsBelowThresholdDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany(self): #貸借対照表計上額（記載省略）、保有目的が純投資目的以外の目的であるみなし保有株式の明細、投資株式計上額が次に大きい会社
		return self.CarryingAmountNotDisclosedAsBelowThresholdDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany

	def getPurposesOfHoldingDetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany(self): #保有目的、保有目的が純投資目的以外の目的であるみなし保有株式の明細、投資株式計上額が次に大きい会社
		return self.PurposesOfHoldingDetailsOfDeemedHoldingsOfEquitySecuritiesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany

	def getQuantitativeEffectsOfShareholdingDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany(self): #定量的な保有効果、保有目的が純投資目的以外の目的であるみなし保有株式の明細、投資株式計上額が次に大きい会社
		return self.QuantitativeEffectsOfShareholdingDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany

	def getReasonForIncreaseInNumberOfSharesDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany(self): #株式数が増加した理由、保有目的が純投資目的以外の目的であるみなし保有株式の明細、投資株式計上額が次に大きい会社
		return self.ReasonForIncreaseInNumberOfSharesDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany

	def getPurposeOfShareholdingQuantitativeEffectsOfShareholdingAndReasonForIncreaseInNumberOfSharesDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany(self): #保有目的、定量的な保有効果及び株式数が増加した理由、保有目的が純投資目的以外の目的であるみなし保有株式の明細、投資株式計上額が次に大きい会社
		return self.PurposeOfShareholdingQuantitativeEffectsOfShareholdingAndReasonForIncreaseInNumberOfSharesDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany

	def getWhetherIssuerOfAforementionedSharesHoldsReportingCompanysSharesDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany(self): #当該株式の発行者による提出会社の株式の保有の有無、保有目的が純投資目的以外の目的であるみなし保有株式の明細、投資株式計上額が次に大きい会社
		return self.WhetherIssuerOfAforementionedSharesHoldsReportingCompanysSharesDetailsOfDeemedHoldingsOfSharesHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany

	def getShareholdingsHeading(self): #株式の保有状況 [目次項目]
		return self.ShareholdingsHeading

	def getGroupCompanyHoldingSecondLargestAmountOfInvestmentEquitySecuritiesInGroupEquitySecuritiesHeldAbstract(self): #投資株式計上額が次に大きい会社（提出会社でない場合）、株式の保有状況 [タイトル項目]
		return self.GroupCompanyHoldingSecondLargestAmountOfInvestmentEquitySecuritiesInGroupEquitySecuritiesHeldAbstract

	def getInvestmentEquitySecuritiesHeldForPureInvestmentSecondLargestHoldingCompanyAbstract(self): #保有目的が純投資目的である投資株式、投資株式計上額が次に大きい会社 [タイトル項目]
		return self.InvestmentEquitySecuritiesHeldForPureInvestmentSecondLargestHoldingCompanyAbstract

	def getEquitySecuritiesNotListedInvestmentEquitySecuritiesHeldForPureInvestmentSecondLargestHoldingCompanyAbstract(self): #非上場株式、保有目的が純投資目的である投資株式、投資株式計上額が次に大きい会社 [タイトル項目]
		return self.EquitySecuritiesNotListedInvestmentEquitySecuritiesHeldForPureInvestmentSecondLargestHoldingCompanyAbstract

	def getNumberOfIssuesSharesNotListedInvestmentSharesHeldForPureInvestmentSecondLargestHoldingCompany(self): #銘柄数、非上場株式、保有目的が純投資目的である投資株式、投資株式計上額が次に大きい会社
		return self.NumberOfIssuesSharesNotListedInvestmentSharesHeldForPureInvestmentSecondLargestHoldingCompany

	def getBookValueEquitySecuritiesNotListedInvestmentEquitySecuritiesHeldForPureInvestmentSecondLargestHoldingCompany(self): #貸借対照表計上額の合計額、非上場株式、保有目的が純投資目的である投資株式、投資株式計上額が次に大きい会社
		return self.BookValueEquitySecuritiesNotListedInvestmentEquitySecuritiesHeldForPureInvestmentSecondLargestHoldingCompany

	def getTotalOfDividendsReceivedEquitySecuritiesNotListedInvestmentEquitySecuritiesHeldForPureInvestmentSecondLargestHoldingCompany(self): #受取配当金の合計額、非上場株式、保有目的が純投資目的である投資株式、投資株式計上額が次に大きい会社
		return self.TotalOfDividendsReceivedEquitySecuritiesNotListedInvestmentEquitySecuritiesHeldForPureInvestmentSecondLargestHoldingCompany

	def getTotalOfGainLossOnSaleEquitySecuritiesNotListedInvestmentEquitySecuritiesHeldForPureInvestmentSecondLargestHoldingCompany(self): #売却損益の合計額、非上場株式、保有目的が純投資目的である投資株式、投資株式計上額が次に大きい会社
		return self.TotalOfGainLossOnSaleEquitySecuritiesNotListedInvestmentEquitySecuritiesHeldForPureInvestmentSecondLargestHoldingCompany

	def getTotalOfValuationGainLossEquitySecuritiesNotListedInvestmentEquitySecuritiesHeldForPureInvestmentSecondLargestHoldingCompany(self): #評価損益の合計額、非上場株式、保有目的が純投資目的である投資株式、投資株式計上額が次に大きい会社
		return self.TotalOfValuationGainLossEquitySecuritiesNotListedInvestmentEquitySecuritiesHeldForPureInvestmentSecondLargestHoldingCompany

	def getEquitySecuritiesOtherThanThoseNotListedInvestmentEquitySecuritiesHeldForPureInvestmentSecondLargestHoldingCompanyAbstract(self): #非上場株式以外の株式、保有目的が純投資目的である投資株式、投資株式計上額が次に大きい会社 [タイトル項目]
		return self.EquitySecuritiesOtherThanThoseNotListedInvestmentEquitySecuritiesHeldForPureInvestmentSecondLargestHoldingCompanyAbstract

	def getNumberOfIssuesSharesOtherThanThoseNotListedInvestmentSharesHeldForPureInvestmentSecondLargestHoldingCompany(self): #銘柄数、非上場株式以外の株式、保有目的が純投資目的である投資株式、投資株式計上額が次に大きい会社
		return self.NumberOfIssuesSharesOtherThanThoseNotListedInvestmentSharesHeldForPureInvestmentSecondLargestHoldingCompany

	def getBookValueEquitySecuritiesOtherThanThoseNotListedInvestmentEquitySecuritiesHeldForPureInvestmentSecondLargestHoldingCompany(self): #貸借対照表計上額の合計額、非上場株式以外の株式、保有目的が純投資目的である投資株式、投資株式計上額が次に大きい会社
		return self.BookValueEquitySecuritiesOtherThanThoseNotListedInvestmentEquitySecuritiesHeldForPureInvestmentSecondLargestHoldingCompany

	def getTotalOfDividendsReceivedEquitySecuritiesOtherThanThoseNotListedInvestmentEquitySecuritiesHeldForPureInvestmentSecondLargestHoldingCompany(self): #受取配当金の合計額、非上場株式以外の株式、保有目的が純投資目的である投資株式、投資株式計上額が次に大きい会社
		return self.TotalOfDividendsReceivedEquitySecuritiesOtherThanThoseNotListedInvestmentEquitySecuritiesHeldForPureInvestmentSecondLargestHoldingCompany

	def getTotalOfGainLossOnSaleEquitySecuritiesOtherThanThoseNotListedInvestmentEquitySecuritiesHeldForPureInvestmentSecondLargestHoldingCompany(self): #売却損益の合計額、非上場株式以外の株式、保有目的が純投資目的である投資株式、投資株式計上額が次に大きい会社
		return self.TotalOfGainLossOnSaleEquitySecuritiesOtherThanThoseNotListedInvestmentEquitySecuritiesHeldForPureInvestmentSecondLargestHoldingCompany

	def getTotalOfValuationGainLossEquitySecuritiesOtherThanThoseNotListedInvestmentEquitySecuritiesHeldForPureInvestmentSecondLargestHoldingCompany(self): #評価損益の合計額、非上場株式以外の株式、保有目的が純投資目的である投資株式、投資株式計上額が次に大きい会社
		return self.TotalOfValuationGainLossEquitySecuritiesOtherThanThoseNotListedInvestmentEquitySecuritiesHeldForPureInvestmentSecondLargestHoldingCompany

	def getShareholdingsHeading(self): #株式の保有状況 [目次項目]
		return self.ShareholdingsHeading

	def getGroupCompanyHoldingSecondLargestAmountOfInvestmentEquitySecuritiesInGroupEquitySecuritiesHeldAbstract(self): #投資株式計上額が次に大きい会社（提出会社でない場合）、株式の保有状況 [タイトル項目]
		return self.GroupCompanyHoldingSecondLargestAmountOfInvestmentEquitySecuritiesInGroupEquitySecuritiesHeldAbstract

	def getInvestmentEquitySecuritiesReclassifiedFromHeldForPureInvestmentToHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompanyTable(self): #投資株式の保有目的を純投資目的から純投資目的以外の目的に変更したもの、投資株式計上額が次に大きい会社 [表]
		return self.InvestmentEquitySecuritiesReclassifiedFromHeldForPureInvestmentToHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompanyTable

	def getSequentialNumbersAxis(self): #連番 [軸]
		return self.SequentialNumbersAxis

	def getRow1Member(self): #1件目 [メンバー]
		return self.Row1Member

	def getRow2Member(self): #2件目 [メンバー]
		return self.Row2Member

	def getRow3Member(self): #3件目 [メンバー]
		return self.Row3Member

	def getInvestmentEquitySecuritiesReclassifiedFromHeldForPureInvestmentToHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompanyLineItems(self): #投資株式の保有目的を純投資目的から純投資目的以外の目的に変更したもの、投資株式計上額が次に大きい会社 [表示項目]
		return self.InvestmentEquitySecuritiesReclassifiedFromHeldForPureInvestmentToHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompanyLineItems

	def getNameOfSecuritiesInvestmentEquitySecuritiesReclassifiedFromHeldForPureInvestmentToHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany(self): #銘柄、投資株式の保有目的を純投資目的から純投資目的以外の目的に変更したもの、投資株式計上額が次に大きい会社
		return self.NameOfSecuritiesInvestmentEquitySecuritiesReclassifiedFromHeldForPureInvestmentToHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany

	def getNumberOfSharesHeldInvestmentEquitySecuritiesReclassifiedFromHeldForPureInvestmentToHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany(self): #株式数、投資株式の保有目的を純投資目的から純投資目的以外の目的に変更したもの、投資株式計上額が次に大きい会社
		return self.NumberOfSharesHeldInvestmentEquitySecuritiesReclassifiedFromHeldForPureInvestmentToHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany

	def getBookValueInvestmentEquitySecuritiesReclassifiedFromHeldForPureInvestmentToHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany(self): #貸借対照表計上額、投資株式の保有目的を純投資目的から純投資目的以外の目的に変更したもの、投資株式計上額が次に大きい会社
		return self.BookValueInvestmentEquitySecuritiesReclassifiedFromHeldForPureInvestmentToHeldForPurposesOtherThanPureInvestmentSecondLargestHoldingCompany

	def getShareholdingsHeading(self): #株式の保有状況 [目次項目]
		return self.ShareholdingsHeading

	def getGroupCompanyHoldingSecondLargestAmountOfInvestmentEquitySecuritiesInGroupEquitySecuritiesHeldAbstract(self): #投資株式計上額が次に大きい会社（提出会社でない場合）、株式の保有状況 [タイトル項目]
		return self.GroupCompanyHoldingSecondLargestAmountOfInvestmentEquitySecuritiesInGroupEquitySecuritiesHeldAbstract

	def getInvestmentEquitySecuritiesReclassifiedFromHeldForPurposesOtherThanPureInvestmentToHeldForPureInvestmentSecondLargestHoldingCompanyTable(self): #投資株式の保有目的を純投資以外の目的から純投資目的に変更したもの、投資株式計上額が次に大きい会社 [表]
		return self.InvestmentEquitySecuritiesReclassifiedFromHeldForPurposesOtherThanPureInvestmentToHeldForPureInvestmentSecondLargestHoldingCompanyTable

	def getSequentialNumbersAxis(self): #連番 [軸]
		return self.SequentialNumbersAxis

	def getRow1Member(self): #1件目 [メンバー]
		return self.Row1Member

	def getRow2Member(self): #2件目 [メンバー]
		return self.Row2Member

	def getRow3Member(self): #3件目 [メンバー]
		return self.Row3Member

	def getInvestmentEquitySecuritiesReclassifiedFromHeldForPurposesOtherThanPureInvestmentToHeldForPureInvestmentSecondLargestHoldingCompanyLineItems(self): #投資株式の保有目的を純投資以外の目的から純投資目的に変更したもの、投資株式計上額が次に大きい会社 [表示項目]
		return self.InvestmentEquitySecuritiesReclassifiedFromHeldForPurposesOtherThanPureInvestmentToHeldForPureInvestmentSecondLargestHoldingCompanyLineItems

	def getNameOfSecuritiesInvestmentEquitySecuritiesReclassifiedFromHeldForPurposesOtherThanPureInvestmentToHeldForPureInvestmentSecondLargestHoldingCompany(self): #銘柄、投資株式の保有目的を純投資以外の目的から純投資目的に変更したもの、投資株式計上額が次に大きい会社
		return self.NameOfSecuritiesInvestmentEquitySecuritiesReclassifiedFromHeldForPurposesOtherThanPureInvestmentToHeldForPureInvestmentSecondLargestHoldingCompany

	def getNumberOfSharesHeldInvestmentEquitySecuritiesReclassifiedFromHeldForPurposesOtherThanPureInvestmentToHeldForPureInvestmentSecondLargestHoldingCompany(self): #株式数、投資株式の保有目的を純投資以外の目的から純投資目的に変更したもの、投資株式計上額が次に大きい会社
		return self.NumberOfSharesHeldInvestmentEquitySecuritiesReclassifiedFromHeldForPurposesOtherThanPureInvestmentToHeldForPureInvestmentSecondLargestHoldingCompany

	def getBookValueInvestmentEquitySecuritiesReclassifiedFromHeldForPurposesOtherThanPureInvestmentToHeldForPureInvestmentSecondLargestHoldingCompany(self): #貸借対照表計上額、投資株式の保有目的を純投資以外の目的から純投資目的に変更したもの、投資株式計上額が次に大きい会社
		return self.BookValueInvestmentEquitySecuritiesReclassifiedFromHeldForPurposesOtherThanPureInvestmentToHeldForPureInvestmentSecondLargestHoldingCompany

	def getNameOfGroupCompanyHoldingLargestAmountOfInvestmentSharesInGroup(self): #最大保有会社（提出会社でない場合）の名称
		return self.NameOfGroupCompanyHoldingLargestAmountOfInvestmentSharesInGroup

	def getNameOfGroupCompanyHoldingSecondLargestAmountOfInvestmentSharesInGroup(self): #投資株式計上額が次に大きい会社（提出会社でない場合）の名称
		return self.NameOfGroupCompanyHoldingSecondLargestAmountOfInvestmentSharesInGroup

	def getFinancialInformationHeading(self): #経理の状況 [目次項目]
		return self.FinancialInformationHeading

	def getFinancialInformationHeading(self): #経理の状況 [目次項目]
		return self.FinancialInformationHeading

	def getRegulationsInAccordanceWithWhichConsolidatedFinancialStatementsHaveBeenPreparedFinancialInformation(self): #連結財務諸表が基づく規則、経理の状況
		return self.RegulationsInAccordanceWithWhichConsolidatedFinancialStatementsHaveBeenPreparedFinancialInformation

	def getRegulationsInAccordanceWithWhichFinancialStatementsHaveBeenPreparedFinancialInformation(self): #財務諸表が基づく規則、経理の状況
		return self.RegulationsInAccordanceWithWhichFinancialStatementsHaveBeenPreparedFinancialInformation

	def getDescriptionOfFactThatCompanyEngagesSpecifiedBusinessAndHasPreparedItsSemiAnnualConsolidatedFinancialStatementsFinancialInformation(self): #特定事業会社であり、中間連結財務諸表等を作成した場合の記載、経理の状況
		return self.DescriptionOfFactThatCompanyEngagesSpecifiedBusinessAndHasPreparedItsSemiAnnualConsolidatedFinancialStatementsFinancialInformation

	def getDescriptionOfFactThatConsolidatedFinancialStatementsHaveBeenPreparedInAccordanceWithSpecialOrdinanceOrRegulationsForIndustryInAppendedListFinancialInformation(self): #連結財務諸表が別記事業の特別の法令若しくは準則に基づく場合の記載、経理の状況
		return self.DescriptionOfFactThatConsolidatedFinancialStatementsHaveBeenPreparedInAccordanceWithSpecialOrdinanceOrRegulationsForIndustryInAppendedListFinancialInformation

	def getDescriptionOfFactThatFinancialStatementsHaveBeenPreparedInAccordanceWithSpecialOrdinanceOrRegulationsForIndustryInAppendedListFinancialInformation(self): #財務諸表が別記事業の特別の法令若しくは準則に基づく場合の記載、経理の状況
		return self.DescriptionOfFactThatFinancialStatementsHaveBeenPreparedInAccordanceWithSpecialOrdinanceOrRegulationsForIndustryInAppendedListFinancialInformation

	def getDescriptionOfFactThatConsolidatedFinancialStatementsHaveBeenPreparedInAccordanceWithIFRSFinancialInformation(self): #指定国際会計基準により連結財務諸表を作成した場合の記載、経理の状況
		return self.DescriptionOfFactThatConsolidatedFinancialStatementsHaveBeenPreparedInAccordanceWithIFRSFinancialInformation

	def getDescriptionOfFactThatConsolidatedFinancialStatementsHaveBeenPreparedInAccordanceWithJMISFinancialInformation(self): #修正国際基準により連結財務諸表を作成した場合の記載、経理の状況
		return self.DescriptionOfFactThatConsolidatedFinancialStatementsHaveBeenPreparedInAccordanceWithJMISFinancialInformation

	def getDescriptionOfFactThatConsolidatedFinancialStatementsHaveBeenPreparedInAccordanceWithUSGAAPFinancialInformation(self): #米国会計基準により連結財務諸表を作成した場合の記載、経理の状況
		return self.DescriptionOfFactThatConsolidatedFinancialStatementsHaveBeenPreparedInAccordanceWithUSGAAPFinancialInformation

	def getDescriptionOfFactThatConsolidatedFinancialStatementsHaveNotBeenPreparedFinancialInformation(self): #連結財務諸表を作成していない場合の記載、経理の状況
		return self.DescriptionOfFactThatConsolidatedFinancialStatementsHaveNotBeenPreparedFinancialInformation

	def getDescriptionOfFactThatConsolidatedFinancialStatementsHaveNotBeenPreparedAndFinancialStatementsHaveBeenPreparedInAccordanceWithIFRSFinancialInformation(self): #連結財務諸表を作成していない場合で指定国際会計基準により財務諸表を作成する場合の記載、経理の状況
		return self.DescriptionOfFactThatConsolidatedFinancialStatementsHaveNotBeenPreparedAndFinancialStatementsHaveBeenPreparedInAccordanceWithIFRSFinancialInformation

	def getDescriptionOfFactThatFinancialStatementsHaveBeenPreparedInAccordanceWithSpecialProvisionFinancialInformation(self): #特例財務諸表を作成する場合の記載、経理の状況
		return self.DescriptionOfFactThatFinancialStatementsHaveBeenPreparedInAccordanceWithSpecialProvisionFinancialInformation

	def getDescriptionOfFactThatQuarterlySecuritiesReportForFirstQuarterOrThirdQuarterPresentsStatementOfCashFlowsFinancialInformation(self): #第１四半期又は第３四半期に係る四半期報告書において四半期キャッシュ・フロー計算書を記載する場合の記載、経理の状況
		return self.DescriptionOfFactThatQuarterlySecuritiesReportForFirstQuarterOrThirdQuarterPresentsStatementOfCashFlowsFinancialInformation

	def getDescriptionOfFactThatQuarterlySecuritiesReportForFirstQuarterOrThirdQuarterPresentsConsolidatedStatementOfCashFlowsFinancialInformation(self): #第１四半期又は第３四半期に係る四半期報告書において四半期連結キャッシュ・フロー計算書を記載する場合の記載、経理の状況
		return self.DescriptionOfFactThatQuarterlySecuritiesReportForFirstQuarterOrThirdQuarterPresentsConsolidatedStatementOfCashFlowsFinancialInformation

	def getDescriptionOfFactThatQuarterlySecuritiesReportPresentsQuarterPeriodStatementOfIncomeFinancialInformation(self): #四半期報告書において四半期会計期間に係る四半期損益計算書を記載する場合の記載、経理の状況
		return self.DescriptionOfFactThatQuarterlySecuritiesReportPresentsQuarterPeriodStatementOfIncomeFinancialInformation

	def getDescriptionOfFactThatQuarterlySecuritiesReportPresentsQuarterPeriodConsolidatedStatementOfComprehensiveIncomeFinancialInformation(self): #四半期報告書において四半期連結会計期間に係る四半期連結損益計算書及び四半期連結包括利益計算書又は四半期連結損益及び包括利益計算書を記載する場合の記載、経理の状況
		return self.DescriptionOfFactThatQuarterlySecuritiesReportPresentsQuarterPeriodConsolidatedStatementOfComprehensiveIncomeFinancialInformation

	def getRemarkableEffortsToEnsureFairPresentationOfConsolidatedFinancialStatementsEtcFinancialInformation(self): #連結財務諸表等の適正性を確保するための特段の取組み、経理の状況
		return self.RemarkableEffortsToEnsureFairPresentationOfConsolidatedFinancialStatementsEtcFinancialInformation

	def getRemarkableEffortsToEnsureFairPresentationOfConsolidatedFinancialStatementsEtcInAccordanceWithIFRSFinancialInformation(self): #指定国際会計基準に基づいて連結財務諸表等を適正に作成することができる体制、経理の状況
		return self.RemarkableEffortsToEnsureFairPresentationOfConsolidatedFinancialStatementsEtcInAccordanceWithIFRSFinancialInformation

	def getRemarkableEffortsToEnsureFairPresentationOfConsolidatedFinancialStatementsEtcAndInternalSystemToPrepareConsolidatedFinancialStatementsEtcFairlyInAccordanceWithIFRSFinancialInformation(self): #連結財務諸表等の適正性を確保するための特段の取組み及び指定国際会計基準に基づいて連結財務諸表等を適正に作成することができる体制、経理の状況
		return self.RemarkableEffortsToEnsureFairPresentationOfConsolidatedFinancialStatementsEtcAndInternalSystemToPrepareConsolidatedFinancialStatementsEtcFairlyInAccordanceWithIFRSFinancialInformation

	def getRemarkableEffortsToEnsureFairPresentationOfConsolidatedFinancialStatementsEtcInAccordanceWithJMISFinancialInformation(self): #修正国際基準に基づいて連結財務諸表等を適正に作成することができる体制、経理の状況
		return self.RemarkableEffortsToEnsureFairPresentationOfConsolidatedFinancialStatementsEtcInAccordanceWithJMISFinancialInformation

	def getNoteOnIndependentAuditFinancialInformation(self): #監査証明について、経理の状況
		return self.NoteOnIndependentAuditFinancialInformation

	def getNoteOnChangeOfIndependentAuditorsFinancialInformation(self): #監査人の交代、経理の状況
		return self.NoteOnChangeOfIndependentAuditorsFinancialInformation

	def getNoteOnChangeInFiscalYearEndsFinancialInformation(self): #決算期変更について、経理の状況
		return self.NoteOnChangeInFiscalYearEndsFinancialInformation

	def getConsolidatedFinancialStatementsEtcHeading(self): #連結財務諸表等 [目次項目]
		return self.ConsolidatedFinancialStatementsEtcHeading

	def getConsolidatedFinancialStatementsHeading(self): #連結財務諸表 [目次項目]
		return self.ConsolidatedFinancialStatementsHeading

	def getConsolidatedBalanceSheetHeading(self): #連結貸借対照表 [目次項目]
		return self.ConsolidatedBalanceSheetHeading

	def getConsolidatedBalanceSheetTextBlock(self): #連結貸借対照表 [テキストブロック]
		return self.ConsolidatedBalanceSheetTextBlock

	def getConsolidatedStatementOfFinancialPositionJMISTextBlock(self): #連結財政状態計算書（JMIS） [テキストブロック]
		return self.ConsolidatedStatementOfFinancialPositionJMISTextBlock

	def getConsolidatedBalanceSheetUSGAAPTextBlock(self): #連結貸借対照表 （US GAAP） [テキストブロック]
		return self.ConsolidatedBalanceSheetUSGAAPTextBlock

	def getConsolidatedStatementOfIncomeAndConsolidatedStatementOfComprehensiveIncomeHeading(self): #連結損益計算書及び連結包括利益計算書 [目次項目]
		return self.ConsolidatedStatementOfIncomeAndConsolidatedStatementOfComprehensiveIncomeHeading

	def getConsolidatedStatementOfIncomeHeading(self): #連結損益計算書 [目次項目]
		return self.ConsolidatedStatementOfIncomeHeading

	def getConsolidatedStatementOfIncomeTextBlock(self): #連結損益計算書 [テキストブロック]
		return self.ConsolidatedStatementOfIncomeTextBlock

	def getConsolidatedStatementOfIncomeJMISTextBlock(self): #連結損益計算書（JMIS） [テキストブロック]
		return self.ConsolidatedStatementOfIncomeJMISTextBlock

	def getConsolidatedStatementOfIncomeUSGAAPTextBlock(self): #連結損益計算書（US GAAP） [テキストブロック]
		return self.ConsolidatedStatementOfIncomeUSGAAPTextBlock

	def getConsolidatedStatementOfComprehensiveIncomeHeading(self): #連結包括利益計算書 [目次項目]
		return self.ConsolidatedStatementOfComprehensiveIncomeHeading

	def getConsolidatedStatementOfComprehensiveIncomeTextBlock(self): #連結包括利益計算書 [テキストブロック]
		return self.ConsolidatedStatementOfComprehensiveIncomeTextBlock

	def getConsolidatedStatementOfComprehensiveIncomeJMISTextBlock(self): #連結包括利益計算書（2計算書）（JMIS） [テキストブロック]
		return self.ConsolidatedStatementOfComprehensiveIncomeJMISTextBlock

	def getConsolidatedStatementOfComprehensiveIncomeUSGAAPTextBlock(self): #連結包括利益計算書（US GAAP） [テキストブロック]
		return self.ConsolidatedStatementOfComprehensiveIncomeUSGAAPTextBlock

	def getConsolidatedStatementOfComprehensiveIncomeSingleStatementHeading(self): #連結損益及び包括利益計算書 [目次項目]
		return self.ConsolidatedStatementOfComprehensiveIncomeSingleStatementHeading

	def getConsolidatedStatementOfComprehensiveIncomeSingleStatementTextBlock(self): #連結損益及び包括利益計算書 [テキストブロック]
		return self.ConsolidatedStatementOfComprehensiveIncomeSingleStatementTextBlock

	def getConsolidatedStatementOfComprehensiveIncomeSingleStatementJMISTextBlock(self): #連結包括利益計算書（１計算書）（JMIS） [テキストブロック]
		return self.ConsolidatedStatementOfComprehensiveIncomeSingleStatementJMISTextBlock

	def getConsolidatedStatementOfComprehensiveIncomeSingleStatementUSGAAPTextBlock(self): #連結損益及び包括利益計算書（US GAAP） [テキストブロック]
		return self.ConsolidatedStatementOfComprehensiveIncomeSingleStatementUSGAAPTextBlock

	def getConsolidatedStatementOfChangesInEquityHeading(self): #連結株主資本等変動計算書 [目次項目]
		return self.ConsolidatedStatementOfChangesInEquityHeading

	def getConsolidatedStatementOfChangesInEquityTextBlock(self): #連結株主資本等変動計算書 [テキストブロック]
		return self.ConsolidatedStatementOfChangesInEquityTextBlock

	def getConsolidatedStatementOfChangesInEquityJMISTextBlock(self): #連結持分変動計算書（JMIS） [テキストブロック]
		return self.ConsolidatedStatementOfChangesInEquityJMISTextBlock

	def getConsolidatedStatementOfEquityUSGAAPTextBlock(self): #連結資本勘定計算書（US GAAP） [テキストブロック]
		return self.ConsolidatedStatementOfEquityUSGAAPTextBlock

	def getConsolidatedStatementOfCashFlowsHeading(self): #連結キャッシュ・フロー計算書 [目次項目]
		return self.ConsolidatedStatementOfCashFlowsHeading

	def getConsolidatedStatementOfCashFlowsTextBlock(self): #連結キャッシュ・フロー計算書 [テキストブロック]
		return self.ConsolidatedStatementOfCashFlowsTextBlock

	def getConsolidatedStatementOfCashFlowsJMISTextBlock(self): #連結キャッシュ・フロー計算書（JMIS） [テキストブロック]
		return self.ConsolidatedStatementOfCashFlowsJMISTextBlock

	def getConsolidatedStatementOfCashFlowsUSGAAPTextBlock(self): #連結キャッシュ・フロー計算書（US GAAP） [テキストブロック]
		return self.ConsolidatedStatementOfCashFlowsUSGAAPTextBlock

	def getNotesConsolidatedFinancialStatementsHeading(self): #注記事項、連結財務諸表 [目次項目]
		return self.NotesConsolidatedFinancialStatementsHeading

	def getNotesUncertaintiesOfEntitysAbilityToContinueAsGoingConcernConsolidatedFinancialStatementsHeading(self): #継続企業の前提に関する事項、連結財務諸表 [目次項目]
		return self.NotesUncertaintiesOfEntitysAbilityToContinueAsGoingConcernConsolidatedFinancialStatementsHeading

	def getNotesUncertaintiesOfEntitysAbilityToContinueAsGoingConcernConsolidatedFinancialStatementsTextBlock(self): #継続企業の前提に関する事項、連結財務諸表 [テキストブロック]
		return self.NotesUncertaintiesOfEntitysAbilityToContinueAsGoingConcernConsolidatedFinancialStatementsTextBlock

	def getNotesSignificantAccountingPoliciesForPreparationOfConsolidatedFinancialStatementsHeading(self): #連結財務諸表作成のための基本となる重要な事項 [目次項目]
		return self.NotesSignificantAccountingPoliciesForPreparationOfConsolidatedFinancialStatementsHeading

	def getNotesSignificantAccountingPoliciesForPreparationOfConsolidatedFinancialStatementsTextBlock(self): #連結財務諸表作成のための基本となる重要な事項 [テキストブロック]
		return self.NotesSignificantAccountingPoliciesForPreparationOfConsolidatedFinancialStatementsTextBlock

	def getNotesSignificantAccountingPoliciesForPreparationOfConsolidatedFinancialStatementsHeading(self): #連結財務諸表作成のための基本となる重要な事項 [目次項目]
		return self.NotesSignificantAccountingPoliciesForPreparationOfConsolidatedFinancialStatementsHeading

	def getNotesSignificantAccountingPoliciesForPreparationOfConsolidatedFinancialStatementsTable(self): #連結財務諸表作成のための基本となる重要な事項 [表]
		return self.NotesSignificantAccountingPoliciesForPreparationOfConsolidatedFinancialStatementsTable

	def getConsolidatedOrNonConsolidatedAxis(self): #連結個別 [軸]
		return self.ConsolidatedOrNonConsolidatedAxis

	def getConsolidatedMember(self): #連結 [メンバー] ※ディメンションデフォルト
		return self.ConsolidatedMember

	def getNotesSignificantAccountingPoliciesForPreparationOfConsolidatedFinancialStatementsLineItems(self): #連結財務諸表作成のための基本となる重要な事項 [表示項目]
		return self.NotesSignificantAccountingPoliciesForPreparationOfConsolidatedFinancialStatementsLineItems

	def getDisclosureOfScopeOfConsolidationAbstract(self): #連結の範囲に関する事項 [タイトル項目]
		return self.DisclosureOfScopeOfConsolidationAbstract

	def getNumberOfConsolidatedSubsidiariesAndNamesOfMajorConsolidatedSubsidiariesTextBlock(self): #連結子会社の数及び主要な連結子会社の名称 [テキストブロック]
		return self.NumberOfConsolidatedSubsidiariesAndNamesOfMajorConsolidatedSubsidiariesTextBlock

	def getNumberOfConsolidatedSubsidiaries(self): #連結子会社の数
		return self.NumberOfConsolidatedSubsidiaries

	def getChangesInScopeOfConsolidationTextBlock(self): #連結の範囲の変更 [テキストブロック]
		return self.ChangesInScopeOfConsolidationTextBlock

	def getNamesOfMajorUnconsolidatedSubsidiariesAndReasonsForExclusionFromScopeOfConsolidationTextBlock(self): #主要な非連結子会社の名称及び連結の範囲から除いた理由 [テキストブロック]
		return self.NamesOfMajorUnconsolidatedSubsidiariesAndReasonsForExclusionFromScopeOfConsolidationTextBlock

	def getNamesOfCompaniesEtcAndReasonsForNotBeingDeemedAsSubsidiariesEvenThoughMoreThanHalfOfVotingRightsAreOwnedByReportingCompanyTextBlock(self): #他の会社等の議決権の過半数を自己の計算において所有しているにもかかわらず当該他の会社等を子会社としなかった場合には、当該他の会社等の名称及び子会社としなかった理由 [テキストブロック]
		return self.NamesOfCompaniesEtcAndReasonsForNotBeingDeemedAsSubsidiariesEvenThoughMoreThanHalfOfVotingRightsAreOwnedByReportingCompanyTextBlock

	def getSummaryOfSpecialPurposeEntitiesSubjectToDisclosureOverviewAndAmountsOfTransactionsWithSuchEntitiesAndOtherRelevantMaterialInformationTextBlock(self): #開示対象特別目的会社の概要、開示対象特別目的会社との取引の概要及び取引金額その他の重要な事項 [テキストブロック]
		return self.SummaryOfSpecialPurposeEntitiesSubjectToDisclosureOverviewAndAmountsOfTransactionsWithSuchEntitiesAndOtherRelevantMaterialInformationTextBlock

	def getDisclosureAboutApplicationOfEquityMethodAbstract(self): #持分法の適用に関する事項 [タイトル項目]
		return self.DisclosureAboutApplicationOfEquityMethodAbstract

	def getNumberOfUnconsolidatedSubsidiariesAndAssociatesAccountedForUsingEquityMethodAndNamesOfMajorEntitiesAccountedForUsingEquityMethodTextBlock(self): #持分法を適用した非連結子会社又は関連会社の数及びこれらのうち主要な会社等の名称 [テキストブロック]
		return self.NumberOfUnconsolidatedSubsidiariesAndAssociatesAccountedForUsingEquityMethodAndNamesOfMajorEntitiesAccountedForUsingEquityMethodTextBlock

	def getNumberOfUnconsolidatedSubsidiariesAndAssociatesAccountedForUsingEquityMethod(self): #持分法を適用した非連結子会社又は関連会社の数
		return self.NumberOfUnconsolidatedSubsidiariesAndAssociatesAccountedForUsingEquityMethod

	def getChangesInScopeOfApplicationOfEquityMethodTextBlock(self): #持分法適用の範囲の変更 [テキストブロック]
		return self.ChangesInScopeOfApplicationOfEquityMethodTextBlock

	def getNumberOfUnconsolidatedSubsidiariesAccountedForUsingEquityMethod(self): #持分法を適用した非連結子会社の数
		return self.NumberOfUnconsolidatedSubsidiariesAccountedForUsingEquityMethod

	def getChangesInScopeOfApplicationOfEquityMethodUnconsolidatedSubsidiariesTextBlock(self): #持分法適用の範囲の変更－非連結子会社 [テキストブロック]
		return self.ChangesInScopeOfApplicationOfEquityMethodUnconsolidatedSubsidiariesTextBlock

	def getNumberOfAssociatesAccountedForUsingEquityMethod(self): #持分法を適用した関連会社の数
		return self.NumberOfAssociatesAccountedForUsingEquityMethod

	def getChangesInScopeOfApplicationOfEquityMethodAssociatesTextBlock(self): #持分法適用の範囲の変更－関連会社 [テキストブロック]
		return self.ChangesInScopeOfApplicationOfEquityMethodAssociatesTextBlock

	def getNamesOfMajorUnconsolidatedSubsidiariesAndAssociatesAndReasonsForNotBeingAccountedForUsingEquityMethodTextBlock(self): #持分法を適用しない非連結子会社又は関連会社がある場合には、これらのうち主要な会社等の名称及び持分法を適用しない理由 [テキストブロック]
		return self.NamesOfMajorUnconsolidatedSubsidiariesAndAssociatesAndReasonsForNotBeingAccountedForUsingEquityMethodTextBlock

	def getNamesOfCompaniesEtcAndReasonsForNotBeingDeemedAsAssociatesEvenThoughMoreThan20PerCentAndLessThanHalfOfVotingRightsAreOwnedByReportingCompanyTextBlock(self): #他の会社等の議決権の百分の二十以上、百分の五十以下を自己の計算において所有しているにもかかわらず当該他の会社等を関連会社としなかった場合には、当該他の会社等の名称及び関連会社としなかった理由 [テキストブロック]
		return self.NamesOfCompaniesEtcAndReasonsForNotBeingDeemedAsAssociatesEvenThoughMoreThan20PerCentAndLessThanHalfOfVotingRightsAreOwnedByReportingCompanyTextBlock

	def getOtherSpecificInformationIfDeemedNecessaryAboutApplicationOfEquityMethodTextBlock(self): #持分法の適用の手続について特に記載する必要があると認められる事項がある場合には、その内容 [テキストブロック]
		return self.OtherSpecificInformationIfDeemedNecessaryAboutApplicationOfEquityMethodTextBlock

	def getDisclosureAboutFiscalYearsEtcOfConsolidatedSubsidiariesTextBlock(self): #連結子会社の事業年度等に関する事項 [テキストブロック]
		return self.DisclosureAboutFiscalYearsEtcOfConsolidatedSubsidiariesTextBlock

	def getDisclosureOfAccountingPoliciesAbstract(self): #会計処理基準に関する事項 [タイトル項目]
		return self.DisclosureOfAccountingPoliciesAbstract

	def getDisclosureOfAccountingPoliciesTextBlock(self): #会計方針に関する事項 [テキストブロック]
		return self.DisclosureOfAccountingPoliciesTextBlock

	def getSignificantAccountingEstimatesConsolidatedFinancialStatementsHeading(self): #重要な会計上の見積り、連結財務諸表 [目次項目]
		return self.SignificantAccountingEstimatesConsolidatedFinancialStatementsHeading

	def getSignificantAccountingEstimatesConsolidatedFinancialStatementsTextBlock(self): #重要な会計上の見積り、連結財務諸表 [テキストブロック]
		return self.SignificantAccountingEstimatesConsolidatedFinancialStatementsTextBlock

	def getNotesChangesInAccountingPoliciesConsolidatedFinancialStatementsHeading(self): #会計方針の変更、連結財務諸表 [目次項目]
		return self.NotesChangesInAccountingPoliciesConsolidatedFinancialStatementsHeading

	def getNotesChangesInAccountingPoliciesInAccordanceWithChangesInAccountingStandardsEtcConsolidatedFinancialStatementsTextBlock(self): #会計基準等の改正等に伴う会計方針の変更、連結財務諸表 [テキストブロック]
		return self.NotesChangesInAccountingPoliciesInAccordanceWithChangesInAccountingStandardsEtcConsolidatedFinancialStatementsTextBlock

	def getNotesVoluntaryChangesInAccountingPoliciesConsolidatedFinancialStatementsTextBlock(self): #会計基準等の改正等以外の正当な理由による会計方針の変更、連結財務諸表 [テキストブロック]
		return self.NotesVoluntaryChangesInAccountingPoliciesConsolidatedFinancialStatementsTextBlock

	def getNotesChangesInAccountingPoliciesWhichAreDifficultToDistinguishFromChangesInAccountingEstimatesConsolidatedFinancialStatementsTextBlock(self): #会計上の見積りの変更と区別することが困難な会計方針の変更、連結財務諸表 [テキストブロック]
		return self.NotesChangesInAccountingPoliciesWhichAreDifficultToDistinguishFromChangesInAccountingEstimatesConsolidatedFinancialStatementsTextBlock

	def getNotesNewAccountingStandardsNotYetAppliedConsolidatedFinancialStatementsHeading(self): #未適用の会計基準等、連結財務諸表 [目次項目]
		return self.NotesNewAccountingStandardsNotYetAppliedConsolidatedFinancialStatementsHeading

	def getNotesNewAccountingStandardsNotYetAppliedConsolidatedFinancialStatementsTextBlock(self): #未適用の会計基準等、連結財務諸表 [テキストブロック]
		return self.NotesNewAccountingStandardsNotYetAppliedConsolidatedFinancialStatementsTextBlock

	def getNotesChangesInPresentationConsolidatedFinancialStatementsHeading(self): #表示方法の変更、連結財務諸表 [目次項目]
		return self.NotesChangesInPresentationConsolidatedFinancialStatementsHeading

	def getNotesChangesInPresentationConsolidatedFinancialStatementsTextBlock(self): #表示方法の変更、連結財務諸表 [テキストブロック]
		return self.NotesChangesInPresentationConsolidatedFinancialStatementsTextBlock

	def getNotesChangesInAccountingEstimatesConsolidatedFinancialStatementsHeading(self): #会計上の見積りの変更、連結財務諸表 [目次項目]
		return self.NotesChangesInAccountingEstimatesConsolidatedFinancialStatementsHeading

	def getNotesChangesInAccountingEstimatesConsolidatedFinancialStatementsTextBlock(self): #会計上の見積りの変更、連結財務諸表 [テキストブロック]
		return self.NotesChangesInAccountingEstimatesConsolidatedFinancialStatementsTextBlock

	def getNotesRestatementConsolidatedFinancialStatementsHeading(self): #修正再表示、連結財務諸表 [目次項目]
		return self.NotesRestatementConsolidatedFinancialStatementsHeading

	def getNotesRestatementConsolidatedFinancialStatementsTextBlock(self): #修正再表示、連結財務諸表 [テキストブロック]
		return self.NotesRestatementConsolidatedFinancialStatementsTextBlock

	def getNotesAdditionalInformationConsolidatedFinancialStatementsHeading(self): #追加情報、連結財務諸表 [目次項目]
		return self.NotesAdditionalInformationConsolidatedFinancialStatementsHeading

	def getNotesAdditionalInformationConsolidatedFinancialStatementsTextBlock(self): #追加情報、連結財務諸表 [テキストブロック]
		return self.NotesAdditionalInformationConsolidatedFinancialStatementsTextBlock

	def getNotesConsolidatedBalanceSheetHeading(self): #連結貸借対照表関係 [目次項目]
		return self.NotesConsolidatedBalanceSheetHeading

	def getNotesConsolidatedBalanceSheetHeading(self): #連結貸借対照表関係 [目次項目]
		return self.NotesConsolidatedBalanceSheetHeading

	def getNotesConsolidatedBalanceSheetTable(self): #連結貸借対照表関係 [表]
		return self.NotesConsolidatedBalanceSheetTable

	def getConsolidatedOrNonConsolidatedAxis(self): #連結個別 [軸]
		return self.ConsolidatedOrNonConsolidatedAxis

	def getConsolidatedMember(self): #連結 [メンバー] ※ディメンションデフォルト
		return self.ConsolidatedMember

	def getNotesConsolidatedBalanceSheetLineItems(self): #連結貸借対照表関係 [表示項目]
		return self.NotesConsolidatedBalanceSheetLineItems

	def getNotesRegardingInventoriesTextBlock(self): #棚卸資産の内訳の注記 [テキストブロック]
		return self.NotesRegardingInventoriesTextBlock

	def getMerchandiseAndFinishedGoods(self): #商品及び製品
		return self.MerchandiseAndFinishedGoods

	def getWorkInProcess(self): #仕掛品
		return self.WorkInProcess

	def getRawMaterialsAndSupplies(self): #原材料及び貯蔵品
		return self.RawMaterialsAndSupplies

	def getInventories(self): #棚卸資産
		return self.Inventories

	def getNotesRegardingAmountsOfNotesAndAccountsReceivableTradeAndContractAssetsTextBlock(self): #受取手形、売掛金及び契約資産の金額の注記 [テキストブロック]
		return self.NotesRegardingAmountsOfNotesAndAccountsReceivableTradeAndContractAssetsTextBlock

	def getNotesReceivableTrade(self): #受取手形
		return self.NotesReceivableTrade

	def getAllowanceForDoubtfulAccountsNotesReceivableTrade(self): #貸倒引当金、受取手形
		return self.AllowanceForDoubtfulAccountsNotesReceivableTrade

	def getNotesReceivableTradeNet(self): #受取手形（純額）
		return self.NotesReceivableTradeNet

	def getAccountsReceivableTrade(self): #売掛金
		return self.AccountsReceivableTrade

	def getAllowanceForDoubtfulAccountsAccountsReceivableTrade(self): #貸倒引当金、売掛金
		return self.AllowanceForDoubtfulAccountsAccountsReceivableTrade

	def getAccountsReceivableTradeNet(self): #売掛金（純額）
		return self.AccountsReceivableTradeNet

	def getContractAssets(self): #契約資産
		return self.ContractAssets

	def getAllowanceForDoubtfulAccountsContractAssets(self): #貸倒引当金、契約資産
		return self.AllowanceForDoubtfulAccountsContractAssets

	def getContractAssetsNet(self): #契約資産（純額）
		return self.ContractAssetsNet

	def getNotesRegardingAllowancesDirectlyDeductedFromBalancesOfAssetsTextBlock(self): #資産の金額から直接控除している引当金の注記 [テキストブロック]
		return self.NotesRegardingAllowancesDirectlyDeductedFromBalancesOfAssetsTextBlock

	def getAllowanceForDoubtfulAccountsCA(self): #貸倒引当金、流動資産、一括控除
		return self.AllowanceForDoubtfulAccountsCA

	def getAllowanceForDoubtfulAccountsIOAByGroup(self): #貸倒引当金、投資その他の資産、一括控除
		return self.AllowanceForDoubtfulAccountsIOAByGroup

	def getAllowanceForDoubtfulAccountsAccountsReceivableTrade(self): #貸倒引当金、売掛金
		return self.AllowanceForDoubtfulAccountsAccountsReceivableTrade

	def getAllowanceForDoubtfulAccountsLongTermLoansReceivable(self): #貸倒引当金、長期貸付金
		return self.AllowanceForDoubtfulAccountsLongTermLoansReceivable

	def getAllowanceForDoubtfulAccountsClaimsInBankruptcyReorganizationClaimsAndOther(self): #貸倒引当金、破産更生債権等
		return self.AllowanceForDoubtfulAccountsClaimsInBankruptcyReorganizationClaimsAndOther

	def getNotesRegardingAccumulatedDepreciationOfPropertyPlantAndEquipmentTextBlock(self): #有形固定資産の減価償却累計額の注記 [テキストブロック]
		return self.NotesRegardingAccumulatedDepreciationOfPropertyPlantAndEquipmentTextBlock

	def getAccumulatedDepreciationPPEByGroup(self): #減価償却累計額、有形固定資産、一括控除
		return self.AccumulatedDepreciationPPEByGroup

	def getAccumulatedDepreciationBuildings(self): #減価償却累計額、建物
		return self.AccumulatedDepreciationBuildings

	def getAccumulatedDepreciationStructures(self): #減価償却累計額、構築物
		return self.AccumulatedDepreciationStructures

	def getAccumulatedDepreciationMachineryAndEquipment(self): #減価償却累計額、機械及び装置
		return self.AccumulatedDepreciationMachineryAndEquipment

	def getNotesRegardingAmountsOfReductionEntryOfPropertyPlantAndEquipmentTextBlock(self): #有形固定資産の圧縮記帳額の注記 [テキストブロック]
		return self.NotesRegardingAmountsOfReductionEntryOfPropertyPlantAndEquipmentTextBlock

	def getNotesRegardingPresentationOfAccumulatedImpairmentLossTextBlock(self): #減損損失累計額の表示に関する注記 [テキストブロック]
		return self.NotesRegardingPresentationOfAccumulatedImpairmentLossTextBlock

	def getNotesRegardingSharesAndBondsEtcOfUnconsolidatedSubsidiariesAndAssociatesTextBlock(self): #非連結子会社及び関連会社の株式及び社債等 [テキストブロック]
		return self.NotesRegardingSharesAndBondsEtcOfUnconsolidatedSubsidiariesAndAssociatesTextBlock

	def getNotesRegardingRevaluationOfLandForBusinessTextBlock(self): #事業用土地の再評価に関する注記 [テキストブロック]
		return self.NotesRegardingRevaluationOfLandForBusinessTextBlock

	def getNotesRegardingPledgedAssetsTextBlock(self): #担保に供している資産の注記 [テキストブロック]
		return self.NotesRegardingPledgedAssetsTextBlock

	def getNotesRegardingAmountOfContractLiabilitiesTextBlock(self): #契約負債の金額の注記 [テキストブロック]
		return self.NotesRegardingAmountOfContractLiabilitiesTextBlock

	def getContractLiabilities(self): #契約負債
		return self.ContractLiabilities

	def getNotesRegardingPresentationOfGoodwillAndNegativeGoodwillTextBlock(self): #のれん及び負ののれんの表示に関する注記 [テキストブロック]
		return self.NotesRegardingPresentationOfGoodwillAndNegativeGoodwillTextBlock

	def getNotesRegardingPresentationOfInventoriesAndProvisionForLossOnConstructionContractsTextBlock(self): #棚卸資産及び工事損失引当金の表示に関する注記 [テキストブロック]
		return self.NotesRegardingPresentationOfInventoriesAndProvisionForLossOnConstructionContractsTextBlock

	def getNotesRegardingReservesUnderSpecialLawsTextBlock(self): #特別法上の準備金等に関する注記 [テキストブロック]
		return self.NotesRegardingReservesUnderSpecialLawsTextBlock

	def getNotesRegardingProvisionIncurredFromBusinessCombinationTextBlock(self): #企業結合に係る特定勘定の注記 [テキストブロック]
		return self.NotesRegardingProvisionIncurredFromBusinessCombinationTextBlock

	def getNotesRegardingGuaranteeObligationsTextBlock(self): #保証債務の注記 [テキストブロック]
		return self.NotesRegardingGuaranteeObligationsTextBlock

	def getNotesRegardingTradeNotesReceivableDiscountedOrTransferredByEndorsementTextBlock(self): #受取手形割引高及び（又は）受取手形裏書譲渡高 [テキストブロック]
		return self.NotesRegardingTradeNotesReceivableDiscountedOrTransferredByEndorsementTextBlock

	def getDiscountedTradeNotesReceivable(self): #受取手形割引高
		return self.DiscountedTradeNotesReceivable

	def getTradeNotesReceivableTransferredByEndorsement(self): #受取手形裏書譲渡高
		return self.TradeNotesReceivableTransferredByEndorsement

	def getNotesRegardingLiabilitiesEtcOfSpecialPurposeEntitiesTextBlock(self): #特別目的会社の債務等に関する注記 [テキストブロック]
		return self.NotesRegardingLiabilitiesEtcOfSpecialPurposeEntitiesTextBlock

	def getNotesRegardingReservesRequiredByContractsTextBlock(self): #契約による積立金の注記 [テキストブロック]
		return self.NotesRegardingReservesRequiredByContractsTextBlock

	def getNotesRegardingPresentationOfNetAssetsOfDesignatedCorporationTextBlock(self): #指定法人の純資産の記載に関する注記 [テキストブロック]
		return self.NotesRegardingPresentationOfNetAssetsOfDesignatedCorporationTextBlock

	def getNotesRegardingClassificationOfAssetsAndLiabilitiesOfIndustryInAppendedListTextBlock(self): #別記事業の資産及び負債の分類に関する注記 [テキストブロック]
		return self.NotesRegardingClassificationOfAssetsAndLiabilitiesOfIndustryInAppendedListTextBlock

	def getNotesRegardingPromissoryNotesDueOnBalanceSheetDateTextBlock(self): #期末日満期手形の会計処理 [テキストブロック]
		return self.NotesRegardingPromissoryNotesDueOnBalanceSheetDateTextBlock

	def getOtherElementsForNotesBalanceSheetAbstract(self): #貸借対照表関係のその他の要素 [タイトル項目]
		return self.OtherElementsForNotesBalanceSheetAbstract

	def getNotesRegardingLoanedWhichBorrowerHasRightToSellOrRepledgeTextBlock(self): #消費貸借契約及び（又は）消費寄託契約により貸し付けている有価証券に関する注記 [テキストブロック]
		return self.NotesRegardingLoanedWhichBorrowerHasRightToSellOrRepledgeTextBlock

	def getNotesRegardingFinancialAssetsBorrowedWhichBorrowerHasRightToSellOrRepledgeTextBlock(self): #自由処分権を有する担保受入金融資産に関する注記 [テキストブロック]
		return self.NotesRegardingFinancialAssetsBorrowedWhichBorrowerHasRightToSellOrRepledgeTextBlock

	def getNotesRegardingLoanedSecuritiesAndFinancialAssetsBorrowedWhichBorrowerHasRightToSellOrRepledgeTextBlock(self): #有価証券の消費貸借契約・消費寄託契約及び自由処分権を有する担保受入金融資産に関する注記 [テキストブロック]
		return self.NotesRegardingLoanedSecuritiesAndFinancialAssetsBorrowedWhichBorrowerHasRightToSellOrRepledgeTextBlock

	def getNotesRegardingLoanParticipationsTextBlock(self): #ローン・パーティシペーションに関する注記 [テキストブロック]
		return self.NotesRegardingLoanParticipationsTextBlock

	def getCreditorsNotesRegardingOverdraftContractsAndOrLoanCommitmentsTextBlock(self): #当座貸越契約及び（又は）貸出コミットメントに関する貸手の注記 [テキストブロック]
		return self.CreditorsNotesRegardingOverdraftContractsAndOrLoanCommitmentsTextBlock

	def getDebtorsNotesRegardingOverdraftContractsAndOrLoanCommitmentsTextBlock(self): #当座貸越契約及び（又は）貸出コミットメントに関する借手の注記 [テキストブロック]
		return self.DebtorsNotesRegardingOverdraftContractsAndOrLoanCommitmentsTextBlock

	def getNotesRegardingTotalAmountsOfSharesOfAndOrLoansToAffiliatedEntitiesTextBlock(self): #関係会社の株式及び（又は）出資金の総額 [テキストブロック]
		return self.NotesRegardingTotalAmountsOfSharesOfAndOrLoansToAffiliatedEntitiesTextBlock

	def getNotesRegardingTotalAmountsOfSharesOfAndOrLoansToUnconsolidatedSubsidiariesAndAssociatesTextBlock(self): #非連結子会社及び関連会社の株式及び（又は）出資金の総額 [テキストブロック]
		return self.NotesRegardingTotalAmountsOfSharesOfAndOrLoansToUnconsolidatedSubsidiariesAndAssociatesTextBlock

	def getNotesRegardingSubordinatedBorrowingsTextBlock(self): #劣後特約付借入金に関する注記 [テキストブロック]
		return self.NotesRegardingSubordinatedBorrowingsTextBlock

	def getNotesRegardingSubordinatedBondsPayableTextBlock(self): #劣後特約付社債に関する注記 [テキストブロック]
		return self.NotesRegardingSubordinatedBondsPayableTextBlock

	def getNotesRegardingGuaranteeObligationForCorporateBondsIncludedInAssetsTextBlock(self): #資産の部の社債に係る保証債務に関する注記 [テキストブロック]
		return self.NotesRegardingGuaranteeObligationForCorporateBondsIncludedInAssetsTextBlock

	def getOtherElementsForNotesBalanceSheetOfBankAbstract(self): #銀行業の貸借対照表関係のその他の要素 [タイトル項目]
		return self.OtherElementsForNotesBalanceSheetOfBankAbstract

	def getNotesRegardingLoansBasedOnBankingActAndActOnEmergencyMeasuresForRevitalizationOfFinancialFunctionsBNKTextBlock(self): #銀行法及び金融機能の再生のための緊急措置に関する法律に基づく債権に関する注記、銀行業 [テキストブロック]
		return self.NotesRegardingLoansBasedOnBankingActAndActOnEmergencyMeasuresForRevitalizationOfFinancialFunctionsBNKTextBlock

	def getNotesRegardingBillsDiscountedInBankingIndustryBNKTextBlock(self): #銀行業における手形割引に関する注記、銀行業 [テキストブロック]
		return self.NotesRegardingBillsDiscountedInBankingIndustryBNKTextBlock

	def getOtherElementsForNotesBalanceSheetOfSecuritiesRelatedBusinessAbstract(self): #第一種金融商品取引業の貸借対照表関係のその他の要素 [タイトル項目]
		return self.OtherElementsForNotesBalanceSheetOfSecuritiesRelatedBusinessAbstract

	def getNotesRegardingMarketValueOfSecuritiesPledgedToCounterpartiesSECTextBlock(self): #差し入れた有価証券等の時価の注記、第一種金融商品取引業 [テキストブロック]
		return self.NotesRegardingMarketValueOfSecuritiesPledgedToCounterpartiesSECTextBlock

	def getNotesRegardingMarketValueOfSecuritiesReceivedAsCollateralFromCounterpartiesSECTextBlock(self): #差し入れを受けた有価証券等の時価の注記、第一種金融商品取引業 [テキストブロック]
		return self.NotesRegardingMarketValueOfSecuritiesReceivedAsCollateralFromCounterpartiesSECTextBlock

	def getBreakdownOfTradingAccountSecuritiesEtcSECTextBlock(self): #商品有価証券等の内訳、第一種金融商品取引業 [テキストブロック]
		return self.BreakdownOfTradingAccountSecuritiesEtcSECTextBlock

	def getOtherElementsForNotesBalanceSheetOfInsuranceAbstract(self): #保険業の貸借対照表関係のその他の要素 [タイトル項目]
		return self.OtherElementsForNotesBalanceSheetOfInsuranceAbstract

	def getNotesRegardingLoansBasedOnInsuranceBusinessActINSTextBlock(self): #保険業法に基づく債権に関する注記、保険業 [テキストブロック]
		return self.NotesRegardingLoansBasedOnInsuranceBusinessActINSTextBlock

	def getNotesRegardingAssetsAndLiabilitiesIncludedInSpecificAccountsSpecifiedByArticle118OfInsuranceBusinessActINSTextBlock(self): #保険業法第118条に規定する特別勘定の資産及び負債に関する注記、保険業 [テキストブロック]
		return self.NotesRegardingAssetsAndLiabilitiesIncludedInSpecificAccountsSpecifiedByArticle118OfInsuranceBusinessActINSTextBlock

	def getNotesRegardingDeferredAssetsIncludedInOtherAssetsSpecifiedByArticle113OfInsuranceBusinessActTextBlock(self): #その他資産に含まれている保険業法第113条に規定する事業費の繰延額の注記 [テキストブロック]
		return self.NotesRegardingDeferredAssetsIncludedInOtherAssetsSpecifiedByArticle113OfInsuranceBusinessActTextBlock

	def getNotesRegardingIncreaseAndDecreaseInReserveForPolicyholderDividendsAndPaymentsOfPolicyholderDividendsINSTextBlock(self): #契約者配当準備金の増減異動及び契約者配当金の支払額に関する注記、保険業 [テキストブロック]
		return self.NotesRegardingIncreaseAndDecreaseInReserveForPolicyholderDividendsAndPaymentsOfPolicyholderDividendsINSTextBlock

	def getNotesRegardingSurplusFromOrganizationChangeSpecifiedByArticle91OfInsuranceBusinessActINSTextBlock(self): #保険業法第91条の規定による組織変更剰余金額の注記、保険業 [テキストブロック]
		return self.NotesRegardingSurplusFromOrganizationChangeSpecifiedByArticle91OfInsuranceBusinessActINSTextBlock

	def getNotesRegardingReservesForOutstandingClaimsReinsuredINSTextBlock(self): #保険業法施行規則第73条第3項において準用する同規則第71条第1項に規定する再保険を付した部分に相当する支払備金の金額の注記、保険業 [テキストブロック]
		return self.NotesRegardingReservesForOutstandingClaimsReinsuredINSTextBlock

	def getNotesRegardingPolicyReservesReinsuredINSTextBlock(self): #保険業法施行規則第71条第1項に規定する再保険を付した部分に相当する責任準備金の金額の注記、保険業 [テキストブロック]
		return self.NotesRegardingPolicyReservesReinsuredINSTextBlock

	def getNotesRegardingObligationsToLifeInsurancePolicyholdersProtectionCorporationOfJapanINSTextBlock(self): #保険業法第259条の規定に基づく生命保険契約者保護機構に対する今後の負担見積額、保険業 [テキストブロック]
		return self.NotesRegardingObligationsToLifeInsurancePolicyholdersProtectionCorporationOfJapanINSTextBlock

	def getBreakdownOfOutstandingClaimsINSTextBlock(self): #支払備金の内訳、保険業 [テキストブロック]
		return self.BreakdownOfOutstandingClaimsINSTextBlock

	def getBreakdownOfPolicyReserveINSTextBlock(self): #責任準備金の内訳、保険業 [テキストブロック]
		return self.BreakdownOfPolicyReserveINSTextBlock

	def getOtherElementsForNotesBalanceSheetOfSpecificFinanceAbstract(self): #特定金融業の貸借対照表関係のその他の要素 [タイトル項目]
		return self.OtherElementsForNotesBalanceSheetOfSpecificFinanceAbstract

	def getNotesRegardingBadLoansSPFTextBlock(self): #不良債権に関する注記、特定金融業 [テキストブロック]
		return self.NotesRegardingBadLoansSPFTextBlock

	def getOtherElementsForNotesBalanceSheetOfCommodityFutureTradingAbstract(self): #商品先物取引業の貸借対照表関係のその他の要素 [タイトル項目]
		return self.OtherElementsForNotesBalanceSheetOfCommodityFutureTradingAbstract

	def getExplanationOfFuturesTransactionMarginCustomerCMDTextBlock(self): #委託者先物取引差金の説明、商品先物取引業 [テキストブロック]
		return self.ExplanationOfFuturesTransactionMarginCustomerCMDTextBlock

	def getNotesConsolidatedStatementOfIncomeHeading(self): #連結損益計算書関係 [目次項目]
		return self.NotesConsolidatedStatementOfIncomeHeading

	def getNotesConsolidatedStatementOfIncomeHeading(self): #連結損益計算書関係 [目次項目]
		return self.NotesConsolidatedStatementOfIncomeHeading

	def getNotesConsolidatedStatementOfIncomeTable(self): #連結損益計算書関係 [表]
		return self.NotesConsolidatedStatementOfIncomeTable

	def getConsolidatedOrNonConsolidatedAxis(self): #連結個別 [軸]
		return self.ConsolidatedOrNonConsolidatedAxis

	def getConsolidatedMember(self): #連結 [メンバー] ※ディメンションデフォルト
		return self.ConsolidatedMember

	def getNotesConsolidatedStatementOfIncomeLineItems(self): #連結損益計算書関係 [表示項目]
		return self.NotesConsolidatedStatementOfIncomeLineItems

	def getNotesRegardingAmountOfRevenueFromContractsWithCustomersTextBlock(self): #顧客との契約から生じる収益の金額の注記 [テキストブロック]
		return self.NotesRegardingAmountOfRevenueFromContractsWithCustomersTextBlock

	def getRevenueFromContractsWithCustomers(self): #顧客との契約から生じる収益
		return self.RevenueFromContractsWithCustomers

	def getNotesRegardingLossOnConstructionContractsTextBlock(self): #工事損失引当金繰入額の注記 [テキストブロック]
		return self.NotesRegardingLossOnConstructionContractsTextBlock

	def getNotesRegardingWriteDownsOfInventoriesTextBlock(self): #棚卸資産の帳簿価額の切下げに関する注記 [テキストブロック]
		return self.NotesRegardingWriteDownsOfInventoriesTextBlock

	def getWriteDownsOfInventories(self): #棚卸資産帳簿価額切下額
		return self.WriteDownsOfInventories

	def getMajorComponentsOfSellingGeneralAndAdministrativeExpensesTextBlock(self): #主要な販売費及び一般管理費 [テキストブロック]
		return self.MajorComponentsOfSellingGeneralAndAdministrativeExpensesTextBlock

	def getDepreciationSGA(self): #減価償却費、販売費及び一般管理費
		return self.DepreciationSGA

	def getProvisionOfAllowanceForDoubtfulAccountsSGA(self): #貸倒引当金繰入額、販売費及び一般管理費
		return self.ProvisionOfAllowanceForDoubtfulAccountsSGA

	def getResearchAndDevelopmentExpensesIncludedInGeneralAndAdministrativeExpensesAndManufacturingCostForCurrentPeriodTextBlock(self): #一般管理費及び当期製造費用に含まれる研究開発費 [テキストブロック]
		return self.ResearchAndDevelopmentExpensesIncludedInGeneralAndAdministrativeExpensesAndManufacturingCostForCurrentPeriodTextBlock

	def getResearchAndDevelopmentExpensesIncludedInGeneralAndAdministrativeExpensesAndManufacturingCostForCurrentPeriod(self): #一般管理費及び当期製造費用に含まれる研究開発費
		return self.ResearchAndDevelopmentExpensesIncludedInGeneralAndAdministrativeExpensesAndManufacturingCostForCurrentPeriod

	def getResearchAndDevelopmentExpensesSGA(self): #研究開発費、販売費及び一般管理費
		return self.ResearchAndDevelopmentExpensesSGA

	def getNotesRegardingImpairmentLossTextBlock(self): #減損損失に関する注記 [テキストブロック]
		return self.NotesRegardingImpairmentLossTextBlock

	def getNotesRegardingReversalOfProvisionIncurredFromBusinessCombinationTextBlock(self): #企業結合に係る特定勘定の取崩益の注記 [テキストブロック]
		return self.NotesRegardingReversalOfProvisionIncurredFromBusinessCombinationTextBlock

	def getNotesRegardingGainOnSalesOfPropertyPlantAndEquipmentTextBlock(self): #固定資産売却益の注記 [テキストブロック]
		return self.NotesRegardingGainOnSalesOfPropertyPlantAndEquipmentTextBlock

	def getNotesRegardingLossOnSalesOfPropertyPlantAndEquipmentTextBlock(self): #固定資産売却損の注記 [テキストブロック]
		return self.NotesRegardingLossOnSalesOfPropertyPlantAndEquipmentTextBlock

	def getNotesRegardingLossOnDisposalOfPropertyPlantAndEquipmentTextBlock(self): #固定資産除却損の注記 [テキストブロック]
		return self.NotesRegardingLossOnDisposalOfPropertyPlantAndEquipmentTextBlock

	def getNotesRegardingLossOnDisposalAndSalesOfPropertyPlantAndEquipmentTextBlock(self): #固定資産除売却損の注記 [テキストブロック]
		return self.NotesRegardingLossOnDisposalAndSalesOfPropertyPlantAndEquipmentTextBlock

	def getNotesRegardingClassificationOfRevenuesAndExpensesOfIndustryInAppendedListTextBlock(self): #別記事業の収益及び費用の分類に関する注記 [テキストブロック]
		return self.NotesRegardingClassificationOfRevenuesAndExpensesOfIndustryInAppendedListTextBlock

	def getOtherElementsForNotesStatementOfIncomeAbstract(self): #損益計算書関係のその他の要素 [タイトル項目]
		return self.OtherElementsForNotesStatementOfIncomeAbstract

	def getBreakdownOfBusinessCostTextBlock(self): #事業費の内訳 [テキストブロック]
		return self.BreakdownOfBusinessCostTextBlock

	def getBreakdownOfPersonnelExpensesTextBlock(self): #人件費の内訳 [テキストブロック]
		return self.BreakdownOfPersonnelExpensesTextBlock

	def getBreakdownOfGainOnSalesOfSecuritiesTextBlock(self): #有価証券売却益の内訳 [テキストブロック]
		return self.BreakdownOfGainOnSalesOfSecuritiesTextBlock

	def getBreakdownOfLossOnSalesOfSecuritiesTextBlock(self): #有価証券売却損の内訳 [テキストブロック]
		return self.BreakdownOfLossOnSalesOfSecuritiesTextBlock

	def getBreakdownOfLossOnValuationOfSecuritiesTextBlock(self): #有価証券評価損の内訳 [テキストブロック]
		return self.BreakdownOfLossOnValuationOfSecuritiesTextBlock

	def getNotesRegardingTransactionsWithAffiliatedEntitiesTextBlock(self): #関係会社との取引に関する注記 [テキストブロック]
		return self.NotesRegardingTransactionsWithAffiliatedEntitiesTextBlock

	def getOtherElementsForNotesStatementOfIncomeOfBankAbstract(self): #銀行業の損益計算書関係のその他の要素 [タイトル項目]
		return self.OtherElementsForNotesStatementOfIncomeOfBankAbstract

	def getMajorComponentsOfOtherIncomeBNKTextBlock(self): #その他の経常収益の主要な内訳、銀行業 [テキストブロック]
		return self.MajorComponentsOfOtherIncomeBNKTextBlock

	def getMajorComponentsOfOtherExpensesBNKTextBlock(self): #その他の経常費用の主要な内訳、銀行業 [テキストブロック]
		return self.MajorComponentsOfOtherExpensesBNKTextBlock

	def getOtherElementsForNotesStatementOfIncomeOfSecuritiesRelatedBusinessAbstract(self): #第一種金融商品取引業の損益計算書関係のその他の要素 [タイトル項目]
		return self.OtherElementsForNotesStatementOfIncomeOfSecuritiesRelatedBusinessAbstract

	def getBreakdownOfNetTradingIncomeSECTextBlock(self): #トレーディング損益の内訳、第一種金融商品取引業 [テキストブロック]
		return self.BreakdownOfNetTradingIncomeSECTextBlock

	def getBreakdownOfFinancialRevenueSECTextBlock(self): #金融収益の内訳、第一種金融商品取引業 [テキストブロック]
		return self.BreakdownOfFinancialRevenueSECTextBlock

	def getBreakdownOfFinancialExpensesSECTextBlock(self): #金融費用の内訳、第一種金融商品取引業 [テキストブロック]
		return self.BreakdownOfFinancialExpensesSECTextBlock

	def getOtherElementsForNotesStatementOfIncomeOfInsuranceAbstract(self): #保険業の損益計算書関係のその他の要素 [タイトル項目]
		return self.OtherElementsForNotesStatementOfIncomeOfInsuranceAbstract

	def getMajorComponentsOfBusinessCostTextBlock(self): #事業費の主な内訳 [テキストブロック]
		return self.MajorComponentsOfBusinessCostTextBlock

	def getAgentFeeEtcINSNonlife(self): #代理店手数料等、損害保険業
		return self.AgentFeeEtcINSNonlife

	def getSalariesINSNonlife(self): #給与、損害保険業
		return self.SalariesINSNonlife

	def getBreakdownOfNetPremiumsWrittenINSTextBlock(self): #正味収入保険料の内訳、保険業 [テキストブロック]
		return self.BreakdownOfNetPremiumsWrittenINSTextBlock

	def getBreakdownOfNetClaimsPaidINSTextBlock(self): #正味支払保険金の内訳、保険業 [テキストブロック]
		return self.BreakdownOfNetClaimsPaidINSTextBlock

	def getBreakdownOfCommissionsAndCollectionFeesINSTextBlock(self): #諸手数料及び集金費の内訳、保険業 [テキストブロック]
		return self.BreakdownOfCommissionsAndCollectionFeesINSTextBlock

	def getBreakdownOfProvisionForOrReversalOfOutstandingClaimsINSTextBlock(self): #支払備金繰入額又は支払備金戻入額の内訳、保険業 [テキストブロック]
		return self.BreakdownOfProvisionForOrReversalOfOutstandingClaimsINSTextBlock

	def getBreakdownOfProvisionForOrReversalOfUnderwritingReservesINSTextBlock(self): #責任準備金繰入額又は責任準備金戻入額の内訳、保険業 [テキストブロック]
		return self.BreakdownOfProvisionForOrReversalOfUnderwritingReservesINSTextBlock

	def getNotesRegardingReversalOfOrProvisionForReservesForOutstandingClaimsReinsuredINSTextBlock(self): #支払備金繰入額又は支払備金戻入額の計算上、差し引かれた又は足し上げられた出再支払備金繰入額又は出再支払備金戻入額の注記、保険業 [テキストブロック]
		return self.NotesRegardingReversalOfOrProvisionForReservesForOutstandingClaimsReinsuredINSTextBlock

	def getNotesRegardingReversalOfOrProvisionForPolicyReservesReinsuredINSTextBlock(self): #責任準備金繰入額又は責任準備金戻入額の計算上、差し引かれた又は足し上げられた出再責任準備金繰入額又は出再責任準備金戻入額の注記、保険業 [テキストブロック]
		return self.NotesRegardingReversalOfOrProvisionForPolicyReservesReinsuredINSTextBlock

	def getBreakdownOfInterestAndDividendIncomeBySourceAssetINSTextBlock(self): #利息及び配当金収入の資産源泉別内訳、保険業 [テキストブロック]
		return self.BreakdownOfInterestAndDividendIncomeBySourceAssetINSTextBlock

	def getInterestAndDividendIncomeGainLossOnSalesAndUnrealizedGainLossForEachOfTradingAccountSecuritiesINSTextBlock(self): #商品有価証券及び売買目的有価証券に係るそれぞれの利息及び配当金収入、売却損益及び評価損益の金額、保険業 [テキストブロック]
		return self.InterestAndDividendIncomeGainLossOnSalesAndUnrealizedGainLossForEachOfTradingAccountSecuritiesINSTextBlock

	def getNotesRegardingUnrealizedGainLossForMoneyTrustINSTextBlock(self): #金銭の信託に係る評価損益の金額の注記、保険業 [テキストブロック]
		return self.NotesRegardingUnrealizedGainLossForMoneyTrustINSTextBlock

	def getNotesRegardingUnrealizedGainLossForDerivativesINSTextBlock(self): #金融派生商品に係る評価損益の金額の注記、保険業 [テキストブロック]
		return self.NotesRegardingUnrealizedGainLossForDerivativesINSTextBlock

	def getMajorComponentsOfOtherExtraordinaryIncomeINSTextBlock(self): #その他特別利益の主な内訳、保険業 [テキストブロック]
		return self.MajorComponentsOfOtherExtraordinaryIncomeINSTextBlock

	def getMajorComponentsOfOtherExtraordinaryLossesINSTextBlock(self): #その他特別損失の主な内訳、保険業 [テキストブロック]
		return self.MajorComponentsOfOtherExtraordinaryLossesINSTextBlock

	def getOtherElementsForNotesStatementOfIncomeOfCommodityFutureTradingAbstract(self): #商品先物取引業の損益計算書関係のその他の要素 [タイトル項目]
		return self.OtherElementsForNotesStatementOfIncomeOfCommodityFutureTradingAbstract

	def getBreakdownOfBrokerageIncomeCMDTextBlock(self): #受取手数料の内訳、商品先物取引業 [テキストブロック]
		return self.BreakdownOfBrokerageIncomeCMDTextBlock

	def getBreakdownOfNetGainOnTradingCMDTextBlock(self): #売買損益の内訳、商品先物取引業 [テキストブロック]
		return self.BreakdownOfNetGainOnTradingCMDTextBlock

	def getExchangeRelatedExpensesCMDTextBlock(self): #取引所等関係費の内訳、商品先物取引業 [テキストブロック]
		return self.ExchangeRelatedExpensesCMDTextBlock

	def getNotesConsolidatedStatementOfComprehensiveIncomeHeading(self): #連結包括利益計算書関係 [目次項目]
		return self.NotesConsolidatedStatementOfComprehensiveIncomeHeading

	def getNotesConsolidatedStatementOfComprehensiveIncomeHeading(self): #連結包括利益計算書関係 [目次項目]
		return self.NotesConsolidatedStatementOfComprehensiveIncomeHeading

	def getNotesConsolidatedStatementOfComprehensiveIncomeTable(self): #連結包括利益計算書関係 [表]
		return self.NotesConsolidatedStatementOfComprehensiveIncomeTable

	def getConsolidatedOrNonConsolidatedAxis(self): #連結個別 [軸]
		return self.ConsolidatedOrNonConsolidatedAxis

	def getConsolidatedMember(self): #連結 [メンバー] ※ディメンションデフォルト
		return self.ConsolidatedMember

	def getNotesConsolidatedStatementOfComprehensiveIncomeLineItems(self): #連結包括利益計算書関係 [表示項目]
		return self.NotesConsolidatedStatementOfComprehensiveIncomeLineItems

	def getNotesRegardingTaxEffectsRelatingToOtherComprehensiveIncomeTextBlock(self): #その他の包括利益に係る税効果額 [テキストブロック]
		return self.NotesRegardingTaxEffectsRelatingToOtherComprehensiveIncomeTextBlock

	def getNotesRegardingReclassificationAdjustmentsRelatingToOtherComprehensiveIncomeTextBlock(self): #その他の包括利益に係る組替調整額 [テキストブロック]
		return self.NotesRegardingReclassificationAdjustmentsRelatingToOtherComprehensiveIncomeTextBlock

	def getNotesRegardingReclassificationAdjustmentsAndTaxEffectsRelatingToOtherComprehensiveIncomeTextBlock(self): #その他の包括利益に係る組替調整額及び税効果額 [テキストブロック]
		return self.NotesRegardingReclassificationAdjustmentsAndTaxEffectsRelatingToOtherComprehensiveIncomeTextBlock

	def getNotesConsolidatedStatementOfComprehensiveIncomeSingleStatementHeading(self): #連結損益及び包括利益計算書関係 [目次項目]
		return self.NotesConsolidatedStatementOfComprehensiveIncomeSingleStatementHeading

	def getNotesConsolidatedStatementOfComprehensiveIncomeSingleStatementHeading(self): #連結損益及び包括利益計算書関係 [目次項目]
		return self.NotesConsolidatedStatementOfComprehensiveIncomeSingleStatementHeading

	def getNotesConsolidatedStatementOfComprehensiveIncomeSingleStatementTable(self): #連結損益及び包括利益計算書関係 [表]
		return self.NotesConsolidatedStatementOfComprehensiveIncomeSingleStatementTable

	def getConsolidatedOrNonConsolidatedAxis(self): #連結個別 [軸]
		return self.ConsolidatedOrNonConsolidatedAxis

	def getConsolidatedMember(self): #連結 [メンバー] ※ディメンションデフォルト
		return self.ConsolidatedMember

	def getNotesConsolidatedStatementOfComprehensiveIncomeSingleStatementLineItems(self): #連結損益及び包括利益計算書関係 [表示項目]
		return self.NotesConsolidatedStatementOfComprehensiveIncomeSingleStatementLineItems

	def getNotesRegardingAmountOfRevenueFromContractsWithCustomersTextBlock(self): #顧客との契約から生じる収益の金額の注記 [テキストブロック]
		return self.NotesRegardingAmountOfRevenueFromContractsWithCustomersTextBlock

	def getRevenueFromContractsWithCustomers(self): #顧客との契約から生じる収益
		return self.RevenueFromContractsWithCustomers

	def getNotesRegardingLossOnConstructionContractsTextBlock(self): #工事損失引当金繰入額の注記 [テキストブロック]
		return self.NotesRegardingLossOnConstructionContractsTextBlock

	def getNotesRegardingWriteDownsOfInventoriesTextBlock(self): #棚卸資産の帳簿価額の切下げに関する注記 [テキストブロック]
		return self.NotesRegardingWriteDownsOfInventoriesTextBlock

	def getWriteDownsOfInventories(self): #棚卸資産帳簿価額切下額
		return self.WriteDownsOfInventories

	def getMajorComponentsOfSellingGeneralAndAdministrativeExpensesTextBlock(self): #主要な販売費及び一般管理費 [テキストブロック]
		return self.MajorComponentsOfSellingGeneralAndAdministrativeExpensesTextBlock

	def getDepreciationSGA(self): #減価償却費、販売費及び一般管理費
		return self.DepreciationSGA

	def getProvisionOfAllowanceForDoubtfulAccountsSGA(self): #貸倒引当金繰入額、販売費及び一般管理費
		return self.ProvisionOfAllowanceForDoubtfulAccountsSGA

	def getResearchAndDevelopmentExpensesIncludedInGeneralAndAdministrativeExpensesAndManufacturingCostForCurrentPeriodTextBlock(self): #一般管理費及び当期製造費用に含まれる研究開発費 [テキストブロック]
		return self.ResearchAndDevelopmentExpensesIncludedInGeneralAndAdministrativeExpensesAndManufacturingCostForCurrentPeriodTextBlock

	def getResearchAndDevelopmentExpensesIncludedInGeneralAndAdministrativeExpensesAndManufacturingCostForCurrentPeriod(self): #一般管理費及び当期製造費用に含まれる研究開発費
		return self.ResearchAndDevelopmentExpensesIncludedInGeneralAndAdministrativeExpensesAndManufacturingCostForCurrentPeriod

	def getResearchAndDevelopmentExpensesSGA(self): #研究開発費、販売費及び一般管理費
		return self.ResearchAndDevelopmentExpensesSGA

	def getNotesRegardingImpairmentLossTextBlock(self): #減損損失に関する注記 [テキストブロック]
		return self.NotesRegardingImpairmentLossTextBlock

	def getNotesRegardingReversalOfProvisionIncurredFromBusinessCombinationTextBlock(self): #企業結合に係る特定勘定の取崩益の注記 [テキストブロック]
		return self.NotesRegardingReversalOfProvisionIncurredFromBusinessCombinationTextBlock

	def getNotesRegardingClassificationOfRevenuesAndExpensesOfIndustryInAppendedListTextBlock(self): #別記事業の収益及び費用の分類に関する注記 [テキストブロック]
		return self.NotesRegardingClassificationOfRevenuesAndExpensesOfIndustryInAppendedListTextBlock

	def getNotesRegardingTaxEffectsRelatingToOtherComprehensiveIncomeTextBlock(self): #その他の包括利益に係る税効果額 [テキストブロック]
		return self.NotesRegardingTaxEffectsRelatingToOtherComprehensiveIncomeTextBlock

	def getNotesRegardingReclassificationAdjustmentsRelatingToOtherComprehensiveIncomeTextBlock(self): #その他の包括利益に係る組替調整額 [テキストブロック]
		return self.NotesRegardingReclassificationAdjustmentsRelatingToOtherComprehensiveIncomeTextBlock

	def getNotesRegardingReclassificationAdjustmentsAndTaxEffectsRelatingToOtherComprehensiveIncomeTextBlock(self): #その他の包括利益に係る組替調整額及び税効果額 [テキストブロック]
		return self.NotesRegardingReclassificationAdjustmentsAndTaxEffectsRelatingToOtherComprehensiveIncomeTextBlock

	def getNotesConsolidatedStatementOfChangesInEquityHeading(self): #連結株主資本等変動計算書関係 [目次項目]
		return self.NotesConsolidatedStatementOfChangesInEquityHeading

	def getNotesConsolidatedStatementOfChangesInEquityHeading(self): #連結株主資本等変動計算書関係 [目次項目]
		return self.NotesConsolidatedStatementOfChangesInEquityHeading

	def getNotesConsolidatedStatementOfChangesInEquityTable(self): #連結株主資本等変動計算書関係 [表]
		return self.NotesConsolidatedStatementOfChangesInEquityTable

	def getConsolidatedOrNonConsolidatedAxis(self): #連結個別 [軸]
		return self.ConsolidatedOrNonConsolidatedAxis

	def getConsolidatedMember(self): #連結 [メンバー] ※ディメンションデフォルト
		return self.ConsolidatedMember

	def getNotesConsolidatedStatementOfChangesInEquityLineItems(self): #連結株主資本等変動計算書関係 [表示項目]
		return self.NotesConsolidatedStatementOfChangesInEquityLineItems

	def getNotesRegardingIssuedSharesAndTreasurySharesTextBlock(self): #発行済株式及び自己株式に関する注記 [テキストブロック]
		return self.NotesRegardingIssuedSharesAndTreasurySharesTextBlock

	def getNotesRegardingNewShareSubscriptionRightsEtcTextBlock(self): #新株予約権等に関する注記 [テキストブロック]
		return self.NotesRegardingNewShareSubscriptionRightsEtcTextBlock

	def getNotesRegardingDividendTextBlock(self): #配当に関する注記 [テキストブロック]
		return self.NotesRegardingDividendTextBlock

	def getNotesConsolidatedStatementOfCashFlowsHeading(self): #連結キャッシュ・フロー計算書関係 [目次項目]
		return self.NotesConsolidatedStatementOfCashFlowsHeading

	def getNotesConsolidatedStatementOfCashFlowsHeading(self): #連結キャッシュ・フロー計算書関係 [目次項目]
		return self.NotesConsolidatedStatementOfCashFlowsHeading

	def getNotesConsolidatedStatementOfCashFlowsTable(self): #連結キャッシュ・フロー計算書関係 [表]
		return self.NotesConsolidatedStatementOfCashFlowsTable

	def getConsolidatedOrNonConsolidatedAxis(self): #連結個別 [軸]
		return self.ConsolidatedOrNonConsolidatedAxis

	def getConsolidatedMember(self): #連結 [メンバー] ※ディメンションデフォルト
		return self.ConsolidatedMember

	def getNotesConsolidatedStatementOfCashFlowsLineItems(self): #連結キャッシュ・フロー計算書関係 [表示項目]
		return self.NotesConsolidatedStatementOfCashFlowsLineItems

	def getReconciliationOfEndingBalanceOfCashAndCashEquivalentsWithAccountBalancesPerBalanceSheetTextBlock(self): #現金及び現金同等物の期末残高と貸借対照表に掲記されている科目の金額との関係 [テキストブロック]
		return self.ReconciliationOfEndingBalanceOfCashAndCashEquivalentsWithAccountBalancesPerBalanceSheetTextBlock

	def getMajorComponentsOfAssetsAndLiabilitiesOfConsolidatedSubsidiaryAcquiredByPurchaseOfSharesDuringReportingPeriodTextBlock(self): #株式の取得により新たに連結子会社となった会社がある場合には、当該会社の資産及び負債の主な内訳 [テキストブロック]
		return self.MajorComponentsOfAssetsAndLiabilitiesOfConsolidatedSubsidiaryAcquiredByPurchaseOfSharesDuringReportingPeriodTextBlock

	def getMajorComponentsOfAssetsAndLiabilitiesOfConsolidatedSubsidiaryDisposedOfBySalesOfSharesDuringReportingPeriodTextBlock(self): #株式の売却により連結子会社でなくなった会社がある場合には、当該会社の資産及び負債の主な内訳 [テキストブロック]
		return self.MajorComponentsOfAssetsAndLiabilitiesOfConsolidatedSubsidiaryDisposedOfBySalesOfSharesDuringReportingPeriodTextBlock

	def getMajorComponentsOfAssetsAndLiabilitiesIncreasedOrDecreasedAsResultOfAcquisitionOrDisposalOfBusinessOrMergerEtcWherebyCashWasPaidOrReceivedAsConsiderationTextBlock(self): #現金及び現金同等物を対価とする事業の譲受け若しくは譲渡又は合併等を行った場合には、当該事業の譲受け若しくは譲渡又は合併等により増加又は減少した資産及び負債の主な内訳 [テキストブロック]
		return self.MajorComponentsOfAssetsAndLiabilitiesIncreasedOrDecreasedAsResultOfAcquisitionOrDisposalOfBusinessOrMergerEtcWherebyCashWasPaidOrReceivedAsConsiderationTextBlock

	def getDescriptionOfSignificantTransactionsNotRequiringUseOfCashOrCashEquivalentsTextBlock(self): #重要な非資金取引の内容 [テキストブロック]
		return self.DescriptionOfSignificantTransactionsNotRequiringUseOfCashOrCashEquivalentsTextBlock

	def getDescriptionOfFactThatCashFlowsFromUsedInInvestingActivitiesIncludeCashFlowsFromAssetManagementActivitiesRelatedToInsuranceBusinessINSTextBlock(self): #投資活動によるキャッシュ・フローには、保険事業に係る資産運用業務から生じるキャッシュ・フローを含んでいる旨、保険業 [テキストブロック]
		return self.DescriptionOfFactThatCashFlowsFromUsedInInvestingActivitiesIncludeCashFlowsFromAssetManagementActivitiesRelatedToInsuranceBusinessINSTextBlock

	def getNotesLeasesConsolidatedFinancialStatementsHeading(self): #リース取引関係、連結財務諸表 [目次項目]
		return self.NotesLeasesConsolidatedFinancialStatementsHeading

	def getNotesLeasesConsolidatedFinancialStatementsTextBlock(self): #リース取引関係、連結財務諸表 [テキストブロック]
		return self.NotesLeasesConsolidatedFinancialStatementsTextBlock

	def getNotesFinancialInstrumentsConsolidatedFinancialStatementsHeading(self): #金融商品関係、連結財務諸表 [目次項目]
		return self.NotesFinancialInstrumentsConsolidatedFinancialStatementsHeading

	def getNotesFinancialInstrumentsConsolidatedFinancialStatementsTextBlock(self): #金融商品関係、連結財務諸表 [テキストブロック]
		return self.NotesFinancialInstrumentsConsolidatedFinancialStatementsTextBlock

	def getNotesSecuritiesConsolidatedFinancialStatementsHeading(self): #有価証券関係、連結財務諸表 [目次項目]
		return self.NotesSecuritiesConsolidatedFinancialStatementsHeading

	def getNotesSecuritiesConsolidatedFinancialStatementsTextBlock(self): #有価証券関係、連結財務諸表 [テキストブロック]
		return self.NotesSecuritiesConsolidatedFinancialStatementsTextBlock

	def getNotesMoneyHeldInTrustConsolidatedFinancialStatementsHeading(self): #金銭の信託関係、連結財務諸表 [目次項目]
		return self.NotesMoneyHeldInTrustConsolidatedFinancialStatementsHeading

	def getNotesMoneyHeldInTrustConsolidatedFinancialStatementsTextBlock(self): #金銭の信託関係、連結財務諸表 [テキストブロック]
		return self.NotesMoneyHeldInTrustConsolidatedFinancialStatementsTextBlock

	def getNotesValuationDifferenceOnAvailableForSaleSecuritiesConsolidatedFinancialStatementsHeading(self): #その他有価証券評価差額金、連結財務諸表 [目次項目]
		return self.NotesValuationDifferenceOnAvailableForSaleSecuritiesConsolidatedFinancialStatementsHeading

	def getNotesValuationDifferenceOnAvailableForSaleSecuritiesConsolidatedFinancialStatementsTextBlock(self): #その他有価証券評価差額金、連結財務諸表 [テキストブロック]
		return self.NotesValuationDifferenceOnAvailableForSaleSecuritiesConsolidatedFinancialStatementsTextBlock

	def getNotesDerivativesConsolidatedFinancialStatementsHeading(self): #デリバティブ取引関係、連結財務諸表 [目次項目]
		return self.NotesDerivativesConsolidatedFinancialStatementsHeading

	def getNotesDerivativesConsolidatedFinancialStatementsTextBlock(self): #デリバティブ取引関係、連結財務諸表 [テキストブロック]
		return self.NotesDerivativesConsolidatedFinancialStatementsTextBlock

	def getNotesRetirementBenefitsConsolidatedFinancialStatementsHeading(self): #退職給付関係、連結財務諸表 [目次項目]
		return self.NotesRetirementBenefitsConsolidatedFinancialStatementsHeading

	def getNotesRetirementBenefitsConsolidatedFinancialStatementsTextBlock(self): #退職給付関係、連結財務諸表 [テキストブロック]
		return self.NotesRetirementBenefitsConsolidatedFinancialStatementsTextBlock

	def getNotesShareOptionsEtcConsolidatedFinancialStatementsHeading(self): #ストック・オプション等関係、連結財務諸表 [目次項目]
		return self.NotesShareOptionsEtcConsolidatedFinancialStatementsHeading

	def getNotesShareOptionsEtcConsolidatedFinancialStatementsTextBlock(self): #ストック・オプション等関係、連結財務諸表 [テキストブロック]
		return self.NotesShareOptionsEtcConsolidatedFinancialStatementsTextBlock

	def getNotesTaxEffectAccountingConsolidatedFinancialStatementsHeading(self): #税効果会計関係、連結財務諸表 [目次項目]
		return self.NotesTaxEffectAccountingConsolidatedFinancialStatementsHeading

	def getNotesTaxEffectAccountingConsolidatedFinancialStatementsTextBlock(self): #税効果会計関係、連結財務諸表 [テキストブロック]
		return self.NotesTaxEffectAccountingConsolidatedFinancialStatementsTextBlock

	def getNotesBusinessCombinationsConsolidatedFinancialStatementsHeading(self): #企業結合等関係、連結財務諸表 [目次項目]
		return self.NotesBusinessCombinationsConsolidatedFinancialStatementsHeading

	def getNotesBusinessCombinationsConsolidatedFinancialStatementsTextBlock(self): #企業結合等関係、連結財務諸表 [テキストブロック]
		return self.NotesBusinessCombinationsConsolidatedFinancialStatementsTextBlock

	def getNotesAssetRetirementObligationsConsolidatedFinancialStatementsHeading(self): #資産除去債務関係、連結財務諸表 [目次項目]
		return self.NotesAssetRetirementObligationsConsolidatedFinancialStatementsHeading

	def getNotesAssetRetirementObligationsConsolidatedFinancialStatementsTextBlock(self): #資産除去債務関係、連結財務諸表 [テキストブロック]
		return self.NotesAssetRetirementObligationsConsolidatedFinancialStatementsTextBlock

	def getNotesRealEstateForLeaseEtcConsolidatedFinancialStatementsHeading(self): #賃貸等不動産関係、連結財務諸表 [目次項目]
		return self.NotesRealEstateForLeaseEtcConsolidatedFinancialStatementsHeading

	def getNotesRealEstateForLeaseEtcConsolidatedFinancialStatementsTextBlock(self): #賃貸等不動産関係、連結財務諸表 [テキストブロック]
		return self.NotesRealEstateForLeaseEtcConsolidatedFinancialStatementsTextBlock

	def getNotesRevenueRecognitionConsolidatedFinancialStatementsHeading(self): #収益認識関係、連結財務諸表 [目次項目]
		return self.NotesRevenueRecognitionConsolidatedFinancialStatementsHeading

	def getNotesRevenueRecognitionConsolidatedFinancialStatementsTextBlock(self): #収益認識関係、連結財務諸表 [テキストブロック]
		return self.NotesRevenueRecognitionConsolidatedFinancialStatementsTextBlock

	def getNotesInventoriesConsolidatedFinancialStatementsHeading(self): #棚卸資産関係、連結財務諸表 [目次項目]
		return self.NotesInventoriesConsolidatedFinancialStatementsHeading

	def getNotesInventoriesConsolidatedFinancialStatementsTextBlock(self): #棚卸資産関係、連結財務諸表 [テキストブロック]
		return self.NotesInventoriesConsolidatedFinancialStatementsTextBlock

	def getNotesSegmentInformationEtcConsolidatedFinancialStatementsHeading(self): #セグメント情報等、連結財務諸表 [目次項目]
		return self.NotesSegmentInformationEtcConsolidatedFinancialStatementsHeading

	def getNotesSegmentInformationEtcConsolidatedFinancialStatementsTextBlock(self): #セグメント情報等、連結財務諸表 [テキストブロック]
		return self.NotesSegmentInformationEtcConsolidatedFinancialStatementsTextBlock

	def getNotesSegmentInformationEtcConsolidatedFinancialStatementsHeading(self): #セグメント情報等、連結財務諸表 [目次項目]
		return self.NotesSegmentInformationEtcConsolidatedFinancialStatementsHeading

	def getNotesSegmentInformationEtcConsolidatedFinancialStatementsTable(self): #セグメント情報等、連結財務諸表 [表]
		return self.NotesSegmentInformationEtcConsolidatedFinancialStatementsTable

	def getConsolidatedOrNonConsolidatedAxis(self): #連結個別 [軸]
		return self.ConsolidatedOrNonConsolidatedAxis

	def getConsolidatedMember(self): #連結 [メンバー] ※ディメンションデフォルト
		return self.ConsolidatedMember

	def getNotesSegmentInformationEtcConsolidatedFinancialStatementsLineItems(self): #セグメント情報等、連結財務諸表 [表示項目]
		return self.NotesSegmentInformationEtcConsolidatedFinancialStatementsLineItems

	def getSegmentInformationAbstract(self): #セグメント情報 [タイトル項目]
		return self.SegmentInformationAbstract

	def getDescriptionOfReportableSegmentsTextBlock(self): #報告セグメントの概要 [テキストブロック]
		return self.DescriptionOfReportableSegmentsTextBlock

	def getDisclosureOfChangesInReportableSegmentsTextBlock(self): #報告セグメントの変更に関する事項 [テキストブロック]
		return self.DisclosureOfChangesInReportableSegmentsTextBlock

	def getDescriptionOfFactThatCompanysBusinessComprisesSingleSegment(self): #単一セグメントである旨
		return self.DescriptionOfFactThatCompanysBusinessComprisesSingleSegment

	def getExplanationOfMeasurementsOfSalesProfitLossAssetLiabilityAndOtherItemsForEachReportableSegmentTextBlock(self): #報告セグメントごとの売上高、利益又は損失、資産、負債その他の項目の金額の算定方法 [テキストブロック]
		return self.ExplanationOfMeasurementsOfSalesProfitLossAssetLiabilityAndOtherItemsForEachReportableSegmentTextBlock

	def getNotesSegmentInformationEtcConsolidatedFinancialStatementsHeading(self): #セグメント情報等、連結財務諸表 [目次項目]
		return self.NotesSegmentInformationEtcConsolidatedFinancialStatementsHeading

	def getSegmentInformationAbstract(self): #セグメント情報 [タイトル項目]
		return self.SegmentInformationAbstract

	def getDisclosureOfSalesProfitLossAssetLiabilityAndOtherItemsForEachReportableSegmentTable(self): #報告セグメントごとの売上高、利益又は損失、資産、負債その他の項目の金額に関する情報 [表]
		return self.DisclosureOfSalesProfitLossAssetLiabilityAndOtherItemsForEachReportableSegmentTable

	def getConsolidatedOrNonConsolidatedAxis(self): #連結個別 [軸]
		return self.ConsolidatedOrNonConsolidatedAxis

	def getConsolidatedMember(self): #連結 [メンバー] ※ディメンションデフォルト
		return self.ConsolidatedMember

	def getOperatingSegmentsAxis(self): #事業セグメント [軸]
		return self.OperatingSegmentsAxis

	def getEntityTotalMember(self): #連結合計又は会社合計 [メンバー] ※ディメンションデフォルト
		return self.EntityTotalMember

	def getTotalOfReportableSegmentsAndOthersMember(self): #報告セグメント及びその他の合計 [メンバー]
		return self.TotalOfReportableSegmentsAndOthersMember

	def getReportableSegmentsMember(self): #報告セグメント [メンバー]
		return self.ReportableSegmentsMember

	def getOtherReportableSegmentsMember(self): #その他の報告セグメント [メンバー]
		return self.OtherReportableSegmentsMember

	def getOperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember(self): #報告セグメント以外の全てのセグメント [メンバー]
		return self.OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember

	def getReconcilingItemsMember(self): #調整項目 [メンバー]
		return self.ReconcilingItemsMember

	def getDisclosureOfSalesProfitLossAssetLiabilityAndOtherItemsForEachReportableSegmentLineItems(self): #報告セグメントごとの売上高、利益又は損失、資産、負債その他の項目の金額に関する情報 [表示項目]
		return self.DisclosureOfSalesProfitLossAssetLiabilityAndOtherItemsForEachReportableSegmentLineItems

	def getSalesSegmentInformationAbstract(self): #売上高、セグメント情報 [タイトル項目]
		return self.SalesSegmentInformationAbstract

	def getRevenuesFromExternalCustomers(self): #外部顧客への売上高
		return self.RevenuesFromExternalCustomers

	def getTransactionsWithOtherSegments(self): #セグメント間の内部売上高又は振替高
		return self.TransactionsWithOtherSegments

	def getNetSales(self): #売上高
		return self.NetSales

	def getRevenue(self): #売上収益
		return self.Revenue

	def getOperatingRevenue1(self): #営業収益
		return self.OperatingRevenue1

	def getOperatingRevenue2(self): #営業収入
		return self.OperatingRevenue2

	def getGrossOperatingRevenue(self): #営業総収入
		return self.GrossOperatingRevenue

	def getOrdinaryIncomeBNK(self): #経常収益、銀行業
		return self.OrdinaryIncomeBNK

	def getOperatingIncomeINS(self): #経常収益、保険業
		return self.OperatingIncomeINS

	def getSegmentProfitLossAbstract(self): #セグメント利益又は損失（△） [タイトル項目]
		return self.SegmentProfitLossAbstract

	def getOperatingIncome(self): #営業利益又は営業損失（△）
		return self.OperatingIncome

	def getOrdinaryIncome(self): #経常利益又は経常損失（△）
		return self.OrdinaryIncome

	def getIncomeBeforeIncomeTaxes(self): #税引前当期純利益又は税引前当期純損失（△）
		return self.IncomeBeforeIncomeTaxes

	def getProfitLossAttributableToOwnersOfParent(self): #親会社株主に帰属する当期純利益又は親会社株主に帰属する当期純損失（△）
		return self.ProfitLossAttributableToOwnersOfParent

	def getProfitLoss(self): #当期純利益又は当期純損失（△）（平成26年3月28日財規等改正後）
		return self.ProfitLoss

	def getAssets(self): #資産
		return self.Assets

	def getLiabilities(self): #負債
		return self.Liabilities

	def getOtherItemsSegmentInformationAbstract(self): #その他の項目、セグメント情報 [タイトル項目]
		return self.OtherItemsSegmentInformationAbstract

	def getDepreciationSegmentInformation(self): #減価償却費、セグメント情報
		return self.DepreciationSegmentInformation

	def getAmortizationOfGoodwillSGA(self): #のれん償却額、販売費及び一般管理費
		return self.AmortizationOfGoodwillSGA

	def getInterestIncomeNOI(self): #受取利息、営業外収益
		return self.InterestIncomeNOI

	def getInterestExpensesNOE(self): #支払利息、営業外費用
		return self.InterestExpensesNOE

	def getEquityInEarningsLossesOfAffiliates(self): #持分法投資利益又は損失（△）
		return self.EquityInEarningsLossesOfAffiliates

	def getExtraordinaryIncome(self): #特別利益
		return self.ExtraordinaryIncome

	def getGainOnNegativeGoodwillEI(self): #負ののれん発生益、特別利益
		return self.GainOnNegativeGoodwillEI

	def getExtraordinaryLoss(self): #特別損失
		return self.ExtraordinaryLoss

	def getImpairmentLossEL(self): #減損損失、特別損失
		return self.ImpairmentLossEL

	def getIncomeTaxExpense(self): #税金費用
		return self.IncomeTaxExpense

	def getInvestmentsInEntitiesAccountedForUsingEquityMethod(self): #持分法適用会社への投資額
		return self.InvestmentsInEntitiesAccountedForUsingEquityMethod

	def getIncreaseInPropertyPlantAndEquipmentAndIntangibleAssets(self): #有形固定資産及び無形固定資産の増加額
		return self.IncreaseInPropertyPlantAndEquipmentAndIntangibleAssets

	def getNotesSegmentInformationEtcConsolidatedFinancialStatementsHeading(self): #セグメント情報等、連結財務諸表 [目次項目]
		return self.NotesSegmentInformationEtcConsolidatedFinancialStatementsHeading

	def getNotesSegmentInformationEtcConsolidatedFinancialStatementsTable(self): #セグメント情報等、連結財務諸表 [表]
		return self.NotesSegmentInformationEtcConsolidatedFinancialStatementsTable

	def getConsolidatedOrNonConsolidatedAxis(self): #連結個別 [軸]
		return self.ConsolidatedOrNonConsolidatedAxis

	def getConsolidatedMember(self): #連結 [メンバー] ※ディメンションデフォルト
		return self.ConsolidatedMember

	def getNotesSegmentInformationEtcConsolidatedFinancialStatementsLineItems(self): #セグメント情報等、連結財務諸表 [表示項目]
		return self.NotesSegmentInformationEtcConsolidatedFinancialStatementsLineItems

	def getSegmentInformationAbstract(self): #セグメント情報 [タイトル項目]
		return self.SegmentInformationAbstract

	def getFootnotesRegardingSegmentInformationTableTextBlock(self): #セグメント表の脚注 [テキストブロック]
		return self.FootnotesRegardingSegmentInformationTableTextBlock

	def getDescriptionOfNatureAndAmountsOfDifferencesBetweenReportableSegmentsTotalAndFinancialStatementsTextBlock(self): #報告セグメント合計額と財務諸表計上額との差額及び当該差額の主な内容（差異調整に関する事項） [テキストブロック]
		return self.DescriptionOfNatureAndAmountsOfDifferencesBetweenReportableSegmentsTotalAndFinancialStatementsTextBlock

	def getNotesInformationAssociatedWithReportableSegmentsAbstract(self): #関連情報 [タイトル項目]
		return self.NotesInformationAssociatedWithReportableSegmentsAbstract

	def getInformationForEachProductOrServiceTextBlock(self): #製品及びサービスごとの情報 [テキストブロック]
		return self.InformationForEachProductOrServiceTextBlock

	def getInformationForEachRegionAbstract(self): #地域ごとの情報 [タイトル項目]
		return self.InformationForEachRegionAbstract

	def getRevenuesFromExternalCustomersInformationForEachRegionTextBlock(self): #売上高、地域ごとの情報 [テキストブロック]
		return self.RevenuesFromExternalCustomersInformationForEachRegionTextBlock

	def getPropertyPlantAndEquipmentInformationForEachRegionTextBlock(self): #有形固定資産、地域ごとの情報 [テキストブロック]
		return self.PropertyPlantAndEquipmentInformationForEachRegionTextBlock

	def getInformationForEachOfMainCustomersTextBlock(self): #主要な顧客ごとの情報 [テキストブロック]
		return self.InformationForEachOfMainCustomersTextBlock

	def getNotesSegmentInformationEtcConsolidatedFinancialStatementsHeading(self): #セグメント情報等、連結財務諸表 [目次項目]
		return self.NotesSegmentInformationEtcConsolidatedFinancialStatementsHeading

	def getDisclosureOfImpairmentLossOnNonCurrentAssetsForEachReportableSegmentAbstract(self): #報告セグメントごとの固定資産の減損損失に関する情報 [タイトル項目]
		return self.DisclosureOfImpairmentLossOnNonCurrentAssetsForEachReportableSegmentAbstract

	def getDisclosureOfImpairmentLossOnNonCurrentAssetsForEachReportableSegmentTable(self): #報告セグメントごとの固定資産の減損損失に関する情報 [表]
		return self.DisclosureOfImpairmentLossOnNonCurrentAssetsForEachReportableSegmentTable

	def getConsolidatedOrNonConsolidatedAxis(self): #連結個別 [軸]
		return self.ConsolidatedOrNonConsolidatedAxis

	def getConsolidatedMember(self): #連結 [メンバー] ※ディメンションデフォルト
		return self.ConsolidatedMember

	def getOperatingSegmentsAxis(self): #事業セグメント [軸]
		return self.OperatingSegmentsAxis

	def getEntityTotalMember(self): #連結合計又は会社合計 [メンバー] ※ディメンションデフォルト
		return self.EntityTotalMember

	def getReportableSegmentsMember(self): #報告セグメント [メンバー]
		return self.ReportableSegmentsMember

	def getOtherReportableSegmentsMember(self): #その他の報告セグメント [メンバー]
		return self.OtherReportableSegmentsMember

	def getOperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember(self): #報告セグメント以外の全てのセグメント [メンバー]
		return self.OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember

	def getUnallocatedAmountsAndEliminationMember(self): #全社・消去 [メンバー]
		return self.UnallocatedAmountsAndEliminationMember

	def getDisclosureOfImpairmentLossOnNonCurrentAssetsForEachReportableSegmentLineItems(self): #報告セグメントごとの固定資産の減損損失に関する情報 [表示項目]
		return self.DisclosureOfImpairmentLossOnNonCurrentAssetsForEachReportableSegmentLineItems

	def getImpairmentLossEL(self): #減損損失、特別損失
		return self.ImpairmentLossEL

	def getNotesSegmentInformationEtcConsolidatedFinancialStatementsHeading(self): #セグメント情報等、連結財務諸表 [目次項目]
		return self.NotesSegmentInformationEtcConsolidatedFinancialStatementsHeading

	def getNotesSegmentInformationEtcConsolidatedFinancialStatementsTable(self): #セグメント情報等、連結財務諸表 [表]
		return self.NotesSegmentInformationEtcConsolidatedFinancialStatementsTable

	def getConsolidatedOrNonConsolidatedAxis(self): #連結個別 [軸]
		return self.ConsolidatedOrNonConsolidatedAxis

	def getConsolidatedMember(self): #連結 [メンバー] ※ディメンションデフォルト
		return self.ConsolidatedMember

	def getNotesSegmentInformationEtcConsolidatedFinancialStatementsLineItems(self): #セグメント情報等、連結財務諸表 [表示項目]
		return self.NotesSegmentInformationEtcConsolidatedFinancialStatementsLineItems

	def getDescriptionOfImpairmentLossNotAllocatedToReportableSegments(self): #報告セグメントに配分されていない減損損失の内容
		return self.DescriptionOfImpairmentLossNotAllocatedToReportableSegments

	def getNotesSegmentInformationEtcConsolidatedFinancialStatementsHeading(self): #セグメント情報等、連結財務諸表 [目次項目]
		return self.NotesSegmentInformationEtcConsolidatedFinancialStatementsHeading

	def getAmortizationAndUnamortizedBalanceOfGoodwillForEachReportableSegmentAbstract(self): #報告セグメントごとののれんの償却額及び未償却残高に関する情報 [タイトル項目]
		return self.AmortizationAndUnamortizedBalanceOfGoodwillForEachReportableSegmentAbstract

	def getAmortizationAndUnamortizedBalanceOfGoodwillForEachReportableSegmentTable(self): #報告セグメントごとののれんの償却額及び未償却残高に関する情報 [表]
		return self.AmortizationAndUnamortizedBalanceOfGoodwillForEachReportableSegmentTable

	def getConsolidatedOrNonConsolidatedAxis(self): #連結個別 [軸]
		return self.ConsolidatedOrNonConsolidatedAxis

	def getConsolidatedMember(self): #連結 [メンバー] ※ディメンションデフォルト
		return self.ConsolidatedMember

	def getOperatingSegmentsAxis(self): #事業セグメント [軸]
		return self.OperatingSegmentsAxis

	def getEntityTotalMember(self): #連結合計又は会社合計 [メンバー] ※ディメンションデフォルト
		return self.EntityTotalMember

	def getReportableSegmentsMember(self): #報告セグメント [メンバー]
		return self.ReportableSegmentsMember

	def getOtherReportableSegmentsMember(self): #その他の報告セグメント [メンバー]
		return self.OtherReportableSegmentsMember

	def getOperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember(self): #報告セグメント以外の全てのセグメント [メンバー]
		return self.OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember

	def getUnallocatedAmountsAndEliminationMember(self): #全社・消去 [メンバー]
		return self.UnallocatedAmountsAndEliminationMember

	def getAmortizationAndUnamortizedBalanceOfGoodwillForEachReportableSegmentLineItems(self): #報告セグメントごとののれんの償却額及び未償却残高に関する情報 [表示項目]
		return self.AmortizationAndUnamortizedBalanceOfGoodwillForEachReportableSegmentLineItems

	def getAmortizationOfGoodwillSGA(self): #のれん償却額、販売費及び一般管理費
		return self.AmortizationOfGoodwillSGA

	def getGoodwill(self): #のれん
		return self.Goodwill

	def getGoodwillBeforeOffsetting(self): #のれん（相殺前）
		return self.GoodwillBeforeOffsetting

	def getNotesSegmentInformationEtcConsolidatedFinancialStatementsHeading(self): #セグメント情報等、連結財務諸表 [目次項目]
		return self.NotesSegmentInformationEtcConsolidatedFinancialStatementsHeading

	def getAmortizationAndUnamortizedBalanceOfNegativeGoodwillForEachReportableSegmentAbstract(self): #報告セグメントごとの負ののれんの償却額及び未償却残高に関する情報 [タイトル項目]
		return self.AmortizationAndUnamortizedBalanceOfNegativeGoodwillForEachReportableSegmentAbstract

	def getAmortizationAndUnamortizedBalanceOfNegativeGoodwillForEachReportableSegmentTable(self): #報告セグメントごとの負ののれんの償却額及び未償却残高に関する情報 [表]
		return self.AmortizationAndUnamortizedBalanceOfNegativeGoodwillForEachReportableSegmentTable

	def getConsolidatedOrNonConsolidatedAxis(self): #連結個別 [軸]
		return self.ConsolidatedOrNonConsolidatedAxis

	def getConsolidatedMember(self): #連結 [メンバー] ※ディメンションデフォルト
		return self.ConsolidatedMember

	def getOperatingSegmentsAxis(self): #事業セグメント [軸]
		return self.OperatingSegmentsAxis

	def getEntityTotalMember(self): #連結合計又は会社合計 [メンバー] ※ディメンションデフォルト
		return self.EntityTotalMember

	def getReportableSegmentsMember(self): #報告セグメント [メンバー]
		return self.ReportableSegmentsMember

	def getOtherReportableSegmentsMember(self): #その他の報告セグメント [メンバー]
		return self.OtherReportableSegmentsMember

	def getOperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember(self): #報告セグメント以外の全てのセグメント [メンバー]
		return self.OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember

	def getUnallocatedAmountsAndEliminationMember(self): #全社・消去 [メンバー]
		return self.UnallocatedAmountsAndEliminationMember

	def getAmortizationAndUnamortizedBalanceOfNegativeGoodwillForEachReportableSegmentLineItems(self): #報告セグメントごとの負ののれんの償却額及び未償却残高に関する情報 [表示項目]
		return self.AmortizationAndUnamortizedBalanceOfNegativeGoodwillForEachReportableSegmentLineItems

	def getAmortizationOfNegativeGoodwillNOI(self): #負ののれん償却額、営業外収益
		return self.AmortizationOfNegativeGoodwillNOI

	def getNegativeGoodwill(self): #負ののれん
		return self.NegativeGoodwill

	def getNegativeGoodwillBeforeOffsetting(self): #負ののれん（相殺前）
		return self.NegativeGoodwillBeforeOffsetting

	def getNotesSegmentInformationEtcConsolidatedFinancialStatementsHeading(self): #セグメント情報等、連結財務諸表 [目次項目]
		return self.NotesSegmentInformationEtcConsolidatedFinancialStatementsHeading

	def getNotesSegmentInformationEtcConsolidatedFinancialStatementsTable(self): #セグメント情報等、連結財務諸表 [表]
		return self.NotesSegmentInformationEtcConsolidatedFinancialStatementsTable

	def getConsolidatedOrNonConsolidatedAxis(self): #連結個別 [軸]
		return self.ConsolidatedOrNonConsolidatedAxis

	def getConsolidatedMember(self): #連結 [メンバー] ※ディメンションデフォルト
		return self.ConsolidatedMember

	def getNotesSegmentInformationEtcConsolidatedFinancialStatementsLineItems(self): #セグメント情報等、連結財務諸表 [表示項目]
		return self.NotesSegmentInformationEtcConsolidatedFinancialStatementsLineItems

	def getDescriptionOfAmortizationOfGoodwillOrUnamortizedBalanceOfGoodwillNotAllocatedToReportableSegments(self): #報告セグメントに配分されていないのれんの償却額又は未償却残高の内容
		return self.DescriptionOfAmortizationOfGoodwillOrUnamortizedBalanceOfGoodwillNotAllocatedToReportableSegments

	def getNotesSegmentInformationEtcConsolidatedFinancialStatementsHeading(self): #セグメント情報等、連結財務諸表 [目次項目]
		return self.NotesSegmentInformationEtcConsolidatedFinancialStatementsHeading

	def getInformationAboutGainOnBargainPurchaseForEachReportableSegmentTable(self): #報告セグメントごとの負ののれん発生益に関する情報 [表]
		return self.InformationAboutGainOnBargainPurchaseForEachReportableSegmentTable

	def getConsolidatedOrNonConsolidatedAxis(self): #連結個別 [軸]
		return self.ConsolidatedOrNonConsolidatedAxis

	def getConsolidatedMember(self): #連結 [メンバー] ※ディメンションデフォルト
		return self.ConsolidatedMember

	def getOperatingSegmentsAxis(self): #事業セグメント [軸]
		return self.OperatingSegmentsAxis

	def getEntityTotalMember(self): #連結合計又は会社合計 [メンバー] ※ディメンションデフォルト
		return self.EntityTotalMember

	def getReportableSegmentsMember(self): #報告セグメント [メンバー]
		return self.ReportableSegmentsMember

	def getOtherReportableSegmentsMember(self): #その他の報告セグメント [メンバー]
		return self.OtherReportableSegmentsMember

	def getOperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember(self): #報告セグメント以外の全てのセグメント [メンバー]
		return self.OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember

	def getUnallocatedAmountsAndEliminationMember(self): #全社・消去 [メンバー]
		return self.UnallocatedAmountsAndEliminationMember

	def getInformationAboutGainOnBargainPurchaseForEachReportableSegmentLineItems(self): #報告セグメントごとの負ののれん発生益に関する情報 [表示項目]
		return self.InformationAboutGainOnBargainPurchaseForEachReportableSegmentLineItems

	def getDescriptionOfFactorsWhichLedToRecognitionOfGainOnBargainPurchaseTextBlock(self): #報告セグメントごとの負ののれん発生益を認識する要因となった事象の概要 [テキストブロック]
		return self.DescriptionOfFactorsWhichLedToRecognitionOfGainOnBargainPurchaseTextBlock

	def getNotesOperationOfPublicFacilitiesConsolidatedFinancialStatementsHeading(self): #公共施設等運営事業関係、連結財務諸表 [目次項目]
		return self.NotesOperationOfPublicFacilitiesConsolidatedFinancialStatementsHeading

	def getNotesOperationOfPublicFacilitiesConsolidatedFinancialStatementsTextBlock(self): #公共施設等運営事業関係、連結財務諸表 [テキストブロック]
		return self.NotesOperationOfPublicFacilitiesConsolidatedFinancialStatementsTextBlock

	def getNotesRelatedPartiesConsolidatedFinancialStatementsHeading(self): #関連当事者情報、連結財務諸表 [目次項目]
		return self.NotesRelatedPartiesConsolidatedFinancialStatementsHeading

	def getNotesRelatedPartiesConsolidatedFinancialStatementsTextBlock(self): #関連当事者情報、連結財務諸表 [テキストブロック]
		return self.NotesRelatedPartiesConsolidatedFinancialStatementsTextBlock

	def getNotesSpecialPurposeEntitiesSubjectToDisclosureConsolidatedFinancialStatementsHeading(self): #開示対象特別目的会社関係、連結財務諸表 [目次項目]
		return self.NotesSpecialPurposeEntitiesSubjectToDisclosureConsolidatedFinancialStatementsHeading

	def getNotesSpecialPurposeEntitiesSubjectToDisclosureConsolidatedFinancialStatementsTextBlock(self): #開示対象特別目的会社関係、連結財務諸表 [テキストブロック]
		return self.NotesSpecialPurposeEntitiesSubjectToDisclosureConsolidatedFinancialStatementsTextBlock

	def getNotesPerShareInformationConsolidatedFinancialStatementsHeading(self): #１株当たり情報、連結財務諸表 [目次項目]
		return self.NotesPerShareInformationConsolidatedFinancialStatementsHeading

	def getNotesPerShareInformationConsolidatedFinancialStatementsTextBlock(self): #１株当たり情報、連結財務諸表 [テキストブロック]
		return self.NotesPerShareInformationConsolidatedFinancialStatementsTextBlock

	def getNotesSignificantEventsAfterReportingPeriodConsolidatedFinancialStatementsHeading(self): #重要な後発事象、連結財務諸表 [目次項目]
		return self.NotesSignificantEventsAfterReportingPeriodConsolidatedFinancialStatementsHeading

	def getNotesSignificantEventsAfterReportingPeriodConsolidatedFinancialStatementsTextBlock(self): #重要な後発事象、連結財務諸表 [テキストブロック]
		return self.NotesSignificantEventsAfterReportingPeriodConsolidatedFinancialStatementsTextBlock

	def getNotesToConsolidatedFinancialStatementsJMISHeading(self): #連結財務諸表注記事項（JMIS） [目次項目]
		return self.NotesToConsolidatedFinancialStatementsJMISHeading

	def getNotesToConsolidatedFinancialStatementsJMISTextBlock(self): #連結財務諸表注記事項（JMIS） [テキストブロック]
		return self.NotesToConsolidatedFinancialStatementsJMISTextBlock

	def getNotesToConsolidatedFinancialStatementsUSGAAPHeading(self): #連結財務諸表注記事項（US GAAP） [目次項目]
		return self.NotesToConsolidatedFinancialStatementsUSGAAPHeading

	def getNotesToConsolidatedFinancialStatementsUSGAAPTextBlock(self): #連結財務諸表注記事項（US GAAP） [テキストブロック]
		return self.NotesToConsolidatedFinancialStatementsUSGAAPTextBlock

	def getAnnexedConsolidatedDetailedSchedulesHeading(self): #連結附属明細表 [目次項目]
		return self.AnnexedConsolidatedDetailedSchedulesHeading

	def getAnnexedConsolidatedDetailedScheduleOfCorporateBondsHeading(self): #社債明細表、連結財務諸表 [目次項目]
		return self.AnnexedConsolidatedDetailedScheduleOfCorporateBondsHeading

	def getAnnexedConsolidatedDetailedScheduleOfCorporateBondsTextBlock(self): #社債明細表、連結財務諸表 [テキストブロック]
		return self.AnnexedConsolidatedDetailedScheduleOfCorporateBondsTextBlock

	def getAnnexedConsolidatedDetailedScheduleOfBorrowingsHeading(self): #借入金等明細表、連結財務諸表 [目次項目]
		return self.AnnexedConsolidatedDetailedScheduleOfBorrowingsHeading

	def getAnnexedConsolidatedDetailedScheduleOfBorrowingsTextBlock(self): #借入金等明細表、連結財務諸表 [テキストブロック]
		return self.AnnexedConsolidatedDetailedScheduleOfBorrowingsTextBlock

	def getAnnexedConsolidatedDetailedScheduleOfAssetRetirementObligationsHeading(self): #資産除去債務明細表、連結財務諸表 [目次項目]
		return self.AnnexedConsolidatedDetailedScheduleOfAssetRetirementObligationsHeading

	def getAnnexedConsolidatedDetailedScheduleOfAssetRetirementObligationsTextBlock(self): #資産除去債務明細表、連結財務諸表 [テキストブロック]
		return self.AnnexedConsolidatedDetailedScheduleOfAssetRetirementObligationsTextBlock

	def getOtherInformationConsolidatedFinancialStatementsEtcHeading(self): #その他、連結財務諸表等 [目次項目]
		return self.OtherInformationConsolidatedFinancialStatementsEtcHeading

	def getOtherInformationConsolidatedFinancialStatementsEtcTextBlock(self): #その他、連結財務諸表等 [テキストブロック]
		return self.OtherInformationConsolidatedFinancialStatementsEtcTextBlock

	def getFinancialStatementsEtcHeading(self): #財務諸表等 [目次項目]
		return self.FinancialStatementsEtcHeading

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

	def getDetailedScheduleOfManufacturingCostTextBlock(self): #製造原価明細書 [テキストブロック]
		return self.DetailedScheduleOfManufacturingCostTextBlock

	def getDetailedScheduleOfCostOfSalesTextBlock(self): #売上原価明細書 [テキストブロック]
		return self.DetailedScheduleOfCostOfSalesTextBlock

	def getDetailedScheduleOfOperatingExpensesForRailwayBusinessTextBlock(self): #鉄道事業営業費明細表 [テキストブロック]
		return self.DetailedScheduleOfOperatingExpensesForRailwayBusinessTextBlock

	def getDetailedScheduleOfOperatingExpensesForMotorwayBusinessTextBlock(self): #自動車道事業営業費明細表 [テキストブロック]
		return self.DetailedScheduleOfOperatingExpensesForMotorwayBusinessTextBlock

	def getDetailedScheduleOfOperatingExpensesTelecommunicationsBusinessTextBlock(self): #電気通信事業営業費用明細表 [テキストブロック]
		return self.DetailedScheduleOfOperatingExpensesTelecommunicationsBusinessTextBlock

	def getDetailedScheduleOfElectricUtilityOperatingExpensesTextBlock(self): #電気事業営業費用明細表 [テキストブロック]
		return self.DetailedScheduleOfElectricUtilityOperatingExpensesTextBlock

	def getDetailedScheduleOfOperatingExpensesGASTextBlock(self): #営業費明細表、ガス事業 [テキストブロック]
		return self.DetailedScheduleOfOperatingExpensesGASTextBlock

	def getDetailedScheduleOfOperatingExpensesNonOperatingExpensesExtraordinaryLossesEtcForHighwayBusinessTextBlock(self): #高速道路事業営業費用、営業外費用及び特別損失等明細表 [テキストブロック]
		return self.DetailedScheduleOfOperatingExpensesNonOperatingExpensesExtraordinaryLossesEtcForHighwayBusinessTextBlock

	def getDetailedScheduleOfOperatingExpensesEDUTextBlock(self): #事業費用明細表、学校法人 [テキストブロック]
		return self.DetailedScheduleOfOperatingExpensesEDUTextBlock

	def getStatementOfChangesInEquityHeading(self): #株主資本等変動計算書 [目次項目]
		return self.StatementOfChangesInEquityHeading

	def getStatementOfChangesInEquityTextBlock(self): #株主資本等変動計算書 [テキストブロック]
		return self.StatementOfChangesInEquityTextBlock

	def getStatementOfCashFlowsHeading(self): #キャッシュ・フロー計算書 [目次項目]
		return self.StatementOfCashFlowsHeading

	def getStatementOfCashFlowsTextBlock(self): #キャッシュ・フロー計算書 [テキストブロック]
		return self.StatementOfCashFlowsTextBlock

	def getNotesFinancialStatementsHeading(self): #注記事項、財務諸表 [目次項目]
		return self.NotesFinancialStatementsHeading

	def getNotesUncertaintiesOfEntitysAbilityToContinueAsGoingConcernFinancialStatementsHeading(self): #継続企業の前提に関する事項、財務諸表 [目次項目]
		return self.NotesUncertaintiesOfEntitysAbilityToContinueAsGoingConcernFinancialStatementsHeading

	def getNotesUncertaintiesOfEntitysAbilityToContinueAsGoingConcernFinancialStatementsTextBlock(self): #継続企業の前提に関する事項、財務諸表 [テキストブロック]
		return self.NotesUncertaintiesOfEntitysAbilityToContinueAsGoingConcernFinancialStatementsTextBlock

	def getNotesSignificantAccountingPoliciesFinancialStatementsHeading(self): #重要な会計方針、財務諸表 [目次項目]
		return self.NotesSignificantAccountingPoliciesFinancialStatementsHeading

	def getNotesSignificantAccountingPoliciesFinancialStatementsTextBlock(self): #重要な会計方針、財務諸表 [テキストブロック]
		return self.NotesSignificantAccountingPoliciesFinancialStatementsTextBlock

	def getSignificantAccountingEstimatesFinancialStatementsHeading(self): #重要な会計上の見積り、財務諸表 [目次項目]
		return self.SignificantAccountingEstimatesFinancialStatementsHeading

	def getSignificantAccountingEstimatesFinancialStatementsTextBlock(self): #重要な会計上の見積り、財務諸表 [テキストブロック]
		return self.SignificantAccountingEstimatesFinancialStatementsTextBlock

	def getNotesChangesInAccountingPoliciesFinancialStatementsHeading(self): #会計方針の変更、財務諸表 [目次項目]
		return self.NotesChangesInAccountingPoliciesFinancialStatementsHeading

	def getNotesChangesInAccountingPoliciesInAccordanceWithChangesInAccountingStandardsEtcFinancialStatementsTextBlock(self): #会計基準等の改正等に伴う会計方針の変更、財務諸表 [テキストブロック]
		return self.NotesChangesInAccountingPoliciesInAccordanceWithChangesInAccountingStandardsEtcFinancialStatementsTextBlock

	def getNotesVoluntaryChangesInAccountingPoliciesFinancialStatementsTextBlock(self): #会計基準等の改正等以外の正当な理由による会計方針の変更、財務諸表 [テキストブロック]
		return self.NotesVoluntaryChangesInAccountingPoliciesFinancialStatementsTextBlock

	def getNotesChangesInAccountingPoliciesWhichAreDifficultToDistinguishFromChangesInAccountingEstimatesFinancialStatementsTextBlock(self): #会計上の見積りの変更と区別することが困難な会計方針の変更、財務諸表 [テキストブロック]
		return self.NotesChangesInAccountingPoliciesWhichAreDifficultToDistinguishFromChangesInAccountingEstimatesFinancialStatementsTextBlock

	def getNotesNewAccountingStandardsNotYetAppliedFinancialStatementsHeading(self): #未適用の会計基準等、財務諸表 [目次項目]
		return self.NotesNewAccountingStandardsNotYetAppliedFinancialStatementsHeading

	def getNotesNewAccountingStandardsNotYetAppliedFinancialStatementsTextBlock(self): #未適用の会計基準等、財務諸表 [テキストブロック]
		return self.NotesNewAccountingStandardsNotYetAppliedFinancialStatementsTextBlock

	def getNotesChangesInPresentationFinancialStatementsHeading(self): #表示方法の変更、財務諸表 [目次項目]
		return self.NotesChangesInPresentationFinancialStatementsHeading

	def getNotesChangesInPresentationFinancialStatementsTextBlock(self): #表示方法の変更、財務諸表 [テキストブロック]
		return self.NotesChangesInPresentationFinancialStatementsTextBlock

	def getNotesChangesInAccountingEstimatesFinancialStatementsHeading(self): #会計上の見積りの変更、財務諸表 [目次項目]
		return self.NotesChangesInAccountingEstimatesFinancialStatementsHeading

	def getNotesChangesInAccountingEstimatesFinancialStatementsTextBlock(self): #会計上の見積りの変更、財務諸表 [テキストブロック]
		return self.NotesChangesInAccountingEstimatesFinancialStatementsTextBlock

	def getNotesRestatementFinancialStatementsHeading(self): #修正再表示、財務諸表 [目次項目]
		return self.NotesRestatementFinancialStatementsHeading

	def getNotesRestatementFinancialStatementsTextBlock(self): #修正再表示、財務諸表 [テキストブロック]
		return self.NotesRestatementFinancialStatementsTextBlock

	def getNotesAdditionalInformationFinancialStatementsHeading(self): #追加情報、財務諸表 [目次項目]
		return self.NotesAdditionalInformationFinancialStatementsHeading

	def getNotesAdditionalInformationFinancialStatementsTextBlock(self): #追加情報、財務諸表 [テキストブロック]
		return self.NotesAdditionalInformationFinancialStatementsTextBlock

	def getNotesBalanceSheetHeading(self): #貸借対照表関係 [目次項目]
		return self.NotesBalanceSheetHeading

	def getNotesBalanceSheetHeading(self): #貸借対照表関係 [目次項目]
		return self.NotesBalanceSheetHeading

	def getNotesBalanceSheetTable(self): #貸借対照表関係 [表]
		return self.NotesBalanceSheetTable

	def getConsolidatedOrNonConsolidatedAxis(self): #連結個別 [軸]
		return self.ConsolidatedOrNonConsolidatedAxis

	def getNonConsolidatedMember(self): #非連結又は個別 [メンバー]
		return self.NonConsolidatedMember

	def getNotesBalanceSheetLineItems(self): #貸借対照表関係 [表示項目]
		return self.NotesBalanceSheetLineItems

	def getNotesRegardingInventoriesTextBlock(self): #棚卸資産の内訳の注記 [テキストブロック]
		return self.NotesRegardingInventoriesTextBlock

	def getMerchandiseAndFinishedGoods(self): #商品及び製品
		return self.MerchandiseAndFinishedGoods

	def getWorkInProcess(self): #仕掛品
		return self.WorkInProcess

	def getRawMaterialsAndSupplies(self): #原材料及び貯蔵品
		return self.RawMaterialsAndSupplies

	def getInventories(self): #棚卸資産
		return self.Inventories

	def getNotesRegardingAmountsOfNotesAndAccountsReceivableTradeAndContractAssetsTextBlock(self): #受取手形、売掛金及び契約資産の金額の注記 [テキストブロック]
		return self.NotesRegardingAmountsOfNotesAndAccountsReceivableTradeAndContractAssetsTextBlock

	def getNotesReceivableTrade(self): #受取手形
		return self.NotesReceivableTrade

	def getAllowanceForDoubtfulAccountsNotesReceivableTrade(self): #貸倒引当金、受取手形
		return self.AllowanceForDoubtfulAccountsNotesReceivableTrade

	def getNotesReceivableTradeNet(self): #受取手形（純額）
		return self.NotesReceivableTradeNet

	def getAccountsReceivableTrade(self): #売掛金
		return self.AccountsReceivableTrade

	def getAllowanceForDoubtfulAccountsAccountsReceivableTrade(self): #貸倒引当金、売掛金
		return self.AllowanceForDoubtfulAccountsAccountsReceivableTrade

	def getAccountsReceivableTradeNet(self): #売掛金（純額）
		return self.AccountsReceivableTradeNet

	def getContractAssets(self): #契約資産
		return self.ContractAssets

	def getAllowanceForDoubtfulAccountsContractAssets(self): #貸倒引当金、契約資産
		return self.AllowanceForDoubtfulAccountsContractAssets

	def getContractAssetsNet(self): #契約資産（純額）
		return self.ContractAssetsNet

	def getNotesRegardingAllowancesDirectlyDeductedFromBalancesOfAssetsTextBlock(self): #資産の金額から直接控除している引当金の注記 [テキストブロック]
		return self.NotesRegardingAllowancesDirectlyDeductedFromBalancesOfAssetsTextBlock

	def getAllowanceForDoubtfulAccountsCA(self): #貸倒引当金、流動資産、一括控除
		return self.AllowanceForDoubtfulAccountsCA

	def getAllowanceForDoubtfulAccountsIOAByGroup(self): #貸倒引当金、投資その他の資産、一括控除
		return self.AllowanceForDoubtfulAccountsIOAByGroup

	def getAllowanceForDoubtfulAccountsAccountsReceivableTrade(self): #貸倒引当金、売掛金
		return self.AllowanceForDoubtfulAccountsAccountsReceivableTrade

	def getAllowanceForDoubtfulAccountsLongTermLoansReceivable(self): #貸倒引当金、長期貸付金
		return self.AllowanceForDoubtfulAccountsLongTermLoansReceivable

	def getAllowanceForDoubtfulAccountsClaimsInBankruptcyReorganizationClaimsAndOther(self): #貸倒引当金、破産更生債権等
		return self.AllowanceForDoubtfulAccountsClaimsInBankruptcyReorganizationClaimsAndOther

	def getNotesRegardingAccumulatedDepreciationOfPropertyPlantAndEquipmentTextBlock(self): #有形固定資産の減価償却累計額の注記 [テキストブロック]
		return self.NotesRegardingAccumulatedDepreciationOfPropertyPlantAndEquipmentTextBlock

	def getAccumulatedDepreciationPPEByGroup(self): #減価償却累計額、有形固定資産、一括控除
		return self.AccumulatedDepreciationPPEByGroup

	def getAccumulatedDepreciationBuildings(self): #減価償却累計額、建物
		return self.AccumulatedDepreciationBuildings

	def getAccumulatedDepreciationStructures(self): #減価償却累計額、構築物
		return self.AccumulatedDepreciationStructures

	def getAccumulatedDepreciationMachineryAndEquipment(self): #減価償却累計額、機械及び装置
		return self.AccumulatedDepreciationMachineryAndEquipment

	def getNotesRegardingAmountsOfReductionEntryOfPropertyPlantAndEquipmentTextBlock(self): #有形固定資産の圧縮記帳額の注記 [テキストブロック]
		return self.NotesRegardingAmountsOfReductionEntryOfPropertyPlantAndEquipmentTextBlock

	def getNotesRegardingPresentationOfAccumulatedImpairmentLossTextBlock(self): #減損損失累計額の表示に関する注記 [テキストブロック]
		return self.NotesRegardingPresentationOfAccumulatedImpairmentLossTextBlock

	def getNotesRegardingAssetsAndLiabilitiesIncurredFromTransactionsWithAffiliatedEntitiesTextBlock(self): #関係会社に関する資産・負債の注記 [テキストブロック]
		return self.NotesRegardingAssetsAndLiabilitiesIncurredFromTransactionsWithAffiliatedEntitiesTextBlock

	def getNotesRegardingRevaluationOfNonCurrentAssetsTextBlock(self): #固定資産の再評価に関する注記 [テキストブロック]
		return self.NotesRegardingRevaluationOfNonCurrentAssetsTextBlock

	def getNotesRegardingRevaluationOfLandForBusinessTextBlock(self): #事業用土地の再評価に関する注記 [テキストブロック]
		return self.NotesRegardingRevaluationOfLandForBusinessTextBlock

	def getNotesRegardingPledgedAssetsTextBlock(self): #担保に供している資産の注記 [テキストブロック]
		return self.NotesRegardingPledgedAssetsTextBlock

	def getNotesRegardingPresentationOfInventoriesAndProvisionForLossOnConstructionContractsTextBlock(self): #棚卸資産及び工事損失引当金の表示に関する注記 [テキストブロック]
		return self.NotesRegardingPresentationOfInventoriesAndProvisionForLossOnConstructionContractsTextBlock

	def getNotesRegardingAmountOfContractLiabilitiesTextBlock(self): #契約負債の金額の注記 [テキストブロック]
		return self.NotesRegardingAmountOfContractLiabilitiesTextBlock

	def getContractLiabilities(self): #契約負債
		return self.ContractLiabilities

	def getNotesRegardingReservesUnderSpecialLawsTextBlock(self): #特別法上の準備金等に関する注記 [テキストブロック]
		return self.NotesRegardingReservesUnderSpecialLawsTextBlock

	def getNotesRegardingProvisionIncurredFromBusinessCombinationTextBlock(self): #企業結合に係る特定勘定の注記 [テキストブロック]
		return self.NotesRegardingProvisionIncurredFromBusinessCombinationTextBlock

	def getNotesRegardingGuaranteeObligationsTextBlock(self): #保証債務の注記 [テキストブロック]
		return self.NotesRegardingGuaranteeObligationsTextBlock

	def getNotesRegardingTradeNotesReceivableDiscountedOrTransferredByEndorsementTextBlock(self): #受取手形割引高及び（又は）受取手形裏書譲渡高 [テキストブロック]
		return self.NotesRegardingTradeNotesReceivableDiscountedOrTransferredByEndorsementTextBlock

	def getDiscountedTradeNotesReceivable(self): #受取手形割引高
		return self.DiscountedTradeNotesReceivable

	def getTradeNotesReceivableTransferredByEndorsement(self): #受取手形裏書譲渡高
		return self.TradeNotesReceivableTransferredByEndorsement

	def getNotesRegardingDepositForSubscriptionsToSharesTextBlock(self): #新株式申込証拠金に関する注記 [テキストブロック]
		return self.NotesRegardingDepositForSubscriptionsToSharesTextBlock

	def getNotesRegardingLimitationsOnDividendTextBlock(self): #配当制限に関する注記 [テキストブロック]
		return self.NotesRegardingLimitationsOnDividendTextBlock

	def getNotesRegardingPresentationOfNetAssetsOfDesignatedCorporationTextBlock(self): #指定法人の純資産の記載に関する注記 [テキストブロック]
		return self.NotesRegardingPresentationOfNetAssetsOfDesignatedCorporationTextBlock

	def getNotesRegardingPromissoryNotesDueOnBalanceSheetDateTextBlock(self): #期末日満期手形の会計処理 [テキストブロック]
		return self.NotesRegardingPromissoryNotesDueOnBalanceSheetDateTextBlock

	def getOtherElementsForNotesBalanceSheetAbstract(self): #貸借対照表関係のその他の要素 [タイトル項目]
		return self.OtherElementsForNotesBalanceSheetAbstract

	def getNotesRegardingLoanedWhichBorrowerHasRightToSellOrRepledgeTextBlock(self): #消費貸借契約及び（又は）消費寄託契約により貸し付けている有価証券に関する注記 [テキストブロック]
		return self.NotesRegardingLoanedWhichBorrowerHasRightToSellOrRepledgeTextBlock

	def getNotesRegardingFinancialAssetsBorrowedWhichBorrowerHasRightToSellOrRepledgeTextBlock(self): #自由処分権を有する担保受入金融資産に関する注記 [テキストブロック]
		return self.NotesRegardingFinancialAssetsBorrowedWhichBorrowerHasRightToSellOrRepledgeTextBlock

	def getNotesRegardingLoanedSecuritiesAndFinancialAssetsBorrowedWhichBorrowerHasRightToSellOrRepledgeTextBlock(self): #有価証券の消費貸借契約・消費寄託契約及び自由処分権を有する担保受入金融資産に関する注記 [テキストブロック]
		return self.NotesRegardingLoanedSecuritiesAndFinancialAssetsBorrowedWhichBorrowerHasRightToSellOrRepledgeTextBlock

	def getNotesRegardingLoanParticipationsTextBlock(self): #ローン・パーティシペーションに関する注記 [テキストブロック]
		return self.NotesRegardingLoanParticipationsTextBlock

	def getCreditorsNotesRegardingOverdraftContractsAndOrLoanCommitmentsTextBlock(self): #当座貸越契約及び（又は）貸出コミットメントに関する貸手の注記 [テキストブロック]
		return self.CreditorsNotesRegardingOverdraftContractsAndOrLoanCommitmentsTextBlock

	def getDebtorsNotesRegardingOverdraftContractsAndOrLoanCommitmentsTextBlock(self): #当座貸越契約及び（又は）貸出コミットメントに関する借手の注記 [テキストブロック]
		return self.DebtorsNotesRegardingOverdraftContractsAndOrLoanCommitmentsTextBlock

	def getNotesRegardingTotalAmountsOfSharesOfAndOrLoansToAffiliatedEntitiesTextBlock(self): #関係会社の株式及び（又は）出資金の総額 [テキストブロック]
		return self.NotesRegardingTotalAmountsOfSharesOfAndOrLoansToAffiliatedEntitiesTextBlock

	def getNotesRegardingTotalAmountsOfSharesOfAndOrLoansToUnconsolidatedSubsidiariesAndAssociatesTextBlock(self): #非連結子会社及び関連会社の株式及び（又は）出資金の総額 [テキストブロック]
		return self.NotesRegardingTotalAmountsOfSharesOfAndOrLoansToUnconsolidatedSubsidiariesAndAssociatesTextBlock

	def getNotesRegardingSubordinatedBorrowingsTextBlock(self): #劣後特約付借入金に関する注記 [テキストブロック]
		return self.NotesRegardingSubordinatedBorrowingsTextBlock

	def getNotesRegardingSubordinatedBondsPayableTextBlock(self): #劣後特約付社債に関する注記 [テキストブロック]
		return self.NotesRegardingSubordinatedBondsPayableTextBlock

	def getNotesRegardingGuaranteeObligationForCorporateBondsIncludedInAssetsTextBlock(self): #資産の部の社債に係る保証債務に関する注記 [テキストブロック]
		return self.NotesRegardingGuaranteeObligationForCorporateBondsIncludedInAssetsTextBlock

	def getOtherElementsForNotesBalanceSheetOfBankAbstract(self): #銀行業の貸借対照表関係のその他の要素 [タイトル項目]
		return self.OtherElementsForNotesBalanceSheetOfBankAbstract

	def getNotesRegardingLoansBasedOnBankingActAndActOnEmergencyMeasuresForRevitalizationOfFinancialFunctionsBNKTextBlock(self): #銀行法及び金融機能の再生のための緊急措置に関する法律に基づく債権に関する注記、銀行業 [テキストブロック]
		return self.NotesRegardingLoansBasedOnBankingActAndActOnEmergencyMeasuresForRevitalizationOfFinancialFunctionsBNKTextBlock

	def getNotesRegardingBillsDiscountedInBankingIndustryBNKTextBlock(self): #銀行業における手形割引に関する注記、銀行業 [テキストブロック]
		return self.NotesRegardingBillsDiscountedInBankingIndustryBNKTextBlock

	def getOtherElementsForNotesBalanceSheetOfSecuritiesRelatedBusinessAbstract(self): #第一種金融商品取引業の貸借対照表関係のその他の要素 [タイトル項目]
		return self.OtherElementsForNotesBalanceSheetOfSecuritiesRelatedBusinessAbstract

	def getNotesRegardingMarketValueOfSecuritiesPledgedToCounterpartiesSECTextBlock(self): #差し入れた有価証券等の時価の注記、第一種金融商品取引業 [テキストブロック]
		return self.NotesRegardingMarketValueOfSecuritiesPledgedToCounterpartiesSECTextBlock

	def getNotesRegardingMarketValueOfSecuritiesReceivedAsCollateralFromCounterpartiesSECTextBlock(self): #差し入れを受けた有価証券等の時価の注記、第一種金融商品取引業 [テキストブロック]
		return self.NotesRegardingMarketValueOfSecuritiesReceivedAsCollateralFromCounterpartiesSECTextBlock

	def getBreakdownOfTradingAccountSecuritiesEtcSECTextBlock(self): #商品有価証券等の内訳、第一種金融商品取引業 [テキストブロック]
		return self.BreakdownOfTradingAccountSecuritiesEtcSECTextBlock

	def getOtherElementsForNotesBalanceSheetOfInsuranceAbstract(self): #保険業の貸借対照表関係のその他の要素 [タイトル項目]
		return self.OtherElementsForNotesBalanceSheetOfInsuranceAbstract

	def getNotesRegardingLoansBasedOnInsuranceBusinessActINSTextBlock(self): #保険業法に基づく債権に関する注記、保険業 [テキストブロック]
		return self.NotesRegardingLoansBasedOnInsuranceBusinessActINSTextBlock

	def getNotesRegardingAssetsAndLiabilitiesIncludedInSpecificAccountsSpecifiedByArticle118OfInsuranceBusinessActINSTextBlock(self): #保険業法第118条に規定する特別勘定の資産及び負債に関する注記、保険業 [テキストブロック]
		return self.NotesRegardingAssetsAndLiabilitiesIncludedInSpecificAccountsSpecifiedByArticle118OfInsuranceBusinessActINSTextBlock

	def getNotesRegardingDeferredAssetsIncludedInOtherAssetsSpecifiedByArticle113OfInsuranceBusinessActTextBlock(self): #その他資産に含まれている保険業法第113条に規定する事業費の繰延額の注記 [テキストブロック]
		return self.NotesRegardingDeferredAssetsIncludedInOtherAssetsSpecifiedByArticle113OfInsuranceBusinessActTextBlock

	def getNotesRegardingIncreaseAndDecreaseInReserveForPolicyholderDividendsAndPaymentsOfPolicyholderDividendsINSTextBlock(self): #契約者配当準備金の増減異動及び契約者配当金の支払額に関する注記、保険業 [テキストブロック]
		return self.NotesRegardingIncreaseAndDecreaseInReserveForPolicyholderDividendsAndPaymentsOfPolicyholderDividendsINSTextBlock

	def getNotesRegardingSurplusFromOrganizationChangeSpecifiedByArticle91OfInsuranceBusinessActINSTextBlock(self): #保険業法第91条の規定による組織変更剰余金額の注記、保険業 [テキストブロック]
		return self.NotesRegardingSurplusFromOrganizationChangeSpecifiedByArticle91OfInsuranceBusinessActINSTextBlock

	def getNotesRegardingReservesForOutstandingClaimsReinsuredINSTextBlock(self): #保険業法施行規則第73条第3項において準用する同規則第71条第1項に規定する再保険を付した部分に相当する支払備金の金額の注記、保険業 [テキストブロック]
		return self.NotesRegardingReservesForOutstandingClaimsReinsuredINSTextBlock

	def getNotesRegardingPolicyReservesReinsuredINSTextBlock(self): #保険業法施行規則第71条第1項に規定する再保険を付した部分に相当する責任準備金の金額の注記、保険業 [テキストブロック]
		return self.NotesRegardingPolicyReservesReinsuredINSTextBlock

	def getNotesRegardingObligationsToLifeInsurancePolicyholdersProtectionCorporationOfJapanINSTextBlock(self): #保険業法第259条の規定に基づく生命保険契約者保護機構に対する今後の負担見積額、保険業 [テキストブロック]
		return self.NotesRegardingObligationsToLifeInsurancePolicyholdersProtectionCorporationOfJapanINSTextBlock

	def getBreakdownOfOutstandingClaimsINSTextBlock(self): #支払備金の内訳、保険業 [テキストブロック]
		return self.BreakdownOfOutstandingClaimsINSTextBlock

	def getBreakdownOfPolicyReserveINSTextBlock(self): #責任準備金の内訳、保険業 [テキストブロック]
		return self.BreakdownOfPolicyReserveINSTextBlock

	def getOtherElementsForNotesBalanceSheetOfSpecificFinanceAbstract(self): #特定金融業の貸借対照表関係のその他の要素 [タイトル項目]
		return self.OtherElementsForNotesBalanceSheetOfSpecificFinanceAbstract

	def getNotesRegardingBadLoansSPFTextBlock(self): #不良債権に関する注記、特定金融業 [テキストブロック]
		return self.NotesRegardingBadLoansSPFTextBlock

	def getOtherElementsForNotesBalanceSheetOfCommodityFutureTradingAbstract(self): #商品先物取引業の貸借対照表関係のその他の要素 [タイトル項目]
		return self.OtherElementsForNotesBalanceSheetOfCommodityFutureTradingAbstract

	def getExplanationOfFuturesTransactionMarginCustomerCMDTextBlock(self): #委託者先物取引差金の説明、商品先物取引業 [テキストブロック]
		return self.ExplanationOfFuturesTransactionMarginCustomerCMDTextBlock

	def getNotesStatementOfIncomeHeading(self): #損益計算書関係 [目次項目]
		return self.NotesStatementOfIncomeHeading

	def getNotesStatementOfIncomeHeading(self): #損益計算書関係 [目次項目]
		return self.NotesStatementOfIncomeHeading

	def getNotesStatementOfIncomeTable(self): #損益計算書関係 [表]
		return self.NotesStatementOfIncomeTable

	def getConsolidatedOrNonConsolidatedAxis(self): #連結個別 [軸]
		return self.ConsolidatedOrNonConsolidatedAxis

	def getNonConsolidatedMember(self): #非連結又は個別 [メンバー]
		return self.NonConsolidatedMember

	def getNotesStatementOfIncomeLineItems(self): #損益計算書関係 [表示項目]
		return self.NotesStatementOfIncomeLineItems

	def getNotesRegardingAmountOfRevenueFromContractsWithCustomersTextBlock(self): #顧客との契約から生じる収益の金額の注記 [テキストブロック]
		return self.NotesRegardingAmountOfRevenueFromContractsWithCustomersTextBlock

	def getRevenueFromContractsWithCustomers(self): #顧客との契約から生じる収益
		return self.RevenueFromContractsWithCustomers

	def getNotesRegardingRevenueFromAffiliatedEntitiesTextBlock(self): #関係会社に対する売上高の注記 [テキストブロック]
		return self.NotesRegardingRevenueFromAffiliatedEntitiesTextBlock

	def getNotesRegardingLossOnConstructionContractsTextBlock(self): #工事損失引当金繰入額の注記 [テキストブロック]
		return self.NotesRegardingLossOnConstructionContractsTextBlock

	def getNotesRegardingWriteDownsOfInventoriesTextBlock(self): #棚卸資産の帳簿価額の切下げに関する注記 [テキストブロック]
		return self.NotesRegardingWriteDownsOfInventoriesTextBlock

	def getWriteDownsOfInventories(self): #棚卸資産帳簿価額切下額
		return self.WriteDownsOfInventories

	def getMajorComponentsOfSellingGeneralAndAdministrativeExpensesTextBlock(self): #主要な販売費及び一般管理費 [テキストブロック]
		return self.MajorComponentsOfSellingGeneralAndAdministrativeExpensesTextBlock

	def getDepreciationSGA(self): #減価償却費、販売費及び一般管理費
		return self.DepreciationSGA

	def getProvisionOfAllowanceForDoubtfulAccountsSGA(self): #貸倒引当金繰入額、販売費及び一般管理費
		return self.ProvisionOfAllowanceForDoubtfulAccountsSGA

	def getMajorComponentsOfSellingExpensesAbstract(self): #主要な販売費 [タイトル項目]
		return self.MajorComponentsOfSellingExpensesAbstract

	def getRetirementBenefitExpensesSellingExpenses(self): #退職給付費用、販売費
		return self.RetirementBenefitExpensesSellingExpenses

	def getDepreciationSellingExpenses(self): #減価償却費、販売費
		return self.DepreciationSellingExpenses

	def getProvisionForBonusesSellingExpenses(self): #賞与引当金繰入額、販売費
		return self.ProvisionForBonusesSellingExpenses

	def getMajorComponentsOfGeneralAndAdministrativeExpensesAbstract(self): #主要な一般管理費 [タイトル項目]
		return self.MajorComponentsOfGeneralAndAdministrativeExpensesAbstract

	def getRetirementBenefitExpensesGA(self): #退職給付費用、一般管理費
		return self.RetirementBenefitExpensesGA

	def getDepreciationGA(self): #減価償却費、一般管理費
		return self.DepreciationGA

	def getProvisionForBonusesGA(self): #賞与引当金繰入額、一般管理費
		return self.ProvisionForBonusesGA

	def getResearchAndDevelopmentExpensesIncludedInGeneralAndAdministrativeExpensesAndManufacturingCostForCurrentPeriodTextBlock(self): #一般管理費及び当期製造費用に含まれる研究開発費 [テキストブロック]
		return self.ResearchAndDevelopmentExpensesIncludedInGeneralAndAdministrativeExpensesAndManufacturingCostForCurrentPeriodTextBlock

	def getResearchAndDevelopmentExpensesIncludedInGeneralAndAdministrativeExpensesAndManufacturingCostForCurrentPeriod(self): #一般管理費及び当期製造費用に含まれる研究開発費
		return self.ResearchAndDevelopmentExpensesIncludedInGeneralAndAdministrativeExpensesAndManufacturingCostForCurrentPeriod

	def getResearchAndDevelopmentExpensesSGA(self): #研究開発費、販売費及び一般管理費
		return self.ResearchAndDevelopmentExpensesSGA

	def getNotesRegardingOperatingExpensesIncurredFromTransactionsWithAffiliatedEntitiesTextBlock(self): #関係会社に係る営業費用の注記 [テキストブロック]
		return self.NotesRegardingOperatingExpensesIncurredFromTransactionsWithAffiliatedEntitiesTextBlock

	def getNotesRegardingNonOperatingIncomeAndNonOperatingExpensesIncurredFromTransactionsWithAffiliatedEntitiesTextBlock(self): #関係会社に係る営業外収益・営業外費用の注記 [テキストブロック]
		return self.NotesRegardingNonOperatingIncomeAndNonOperatingExpensesIncurredFromTransactionsWithAffiliatedEntitiesTextBlock

	def getNotesRegardingTotalAmountOfOperatingTransactionsFromOrToAffiliatedEntitiesAndTotalAmountOfNonOperatingTransactionsFromOrToAffiliatedEntitiesTextBlock(self): #関係会社との営業取引による取引高の総額及び営業取引以外の取引による取引高の総額の注記 [テキストブロック]
		return self.NotesRegardingTotalAmountOfOperatingTransactionsFromOrToAffiliatedEntitiesAndTotalAmountOfNonOperatingTransactionsFromOrToAffiliatedEntitiesTextBlock

	def getNotesRegardingImpairmentLossTextBlock(self): #減損損失に関する注記 [テキストブロック]
		return self.NotesRegardingImpairmentLossTextBlock

	def getNotesRegardingReversalOfProvisionIncurredFromBusinessCombinationTextBlock(self): #企業結合に係る特定勘定の取崩益の注記 [テキストブロック]
		return self.NotesRegardingReversalOfProvisionIncurredFromBusinessCombinationTextBlock

	def getNotesRegardingGainOnSalesOfPropertyPlantAndEquipmentTextBlock(self): #固定資産売却益の注記 [テキストブロック]
		return self.NotesRegardingGainOnSalesOfPropertyPlantAndEquipmentTextBlock

	def getNotesRegardingLossOnSalesOfPropertyPlantAndEquipmentTextBlock(self): #固定資産売却損の注記 [テキストブロック]
		return self.NotesRegardingLossOnSalesOfPropertyPlantAndEquipmentTextBlock

	def getNotesRegardingLossOnDisposalOfPropertyPlantAndEquipmentTextBlock(self): #固定資産除却損の注記 [テキストブロック]
		return self.NotesRegardingLossOnDisposalOfPropertyPlantAndEquipmentTextBlock

	def getNotesRegardingLossOnDisposalAndSalesOfPropertyPlantAndEquipmentTextBlock(self): #固定資産除売却損の注記 [テキストブロック]
		return self.NotesRegardingLossOnDisposalAndSalesOfPropertyPlantAndEquipmentTextBlock

	def getOtherElementsForNotesStatementOfIncomeAbstract(self): #損益計算書関係のその他の要素 [タイトル項目]
		return self.OtherElementsForNotesStatementOfIncomeAbstract

	def getBreakdownOfBusinessCostTextBlock(self): #事業費の内訳 [テキストブロック]
		return self.BreakdownOfBusinessCostTextBlock

	def getBreakdownOfPersonnelExpensesTextBlock(self): #人件費の内訳 [テキストブロック]
		return self.BreakdownOfPersonnelExpensesTextBlock

	def getBreakdownOfGainOnSalesOfSecuritiesTextBlock(self): #有価証券売却益の内訳 [テキストブロック]
		return self.BreakdownOfGainOnSalesOfSecuritiesTextBlock

	def getBreakdownOfLossOnSalesOfSecuritiesTextBlock(self): #有価証券売却損の内訳 [テキストブロック]
		return self.BreakdownOfLossOnSalesOfSecuritiesTextBlock

	def getBreakdownOfLossOnValuationOfSecuritiesTextBlock(self): #有価証券評価損の内訳 [テキストブロック]
		return self.BreakdownOfLossOnValuationOfSecuritiesTextBlock

	def getNotesRegardingTransactionsWithAffiliatedEntitiesTextBlock(self): #関係会社との取引に関する注記 [テキストブロック]
		return self.NotesRegardingTransactionsWithAffiliatedEntitiesTextBlock

	def getOtherElementsForNotesStatementOfIncomeOfBankAbstract(self): #銀行業の損益計算書関係のその他の要素 [タイトル項目]
		return self.OtherElementsForNotesStatementOfIncomeOfBankAbstract

	def getMajorComponentsOfOtherIncomeBNKTextBlock(self): #その他の経常収益の主要な内訳、銀行業 [テキストブロック]
		return self.MajorComponentsOfOtherIncomeBNKTextBlock

	def getMajorComponentsOfOtherExpensesBNKTextBlock(self): #その他の経常費用の主要な内訳、銀行業 [テキストブロック]
		return self.MajorComponentsOfOtherExpensesBNKTextBlock

	def getOtherElementsForNotesStatementOfIncomeOfSecuritiesRelatedBusinessAbstract(self): #第一種金融商品取引業の損益計算書関係のその他の要素 [タイトル項目]
		return self.OtherElementsForNotesStatementOfIncomeOfSecuritiesRelatedBusinessAbstract

	def getBreakdownOfNetTradingIncomeSECTextBlock(self): #トレーディング損益の内訳、第一種金融商品取引業 [テキストブロック]
		return self.BreakdownOfNetTradingIncomeSECTextBlock

	def getBreakdownOfFinancialRevenueSECTextBlock(self): #金融収益の内訳、第一種金融商品取引業 [テキストブロック]
		return self.BreakdownOfFinancialRevenueSECTextBlock

	def getBreakdownOfFinancialExpensesSECTextBlock(self): #金融費用の内訳、第一種金融商品取引業 [テキストブロック]
		return self.BreakdownOfFinancialExpensesSECTextBlock

	def getOtherElementsForNotesStatementOfIncomeOfInsuranceAbstract(self): #保険業の損益計算書関係のその他の要素 [タイトル項目]
		return self.OtherElementsForNotesStatementOfIncomeOfInsuranceAbstract

	def getMajorComponentsOfBusinessCostTextBlock(self): #事業費の主な内訳 [テキストブロック]
		return self.MajorComponentsOfBusinessCostTextBlock

	def getAgentFeeEtcINSNonlife(self): #代理店手数料等、損害保険業
		return self.AgentFeeEtcINSNonlife

	def getSalariesINSNonlife(self): #給与、損害保険業
		return self.SalariesINSNonlife

	def getBreakdownOfNetPremiumsWrittenINSTextBlock(self): #正味収入保険料の内訳、保険業 [テキストブロック]
		return self.BreakdownOfNetPremiumsWrittenINSTextBlock

	def getBreakdownOfNetClaimsPaidINSTextBlock(self): #正味支払保険金の内訳、保険業 [テキストブロック]
		return self.BreakdownOfNetClaimsPaidINSTextBlock

	def getBreakdownOfCommissionsAndCollectionFeesINSTextBlock(self): #諸手数料及び集金費の内訳、保険業 [テキストブロック]
		return self.BreakdownOfCommissionsAndCollectionFeesINSTextBlock

	def getBreakdownOfProvisionForOrReversalOfOutstandingClaimsINSTextBlock(self): #支払備金繰入額又は支払備金戻入額の内訳、保険業 [テキストブロック]
		return self.BreakdownOfProvisionForOrReversalOfOutstandingClaimsINSTextBlock

	def getBreakdownOfProvisionForOrReversalOfUnderwritingReservesINSTextBlock(self): #責任準備金繰入額又は責任準備金戻入額の内訳、保険業 [テキストブロック]
		return self.BreakdownOfProvisionForOrReversalOfUnderwritingReservesINSTextBlock

	def getNotesRegardingReversalOfOrProvisionForReservesForOutstandingClaimsReinsuredINSTextBlock(self): #支払備金繰入額又は支払備金戻入額の計算上、差し引かれた又は足し上げられた出再支払備金繰入額又は出再支払備金戻入額の注記、保険業 [テキストブロック]
		return self.NotesRegardingReversalOfOrProvisionForReservesForOutstandingClaimsReinsuredINSTextBlock

	def getNotesRegardingReversalOfOrProvisionForPolicyReservesReinsuredINSTextBlock(self): #責任準備金繰入額又は責任準備金戻入額の計算上、差し引かれた又は足し上げられた出再責任準備金繰入額又は出再責任準備金戻入額の注記、保険業 [テキストブロック]
		return self.NotesRegardingReversalOfOrProvisionForPolicyReservesReinsuredINSTextBlock

	def getBreakdownOfInterestAndDividendIncomeBySourceAssetINSTextBlock(self): #利息及び配当金収入の資産源泉別内訳、保険業 [テキストブロック]
		return self.BreakdownOfInterestAndDividendIncomeBySourceAssetINSTextBlock

	def getInterestAndDividendIncomeGainLossOnSalesAndUnrealizedGainLossForEachOfTradingAccountSecuritiesINSTextBlock(self): #商品有価証券及び売買目的有価証券に係るそれぞれの利息及び配当金収入、売却損益及び評価損益の金額、保険業 [テキストブロック]
		return self.InterestAndDividendIncomeGainLossOnSalesAndUnrealizedGainLossForEachOfTradingAccountSecuritiesINSTextBlock

	def getNotesRegardingUnrealizedGainLossForMoneyTrustINSTextBlock(self): #金銭の信託に係る評価損益の金額の注記、保険業 [テキストブロック]
		return self.NotesRegardingUnrealizedGainLossForMoneyTrustINSTextBlock

	def getNotesRegardingUnrealizedGainLossForDerivativesINSTextBlock(self): #金融派生商品に係る評価損益の金額の注記、保険業 [テキストブロック]
		return self.NotesRegardingUnrealizedGainLossForDerivativesINSTextBlock

	def getMajorComponentsOfOtherExtraordinaryIncomeINSTextBlock(self): #その他特別利益の主な内訳、保険業 [テキストブロック]
		return self.MajorComponentsOfOtherExtraordinaryIncomeINSTextBlock

	def getMajorComponentsOfOtherExtraordinaryLossesINSTextBlock(self): #その他特別損失の主な内訳、保険業 [テキストブロック]
		return self.MajorComponentsOfOtherExtraordinaryLossesINSTextBlock

	def getOtherElementsForNotesStatementOfIncomeOfCommodityFutureTradingAbstract(self): #商品先物取引業の損益計算書関係のその他の要素 [タイトル項目]
		return self.OtherElementsForNotesStatementOfIncomeOfCommodityFutureTradingAbstract

	def getBreakdownOfBrokerageIncomeCMDTextBlock(self): #受取手数料の内訳、商品先物取引業 [テキストブロック]
		return self.BreakdownOfBrokerageIncomeCMDTextBlock

	def getBreakdownOfNetGainOnTradingCMDTextBlock(self): #売買損益の内訳、商品先物取引業 [テキストブロック]
		return self.BreakdownOfNetGainOnTradingCMDTextBlock

	def getExchangeRelatedExpensesCMDTextBlock(self): #取引所等関係費の内訳、商品先物取引業 [テキストブロック]
		return self.ExchangeRelatedExpensesCMDTextBlock

	def getNotesStatementOfChangesInEquityHeading(self): #株主資本等変動計算書関係 [目次項目]
		return self.NotesStatementOfChangesInEquityHeading

	def getNotesStatementOfChangesInEquityHeading(self): #株主資本等変動計算書関係 [目次項目]
		return self.NotesStatementOfChangesInEquityHeading

	def getNotesStatementOfChangesInEquityTable(self): #株主資本等変動計算書関係 [表]
		return self.NotesStatementOfChangesInEquityTable

	def getConsolidatedOrNonConsolidatedAxis(self): #連結個別 [軸]
		return self.ConsolidatedOrNonConsolidatedAxis

	def getNonConsolidatedMember(self): #非連結又は個別 [メンバー]
		return self.NonConsolidatedMember

	def getNotesStatementOfChangesInEquityLineItems(self): #株主資本等変動計算書関係 [表示項目]
		return self.NotesStatementOfChangesInEquityLineItems

	def getNotesRegardingIssuedSharesAndTreasurySharesTextBlock(self): #発行済株式及び自己株式に関する注記 [テキストブロック]
		return self.NotesRegardingIssuedSharesAndTreasurySharesTextBlock

	def getNotesRegardingTreasurySharesTextBlock(self): #自己株式に関する注記 [テキストブロック]
		return self.NotesRegardingTreasurySharesTextBlock

	def getNotesRegardingNewShareSubscriptionRightsEtcTextBlock(self): #新株予約権等に関する注記 [テキストブロック]
		return self.NotesRegardingNewShareSubscriptionRightsEtcTextBlock

	def getNotesRegardingDividendTextBlock(self): #配当に関する注記 [テキストブロック]
		return self.NotesRegardingDividendTextBlock

	def getNotesStatementOfCashFlowsHeading(self): #キャッシュ・フロー計算書関係 [目次項目]
		return self.NotesStatementOfCashFlowsHeading

	def getNotesStatementOfCashFlowsHeading(self): #キャッシュ・フロー計算書関係 [目次項目]
		return self.NotesStatementOfCashFlowsHeading

	def getNotesStatementOfCashFlowsTable(self): #キャッシュ・フロー計算書関係 [表]
		return self.NotesStatementOfCashFlowsTable

	def getConsolidatedOrNonConsolidatedAxis(self): #連結個別 [軸]
		return self.ConsolidatedOrNonConsolidatedAxis

	def getNonConsolidatedMember(self): #非連結又は個別 [メンバー]
		return self.NonConsolidatedMember

	def getNotesStatementOfCashFlowsLineItems(self): #キャッシュ・フロー計算書関係 [表示項目]
		return self.NotesStatementOfCashFlowsLineItems

	def getReconciliationOfEndingBalanceOfCashAndCashEquivalentsWithAccountBalancesPerBalanceSheetTextBlock(self): #現金及び現金同等物の期末残高と貸借対照表に掲記されている科目の金額との関係 [テキストブロック]
		return self.ReconciliationOfEndingBalanceOfCashAndCashEquivalentsWithAccountBalancesPerBalanceSheetTextBlock

	def getMajorComponentsOfAssetsAndLiabilitiesIncreasedOrDecreasedAsResultOfAcquisitionOrDisposalOfBusinessOrMergerEtcWherebyCashWasPaidOrReceivedAsConsiderationTextBlock(self): #現金及び現金同等物を対価とする事業の譲受け若しくは譲渡又は合併等を行った場合には、当該事業の譲受け若しくは譲渡又は合併等により増加又は減少した資産及び負債の主な内訳 [テキストブロック]
		return self.MajorComponentsOfAssetsAndLiabilitiesIncreasedOrDecreasedAsResultOfAcquisitionOrDisposalOfBusinessOrMergerEtcWherebyCashWasPaidOrReceivedAsConsiderationTextBlock

	def getDescriptionOfSignificantTransactionsNotRequiringUseOfCashOrCashEquivalentsTextBlock(self): #重要な非資金取引の内容 [テキストブロック]
		return self.DescriptionOfSignificantTransactionsNotRequiringUseOfCashOrCashEquivalentsTextBlock

	def getDescriptionOfFactThatCashFlowsFromUsedInInvestingActivitiesIncludeCashFlowsFromAssetManagementActivitiesRelatedToInsuranceBusinessINSTextBlock(self): #投資活動によるキャッシュ・フローには、保険事業に係る資産運用業務から生じるキャッシュ・フローを含んでいる旨、保険業 [テキストブロック]
		return self.DescriptionOfFactThatCashFlowsFromUsedInInvestingActivitiesIncludeCashFlowsFromAssetManagementActivitiesRelatedToInsuranceBusinessINSTextBlock

	def getNotesLeasesFinancialStatementsHeading(self): #リース取引関係、財務諸表 [目次項目]
		return self.NotesLeasesFinancialStatementsHeading

	def getNotesLeasesFinancialStatementsTextBlock(self): #リース取引関係、財務諸表 [テキストブロック]
		return self.NotesLeasesFinancialStatementsTextBlock

	def getNotesFinancialInstrumentsFinancialStatementsHeading(self): #金融商品関係、財務諸表 [目次項目]
		return self.NotesFinancialInstrumentsFinancialStatementsHeading

	def getNotesFinancialInstrumentsFinancialStatementsTextBlock(self): #金融商品関係、財務諸表 [テキストブロック]
		return self.NotesFinancialInstrumentsFinancialStatementsTextBlock

	def getNotesSecuritiesFinancialStatementsHeading(self): #有価証券関係、財務諸表 [目次項目]
		return self.NotesSecuritiesFinancialStatementsHeading

	def getNotesSecuritiesFinancialStatementsTextBlock(self): #有価証券関係、財務諸表 [テキストブロック]
		return self.NotesSecuritiesFinancialStatementsTextBlock

	def getNotesMoneyHeldInTrustFinancialStatementsHeading(self): #金銭の信託関係、財務諸表 [目次項目]
		return self.NotesMoneyHeldInTrustFinancialStatementsHeading

	def getNotesMoneyHeldInTrustFinancialStatementsTextBlock(self): #金銭の信託関係、財務諸表 [テキストブロック]
		return self.NotesMoneyHeldInTrustFinancialStatementsTextBlock

	def getNotesValuationDifferenceOnAvailableForSaleSecuritiesFinancialStatementsHeading(self): #その他有価証券評価差額金、財務諸表 [目次項目]
		return self.NotesValuationDifferenceOnAvailableForSaleSecuritiesFinancialStatementsHeading

	def getNotesValuationDifferenceOnAvailableForSaleSecuritiesFinancialStatementsTextBlock(self): #その他有価証券評価差額金、財務諸表 [テキストブロック]
		return self.NotesValuationDifferenceOnAvailableForSaleSecuritiesFinancialStatementsTextBlock

	def getNotesDerivativesFinancialStatementsHeading(self): #デリバティブ取引関係、財務諸表 [目次項目]
		return self.NotesDerivativesFinancialStatementsHeading

	def getNotesDerivativesFinancialStatementsTextBlock(self): #デリバティブ取引関係、財務諸表 [テキストブロック]
		return self.NotesDerivativesFinancialStatementsTextBlock

	def getNotesRetirementBenefitsFinancialStatementsHeading(self): #退職給付関係、財務諸表 [目次項目]
		return self.NotesRetirementBenefitsFinancialStatementsHeading

	def getNotesRetirementBenefitsFinancialStatementsTextBlock(self): #退職給付関係、財務諸表 [テキストブロック]
		return self.NotesRetirementBenefitsFinancialStatementsTextBlock

	def getNotesShareOptionsEtcFinancialStatementsHeading(self): #ストック・オプション等関係、財務諸表 [目次項目]
		return self.NotesShareOptionsEtcFinancialStatementsHeading

	def getNotesShareOptionsEtcFinancialStatementsTextBlock(self): #ストック・オプション等関係、財務諸表 [テキストブロック]
		return self.NotesShareOptionsEtcFinancialStatementsTextBlock

	def getNotesTaxEffectAccountingFinancialStatementsHeading(self): #税効果会計関係、財務諸表 [目次項目]
		return self.NotesTaxEffectAccountingFinancialStatementsHeading

	def getNotesTaxEffectAccountingFinancialStatementsTextBlock(self): #税効果会計関係、財務諸表 [テキストブロック]
		return self.NotesTaxEffectAccountingFinancialStatementsTextBlock

	def getNotesBusinessCombinationsFinancialStatementsHeading(self): #企業結合等関係、財務諸表 [目次項目]
		return self.NotesBusinessCombinationsFinancialStatementsHeading

	def getNotesBusinessCombinationsFinancialStatementsTextBlock(self): #企業結合等関係、財務諸表 [テキストブロック]
		return self.NotesBusinessCombinationsFinancialStatementsTextBlock

	def getNotesAssetRetirementObligationsFinancialStatementsHeading(self): #資産除去債務関係、財務諸表 [目次項目]
		return self.NotesAssetRetirementObligationsFinancialStatementsHeading

	def getNotesAssetRetirementObligationsFinancialStatementsTextBlock(self): #資産除去債務関係、財務諸表 [テキストブロック]
		return self.NotesAssetRetirementObligationsFinancialStatementsTextBlock

	def getNotesRealEstateForLeaseEtcFinancialStatementsHeading(self): #賃貸等不動産関係、財務諸表 [目次項目]
		return self.NotesRealEstateForLeaseEtcFinancialStatementsHeading

	def getNotesRealEstateForLeaseEtcFinancialStatementsTextBlock(self): #賃貸等不動産関係、財務諸表 [テキストブロック]
		return self.NotesRealEstateForLeaseEtcFinancialStatementsTextBlock

	def getNotesRevenueRecognitionFinancialStatementsHeading(self): #収益認識関係、財務諸表 [目次項目]
		return self.NotesRevenueRecognitionFinancialStatementsHeading

	def getNotesRevenueRecognitionFinancialStatementsTextBlock(self): #収益認識関係、財務諸表 [テキストブロック]
		return self.NotesRevenueRecognitionFinancialStatementsTextBlock

	def getNotesInventoriesFinancialStatementsHeading(self): #棚卸資産関係、財務諸表 [目次項目]
		return self.NotesInventoriesFinancialStatementsHeading

	def getNotesInventoriesFinancialStatementsTextBlock(self): #棚卸資産関係、財務諸表 [テキストブロック]
		return self.NotesInventoriesFinancialStatementsTextBlock

	def getNotesSegmentInformationEtcFinancialStatementsHeading(self): #セグメント情報等、財務諸表 [目次項目]
		return self.NotesSegmentInformationEtcFinancialStatementsHeading

	def getNotesSegmentInformationEtcFinancialStatementsTextBlock(self): #セグメント情報等、財務諸表 [テキストブロック]
		return self.NotesSegmentInformationEtcFinancialStatementsTextBlock

	def getNotesSegmentInformationEtcFinancialStatementsHeading(self): #セグメント情報等、財務諸表 [目次項目]
		return self.NotesSegmentInformationEtcFinancialStatementsHeading

	def getNotesSegmentInformationEtcFinancialStatementsTable(self): #セグメント情報等、財務諸表 [表]
		return self.NotesSegmentInformationEtcFinancialStatementsTable

	def getConsolidatedOrNonConsolidatedAxis(self): #連結個別 [軸]
		return self.ConsolidatedOrNonConsolidatedAxis

	def getNonConsolidatedMember(self): #非連結又は個別 [メンバー]
		return self.NonConsolidatedMember

	def getNotesSegmentInformationEtcFinancialStatementsLineItems(self): #セグメント情報等、財務諸表 [表示項目]
		return self.NotesSegmentInformationEtcFinancialStatementsLineItems

	def getSegmentInformationAbstract(self): #セグメント情報 [タイトル項目]
		return self.SegmentInformationAbstract

	def getDescriptionOfReportableSegmentsTextBlock(self): #報告セグメントの概要 [テキストブロック]
		return self.DescriptionOfReportableSegmentsTextBlock

	def getDisclosureOfChangesInReportableSegmentsTextBlock(self): #報告セグメントの変更に関する事項 [テキストブロック]
		return self.DisclosureOfChangesInReportableSegmentsTextBlock

	def getDescriptionOfFactThatCompanysBusinessComprisesSingleSegment(self): #単一セグメントである旨
		return self.DescriptionOfFactThatCompanysBusinessComprisesSingleSegment

	def getExplanationOfMeasurementsOfSalesProfitLossAssetLiabilityAndOtherItemsForEachReportableSegmentTextBlock(self): #報告セグメントごとの売上高、利益又は損失、資産、負債その他の項目の金額の算定方法 [テキストブロック]
		return self.ExplanationOfMeasurementsOfSalesProfitLossAssetLiabilityAndOtherItemsForEachReportableSegmentTextBlock

	def getNotesSegmentInformationEtcFinancialStatementsHeading(self): #セグメント情報等、財務諸表 [目次項目]
		return self.NotesSegmentInformationEtcFinancialStatementsHeading

	def getSegmentInformationAbstract(self): #セグメント情報 [タイトル項目]
		return self.SegmentInformationAbstract

	def getDisclosureOfSalesProfitLossAssetLiabilityAndOtherItemsForEachReportableSegmentTable(self): #報告セグメントごとの売上高、利益又は損失、資産、負債その他の項目の金額に関する情報 [表]
		return self.DisclosureOfSalesProfitLossAssetLiabilityAndOtherItemsForEachReportableSegmentTable

	def getConsolidatedOrNonConsolidatedAxis(self): #連結個別 [軸]
		return self.ConsolidatedOrNonConsolidatedAxis

	def getNonConsolidatedMember(self): #非連結又は個別 [メンバー]
		return self.NonConsolidatedMember

	def getOperatingSegmentsAxis(self): #事業セグメント [軸]
		return self.OperatingSegmentsAxis

	def getEntityTotalMember(self): #連結合計又は会社合計 [メンバー] ※ディメンションデフォルト
		return self.EntityTotalMember

	def getTotalOfReportableSegmentsAndOthersMember(self): #報告セグメント及びその他の合計 [メンバー]
		return self.TotalOfReportableSegmentsAndOthersMember

	def getReportableSegmentsMember(self): #報告セグメント [メンバー]
		return self.ReportableSegmentsMember

	def getOtherReportableSegmentsMember(self): #その他の報告セグメント [メンバー]
		return self.OtherReportableSegmentsMember

	def getOperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember(self): #報告セグメント以外の全てのセグメント [メンバー]
		return self.OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember

	def getReconcilingItemsMember(self): #調整項目 [メンバー]
		return self.ReconcilingItemsMember

	def getDisclosureOfSalesProfitLossAssetLiabilityAndOtherItemsForEachReportableSegmentLineItems(self): #報告セグメントごとの売上高、利益又は損失、資産、負債その他の項目の金額に関する情報 [表示項目]
		return self.DisclosureOfSalesProfitLossAssetLiabilityAndOtherItemsForEachReportableSegmentLineItems

	def getSalesSegmentInformationAbstract(self): #売上高、セグメント情報 [タイトル項目]
		return self.SalesSegmentInformationAbstract

	def getRevenuesFromExternalCustomers(self): #外部顧客への売上高
		return self.RevenuesFromExternalCustomers

	def getTransactionsWithOtherSegments(self): #セグメント間の内部売上高又は振替高
		return self.TransactionsWithOtherSegments

	def getNetSales(self): #売上高
		return self.NetSales

	def getOperatingRevenue1(self): #営業収益
		return self.OperatingRevenue1

	def getOperatingRevenue2(self): #営業収入
		return self.OperatingRevenue2

	def getGrossOperatingRevenue(self): #営業総収入
		return self.GrossOperatingRevenue

	def getOrdinaryIncomeBNK(self): #経常収益、銀行業
		return self.OrdinaryIncomeBNK

	def getOperatingIncomeINS(self): #経常収益、保険業
		return self.OperatingIncomeINS

	def getSegmentProfitLossAbstract(self): #セグメント利益又は損失（△） [タイトル項目]
		return self.SegmentProfitLossAbstract

	def getOperatingIncome(self): #営業利益又は営業損失（△）
		return self.OperatingIncome

	def getOrdinaryIncome(self): #経常利益又は経常損失（△）
		return self.OrdinaryIncome

	def getIncomeBeforeIncomeTaxes(self): #税引前当期純利益又は税引前当期純損失（△）
		return self.IncomeBeforeIncomeTaxes

	def getProfitLoss(self): #当期純利益又は当期純損失（△）（平成26年3月28日財規等改正後）
		return self.ProfitLoss

	def getAssets(self): #資産
		return self.Assets

	def getLiabilities(self): #負債
		return self.Liabilities

	def getOtherItemsSegmentInformationAbstract(self): #その他の項目、セグメント情報 [タイトル項目]
		return self.OtherItemsSegmentInformationAbstract

	def getDepreciationSegmentInformation(self): #減価償却費、セグメント情報
		return self.DepreciationSegmentInformation

	def getAmortizationOfGoodwillSGA(self): #のれん償却額、販売費及び一般管理費
		return self.AmortizationOfGoodwillSGA

	def getInterestIncomeNOI(self): #受取利息、営業外収益
		return self.InterestIncomeNOI

	def getInterestExpensesNOE(self): #支払利息、営業外費用
		return self.InterestExpensesNOE

	def getExtraordinaryIncome(self): #特別利益
		return self.ExtraordinaryIncome

	def getGainOnNegativeGoodwillEI(self): #負ののれん発生益、特別利益
		return self.GainOnNegativeGoodwillEI

	def getExtraordinaryLoss(self): #特別損失
		return self.ExtraordinaryLoss

	def getImpairmentLossEL(self): #減損損失、特別損失
		return self.ImpairmentLossEL

	def getIncomeTaxExpense(self): #税金費用
		return self.IncomeTaxExpense

	def getIncreaseInPropertyPlantAndEquipmentAndIntangibleAssets(self): #有形固定資産及び無形固定資産の増加額
		return self.IncreaseInPropertyPlantAndEquipmentAndIntangibleAssets

	def getNotesSegmentInformationEtcFinancialStatementsHeading(self): #セグメント情報等、財務諸表 [目次項目]
		return self.NotesSegmentInformationEtcFinancialStatementsHeading

	def getNotesSegmentInformationEtcFinancialStatementsTable(self): #セグメント情報等、財務諸表 [表]
		return self.NotesSegmentInformationEtcFinancialStatementsTable

	def getConsolidatedOrNonConsolidatedAxis(self): #連結個別 [軸]
		return self.ConsolidatedOrNonConsolidatedAxis

	def getNonConsolidatedMember(self): #非連結又は個別 [メンバー]
		return self.NonConsolidatedMember

	def getNotesSegmentInformationEtcFinancialStatementsLineItems(self): #セグメント情報等、財務諸表 [表示項目]
		return self.NotesSegmentInformationEtcFinancialStatementsLineItems

	def getSegmentInformationAbstract(self): #セグメント情報 [タイトル項目]
		return self.SegmentInformationAbstract

	def getFootnotesRegardingSegmentInformationTableTextBlock(self): #セグメント表の脚注 [テキストブロック]
		return self.FootnotesRegardingSegmentInformationTableTextBlock

	def getDescriptionOfNatureAndAmountsOfDifferencesBetweenReportableSegmentsTotalAndFinancialStatementsTextBlock(self): #報告セグメント合計額と財務諸表計上額との差額及び当該差額の主な内容（差異調整に関する事項） [テキストブロック]
		return self.DescriptionOfNatureAndAmountsOfDifferencesBetweenReportableSegmentsTotalAndFinancialStatementsTextBlock

	def getNotesInformationAssociatedWithReportableSegmentsAbstract(self): #関連情報 [タイトル項目]
		return self.NotesInformationAssociatedWithReportableSegmentsAbstract

	def getInformationForEachProductOrServiceTextBlock(self): #製品及びサービスごとの情報 [テキストブロック]
		return self.InformationForEachProductOrServiceTextBlock

	def getInformationForEachRegionAbstract(self): #地域ごとの情報 [タイトル項目]
		return self.InformationForEachRegionAbstract

	def getRevenuesFromExternalCustomersInformationForEachRegionTextBlock(self): #売上高、地域ごとの情報 [テキストブロック]
		return self.RevenuesFromExternalCustomersInformationForEachRegionTextBlock

	def getPropertyPlantAndEquipmentInformationForEachRegionTextBlock(self): #有形固定資産、地域ごとの情報 [テキストブロック]
		return self.PropertyPlantAndEquipmentInformationForEachRegionTextBlock

	def getInformationForEachOfMainCustomersTextBlock(self): #主要な顧客ごとの情報 [テキストブロック]
		return self.InformationForEachOfMainCustomersTextBlock

	def getNotesSegmentInformationEtcFinancialStatementsHeading(self): #セグメント情報等、財務諸表 [目次項目]
		return self.NotesSegmentInformationEtcFinancialStatementsHeading

	def getDisclosureOfImpairmentLossOnNonCurrentAssetsForEachReportableSegmentAbstract(self): #報告セグメントごとの固定資産の減損損失に関する情報 [タイトル項目]
		return self.DisclosureOfImpairmentLossOnNonCurrentAssetsForEachReportableSegmentAbstract

	def getDisclosureOfImpairmentLossOnNonCurrentAssetsForEachReportableSegmentTable(self): #報告セグメントごとの固定資産の減損損失に関する情報 [表]
		return self.DisclosureOfImpairmentLossOnNonCurrentAssetsForEachReportableSegmentTable

	def getConsolidatedOrNonConsolidatedAxis(self): #連結個別 [軸]
		return self.ConsolidatedOrNonConsolidatedAxis

	def getNonConsolidatedMember(self): #非連結又は個別 [メンバー]
		return self.NonConsolidatedMember

	def getOperatingSegmentsAxis(self): #事業セグメント [軸]
		return self.OperatingSegmentsAxis

	def getEntityTotalMember(self): #連結合計又は会社合計 [メンバー] ※ディメンションデフォルト
		return self.EntityTotalMember

	def getReportableSegmentsMember(self): #報告セグメント [メンバー]
		return self.ReportableSegmentsMember

	def getOtherReportableSegmentsMember(self): #その他の報告セグメント [メンバー]
		return self.OtherReportableSegmentsMember

	def getOperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember(self): #報告セグメント以外の全てのセグメント [メンバー]
		return self.OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember

	def getUnallocatedAmountsAndEliminationMember(self): #全社・消去 [メンバー]
		return self.UnallocatedAmountsAndEliminationMember

	def getDisclosureOfImpairmentLossOnNonCurrentAssetsForEachReportableSegmentLineItems(self): #報告セグメントごとの固定資産の減損損失に関する情報 [表示項目]
		return self.DisclosureOfImpairmentLossOnNonCurrentAssetsForEachReportableSegmentLineItems

	def getImpairmentLossEL(self): #減損損失、特別損失
		return self.ImpairmentLossEL

	def getNotesSegmentInformationEtcFinancialStatementsHeading(self): #セグメント情報等、財務諸表 [目次項目]
		return self.NotesSegmentInformationEtcFinancialStatementsHeading

	def getNotesSegmentInformationEtcFinancialStatementsTable(self): #セグメント情報等、財務諸表 [表]
		return self.NotesSegmentInformationEtcFinancialStatementsTable

	def getConsolidatedOrNonConsolidatedAxis(self): #連結個別 [軸]
		return self.ConsolidatedOrNonConsolidatedAxis

	def getNonConsolidatedMember(self): #非連結又は個別 [メンバー]
		return self.NonConsolidatedMember

	def getNotesSegmentInformationEtcFinancialStatementsLineItems(self): #セグメント情報等、財務諸表 [表示項目]
		return self.NotesSegmentInformationEtcFinancialStatementsLineItems

	def getDescriptionOfImpairmentLossNotAllocatedToReportableSegments(self): #報告セグメントに配分されていない減損損失の内容
		return self.DescriptionOfImpairmentLossNotAllocatedToReportableSegments

	def getNotesSegmentInformationEtcFinancialStatementsHeading(self): #セグメント情報等、財務諸表 [目次項目]
		return self.NotesSegmentInformationEtcFinancialStatementsHeading

	def getAmortizationAndUnamortizedBalanceOfGoodwillForEachReportableSegmentAbstract(self): #報告セグメントごとののれんの償却額及び未償却残高に関する情報 [タイトル項目]
		return self.AmortizationAndUnamortizedBalanceOfGoodwillForEachReportableSegmentAbstract

	def getAmortizationAndUnamortizedBalanceOfGoodwillForEachReportableSegmentTable(self): #報告セグメントごとののれんの償却額及び未償却残高に関する情報 [表]
		return self.AmortizationAndUnamortizedBalanceOfGoodwillForEachReportableSegmentTable

	def getConsolidatedOrNonConsolidatedAxis(self): #連結個別 [軸]
		return self.ConsolidatedOrNonConsolidatedAxis

	def getNonConsolidatedMember(self): #非連結又は個別 [メンバー]
		return self.NonConsolidatedMember

	def getOperatingSegmentsAxis(self): #事業セグメント [軸]
		return self.OperatingSegmentsAxis

	def getEntityTotalMember(self): #連結合計又は会社合計 [メンバー] ※ディメンションデフォルト
		return self.EntityTotalMember

	def getReportableSegmentsMember(self): #報告セグメント [メンバー]
		return self.ReportableSegmentsMember

	def getOtherReportableSegmentsMember(self): #その他の報告セグメント [メンバー]
		return self.OtherReportableSegmentsMember

	def getOperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember(self): #報告セグメント以外の全てのセグメント [メンバー]
		return self.OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember

	def getUnallocatedAmountsAndEliminationMember(self): #全社・消去 [メンバー]
		return self.UnallocatedAmountsAndEliminationMember

	def getAmortizationAndUnamortizedBalanceOfGoodwillForEachReportableSegmentLineItems(self): #報告セグメントごとののれんの償却額及び未償却残高に関する情報 [表示項目]
		return self.AmortizationAndUnamortizedBalanceOfGoodwillForEachReportableSegmentLineItems

	def getAmortizationOfGoodwillSGA(self): #のれん償却額、販売費及び一般管理費
		return self.AmortizationOfGoodwillSGA

	def getGoodwill(self): #のれん
		return self.Goodwill

	def getGoodwillBeforeOffsetting(self): #のれん（相殺前）
		return self.GoodwillBeforeOffsetting

	def getNotesSegmentInformationEtcFinancialStatementsHeading(self): #セグメント情報等、財務諸表 [目次項目]
		return self.NotesSegmentInformationEtcFinancialStatementsHeading

	def getAmortizationAndUnamortizedBalanceOfNegativeGoodwillForEachReportableSegmentAbstract(self): #報告セグメントごとの負ののれんの償却額及び未償却残高に関する情報 [タイトル項目]
		return self.AmortizationAndUnamortizedBalanceOfNegativeGoodwillForEachReportableSegmentAbstract

	def getAmortizationAndUnamortizedBalanceOfNegativeGoodwillForEachReportableSegmentTable(self): #報告セグメントごとの負ののれんの償却額及び未償却残高に関する情報 [表]
		return self.AmortizationAndUnamortizedBalanceOfNegativeGoodwillForEachReportableSegmentTable

	def getConsolidatedOrNonConsolidatedAxis(self): #連結個別 [軸]
		return self.ConsolidatedOrNonConsolidatedAxis

	def getNonConsolidatedMember(self): #非連結又は個別 [メンバー]
		return self.NonConsolidatedMember

	def getOperatingSegmentsAxis(self): #事業セグメント [軸]
		return self.OperatingSegmentsAxis

	def getEntityTotalMember(self): #連結合計又は会社合計 [メンバー] ※ディメンションデフォルト
		return self.EntityTotalMember

	def getReportableSegmentsMember(self): #報告セグメント [メンバー]
		return self.ReportableSegmentsMember

	def getOtherReportableSegmentsMember(self): #その他の報告セグメント [メンバー]
		return self.OtherReportableSegmentsMember

	def getOperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember(self): #報告セグメント以外の全てのセグメント [メンバー]
		return self.OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember

	def getUnallocatedAmountsAndEliminationMember(self): #全社・消去 [メンバー]
		return self.UnallocatedAmountsAndEliminationMember

	def getAmortizationAndUnamortizedBalanceOfNegativeGoodwillForEachReportableSegmentLineItems(self): #報告セグメントごとの負ののれんの償却額及び未償却残高に関する情報 [表示項目]
		return self.AmortizationAndUnamortizedBalanceOfNegativeGoodwillForEachReportableSegmentLineItems

	def getAmortizationOfNegativeGoodwillNOI(self): #負ののれん償却額、営業外収益
		return self.AmortizationOfNegativeGoodwillNOI

	def getNegativeGoodwill(self): #負ののれん
		return self.NegativeGoodwill

	def getNegativeGoodwillBeforeOffsetting(self): #負ののれん（相殺前）
		return self.NegativeGoodwillBeforeOffsetting

	def getNotesSegmentInformationEtcFinancialStatementsHeading(self): #セグメント情報等、財務諸表 [目次項目]
		return self.NotesSegmentInformationEtcFinancialStatementsHeading

	def getNotesSegmentInformationEtcFinancialStatementsTable(self): #セグメント情報等、財務諸表 [表]
		return self.NotesSegmentInformationEtcFinancialStatementsTable

	def getConsolidatedOrNonConsolidatedAxis(self): #連結個別 [軸]
		return self.ConsolidatedOrNonConsolidatedAxis

	def getNonConsolidatedMember(self): #非連結又は個別 [メンバー]
		return self.NonConsolidatedMember

	def getNotesSegmentInformationEtcFinancialStatementsLineItems(self): #セグメント情報等、財務諸表 [表示項目]
		return self.NotesSegmentInformationEtcFinancialStatementsLineItems

	def getDescriptionOfAmortizationOfGoodwillOrUnamortizedBalanceOfGoodwillNotAllocatedToReportableSegments(self): #報告セグメントに配分されていないのれんの償却額又は未償却残高の内容
		return self.DescriptionOfAmortizationOfGoodwillOrUnamortizedBalanceOfGoodwillNotAllocatedToReportableSegments

	def getNotesSegmentInformationEtcFinancialStatementsHeading(self): #セグメント情報等、財務諸表 [目次項目]
		return self.NotesSegmentInformationEtcFinancialStatementsHeading

	def getInformationAboutGainOnBargainPurchaseForEachReportableSegmentTable(self): #報告セグメントごとの負ののれん発生益に関する情報 [表]
		return self.InformationAboutGainOnBargainPurchaseForEachReportableSegmentTable

	def getConsolidatedOrNonConsolidatedAxis(self): #連結個別 [軸]
		return self.ConsolidatedOrNonConsolidatedAxis

	def getNonConsolidatedMember(self): #非連結又は個別 [メンバー]
		return self.NonConsolidatedMember

	def getOperatingSegmentsAxis(self): #事業セグメント [軸]
		return self.OperatingSegmentsAxis

	def getEntityTotalMember(self): #連結合計又は会社合計 [メンバー] ※ディメンションデフォルト
		return self.EntityTotalMember

	def getReportableSegmentsMember(self): #報告セグメント [メンバー]
		return self.ReportableSegmentsMember

	def getOtherReportableSegmentsMember(self): #その他の報告セグメント [メンバー]
		return self.OtherReportableSegmentsMember

	def getOperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember(self): #報告セグメント以外の全てのセグメント [メンバー]
		return self.OperatingSegmentsNotIncludedInReportableSegmentsAndOtherRevenueGeneratingBusinessActivitiesMember

	def getUnallocatedAmountsAndEliminationMember(self): #全社・消去 [メンバー]
		return self.UnallocatedAmountsAndEliminationMember

	def getInformationAboutGainOnBargainPurchaseForEachReportableSegmentLineItems(self): #報告セグメントごとの負ののれん発生益に関する情報 [表示項目]
		return self.InformationAboutGainOnBargainPurchaseForEachReportableSegmentLineItems

	def getDescriptionOfFactorsWhichLedToRecognitionOfGainOnBargainPurchaseTextBlock(self): #報告セグメントごとの負ののれん発生益を認識する要因となった事象の概要 [テキストブロック]
		return self.DescriptionOfFactorsWhichLedToRecognitionOfGainOnBargainPurchaseTextBlock

	def getNotesOperationOfPublicFacilitiesFinancialStatementsHeading(self): #公共施設等運営事業関係、財務諸表 [目次項目]
		return self.NotesOperationOfPublicFacilitiesFinancialStatementsHeading

	def getNotesOperationOfPublicFacilitiesFinancialStatementsTextBlock(self): #公共施設等運営事業関係、財務諸表 [テキストブロック]
		return self.NotesOperationOfPublicFacilitiesFinancialStatementsTextBlock

	def getNotesRelatedPartiesFinancialStatementsHeading(self): #関連当事者情報、財務諸表 [目次項目]
		return self.NotesRelatedPartiesFinancialStatementsHeading

	def getNotesRelatedPartiesFinancialStatementsTextBlock(self): #関連当事者情報、財務諸表 [テキストブロック]
		return self.NotesRelatedPartiesFinancialStatementsTextBlock

	def getNotesEquityInEarningsLossesOfAffiliatesIfEquityMethodIsAppliedFinancialStatementsHeading(self): #持分法損益等、財務諸表 [目次項目]
		return self.NotesEquityInEarningsLossesOfAffiliatesIfEquityMethodIsAppliedFinancialStatementsHeading

	def getNotesEquityInEarningsLossesOfAffiliatesIfEquityMethodIsAppliedFinancialStatementsTextBlock(self): #持分法損益等、財務諸表 [テキストブロック]
		return self.NotesEquityInEarningsLossesOfAffiliatesIfEquityMethodIsAppliedFinancialStatementsTextBlock

	def getNotesSpecialPurposeEntitiesSubjectToDisclosureFinancialStatementsHeading(self): #開示対象特別目的会社関係、財務諸表 [目次項目]
		return self.NotesSpecialPurposeEntitiesSubjectToDisclosureFinancialStatementsHeading

	def getNotesSpecialPurposeEntitiesSubjectToDisclosureFinancialStatementsTextBlock(self): #開示対象特別目的会社関係、財務諸表 [テキストブロック]
		return self.NotesSpecialPurposeEntitiesSubjectToDisclosureFinancialStatementsTextBlock

	def getNotesPerShareInformationFinancialStatementsHeading(self): #１株当たり情報、財務諸表 [目次項目]
		return self.NotesPerShareInformationFinancialStatementsHeading

	def getNotesPerShareInformationFinancialStatementsTextBlock(self): #１株当たり情報、財務諸表 [テキストブロック]
		return self.NotesPerShareInformationFinancialStatementsTextBlock

	def getNotesSignificantEventsAfterReportingPeriodFinancialStatementsHeading(self): #重要な後発事象、財務諸表 [目次項目]
		return self.NotesSignificantEventsAfterReportingPeriodFinancialStatementsHeading

	def getNotesSignificantEventsAfterReportingPeriodFinancialStatementsTextBlock(self): #重要な後発事象、財務諸表 [テキストブロック]
		return self.NotesSignificantEventsAfterReportingPeriodFinancialStatementsTextBlock

	def getAnnexedDetailedSchedulesHeading(self): #附属明細表 [目次項目]
		return self.AnnexedDetailedSchedulesHeading

	def getAnnexedDetailedScheduleOfSecuritiesHeading(self): #有価証券明細表 [目次項目]
		return self.AnnexedDetailedScheduleOfSecuritiesHeading

	def getAnnexedDetailedScheduleOfSecuritiesTextBlock(self): #有価証券明細表 [テキストブロック]
		return self.AnnexedDetailedScheduleOfSecuritiesTextBlock

	def getAnnexedDetailedScheduleOfPropertyPlantAndEquipmentEtcHeading(self): #有形固定資産等明細表 [目次項目]
		return self.AnnexedDetailedScheduleOfPropertyPlantAndEquipmentEtcHeading

	def getAnnexedDetailedScheduleOfPropertyPlantAndEquipmentEtcTextBlock(self): #有形固定資産等明細表 [テキストブロック]
		return self.AnnexedDetailedScheduleOfPropertyPlantAndEquipmentEtcTextBlock

	def getAnnexedDetailedScheduleOfCorporateBondsFinancialStatementsHeading(self): #社債明細表、財務諸表 [目次項目]
		return self.AnnexedDetailedScheduleOfCorporateBondsFinancialStatementsHeading

	def getAnnexedDetailedScheduleOfCorporateBondsFinancialStatementsTextBlock(self): #社債明細表、財務諸表 [テキストブロック]
		return self.AnnexedDetailedScheduleOfCorporateBondsFinancialStatementsTextBlock

	def getAnnexedDetailedScheduleOfBorrowingsFinancialStatementsHeading(self): #借入金等明細表、財務諸表 [目次項目]
		return self.AnnexedDetailedScheduleOfBorrowingsFinancialStatementsHeading

	def getAnnexedDetailedScheduleOfBorrowingsFinancialStatementsTextBlock(self): #借入金等明細表、財務諸表 [テキストブロック]
		return self.AnnexedDetailedScheduleOfBorrowingsFinancialStatementsTextBlock

	def getAnnexedDetailedScheduleOfProvisionsHeading(self): #引当金明細表 [目次項目]
		return self.AnnexedDetailedScheduleOfProvisionsHeading

	def getAnnexedDetailedScheduleOfProvisionsTextBlock(self): #引当金明細表 [テキストブロック]
		return self.AnnexedDetailedScheduleOfProvisionsTextBlock

	def getAnnexedDetailedScheduleOfAssetRetirementObligationsFinancialStatementsHeading(self): #資産除去債務明細表、財務諸表 [目次項目]
		return self.AnnexedDetailedScheduleOfAssetRetirementObligationsFinancialStatementsHeading

	def getAnnexedDetailedScheduleOfAssetRetirementObligationsFinancialStatementsTextBlock(self): #資産除去債務明細表、財務諸表 [テキストブロック]
		return self.AnnexedDetailedScheduleOfAssetRetirementObligationsFinancialStatementsTextBlock

	def getAnnexedDetailedScheduleOfWaterTransportationRevenuesAndExpensesHeading(self): #海運業収益及び費用明細表 [目次項目]
		return self.AnnexedDetailedScheduleOfWaterTransportationRevenuesAndExpensesHeading

	def getAnnexedDetailedScheduleOfWaterTransportationRevenuesAndExpensesTextBlock(self): #海運業収益及び費用明細表 [テキストブロック]
		return self.AnnexedDetailedScheduleOfWaterTransportationRevenuesAndExpensesTextBlock

	def getAnnexedDetailedScheduleOfSecuritiesInTrustCNAHeading(self): #信託有価証券明細表、建設保証業 [目次項目]
		return self.AnnexedDetailedScheduleOfSecuritiesInTrustCNAHeading

	def getAnnexedDetailedScheduleOfSecuritiesInTrustCNATextBlock(self): #信託有価証券明細表、建設保証業 [テキストブロック]
		return self.AnnexedDetailedScheduleOfSecuritiesInTrustCNATextBlock

	def getAnnexedDetailedScheduleOfBusinessCostINSHeading(self): #事業費明細表、保険業 [目次項目]
		return self.AnnexedDetailedScheduleOfBusinessCostINSHeading

	def getAnnexedDetailedScheduleOfBusinessCostINSTextBlock(self): #事業費明細表、保険業 [テキストブロック]
		return self.AnnexedDetailedScheduleOfBusinessCostINSTextBlock

	def getAnnexedDetailedScheduleOfNonCurrentAssetsELCHeading(self): #固定資産等明細表、電気通信事業 [目次項目]
		return self.AnnexedDetailedScheduleOfNonCurrentAssetsELCHeading

	def getAnnexedDetailedScheduleOfNonCurrentAssetsELCTextBlock(self): #固定資産等明細表、電気通信事業 [テキストブロック]
		return self.AnnexedDetailedScheduleOfNonCurrentAssetsELCTextBlock

	def getAnnexedDetailedScheduleOfNonCurrentAssetsGASHeading(self): #固定資産等明細表、ガス事業 [目次項目]
		return self.AnnexedDetailedScheduleOfNonCurrentAssetsGASHeading

	def getAnnexedDetailedScheduleOfNonCurrentAssetsGASTextBlock(self): #固定資産等明細表、ガス事業 [テキストブロック]
		return self.AnnexedDetailedScheduleOfNonCurrentAssetsGASTextBlock

	def getAnnexedDetailedScheduleOfNonCurrentAssetsHWYHeading(self): #固定資産等明細表、高速道路事業 [目次項目]
		return self.AnnexedDetailedScheduleOfNonCurrentAssetsHWYHeading

	def getAnnexedDetailedScheduleOfNonCurrentAssetsHWYTextBlock(self): #固定資産等明細表、高速道路事業 [テキストブロック]
		return self.AnnexedDetailedScheduleOfNonCurrentAssetsHWYTextBlock

	def getAnnexedDetailedScheduleOfIncreaseAndDecreaseOfNonCurrentAssetsELEHeading(self): #固定資産期中増減明細表、電気事業 [目次項目]
		return self.AnnexedDetailedScheduleOfIncreaseAndDecreaseOfNonCurrentAssetsELEHeading

	def getAnnexedDetailedScheduleOfIncreaseAndDecreaseOfNonCurrentAssetsELETextBlock(self): #固定資産期中増減明細表、電気事業 [テキストブロック]
		return self.AnnexedDetailedScheduleOfIncreaseAndDecreaseOfNonCurrentAssetsELETextBlock

	def getAnnexedDetailedScheduleOfIncreaseAndDecreaseOfNonCurrentAssetsPart2IntangibleAssetsELEHeading(self): #固定資産期中増減明細表（無形固定資産再掲）、電気事業 [目次項目]
		return self.AnnexedDetailedScheduleOfIncreaseAndDecreaseOfNonCurrentAssetsPart2IntangibleAssetsELEHeading

	def getAnnexedDetailedScheduleOfIncreaseAndDecreaseOfNonCurrentAssetsPart2IntangibleAssetsELETextBlock(self): #固定資産期中増減明細表（無形固定資産再掲）、電気事業 [テキストブロック]
		return self.AnnexedDetailedScheduleOfIncreaseAndDecreaseOfNonCurrentAssetsPart2IntangibleAssetsELETextBlock

	def getAnnexedDetailedScheduleOfDepreciationEtcELEHeading(self): #減価償却費等明細表、電気事業 [目次項目]
		return self.AnnexedDetailedScheduleOfDepreciationEtcELEHeading

	def getAnnexedDetailedScheduleOfDepreciationEtcELETextBlock(self): #減価償却費等明細表、電気事業 [テキストブロック]
		return self.AnnexedDetailedScheduleOfDepreciationEtcELETextBlock

	def getAnnexedDetailedScheduleOfLongTermAndShortTermInvestmentsELEHeading(self): #長期投資及び短期投資明細表、電気事業 [目次項目]
		return self.AnnexedDetailedScheduleOfLongTermAndShortTermInvestmentsELEHeading

	def getAnnexedDetailedScheduleOfLongTermAndShortTermInvestmentsELETextBlock(self): #長期投資及び短期投資明細表、電気事業 [テキストブロック]
		return self.AnnexedDetailedScheduleOfLongTermAndShortTermInvestmentsELETextBlock

	def getAnnexedDetailedScheduleOfBorrowingsLongTermPayablesLeaseObligationsOtherNonCurrentLiabilitiesAndCommercialPapersELEHeading(self): #借入金、長期未払債務、リース債務、雑固定負債及びコマーシャル・ペーパー明細表、電気事業 [目次項目]
		return self.AnnexedDetailedScheduleOfBorrowingsLongTermPayablesLeaseObligationsOtherNonCurrentLiabilitiesAndCommercialPapersELEHeading

	def getAnnexedDetailedScheduleOfBorrowingsLongTermPayablesLeaseObligationsOtherNonCurrentLiabilitiesAndCommercialPapersELETextBlock(self): #借入金、長期未払債務、リース債務、雑固定負債及びコマーシャル・ペーパー明細表、電気事業 [テキストブロック]
		return self.AnnexedDetailedScheduleOfBorrowingsLongTermPayablesLeaseObligationsOtherNonCurrentLiabilitiesAndCommercialPapersELETextBlock

	def getAnnexedDetailedScheduleOfCorporateBondsAndShortTermAndLongTermBorrowingsHWYHeading(self): #社債、長期借入金及び短期借入金の増減明細表、高速道路事業 [目次項目]
		return self.AnnexedDetailedScheduleOfCorporateBondsAndShortTermAndLongTermBorrowingsHWYHeading

	def getAnnexedDetailedScheduleOfCorporateBondsAndShortTermAndLongTermBorrowingsHWYTextBlock(self): #社債、長期借入金及び短期借入金の増減明細表、高速道路事業 [テキストブロック]
		return self.AnnexedDetailedScheduleOfCorporateBondsAndShortTermAndLongTermBorrowingsHWYTextBlock

	def getAnnexedDetailedScheduleOfMedicalCorporationBondsHeading(self): #社会医療法人債明細表 [目次項目]
		return self.AnnexedDetailedScheduleOfMedicalCorporationBondsHeading

	def getAnnexedDetailedScheduleOfMedicalCorporationBondsTextBlock(self): #社会医療法人債明細表 [テキストブロック]
		return self.AnnexedDetailedScheduleOfMedicalCorporationBondsTextBlock

	def getAnnexedDetailedScheduleOfSchoolBondsHeading(self): #学校債明細表 [目次項目]
		return self.AnnexedDetailedScheduleOfSchoolBondsHeading

	def getAnnexedDetailedScheduleOfSchoolBondsTextBlock(self): #学校債明細表 [テキストブロック]
		return self.AnnexedDetailedScheduleOfSchoolBondsTextBlock

	def getComponentsOfMajorAssetsAndLiabilitiesHeading(self): #主な資産及び負債の内容 [目次項目]
		return self.ComponentsOfMajorAssetsAndLiabilitiesHeading

	def getComponentsOfMajorAssetsAndLiabilitiesTextBlock(self): #主な資産及び負債の内容 [テキストブロック]
		return self.ComponentsOfMajorAssetsAndLiabilitiesTextBlock

	def getOtherInformationFinancialStatementsEtcHeading(self): #その他、財務諸表等 [目次項目]
		return self.OtherInformationFinancialStatementsEtcHeading

	def getOtherInformationFinancialStatementsEtcTextBlock(self): #その他、財務諸表等 [テキストブロック]
		return self.OtherInformationFinancialStatementsEtcTextBlock

	def getOverviewOfOperationalProceduresForSharesHeading(self): #提出会社の株式事務の概要 [目次項目]
		return self.OverviewOfOperationalProceduresForSharesHeading

	def getOverviewOfOperationalProceduresForSharesTextBlock(self): #提出会社の株式事務の概要 [テキストブロック]
		return self.OverviewOfOperationalProceduresForSharesTextBlock

	def getReferenceInformationOfReportingCompanyHeading(self): #提出会社の参考情報 [目次項目]
		return self.ReferenceInformationOfReportingCompanyHeading

	def getInformationAboutParentCompanyEtcOfReportingCompanyHeading(self): #提出会社の親会社等の情報 [目次項目]
		return self.InformationAboutParentCompanyEtcOfReportingCompanyHeading

	def getInformationAboutParentCompanyEtcOfReportingCompanyTextBlock(self): #提出会社の親会社等の情報 [テキストブロック]
		return self.InformationAboutParentCompanyEtcOfReportingCompanyTextBlock

	def getOtherReferenceInformationHeading(self): #その他の参考情報 [目次項目]
		return self.OtherReferenceInformationHeading

	def getOtherReferenceInformationTextBlock(self): #その他の参考情報 [テキストブロック]
		return self.OtherReferenceInformationTextBlock

	def getInformationAboutCompanyWhichProvidesGuaranteeToReportingCompanyHeading(self): #提出会社の保証会社等の情報 [目次項目]
		return self.InformationAboutCompanyWhichProvidesGuaranteeToReportingCompanyHeading

	def getInformationAboutCompanyWhichProvidesGuaranteeToReportingCompanyTextBlock(self): #提出会社の保証会社等の情報 [テキストブロック]
		return self.InformationAboutCompanyWhichProvidesGuaranteeToReportingCompanyTextBlock

	def getInformationAboutGuaranteeCompanyHeading(self): #保証会社情報 [目次項目]
		return self.InformationAboutGuaranteeCompanyHeading

	def getInformationAboutGuaranteeCompanyTextBlock(self): #保証会社情報 [テキストブロック]
		return self.InformationAboutGuaranteeCompanyTextBlock

	def getCorporateBondsUnderGuaranteeHeading(self): #保証の対象となっている社債 [目次項目]
		return self.CorporateBondsUnderGuaranteeHeading

	def getCorporateBondsUnderGuaranteeTextBlock(self): #保証の対象となっている社債 [テキストブロック]
		return self.CorporateBondsUnderGuaranteeTextBlock

	def getInformationAboutGuaranteeCompanySubjectToOngoingDisclosureHeading(self): #継続開示会社たる保証会社に関する事項 [目次項目]
		return self.InformationAboutGuaranteeCompanySubjectToOngoingDisclosureHeading

	def getInformationAboutGuaranteeCompanySubjectToOngoingDisclosureTextBlock(self): #継続開示会社たる保証会社に関する事項 [テキストブロック]
		return self.InformationAboutGuaranteeCompanySubjectToOngoingDisclosureTextBlock

	def getDocumentsSubmittedByGuaranteeCompanyHeading(self): #保証会社が提出した書類 [目次項目]
		return self.DocumentsSubmittedByGuaranteeCompanyHeading

	def getAnnualSecuritiesReportAndAttachedDocumentsQuarterlySecuritiesReportOrSemiAnnualSecuritiesReportDocumentsSubmittedByGuaranteeCompanyHeading(self): #有価証券報告書及びその添付書類又は四半期報告書若しくは半期報告書、保証会社が提出した書類 [目次項目]
		return self.AnnualSecuritiesReportAndAttachedDocumentsQuarterlySecuritiesReportOrSemiAnnualSecuritiesReportDocumentsSubmittedByGuaranteeCompanyHeading

	def getAnnualSecuritiesReportAndAttachedDocumentsQuarterlySecuritiesReportOrSemiAnnualSecuritiesReportDocumentsSubmittedByGuaranteeCompanyTextBlock(self): #有価証券報告書及びその添付書類又は四半期報告書若しくは半期報告書、保証会社が提出した書類 [テキストブロック]
		return self.AnnualSecuritiesReportAndAttachedDocumentsQuarterlySecuritiesReportOrSemiAnnualSecuritiesReportDocumentsSubmittedByGuaranteeCompanyTextBlock

	def getExtraordinarySecuritiesReportDocumentsSubmittedByGuaranteeCompanyHeading(self): #臨時報告書、保証会社が提出した書類 [目次項目]
		return self.ExtraordinarySecuritiesReportDocumentsSubmittedByGuaranteeCompanyHeading

	def getExtraordinarySecuritiesReportDocumentsSubmittedByGuaranteeCompanyTextBlock(self): #臨時報告書、保証会社が提出した書類 [テキストブロック]
		return self.ExtraordinarySecuritiesReportDocumentsSubmittedByGuaranteeCompanyTextBlock

	def getAmendmentReportDocumentsSubmittedByGuaranteeCompanyHeading(self): #訂正報告書、保証会社が提出した書類 [目次項目]
		return self.AmendmentReportDocumentsSubmittedByGuaranteeCompanyHeading

	def getAmendmentReportDocumentsSubmittedByGuaranteeCompanyTextBlock(self): #訂正報告書、保証会社が提出した書類 [テキストブロック]
		return self.AmendmentReportDocumentsSubmittedByGuaranteeCompanyTextBlock

	def getPlaceForPublicInspectionDocumentsSubmittedByGuaranteeCompanyHeading(self): #上記書類を縦覧に供している場所、保証会社が提出した書類 [目次項目]
		return self.PlaceForPublicInspectionDocumentsSubmittedByGuaranteeCompanyHeading

	def getPlaceForPublicInspectionDocumentsSubmittedByGuaranteeCompanyTextBlock(self): #上記書類を縦覧に供している場所、保証会社が提出した書類 [テキストブロック]
		return self.PlaceForPublicInspectionDocumentsSubmittedByGuaranteeCompanyTextBlock

	def getInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureHeading(self): #継続開示会社に該当しない保証会社に関する事項 [目次項目]
		return self.InformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureHeading

	def getInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureTextBlock(self): #継続開示会社に該当しない保証会社に関する事項 [テキストブロック]
		return self.InformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureTextBlock

	def getCompanyNameTitleAndNameOfRepresentativeAndAddressOfRegisteredHeadquarterHeading(self): #会社名・代表者の役職氏名及び本店の所在の場所 [目次項目]
		return self.CompanyNameTitleAndNameOfRepresentativeAndAddressOfRegisteredHeadquarterHeading

	def getCompanyNameTitleAndNameOfRepresentativeAndAddressOfRegisteredHeadquarterTextBlock(self): #会社名・代表者の役職氏名及び本店の所在の場所 [テキストブロック]
		return self.CompanyNameTitleAndNameOfRepresentativeAndAddressOfRegisteredHeadquarterTextBlock

	def getOverviewOfCompanyInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureHeading(self): #企業の概況、継続開示会社に該当しない保証会社に関する事項 [目次項目]
		return self.OverviewOfCompanyInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureHeading

	def getOverviewOfCompanyInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureTextBlock(self): #企業の概況、継続開示会社に該当しない保証会社に関する事項 [テキストブロック]
		return self.OverviewOfCompanyInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureTextBlock

	def getOverviewOfBusinessInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureHeading(self): #事業の状況、継続開示会社に該当しない保証会社に関する事項 [目次項目]
		return self.OverviewOfBusinessInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureHeading

	def getOverviewOfBusinessInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureTextBlock(self): #事業の状況、継続開示会社に該当しない保証会社に関する事項 [テキストブロック]
		return self.OverviewOfBusinessInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureTextBlock

	def getInformationAboutFacilitiesInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureHeading(self): #設備の状況、継続開示会社に該当しない保証会社に関する事項 [目次項目]
		return self.InformationAboutFacilitiesInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureHeading

	def getInformationAboutFacilitiesInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureTextBlock(self): #設備の状況、継続開示会社に該当しない保証会社に関する事項 [テキストブロック]
		return self.InformationAboutFacilitiesInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureTextBlock

	def getGuaranteeCompanyInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureHeading(self): #保証会社の状況、継続開示会社に該当しない保証会社に関する事項 [目次項目]
		return self.GuaranteeCompanyInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureHeading

	def getGuaranteeCompanyInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureTextBlock(self): #保証会社の状況、継続開示会社に該当しない保証会社に関する事項 [テキストブロック]
		return self.GuaranteeCompanyInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureTextBlock

	def getFinancialInformationInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureHeading(self): #経理の状況、継続開示会社に該当しない保証会社に関する事項 [目次項目]
		return self.FinancialInformationInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureHeading

	def getFinancialInformationInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureTextBlock(self): #経理の状況、継続開示会社に該当しない保証会社に関する事項 [テキストブロック]
		return self.FinancialInformationInformationAboutGuaranteeCompanyNotSubjectToOngoingDisclosureTextBlock

	def getInformationAboutCompaniesOtherThanGuaranteeCompanyHeading(self): #保証会社以外の会社の情報 [目次項目]
		return self.InformationAboutCompaniesOtherThanGuaranteeCompanyHeading

	def getInformationAboutCompaniesOtherThanGuaranteeCompanyTextBlock(self): #保証会社以外の会社の情報 [テキストブロック]
		return self.InformationAboutCompaniesOtherThanGuaranteeCompanyTextBlock

	def getReasonForDisclosureOfInformationOfCompanyConcernedHeading(self): #当該会社の情報の開示を必要とする理由 [目次項目]
		return self.ReasonForDisclosureOfInformationOfCompanyConcernedHeading

	def getReasonForDisclosureOfInformationOfCompanyConcernedTextBlock(self): #当該会社の情報の開示を必要とする理由 [テキストブロック]
		return self.ReasonForDisclosureOfInformationOfCompanyConcernedTextBlock

	def getInformationAboutCompanyConcernedSubjectToOngoingDisclosureHeading(self): #継続開示会社たる当該会社に関する事項 [目次項目]
		return self.InformationAboutCompanyConcernedSubjectToOngoingDisclosureHeading

	def getInformationAboutCompanyConcernedSubjectToOngoingDisclosureTextBlock(self): #継続開示会社たる当該会社に関する事項 [テキストブロック]
		return self.InformationAboutCompanyConcernedSubjectToOngoingDisclosureTextBlock

	def getInformationAboutCompanyConcernedNotSubjectToOngoingDisclosureHeading(self): #継続開示会社に該当しない当該会社に関する事項 [目次項目]
		return self.InformationAboutCompanyConcernedNotSubjectToOngoingDisclosureHeading

	def getInformationAboutCompanyConcernedNotSubjectToOngoingDisclosureTextBlock(self): #継続開示会社に該当しない当該会社に関する事項 [テキストブロック]
		return self.InformationAboutCompanyConcernedNotSubjectToOngoingDisclosureTextBlock

	def getInformationAboutIndexEtcHeading(self): #指数等の情報 [目次項目]
		return self.InformationAboutIndexEtcHeading

	def getInformationAboutIndexEtcTextBlock(self): #指数等の情報 [テキストブロック]
		return self.InformationAboutIndexEtcTextBlock

	def getReasonForDisclosureOfSaidIndexEtcHeading(self): #当該指数等の情報の開示を必要とする理由 [目次項目]
		return self.ReasonForDisclosureOfSaidIndexEtcHeading

	def getReasonForDisclosureOfSaidIndexEtcTextBlock(self): #当該指数等の情報の開示を必要とする理由 [テキストブロック]
		return self.ReasonForDisclosureOfSaidIndexEtcTextBlock

	def getHistoricalRecordsOfIndexEtcHeading(self): #当該指数等の推移 [目次項目]
		return self.HistoricalRecordsOfIndexEtcHeading

	def getHistoricalRecordsOfIndexEtcTextBlock(self): #当該指数等の推移 [テキストブロック]
		return self.HistoricalRecordsOfIndexEtcTextBlock

	def getIndependentAuditorsReportHeading(self): #独立監査人の報告書 [目次項目]
		return self.IndependentAuditorsReportHeading

	def getIndependentAuditorsReportConsolidatedTextBlock(self): #独立監査人の報告書、連結 [テキストブロック]
		return self.IndependentAuditorsReportConsolidatedTextBlock

	def getIndependentAuditorsReportNonConsolidatedTextBlock(self): #独立監査人の報告書、個別 [テキストブロック]
		return self.IndependentAuditorsReportNonConsolidatedTextBlock

	def getIndependentAuditorsReportHeading(self): #独立監査人の報告書 [目次項目]
		return self.IndependentAuditorsReportHeading

	def getIndependentAuditorsReportConsolidatedTextBlock(self): #独立監査人の報告書、連結 [テキストブロック]
		return self.IndependentAuditorsReportConsolidatedTextBlock

	def getAuditFirm1Consolidated(self): #監査法人１、連結
		return self.AuditFirm1Consolidated

	def getCPA1AuditFirm1Consolidated(self): #公認会計士１、監査法人１、連結
		return self.CPA1AuditFirm1Consolidated

	def getCPA2AuditFirm1Consolidated(self): #公認会計士２、監査法人１、連結
		return self.CPA2AuditFirm1Consolidated

	def getCPA3AuditFirm1Consolidated(self): #公認会計士３、監査法人１、連結
		return self.CPA3AuditFirm1Consolidated

	def getCPA4AuditFirm1Consolidated(self): #公認会計士４、監査法人１、連結
		return self.CPA4AuditFirm1Consolidated

	def getCPA5AuditFirm1Consolidated(self): #公認会計士５、監査法人１、連結
		return self.CPA5AuditFirm1Consolidated

	def getAuditFirm2Consolidated(self): #監査法人２、連結
		return self.AuditFirm2Consolidated

	def getCPA1AuditFirm2Consolidated(self): #公認会計士１、監査法人２、連結
		return self.CPA1AuditFirm2Consolidated

	def getCPA2AuditFirm2Consolidated(self): #公認会計士２、監査法人２、連結
		return self.CPA2AuditFirm2Consolidated

	def getKeyAuditMattersConsolidatedTextBlock(self): #監査上の主要な検討事項、連結 [テキストブロック]
		return self.KeyAuditMattersConsolidatedTextBlock

	def getOverviewKAMConsolidatedTextBlock(self): #全体概要、監査上の主要な検討事項、連結 [テキストブロック]
		return self.OverviewKAMConsolidatedTextBlock

	def getOtherInformationConsolidatedTextBlock(self): #その他の記載内容、連結 [テキストブロック]
		return self.OtherInformationConsolidatedTextBlock

	def getUncorrectedMaterialMisstatementOtherInformationConsolidatedTextBlock(self): #未修正の重要な誤り、その他の記載内容、連結 [テキストブロック]
		return self.UncorrectedMaterialMisstatementOtherInformationConsolidatedTextBlock

	def getIndependentAuditorsReportNonConsolidatedTextBlock(self): #独立監査人の報告書、個別 [テキストブロック]
		return self.IndependentAuditorsReportNonConsolidatedTextBlock

	def getAuditFirm1NonConsolidated(self): #監査法人１、個別
		return self.AuditFirm1NonConsolidated

	def getCPA1AuditFirm1NonConsolidated(self): #公認会計士１、監査法人１、個別
		return self.CPA1AuditFirm1NonConsolidated

	def getCPA2AuditFirm1NonConsolidated(self): #公認会計士２、監査法人１、個別
		return self.CPA2AuditFirm1NonConsolidated

	def getCPA3AuditFirm1NonConsolidated(self): #公認会計士３、監査法人１、個別
		return self.CPA3AuditFirm1NonConsolidated

	def getCPA4AuditFirm1NonConsolidated(self): #公認会計士４、監査法人１、個別
		return self.CPA4AuditFirm1NonConsolidated

	def getCPA5AuditFirm1NonConsolidated(self): #公認会計士５、監査法人１、個別
		return self.CPA5AuditFirm1NonConsolidated

	def getAuditFirm2NonConsolidated(self): #監査法人２、個別
		return self.AuditFirm2NonConsolidated

	def getCPA1AuditFirm2NonConsolidated(self): #公認会計士１、監査法人２、個別
		return self.CPA1AuditFirm2NonConsolidated

	def getCPA2AuditFirm2NonConsolidated(self): #公認会計士２、監査法人２、個別
		return self.CPA2AuditFirm2NonConsolidated

	def getKeyAuditMattersNonConsolidatedTextBlock(self): #監査上の主要な検討事項、個別 [テキストブロック]
		return self.KeyAuditMattersNonConsolidatedTextBlock

	def getOverviewKAMNonConsolidatedTextBlock(self): #全体概要、監査上の主要な検討事項、個別 [テキストブロック]
		return self.OverviewKAMNonConsolidatedTextBlock

	def getOtherInformationNonConsolidatedTextBlock(self): #その他の記載内容、個別 [テキストブロック]
		return self.OtherInformationNonConsolidatedTextBlock

	def getUncorrectedMaterialMisstatementOtherInformationNonConsolidatedTextBlock(self): #未修正の重要な誤り、その他の記載内容、個別 [テキストブロック]
		return self.UncorrectedMaterialMisstatementOtherInformationNonConsolidatedTextBlock

	def getIndependentAuditorsReportHeading(self): #独立監査人の報告書 [目次項目]
		return self.IndependentAuditorsReportHeading

	def getKeyAuditMattersDetailAbstract(self): #監査上の主要な検討事項（個別説明） [タイトル項目]
		return self.KeyAuditMattersDetailAbstract

	def getKeyAuditMattersTable(self): #監査上の主要な検討事項 [表]
		return self.KeyAuditMattersTable

	def getSequentialNumbersAxis(self): #連番 [軸]
		return self.SequentialNumbersAxis

	def getRow1Member(self): #1件目 [メンバー]
		return self.Row1Member

	def getRow2Member(self): #2件目 [メンバー]
		return self.Row2Member

	def getRow3Member(self): #3件目 [メンバー]
		return self.Row3Member

	def getKeyAuditMattersConsolidatedLineItems(self): #監査上の主要な検討事項、連結 [表示項目]
		return self.KeyAuditMattersConsolidatedLineItems

	def getShortDescriptionKAMConsolidated(self): #見出し、監査上の主要な検討事項、連結
		return self.ShortDescriptionKAMConsolidated

	def getReferenceKAMConsolidated(self): #開示への参照、監査上の主要な検討事項、連結
		return self.ReferenceKAMConsolidated

	def getReference2KAMConsolidated(self): #開示への参照２、監査上の主要な検討事項、連結
		return self.Reference2KAMConsolidated

	def getReference3KAMConsolidated(self): #開示への参照３、監査上の主要な検討事項、連結
		return self.Reference3KAMConsolidated

	def getReference4KAMConsolidated(self): #開示への参照４、監査上の主要な検討事項、連結
		return self.Reference4KAMConsolidated

	def getReference5KAMConsolidated(self): #開示への参照５、監査上の主要な検討事項、連結
		return self.Reference5KAMConsolidated

	def getDescriptionIncludingReasonKAMConsolidatedTextBlock(self): #内容及び理由、監査上の主要な検討事項、連結 [テキストブロック]
		return self.DescriptionIncludingReasonKAMConsolidatedTextBlock

	def getAuditorsResponseKAMConsolidatedTextBlock(self): #監査上の対応、監査上の主要な検討事項、連結 [テキストブロック]
		return self.AuditorsResponseKAMConsolidatedTextBlock

	def getKeyAuditMattersNonConsolidatedLineItems(self): #監査上の主要な検討事項、個別 [表示項目]
		return self.KeyAuditMattersNonConsolidatedLineItems

	def getShortDescriptionKAMNonConsolidated(self): #見出し、監査上の主要な検討事項、個別
		return self.ShortDescriptionKAMNonConsolidated

	def getReferenceKAMNonConsolidated(self): #開示への参照、監査上の主要な検討事項、個別
		return self.ReferenceKAMNonConsolidated

	def getReference2KAMNonConsolidated(self): #開示への参照２、監査上の主要な検討事項、個別
		return self.Reference2KAMNonConsolidated

	def getReference3KAMNonConsolidated(self): #開示への参照３、監査上の主要な検討事項、個別
		return self.Reference3KAMNonConsolidated

	def getReference4KAMNonConsolidated(self): #開示への参照４、監査上の主要な検討事項、個別
		return self.Reference4KAMNonConsolidated

	def getReference5KAMNonConsolidated(self): #開示への参照５、監査上の主要な検討事項、個別
		return self.Reference5KAMNonConsolidated

	def getDescriptionIncludingReasonKAMNonConsolidatedTextBlock(self): #内容及び理由、監査上の主要な検討事項、個別 [テキストブロック]
		return self.DescriptionIncludingReasonKAMNonConsolidatedTextBlock

	def getAuditorsResponseKAMNonConsolidatedTextBlock(self): #監査上の対応、監査上の主要な検討事項、個別 [テキストブロック]
		return self.AuditorsResponseKAMNonConsolidatedTextBlock

	def getSameAsKAMForConsolidatedFSKAMNonConsolidatedTextBlock(self): #連結と同一内容である旨、監査上の主要な検討事項、個別 [テキストブロック]
		return self.SameAsKAMForConsolidatedFSKAMNonConsolidatedTextBlock
