# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_56`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_56/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 25 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 74 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 569 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 569 as fallback play end.
> - Overlapping action conflict at frame 420 for track '0': 'Action_BallCarry' vs 'Action_BlockSecondLevel'. Overriding with 'Action_BlockSecondLevel'.
> - Validation warning: Action 'Action_BlockSecondLevel' for track '0' (RB) duration 104 frames exceeds threshold 90 frames [start=420, end=523].
> - Validation warning: Action 'Action_ZoneBlock' for track '1' (LT) duration 133 frames exceeds threshold 90 frames [start=391, end=523].
> - Validation warning: Action 'Action_ZoneBlock' for track '2' (RT) duration 133 frames exceeds threshold 90 frames [start=391, end=523].
> - Validation warning: Action 'Action_ZoneBlock' for track '3' (LG) duration 133 frames exceeds threshold 90 frames [start=391, end=523].
> - Validation warning: Action 'Action_ZoneBlock' for track '8' (RG) duration 133 frames exceeds threshold 90 frames [start=391, end=523].
> - Validation warning: Action 'Action_ZoneBlock' for track '9' (C) duration 133 frames exceeds threshold 90 frames [start=391, end=523].
> - Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [388–398], lower_priority='Action_ZoneBlock' annotated_start=391, effective_Action_ZoneBlock_start=399.
> - Action 'Action_BlockSecondLevel' range [420-504] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [391-416] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [524-569] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [388-561] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-355] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [388-409] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [412-415] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [434-436] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [438-443] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [446-450] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [420-490] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [524-554] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-297] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [399-439] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [445-451] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [524-536] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [388-452] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [455-569] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [388-569] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [388-409] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [411-455] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [458-464] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [470-477] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [479-483] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [486-569] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [388-409] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [419-420] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [432-483] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [296-302] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [408-487] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [447-510] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [447-511] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [513-543] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [456-490] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [548-549] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [557-561] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [567-569] for track '24' has 1 frames without a visible bounding box.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.