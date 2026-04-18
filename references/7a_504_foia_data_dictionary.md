# 7(a) and 504 FOIA Data Dictionary

## 7(a) Data Dictionary

| Field Name | Definition |
|---|---|
| AsOfDate | Date when the data was recorded |
| Program | Indicator of whether loan was approved under SBA's 7(a) or 504 loan program |
| LocationID | SBA's unique lender ID code |
| BorrName | Borrower name |
| BorrStreet | Borrower street address |
| BorrCity | Borrower city |
| BorrState | Borrower state |
| BorrZip | Borrower zip code |
| BankName | Name of the bank that the loan is currently assigned to |
| BankFDICNumber | The Federal Depository Insurance Corporation certificate ID of the lender |
| BankNCUANumber | The National Credit Union Association charter number of the lender |
| BankStreet | Bank street address |
| BankCity | Bank city |
| BankState | Bank state |
| BankZip | Bank zip code |
| GrossApproval | Total loan amount |
| SBAGuaranteedApproval | Amount of SBA's loan guaranty |
| ApprovalDate | Date the loan was approved |
| ApprovalFY | Fiscal year the loan was approved |
| FirstDisbursementDate | Date of first loan disbursement (if available) |
| ProcessingMethod | Specific processing method loan was approved under. See SOP 50 10 5 for definitions and rules for each processing method. *(See 7(a) Processing Methods table below.)* |
| Subprogram | Subprogram description — specific subprogram loan was approved under. See SOP 50 10 5 for definitions and rules for each subprogram. |
| InitialInterestRate | Initial interest rate — total interest rate (base rate plus spread) at time loan was approved |
| FixedorVariableInterestInd | Fixed/variable interest rate indicator |
| TermInMonths | Length of loan term |
| NaicsCode | North American Industry Classification System (NAICS) code |
| NaicsDescription | North American Industry Classification System (NAICS) description |
| FranchiseCode | Franchise Code |
| FranchiseName | Franchise Name (if applicable) |
| ProjectCounty | County where project occurs |
| ProjectState | State where project occurs |
| SBADistrictOffice | SBA district office |
| CongressionalDistrict | Congressional district where project occurs |
| BusinessType | Borrower Business Type — Individual, Partnership, or Corporation |
| BusinessAge | Business age category *(see Business Age Categories below; collected starting FY 2018)* |
| LoanStatus | Current status of loan *(see 7(a) Loan Status Codes below)* |
| PaidInFullDate | Date loan was paid in full (if applicable) |
| ChargeOffDate | Date SBA charged off loan (if applicable) |
| GrossChargeOffAmount | Total loan balance charged off (includes guaranteed and non-guaranteed portion of loan) |
| RevolverStatus | Indicator of whether a loan is a term loan or revolving line of credit (0 = Term, 1 = Revolver) |
| JobsSupported | Total Jobs Created + Jobs Retained as reported by lender on SBA Loan Application. SBA does not review, audit, or validate these numbers — they are simply self-reported, good faith estimates by the lender. |
| CollateralInd | An indicator whether the SBA lender reported that the loan was backed by collateral |
| SoldSecMrktInd | An indicator if the loan was sold on the secondary market. This is a static field once it is sold on the secondary market. Equals 'Y' if sold on the secondary market. Once it is 'Y' it will stay 'Y' for its entirety. |

### 7(a) Processing Methods

| Code | Method |
|---|---|
| 7AG | 7a General |
| 7EW | 7a with EWCP |
| WCP | 7a with WCP |
| SGC | Builders Line of Credit (CAPLine) |
| CLP | Certified Lenders Program |
| CLW | Certified Lenders Program with EWCP |
| CAI | Community Advantage Initiative |
| CAT | Community Advantage International Trade |
| CAR | Community Advantage RLOC |
| CRL | Community Advantage Recovery Loan |
| CMX | Community Express |
| CTR | Contract Loan Line of Credit (CAPLine) |
| FPL | Dealer Floor Plan Loans |
| DLC | Domestic Revolving Line of Credit |
| EXP | Export Express |
| EIH | Export Import Harmonization (EXIM) |
| GOL | Gulf Opportunity Pilot Loan Program |
| ITR | International Trade Loans |
| LDP | Low Documentation Program |
| PTX | Patriot Express Loans |
| PLP | Preferred Lenders Program |
| PLW | Preferred Lenders with EWCP |
| PWC | Preferred Lenders with WCP |
| RLI | Rural Loan Initiative |
| SBL | SBA Express Bridge Loan |
| SBX | SBA Express Program |
| SLC | Seasonal Line of Credit (CAPLine) |
| SAB | Small Asset Base Line of Credit (CAPLine) |
| LAI | Small Loan Advantage Initiative |
| STC | Standard Asset Base Working Capital Line of Credit (CAPLine) |

