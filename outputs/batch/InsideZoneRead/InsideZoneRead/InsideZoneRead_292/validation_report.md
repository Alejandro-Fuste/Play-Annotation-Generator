# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_292`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_292/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 95 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 449 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
> - Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [11–22], lower_priority='Action_ZoneBlock' annotated_start=14, effective_Action_ZoneBlock_start=23.
> - Action 'Action_None' range [11-110] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [11-87] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [90-91] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [54-104] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [106-181] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [189-197] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [206-207] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [214-215] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [220-223] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [230-247] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [249-263] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [266-299] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [301-324] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [337-340] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [343-346] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [349-359] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [361-378] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [380-387] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [393-394] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [409-412] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-104] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-125] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-136] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-141] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-45] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-77] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [83-100] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-108] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-373] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [375-419] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [423-426] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [430-431] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [440-444] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-40] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [49-449] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [11-19] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-27] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-117] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-120] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-424] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [121-125] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-449] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-270] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [273-422] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [430-449] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-185] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [189-194] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-266] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [239-449] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-284] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-288] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-328] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [330-419] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [422-444] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-290] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [308-310] for track '28' has 1 frames without a visible bounding box.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.