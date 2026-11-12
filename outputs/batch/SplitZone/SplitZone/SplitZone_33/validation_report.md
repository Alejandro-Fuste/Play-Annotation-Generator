# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_33`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_33/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 82 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 509 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 509 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '3' (LT) duration 95 frames exceeds threshold 90 frames [start=293, end=387].
> - Validation warning: Action 'Action_ZoneBlock' for track '8' (RG) duration 95 frames exceeds threshold 90 frames [start=293, end=387].
> - Validation warning: Action 'Action_ZoneBlock' for track '14' (RT) duration 95 frames exceeds threshold 90 frames [start=293, end=387].
> - Validation warning: Action 'Action_ZoneBlock' for track '19' (LG) duration 95 frames exceeds threshold 90 frames [start=293, end=387].
> - Validation warning: Action 'Action_ZoneBlock' for track '20' (C) duration 95 frames exceeds threshold 90 frames [start=293, end=387].
> - Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [290–306], lower_priority='Action_ZoneBlock' annotated_start=293, effective_Action_ZoneBlock_start=307.
> - Action 'Action_None' range [290-451] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [290-320] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-327] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [337-347] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [349-483] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [388-473] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-388] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [399-405] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [413-414] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [422-463] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [388-414] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [293-311] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [313-387] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [388-477] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [330-354] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [356-503] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-498] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [330-469] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-356] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-381] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [386-424] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [430-447] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [459-461] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [463-469] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-337] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [342-362] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [364-509] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [293-324] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [388-475] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [307-333] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [335-337] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [388-489] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-489] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [309-314] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [317-318] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-320] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [354-356] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [348-349] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [351-352] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [400-409] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [419-466] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [404-405] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [443-445] for track '28' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.