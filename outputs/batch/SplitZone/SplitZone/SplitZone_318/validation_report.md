# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_318`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_318/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 110 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 449 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
> - Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [272–285], lower_priority='Action_ZoneBlock' annotated_start=282, effective_Action_ZoneBlock_start=286.
> - Segment 'Action_ZoneBlock' for track '21' has invalid range: start=282, end=179. Clamping end to start.
> - Action 'Action_None' range [272-332] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-397] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [324-352] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-98] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ReadEdgeDefender' range [292-305] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [310-339] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [342-414] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [421-422] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [424-425] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [433-436] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-434] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [436-439] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-311] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [320-355] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [358-361] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [367-369] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [373-378] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [272-310] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-362] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [364-405] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [410-449] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-354] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-320] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-449] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [272-285] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [315-321] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [324-342] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [347-354] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [359-362] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [367-369] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [387-445] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [447-449] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-293] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-405] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-436] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-276] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [282-310] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [317-319] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-317] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-3] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-39] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-60] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-63] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-97] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-101] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-136] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-142] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-179] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [295-296] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [300-332] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [334-336] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [353-449] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [347-449] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [372-384] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [396-401] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [402-408] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [403-426] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [429-433] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [438-439] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [422-427] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [431-436] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [439-446] for track '33' has 1 frames without a visible bounding box.
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