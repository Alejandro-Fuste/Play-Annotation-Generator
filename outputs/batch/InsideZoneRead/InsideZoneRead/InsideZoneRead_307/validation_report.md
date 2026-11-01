# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_307`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_307/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 100 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 614: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [2–11], lower_priority='Action_ZoneBlock' annotated_start=5, effective_Action_ZoneBlock_start=12.
> - Action 'Action_None' range [2-180] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-172] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-180] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [2-59] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-93] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-101] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-108] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [111-132] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-142] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-145] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-156] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-180] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [2-53] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-28] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-33] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-67] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-74] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-86] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-118] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [120-125] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-180] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [2-65] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-166] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [5-25] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [31-38] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [40-43] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-74] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-171] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-22] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-33] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-58] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-164] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-40] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-154] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [5-63] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-80] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-84] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-163] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-32] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-57] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [60-78] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-180] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [40-180] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [5-7] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [19-60] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [63-65] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [68-72] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [2-7] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [9-11] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [12-19] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [58-77] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [78-180] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-51] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [54-72] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-78] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-98] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [100-179] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-153] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-161] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-36] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-72] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [76-167] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-172] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [93-95] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-102] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-157] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [107-108] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-133] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-180] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-174] for track '29' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.