# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_346`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_346/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 72 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 692: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '7' (C): higher_priority='Action_BallSnap' [18–34], lower_priority='Action_ZoneBlock' annotated_start=21, effective_Action_ZoneBlock_start=35.
> - Action 'Action_None' range [18-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-107] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-210] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [18-58] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-140] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-210] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [18-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [67-205] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-123] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-148] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-198] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-138] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-29] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [32-136] for track '10' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [138-140] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [21-79] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-210] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [18-49] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-55] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [18-43] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-46] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-82] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [86-89] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-94] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-97] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-116] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-210] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [18-39] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-60] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-170] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-210] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [64-147] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-84] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-210] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [94-189] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-203] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [205-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-137] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-142] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-210] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [165-197] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [166-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-205] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-201] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-210] for track '27' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.