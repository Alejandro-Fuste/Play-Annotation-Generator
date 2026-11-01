# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_331`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_331/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
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
> - Validation warning: Action 'Action_ZoneBlock' for track '15' (RT) duration 98 frames exceeds threshold 90 frames [start=27, end=124].
> - Validation warning: Action 'Action_ZoneBlock' for track '17' (LG) duration 98 frames exceeds threshold 90 frames [start=27, end=124].
> - Validation warning: Action 'Action_ZoneBlock' for track '18' (C) duration 98 frames exceeds threshold 90 frames [start=27, end=124].
> - Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [24–37], lower_priority='Action_ZoneBlock' annotated_start=27, effective_Action_ZoneBlock_start=38.
> - Validation warning: Action 'Action_ZoneBlock' for track '20' (LT) duration 98 frames exceeds threshold 90 frames [start=27, end=124].
> - Action 'Action_None' range [24-208] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [24-176] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-147] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-186] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [189-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-210] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [24-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-75] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-62] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-99] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-65] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-183] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [24-179] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [24-193] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [195-210] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [125-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [66-199] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [27-50] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-210] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [38-74] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [79-124] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [125-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [27-49] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [54-61] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [73-75] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [27-65] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [67-87] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [91-124] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [125-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-43] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [60-79] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-82] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-101] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-164] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-171] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-195] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-198] for track '28' has 1 frames without a visible bounding box.
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