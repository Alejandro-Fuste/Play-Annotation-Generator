# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_180`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_180/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 80 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '3' (RG) duration 91 frames exceeds threshold 90 frames [start=45, end=135].
> - Validation warning: Action 'Action_ZoneBlock' for track '9' (LT) duration 91 frames exceeds threshold 90 frames [start=45, end=135].
> - Validation warning: Action 'Action_ZoneBlock' for track '12' (RT) duration 91 frames exceeds threshold 90 frames [start=45, end=135].
> - Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [42–54], lower_priority='Action_ZoneBlock' annotated_start=45, effective_Action_ZoneBlock_start=55.
> - Action 'Action_BallCarry' range [68-74] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [78-128] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-103] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [105-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-68] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [45-59] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [61-89] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [94-104] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '3' starts at frame 136, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [136-180] for track '3' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [42-66] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-125] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-180] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-32] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-37] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-57] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-65] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [49-88] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-91] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-107] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-120] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-130] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-144] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-154] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [45-87] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [136-180] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [45-73] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [45-103] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-32] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-41] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [70-180] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-39] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' for track '14' starts at frame 42, but the player has no visible bounding box on this frame.
> - Action 'Action_BallSnap' range [42-44] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [55-65] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-119] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-139] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-180] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-82] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-101] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-112] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-125] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [103-110] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-143] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [147-159] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [104-105] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-119] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [125-135] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-157] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [160-164] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [169-180] for track '20' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [123-177] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-133] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [144-180] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [136-180] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [138-141] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [154-156] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-178] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-180] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-180] for track '26' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.