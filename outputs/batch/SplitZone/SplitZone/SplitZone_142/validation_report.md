# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_142`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_142/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 79 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '5' (C) duration 156 frames exceeds threshold 90 frames [start=74, end=229].
> - Resolved action overlap for track '5' (C): higher_priority='Action_BallSnap' [71–78], lower_priority='Action_ZoneBlock' annotated_start=74, effective_Action_ZoneBlock_start=79.
> - Validation warning: Action 'Action_ZoneBlock' for track '6' (RT) duration 156 frames exceeds threshold 90 frames [start=74, end=229].
> - Validation warning: Action 'Action_ZoneBlock' for track '8' (RG) duration 156 frames exceeds threshold 90 frames [start=74, end=229].
> - Validation warning: Action 'Action_ZoneBlock' for track '10' (LT) duration 156 frames exceeds threshold 90 frames [start=74, end=229].
> - Action 'Action_None' range [71-220] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-249] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-117] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [94-137] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [79-160] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [168-229] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-240] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [79-152] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [160-161] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [74-110] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [74-93] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-123] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-269] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-202] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-217] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-220] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-143] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [172-173] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-176] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-269] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-36] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-245] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-70] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-222] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-89] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-114] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-104] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [107-167] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [105-230] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-130] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-136] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-127] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-138] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-225] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-244] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [263-265] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-264] for track '32' has 1 frames without a visible bounding box.
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