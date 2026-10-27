# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_256`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_256/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 120 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Overlapping action conflict at frame 133 for track '10': 'Action_DownBlock' vs 'Action_PullLeadBlock'. Overriding with 'Action_PullLeadBlock'.
> - Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [131–145], lower_priority='Action_PullLeadBlock' annotated_start=133, effective_Action_PullLeadBlock_start=146.
> - Action 'Action_None' range [131-188] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-239] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-198] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-218] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [232-238] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-302] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [133-149] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-317] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-82] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-201] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-240] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-264] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [133-156] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [158-159] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [161-163] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [166-198] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-245] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [133-165] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-213] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [218-272] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [280-281] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-287] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [290-291] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [311-327] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-69] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PlaySideFakeStep' range [140-173] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [178-209] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-191] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-89] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-130] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [146-151] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [159-175] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-256] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-297] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [301-355] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-185] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-220] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-73] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-162] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-169] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-209] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-255] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [281-340] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [343-350] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-70] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '13' starts at frame 131, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [131-131] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-162] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-34] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-38] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-70] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-85] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-94] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-141] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-169] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-226] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-230] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-260] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-278] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-313] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-22] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-154] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-244] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-256] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-165] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-224] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [226-253] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-332] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [204-223] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-289] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-266] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-346] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-241] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-305] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-313] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [317-331] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [228-359] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-346] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [235-320] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-276] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-281] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-280] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [290-316] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [313-316] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [338-358] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [344-345] for track '30' has 1 frames without a visible bounding box.
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