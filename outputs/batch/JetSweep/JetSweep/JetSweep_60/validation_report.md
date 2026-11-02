# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_60`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_60/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 102 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 122: Duplicate assignment for track ID '21' in grid. Overwriting previous assignment.
> - Row 122: Duplicate assignment for track ID '21' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [57–62], lower_priority='Action_ZoneBlock' annotated_start=62, effective_Action_ZoneBlock_start=63.
> - Action 'Action_None' range [57-306] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-75] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-329] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-249] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-329] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-167] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [169-236] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-243] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [251-260] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-269] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-209] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-118] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-140] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-143] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-243] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [254-257] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-260] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-303] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [57-243] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-281] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [287-290] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [298-303] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [63-67] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-201] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-199] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-140] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-289] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [62-98] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-329] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [81-272] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-215] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-251] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [57-62] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-125] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-287] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [57-78] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-82] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [62-77] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [79-85] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-266] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-81] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [84-243] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [245-248] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-255] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-266] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-293] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-81] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-287] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [289-308] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [187-190] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [232-245] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [300-306] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [319-325] for track '30' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
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