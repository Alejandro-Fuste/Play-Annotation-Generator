# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_282`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_282/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 85 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 449 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
> - Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [159–175], lower_priority='Action_ZoneBlock' annotated_start=146, effective_Action_ZoneBlock_start=176.
> - Action 'Action_None' range [159-449] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-446] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-251] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-449] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [207-274] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-449] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-374] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-432] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [206-365] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [367-368] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [372-390] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [393-396] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-449] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [159-444] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [176-190] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [159-283] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-298] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [146-169] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-273] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [277-291] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [214-217] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-216] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-238] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-257] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [300-449] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [339-340] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [345-351] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [379-383] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [390-399] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [402-403] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [411-414] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [417-428] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [432-449] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [416-418] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [438-442] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [440-441] for track '33' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.