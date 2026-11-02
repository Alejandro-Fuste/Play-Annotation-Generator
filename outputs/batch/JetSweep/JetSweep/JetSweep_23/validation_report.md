# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_23`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_23/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 26 |
| Action Segments inferred | 112 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [75–86], lower_priority='Action_ZoneBlock' annotated_start=77, effective_Action_ZoneBlock_start=87.
> - Action 'Action_None' range [75-190] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-218] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [229-230] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-237] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-212] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-236] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [75-151] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [106-219] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [77-133] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-147] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-229] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-155] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-216] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-144] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-151] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [154-183] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [187-199] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-229] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-239] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-168] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [177-198] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-215] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [217-221] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [224-228] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [75-80] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [82-84] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' for track '14' starts at frame 87, but the player has no visible bounding box on this frame.
> - Action 'Action_ZoneBlock' range [87-87] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [89-91] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [111-144] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [77-98] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [109-123] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-69] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' for track '16' starts at frame 98, but the player has no visible bounding box on this frame.
> - Action 'Action_BlockSecondLevel' range [98-98] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [104-144] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [75-91] for track '17' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [110-229] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [234-237] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-76] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [77-102] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [106-107] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [109-123] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-148] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-69] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-72] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-87] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [89-153] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [160-208] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [211-226] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-236] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-66] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [75-91] for track '20' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [93-98] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-105] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-32] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-56] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-62] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [86-87] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-91] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-98] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-105] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-122] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-147] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-112] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-146] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [151-183] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-190] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-198] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-226] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-229] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-239] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-181] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [209-212] for track '26' has 1 frames without a visible bounding box.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.