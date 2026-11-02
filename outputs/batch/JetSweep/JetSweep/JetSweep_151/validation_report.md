# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_151`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_151/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 73 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [46–59], lower_priority='Action_ZoneBlock' annotated_start=48, effective_Action_ZoneBlock_start=60.
> - Action 'Action_BallCarry' range [69-217] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [219-221] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-176] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-194] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-203] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-209] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-186] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [46-170] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-173] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-239] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [48-78] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-164] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [60-67] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [70-71] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-189] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-186] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-227] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-81] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-124] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-131] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [133-150] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [154-159] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-171] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-85] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-95] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-159] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-191] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-210] for track '28' has 1 frames without a visible bounding box.
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