# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_192`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_192/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 101 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '1' (RG) duration 106 frames exceeds threshold 90 frames [start=108, end=213].
> - Validation warning: Action 'Action_ZoneBlock' for track '3' (LG) duration 106 frames exceeds threshold 90 frames [start=108, end=213].
> - Validation warning: Action 'Action_ZoneBlock' for track '8' (RT) duration 106 frames exceeds threshold 90 frames [start=108, end=213].
> - Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [105–119], lower_priority='Action_ZoneBlock' annotated_start=108, effective_Action_ZoneBlock_start=120.
> - Action 'Action_None' range [105-134] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [139-154] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-174] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-182] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-197] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-215] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [108-123] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-112] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-175] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-203] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [108-117] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [122-126] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [175-186] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [214-224] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [128-137] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [138-150] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [152-153] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [174-182] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [195-213] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-122] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [124-186] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [188-205] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [208-244] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-252] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [138-145] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [175-176] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [178-182] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [195-199] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [208-230] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [232-260] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [265-268] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [108-111] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [168-179] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [181-191] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-269] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [105-119] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-166] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [170-171] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [105-112] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [144-145] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [155-156] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-126] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [131-166] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [170-171] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-51] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-90] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [116-132] for track '12' has 4 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [152-153] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [155-203] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [105-269] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [122-168] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [178-183] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-154] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-159] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-168] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-185] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-269] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-182] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-196] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-201] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-205] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-229] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-233] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-239] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-243] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-252] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-235] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-244] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-207] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [209-251] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-269] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-244] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-269] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-260] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [267-268] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-226] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-269] for track '26' has 2 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.