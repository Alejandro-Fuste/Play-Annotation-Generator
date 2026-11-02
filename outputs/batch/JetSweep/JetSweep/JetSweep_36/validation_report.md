# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_36`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_36/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 26 |
| Action Segments inferred | 92 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 74: Duplicate assignment for track ID '19' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Resolved action overlap for track '8' (C): higher_priority='Action_BallSnap' [84–90], lower_priority='Action_ZoneBlock' annotated_start=83, effective_Action_ZoneBlock_start=91.
> - Action 'Action_LeadBlock' range [83-140] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-211] for track '2' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [215-219] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-232] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [234-238] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [241-242] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-250] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [258-260] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-183] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [106-274] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [106-127] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-254] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-224] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [91-109] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-116] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-155] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [160-191] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-284] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [84-329] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-112] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-144] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [161-211] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [213-214] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-217] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-359] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [83-97] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [99-106] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [110-129] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-269] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-278] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [280-286] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [288-359] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-138] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-359] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-129] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-143] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [83-102] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-170] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-179] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-229] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-354] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [179-183] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-280] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-248] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-292] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [319-321] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [323-326] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [328-341] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [344-348] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [334-341] for track '27' has 1 frames without a visible bounding box.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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