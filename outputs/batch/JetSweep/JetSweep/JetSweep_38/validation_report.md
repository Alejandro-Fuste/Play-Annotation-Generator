# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_38`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_38/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 28 |
| Action Segments inferred | 78 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 78: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [81–90], lower_priority='Action_ZoneBlock' annotated_start=82, effective_Action_ZoneBlock_start=91.
> - Action 'Action_None' range [81-221] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-205] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-238] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-207] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-155] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [81-225] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-213] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-224] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-146] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-156] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-230] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-239] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-185] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-195] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [163-234] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-222] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [91-93] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [95-110] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [82-109] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-230] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-239] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-239] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-114] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-97] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-141] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-147] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [149-159] for track '23' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [163-165] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-215] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-230] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-227] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-239] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-237] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-213] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-219] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-239] for track '28' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.