# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_257`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_257/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 88 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 509 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 516: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 509 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '14' (LT) duration 101 frames exceeds threshold 90 frames [start=318, end=418].
> - Validation warning: Action 'Action_ZoneBlock' for track '15' (C) duration 101 frames exceeds threshold 90 frames [start=318, end=418].
> - Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [315–319], lower_priority='Action_ZoneBlock' annotated_start=318, effective_Action_ZoneBlock_start=320.
> - Action 'Action_None' range [315-487] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-363] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [366-375] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [390-393] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-434] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [351-434] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [332-370] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [351-381] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-369] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [374-385] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [387-388] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [391-401] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [409-469] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-56] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-72] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-314] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-349] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [353-363] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [368-374] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [376-482] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-361] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [363-434] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-466] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [473-509] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [318-418] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [315-434] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-434] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [315-434] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [347-404] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [419-434] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-349] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [352-353] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [358-359] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [363-434] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [466-499] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [318-371] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [385-392] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [401-483] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [435-447] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [435-475] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [478-481] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [485-494] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [486-490] for track '32' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.