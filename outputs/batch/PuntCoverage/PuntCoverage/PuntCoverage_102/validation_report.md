# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntCoverage_102`
- **Input XML**: `outputs/batch/PuntCoverage/PuntCoverage/PuntCoverage_102/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntCoverage.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 38 |
| Player Tracks | 38 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 86 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Action 'Action_PreSnap' range [0-179] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-75] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-161] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-213] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_Tackle' range [214-226] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_Tackle' range [232-233] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_Tackle' range [239-288] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_Tackle' range [298-299] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-329] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-329] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-188] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-204] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [207-259] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-152] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-329] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-329] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-168] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-173] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-194] for track '12' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-198] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-206] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-329] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-141] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-93] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-145] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-167] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-329] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-308] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-158] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-173] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-181] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-43] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-56] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-83] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-86] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-97] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-103] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-107] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-149] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-196] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-100] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [210-293] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [304-308] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-158] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-327] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-182] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-190] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-201] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-237] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [239-242] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [244-248] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [254-256] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [258-260] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [262-263] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-188] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-214] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [229-233] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [241-250] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [254-256] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-202] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-238] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [271-272] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [259-263] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [265-268] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [271-277] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [280-289] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [276-277] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [286-299] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [323-324] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [326-329] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [295-296] for track '37' has 1 frames without a visible bounding box.
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
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.