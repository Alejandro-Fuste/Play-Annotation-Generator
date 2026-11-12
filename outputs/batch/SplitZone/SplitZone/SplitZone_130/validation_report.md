# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_130`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_130/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 84 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '0' (LT) duration 99 frames exceeds threshold 90 frames [start=144, end=242].
> - Validation warning: Action 'Action_ZoneBlock' for track '7' (RG) duration 99 frames exceeds threshold 90 frames [start=144, end=242].
> - Validation warning: Action 'Action_ZoneBlock' for track '9' (RT) duration 99 frames exceeds threshold 90 frames [start=144, end=242].
> - Validation warning: Action 'Action_ZoneBlock' for track '12' (LG) duration 99 frames exceeds threshold 90 frames [start=144, end=242].
> - Validation warning: Action 'Action_ZoneBlock' for track '16' (C) duration 99 frames exceeds threshold 90 frames [start=144, end=242].
> - Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [141–150], lower_priority='Action_ZoneBlock' annotated_start=144, effective_Action_ZoneBlock_start=151.
> - Action 'Action_ZoneBlock' range [144-189] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-308] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-316] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [147-181] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [186-242] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [243-285] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [287-294] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [148-196] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-177] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-225] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-325] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [327-329] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-199] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-263] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [141-243] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [144-174] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-261] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-314] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [144-170] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [176-181] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [183-185] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [187-220] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-237] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [144-164] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-255] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-260] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-316] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-238] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-155] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-129] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-133] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-144] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-156] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-198] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [151-171] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [174-242] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [141-239] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-82] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [155-264] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-175] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-179] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-215] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [224-268] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-222] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [192-252] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [210-217] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-221] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-258] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-261] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-279] for track '27' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.