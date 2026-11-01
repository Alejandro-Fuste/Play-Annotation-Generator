# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_241`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_241/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 92 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 482: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [1–12], lower_priority='Action_ZoneBlock' annotated_start=4, effective_Action_ZoneBlock_start=13.
> - Action 'Action_None' range [1-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-186] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-50] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-210] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [1-62] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [64-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-140] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-175] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-77] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-148] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [150-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [42-179] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [183-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-90] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-186] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [189-192] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-199] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [4-65] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-33] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-51] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-59] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-68] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-85] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [4-22] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [41-43] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-210] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [13-40] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [44-50] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-138] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-38] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-59] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [67-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-67] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [99-106] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-152] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [154-167] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [171-210] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [96-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-110] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-122] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-128] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-164] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-179] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-199] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-181] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-186] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-193] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-200] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-201] for track '32' has 1 frames without a visible bounding box.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
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