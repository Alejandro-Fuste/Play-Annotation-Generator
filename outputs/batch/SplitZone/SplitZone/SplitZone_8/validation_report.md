# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_8`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_8/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 28 |
| Ball Tracks | 1 |
| CSV events parsed | 19 |
| Action Segments inferred | 76 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [172–188], lower_priority='Action_ZoneBlock' annotated_start=175, effective_Action_ZoneBlock_start=189.
> - Action 'Action_PreSnap' range [0-80] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-236] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-243] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-36] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-39] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-264] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [196-216] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '2' starts at frame 217, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [217-245] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [172-270] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-219] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [263-290] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-71] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-222] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-235] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [243-324] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-216] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [217-245] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [247-338] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [343-359] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [175-190] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [208-209] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [222-240] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-321] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [175-191] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [206-246] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [172-275] for track '10' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [284-287] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [263-296] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-68] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [189-207] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [221-228] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [247-262] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-276] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-174] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [175-179] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [233-262] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-318] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-201] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-263] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [225-240] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-248] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-256] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-320] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-243] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-344] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [346-359] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-327] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-331] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [293-344] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [320-323] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [333-340] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [334-337] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [351-352] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [354-359] for track '28' has 1 frames without a visible bounding box.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.