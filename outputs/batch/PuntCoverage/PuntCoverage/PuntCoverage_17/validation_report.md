# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntCoverage_17`
- **Input XML**: `outputs/batch/PuntCoverage/PuntCoverage/PuntCoverage_17/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntCoverage.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 37 |
| Player Tracks | 37 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 119 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_None' range [4-166] for track '0' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [172-174] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-178] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-299] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-78] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [4-169] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-182] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-221] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-174] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-204] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [76-119] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-54] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-173] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [175-195] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-205] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-214] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-299] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-86] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-181] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-188] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [194-195] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-254] for track '7' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [275-276] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-168] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [170-171] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-174] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-179] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-192] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [198-203] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [207-299] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-263] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-50] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-53] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-67] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-299] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [4-53] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [57-62] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [4-222] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-299] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [4-227] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [230-283] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-57] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-170] for track '15' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-173] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-219] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-225] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [230-272] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_Tackle' range [273-277] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_Tackle' range [284-288] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_LongSnap' range [4-27] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-88] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-299] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-299] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-199] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [201-202] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-299] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-172] for track '19' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [176-177] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-181] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-136] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-181] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-277] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-56] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-218] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [220-222] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-232] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-261] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [67-73] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-299] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-96] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [108-110] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-130] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-136] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-141] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [217-286] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-141] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-164] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-183] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-232] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-245] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-285] for track '34' has 1 frames without a visible bounding box.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.