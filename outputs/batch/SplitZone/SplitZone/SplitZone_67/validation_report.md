# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_67`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_67/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 107 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 136: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [136–152], lower_priority='Action_ZoneBlock' annotated_start=139, effective_Action_ZoneBlock_start=153.
> - Action 'Action_None' range [136-201] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [203-245] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [247-248] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-259] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-225] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-244] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [246-329] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [136-319] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [325-327] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [143-193] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [195-197] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [199-200] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-243] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-267] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [136-158] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-235] for track '7' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [223-259] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-267] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-273] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-276] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-287] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-290] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-241] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-264] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-270] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [223-242] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-264] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-217] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-233] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [237-239] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-255] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [259-329] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-241] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-267] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-317] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [323-329] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-230] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [165-169] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [171-243] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [254-256] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [262-271] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [274-287] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [153-190] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-258] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [139-218] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-244] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-270] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [275-278] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [283-288] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-319] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [151-222] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-328] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-205] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-241] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-247] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-267] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [269-271] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-214] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-219] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [259-310] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [264-269] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-276] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-285] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [287-329] for track '27' has 3 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
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