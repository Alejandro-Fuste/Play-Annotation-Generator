# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_296`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_296/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 25 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 58 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 592: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [19–30], lower_priority='Action_ZoneBlock' annotated_start=22, effective_Action_ZoneBlock_start=31.
> - Action 'Action_None' range [19-180] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [19-110] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-116] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [19-60] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-180] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-180] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-74] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-113] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [19-118] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [120-174] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-180] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [22-67] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-180] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [68-180] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-180] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [31-47] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [50-76] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-60] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-69] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-110] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-38] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-53] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [62-180] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-128] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-133] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-174] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-180] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-138] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [131-132] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-174] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [177-180] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-180] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-180] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-180] for track '24' has 1 frames without a visible bounding box.
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