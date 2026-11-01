# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_111`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_111/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 79 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 224: Duplicate assignment for track ID '14' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [38–52], lower_priority='Action_ZoneBlock' annotated_start=41, effective_Action_ZoneBlock_start=53.
> - Action 'Action_None' range [38-98] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-186] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-198] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-206] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-76] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-239] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [38-107] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-57] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-175] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-221] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-177] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-239] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [41-59] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-75] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-95] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-74] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-128] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-219] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [38-206] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [38-180] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-208] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-214] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [41-50] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [64-65] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [69-71] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [53-106] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-70] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-112] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-183] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-93] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-149] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [122-166] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-193] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-196] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-237] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [215-216] for track '29' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.