### Business Age Categories

SBA began collecting business age information in fiscal year 2018:

- Change of Ownership
- Existing or more than 2 years old
- New Business or 2 years or less
- Startup, Loan Funds will Open Business

### 7(a) Loan Status Codes

| Code | Meaning |
|---|---|
| COMMIT | Undisbursed |
| PIF | Paid In Full |
| CHGOFF | Charged Off |
| CANCLD | Cancelled |
| EXEMPT | The status of loans that have been disbursed but have not been cancelled, paid in full, or charged off are exempt from disclosure under FOIA Exemption 4 |

---

## 504 Data Dictionary

| Field Name | Definition |
|---|---|
| AsOfDate | Date when the data was recorded |
| Program | Indicator of whether loan was approved under SBA's 7(a) or 504 loan program |
| LocationID | SBA's unique lender ID code |
| BorrName | Borrower name |
| BorrStreet | Borrower street address |
| BorrCity | Borrower city |
| BorrState | Borrower state |
| BorrZip | Borrower zip code |
| CDC_Name | Name of CDC that the loan is currently assigned to |
| CDC_Street | CDC street address |
| CDC_City | CDC city |
| CDC_State | CDC state |
| CDC_Zip | CDC zip code |
| ThirdPartyLender_Name | Name of third party lender |
| ThirdPartyLender_City | Third party lender city |
| ThirdPartyLender_State | Third party lender state |
| ThirdPartyDollars | Third party loan amount |
| GrossApproval | SBA/CDC loan amount |
| ApprovalDate | Date the loan was approved |
| ApprovalFiscalYear | Fiscal year the loan was approved |
| FirstDisbursementDate | Date of first loan disbursement (if available) |
| ProcessingMethod | Specific processing method loan was approved under. See SOP 50 10 5 for definitions and rules for each processing method. *(See 504 Processing Methods table below.)* |
| Subprogram | Subprogram description — specific subprogram loan was approved under. See SOP 50 10 5 for definitions and rules for each subprogram. |
| TermInMonths | Length of loan term |
| NaicsCode | North American Industry Classification System (NAICS) code |
| NaicsDescription | North American Industry Classification System (NAICS) description |
| FranchiseCode | Franchise Code |
| FranchiseName | Franchise Name (if applicable) |
| ProjectCounty | County where project occurs |
| ProjectState | State where project occurs |
| SBADistrictOffice | SBA district office |
| CongressionalDistrict | Congressional district where project occurs |
| BusinessType | Borrower Business Type — Individual, Partnership, or Corporation |
| BusinessAge | Business age category *(see Business Age Categories below; collected starting FY 2018)* |
| LoanStatus | Current status of loan *(see 504 Loan Status Codes below)* |
| PaidInFullDate | Date loan was paid in full (if applicable) |
| ChargeOffDate | Date SBA charged off loan (if applicable) |
| GrossChargeOffAmount | Total SBA/CDC loan balance charged off |
| JobsSupported | Total Jobs Created + Jobs Retained as reported by lender on SBA Loan Application. SBA does not review, audit, or validate these numbers — they are simply self-reported, good faith estimates by the lender. |
| CollateralInd | An indicator whether the SBA lender reported that the loan was backed by collateral |

### 504 Processing Methods

| Code | Method |
|---|---|
| 504 | 504 Basic |
| 5RF | 504 Commercial Real Estate Refinance Program |
| 5RE | 504 Refinancing Program |
| 5EX | ALP Express |
| 5XR | ALP Express Debt Refi |
| ALP | Accredited Lenders Program |
| 5RX | PCLP Debt Refinance |
| PCP | Premier Certified Lenders Program |

### Business Age Categories

SBA began collecting business age information in fiscal year 2018:

- Change of Ownership
- Existing or more than 2 years old
- New Business or 2 years or less
- Startup, Loan Funds will Open Business

### 504 Loan Status Codes

| Code | Meaning |
|---|---|
| NOT FUNDED | Undisbursed |
| PIF | Paid In Full |
| CHGOFF | Charged Off |
| CANCLD | Cancelled |
| EXEMPT | The status of loans that have been disbursed but have not been cancelled, paid in full, or charged off are exempt from disclosure under FOIA Exemption 4 |
