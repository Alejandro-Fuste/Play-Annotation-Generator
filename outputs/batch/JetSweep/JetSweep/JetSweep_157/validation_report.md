# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_157`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_157/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 110 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 316: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Validation warning: Action 'Action_LeadBlock' for track '1' (RB) duration 106 frames exceeds threshold 90 frames [start=59, end=164].
> - Validation warning: Action 'Action_ZoneBlock' for track '9' (LT) duration 106 frames exceeds threshold 90 frames [start=59, end=164].
> - Validation warning: Action 'Action_ZoneBlock' for track '18' (RT) duration 106 frames exceeds threshold 90 frames [start=59, end=164].
> - Validation warning: Action 'Action_ZoneBlock' for track '20' (LG) duration 106 frames exceeds threshold 90 frames [start=59, end=164].
> - Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [57–71], lower_priority='Action_ZoneBlock' annotated_start=59, effective_Action_ZoneBlock_start=72.
> - Action 'Action_None' range [57-204] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [239-269] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [59-118] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [127-128] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-146] for track '2' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [149-156] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [160-204] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [57-177] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [180-191] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-204] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-216] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-191] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-91] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-101] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-115] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [118-120] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-205] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-156] for track '7' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [160-269] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-239] for track '8' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [243-244] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-258] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [59-86] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [91-120] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [124-127] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [130-133] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [135-139] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [165-269] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [57-161] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-208] for track '10' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [57-120] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-134] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-151] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [57-120] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-133] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [135-158] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [160-206] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [57-269] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [59-95] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [97-101] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [81-155] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [57-233] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-239] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [59-99] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [101-134] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [59-120] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [130-132] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [144-164] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-178] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [180-191] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-204] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [90-93] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-177] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-192] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [194-195] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-201] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-101] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-120] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-132] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-191] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [195-205] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-232] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-244] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [263-269] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-248] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-254] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-269] for track '28' has 1 frames without a visible bounding box.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
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