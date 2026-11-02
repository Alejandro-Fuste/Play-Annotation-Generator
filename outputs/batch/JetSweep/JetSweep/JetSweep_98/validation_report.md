# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_98`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_98/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 72 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 198: Duplicate assignment for track ID '14' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [69–80], lower_priority='Action_ZoneBlock' annotated_start=70, effective_Action_ZoneBlock_start=81.
> - Action 'Action_BallCarry' range [94-200] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [205-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-108] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-190] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-140] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-180] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-184] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-206] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-150] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [70-95] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [98-101] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-170] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [81-105] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-75] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [117-160] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-165] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-176] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-188] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-192] for track '29' has 1 frames without a visible bounding box.
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