# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_27`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_27/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 81 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 56: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [64–78], lower_priority='Action_ZoneBlock' annotated_start=66, effective_Action_ZoneBlock_start=79.
> - Action 'Action_None' range [64-94] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-91] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-98] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [106-190] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [64-159] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-156] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-201] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-226] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-183] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-173] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [64-171] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [173-216] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [64-146] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-202] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [129-176] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [179-239] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [66-70] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-239] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [66-79] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-140] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-239] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [95-189] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [191-239] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-133] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-123] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-137] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-140] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-138] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-151] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [153-164] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-183] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-239] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-189] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-197] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-209] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-218] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-232] for track '31' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.