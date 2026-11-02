# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_194`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_194/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 91 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [52–61], lower_priority='Action_ZoneBlock' annotated_start=53, effective_Action_ZoneBlock_start=62.
> - Action 'Action_None' range [52-70] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' for track '1' starts at frame 53, but the player has no visible bounding box on this frame.
> - Action 'Action_ZoneBlock' range [53-56] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [67-90] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-30] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-46] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [52-78] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-96] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-212] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [101-115] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-122] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-63] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-72] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-101] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [53-58] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-65] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-101] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-18] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-26] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [33-70] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [71-85] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-154] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-159] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-206] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-5] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-35] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [45-48] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-99] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-5] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-55] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-127] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-8] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-61] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-76] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-112] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-183] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-51] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [52-60] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [63-76] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-106] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-123] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [125-134] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [137-141] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-48] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-58] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-96] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-62] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-74] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-77] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-206] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-222] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-76] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-142] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [86-104] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [123-151] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-96] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-155] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [158-159] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-215] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-161] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [125-130] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-146] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-231] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [171-172] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-176] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-211] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-226] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-230] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-239] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-234] for track '30' has 1 frames without a visible bounding box.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
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