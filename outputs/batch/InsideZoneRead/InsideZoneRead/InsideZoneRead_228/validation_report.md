# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_228`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_228/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 25 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 74 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [85–101], lower_priority='Action_ZoneBlock' annotated_start=88, effective_Action_ZoneBlock_start=102.
> - Action 'Action_PreSnap' range [7-84] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-207] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-87] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-167] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-15] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-26] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-84] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-177] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [181-186] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-126] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-130] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-210] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-41] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [85-175] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [178-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-35] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [123-128] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [170-172] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [190-205] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-18] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [116-122] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-135] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-207] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-38] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [85-135] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-46] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [85-95] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [99-100] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [111-115] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [120-127] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [138-143] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [154-157] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-162] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [165-202] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-38] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-84] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-152] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-156] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-170] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-173] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-180] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-184] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [88-117] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [120-141] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-163] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [88-103] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [42-54] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-73] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-76] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [88-100] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-210] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [143-210] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [157-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-172] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-181] for track '24' has 1 frames without a visible bounding box.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
> - Player track '7' has undefined position. Will map to Position_Unknown.
> - Player track '7' has undefined team_side. Will map to Team_Unknown.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
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