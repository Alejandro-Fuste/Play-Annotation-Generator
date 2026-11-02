# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_186`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_186/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 104 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '1' (LT) duration 107 frames exceeds threshold 90 frames [start=96, end=202].
> - Validation warning: Action 'Action_LeadBlock' for track '2' (TE2) duration 147 frames exceeds threshold 90 frames [start=96, end=242].
> - Validation warning: Action 'Action_ZoneBlock' for track '5' (LG) duration 104 frames exceeds threshold 90 frames [start=96, end=199].
> - Validation warning: Action 'Action_ZoneBlock' for track '9' (C) duration 118 frames exceeds threshold 90 frames [start=96, end=213].
> - Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [95–109], lower_priority='Action_ZoneBlock' annotated_start=96, effective_Action_ZoneBlock_start=110.
> - Validation warning: Action 'Action_ZoneBlock' for track '13' (RG) duration 116 frames exceeds threshold 90 frames [start=96, end=211].
> - Validation warning: Action 'Action_ZoneBlock' for track '17' (RT) duration 107 frames exceeds threshold 90 frames [start=96, end=202].
> - Action 'Action_None' range [95-132] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [135-138] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-143] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [96-202] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [96-192] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [224-236] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [243-246] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-329] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-213] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [222-316] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-188] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [194-195] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-204] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [96-199] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-153] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-114] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-180] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [182-259] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [263-274] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-293] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [121-213] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [110-213] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [95-225] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-276] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [278-329] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-99] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-135] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [137-184] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-189] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-192] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [96-211] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-64] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '14' starts at frame 95, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [95-95] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-124] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [126-205] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [207-208] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-213] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-218] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-234] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-192] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-254] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-267] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-290] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-295] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [305-309] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-103] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [96-199] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [201-202] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-180] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-278] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [303-329] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [121-205] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [212-216] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [220-234] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [236-241] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [259-265] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-135] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [140-206] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-129] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-132] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-172] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-201] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-167] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-178] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-178] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-187] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [208-216] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-289] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-294] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-309] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-224] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-228] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-327] for track '31' has 1 frames without a visible bounding box.
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
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.