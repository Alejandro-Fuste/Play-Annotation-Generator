# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_159`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_159/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 84 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '7' (RT) duration 116 frames exceeds threshold 90 frames [start=98, end=213].
> - Validation warning: Action 'Action_ZoneBlock' for track '16' (RG) duration 116 frames exceeds threshold 90 frames [start=98, end=213].
> - Validation warning: Action 'Action_ZoneBlock' for track '18' (C) duration 116 frames exceeds threshold 90 frames [start=98, end=213].
> - Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [95–112], lower_priority='Action_ZoneBlock' annotated_start=98, effective_Action_ZoneBlock_start=113.
> - Action 'Action_SplitBlock' range [99-175] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-299] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-299] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-296] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [95-248] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-252] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-289] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-296] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [98-118] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-195] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-201] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-215] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-182] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [95-143] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-149] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-206] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-279] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [142-287] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [290-292] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-288] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [98-104] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-270] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-275] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-77] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-108] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-117] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-224] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-174] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [98-117] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [126-153] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [156-159] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [98-108] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-135] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-190] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-161] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-299] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-226] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-299] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-269] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-280] for track '26' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.