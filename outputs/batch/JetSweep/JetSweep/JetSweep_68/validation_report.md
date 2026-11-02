# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_68`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_68/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 82 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 138: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [44–65], lower_priority='Action_ZoneBlock' annotated_start=49, effective_Action_ZoneBlock_start=66.
> - Action 'Action_None' range [44-140] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-168] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-238] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [249-250] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [49-103] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-179] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-191] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-200] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-227] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-269] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [44-269] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-122] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [130-132] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-198] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-130] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-188] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-231] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-261] for track '13' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [263-269] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-269] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-78] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-253] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [44-65] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [66-71] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [49-105] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-269] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-142] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [148-166] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-85] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-93] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [98-100] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-105] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-150] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-156] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-147] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-269] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-269] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-244] for track '30' has 1 frames without a visible bounding box.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
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