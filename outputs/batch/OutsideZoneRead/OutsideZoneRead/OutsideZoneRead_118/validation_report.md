# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneRead_118`
- **Input XML**: `outputs/batch/OutsideZoneRead/OutsideZoneRead/OutsideZoneRead_118/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 89 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [21–34], lower_priority='Action_ZoneBlock' annotated_start=24, effective_Action_ZoneBlock_start=35.
> - Action 'Action_None' range [21-80] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [90-114] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-61] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [21-50] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-101] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-86] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-91] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-124] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [24-67] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-97] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-38] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [65-257] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [265-267] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [271-291] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [295-296] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-54] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-72] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-77] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-84] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-87] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-91] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-125] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-50] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-62] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-75] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-79] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-90] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-47] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-70] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [21-27] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-39] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [37-50] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-118] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-71] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-75] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-109] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-99] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-115] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-94] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-107] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-110] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-138] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-299] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-253] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-272] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-285] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [144-292] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-150] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-162] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-262] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-272] for track '33' has 1 frames without a visible bounding box.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.